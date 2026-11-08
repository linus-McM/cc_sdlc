"""Stage workflows: the catalog of plugin Workflow scripts and the env that turns the Workflow tool on.

Each stage ships one `workflows/<name>.js` (invoked as `sdlc:<name>`). Plugin settings cannot set
env, so `env` merges `[workflows.env]` into the project's `.claude/settings.local.json` (never
overwriting a value the user set) and exports it to `CLAUDE_ENV_FILE` when a SessionStart hook
provides one. Only CLAUDE_CODE_WORKFLOW* keys, only in projects with a .sdlc.toml. Off switches: `[workflows] enabled = false`, `auto_env = false`, SDLC_WORKFLOWS=off.
"""

from __future__ import annotations

import json
import os
import re
import shlex
from pathlib import Path

from . import artifacts as a
from . import project as p

DIR = p.PLUGIN_ROOT / "workflows"
SETTINGS = ".claude/settings.local.json"
KEY = re.compile(r"CLAUDE_CODE_WORKFLOW[A-Z0-9_]*")  # a checked-in .sdlc.toml must not reach PATH, NODE_OPTIONS or the shell
CATALOG = {
    "plan": "intent-scout",
    "design": "design-panel",
    "build": "plan-critic",
    "test": "review",
    "deploy": "release-readiness",
    "maintain": "diagnose",
}
RISKS = ("low", "medium", "high")


def enabled(root: Path) -> bool:
    return os.environ.get("SDLC_WORKFLOWS") != "off" and bool(p.config(root)["workflows"]["enabled"])


def meta(text: str) -> dict:
    """The script's `export const meta` literal (written as JSON so Python can read it); phases as titles."""
    found = re.search(r"^export const meta = (\{.*?^\})", text, re.M | re.S)
    data = json.loads(found.group(1)) if found else p.fail("workflow script has no `export const meta = {...}` block")
    return {**data, "phases": [ph["title"] for ph in data.get("phases", [])]}


def catalog(root: Path) -> dict:
    return {"ok": True, "enabled": enabled(root), "workflows": {stage: f"sdlc:{name}" for stage, name in CATALOG.items()}}


def gate(root: Path, stage: str | None, slug: str | None) -> dict:
    """Whether `stage` runs its workflow for this feature: intent.md's Risk must meet `[workflows.min_risk]`."""
    if stage not in CATALOG:
        return p.fail(f"unknown stage {stage!r}; expected one of {', '.join(CATALOG)}")
    if stage == "maintain" and not slug and not p.features(root):
        risk, note = "high", "no feature: diagnose runs on a band breach"
    else:
        found = a.meta((p.feature(root, slug) / "intent.md").read_text(), "Risk") or "low"
        risk, note = (found, f"intent.md Risk: {found}") if found in RISKS else ("high", f"unknown intent.md Risk {found!r}, treated as high")
    floor = p.config(root)["workflows"]["min_risk"][stage]
    on = enabled(root)
    run = on and RISKS.index(risk) >= RISKS.index(floor if floor in RISKS else "high")
    why = "workflows are off" if not on else (f"meets min_risk {floor}" if run else f"below min_risk {floor}: do the step inline")
    return {"ok": True, "stage": stage, "workflow": f"sdlc:{CATALOG[stage]}", "run": run, "risk": risk, "min_risk": floor, "reason": f"{note}; {why}"}


def env(root: Path) -> dict:
    """Merge `[workflows.env]` into the local settings; report which keys were written and which the user kept."""
    conf = p.config(root)["workflows"]
    if not (enabled(root) and conf["auto_env"] and (root / p.CONFIG_NAME).exists()):
        return {"ok": True, "written": [], "kept": [], "reason": "workflow env is off (or this is not an sdlc project)"}
    wanted = {key: str(value) for key, value in conf["env"].items()}
    if bad := [key for key in wanted if not KEY.fullmatch(key)]:
        return p.fail(f"[workflows.env] may only set CLAUDE_CODE_WORKFLOW* variables; refused: {', '.join(bad)}")
    path = root / SETTINGS
    data = p.read_json(path, {})
    current = data.get("env", {}) if isinstance(data, dict) else None
    if not isinstance(current, dict):
        return p.fail(f"{SETTINGS} is not a JSON object with an `env` object; fix it or set {', '.join(wanted)} yourself", path=str(path))
    merged = {**wanted, **current}  # a value the user set wins
    written = [key for key in wanted if key not in current]
    kept = [key for key in wanted if key in current and str(current[key]) != wanted[key]]
    if written:
        path.parent.mkdir(parents=True, exist_ok=True)
        p.write_json(path, {**data, "env": merged})
    export({key: str(merged[key]) for key in wanted})
    result = {"ok": True, "settings": SETTINGS, "written": written, "kept": kept}
    return {**result, "next": "restart Claude Code so the new env reaches the Workflow tool"} if written else result


def export(values: dict) -> None:
    """Append `export K=V` lines to the SessionStart env file, once each, so this session's Bash sees them."""
    if not (target := os.environ.get("CLAUDE_ENV_FILE")):
        return
    path = Path(target)
    have = path.read_text() if path.exists() else ""
    lines = [f"export {key}={shlex.quote(value)}" for key, value in values.items()]
    if missing := [line for line in lines if line not in have.splitlines()]:
        with path.open("a") as fh:
            fh.write("".join(line + "\n" for line in missing))
