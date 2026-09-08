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


def test_frontmatter_subset_round_trip():
    from sdlc import knowledge as k

    data = {
        "type": "Feature",
        "title": "Rehearsal: and band nits",
        "description": "Five nits left open by the review.",
        "resource": "sdlc/rehearsal-and-band-nits",
        "tags": ["feature", "accepted"],
        "status": "draft",
        "generated": {"by": "sdlc/0.2.0", "at": "2026-09-09T07:30:00Z"},
        "verified": [
            {"by": "process:sdlc-test", "at": "2026-09-08T05:50:00Z"},
            {"by": "human:linus-mcmanamey", "at": "2026-09-08T05:55:00Z"},
        ],
        "stale_after": "2026-09-23T07:30:00Z",
        "source_commit": "8409f99e",
        "sources": [{"id": "intent", "resource": "sdlc/x/intent.md", "last_modified": "2026-09-08T05:40:00Z"}],
        "okf_version": "0.2",
    }
    text = k.dump_frontmatter(data) + "# Body\n\nhello [x](/features/x.md)\n"
    assert text.startswith("---\n") and "\n---\n" in text
    front, body = k.split_document(text)
    assert front == data
    assert body == "# Body\n\nhello [x](/features/x.md)\n"
    assert k.split_document("no frontmatter\n") == ({}, "no frontmatter\n")
    raw = "---\ntype: Feature\nweird: [unclosed\n  - : :\n---\nbody\n"
    front, body = k.split_document(raw)
    assert front["type"] == "Feature" and "_raw" in front and body == "body\n"
    assert k.split_document("---\n[[[\n---\nb\n")[0] == {"_raw": "[[[\n"}
