"""Deploy-stage mechanics: per-environment tiers, rollback rehearsal, release record, PR body."""

from __future__ import annotations

import os
import tempfile
from pathlib import Path

from . import artifacts as a
from . import build, knowledge, testing
from . import project as p
from .project import Blocked, fail

TIERS = ("free", "ask", "gate")


def state(feature: Path) -> dict:
    return p.read_json(feature / "deploy.json", {"deployments": []})


def released(feature: Path) -> bool:
    return any(d["env"] == "production" for d in state(feature)["deployments"])


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


def approver() -> str:
    """The named release manager from RELEASE_APPROVAL, or empty."""
    return os.environ.get("RELEASE_APPROVAL", "")


def gated(cfg: dict) -> list[str]:
    """Environments at the `gate` tier in a `[deploy]` config table."""
    return [env for env, tier in cfg["environments"].items() if tier == "gate"]


def check(root: Path, feature: Path, env: str) -> dict:
    cfg = p.config(root)["deploy"]
    tier = cfg["environments"].get(env)
    if tier not in TIERS:
        fail(f"unknown environment {env!r}; known: {sorted(cfg['environments'])}")
    reasons = readiness(feature)
    approver_name = approver()
    if tier == "gate":
        if not cfg["rollback"]:
            reasons.append("no rollback command in .sdlc.toml deploy.rollback")
        elif "rollback" not in state(feature):
            reasons.append("rollback not rehearsed; run `deploy rehearse` in staging first")
        if not approver_name:
            reasons.append("RELEASE_APPROVAL unset; a named release manager must authorize production")
    if reasons:
        fail("; ".join(reasons), env=env, tier=tier, decision="blocked", reasons=reasons)
    decision = "ask" if tier == "ask" else "allow"
    return {
        "ok": True,
        "env": env,
        "tier": tier,
        "decision": decision,
        "approver": approver_name or p.author(root),
    }


def rehearse(root: Path, feature: Path) -> dict:
    """Run deploy.rollback in a throwaway detached worktree of HEAD; the checkout itself is never touched."""
    cmd = p.config(root)["deploy"]["rollback"]
    if not cmd:
        fail("no rollback command in .sdlc.toml deploy.rollback")
    prefix = p.git(root, "rev-parse", "--show-prefix")  # the project's path inside the repo, "" at the top
    with tempfile.TemporaryDirectory(prefix="sdlc-rehearsal-", ignore_cleanup_errors=True) as tmp:
        added = p.run_git(root, "worktree", "add", "--detach", tmp, "HEAD")
        if added.returncode != 0:
            fail(f"rollback rehearsal could not create a worktree: {added.stderr.strip()}")
        cwd = Path(tmp) / prefix
        missing = not cwd.is_dir()
        result = None if missing else build.run_cmd(cwd, cmd)
        removed = p.run_git(root, "worktree", "remove", "--force", tmp)
    if missing:
        fail(f"project path {prefix or '.'} does not exist at HEAD; commit it before rehearsing")
    if removed.returncode != 0:
        result["leftover"] = f"worktree entry not removed ({removed.stderr.strip()}); run `git worktree prune`"
    p.write_json(feature / "deploy.json", {**state(feature), "rollback": {**result, "ts": p.today()}})
    if result["exit"] != 0:
        fail("rollback rehearsal failed", **result)
    if "leftover" in result:
        fail(f"rollback rehearsed, but the {result['leftover']}", **result)
    return {"ok": True, **result}


def record(root: Path, feature: Path, env: str) -> dict:
    verdict = check(root, feature, env)
    data = state(feature)
    entry = {
        "env": env,
        "ts": p.today(),
        "sha": p.head_commit(root),
        "approver": verdict["approver"],
    }
    data["deployments"].append(entry)
    p.write_json(feature / "deploy.json", data)
    return {
        "ok": True,
        **entry,
        "next": "/sdlc:maintain" if env == "production" else "deploy to the next environment",
    }


def knowledge_diff(root: Path) -> str:
    """`git diff --stat main...HEAD` for the OKF bundle, so reviewers see what the change taught the knowledge base."""
    if not knowledge.enabled(root):
        return "knowledge layer off"
    bundle = knowledge.cfg(root)["bundle"]
    result = p.run_git(root, "diff", "--stat", "main...HEAD", "--", bundle)
    if result.returncode != 0:
        return f"diff unavailable: {result.stderr.strip().splitlines()[-1] if result.stderr.strip() else 'git diff failed'}"
    stat = result.stdout.strip()
    return f"```\n{stat}\n```" if stat else f"no knowledge changes under {bundle} against main"


def pr_body(root: Path, feature: Path) -> dict:
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
            "### Knowledge",
            knowledge_diff(root),
            "",
        ]
    )
    path = feature / "pr-body.md"
    path.write_text(body)
    return {"ok": True, "path": str(path), "next": f"gh pr create --body-file {path}"}
