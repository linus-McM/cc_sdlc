"""Archify stage documents: [docs] config, render/check/open mechanics and the accept gates."""

from pathlib import Path

from sdlc import project

DISABLED = {"ok": True, "skipped": "docs disabled", "stage": "docs"}


def test_defaults_and_disabled_verdicts(run, repo: Path, toml_config, monkeypatch):
    conf = project.config(repo)["docs"]
    assert conf["enabled"] is True and conf["dir"] == "docs" and conf["quality"] == "showcase"
    assert conf["open"] is True and conf["min_node"] == 18 and conf["min_version"] == "2.17"
    assert conf["types"] == {
        "plan": "architecture",
        "design": "dataflow",
        "build": "workflow",
        "test": "sequence",
        "deploy": "lifecycle",
        "maintain": "lifecycle",
    }
    run("plan", "new", "Feat")
    for action in ("render", "check", "open"):
        assert run("docs", action, "plan") == DISABLED  # SDLC_DOCS=off from the repo fixture
    monkeypatch.delenv("SDLC_DOCS")
    toml_config(docs={"enabled": False})
    for action in ("render", "check", "open"):
        assert run("docs", action, "plan") == DISABLED
