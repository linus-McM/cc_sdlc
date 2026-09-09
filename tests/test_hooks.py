import json
from pathlib import Path

import pytest

from sdlc import hooks


@pytest.fixture(autouse=True)
def no_release_approval(monkeypatch):
    monkeypatch.delenv("RELEASE_APPROVAL", raising=False)


def edit(path: str) -> dict:
    return {"tool_name": "Edit", "tool_input": {"file_path": path}}


def bash(cmd: str) -> dict:
    return {"tool_name": "Bash", "tool_input": {"command": cmd}}


def denied(out) -> bool:
    return out is not None and out["hookSpecificOutput"]["permissionDecision"] == "deny"


def test_pre_edit_allows_ordinary_file(repo: Path):
    assert hooks.pre_edit(edit(str(repo / "src/x.py")), repo) is None


def test_hooks_ignore_paths_outside_root(run, repo: Path, accepted_plan, toml_config):
    toml_config(build={"protected_paths": ["**"]})
    outside = str(repo.parent / "elsewhere.py")
    assert hooks.pre_edit(edit(outside), repo) is None
    assert hooks.post_edit(edit(outside), repo) is None
    assert hooks.pre_edit(edit(str(repo / "inside.py")), repo) is not None
    assert hooks.pre_edit(edit(str(repo / "src/../inside.py")), repo) is not None
    assert hooks.pre_edit(edit(str(repo / "src/../../elsewhere.py")), repo) is None


def test_hooks_judge_symlinks_by_their_in_repo_name(repo: Path, toml_config):
    toml_config(build={"protected_paths": ["linked.py"]})
    (repo.parent / "outside_secret.py").write_text("x")
    (repo / "linked.py").symlink_to(repo.parent / "outside_secret.py")
    out = hooks.pre_edit(edit(str(repo / "linked.py")), repo)
    assert out is not None and "linked.py" in out["hookSpecificOutput"]["permissionDecisionReason"]


def test_pre_edit_blocks_protected_path(repo: Path, toml_config):
    toml_config(build={"protected_paths": ["src/gen/**"]})
    out = hooks.pre_edit(edit(str(repo / "src/gen/a.py")), repo)
    assert out["hookSpecificOutput"]["permissionDecision"] == "deny"
    assert "protected" in out["hookSpecificOutput"]["permissionDecisionReason"]


def test_pre_edit_blocks_tests_only_while_fix_lock(run, repo: Path, accepted_plan):
    test_file = str(repo / "tests/test_feat.py")
    assert hooks.pre_edit(edit(test_file), repo) is None
    run("build", "fix", "on")
    out = hooks.pre_edit(edit(test_file), repo)
    assert out["hookSpecificOutput"]["permissionDecision"] == "deny"
    assert hooks.pre_edit(edit(str(repo / "src/feat.py")), repo) is None


def test_pre_bash_production_gate(repo: Path, monkeypatch):
    assert denied(hooks.pre_bash(bash("make deploy ENV=production"), repo))
    monkeypatch.setenv("RELEASE_APPROVAL", "release-manager")
    assert hooks.pre_bash(bash("make deploy ENV=production"), repo) is None
    assert hooks.pre_bash(bash("make deploy ENV=staging"), repo) is None


def test_pre_bash_ignores_prose_and_heredocs(repo: Path):
    heredoc = "cat > sdlc/x/intent.md <<'EOF'\n# Intent\nwe deploy to production when it's ready\nEOF"
    assert hooks.pre_bash(bash(heredoc), repo) is None
    assert hooks.pre_bash(bash('git commit -m "deploy(x): ship production gate"'), repo) is None
    assert hooks.pre_bash(bash("python3 - <<'EOF'\nprint(\"deploy production\")\nEOF"), repo) is None
    two_heredocs = "cat <<A\ndeploy production\nA\ncat <<-'B'\n./deploy.sh production\n\tB\necho done"
    assert hooks.pre_bash(bash(two_heredocs), repo) is None


def test_pre_bash_scans_every_command_line_outside_heredocs(repo: Path):
    for cmd in (
        "./deploy.sh \\\n  production",
        "set -e\n./deploy.sh production",
        "uv run pytest -q\npython3 scripts/sdlc.py deploy check production",
        "./deploy.sh production;",
        "bin/deploy production/",
        "cat <<EOF\nnotes\nEOF\n./deploy.sh production",
    ):
        assert denied(hooks.pre_bash(bash(cmd), repo)), cmd


def test_pre_bash_fallback_matches_tokens_not_text(repo: Path):
    for cmd in ("./deploy.sh production", "python3 scripts/sdlc.py deploy record production", "make deploy ENV=Production", "deploy it's production"):
        assert denied(hooks.pre_bash(bash(cmd), repo)), cmd
    for cmd in ("./deploy.sh staging", "bin/deploy prod", "echo production", "deployment-notes production", "ls deploy production.txt", "\n\n"):
        assert hooks.pre_bash(bash(cmd), repo) is None, cmd
    reason = hooks.pre_bash(bash("./deploy.sh production"), repo)["hookSpecificOutput"]["permissionDecisionReason"]
    assert "deploy.check" in reason and "./deploy.sh" in reason


def test_pre_bash_denies_configured_release_command(repo: Path, monkeypatch, toml_config):
    toml_config(deploy={"command": "./release.sh {env}"})
    assert denied(hooks.pre_bash(bash("./release.sh production && echo done"), repo))
    assert hooks.pre_bash(bash("./release.sh staging"), repo) is None
    assert hooks.pre_bash(bash('git commit -m "./release.sh production"'), repo) is None  # quoted prose
    assert hooks.pre_bash(bash("cat <<EOF\n./release.sh production\nEOF"), repo) is None  # heredoc body
    # the token fallback still applies alongside the configured command
    assert denied(hooks.pre_bash(bash("./deploy.sh --force production"), repo))
    assert denied(hooks.pre_bash(bash("make deploy production"), repo))
    monkeypatch.setenv("RELEASE_APPROVAL", "release-manager")
    assert hooks.pre_bash(bash("./release.sh production"), repo) is None


