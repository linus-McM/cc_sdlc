"""Graph-selected Repomix context packs: one commit-pinned snapshot per stage that its Workflow agents share.

Seeds come from the stage artifact, grow one hop through graphify-out/graph.json, pass a frozen secret
exclude list, Bandit and Repomix's own secret check, and land in graphify-out/packs/ (never committed).
`require` is the plan and test gate: a pack built at HEAD, and at test one covering every changed file.
"""

from __future__ import annotations

import fnmatch
import hashlib
import html
import json
import os
import re
import shutil
from collections import defaultdict
from pathlib import Path

from . import artifacts as a
from . import deploy, knowledge
from . import project as p
from .build import is_sdlc_owned, planned_files
from .project import StepSkipped, fail, ran

GATED = frozenset({"plan", "test"})  # stages whose exit needs a pack at HEAD; a code constant, never config
REPOMIX_INSTALL = ["npm", "i", "-g", "repomix"]
INSTALL_CMD = " ".join(REPOMIX_INSTALL)
PACKS_OFF = {"ok": True, "skipped": "packs disabled (SDLC_PACKS=off)"}
BACKTICK = re.compile(r"`([^`\s]+)`")
LINE_SUFFIX = re.compile(r":\d+(-\d+)?$")


def tracked(root: Path) -> list[str]:
    return p.git(root, "ls-files").splitlines()


def resolve(files: list[str], tokens: list[str]) -> tuple[list[str], list[str]]:
    """Tracked `files` a token names (a file, a directory or a glob); tokens naming nothing are returned, never guessed."""
    known, found, unresolved = set(files), set(), []
    for token in tokens:
        name = LINE_SUFFIX.sub("", token).rstrip("/")
        glob = any(c in name for c in "*?[")
        hits = [name] if name in known else [f for f in files if f.startswith(name + "/") or (glob and fnmatch.fnmatch(f, name))]
        found.update(hits)
        if not hits:
            unresolved.append(token)
    return sorted(found), unresolved


def section_tokens(path: Path, heading: str) -> list[str]:
    return BACKTICK.findall(a.sections(path.read_text()).get(heading, "")) if path.exists() else []


def changed_since(root: Path, spec: str) -> list[str]:
    """Committed text files changed in `spec` (a git range); deleted, binary (numstat `-`) and sdlc-owned paths left out."""
    rows = [line.split("\t", 2) for line in p.git(root, "diff", "--numstat", "--diff-filter=d", spec).splitlines() if line]
    return [path for added, _, path in rows if added != "-" and not is_sdlc_owned(path)]


def plan_seeds(root: Path, feature: Path) -> list[str]:
    return section_tokens(feature / "intent.md", "Affected users and systems")


def maintain_seeds(root: Path, feature: Path) -> list[str]:
    shas = [d["sha"] for d in deploy.production(feature) if d.get("sha")]
    return changed_since(root, f"{shas[-1]}..HEAD") if shas else []


# stage -> seed tokens from its artifact; Deploy builds no pack (the PR body's knowledge diff is enough there)
SEEDS = {
    "plan": plan_seeds,
    "design": lambda r, f: plan_seeds(r, f) + section_tokens(f / "spec.md", "Design"),
    "build": lambda r, f: planned_files(f),
    "test": lambda r, f: review_changes(r),
    "maintain": maintain_seeds,
}


def seeds(root: Path, feature: Path, stage: str, files: list[str] | None = None) -> tuple[list[str], list[str]]:
    return resolve(tracked(root) if files is None else files, SEEDS[stage](root, feature))


# secret-bearing paths that never reach Repomix, whatever the graph selects; frozen here, no config key shrinks it.
# A pattern without `/` matches the file name, one with `/` the whole path (`/**` = everything below).
EXCLUDE = (
    ".env*",
    ".claude/settings.local.json",
    *("*.pem", "*.key", "*.p12", "*.pfx", "*.keystore", "*.jks"),
    *("id_rsa*", "id_dsa*", "id_ecdsa*", "id_ed25519*"),
    *(".netrc", ".npmrc", ".pypirc", "*credentials*"),
    "graphify-out/**",
    ".git/**",
)


