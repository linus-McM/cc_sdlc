"""Session handover: each stage boundary leaves sdlc/<slug>/HANDOVER.md so a fresh session can pick the feature up."""

from pathlib import Path

from conftest import INTENT_BODY, SPEC_BODY, fill
from sdlc import project as p

HANDOVER = "sdlc/feat/HANDOVER.md"
RESUME = "To resume in a fresh session, read this file and the artifact above."


def test_accept_writes_the_handover(run, repo: Path):
    run("plan", "new", "Feat")
    fill(repo / "sdlc/feat/intent.md", **INTENT_BODY)
    out = run("plan", "accept")
    assert out["handover"] == HANDOVER
    lines = (repo / HANDOVER).read_text().splitlines()
    assert lines[0] == "# Handover: Feat"
    assert any("plan accept" in line for line in lines)
    assert any("sdlc/feat/intent.md" in line for line in lines)
    assert any("/sdlc:design" in line for line in lines)
    assert lines[-1] == RESUME
    assert len(lines) < 25


def test_open_items_come_from_spec_concerns(run, repo: Path, accepted_intent):
    run("design", "new")
    fill(repo / "sdlc/feat/spec.md", **{**SPEC_BODY, "Concerns": "- PII in logs: redacted at the logger"})
    assert run("design", "accept")["ok"]
    text = (repo / HANDOVER).read_text()
    assert "PII in logs: redacted at the logger" in text
    assert "/sdlc:build" in text


def test_review_overwrites_with_findings(run, repo: Path, accepted_plan):
    (repo / "sdlc/feat/review.md").write_text("# Review\n\n## Bugs\n- none\n\n## Security\n- none\n\n## Compliance\n- R1: met, tests/test_feat.py\n- Nit: name\n")
    assert run("test", "review")["handover"] == HANDOVER
    text = (repo / HANDOVER).read_text()
    assert "test review" in text and "plan accept" not in text
    assert "Nit: name" in text
    assert "complete: the feature is built, tested and reviewed" in text and "/sdlc:deploy is optional" in text


def test_handover_lands_in_the_checkpoint_commit(run, repo: Path, checkpoint_on, accepted_intent):
    assert HANDOVER in p.git(repo, "show", "--name-only", "--format=", "HEAD").split()


def test_non_handover_boundaries_write_nothing(run, repo: Path):
    assert "handover" not in run("maintain", "lesson", "cache bug")
    assert not list((repo / "sdlc").glob("*/HANDOVER.md"))


def test_handover_can_be_turned_off(run, repo: Path, toml_config):
    toml_config(checkpoint={"handover": False})
    run("plan", "new", "Feat")
    fill(repo / "sdlc/feat/intent.md", **INTENT_BODY)
    out = run("plan", "accept")
    assert out["ok"] and "handover" not in out
    assert not (repo / HANDOVER).exists()


def test_a_failed_handover_does_not_fail_the_boundary(run, repo: Path):
    run("plan", "new", "Feat")
    fill(repo / "sdlc/feat/intent.md", **INTENT_BODY)
    (repo / HANDOVER).mkdir()  # a directory in the way: the write fails
    out = run("plan", "accept")
    assert out["ok"]
    assert out["handover"]["ok"] is False
