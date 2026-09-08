"""Project-level state: config schema, artifact home, git and JSONL helpers, the Blocked verdict."""

from __future__ import annotations

import json
import os
import subprocess
import tomllib
from datetime import UTC, datetime
from pathlib import Path

PLUGIN_ROOT = Path(__file__).resolve().parents[2]
TEMPLATES = PLUGIN_ROOT / "templates"
CONFIG_NAME = ".sdlc.toml"
DEFAULT_CONFIG = """# sdlc plugin configuration (read by every stage; commit it)
[commands]
test = "pytest -q"          # must exit non-zero on failure
lint = ""                   # optional
build = ""                  # optional

[build]
require_tdd = true          # `test run` refuses without a recorded red->green cycle
protected_paths = []        # globs Claude may never edit, e.g. "src/gen/**"
test_globs = ["tests/**", "test_*.py", "*_test.py", "*.test.*", "*.spec.*"]

[deploy]
command = ""                # release command with {env}, e.g. "./deploy.sh {env}"; the pre-bash hook gates it
rollback = ""               # single rehearsed command; required before production
[deploy.environments]
dev = "free"                # agent deploys freely
staging = "ask"             # agent asks before deploying
production = "gate"         # needs RELEASE_APPROVAL=<name> in the environment

[evals]
threshold = 1.0             # minimum pass rate for `test evals`

[maintain]
metrics = "sdlc/metrics.jsonl"   # {"metric": str, "value": float, "ts": str} per line

[knowledge]
enabled = true              # Graphify graph + OKF bundle; SDLC_KNOWLEDGE=off also disables
auto_install = false        # SessionStart installs missing tools only when true; stage commands always do
bundle = "sdlc/knowledge"   # OKF bundle root, relative to the project root
claude_md_pointer = true    # add a two-line pointer block to CLAUDE.md
clean_every = 5             # force a clean graph rebuild after this many incremental refreshes
max_behind = 1              # `knowledge status` fails when an index is behind HEAD by more commits
stale_after_days = 14       # concept stale_after = generation time + this
artifact_skew_seconds = 300 # graph.json / GRAPH_REPORT.md / graph.html mtimes may differ this much
min_community_nodes = 3     # smaller Graphify communities get no Module concept
god_nodes = 10              # Hub concepts from `graphify god-nodes --top N`
ignore = ["sdlc/*/references/", "sdlc/knowledge/", "graphify-out/", ".venv/"]   # written to .graphifyignore
"""
DEFAULTS = tomllib.loads(DEFAULT_CONFIG)


class Blocked(Exception):
    """A gate refused; `.verdict` is the JSON dict the CLI prints."""

    def __init__(self, reason: str, **extra):
        super().__init__(reason)
        self.verdict = {"ok": False, "reason": reason, **extra}


def fail(reason: str, **extra):
    raise Blocked(reason, **extra)


def merge(base: dict, over: dict) -> dict:
    out = dict(base)
    for key, value in over.items():
        out[key] = merge(out[key], value) if isinstance(value, dict) and isinstance(out.get(key), dict) else value
    return out


def config(root: Path) -> dict:
    """DEFAULT_CONFIG deep-merged with .sdlc.toml, so every key is always present."""
    path = root / CONFIG_NAME
    return merge(DEFAULTS, tomllib.loads(path.read_text()) if path.exists() else {})


def ensure_config(root: Path) -> None:
    path = root / CONFIG_NAME
    if not path.exists():
        path.write_text(DEFAULT_CONFIG)


def home(root: Path, create: bool = False) -> Path:
    path = root / os.environ.get("SDLC_HOME", "sdlc")
    if create:
        path.mkdir(parents=True, exist_ok=True)
    return path


def feature(root: Path, slug: str | None) -> Path:
    """The named feature directory, or the most recently modified one; Blocked when none exists."""
    base = home(root)
    if slug:
        target = base / slug
        if (target / "intent.md").exists():
            return target
    elif base.exists():
        dirs = [d for d in base.iterdir() if (d / "intent.md").exists()]
        if dirs:
            return max(dirs, key=lambda d: d.stat().st_mtime)
    return fail("no feature found; run /sdlc:plan new first")


def run_cmd(root: Path, argv: list[str], env: dict | None = None) -> subprocess.CompletedProcess:
    """Run an external tool without a shell; never raises on a non-zero exit."""
    full = {**os.environ, **env} if env else None
    return subprocess.run(argv, cwd=root, capture_output=True, text=True, check=False, env=full)


def run_git(root: Path, *args: str) -> subprocess.CompletedProcess:
    return run_cmd(root, ["git", *args])


def git(root: Path, *args: str) -> str:
    return run_git(root, *args).stdout.rstrip("\n")


def author(root: Path) -> str:
    return git(root, "config", "user.name") or os.environ.get("USER", "unknown")


def changed_files(root: Path) -> list[str]:
    """Staged, unstaged and untracked paths in one git call."""
    lines = git(root, "status", "--porcelain", "--untracked-files=all").splitlines()
    return sorted(line[3:].split(" -> ")[-1] for line in lines)


def today() -> str:
    return datetime.now(UTC).date().isoformat()


def read_jsonl(path: Path) -> list[dict]:
    return [json.loads(line) for line in path.read_text().splitlines() if line.strip()] if path.exists() else []


def append_jsonl(path: Path, row: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("a") as fh:
        fh.write(json.dumps(row) + "\n")


def read_json(path: Path, default=None):
    if not path.exists():
        return default
    try:
        return json.loads(path.read_text())
    except json.JSONDecodeError as err:
        return fail(f"{path.name} is not valid JSON ({err.msg} at line {err.lineno}); rewrite or delete it", path=str(path))


def write_json(path: Path, data) -> None:
    path.write_text(json.dumps(data, indent=2) + "\n")