def secret_rule(path: str) -> str | None:
    for rule in EXCLUDE:
        if path.startswith(rule[:-2]) if rule.endswith("/**") else fnmatch.fnmatch(path if "/" in rule else Path(path).name, rule):
            return rule
    return None


def git_ignored(root: Path, files: list[str]) -> set[str]:
    """Files git would ignore, tracked or not (`--no-index`)."""
    return set(p.run_cmd(root, ["git", "check-ignore", "--no-index", "--stdin"], input="\n".join(files)).stdout.splitlines()) if files else set()


def admit(root: Path, files: list[str], known: set[str] | None = None) -> tuple[list[str], list[dict]]:
    """Split the selection into files Repomix may read and exclusions with the rule that matched; `known` = tracked files."""
    known = set(tracked(root)) if known is None else known
    ignored, base = git_ignored(root, files), root.resolve()
    admitted, excluded = [], []
    for path in sorted(files):
        full = root / path
        rule = (
            secret_rule(path)
            or ("untracked" if path not in known else None)
            or ("symlink" if full.is_symlink() else None)
            or ("outside root" if not full.resolve().is_relative_to(base) else None)
            or ("git-ignored" if path in ignored else None)
        )
        if rule:
            excluded.append({"path": path, "rule": rule})
        else:
            admitted.append(path)
    return admitted, excluded


def expand(graph: dict, seeds: list[str], hops: int) -> dict[str, str]:
    """{path: seed|caller|callee|community}: files `hops` `calls` links from a seed, plus each seed's community."""
    files: dict[str, str] = dict.fromkeys(seeds, "seed")
    node_file, by_file, community_files = {}, defaultdict(set), defaultdict(set)
    for node in graph["nodes"]:
        if path := node.get("source_file"):
            node_file[node["id"]] = path
            by_file[path].add(node["id"])
            community_files[node.get("community")].add(path)
    callees, callers = defaultdict(set), defaultdict(set)
    for link in graph["links"]:
        if link.get("relation") == "calls":
            callees[link["source"]].add(link["target"])
            callers[link["target"]].add(link["source"])
    frontier = {n for s in seeds for n in by_file[s]}
    for _ in range(hops):
        reached = {t: "callee" for n in frontier for t in callees[n]} | {s: "caller" for n in frontier for s in callers[n]}
        frontier = set()
        for node_id, reason in reached.items():
            if (path := node_file.get(node_id)) and path not in files:
                files[path] = reason
                frontier.add(node_id)
    seed_communities = {n.get("community") for n in graph["nodes"] if n.get("source_file") in seeds} - {None}
    for community in seed_communities:
        for path in sorted(community_files[community]):
            files.setdefault(path, "community")
    return files


# --- preconditions: the layer is on, the stage builds packs, Repomix exists, the graph describes HEAD ---


def switched_off() -> bool:
    """SDLC_PACKS=off: packs and their gates skip visibly (tests default to it; the `packs` fixture turns them on)."""
    return os.environ.get("SDLC_PACKS") == "off"


def off(root: Path) -> dict | None:
    """The visible skip verdict when packs do not apply: layer off (SDLC_KNOWLEDGE / [knowledge] enabled) or SDLC_PACKS=off.
    Read at call time: packs is imported while knowledge may still be initialising."""
    if not knowledge.enabled(root):
        return dict(knowledge.SKIPPED)
    return dict(PACKS_OFF) if switched_off() else None


def repomix_on_path() -> bool:
    return shutil.which("repomix") is not None


def missing_repomix() -> str | None:
    return None if repomix_on_path() else f"repomix not on PATH; install it with `{INSTALL_CMD}` (or `sdlc knowledge bootstrap`)"


# the knowledge bootstrap's `repomix` step (knowledge.STEPS calls these at run time)
def repomix_present(root: Path, conf: dict) -> bool:
    if switched_off():
        raise StepSkipped(PACKS_OFF["skipped"])
    return repomix_on_path()


def install_repomix(root: Path, conf: dict) -> str:
    return ran(root, REPOMIX_INSTALL, repomix_on_path)


def update_repomix(root: Path, conf: dict) -> str:
    return ran(root, ["npm", "update", "-g", "repomix"], repomix_on_path)


