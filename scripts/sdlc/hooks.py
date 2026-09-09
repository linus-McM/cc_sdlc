"""Deterministic guardrails. Invoked by hooks/hooks.json: `hook.py <event>` with the hook JSON on stdin.

Events: pre-edit (protected paths, fix lock), pre-bash (advisory release check; `deploy.check` is
the gate), post-edit (plan sync, knowledge concepts touched), post-bash (knowledge staleness after
a commit), session-start (knowledge bootstrap, check-only unless auto_install, no git). Each handler
returns a hook JSON dict to print, or None to stay silent. The per-call handlers stay cheap (one
config read, no git except after a commit) because they fire on every Edit and Bash call.
"""

from __future__ import annotations

import json
import os
import re
import shlex
import sys
from pathlib import Path

from . import artifacts as a
from . import build, deploy, knowledge
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


def context(text: str, event: str = "PostToolUse") -> dict:
    return {"hookSpecificOutput": {"hookEventName": event, "additionalContext": text}}


def rel_path(payload: dict, root: Path) -> str | None:
    raw = payload.get("tool_input", {}).get("file_path")
    if not raw:
        return None
    # Judge a path by its name inside the project (`..` collapsed, symlinks kept) so a link to an
    # outside file is still the protected in-repo name; a path that leaves the project is not ours.
    lexical = (Path(os.path.abspath(raw)), Path(os.path.abspath(root)))  # noqa: PTH100  resolve() would follow the link
    for path, base in (lexical, (Path(raw).resolve(), root.resolve())):
        if path.is_relative_to(base):
            return path.relative_to(base).as_posix()
    return None


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


HEREDOC = re.compile(r"<<-?\s*(['\"]?)(\w+)\1")


def command_lines(cmd: str) -> list[str]:
    """Logical command lines: backslash continuations joined, heredoc bodies dropped."""
    lines, terminator = [], None
    for line in cmd.replace("\\\n", " ").splitlines():
        if terminator:
            terminator = None if line.strip() == terminator else terminator
        elif line.strip():
            lines.append(line)
            if m := HEREDOC.search(line):
                terminator = m.group(2)
    return lines


def tokens(text: str) -> list[str]:
    """Shell tokens of every command line; quoted prose stays one token, unbalanced quotes fall back to whitespace."""
    out: list[str] = []
    for line in command_lines(text):
        try:
            out += shlex.split(line)
        except ValueError:
            out += line.split()
    return out


def release_hit(cmd: str, template: str, gated: list[str]) -> str | None:
    """What in `cmd` looks like a release to a gated environment, or None.

    Always: a token whose basename is `deploy` co-occurs with a token naming a gate-tier environment
    (the configured names only), also matching the value after `=` and ignoring trailing punctuation.
    Additionally, when `template` (deploy.command) is configured, its rendering for a gated env
    appearing as a contiguous token run.
    """
    toks = tokens(cmd)
    for env in gated if template.strip() else ():
        want = tokens(template.replace("{env}", env))
        if any(toks[i : i + len(want)] == want for i in range(len(toks) - len(want) + 1)):
            return " ".join(want)
    names = {env.lower() for env in gated}
    program = next((t for t in toks if Path(t).stem.lower() == "deploy"), None)
    env = next((t for t in toks if t.rpartition("=")[2].strip(";,/").lower() in names), None)
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
    notes = []
    planned = build.planned_files(feature)
    if planned and rel not in planned:
        notes.append(f"{rel} is not listed in {feature.name}/plan.md 'Files that change'; update plan.md in the same commit")
    if concepts := knowledge.concepts_for(root, rel):
        notes.append("knowledge concepts describing this file (regenerated on commit): " + ", ".join(concepts))
    return context("\n".join(notes)) if notes else None


def is_commit(cmd: str) -> bool:
    toks = tokens(cmd)
    return "git" in toks and "commit" in toks[toks.index("git") + 1 :]


def post_bash(payload: dict, root: Path) -> dict | None:
    """After a commit: say when an index has fallen further behind than the configured tolerance."""
    cmd = payload.get("tool_input", {}).get("command", "")
    if not is_commit(cmd) or not knowledge.enabled(root):
        return None
    verdict = knowledge.status(root)
    if verdict.get("ok", True) or not verdict.get("reasons"):
        return None
    return context("knowledge: " + "; ".join(verdict["reasons"]) + " (the post-commit hook may still be running; check `sdlc knowledge status`)")


def session_start(payload: dict, root: Path) -> dict | None:
    """Bootstrap report for the session: check-only unless [knowledge] auto_install is set."""
    if not knowledge.enabled(root):
        return None
    conf = knowledge.cfg(root)
    verdict = knowledge.bootstrap(root, check=not conf["auto_install"])
    steps = verdict.get("steps", [])
    lines = [f"{s['name']}: {s['state']}" + (f" ({s['detail']})" if s["state"] not in ("present", "skipped") and s["detail"] else "") for s in steps]
    if all(s["state"] == "present" for s in steps):
        text = f"sdlc knowledge: all present; read {conf['bundle']}/index.md first, `graphify query` for call-graph questions."
    else:
        text = "sdlc knowledge bootstrap (" + verdict.get("mode", "check") + "): " + "; ".join(lines)
        if verdict.get("reason"):
            text += f". {verdict['reason']}"
        if verdict.get("ok"):
            text += f" Read {conf['bundle']}/index.md first."
    text += " `sdlc knowledge status` reports how far each index is behind HEAD."
    return context(text, "SessionStart")


HANDLERS = {"pre-edit": pre_edit, "pre-bash": pre_bash, "post-edit": post_edit, "post-bash": post_bash, "session-start": session_start}


def main(argv: list[str], root: Path | None = None) -> int:
    payload = json.load(sys.stdin)
    root = root or Path(payload.get("cwd") or os.environ.get("CLAUDE_PROJECT_DIR") or Path.cwd())
    try:
        out = HANDLERS[argv[0]](payload, root)
    except Blocked as blocked:  # a config or state problem is reported as context; a pre-tool hook never denies on it
        out = None if argv[0].startswith("pre-") else context(f"sdlc hook {argv[0]}: {blocked.verdict['reason']}", "SessionStart" if argv[0] == "session-start" else "PostToolUse")
    if out:
        print(json.dumps(out))
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
