import json
import os
import subprocess
import sys
from pathlib import Path

import pytest

from conftest import REVIEW_OK
from sdlc import hooks
from sdlc import project as p


def edit(path: str) -> dict:
    return {"tool_name": "Edit", "tool_input": {"file_path": path}}


def bash(cmd: str) -> dict:
    return {"tool_name": "Bash", "tool_input": {"command": cmd}}


def asks(out) -> bool:
    """A release to a gated environment is put to the user, never denied: `deploy.check` is the gate."""
    return out is not None and out["hookSpecificOutput"]["permissionDecision"] == "ask"


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
    assert asks(hooks.pre_bash(bash("make deploy ENV=production"), repo))
    monkeypatch.setenv("RELEASE_APPROVAL", "release-manager")  # no named sign-off: the variable changes nothing
    assert asks(hooks.pre_bash(bash("make deploy ENV=production"), repo))
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
        assert asks(hooks.pre_bash(bash(cmd), repo)), cmd


def test_pre_bash_fallback_matches_tokens_not_text(repo: Path):
    for cmd in ("./deploy.sh production", "python3 scripts/sdlc.py deploy record production", "make deploy ENV=Production", "deploy it's production"):
        assert asks(hooks.pre_bash(bash(cmd), repo)), cmd
    for cmd in ("./deploy.sh staging", "bin/deploy prod", "echo production", "deployment-notes production", "ls deploy production.txt", "\n\n"):
        assert hooks.pre_bash(bash(cmd), repo) is None, cmd
    reason = hooks.pre_bash(bash("./deploy.sh production"), repo)["hookSpecificOutput"]["permissionDecisionReason"]
    assert "deploy.check" in reason and "./deploy.sh" in reason


def test_pre_bash_asks_about_a_configured_release_command(repo: Path, toml_config):
    toml_config(deploy={"command": "./release.sh {env}"})
    assert asks(hooks.pre_bash(bash("./release.sh production && echo done"), repo))
    assert hooks.pre_bash(bash("./release.sh staging"), repo) is None
    assert hooks.pre_bash(bash('git commit -m "./release.sh production"'), repo) is None  # quoted prose
    assert hooks.pre_bash(bash("cat <<EOF\n./release.sh production\nEOF"), repo) is None  # heredoc body
    # the token fallback still applies alongside the configured command
    assert asks(hooks.pre_bash(bash("./deploy.sh --force production"), repo))
    assert asks(hooks.pre_bash(bash("make deploy production"), repo))


def test_pre_bash_gated_names_come_from_config_only(repo: Path, toml_config):
    toml_config(**{"deploy.environments": {"prod": "gate", "production": "free"}})
    assert asks(hooks.pre_bash(bash("bin/deploy prod"), repo))
    assert hooks.pre_bash(bash("bin/deploy production"), repo) is None


def test_pre_bash_survives_bad_release_command_config(repo: Path, toml_config):
    toml_config(deploy={"command": './deploy.sh "{env}'})  # unbalanced quote
    assert hooks.pre_bash(bash("ls -la"), repo) is None
    assert asks(hooks.pre_bash(bash('./deploy.sh "production'), repo))
    toml_config(deploy={"command": "   "})
    assert hooks.pre_bash(bash("ls -la"), repo) is None
    assert asks(hooks.pre_bash(bash("./deploy.sh production"), repo))


def test_post_edit_warns_when_file_not_in_plan(run, repo: Path, accepted_plan):
    out = hooks.post_edit(edit(str(repo / "rogue.py")), repo)
    assert "plan.md" in out["hookSpecificOutput"]["additionalContext"]
    assert hooks.post_edit(edit(str(repo / "src/feat.py")), repo) is None
    assert hooks.post_edit(edit(str(repo / "sdlc/feat/plan.md")), repo) is None


def test_post_edit_drops_the_plan_note_once_the_feature_is_ready_to_deploy(run, repo: Path, accepted_plan):
    (repo / "sdlc/feat/test-report.json").write_text(json.dumps({"passed": True}))
    assert "plan.md" in hooks.post_edit(edit(str(repo / "rogue.py")), repo)["hookSpecificOutput"]["additionalContext"]  # review still owed
    (repo / "sdlc/feat/review.md").write_text(REVIEW_OK)
    assert hooks.post_edit(edit(str(repo / "rogue.py")), repo) is None