def exemptions(root: Path, conf: dict) -> list[str]:
    """Paths whose change never makes the graph stale: [knowledge] ignore, the SDLC home and [checkpoint] paths."""
    return [*conf["knowledge"]["ignore"], p.rel(root, p.home(root)) + "/", *conf["checkpoint"]["paths"]]


def exempt(path: str, patterns: list[str]) -> bool:
    return is_sdlc_owned(path) or any(fnmatch.fnmatch(path, pat + "*") if pat.endswith("/") else path == pat for pat in patterns)


def fresh_graph(root: Path, conf: dict) -> dict:
    """The graph, provided it names a commit and no non-exempt file changed since; graphify-out/ must be ignored."""
    ignore = root / ".graphifyignore"
    if not ignore.exists() or not {"graphify-out", "graphify-out/", "graphify-out/**"} & {line.strip() for line in ignore.read_text().splitlines()}:
        fail(".graphifyignore must list graphify-out/ so a pack never becomes graph input; run `sdlc knowledge bootstrap`")
    graph = knowledge.load_graph(root)
    if not (built := graph.get("built_at_commit")):
        fail("graphify-out/graph.json missing or without built_at_commit; run `sdlc knowledge bootstrap`")
    patterns = exemptions(root, conf)
    if stale := [f for f in p.git(root, "diff", "--name-only", built, "HEAD").splitlines() if f and not exempt(f, patterns)]:
        fail("graph.json is behind HEAD for files a pack would select; run `graphify update .` (or wait for the post-commit rebuild)", stale=stale)
    return graph


def build(root: Path, slug: str | None, stage: str | None, max_tokens: int | None = None) -> dict:
    """Select, guard and pack the files a stage's agents need; see the module docstring."""
    if skipped := off(root):
        return skipped
    if stage not in SEEDS:
        fail(f"no context pack for stage {stage!r}: packs are built for {', '.join(SEEDS)}; Deploy builds no pack (the PR body's knowledge diff is enough there)")
    feature = p.feature(root, slug)
    if reason := missing_repomix():
        if stage in GATED:
            fail(reason)
        return {"ok": True, "skipped": reason}
    conf = p.config(root)
    files, seed_files, unresolved, excluded = select(root, feature, stage, fresh_graph(root, conf), conf["knowledge"]["pack_hops"])
    admitted = list(files)
    budget = max_tokens if max_tokens is not None else conf["knowledge"]["pack_max_tokens"]
    version = p.run_cmd(root, ["repomix", "--version"]).stdout.strip()
    head = p.head_commit(root)
    key = hashlib.sha256(json.dumps([head, sorted(files), budget, version]).encode()).hexdigest()
    out = store(root) / feature.name
    manifest_path = out / f"{stage}-{key[:12]}.json"
    if (cached := p.read_json(manifest_path)) and Path(cached["path"]).exists():
        return {"ok": True, **verdict_of(cached), "reused": True}
    run_bandit(root, [f for f in admitted if f.endswith(".py")])
    return write_pack(root, out, manifest_path, {"slug": feature.name, "stage": stage, "head": head, "key": key, "repomix_version": version}, files, seed_files, unresolved, excluded, budget)


def select(root: Path, feature: Path, stage: str, graph: dict, hops: int) -> tuple[dict, list[str], list[str], list[dict]]:
    """({admitted path: reason}, seeds, unresolved tokens, exclusions); refuses when an admitted file is dirty."""
    known = tracked(root)
    seed_files, unresolved = seeds(root, feature, stage, known)
    selected = expand(graph, seed_files, hops)
    admitted, excluded = admit(root, list(selected), set(known))
    if dirty := p.changed_files(root, *admitted):
        fail("packed files have uncommitted changes; a pack is pinned to HEAD, so commit or stash them first", dirty=dirty)
    return {f: selected[f] for f in admitted}, seed_files, unresolved, excluded


