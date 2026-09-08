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


STEP_NAMES = ["uv", "graphify", "skill", "hooks", "graphifyignore", "graph", "bundle", "claude_md"]


def states(out: dict) -> dict[str, str]:
    return {s["name"]: s["state"] for s in out["steps"]}


def test_bootstrap_installs_in_order_and_reports_steps(run, repo: Path, knowledge):
    out = run("knowledge", "bootstrap")
    assert out["ok"], out
    assert [s["name"] for s in out["steps"]] == STEP_NAMES
    assert states(out) == {
        "uv": "present",
        "graphify": "installed",
        "skill": "installed",
        "hooks": "installed",
        "graphifyignore": "built",
        "graph": "built",
        "bundle": "built",
        "claude_md": "built",
    }
    assert knowledge.calls() == [
        "uv tool install graphifyy",
        "graphify install --platform claude",
        "graphify hook install",  # no `hook status` call: the hook file did not exist yet
        "graphify update .",
    ]
    assert next(s for s in out["steps"] if s["name"] == "graphify")["detail"] == "uv tool install graphifyy"
    assert knowledge.skill.exists()
    assert (repo / ".graphifyignore").read_text() == "sdlc/*/references/\ngraphify-out/\n.venv/\n"
    assert (repo / "graphify-out/graph.json").exists()
    assert (repo / "sdlc/knowledge/index.md").exists() and (repo / "sdlc/knowledge/log.md").exists()
    claude_md = (repo / "CLAUDE.md").read_text()
    assert claude_md.count("<!-- sdlc-knowledge-start -->") == 1 and "sdlc/knowledge/index.md" in claude_md
    assert "human:" not in (repo / "sdlc/knowledge/index.md").read_text()


def test_bootstrap_healthy_project_makes_no_calls(run, repo: Path, knowledge, monkeypatch):
    run("knowledge", "bootstrap")
    before = knowledge.calls()
    again = run("knowledge", "bootstrap")
    assert set(states(again).values()) == {"present"}
    assert knowledge.calls() == [*before, "graphify hook status"]  # first re-check verifies hooks once
    import subprocess

    def boom(*a, **kw):
        raise AssertionError("subprocess used on a healthy project")

    monkeypatch.setattr(subprocess, "run", boom)
    third = run("knowledge", "bootstrap")
    assert third["ok"] and set(states(third).values()) == {"present"}
    assert (repo / "CLAUDE.md").read_text().count("<!-- sdlc-knowledge-start -->") == 1


def test_bootstrap_missing_uv_fails_closed(run, repo: Path, knowledge):
    knowledge.uninstall("uv")
    out = run("knowledge", "bootstrap")
    assert out["ok"] is False and "uv" in out["reason"]
    st = states(out)
    assert st["uv"] == "failed" and st["graphify"] == "skipped" and st["bundle"] == "skipped"
    assert not any("pip" in c for c in knowledge.calls())
    assert not (repo / "graphify-out").exists()


def test_bootstrap_check_mode_installs_nothing(run, repo: Path, knowledge):
    out = run("knowledge", "bootstrap", "check")
    assert out["ok"] is False and out["mode"] == "check"
    st = states(out)
    assert st["uv"] == "present" and st["graphify"] == "missing" and st["bundle"] == "missing"
    assert knowledge.calls() == []
    assert not (repo / "CLAUDE.md").exists() and not (repo / ".graphifyignore").exists()


GRAPHIFY_BLOCK = "#!/bin/sh\n# graphify-hook-start\necho graphify\n# graphify-hook-end\n"


def test_hook_block_idempotent_and_removable(run, repo: Path, knowledge):
    from sdlc import knowledge as k
    from sdlc import project as p

    hook = repo / ".git/hooks/post-commit"
    hook.parent.mkdir(exist_ok=True)
    hook.write_text(GRAPHIFY_BLOCK)
    hook.chmod(0o644)
    assert k.install_hook(repo)["ok"] and k.install_hook(repo)["ok"]
    text = hook.read_text()
    assert text.count("# sdlc-knowledge-start") == 1 and text.count("# sdlc-knowledge-end") == 1
    assert text.index("# graphify-hook-end") < text.index("# sdlc-knowledge-start")
    for needle in (str(p.PLUGIN_ROOT), "GRAPHIFY_SKIP_HOOK", "'^sdlc/knowledge/'", "'^graphify-out/'", "knowledge refresh --quiet"):
        assert needle in text, needle
    assert hook.stat().st_mode & 0o111
    assert run("knowledge", "unhook")["ok"]
    after = hook.read_text()
    assert "sdlc-knowledge" not in after and after == GRAPHIFY_BLOCK
    # bootstrap treats a post-commit with Graphify's block but not ours as hooks missing
    out = run("knowledge", "bootstrap")
    assert states(out)["hooks"] == "installed"
    assert "graphify hook install" not in knowledge.calls()
    assert "# sdlc-knowledge-start" in hook.read_text()
    # no post-commit at all: install_hook creates one with a shebang
    hook.unlink()
    assert k.install_hook(repo)["ok"] and hook.read_text().startswith("#!/bin/sh\n") and hook.stat().st_mode & 0o111