def test_main_judges_an_edit_by_the_worktree_that_holds_the_file(run, repo: Path, accepted_plan, monkeypatch, capsys):
    linked = repo / ".claude/worktrees/other"
    p.git(repo, "add", "-A")
    p.git(repo, "commit", "-qm", "plan")
    p.git(repo, "worktree", "add", "-q", "-b", "other", str(linked))

    def said(path: Path) -> str:
        monkeypatch.setattr("sys.stdin", __import__("io").StringIO(json.dumps(edit(str(path)))))
        assert hooks.main(["post-edit"], repo) == 0
        return capsys.readouterr().out

    assert said(linked / "src/feat.py") == ""  # planned, by its path inside the linked worktree
    assert '"rogue.py is not listed' in said(linked / "rogue.py")


def test_checkout_keeps_the_session_root_for_another_repository(repo: Path, tmp_path: Path):
    other = tmp_path / "another"
    (other / ".git").mkdir(parents=True)
    assert hooks.checkout(edit(str(other / "x.py")), repo) == repo
    assert hooks.checkout(edit(str(repo / "src/x.py")), repo) == repo
    assert hooks.checkout(bash("ls"), repo) == repo


def test_post_edit_says_each_note_once_per_file_per_session(run, repo: Path, accepted_plan):
    payload = {**edit(str(repo / "rogue.py")), "session_id": "s1"}
    assert "plan.md" in hooks.post_edit(payload, repo)["hookSpecificOutput"]["additionalContext"]
    assert hooks.post_edit(payload, repo) is None  # said once this session
    assert hooks.post_edit({**edit(str(repo / "other.py")), "session_id": "s1"}, repo) is not None  # another file still speaks
    assert hooks.post_edit({**payload, "session_id": "s2"}, repo) is not None  # a new session speaks again
    assert hooks.post_edit(edit(str(repo / "rogue.py")), repo) is not None  # no session id: no dedupe
    assert (repo / ".git/sdlc/hook-notes-s1.json").exists() and not list((repo / "sdlc").rglob("hook-notes-*"))


def test_post_edit_dedupe_survives_a_corrupt_state_file(run, repo: Path, accepted_plan):
    state = repo / ".git/sdlc/hook-notes-s1.json"
    state.parent.mkdir(parents=True, exist_ok=True)
    state.write_text("{not json")
    payload = {**edit(str(repo / "rogue.py")), "session_id": "s1"}
    assert "plan.md" in hooks.post_edit(payload, repo)["hookSpecificOutput"]["additionalContext"]


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
    assert "archify: skipped" in text  # SDLC_DOCS=off: the step does not apply, the session still starts
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


def test_session_start_repairs_a_stale_hook_block_without_auto_install(repo: Path, knowledge, toml_config, monkeypatch):
    from sdlc import project as p

    payload = {"hook_event_name": "SessionStart", "cwd": str(repo)}
    hook = repo / ".git/hooks/post-commit"
    hooks.session_start(payload, repo)
    assert not hook.exists()  # check-only: a project that never opted in gets no block from a session start
    toml_config(knowledge={"auto_install": True})
    hooks.session_start(payload, repo)
    toml_config(knowledge={"auto_install": False})
    hook.write_text(hook.read_text().replace(str(p.PLUGIN_ROOT), "/old/plugin/0.3.0"))  # the plugin moved or upgraded
    import subprocess

    def boom(*a, **kw):
        raise AssertionError("repairing the block rewrites a file; it never spawns a process")

    monkeypatch.setattr(subprocess, "run", boom)
    text = hooks.session_start(payload, repo)["hookSpecificOutput"]["additionalContext"]
    assert "/old/plugin/0.3.0" not in hook.read_text() and str(p.PLUGIN_ROOT) in hook.read_text()
    assert "all present" in text and "post-commit block repointed" in text


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
    again = {**edit(str(repo / "src/web/api.py")), "session_id": "s1"}
    assert "api-py.md" in hooks.post_edit(again, repo)["hookSpecificOutput"]["additionalContext"]
    assert hooks.post_edit(again, repo) is None  # both notes already said this session


HOOKS_JSON = json.loads((p.PLUGIN_ROOT / "hooks" / "hooks.json").read_text())["hooks"]


def shell_hook(event: str, matcher: str) -> str:
    return next(h["hooks"][0]["command"] for h in HOOKS_JSON[event] if h.get("matcher") == matcher)