def write_pack(root: Path, out: Path, manifest_path: Path, identity: dict, files: dict, seed_files: list[str], unresolved: list[str], excluded: list[dict], budget: int) -> dict:
    """Walk the ladder into a temp file, then write the manifest and move the pack into place; older pairs pruned."""
    stage, key = identity["stage"], identity["key"]
    out.mkdir(parents=True, exist_ok=True)
    tmp = out / f".{stage}-{key[:12]}.tmp.xml"
    try:
        packed, steps = ladder(root, list(files), set(seed_files), budget, tmp)
        tokens = steps[-1]["tokens"]
        pack_path = manifest_path.with_suffix(".xml")
        manifest = {
            **identity,
            "path": str(pack_path),
            "manifest": str(manifest_path),
            "files": {f: files[f] for f in packed},
            "seeds": seed_files,
            "unresolved": unresolved,
            "excluded": excluded,
            "tokens": tokens,
            "steps": steps,
            "over_budget": bool(budget) and tokens > budget,
            "budget": budget,
            "built": p.now_iso(),
        }
        p.write_json(manifest_path, manifest)
        tmp.replace(pack_path)
    finally:
        tmp.unlink(missing_ok=True)
    prune(out, stage, keep=key[:12])
    return {"ok": True, **verdict_of(manifest), "reused": False}


VERDICT_KEYS = ("path", "manifest", "files", "seeds", "unresolved", "excluded", "tokens", "steps", "over_budget")


def verdict_of(manifest: dict) -> dict:
    verdict = {k: manifest[k] for k in VERDICT_KEYS}
    if manifest["over_budget"]:
        verdict["reason"] = f"over budget: seeds only still needs {manifest['tokens']} tokens (budget {manifest['budget']}); the pack is written anyway"
    return verdict


# (rung, --compress, seeds only): tried in order until the pack fits the budget; with no budget only `full` runs
LADDER = (("full", False, False), ("compress", True, False), ("seeds", True, True))


def ladder(root: Path, admitted: list[str], seed_set: set[str], budget: int, out: Path) -> tuple[list[str], list[dict]]:
    """Step down the ladder, recording every rung tried with its tokens and dropped files; seeds are never dropped."""
    steps: list[dict] = []
    for rung, compress, seeds_only in LADDER:
        files = [f for f in admitted if f in seed_set] if seeds_only else admitted
        tokens = run_repomix(root, files, out, compress)
        steps.append({"rung": rung, "tokens": tokens, "dropped": sorted(set(admitted) - set(files))})
        if not budget or tokens <= budget:
            break
    return files, steps


def packs_dir(root: Path) -> Path:
    return knowledge.graph_path(root).parent / "packs"


def store(root: Path) -> Path:
    """packs_dir, created with a `*` .gitignore on first use so nothing in it is ever committed."""
    base = packs_dir(root)
    base.mkdir(parents=True, exist_ok=True)
    if not (ignore := base / ".gitignore").exists():
        ignore.write_text("*\n")
    return base


def prune(out: Path, stage: str, keep: str) -> None:
    for old in out.glob(f"{stage}-*"):
        if not old.name.startswith(f"{stage}-{keep}."):
            old.unlink()


# --- Bandit: hardcoded-password tests over the Python files, before Repomix; fails closed ---

BANDIT = "bandit==1.9.4"  # pinned so a release cannot change what refuses a pack; bump deliberately
BANDIT_TESTS = "B105,B106,B107"


def run_bandit(root: Path, py_files: list[str]) -> None:
    if not py_files:
        return
    argv = [knowledge.find_uv() or "uv", "tool", "run", "--from", BANDIT, "bandit", "-q", "-f", "json", "-t", BANDIT_TESTS, *py_files]
    result = p.run_cmd(root, argv)
    if result.returncode not in (0, 1):
        fail(f"bandit exited {result.returncode}; no pack written (the scan fails closed)", stderr=result.stderr.strip()[-300:])
    try:
        results = json.loads(result.stdout)["results"]
    except (json.JSONDecodeError, KeyError, TypeError):
        fail("bandit printed no readable JSON; no pack written (the scan fails closed)")
    if findings := [f"{os.path.normpath(r['filename'])}:{r['line_number']} {r['test_id']}" for r in results]:  # bandit prints ./path
        fail("bandit found hardcoded passwords; no pack written. Move the secret out of the source", findings=findings)


# --- Repomix, and the scanner that refuses anything but exactly the requested files ---

