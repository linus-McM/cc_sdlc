import shutil
import subprocess
from pathlib import Path

import pytest

from conftest import load
from sdlc import cli, project
from sdlc.project import git


@pytest.fixture
def tested(run, repo: Path, accepted_plan, toml_config):
    """Feature with a green TDD cycle, passing test-report and review.md."""
    toml_config(commands={"test": "exit 1"}, deploy={"rollback": "echo rolled-back"})
    run("build", "red", "s")
    toml_config(commands={"test": "exit 0"}, deploy={"rollback": "echo rolled-back"})
    run("build", "green", "s")
    assert run("test", "run")["ok"]
    (repo / "sdlc/feat/review.md").write_text("# R\n\n## Bugs\n- none\n\n## Security\n- none\n\n## Compliance\n- none\n")
    return "feat"


def test_deploy_check_blocks_without_test_report(run, accepted_plan):
    out = run("deploy", "check", "dev")
    assert out["ok"] is False and "test-report" in out["reason"]


def test_deploy_check_dev_is_free(run, tested):
    out = run("deploy", "check", "dev")
    assert out["ok"] and out["decision"] == "allow" and out["tier"] == "free"


def test_deploy_check_staging_asks(run, tested):
    assert run("deploy", "check", "staging")["decision"] == "ask"


def test_deploy_check_production_gate(run, repo: Path, tested, monkeypatch):
    monkeypatch.delenv("RELEASE_APPROVAL", raising=False)
    out = run("deploy", "check", "production")
    assert out["ok"] is False and out["decision"] == "blocked"
    assert any("rollback" in r for r in out["reasons"])
    assert any("RELEASE_APPROVAL" in r for r in out["reasons"])
    assert run("deploy", "rehearse")["ok"]
    monkeypatch.setenv("RELEASE_APPROVAL", "rm")
    out = run("deploy", "check", "production")
    assert out["ok"] and out["decision"] == "allow" and out["approver"] == "rm"


def test_deploy_rehearse_records_rollback(run, repo: Path, tested):
    out = run("deploy", "rehearse")
    assert out["ok"] and out["tail"] == "rolled-back"
    assert load(repo / "sdlc/feat/deploy.json")["rollback"]["exit"] == 0


def test_deploy_rehearse_runs_in_throwaway_worktree(run, repo: Path, tested, toml_config):
    toml_config(commands={"test": "exit 0"}, deploy={"rollback": "git revert --no-edit HEAD"})
    head, status = git(repo, "rev-parse", "HEAD"), git(repo, "status", "--porcelain")
    out = run("deploy", "rehearse")
    assert out["ok"] and out["exit"] == 0 and "Revert" in out["tail"]
    assert git(repo, "rev-parse", "HEAD") == head
    assert git(repo, "status", "--porcelain") == status
    assert len(git(repo, "worktree", "list").splitlines()) == 1


def test_deploy_rehearse_needs_git(run, repo: Path, tested):
    shutil.rmtree(repo / ".git")
    out = run("deploy", "rehearse")
    assert out["ok"] is False and "not a git repository" in out["reason"]


def test_deploy_rehearse_reports_leftover_worktree(run, repo: Path, tested, monkeypatch):
    real = project.run_git

    def flaky(root, *args):
        if args[:2] == ("worktree", "remove"):
            return subprocess.CompletedProcess(args, 1, stdout="", stderr="boom")
        return real(root, *args)

    monkeypatch.setattr(project, "run_git", flaky)
    out = run("deploy", "rehearse")
    assert out["ok"] is False and "boom" in out["reason"] and "git worktree prune" in out["reason"]
    rollback = load(repo / "sdlc/feat/deploy.json")["rollback"]
    assert rollback["exit"] == 0 and "git worktree prune" in rollback["leftover"]


def test_deploy_rehearse_runs_at_project_path(repo: Path, tested, toml_config):
    """A project that is a subdirectory of the repo rehearses at that same subdirectory in the worktree."""
    toml_config(commands={"test": "exit 0"}, deploy={"rollback": "pwd"})
    app = repo / "app"
    app.mkdir()
    for name in (".sdlc.toml", "sdlc"):
        (repo / name).rename(app / name)
    git(repo, "add", "-A")
    out = cli.main(["deploy", "rehearse"], root=app)  # app/ not committed yet: no such path at HEAD
    assert out["ok"] is False and "app" in out["reason"] and "HEAD" in out["reason"]
    assert len(git(repo, "worktree", "list").splitlines()) == 1
    git(repo, "commit", "-qm", "move project under app/")
    out = cli.main(["deploy", "rehearse"], root=app)
    assert out["ok"] and out["tail"].endswith("/app"), out


