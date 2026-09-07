"""Deploy-stage mechanics: per-environment tiers, rollback rehearsal, release record, PR body."""

from __future__ import annotations

import os
from pathlib import Path

from . import artifacts as a
from . import build, testing
from . import project as p
from .project import Blocked, fail

TIERS = ("free", "ask", "gate")


def state(feature: Path) -> dict:
    return p.read_json(feature / "deploy.json", {"deployments": []})


def readiness(feature: Path) -> list[str]:
    """Reasons the feature is not ready for any environment; empty when ready."""
    reasons = []
    rep = testing.report(feature)
    if rep is None:
        reasons.append("test-report.json missing; run `test run`")
    elif not rep["passed"]:
        reasons.append("test-report.json shows failures")
    try:
        testing.review(feature)
    except Blocked:
        reasons.append("review.md missing or incomplete; run `test review`")
    return reasons


def check(root: Path, feature: Path, env: str) -> dict:
    cfg = p.config(root)["deploy"]
    tier = cfg["environments"].get(env)
    if tier not in TIERS:
        fail(f"unknown environment {env!r}; known: {sorted(cfg['environments'])}")
    reasons = readiness(feature)
    approver = os.environ.get("RELEASE_APPROVAL", "")
    if tier == "gate":
        if not cfg["rollback"]:
            reasons.append("no rollback command in .sdlc.toml deploy.rollback")
        elif "rollback" not in state(feature):
            reasons.append("rollback not rehearsed; run `deploy rehearse` in staging first")
        if not approver:
            reasons.append(
                "RELEASE_APPROVAL unset; a named release manager must authorize production"
            )
    if reasons:
        fail("; ".join(reasons), env=env, tier=tier, decision="blocked", reasons=reasons)
    decision = "ask" if tier == "ask" else "allow"
    return {
        "ok": True,
        "env": env,
        "tier": tier,
        "decision": decision,
        "approver": approver or p.author(root),
    }


def rehearse(root: Path, feature: Path) -> dict:
    cmd = p.config(root)["deploy"]["rollback"]
    if not cmd:
        fail("no rollback command in .sdlc.toml deploy.rollback")
    result = build.run_cmd(root, cmd)
    p.write_json(
        feature / "deploy.json", {**state(feature), "rollback": {**result, "ts": p.today()}}
    )
    if result["exit"] != 0:
        fail("rollback rehearsal failed", **result)
    return {"ok": True, **result}


def record(root: Path, feature: Path, env: str) -> dict:
    verdict = check(root, feature, env)
    data = state(feature)
    entry = {
        "env": env,
        "ts": p.today(),
        "sha": p.git(root, "rev-parse", "HEAD"),
        "approver": verdict["approver"],
    }
    data["deployments"].append(entry)
    p.write_json(feature / "deploy.json", data)
    return {
        "ok": True,
        **entry,
        "next": "/sdlc:maintain" if env == "production" else "deploy to the next environment",
    }


def pr_body(feature: Path) -> dict:
    intent = (feature / "intent.md").read_text()
    rep = testing.report(feature) or {}
    try:
        rev = testing.review(feature)
    except Blocked:
        rev = {"important": "?", "nits": "?"}
    body = "\n".join(
        [
            f"## {a.title(intent)}",
            "",
            "### Why",
            a.sections(intent).get("Problem", ""),
            "",
            "### Artifacts",
            f"- sdlc/{feature.name}/intent.md, spec.md, plan.md (accepted)",
            f"- test-report: {'passed' if rep.get('passed') else 'missing/failed'}, tdd cycles: {rep.get('cycles', 0)}",
            f"- review: Important: {rev['important']}, Nit: {rev['nits']}",
            "",
            "### Proof",
            a.sections((feature / "plan.md").read_text()).get("Proof", ""),
            "",
        ]
    )
    path = feature / "pr-body.md"
    path.write_text(body)
    return {"ok": True, "path": str(path), "next": f"gh pr create --body-file {path}"}