CONFIG = p.TEMPLATES / "knowledge" / "repomix.config.json"
SUSPICIOUS = re.compile(r"suspicious file\(s\) detected")
LISTED = re.compile(r"^\s*\d+\.\s+(\S.*?)\s*$")
TOTAL = re.compile(r"Total Tokens:\s*([\d,]+)")
PACKED = re.compile(r'<file path="([^"]+)">')


def run_repomix(root: Path, files: list[str], out: Path, compress: bool) -> int:
    """Pack `files` into `out` with the plugin's config (secret check forced on); the token count, or a refusal."""
    argv = ["repomix", "--stdin", "--config", str(CONFIG), "--style", "xml", "--output", str(out), *(["--compress"] if compress else [])]
    result = p.run_cmd(root, argv, input="\n".join(files) + "\n", env={"NO_COLOR": "1"})
    if result.returncode != 0:
        fail(f"repomix exited {result.returncode}; no pack written", stderr=result.stderr.strip()[-300:])
    scan_output(result.stdout, files, out.read_text() if out.exists() else "")
    match = TOTAL.search(result.stdout)
    return int(match.group(1).replace(",", "")) if match else 0


def suspicious(stdout: str) -> list[str]:
    """Files Repomix's secret check flagged, read from its Security Check block only (the top-files list looks alike)."""
    lines = stdout.splitlines()
    start = next((i for i, line in enumerate(lines) if SUSPICIOUS.search(line)), None)
    found = []
    for line in lines[start + 1 :] if start is not None else []:
        if not line.strip():
            break
        if match := LISTED.match(line):
            found.append(match.group(1))
    return found


def scan_output(stdout: str, requested: list[str], xml: str) -> None:
    """Refuse unless the output holds exactly the requested files; verdicts name paths, never file contents."""
    if flagged := suspicious(stdout):
        fail("repomix's secret check flagged files; no pack written. Remove the secret or keep the file out of the stage artifact", flagged=flagged)
    packed = {html.unescape(path) for path in PACKED.findall(xml)}  # parsable style escapes contents, so only headers match
    if missing := sorted(set(requested) - packed):
        fail("repomix left requested files out of the pack; no pack written", missing=missing)
    if extra := sorted(packed - set(requested)):
        fail("repomix packed files that were not requested; no pack written", extra=extra)


# --- the gate: plan accept and test review need this stage's pack, built at HEAD ---


def latest(root: Path, slug: str, stage: str) -> dict | None:
    """The newest manifest for a slug and stage whose pack file still exists."""
    manifests = sorted((packs_dir(root) / slug).glob(f"{stage}-*.json"), key=lambda f: f.stat().st_mtime)
    newest = p.read_json(manifests[-1]) if manifests else None
    return newest if newest and Path(newest["path"]).exists() else None


def require(root: Path, feature: Path, stage: str) -> dict:
    """The gate for a stage in GATED: ok (visibly skipped) when packs are off; otherwise refuse without a pack at HEAD."""
    if skipped := off(root):
        return skipped
    if reason := missing_repomix():
        fail(reason)
    command = f"sdlc knowledge pack {stage} --slug {feature.name}"
    manifest = latest(root, feature.name, stage)
    if not manifest:
        fail(f"no {stage} context pack for {feature.name}; run `{command}` first", next=command)
    if manifest["head"] != (head := p.head_commit(root)):
        fail(f"the {stage} context pack was built at {manifest['head'][:12]}, not HEAD {head[:12]}; run `{command}`", next=command)
    if stage == "test":
        covered(root, manifest, command)
    return {"ok": True, "path": manifest["path"], "head": manifest["head"], "files": len(manifest["files"])}


def review_changes(root: Path) -> list[str]:
    """Files the test pack seeds from and must cover: the branch diff against `[knowledge] pack_base`."""
    return changed_since(root, f"{p.config(root)['knowledge']['pack_base']}...HEAD")


def covered(root: Path, manifest: dict, command: str) -> None:
    changed = review_changes(root)
    if secrets := [{"path": f, "rule": rule} for f in changed if (rule := secret_rule(f))]:
        fail("the branch commits files a secret rule excludes; remove them from history before review", secrets=secrets)
    if missing := sorted(set(changed) - set(manifest["files"])):
        fail(f"the test context pack does not cover every changed file; run `{command}`", missing=missing, next=command)
