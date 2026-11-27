"""Build-stage mechanics: the approved plan, the red/green TDD log, plan sync in both directions, fix lock."""

from __future__ import annotations

import os
import re
import shlex
import subprocess
from pathlib import Path

from . import artifacts as a
from . import checkpoint
from . import project as p
from .project import fail

SDLC_OWNED = ("sdlc/", ".sdlc.toml", "CLAUDE.md", "REVIEW.md")  # REVIEW.md: `test run` copies the template in
APPROVED = "approved.json"  # what the user approved at `build accept`: the plan's files and steps, and the commit the build starts from
STEP = re.compile(r"(?:step[\s-]*)?(\d+)\b", re.IGNORECASE)  # `2`, `2: parse`, `step 2`: the plan step a TDD log entry belongs to


def run_cmd(root: Path, cmd: str) -> dict:
    # cmd is the operator-configured .sdlc.toml command, so a shell is intended
    proc = subprocess.run(cmd, shell=True, cwd=root, capture_output=True, text=True, check=False)  # nosec B602
    output = (proc.stdout + proc.stderr).strip()
    return {"cmd": cmd, "exit": proc.returncode, "tail": "\n".join(output.splitlines()[-20:])}


def completed(log: list[dict]) -> list[str]:
    """The step name of every completed red->green pair, matched per step name in order."""
    done, open_reds = [], set()
    for entry in log:
        if entry["phase"] == "red":
            open_reds.add(entry["step"])
        elif entry["phase"] == "green" and entry["step"] in open_reds:
            open_reds.discard(entry["step"])
            done.append(entry["step"])
    return done


def cycles(log: list[dict]) -> int:
    return len(completed(log))


def plan_state(feature: Path) -> dict:
    """What an approval pins: plan.md's files and its numbered steps."""
    found = a.sections((feature / "plan.md").read_text())
    return {"files": a.list_items(found.get("Files that change", "")), "steps": {str(n): text for n, text in a.numbered(found.get("Order of work", "")).items()}}


def approve(root: Path, feature: Path) -> dict:
    """Record the plan as approved. A later approval keeps the first one's base commit: the build is measured from where it started."""
    earlier = p.read_json(feature / APPROVED, {})
    data = {"base": earlier.get("base") or p.head_commit(root), "ts": p.today(), **plan_state(feature)}
    p.write_json(feature / APPROVED, data)
    return {"path": str(feature / APPROVED), "base": data["base"][:12], "files": len(data["files"]), "steps": len(data["steps"])}


def deviations(feature: Path) -> dict:
    """How plan.md differs now from the plan the user approved; empty when it does not, or when nothing was approved."""
    if not (approved := p.read_json(feature / APPROVED)):
        return {}
    now = plan_state(feature)
    found = {
        "files_added": sorted(set(now["files"]) - set(approved["files"])),
        "files_removed": sorted(set(approved["files"]) - set(now["files"])),
        "steps_changed": sorted((n for n in {*now["steps"], *approved["steps"]} if now["steps"].get(n) != approved["steps"].get(n)), key=int),
    }
    return {kind: items for kind, items in found.items() if items}


def missing_steps(feature: Path, log: list[dict]) -> list[str]:
    """Numbered plan.md steps with no completed red->green cycle. A log step belongs to the plan step whose number it starts with."""
    done = {m.group(1) for step in completed(log) if (m := STEP.match(step.strip()))}
    return [n for n in plan_state(feature)["steps"] if n not in done]


def untouched(root: Path, feature: Path) -> list[str]:
    """Planned files the build never changed since the approval's base commit; empty when there is no approval or the base is gone (a rebase)."""
    if not (approved := p.read_json(feature / APPROVED)):
        return []
    diff = p.run_git(root, "diff", "--name-only", "--relative", approved["base"], "--")
    if diff.returncode != 0:
        return []
    touched = {*diff.stdout.splitlines(), *p.changed_files(root)}
    return [f for f in planned_files(feature) if f not in touched]


def scoped(root: Path, selector: str | None) -> str | None:
    """`[commands] test_one` rendered for `selector` (shell-quoted), or None when either is missing."""
    template = p.config(root)["commands"]["test_one"]
    return template.replace("{selector}", shlex.quote(selector)) if selector and "{selector}" in template else None


