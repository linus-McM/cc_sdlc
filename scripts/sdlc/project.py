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
rollback = ""               # single rehearsed command; required before production
[deploy.environments]
dev = "free"                # agent deploys freely
staging = "ask"             # agent asks before deploying
production = "gate"         # needs RELEASE_APPROVAL=<name> in the environment

[evals]
threshold = 1.0             # minimum pass rate for `test evals`

[maintain]
metrics = "sdlc/metrics.jsonl"   # {"metric": str, "value": float, "ts": str} per line
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
        out[key] = (
            merge(out[key], value)
            if isinstance(value, dict) and isinstance(out.get(key), dict)
            else value
        )
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


def git(root: Path, *args: str) -> str:
    return subprocess.run(
        ["git", *args], cwd=root, capture_output=True, text=True, check=False
    ).stdout.strip()


def author(root: Path) -> str:
    return git(root, "config", "user.name") or os.environ.get("USER", "unknown")


def changed_files(root: Path) -> list[str]:
    """Staged, unstaged and untracked paths in one git call."""
    lines = git(root, "status", "--porcelain", "--untracked-files=all").splitlines()
    return sorted(line[3:].split(" -> ")[-1] for line in lines)


def today() -> str:
    return datetime.now(UTC).date().isoformat()


def read_jsonl(path: Path) -> list[dict]:
    return (
        [json.loads(line) for line in path.read_text().splitlines() if line.strip()]
        if path.exists()
        else []
    )


def append_jsonl(path: Path, row: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("a") as fh:
        fh.write(json.dumps(row) + "\n")


def read_json(path: Path, default=None):
    return json.loads(path.read_text()) if path.exists() else default


def write_json(path: Path, data) -> None:
    path.write_text(json.dumps(data, indent=2))
