"""Stage-boundary checkpoints: `cli.main` commits the SDLC home directory and `[checkpoint] paths` after each boundary.
The commit carries a pathspec, so source code stays out and work already staged in the index survives.
"""

from __future__ import annotations

import os
from pathlib import Path

from . import project as p
from .project import fail

SKIPPED = {"ok": True, "committed": False, "skipped": "checkpoints disabled"}
IN_PROGRESS = ("MERGE_HEAD", "CHERRY_PICK_HEAD", "REVERT_HEAD", "rebase-merge", "rebase-apply")


def enabled(root: Path) -> bool:
    return os.environ.get("SDLC_CHECKPOINT") != "off" and bool(p.config(root)["checkpoint"]["enabled"])


when_enabled = p.when_enabled(enabled, SKIPPED)


def pending(root: Path) -> list[str]:
    """Changed files under the SDLC home directory or `[checkpoint] paths`; git-ignored files never appear."""
    return p.changed_files(root, p.rel(root, p.home(root)), *p.config(root)["checkpoint"]["paths"])


def busy(root: Path) -> bool:
    git_dir = root / p.git(root, "rev-parse", "--git-dir")  # per-worktree, so a linked worktree's rebase is seen
    return any((git_dir / marker).exists() for marker in IN_PROGRESS)


def subject(root: Path, stage: str, action: str, produced: Path, files: list[str]) -> str:
    """`<stage>(<slug>): <action> — <file>` for a feature's artifact, `<stage>: ...` for one directly under the home directory."""
    scope = produced.parent.name if produced.parent != p.home(root) else ""
    extras = len(files) - (p.rel(root, produced) in files)
    tail = f" (+{extras} file{'s' if extras > 1 else ''})" if extras else ""
    return f"{stage}{f'({scope})' if scope else ''}: {action} — {produced.name}{tail}"


@when_enabled
def commit(root: Path, stage: str, action: str, produced: Path) -> dict:
    """Commit what the boundary produced plus anything generated since the last one. Nothing changed is a success, not a refusal."""
    if busy(root):
        return {"ok": True, "committed": False, "reason": "a merge, rebase, cherry-pick or revert is in progress"}
    if not (files := pending(root)):
        return {"ok": True, "committed": False, "reason": "nothing to checkpoint"}
    message = subject(root, stage, action, produced, files)
    for argv in (["add", "--", *files], ["commit", "--no-verify", "-m", message, "--", *files]):
        result = p.run_git(root, *argv)
        if result.returncode != 0:
            fail(f"git {argv[0]} failed: {(result.stderr.strip().splitlines() or ['no output'])[-1]}", committed=False, message=message)
    return {"ok": True, "committed": True, "message": message, "files": files}
