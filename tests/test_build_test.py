import json
from pathlib import Path

from conftest import load


def test_build_new_gated_on_accepted_spec(run, accepted_intent):
    assert run("build", "new")["ok"] is False


def test_build_new_then_accept(run, repo: Path, accepted_plan):
    assert "Status: accepted" in (repo / "sdlc/feat/plan.md").read_text()


def test_build_red_records_failing_run_and_rejects_passing(run, repo: Path, accepted_plan, toml_config):
    toml_config(commands={"test": "exit 1"})
    out = run("build", "red", "step1")
    assert out["ok"] and out["phase"] == "red"
    toml_config(commands={"test": "exit 0"})
    out = run("build", "red", "step1")
    assert out["ok"] is False and "passed" in out["reason"]
    log = [json.loads(line) for line in (repo / "sdlc/feat/tdd.jsonl").read_text().splitlines()]
    assert [e["phase"] for e in log] == ["red"]


def test_build_green_requires_prior_red_and_passing_tests(run, repo: Path, accepted_plan, toml_config):
    toml_config(commands={"test": "exit 0"})
    assert run("build", "green", "step1")["ok"] is False  # no red first
    toml_config(commands={"test": "exit 1"})
    run("build", "red", "step1")
    assert run("build", "green", "step1")["ok"] is False  # still failing
    toml_config(commands={"test": "exit 0"})
    out = run("build", "green", "step1")
    assert out["ok"] and out["cycles"] == 1


def test_build_sync_flags_unplanned_files(run, repo: Path, accepted_plan):
    (repo / "src").mkdir()
    (repo / "src/feat.py").write_text("x")
    (repo / "rogue.py").write_text("x")
    out = run("build", "sync")
    assert out["ok"] is False
    assert out["unplanned"] == ["rogue.py"]
    (repo / "rogue.py").unlink()
    assert run("build", "sync")["ok"] is True


def test_build_sync_ignores_sdlc_artifacts_and_config(run, repo: Path, accepted_plan):
    assert run("build", "sync")["ok"] is True


def test_build_sync_keeps_unstaged_first_line_path_intact(run, repo: Path, accepted_plan):
    """` M path` is the first porcelain line; stripping its leading space mangled the path."""
    (repo / "README.md").write_text("changed\n")
    out = run("build", "sync")
    assert out["ok"] is False
    assert out["unplanned"] == ["README.md"]


def test_build_fix_toggles_lock(run, repo: Path, accepted_plan):
    assert run("build", "fix", "on")["ok"]
    assert (repo / "sdlc/feat/.fix-lock").exists()
    assert run("build", "fix", "off")["ok"]
    assert not (repo / "sdlc/feat/.fix-lock").exists()


def test_test_run_gated_on_accepted_plan(run, accepted_spec):
    assert run("test", "run")["ok"] is False


def test_test_run_requires_tdd_cycle(run, repo: Path, accepted_plan, toml_config):
    toml_config(commands={"test": "exit 0"})
    out = run("test", "run")
    assert out["ok"] is False and "red" in out["reason"]


def test_test_run_writes_report(run, repo: Path, accepted_plan, toml_config):
    toml_config(commands={"test": "exit 1"})
    run("build", "red", "s")
    toml_config(commands={"test": "echo ok", "lint": "echo lint"})
    run("build", "green", "s")
    out = run("test", "run")
    assert out["ok"] is True
    report = load(repo / "sdlc/feat/test-report.json")
    assert report["passed"] is True
    assert [r["name"] for r in report["results"]] == ["test", "lint"]
    assert report["results"][0]["tail"].strip() == "ok"


def test_test_run_failure_reported_not_hidden(run, repo: Path, accepted_plan, toml_config):
    toml_config(commands={"test": "exit 1"})
    run("build", "red", "s")
    toml_config(commands={"test": "exit 0"})
    run("build", "green", "s")
    toml_config(commands={"test": "echo boom; exit 3"})
    out = run("test", "run")
    assert out["ok"] is False and out["failed"] == ["test"]


def test_test_review_validates_findings_file(run, repo: Path, accepted_plan):
    assert run("test", "review")["ok"] is False
    (repo / "sdlc/feat/review.md").write_text("# Review\n\n## Bugs\n- none\n\n## Security\n- Important: PII in log (src/feat.py:3)\n\n## Compliance\n- Nit: name\n")
    out = run("test", "review")
    assert out["ok"] is True
    assert out["important"] == 1 and out["nits"] == 1
    assert out["next"] == "/sdlc:deploy"
