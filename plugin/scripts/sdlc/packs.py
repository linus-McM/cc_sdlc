"""Graph-selected Repomix context packs: one commit-pinned snapshot per stage that its Workflow agents share.

Seeds come from the stage artifact, grow one hop through graphify-out/graph.json, pass a frozen secret
exclude list, Bandit and Repomix's own secret check, and land in graphify-out/packs/ (never committed).
`require` is the plan and test gate: a pack built at HEAD, and at test one covering every changed file.
"""

from __future__ import annotations

import fnmatch
import hashlib
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
from .project import fail

GATED = frozenset({"plan", "test"})  # stages whose exit needs a pack at HEAD; a code constant, never config
INSTALL_CMD = "npm i -g repomix"
PACKS_OFF = {"ok": True, "skipped": "packs disabled (SDLC_PACKS=off)"}
BACKTICK = re.compile(r"`([^`\s]+)`")
LINE_SUFFIX = re.compile(r":\d+(-\d+)?$")


def tracked(root: Path) -> list[str]:
    return p.git(root, "ls-files").splitlines()


def resolve(root: Path, tokens: list[str]) -> tuple[list[str], list[str]]:
    """Tracked files a token names (a file, a directory or a glob); tokens naming nothing are returned, never guessed."""
    files, found, unresolved = tracked(root), set(), []
    for token in tokens:
        name = LINE_SUFFIX.sub("", token).rstrip("/")
        glob = any(c in name for c in "*?[")
        hits = [f for f in files if f == name or f.startswith(name + "/") or (glob and fnmatch.fnmatch(f, name))]
        found.update(hits)
        if not hits:
            unresolved.append(token)
    return sorted(found), unresolved


def section_tokens(path: Path, heading: str) -> list[str]:
    return BACKTICK.findall(a.sections(path.read_text()).get(heading, "")) if path.exists() else []


def changed_since(root: Path, spec: str) -> list[str]:
    """Committed files changed in `spec` (a git range), without deleted and sdlc-owned paths."""
    return [f for f in p.git(root, "diff", "--name-only", "--diff-filter=d", spec).splitlines() if f and not is_sdlc_owned(f)]


def last_production(feature: Path) -> str | None:
    shas = [d["sha"] for d in deploy.state(feature)["deployments"] if d["env"] == "production"]
    return shas[-1] if shas else None


def plan_seeds(root: Path, feature: Path) -> list[str]:
    return section_tokens(feature / "intent.md", "Affected users and systems")


def maintain_seeds(root: Path, feature: Path) -> list[str]:
    sha = last_production(feature)
    return changed_since(root, f"{sha}..HEAD") if sha else []


# stage -> seed tokens from its artifact; Deploy builds no pack (the PR body's knowledge diff is enough there)
SEEDS = {
    "plan": plan_seeds,
    "design": lambda r, f: plan_seeds(r, f) + section_tokens(f / "spec.md", "Design"),
    "build": lambda r, f: planned_files(f),
    "test": lambda r, f: changed_since(r, f"{p.config(r)['knowledge']['pack_base']}...HEAD"),
    "maintain": maintain_seeds,
}


def seeds(root: Path, feature: Path, stage: str) -> tuple[list[str], list[str]]:
    return resolve(root, SEEDS[stage](root, feature))


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


def admit(root: Path, files: list[str]) -> tuple[list[str], list[dict]]:
    """Split the selection into files Repomix may read and exclusions with the rule that matched."""
    known, ignored, base = set(tracked(root)), git_ignored(root, files), root.resolve()
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
    node_file = {n["id"]: n.get("source_file") for n in graph["nodes"] if n.get("source_file")}
    by_file = defaultdict(set)
    for node_id, path in node_file.items():
        by_file[path].add(node_id)
    calls = [(link["source"], link["target"]) for link in graph["links"] if link.get("relation") == "calls"]
    frontier = {n for s in seeds for n in by_file[s]}
    for _ in range(hops):
        reached = {target: "callee" for source, target in calls if source in frontier} | {source: "caller" for source, target in calls if target in frontier}
        frontier = set()
        for node_id, reason in reached.items():
            if (path := node_file.get(node_id)) and path not in files:
                files[path] = reason
                frontier.add(node_id)
    communities = {n.get("community") for n in graph["nodes"] if n.get("source_file") in seeds} - {None}
    for node in graph["nodes"]:
        if node.get("community") in communities and (path := node.get("source_file")):
            files.setdefault(path, "community")
    return files


# --- preconditions: the layer is on, the stage builds packs, Repomix exists, the graph describes HEAD ---


