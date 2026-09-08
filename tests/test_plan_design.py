from pathlib import Path

from conftest import fill
from sdlc import stages
from sdlc.project import write_json


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
    assert out["next"] in stages.COMMANDS


def test_status_next_points_at_first_unaccepted_stage(run, accepted_intent):
    assert run("status")["next"] == "/sdlc:design"
    run("design", "new")
    assert run("status")["next"] == "/sdlc:design"


def test_status_next_before_any_acceptance(run):
    run("plan", "new", "Feat")
    assert run("status")["next"] == "/sdlc:plan"


def test_status_next_after_spec(run, accepted_spec):
    assert run("status")["next"] == "/sdlc:build"


def test_status_next_walks_test_deploy_maintain(run, repo: Path, accepted_plan):
    feature = repo / "sdlc/feat"
    assert run("status")["next"] == "/sdlc:test"
    write_json(feature / "test-report.json", {"passed": True})
    assert run("status")["next"] == "/sdlc:test"  # review.md still missing
    (feature / "review.md").write_text("# Review\n## Bugs\n- none\n## Security\n- none\n## Compliance\n- none\n")
    assert run("status")["next"] == "/sdlc:deploy"
    write_json(feature / "deploy.json", {"deployments": [{"env": "staging"}]})
    assert run("status")["next"] == "/sdlc:deploy"
    write_json(feature / "deploy.json", {"deployments": [{"env": "staging"}, {"env": "production"}]})
    assert run("status")["next"] == "/sdlc:maintain"


def test_status_next_agrees_with_deploy_gate_on_failed_report(run, repo: Path, accepted_plan):
    write_json(repo / "sdlc/feat/test-report.json", {"passed": False})
    (repo / "sdlc/feat/review.md").write_text("# Review\n## Bugs\n- none\n## Security\n- none\n## Compliance\n- none\n")
    assert run("status")["next"] == "/sdlc:test"


def test_status_reports_corrupt_json_as_verdict_not_traceback(run, repo: Path, accepted_plan):
    (repo / "sdlc/feat/test-report.json").write_text('{"passed": tr')
    out = run("status")
    assert out["ok"] is False
    assert "test-report.json" in out["reason"]


def test_accept_publishes_feature_concept(run, repo: Path, knowledge):
    from sdlc import knowledge as k

    out = run("plan", "new", "Feat")
    assert out["ok"] and out["knowledge"]["ok"] and out["knowledge"]["mode"] == "install"
    fill(
        repo / "sdlc/feat/intent.md",
        **{"Problem": "p", "Proposed outcome": "o", "Affected users and systems": "u", "Constraints": "c", "Open questions": "none"},
    )
    out = run("plan", "accept")
    assert out["ok"] and out["knowledge"]["actor"] == "human:t"
    front, _ = k.split_document((repo / "sdlc/knowledge/features/feat.md").read_text())
    assert front["status"] == "stable" and front["verified"] == [{"by": "human:t", "at": front["verified"][0]["at"]}]
    assert "accepted" in front["tags"]
