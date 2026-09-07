from pathlib import Path

from conftest import fill


def test_plan_new_creates_intent_from_template(run, repo: Path):
    out = run("plan", "new", "Claims status self-service")
    path = repo / "sdlc" / "claims-status-self-service" / "intent.md"
    assert out["ok"] and out["slug"] == "claims-status-self-service"
    assert path.exists()
    text = path.read_text()
    assert text.startswith("# Intent: Claims status self-service")
    for h in (
        "Problem",
        "Proposed outcome",
        "Affected users and systems",
        "Constraints",
        "Open questions",
    ):
        assert f"## {h}" in text


def test_plan_new_refuses_duplicate(run):
    run("plan", "new", "Dup")
    assert run("plan", "new", "Dup")["ok"] is False


def test_plan_check_fails_on_placeholders_then_passes(run, repo: Path):
    run("plan", "new", "Feat")
    assert run("plan", "check")["ok"] is False
    fill(
        repo / "sdlc/feat/intent.md",
        **{
            "Problem": "p",
            "Proposed outcome": "o",
            "Affected users and systems": "u",
            "Constraints": "c",
            "Open questions": "none",
        },
    )
    assert run("plan", "check")["ok"] is True


def test_plan_accept_requires_valid_intent_and_sets_status(run, repo: Path):
    run("plan", "new", "Feat")
    assert run("plan", "accept")["ok"] is False
    fill(
        repo / "sdlc/feat/intent.md",
        **{
            "Problem": "p",
            "Proposed outcome": "o",
            "Affected users and systems": "u",
            "Constraints": "c",
            "Open questions": "none",
        },
    )
    out = run("plan", "accept")
    assert out["ok"] and out["next"] == "/sdlc:design"
    assert "Status: accepted" in (repo / "sdlc/feat/intent.md").read_text()


def test_design_gate_blocks_until_intent_accepted(run, repo: Path, accepted_intent):
    assert run("design", "new")["ok"] is True
    spec = repo / "sdlc/feat/spec.md"
    assert spec.exists()
    for h in ("Requirements", "Design", "Concerns", "Open questions", "Proof"):
        assert f"## {h}" in spec.read_text()


def test_design_new_blocked_without_accepted_intent(run):
    run("plan", "new", "Feat")
    out = run("design", "new")
    assert out["ok"] is False and "intent.md" in out["reason"]


def test_design_accept_flow(run, repo: Path, accepted_intent):
    run("design", "new")
    assert run("design", "accept")["ok"] is False
    fill(
        repo / "sdlc/feat/spec.md",
        Requirements="r",
        Design="d",
        Concerns="none",
        **{"Open questions": "none", "Proof": "tests/test_feat.py"},
    )
    out = run("design", "accept")
    assert out["ok"] and out["next"] == "/sdlc:build"


def test_status_reports_stage_progress(run, repo: Path, accepted_intent):
    out = run("status")
    assert out["slug"] == "feat"
    assert out["artifacts"]["intent.md"] == "accepted"
    assert out["artifacts"]["spec.md"] == "missing"
