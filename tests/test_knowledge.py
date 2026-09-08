from pathlib import Path

from sdlc import project as p

KNOWLEDGE_DEFAULTS = {
    "enabled": True,
    "auto_install": False,
    "bundle": "sdlc/knowledge",
    "claude_md_pointer": True,
    "clean_every": 5,
    "max_behind": 1,
    "stale_after_days": 14,
    "artifact_skew_seconds": 300,
    "min_community_nodes": 3,
    "god_nodes": 10,
    "ignore": ["sdlc/*/references/", "graphify-out/", ".venv/"],
}
ACTIONS = ("bootstrap", "status", "refresh", "check", "unhook")


def test_defaults_and_disabled_verdicts(run, repo: Path, toml_config, monkeypatch):
    assert p.config(repo)["knowledge"] == KNOWLEDGE_DEFAULTS
    for action in ACTIONS:  # SDLC_KNOWLEDGE=off from the repo fixture
        assert run("knowledge", action) == {"ok": True, "skipped": "knowledge disabled", "stage": "knowledge"}
    monkeypatch.delenv("SDLC_KNOWLEDGE")
    toml_config(knowledge={"enabled": False})
    for action in ACTIONS:
        assert run("knowledge", action) == {"ok": True, "skipped": "knowledge disabled", "stage": "knowledge"}
