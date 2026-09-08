"""Deterministic guardrails. Invoked by hooks/hooks.json: `hook.py <event>` with the hook JSON on stdin.

Events: pre-edit (protected paths, fix lock), pre-bash (production gate), post-edit (plan sync).
Each handler returns a hook JSON dict to print, or None to stay silent. Cheap string checks run
before any filesystem or git work because these fire on every Edit and Bash call.
"""

from __future__ import annotations

import json
import os
import shlex
import sys
from pathlib import Path

from . import artifacts as a
from . import build, deploy
from . import project as p
from .project import Blocked


def deny(reason: str) -> dict:
    return {
        "hookSpecificOutput": {
            "hookEventName": "PreToolUse",
            "permissionDecision": "deny",
            "permissionDecisionReason": reason,
        }
    }


def context(text: str) -> dict:
    return {"hookSpecificOutput": {"hookEventName": "PostToolUse", "additionalContext": text}}


def rel_path(payload: dict, root: Path) -> str | None:
    raw = payload.get("tool_input", {}).get("file_path")
    if not raw:
        return None
    path = Path(raw)
    try:
        return path.resolve().relative_to(root.resolve()).as_posix()
    except ValueError:
        return path.as_posix()


def active_feature(root: Path) -> Path | None:
    try:
        return p.feature(root, None)
    except Blocked:
        return None


def pre_edit(payload: dict, root: Path) -> dict | None:
    rel = rel_path(payload, root)
    if rel is None:
        return None
    cfg = p.config(root)["build"]
    if a.matches(rel, cfg["protected_paths"]):
        return deny(f"{rel} is a protected path (.sdlc.toml build.protected_paths); changes need the path owner")
    if a.matches(rel, cfg["test_globs"]) and (feature := active_feature(root)) and (feature / ".fix-lock").exists():
        return deny(f"{rel} is a test file and the fix lock is on: fix the code, not the test (`build fix off` to release)")
    return None


ADVISORY = "the hook is advisory; `deploy.check` enforces authorization: set RELEASE_APPROVAL=<release manager> after sign-off"


def tokens(cmd: str) -> list[str]:
    """Shell tokens of the first non-empty line; later lines, heredoc bodies and quoted prose stay out."""
    first = next((line for line in cmd.splitlines() if line.strip()), "")
    try:
        return shlex.split(first)
    except ValueError:
        return first.split()


def release_hit(cmd: str, template: str, gated: list[str]) -> str | None:
    """What in `cmd` looks like a release to a gated environment, or None.

    With `template` (deploy.command) configured: its rendering for a gated env must appear as a
    contiguous token run. Otherwise: a token whose basename is `deploy` co-occurs with a gated env
    (or `prod`) token, also matching the value after `=`.
    """
    toks = tokens(cmd)
    if template:
        for env in gated:
            want = shlex.split(template.replace("{env}", env))
            if any(toks[i : i + len(want)] == want for i in range(len(toks) - len(want) + 1)):
                return " ".join(want)
        return None
    names = {*gated, "prod"}
    program = next((t for t in toks if Path(t).stem.lower() == "deploy"), None)
    env = next((t for t in toks if t.rpartition("=")[2].lower() in names), None)
    return f"{program} ... {env}" if program and env else None


def pre_bash(payload: dict, root: Path) -> dict | None:
    cmd = payload.get("tool_input", {}).get("command", "")
    if not cmd.strip() or deploy.approver():
        return None
    cfg = p.config(root)["deploy"]
    hit = release_hit(cmd, cfg["command"], deploy.gated(cfg))
    return deny(f"`{hit}` looks like a release to a gated environment; {ADVISORY}") if hit else None


def post_edit(payload: dict, root: Path) -> dict | None:
    rel = rel_path(payload, root)
    if rel is None or build.is_sdlc_owned(rel) or not (feature := active_feature(root)):
        return None
    planned = build.planned_files(feature)
    if planned and rel not in planned:
        return context(f"{rel} is not listed in {feature.name}/plan.md 'Files that change'; update plan.md in the same commit")
    return None


HANDLERS = {"pre-edit": pre_edit, "pre-bash": pre_bash, "post-edit": post_edit}


def main(argv: list[str], root: Path | None = None) -> int:
    payload = json.load(sys.stdin)
    root = root or Path(payload.get("cwd") or os.environ.get("CLAUDE_PROJECT_DIR") or Path.cwd())
    out = HANDLERS[argv[0]](payload, root)
    if out:
        print(json.dumps(out))
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