def tdd(root: Path, feature: Path, phase: str, step: str, selector: str | None = None) -> dict:
    """Record a red or green run. With `selector` and `[commands] test_one`, red runs that one test, and green runs it
    first and the full suite only once it passes. A passing green also runs plan sync and commits the step."""
    full = p.config(root)["commands"]["test"]
    one = scoped(root, selector)
    log = p.read_jsonl(feature / "tdd.jsonl")
    if phase == "green" and not any(e["phase"] == "red" and e["step"] == step for e in log):
        fail(f"no red run recorded for step {step!r}; run `build red {step}` first")
    cmd = one or full
    result = run_cmd(root, cmd)
    if phase == "red" and result["exit"] == 0:
        fail(f"tests passed; a red step must fail first ({cmd})", **result)
    if phase == "green":
        if result["exit"] != 0:
            fail("tests still failing; fix the code, not the tests", **result)
        if one and (result := run_cmd(root, full))["exit"] != 0:
            fail("the step's test passes but the full suite fails; fix the code, not the tests", **result)
    entry = {"phase": phase, "step": step, "exit": result["exit"], "ts": p.today()}
    p.append_jsonl(feature / "tdd.jsonl", entry)
    verdict = {"ok": True, "phase": phase, "step": step, "cycles": cycles([*log, entry])}
    if selector:
        verdict["scoped"] = bool(one)  # false: no `[commands] test_one` with {selector}, so the full suite ran
    if phase == "red":
        return {**verdict, "tail": result["tail"]}  # why it fails; a passing green needs no output
    verdict["sync"] = p.attempt(sync, root, feature)
    if verdict["sync"]["ok"]:
        verdict["commit"] = p.attempt(commit_step, root, feature, step)
    else:
        verdict["next"] = "list the unplanned files in plan.md 'Files that change' or revert them, then `build sync` and commit the step"
    return verdict


def commit_step(root: Path, feature: Path, step: str) -> dict:
    """Commit everything the step changed as `build(<slug>): <step>`; plan sync has passed, so every changed file is planned or SDLC-owned."""
    if not (p.config(root)["build"]["commit_steps"] and checkpoint.enabled(root)):
        return {"ok": True, "committed": False, "skipped": "step commits disabled"}
    if checkpoint.busy(root):
        return {"ok": True, "committed": False, "reason": "a merge, rebase, cherry-pick or revert is in progress"}
    if not (files := p.changed_files(root)):
        return {"ok": True, "committed": False, "reason": "nothing to commit"}
    message = f"build({feature.name}): {step}"
    for argv in (["add", "--", *files], ["commit", "-m", message, "--", *files]):  # the project's own commit hooks run: this is source code
        result = p.run_git(root, *argv)
        if result.returncode != 0:
            fail(f"git {argv[0]} failed: {((result.stderr.strip() or result.stdout.strip()).splitlines() or ['no output'])[-1]}", committed=False, message=message)
    return {"ok": True, "committed": True, "message": message, "files": len(files)}


def simplify_required(root: Path) -> bool:
    return os.environ.get("SDLC_SIMPLIFY") != "off" and bool(p.config(root)["build"]["require_simplify"])


def simplified(log: list[dict]) -> bool:
    """A simplify pass is recorded and no step went green after it."""
    last = next((e["phase"] for e in reversed(log) if e["phase"] in ("green", "simplify")), None)
    return last == "simplify"


def simplify(root: Path, feature: Path) -> dict:
    """Record the `/simplify` pass over the finished build: the test and lint commands pass, plan sync passes, and the
    result is committed as `build(<slug>): simplify`. Python cannot see the skill run; this is the engineer's record
    that it did, and `test run` is refused without one since the last green."""
    conf = p.config(root)["commands"]
    results = [{"name": name, **run_cmd(root, cmd)} for name in ("test", "lint") if (cmd := conf[name])]
    if failed := [r["name"] for r in results if r["exit"] != 0]:
        fail("checks failed after /simplify: fix the simplification or revert it, never the tests", failed=failed, results=results)
    sync(root, feature)
    commit = p.attempt(commit_step, root, feature, "simplify")
    p.append_jsonl(feature / "tdd.jsonl", {"phase": "simplify", "step": "simplify", "exit": 0, "ts": p.today()})
    return {"ok": True, "phase": "simplify", "commit": commit, "next": "/sdlc:test"}


def planned_files(feature: Path) -> list[str]:
    plan = feature / "plan.md"
    return a.list_items(a.sections(plan.read_text()).get("Files that change", "")) if plan.exists() else []


def is_sdlc_owned(rel: str) -> bool:
    return rel.startswith(SDLC_OWNED)


def sync(root: Path, feature: Path) -> dict:
    planned = planned_files(feature)
    unplanned = [f for f in p.changed_files(root) if f not in planned and not is_sdlc_owned(f)]
    if unplanned:
        fail(
            "changed files not listed in plan.md; add them in the same commit",
            unplanned=unplanned,
            planned=planned,
        )
    return {"ok": True, "unplanned": []}


def fix(feature: Path, state: str) -> dict:
    lock = feature / ".fix-lock"
    on = state == "on"
    lock.touch() if on else lock.unlink(missing_ok=True)
    return {
        "ok": True,
        "fix_lock": on,
        "next": "test files are read-only while the lock is on" if on else "/sdlc:test",
    }
