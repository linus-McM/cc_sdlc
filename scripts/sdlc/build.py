"""Build-stage mechanics: red/green TDD log, plan sync, fix lock."""

from __future__ import annotations

import subprocess
from pathlib import Path

from . import artifacts as a
from . import project as p
from .project import fail

SDLC_OWNED = ("sdlc/", ".sdlc.toml", "CLAUDE.md")


def run_cmd(root: Path, cmd: str) -> dict:
    proc = subprocess.run(cmd, shell=True, cwd=root, capture_output=True, text=True, check=False)
    output = (proc.stdout + proc.stderr).strip()
    return {"cmd": cmd, "exit": proc.returncode, "tail": "\n".join(output.splitlines()[-20:])}


def cycles(log: list[dict]) -> int:
    """Completed red->green pairs, matched per step name in order."""
    done, open_reds = 0, set()
    for entry in log:
        if entry["phase"] == "red":
            open_reds.add(entry["step"])
        elif entry["step"] in open_reds:
            open_reds.discard(entry["step"])
            done += 1
    return done


def tdd(root: Path, feature: Path, phase: str, step: str) -> dict:
    cmd = p.config(root)["commands"]["test"]
    result = run_cmd(root, cmd)
    log = p.read_jsonl(feature / "tdd.jsonl")
    if phase == "red" and result["exit"] == 0:
        fail(f"tests passed; a red step must fail first ({cmd})", **result)
    if phase == "green":
        if not any(e["phase"] == "red" and e["step"] == step for e in log):
            fail(f"no red run recorded for step {step!r}; run `build red {step}` first")
        if result["exit"] != 0:
            fail("tests still failing; fix the code, not the tests", **result)
    entry = {"phase": phase, "step": step, "exit": result["exit"], "ts": p.today()}
    p.append_jsonl(feature / "tdd.jsonl", entry)
    return {
        "ok": True,
        "phase": phase,
        "step": step,
        "cycles": cycles(log + [entry]),
        "tail": result["tail"],
    }


def planned_files(feature: Path) -> list[str]:
    plan = feature / "plan.md"
    return (
        a.list_items(a.sections(plan.read_text()).get("Files that change", ""))
        if plan.exists()
        else []
    )


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
    return {"ok": True, "planned": planned, "unplanned": []}


def fix(feature: Path, state: str) -> dict:
    lock = feature / ".fix-lock"
    on = state == "on"
    lock.touch() if on else lock.unlink(missing_ok=True)
    return {
        "ok": True,
        "fix_lock": on,
        "next": "test files are read-only while the lock is on" if on else "/sdlc:test",
    }
