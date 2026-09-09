"""Continuous evals: run each evals/*.json prompt non-interactively, then its deterministic checks."""

from __future__ import annotations

import json
import os
import subprocess
from pathlib import Path

from . import build
from . import project as p
from .project import fail


def run_eval(root: Path, path: Path) -> dict:
    spec = json.loads(path.read_text())
    cmd = [
        os.environ.get("SDLC_CLAUDE_BIN", "claude"),
        "-p",
        spec["prompt"],
        "--output-format",
        "json",
    ]
    if spec.get("allowed_tools"):
        cmd += ["--allowedTools", ",".join(spec["allowed_tools"])]
    agent = subprocess.run(cmd, cwd=root, capture_output=True, text=True, check=False)
    checks = [build.run_cmd(root, c) for c in spec.get("checks", [])]
    passed = agent.returncode == 0 and all(c["exit"] == 0 for c in checks)
    return {"name": path.stem, "passed": passed, "agent_exit": agent.returncode, "checks": checks}


def run(root: Path) -> dict:
    suite = sorted((root / "evals").glob("*.json"))
    if not suite:
        fail("no evals/*.json found; write one per real task with its prompt and checks")
    results = [run_eval(root, e) for e in suite]
    rate = sum(r["passed"] for r in results) / len(results)
    threshold = p.config(root)["evals"]["threshold"]
    report = {"pass_rate": rate, "threshold": threshold, "results": results, "ts": p.today()}
    p.write_json(p.home(root, create=True) / "evals-report.json", report)
    if rate < threshold:
        fail(f"pass rate {rate:.2f} below threshold {threshold}", **report)
    return {"ok": True, **report}