def off(root: Path) -> dict | None:
    """The visible skip verdict when packs do not apply: layer off (SDLC_KNOWLEDGE / [knowledge] enabled) or SDLC_PACKS=off.
    Read at call time: packs is imported while knowledge may still be initialising."""
    if not knowledge.enabled(root):
        return dict(knowledge.SKIPPED)
    return dict(PACKS_OFF) if os.environ.get("SDLC_PACKS") == "off" else None


def missing_repomix() -> str | None:
    return None if shutil.which("repomix") else f"repomix not on PATH; install it with `{INSTALL_CMD}` (or `sdlc knowledge bootstrap`)"


def exempt(root: Path, path: str, conf: dict) -> bool:
    """Paths whose change never makes the graph stale: the SDLC home, [knowledge] ignore, [checkpoint] paths, sdlc-owned files."""
    patterns = [*conf["knowledge"]["ignore"], p.rel(root, p.home(root)) + "/", *conf["checkpoint"]["paths"]]
    return is_sdlc_owned(path) or any(fnmatch.fnmatch(path, pat + "*") if pat.endswith("/") else path == pat for pat in patterns)


def fresh_graph(root: Path) -> dict:
    """The graph, provided graph.json names a commit and no non-exempt file changed since; graphify-out/ must be ignored."""
    ignore = root / ".graphifyignore"
    if not ignore.exists() or not {"graphify-out", "graphify-out/", "graphify-out/**"} & {line.strip() for line in ignore.read_text().splitlines()}:
        fail(".graphifyignore must list graphify-out/ so a pack never becomes graph input; run `sdlc knowledge bootstrap`")
    built = knowledge.graph_commit(root)
    if not built:
        fail("graphify-out/graph.json missing or without built_at_commit; run `sdlc knowledge bootstrap`")
    conf = p.config(root)
    stale = [f for f in p.git(root, "diff", "--name-only", built, "HEAD").splitlines() if f and not exempt(root, f, conf)]
    if stale:
        fail("graph.json is behind HEAD for files a pack would select; run `graphify update .` (or wait for the post-commit rebuild)", stale=stale)
    return knowledge.load_graph(root)


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
    graph = fresh_graph(root)
    seed_files, unresolved = seeds(root, feature, stage)
    selected = expand(graph, seed_files, p.config(root)["knowledge"]["pack_hops"])
    admitted, excluded = admit(root, list(selected))
    if dirty := p.changed_files(root, *admitted):
        fail("packed files have uncommitted changes; a pack is pinned to HEAD, so commit or stash them first", dirty=dirty)
    files = {f: selected[f] for f in admitted}
    budget = max_tokens if max_tokens is not None else p.config(root)["knowledge"]["pack_max_tokens"]
    version = p.run_cmd(root, ["repomix", "--version"]).stdout.strip()
    head = p.head_commit(root)
    key = hashlib.sha256(json.dumps([head, sorted(files), budget, version]).encode()).hexdigest()
    out = store(root) / feature.name
    manifest_path = out / f"{stage}-{key[:12]}.json"
    if (cached := p.read_json(manifest_path)) and Path(cached["path"]).exists():
        return {"ok": True, **verdict_of(cached), "reused": True}
    run_bandit(root, [f for f in admitted if f.endswith(".py")])
    out.mkdir(parents=True, exist_ok=True)
    tmp = out / f".{stage}-{key[:12]}.tmp.xml"
    try:
        packed, steps = ladder(root, admitted, set(seed_files), budget, tmp)
        tokens = steps[-1]["tokens"]
        pack_path = manifest_path.with_suffix(".xml")
        manifest = {
            "slug": feature.name,
            "stage": stage,
            "head": head,
            "key": key,
            "repomix_version": version,
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
        write_atomic(manifest_path, json.dumps(manifest, indent=2) + "\n")
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


def store(root: Path) -> Path:
    """graphify-out/packs/, with a `*` .gitignore written on first use so nothing in it is ever committed."""
    base = knowledge.graph_path(root).parent / "packs"
    base.mkdir(parents=True, exist_ok=True)
    if not (ignore := base / ".gitignore").exists():
        ignore.write_text("*\n")
    return base


def write_atomic(path: Path, text: str) -> None:
    tmp = path.with_name(f".{path.name}.tmp")
    tmp.write_text(text)
    tmp.replace(path)


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
    if findings := [f"{r['filename']}:{r['line_number']} {r['test_id']}" for r in results]:
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
    packed = set(PACKED.findall(xml))
    if missing := sorted(set(requested) - packed):
        fail("repomix left requested files out of the pack; no pack written", missing=missing)
    if extra := sorted(packed - set(requested)):
        fail("repomix packed files that were not requested; no pack written", extra=extra)
