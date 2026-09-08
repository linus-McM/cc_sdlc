import json
from pathlib import Path

from sdlc import hooks


def edit(path: str) -> dict:
    return {"tool_name": "Edit", "tool_input": {"file_path": path}}


def bash(cmd: str) -> dict:
    return {"tool_name": "Bash", "tool_input": {"command": cmd}}


def test_pre_edit_allows_ordinary_file(repo: Path):
    assert hooks.pre_edit(edit(str(repo / "src/x.py")), repo) is None


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
    monkeypatch.delenv("RELEASE_APPROVAL", raising=False)
    out = hooks.pre_bash(bash("make deploy ENV=production"), repo)
    assert out["hookSpecificOutput"]["permissionDecision"] == "deny"
    monkeypatch.setenv("RELEASE_APPROVAL", "release-manager")
    assert hooks.pre_bash(bash("make deploy ENV=production"), repo) is None
    assert hooks.pre_bash(bash("make deploy ENV=staging"), repo) is None


def denied(out) -> bool:
    return out is not None and out["hookSpecificOutput"]["permissionDecision"] == "deny"


def test_pre_bash_ignores_prose_and_heredocs(repo: Path, monkeypatch):
    monkeypatch.delenv("RELEASE_APPROVAL", raising=False)
    heredoc = "cat > sdlc/x/intent.md <<'EOF'\n# Intent\nwe deploy to production when it's ready\nEOF"
    assert hooks.pre_bash(bash(heredoc), repo) is None
    assert hooks.pre_bash(bash('git commit -m "deploy(x): ship production gate"'), repo) is None
    assert hooks.pre_bash(bash("uv run pytest -q\npython3 scripts/sdlc.py deploy check production"), repo) is None
    assert hooks.pre_bash(bash("python3 - <<'EOF'\nprint(\"deploy production\")\nEOF"), repo) is None


def test_pre_bash_fallback_matches_tokens_not_text(repo: Path, monkeypatch):
    monkeypatch.delenv("RELEASE_APPROVAL", raising=False)
    for cmd in ("./deploy.sh production", "bin/deploy prod", "python3 scripts/sdlc.py deploy record production", "make deploy ENV=Production"):
        assert denied(hooks.pre_bash(bash(cmd), repo)), cmd
    for cmd in ("./deploy.sh staging", "echo production", "deployment-notes production", "ls deploy production.txt"):
        assert hooks.pre_bash(bash(cmd), repo) is None, cmd


def test_pre_bash_denies_configured_release_command(repo: Path, monkeypatch, toml_config):
    monkeypatch.delenv("RELEASE_APPROVAL", raising=False)
    toml_config(deploy={"command": "./release.sh {env}"})
    assert denied(hooks.pre_bash(bash("./release.sh production && echo done"), repo))
    assert hooks.pre_bash(bash("./release.sh staging"), repo) is None
    assert hooks.pre_bash(bash("./deploy.sh production"), repo) is None  # not the configured command
    monkeypatch.setenv("RELEASE_APPROVAL", "release-manager")
    assert hooks.pre_bash(bash("./release.sh production"), repo) is None


def test_pre_bash_reason_names_mechanic_gate(repo: Path, monkeypatch):
    monkeypatch.delenv("RELEASE_APPROVAL", raising=False)
    reason = hooks.pre_bash(bash("./deploy.sh production"), repo)["hookSpecificOutput"]["permissionDecisionReason"]
    assert "deploy.check" in reason and "./deploy.sh" in reason


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
