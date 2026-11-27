"""Deterministic guardrails. Invoked by hooks/hooks.json: `hook.py <event>` with the hook JSON on stdin.

Events: pre-edit (protected paths, fix lock), pre-bash (asks before a release to a gate-tier environment; `deploy.check` is
the gate), post-edit (plan sync, knowledge concepts touched), post-bash (knowledge staleness after
a commit), session-start (workflow env merge into .claude/settings.local.json, then the knowledge
bootstrap, check-only unless auto_install, no git). Each handler
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
from . import project as p
from .project import Blocked, attempt


def decide(decision: str, reason: str) -> dict:
    return {
        "hookSpecificOutput": {
            "hookEventName": "PreToolUse",
            "permissionDecision": decision,
            "permissionDecisionReason": reason,
        }
    }


def deny(reason: str) -> dict:
    return decide("deny", reason)


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
        return deny(f"{rel} is a protected path (.sdlc.toml build.protected_paths); Claude never edits it")
    if a.matches(rel, cfg["test_globs"]) and (feature := active_feature(root)) and (feature / ".fix-lock").exists():
        return deny(f"{rel} is a test file and the fix lock is on: fix the code, not the test (`build fix off` to release)")
    return None


ADVISORY = "the hook only asks; `deploy.check` is the gate, so run `sdlc deploy check <env>` first"


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
    from . import deploy  # imported where used: every handler pays only for what it needs (this runs on every tool call)

    cmd = payload.get("tool_input", {}).get("command", "")
    if not cmd.strip():
        return None
    cfg = p.config(root)["deploy"]
    hit = release_hit(cmd, cfg["command"], deploy.gated(cfg))
    return decide("ask", f"`{hit}` looks like a release to a gated environment; {ADVISORY}") if hit else None


def post_edit(payload: dict, root: Path) -> dict | None:
    from . import build, knowledge

    rel = rel_path(payload, root)
    if rel is None or build.is_sdlc_owned(rel) or not (feature := active_feature(root)):
        return None
    notes = {}  # kind -> text; the concepts note is keyed by its text, so a changed list speaks again
    planned = build.planned_files(feature)
    if planned and rel not in planned and not ready_to_deploy(feature):
        notes["plan"] = f"{rel} is not listed in {feature.name}/plan.md 'Files that change'; update plan.md in the same commit"
    if concepts := knowledge.concepts_for(root, rel):
        text = "knowledge concepts describing this file (regenerated on commit): " + ", ".join(concepts)
        notes[f"concepts:{text}"] = text
    notes = unsaid(root, payload.get("session_id"), rel, notes)
    return context("\n".join(notes.values())) if notes else None


def ready_to_deploy(feature: Path) -> bool:
    """Whether the feature is past build and test: its plan no longer says which files an edit may touch."""
    from . import deploy

    return not deploy.readiness(feature)


def git_dir(root: Path) -> Path | None:
    """The per-worktree git dir, read from `.git` without spawning git (this runs on every edit)."""
    dot = root / ".git"
    if dot.is_dir():
        return dot
    if dot.is_file() and (line := dot.read_text().strip()).startswith("gitdir:"):
        return (root / line.split(":", 1)[1].strip()).resolve()
    return None


def common_dir(root: Path) -> Path | None:
    """The git dir shared by every worktree of the repository checked out at `root`."""
    if (base := git_dir(root)) is None:
        return None
    link = base / "commondir"
    return (base / link.read_text().strip() if link.is_file() else base).resolve()


def checkout(payload: dict, root: Path) -> Path:
    """The worktree of this repository that holds the edited file, else `root`.

    A session rooted in one worktree can edit a file in another; that edit is judged by the plan and the
    repo-relative path of the worktree the file is in, not by the session's.
    """
    raw = payload.get("tool_input", {}).get("file_path")
    if not raw:
        return root
    for folder in Path(os.path.abspath(raw)).parents:  # noqa: PTH100  lexical, as in rel_path
        if (folder / ".git").exists():
            return folder if common_dir(folder) == common_dir(root) else root
    return root


def unsaid(root: Path, session: str | None, rel: str, notes: dict) -> dict:
    """The notes not yet said for `rel` this session, recorded as said; everything when there is no session or state.

    The state lives in the git dir, not the SDLC home, so a checkpoint never commits it.
    """
    if not session or not notes:
        return notes
    try:
        if (base := git_dir(root)) is None:
            return notes
        path = base / "sdlc" / f"hook-notes-{re.sub(r'[^A-Za-z0-9_-]', '_', session)}.json"
        said = json.loads(path.read_text()) if path.exists() else {}
        known = set(said.get(rel, []))
        fresh = {kind: text for kind, text in notes.items() if kind not in known}
        if fresh:
            said[rel] = sorted(known | set(fresh))
            path.parent.mkdir(parents=True, exist_ok=True)
            p.write_json(path, said)
        return fresh
    except (OSError, ValueError, AttributeError, TypeError):  # unreadable or odd state: speak rather than break the hook
        return notes


def is_commit(cmd: str) -> bool:
    toks = tokens(cmd)
    return "git" in toks and "commit" in toks[toks.index("git") + 1 :]


def post_bash(payload: dict, root: Path) -> dict | None:
    """After a commit: say when an index has fallen further behind than the configured tolerance."""
    cmd = payload.get("tool_input", {}).get("command", "")
    if not is_commit(cmd):
        return None
    from . import knowledge

    if not knowledge.enabled(root):
        return None
    verdict = knowledge.status(root)
    if verdict.get("ok", True) or not verdict.get("reasons"):
        return None
    return context("knowledge: " + "; ".join(verdict["reasons"]) + " (the post-commit hook may still be running; check `sdlc knowledge status`)")


def session_start(payload: dict, root: Path) -> dict | None:
    """Session report: the workflow env merge, then the knowledge bootstrap (check-only unless [knowledge] auto_install)."""
    notes = [note for note in (workflow_note(root), knowledge_note(root)) if note]
    return context(" ".join(notes), "SessionStart") if notes else None


def workflow_note(root: Path) -> str | None:
    from . import workflows

    verdict = attempt(workflows.env, root)
    if not verdict["ok"]:
        return f"sdlc workflows: {verdict['reason']}."
    if verdict["written"]:
        return f"sdlc workflows: set {', '.join(verdict['written'])} in {verdict['settings']}; {verdict['next']}."
    return None


def knowledge_note(root: Path) -> str | None:
    from . import knowledge

    if not knowledge.enabled(root):
        return None
    conf = knowledge.cfg(root)
    repointed = knowledge.repoint_hook(root)  # before bootstrap, so hooks_present sees the repaired block
    verdict = knowledge.bootstrap(root, check=not conf["auto_install"])
    steps = verdict.get("steps", [])
    lines = [f"{s['name']}: {s['state']}" + (f" ({s['detail']})" if s["state"] not in ("present", "skipped") and s["detail"] else "") for s in steps]
    if all(s["state"] in ("present", "skipped") for s in steps):  # skipped: the step does not apply here
        text = f"sdlc knowledge: all present; read {conf['bundle']}/index.md first, `graphify query` for call-graph questions."
    else:
        text = "sdlc knowledge bootstrap (" + verdict.get("mode", "check") + "): " + "; ".join(lines)
        if verdict.get("reason"):
            text += f". {verdict['reason']}"
        if verdict.get("ok"):
            text += f" Read {conf['bundle']}/index.md first."
    if repointed:
        text += " post-commit block repointed at this plugin's path."
    return text + " `sdlc knowledge status` reports how far each index is behind HEAD."


HANDLERS = {"pre-edit": pre_edit, "pre-bash": pre_bash, "post-edit": post_edit, "post-bash": post_bash, "session-start": session_start}


def main(argv: list[str], root: Path | None = None) -> int:
    payload = json.load(sys.stdin)
    root = root or Path(payload.get("cwd") or os.environ.get("CLAUDE_PROJECT_DIR") or Path.cwd())
    try:
        out = HANDLERS[argv[0]](payload, checkout(payload, root))
    except Blocked as blocked:  # a config or state problem is reported as context; a pre-tool hook never denies on it
        out = None if argv[0].startswith("pre-") else context(f"sdlc hook {argv[0]}: {blocked.verdict['reason']}", "SessionStart" if argv[0] == "session-start" else "PostToolUse")
    if out:
        print(json.dumps(out))
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