def test_pre_bash_gated_names_come_from_config_only(repo: Path, toml_config):
    toml_config(**{"deploy.environments": {"prod": "gate", "production": "free"}})
    assert denied(hooks.pre_bash(bash("bin/deploy prod"), repo))
    assert hooks.pre_bash(bash("bin/deploy production"), repo) is None


def test_pre_bash_survives_bad_release_command_config(repo: Path, toml_config):
    toml_config(deploy={"command": './deploy.sh "{env}'})  # unbalanced quote
    assert hooks.pre_bash(bash("ls -la"), repo) is None
    assert denied(hooks.pre_bash(bash('./deploy.sh "production'), repo))
    toml_config(deploy={"command": "   "})
    assert hooks.pre_bash(bash("ls -la"), repo) is None
    assert denied(hooks.pre_bash(bash("./deploy.sh production"), repo))


def test_post_edit_warns_when_file_not_in_plan(run, repo: Path, accepted_plan):
    out = hooks.post_edit(edit(str(repo / "rogue.py")), repo)
    assert "plan.md" in out["hookSpecificOutput"]["additionalContext"]
    assert hooks.post_edit(edit(str(repo / "src/feat.py")), repo) is None
    assert hooks.post_edit(edit(str(repo / "sdlc/feat/plan.md")), repo) is None


def test_main_reads_stdin_and_prints_json(repo: Path, monkeypatch, capsys, toml_config):
    toml_config(build={"protected_paths": ["frozen/**"]})
    monkeypatch.setattr("sys.stdin", __import__("io").StringIO(json.dumps(edit(str(repo / "frozen/a.py")))))
    assert hooks.main(["pre-edit"], repo) == 0
    printed = json.loads(capsys.readouterr().out)
    assert printed["hookSpecificOutput"]["permissionDecision"] == "deny"


def test_session_start_context_lists_steps(repo: Path, knowledge, toml_config, monkeypatch):
    payload = {"hook_event_name": "SessionStart", "cwd": str(repo)}
    out = hooks.session_start(payload, repo)
    text = out["hookSpecificOutput"]["additionalContext"]
    assert out["hookSpecificOutput"]["hookEventName"] == "SessionStart"
    assert "graphify: missing" in text and "sdlc knowledge bootstrap" in text
    assert knowledge.calls() == []  # check-only by default: nothing installed from a session start
    toml_config(knowledge={"auto_install": True})
    out = hooks.session_start(payload, repo)
    text = out["hookSpecificOutput"]["additionalContext"]
    assert "graphify: installed" in text and "bundle: built" in text
    assert "uv tool install graphifyy" in knowledge.calls()
    assert "sdlc/knowledge/index.md" in text
    import subprocess

    def boom(*a, **kw):
        raise AssertionError("session start must not spawn a process on a healthy project")

    monkeypatch.setattr(subprocess, "run", boom)
    out = hooks.session_start(payload, repo)
    assert "all present" in out["hookSpecificOutput"]["additionalContext"] and "sdlc knowledge status" in out["hookSpecificOutput"]["additionalContext"]


def test_session_start_silent_when_disabled(repo: Path):
    assert hooks.session_start({"cwd": str(repo)}, repo) is None  # SDLC_KNOWLEDGE=off in the repo fixture


def test_post_bash_flags_stale_after_commit(run, repo: Path, knowledge, accepted_plan):
    import subprocess

    run("knowledge", "bootstrap")
    run("knowledge", "refresh")
    assert hooks.post_bash(bash("git commit -m x"), repo) is None  # nothing behind
    assert hooks.post_bash(bash("ls -la"), repo) is None
    for n in range(2):
        (repo / f"f{n}.txt").write_text("x\n")
        subprocess.run(["git", "add", "-A"], cwd=repo, check=True)
        subprocess.run(["git", "commit", "-qm", f"c{n}"], cwd=repo, check=True)
    assert hooks.post_bash(bash("ls -la"), repo) is None  # only a commit command triggers the look
    out = hooks.post_bash(bash("git -c user.name=t commit -qm done"), repo)
    text = out["hookSpecificOutput"]["additionalContext"]
    assert out["hookSpecificOutput"]["hookEventName"] == "PostToolUse"
    assert "bundle is 2 commits behind" in text and "sdlc knowledge refresh" in text


def test_post_edit_names_module_concepts(run, repo: Path, knowledge, accepted_plan):
    from test_knowledge import seed_sources

    seed_sources(repo)
    run("knowledge", "bootstrap")
    run("knowledge", "refresh")
    out = hooks.post_edit(edit(str(repo / "src/web/api.py")), repo)
    text = out["hookSpecificOutput"]["additionalContext"]
    assert "sdlc/knowledge/modules/api-py.md" in text and "plan.md" in text  # not in the plan either
    assert "modules/core-py.md" not in text
    shared = hooks.post_edit(edit(str(repo / "src/app/util.py")), repo)["hookSpecificOutput"]["additionalContext"]
    assert "modules/core-py.md" in shared and "modules/fmt.md" in shared  # a file spanning two communities names both
    assert hooks.post_edit(edit(str(repo / "unrelated.py")), repo)["hookSpecificOutput"]["additionalContext"].count("knowledge") == 0