def test_deploy_rehearse_fails_when_no_rollback_configured(run, tested, toml_config):
    toml_config(commands={"test": "exit 0"})
    assert run("deploy", "rehearse")["ok"] is False


def test_deploy_record_appends_history(run, repo: Path, tested, monkeypatch):
    monkeypatch.setenv("RELEASE_APPROVAL", "rm")
    run("deploy", "rehearse")
    out = run("deploy", "record", "production")
    assert out["ok"]
    history = load(repo / "sdlc/feat/deploy.json")["deployments"]
    assert history[0]["env"] == "production" and history[0]["approver"] == "rm"
    assert len(history[0]["sha"]) >= 7


def test_deploy_pr_writes_body_from_artifacts(run, repo: Path, tested):
    out = run("deploy", "pr")
    body = (repo / "sdlc/feat/pr-body.md").read_text()
    assert out["ok"] and out["path"].endswith("pr-body.md")
    for token in ("intent.md", "spec.md", "plan.md", "test-report", "Important: 0"):
        assert token in body


def test_deploy_unknown_env_rejected(run, tested):
    assert run("deploy", "check", "moon")["ok"] is False


def test_pr_body_has_knowledge_section(run, repo: Path, tested, knowledge):
    import subprocess

    body = repo / "sdlc/feat/pr-body.md"
    run("deploy", "pr")
    text = body.read_text()
    assert "### Knowledge" in text and "no knowledge changes" in text  # no bundle diff against main yet
    subprocess.run(["git", "branch", "-m", "main", "trunk"], cwd=repo, check=True)
    run("deploy", "pr")
    assert "diff unavailable" in body.read_text().split("### Knowledge", 1)[1]  # a git error is not "no changes"
    subprocess.run(["git", "branch", "-m", "trunk", "main"], cwd=repo, check=True)
    subprocess.run(["git", "checkout", "-qb", "feature"], cwd=repo, check=True)
    run("knowledge", "bootstrap")
    subprocess.run(["git", "add", "-A"], cwd=repo, check=True)
    subprocess.run(["git", "commit", "-qm", "bundle"], cwd=repo, check=True)
    run("deploy", "pr")
    text = body.read_text().split("### Knowledge", 1)[1]
    assert "sdlc/knowledge/index.md" in text and "sdlc/knowledge/features/feat.md" in text


def test_templates_and_config_carry_knowledge_bands_and_evals():
    import json
    import tomllib

    from sdlc import project as p

    repo = p.PLUGIN_ROOT.parent  # the plugin ships under plugin/; dogfood output lives on the dogfood branch only
    metrics = tomllib.loads((p.PLUGIN_ROOT / "templates/bands.toml").read_text())["metrics"]
    assert metrics["knowledge_stale"]["bad"] == "high" and metrics["knowledge_behind"]["bad"] == "high"
    evals = json.loads((p.PLUGIN_ROOT / "templates/evals/knowledge-questions.json").read_text())
    assert len(evals["questions"]) == 5 and all({"question", "check"} <= set(q) for q in evals["questions"])
    ignored = (repo / ".gitignore").read_text().splitlines()
    assert "graphify-out/" in ignored
    conf = tomllib.loads((repo / ".sdlc.toml").read_text())
    package_only = "sdlc/" in ignored  # dev/main; the dogfood branch tracks sdlc/ and runs both layers
    assert conf["knowledge"]["enabled"] is not package_only and conf["docs"]["enabled"] is not package_only
    assert conf["commands"]["build"].startswith("claude plugin validate --strict plugin")
    version = json.loads((p.PLUGIN_ROOT / ".claude-plugin/plugin.json").read_text())["version"]  # CI bumps it; the three files must agree
    market = json.loads((repo / ".claude-plugin/marketplace.json").read_text())["plugins"][0]
    assert market["version"] == version and market["source"] == {"source": "git-subdir", "url": "https://github.com/linus-McM/cc_sdlc.git", "path": "plugin", "ref": "main"}
