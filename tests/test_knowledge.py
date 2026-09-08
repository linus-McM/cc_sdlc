import json
import shutil
import subprocess
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
        "graphify god-nodes --top 10 --json",  # the first bundle generation
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


def seed_sources(repo: Path) -> None:
    """Code files the fixture graph names, plus lessons, bands and one metric reading."""
    for rel in ("src/app/core.py", "src/app/util.py", "src/web/api.py", "src/web/views.py"):
        (repo / rel).parent.mkdir(parents=True, exist_ok=True)
        (repo / rel).write_text(f"# {rel}\n")
    (repo / "sdlc/lessons.md").write_text(
        "# Lessons\n\n- 2026-09-07: rollback rehearsal ran in the working checkout; rehearse in a worktree\n"
        "- 2026-09-08: rollback rehearsal ran in the working checkout; now fixed by rehearsing in a worktree per deploy.rehearse\n"
        "- 2026-09-08: write one step's failing test, green it, then the next\n"
    )
    (repo / "sdlc/bands.toml").write_text('[metrics.tests_passed]\nwindow = 30\ntiers = ["log", "diagnose", "propose"]\nbad = "low"\n')
    (repo / "sdlc/metrics.jsonl").write_text('{"metric": "tests_passed", "value": 76.0, "ts": "2026-09-08"}\n')
    subprocess.run(["git", "add", "-A"], cwd=repo, check=True)
    subprocess.run(["git", "commit", "-qm", "seed"], cwd=repo, check=True)


def head(repo: Path) -> str:
    return subprocess.run(["git", "rev-parse", "HEAD"], cwd=repo, capture_output=True, text=True, check=True).stdout.strip()


def bundle_files(repo: Path) -> dict[str, bytes]:
    home = repo / "sdlc/knowledge"
    return {str(f.relative_to(home)): f.read_bytes() for f in home.rglob("*") if f.is_file()}


def test_refresh_builds_bundle_from_graph_and_artifacts(run, repo: Path, knowledge, accepted_plan):
    from sdlc import knowledge as k

    seed_sources(repo)
    assert run("knowledge", "bootstrap")["ok"]  # generates the first bundle; drop it to watch refresh create
    home = repo / "sdlc/knowledge"
    shutil.rmtree(home)
    out = run("knowledge", "refresh")
    assert out["ok"] and out["source_commit"] == head(repo), out
    names = sorted(str(f.relative_to(home)) for f in home.rglob("*.md"))
    assert names == [
        "bands/index.md",
        "bands/tests-passed.md",
        "features/feat.md",
        "features/index.md",
        "hubs/get.md",
        "hubs/index.md",
        "hubs/run.md",
        "index.md",
        "lessons/2026-09-07-1.md",
        "lessons/2026-09-08-1.md",
        "lessons/2026-09-08-2.md",
        "lessons/index.md",
        "log.md",
        "modules/api-py.md",
        "modules/core-py.md",
        "modules/index.md",
    ]
    assert out["concepts"] == 9 and out["created"] == 9 and out["updated"] == 0 and out["tombstoned"] == 0
    front, body = k.split_document((home / "features/feat.md").read_text())
    assert front["type"] == "Feature" and front["title"] == "Feat" and front["status"] == "draft"
    assert front["generated"]["by"] == "sdlc/0.2.0" and front["source_commit"] == head(repo)
    assert "verified" not in front and front["stale_after"] > front["generated"]["at"]
    assert front["resource"] == "sdlc/feat"
    assert [src["resource"] for src in front["sources"]] == ["sdlc/feat/intent.md", "sdlc/feat/spec.md", "sdlc/feat/plan.md"]
    for heading in ("# Problem", "# Outcome", "# Requirements", "# Files", "# Review", "# Status"):
        assert heading in body
    front, body = k.split_document((home / "modules/api-py.md").read_text())
    assert front["type"] == "Module" and front["resource"] == "src/web"
    assert "[core.py](/modules/core-py.md)" in body.split("# Depends on")[1].split("# Inferred")[0]
    assert "[core.py](/modules/core-py.md)" in body.split("# Inferred")[1].split("# Features")[0]
    assert "get() (src/web/api.py:L12)" in body
    front, body = k.split_document((home / "hubs/run.md").read_text())
    assert front["type"] == "Hub" and "[core.py](/modules/core-py.md)" in body
    front, _ = k.split_document((home / "lessons/2026-09-08-1.md").read_text())
    assert front["type"] == "Lesson" and front["supersedes"] == "/lessons/2026-09-07-1.md"
    assert "supersedes" not in k.split_document((home / "lessons/2026-09-08-2.md").read_text())[0]
    front, body = k.split_document((home / "bands/tests-passed.md").read_text())
    assert front["type"] == "Control Band" and "76.0" in body and "low" in body
    index = (home / "index.md").read_text()
    assert index.startswith('---\nokf_version: "0.2"\n---\n')
    for section in ("# Features", "# Modules", "# Hubs", "# Lessons", "# Bands"):
        assert section in index
    assert "* [Feat](feat.md) - " in (home / "features/index.md").read_text()  # sub-index links are relative
    log = (home / "log.md").read_text()
    assert log.startswith("# Knowledge Update Log\n\n## " + __import__("sdlc.project", fromlist=["today"]).today())
    assert log.count("**Creation**") == 9
    state = json.loads((home / ".state.json").read_text())
    assert state["commit"] == head(repo) and state["updates"] == 1
    rows = [json.loads(line) for line in (repo / "sdlc/metrics.jsonl").read_text().splitlines()]
    assert [r["metric"] for r in rows[-5:]] == [
        "knowledge_nodes",
        "knowledge_communities",
        "knowledge_stale",
        "knowledge_unverified",
        "knowledge_behind",
    ]
    assert rows[-5]["value"] == 12 and rows[-4]["value"] == 3 and rows[-2]["value"] == 9
    assert "human:" not in "".join(f.read_text() for f in home.rglob("*.md"))


def test_refresh_is_idempotent(run, repo: Path, knowledge, accepted_plan):
    seed_sources(repo)
    run("knowledge", "bootstrap")
    run("knowledge", "refresh")
    before = bundle_files(repo)
    out = run("knowledge", "refresh")
    assert out["ok"] and out["created"] == 0 and out["updated"] == 0
    after = bundle_files(repo)
    assert {n for n in before if before[n] != after.get(n)} | {n for n in after if n not in before} == {".state.json"}
    assert json.loads(after[".state.json"])["updates"] == json.loads(before[".state.json"])["updates"] + 1
