"""Graph-selected Repomix context packs: one commit-pinned snapshot per stage that its Workflow agents share.

Seeds come from the stage artifact, grow one hop through graphify-out/graph.json, pass a frozen secret
exclude list, Bandit and Repomix's own secret check, and land in graphify-out/packs/ (never committed).
`require` is the plan and test gate: a pack built at HEAD, and at test one covering every changed file.
"""

from __future__ import annotations

import fnmatch
import re
from collections import defaultdict
from pathlib import Path

from . import artifacts as a
from . import build, deploy
from . import project as p

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
    return [f for f in p.git(root, "diff", "--name-only", "--diff-filter=d", spec).splitlines() if f and not build.is_sdlc_owned(f)]


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
    "build": lambda r, f: build.planned_files(f),
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
