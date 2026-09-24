"""Stage-boundary checkpoints: every accepted artifact lands in its own commit."""

from pathlib import Path

from conftest import BASE, INTENT_BODY, PLAN_BODY, SPEC_BODY, fill, series
from sdlc import checkpoint
from sdlc import project as p

REVIEW = "# Review\n\n## Bugs\n- none\n\n## Security\n- none\n\n## Compliance\n- Nit: name\n"


def subjects(repo: Path) -> list[str]:
    return p.git(repo, "log", "--format=%s").splitlines()


def files_in(repo: Path) -> list[str]:
    return sorted(p.git(repo, "show", "--name-only", "--format=", "HEAD").split())


def test_plan_accept_commits_the_intent(run, repo: Path, checkpoint_on, accepted_intent):
    assert subjects(repo)[0] == "plan(feat): accept — intent.md (+1 file)"  # .sdlc.toml, written by `plan new`, rides along
    assert files_in(repo) == [".sdlc.toml", "sdlc/feat/intent.md"]
    assert p.changed_files(repo) == []


def test_each_accept_is_its_own_commit(run, repo: Path, checkpoint_on, accepted_plan):
    assert subjects(repo)[:3] == [
        "build(feat): accept — plan.md",
        "design(feat): accept — spec.md",
        "plan(feat): accept — intent.md (+1 file)",
    ]


def test_extra_generated_files_ride_along_and_are_counted(run, repo: Path, checkpoint_on, accepted_spec):
    run("build", "new")
    (repo / "sdlc/feat/notes.md").write_text("scratch\n")  # a second generated file, same boundary
    fill(repo / "sdlc/feat/plan.md", **PLAN_BODY)
    assert run("build", "accept")["ok"]
    assert subjects(repo)[0] == "build(feat): accept — plan.md (+1 file)"
    assert files_in(repo) == ["sdlc/feat/notes.md", "sdlc/feat/plan.md"]


def test_source_changes_are_never_swept_in(run, repo: Path, checkpoint_on, accepted_intent):
    (repo / "src.py").write_text("half finished\n")
    run("design", "new")
    fill(repo / "sdlc/feat/spec.md", **SPEC_BODY)
    assert run("design", "accept")["ok"]
    assert files_in(repo) == ["sdlc/feat/spec.md"]
    assert p.changed_files(repo) == ["src.py"]


def test_staged_unrelated_work_stays_staged(run, repo: Path, checkpoint_on, accepted_intent):
    (repo / "src.py").write_text("staged\n")
    p.run_git(repo, "add", "src.py")
    run("design", "new")
    fill(repo / "sdlc/feat/spec.md", **SPEC_BODY)
    assert run("design", "accept")["ok"]
    assert files_in(repo) == ["sdlc/feat/spec.md"]
    assert p.git(repo, "diff", "--cached", "--name-only") == "src.py"


def test_review_deploy_and_maintain_are_boundaries(run, repo: Path, checkpoint_on, accepted_plan):
    (repo / "sdlc/feat/review.md").write_text(REVIEW)
    assert run("test", "review")["ok"]
    assert subjects(repo)[0] == "test(feat): review — review.md"

    fill(repo / "sdlc/feat/plan.md", Proof="done")
    p.write_json(repo / "sdlc/feat/test-report.json", {"ok": True, "passed": ["test"]})
    assert run("deploy", "record", "dev")["ok"]
    assert subjects(repo)[0] == "deploy(feat): record dev — deploy.json (+2 files)"  # the edited plan.md and test-report.json

    assert run("maintain", "lesson", "cache bug")["ok"]
    assert subjects(repo)[0] == "maintain: lesson — lessons.md"  # a file directly under sdlc/ has no feature scope


def test_propose_commits_the_next_intent(run, repo: Path, checkpoint_on):
    series(repo, "ci_test_failure_rate", [*BASE, 20.0])
    out = run("maintain", "propose", "ci_test_failure_rate")
    assert out["ok"]
    assert subjects(repo)[0].startswith(f"maintain({out['slug']}): propose — intent.md")
    assert f"sdlc/{out['slug']}/intent.md" in files_in(repo)


def test_nothing_to_commit_is_not_an_error(repo: Path, checkpoint_on):
    before = subjects(repo)
    out = checkpoint.commit(repo, "plan", "accept", repo / "sdlc/feat/intent.md")
    assert out["ok"] is True and out["committed"] is False
    assert subjects(repo) == before


def test_layer_off_never_commits(run, repo: Path, accepted_intent):
    assert subjects(repo) == ["init"]  # the `repo` fixture sets SDLC_CHECKPOINT=off
    assert "sdlc/feat/intent.md" in p.changed_files(repo)


def test_config_can_disable_the_layer(run, repo: Path, checkpoint_on, toml_config):
    toml_config(checkpoint={"enabled": False})
    run("plan", "new", "Feat")
    fill(repo / "sdlc/feat/intent.md", **INTENT_BODY)
    assert run("plan", "accept")["ok"]
    assert subjects(repo) == ["init"]


def test_a_failed_commit_never_fails_the_stage(run, repo: Path, checkpoint_on, monkeypatch):
    run("plan", "new", "Feat")
    fill(repo / "sdlc/feat/intent.md", **INTENT_BODY)
    real = p.run_git
    monkeypatch.setattr(p, "run_git", lambda root, *args: p.run_cmd(root, ["git", "no-such-command"]) if args[0] == "commit" else real(root, *args))
    out = run("plan", "accept")
    assert out["ok"] is True and out["status"] == "accepted"
    assert out["checkpoint"]["ok"] is False


def test_a_merge_in_progress_defers_the_checkpoint(repo: Path, checkpoint_on):
    (repo / "sdlc/feat").mkdir(parents=True)
    (repo / "sdlc/feat/intent.md").write_text("x\n")
    (repo / ".git/MERGE_HEAD").write_text(p.head_commit(repo) + "\n")
    out = checkpoint.commit(repo, "plan", "accept", repo / "sdlc/feat/intent.md")
    assert out["committed"] is False and "in progress" in out["reason"]
    assert subjects(repo) == ["init"]