@pytest.fixture
def hook_shell(tmp_path: Path, monkeypatch):
    """Run a hooks.json command line with a fake `uv` that records its arguments and stdin; returns (ran, stdin)."""
    project, bin_dir = tmp_path / "project", tmp_path / "bin"
    project.mkdir()
    bin_dir.mkdir()
    (bin_dir / "uv").write_text('#!/bin/sh\necho "$*" > "$(dirname "$0")/args"\ncat > "$(dirname "$0")/stdin"\n')
    (bin_dir / "uv").chmod(0o755)

    def _run(command: str, payload: dict, toml: str | None = "", **env: str) -> tuple[bool, str]:
        for name in ("args", "stdin"):
            (bin_dir / name).unlink(missing_ok=True)
        (project / ".sdlc.toml").unlink(missing_ok=True)
        if toml is not None:
            (project / ".sdlc.toml").write_text(toml)
        full = {**os.environ, "PATH": f"{bin_dir}:{os.environ['PATH']}", "HOME": str(tmp_path), "CLAUDE_PROJECT_DIR": str(project), "CLAUDE_PLUGIN_ROOT": "/plugin", **env}
        done = subprocess.run(["sh", "-c", command], input=json.dumps(payload), capture_output=True, text=True, env=full, check=False)
        assert done.returncode == 0, done.stderr
        ran = (bin_dir / "args").exists()
        return ran, (bin_dir / "stdin").read_text() if ran else ""

    return _run


def test_post_bash_shell_filter_starts_python_only_after_a_commit(hook_shell):
    command = shell_hook("PostToolUse", "Bash")
    assert hook_shell(command, bash("ls -la")) == (False, "")
    payload = bash("git commit -m 'x \"quoted\"'")
    ran, stdin = hook_shell(command, payload)
    assert ran and json.loads(stdin) == payload  # the hook JSON reaches Python unchanged
    assert hook_shell(command, payload, toml=None) == (False, "")  # not an sdlc project


@pytest.mark.parametrize(
    ("cmd", "toml", "env", "runs"),
    [
        ("ls -la", "", {}, False),
        ("ls -la", '[deploy]\ncommand = ""   # none\n', {}, False),
        ("./deploy.sh production", "", {}, True),
        ("./DEPLOY.sh production", "", {}, True),
        ("ls -la", '[deploy]\ncommand = "./ship {env}"\n', {}, True),
        ("ls -la", "[deploy]\ncommand = '''\n./ship {env}'''\n", {}, True),
        ("ls -la", 'deploy.command = "./ship {env}"\n', {}, True),
        ("./deploy.sh production", "", {"RELEASE_APPROVAL": "sam"}, True),
    ],
)
def test_pre_bash_shell_filter_is_a_superset_of_the_python_rule(hook_shell, cmd, toml, env, runs):
    ran, _ = hook_shell(shell_hook("PreToolUse", "Bash"), bash(cmd), toml, **env)
    assert ran is runs


def test_every_python_verdict_passes_the_shell_filter(hook_shell, repo: Path, toml_config):
    """Whatever `pre_bash` asks about must reach Python: the shell filter may only drop calls Python would allow."""
    toml_config(deploy={"command": "./ship {env}"})
    toml = (repo / ".sdlc.toml").read_text()
    for cmd in ("./ship production", "bash scripts/deploy.sh production", "make deploy ENV=production", "ENV=production ./deploy"):
        if hooks.pre_bash(bash(cmd), repo) is not None:
            assert hook_shell(shell_hook("PreToolUse", "Bash"), bash(cmd), toml)[0], cmd
    assert hooks.pre_bash(bash("./ship production"), repo) is not None


def test_hook_module_imports_stay_lazy():
    """Every handler pays only for what it uses: importing sdlc.hooks must not load the knowledge, docs or packs layers."""
    code = "import sys; sys.path.insert(0, sys.argv[1]); import sdlc.hooks; print(sorted(m for m in sys.modules if m.startswith('sdlc.')))"
    out = subprocess.run([sys.executable, "-c", code, str(p.PLUGIN_ROOT / "scripts")], capture_output=True, text=True, check=True).stdout
    assert json.loads(out.replace("'", '"')) == ["sdlc.artifacts", "sdlc.hooks", "sdlc.project"]
