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
    "ignore": ["sdlc/*/references/", "sdlc/*/docs/", "sdlc/docs/", "sdlc/knowledge/", "graphify-out/", ".venv/"],
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


STEP_NAMES = ["uv", "graphify", "skill", "archify", "hooks", "graphifyignore", "graph", "bundle", "claude_md"]


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
        "archify": "skipped",  # SDLC_DOCS=off in the repo fixture
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
    assert (repo / ".graphifyignore").read_text() == "sdlc/*/references/\nsdlc/*/docs/\nsdlc/docs/\nsdlc/knowledge/\ngraphify-out/\n.venv/\n"
    assert (repo / "graphify-out/graph.json").exists()
    assert (repo / "sdlc/knowledge/index.md").exists() and (repo / "sdlc/knowledge/log.md").exists()
    claude_md = (repo / "CLAUDE.md").read_text()
    assert claude_md.count("<!-- sdlc-knowledge-start -->") == 1 and "sdlc/knowledge/index.md" in claude_md
    assert "human:" not in (repo / "sdlc/knowledge/index.md").read_text()


def test_bootstrap_healthy_project_makes_no_calls(run, repo: Path, knowledge, monkeypatch):
    run("knowledge", "bootstrap")
    before = knowledge.calls()
    again = run("knowledge", "bootstrap")
    assert set(states(again).values()) == {"present", "skipped"}  # archify: docs off
    assert knowledge.calls() == before  # both hook blocks are read from the file; no `graphify hook status`
    import subprocess

    def boom(*a, **kw):
        raise AssertionError("subprocess used on a healthy project")

    monkeypatch.setattr(subprocess, "run", boom)
    third = run("knowledge", "bootstrap")
    assert third["ok"] and set(states(third).values()) == {"present", "skipped"}
    assert (repo / "CLAUDE.md").read_text().count("<!-- sdlc-knowledge-start -->") == 1


def test_bootstrap_installs_uv_when_missing(run, repo: Path, knowledge, monkeypatch):
    from sdlc import knowledge as k

    shutil.copy(knowledge.bin / "uv", knowledge.bin / "uv.hidden")
    knowledge.uninstall("uv")
    monkeypatch.setattr(k, "uv_install_command", lambda: ["sh", "-c", f"cp '{knowledge.bin}/uv.hidden' '{knowledge.bin}/uv'"])
    out = run("knowledge", "bootstrap")
    assert out["ok"], out
    st = states(out)
    assert st["uv"] == "installed" and st["graphify"] == "installed" and st["bundle"] == "built"
    assert "uv.hidden" in next(s for s in out["steps"] if s["name"] == "uv")["detail"]  # the command that ran is reported
    assert knowledge.calls()[0] == "uv tool install graphifyy"


def test_bootstrap_uv_installer_failure_fails_closed(run, repo: Path, knowledge, monkeypatch):
    from sdlc import knowledge as k

    knowledge.uninstall("uv")
    monkeypatch.setattr(k, "uv_install_command", lambda: ["sh", "-c", "echo no network >&2; exit 7"])
    out = run("knowledge", "bootstrap")
    assert out["ok"] is False and "uv" in out["reason"] and "no network" in out["reason"]
    st = states(out)
    assert st["uv"] == "failed" and st["graphify"] == "skipped" and st["bundle"] == "skipped"
    assert not any("pip" in c for c in knowledge.calls()) and knowledge.calls() == []
    assert not (repo / "graphify-out").exists()
    assert states(run("knowledge", "bootstrap", "check"))["uv"] == "missing"


def test_uv_install_command_is_gated_by_operating_system():
    from sdlc import knowledge as k

    posix = k.uv_install_command("Darwin")
    assert posix[0] == "sh" and "https://astral.sh/uv/install.sh" in posix[-1] and "curl" in posix[-1]
    assert k.uv_install_command("Linux") == posix
    win = k.uv_install_command("Windows")
    assert win[0] == "powershell" and "https://astral.sh/uv/install.ps1" in win[-1] and "irm" in win[-1]
    assert not any("pip" in part for part in posix + win)


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
    for needle in (str(p.PLUGIN_ROOT), "GRAPHIFY_SKIP_HOOK", "'^sdlc/knowledge/'", "'^graphify-out/'", "knowledge refresh"):
        assert needle in text, needle
    assert 'uv run --no-project "' + str(p.PLUGIN_ROOT) + '/scripts/sdlc.py" knowledge refresh' in text  # uv, not a bare python3
    assert "command -v uv" in text and "python3 " not in text.split("# sdlc-knowledge-start")[1]
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
        "modules/fmt.md",
        "modules/index.md",
    ]
    assert out["concepts"] == 10 and out["created"] == 10 and out["updated"] == 0 and out["tombstoned"] == 0
    assert not (home / "modules/guide.md").exists()  # a markdown-heading community is not a Module, whatever its size
    assert not (home / "hubs/intro.md").exists()  # document nodes are never hubs, whatever their degree
    front, body = k.split_document((home / "features/feat.md").read_text())
    assert front["type"] == "Feature" and front["title"] == "Feat" and front["status"] == "draft"
    assert front["generated"]["by"] == f"sdlc/{k.plugin_version()}" and front["source_commit"] == head(repo)  # whatever plugin.json says
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
    assert log.count("**Creation**") == 10
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
    assert rows[-5]["value"] == 19 and rows[-4]["value"] == 5 and rows[-2]["value"] == 10
    assert "human:" not in "".join(f.read_text() for f in home.rglob("*.md"))
    intent = repo / "sdlc/feat/intent.md"
    intent.write_text(intent.read_text().replace("## Problem\np", "## Problem\np with trailing space   \nand a tab\t", 1))
    lessons = repo / "sdlc/lessons.md"
    lessons.write_text(lessons.read_text() + "- 2026-09-09: " + ("word " * 60).strip() + "\n")  # truncated descriptions and titles end on a space
    run("knowledge", "refresh")
    for f in home.rglob("*.md"):  # generated files never carry trailing whitespace (pre-commit would rewrite them)
        assert not any(line != line.rstrip() for line in f.read_text().splitlines()), f


def test_refresh_is_idempotent(run, repo: Path, knowledge, accepted_plan):
    seed_sources(repo)
    run("knowledge", "bootstrap")
    run("knowledge", "refresh")
    before = bundle_files(repo)
    out = run("knowledge", "refresh")
    assert out["ok"] and out["created"] == 0 and out["updated"] == 0
    after = bundle_files(repo)
    assert {n for n in before if before[n] != after.get(n)} | {n for n in after if n not in before} <= {".state.json"}
    assert json.loads(after[".state.json"])["updates"] == json.loads(before[".state.json"])["updates"]  # same graph build consumed


def commit_all(repo: Path, msg: str) -> None:
    subprocess.run(["git", "add", "-A"], cwd=repo, check=True)
    subprocess.run(["git", "commit", "-qm", msg], cwd=repo, check=True)


def test_refresh_invalidates_changed_sources_and_tombstones_deleted(run, repo: Path, knowledge, accepted_plan):
    from sdlc import knowledge as k

    seed_sources(repo)
    run("knowledge", "bootstrap")
    run("knowledge", "refresh")  # the fixture's `plan new` bootstrapped before the sources existed
    home = repo / "sdlc/knowledge"
    feat = home / "features/feat.md"
    feat.write_text(feat.read_text().replace("status: draft", "status: stable", 1))
    commit_all(repo, "bundle")
    # a source edit that leaves the generated content identical still resets the concept to draft
    intent = repo / "sdlc/feat/intent.md"
    intent.write_text(intent.read_text().replace("## Constraints\nc", "## Constraints\nc and more", 1))
    commit_all(repo, "intent constraints")
    out = run("knowledge", "refresh")
    assert out["ok"] and out["updated"] == 1 and out["created"] == 0
    front, body = k.split_document(feat.read_text())
    assert front["status"] == "draft" and front["source_commit"] == head(repo)
    assert "**Update**: [Feat](/features/feat.md)" in (home / "log.md").read_text()
    # unchanged sources, unchanged content: nothing rewritten
    assert run("knowledge", "refresh")["updated"] == 0
    # deleted source: every lesson concept becomes a tombstone, nothing is deleted
    (repo / "sdlc/lessons.md").unlink()
    commit_all(repo, "drop lessons")
    out = run("knowledge", "refresh")
    assert out["tombstoned"] == 3 and out["ok"]
    for name in ("2026-09-07-1", "2026-09-08-1", "2026-09-08-2"):
        front, body = k.split_document((home / f"lessons/{name}.md").read_text())
        assert front["status"] == "deprecated" and front["type"] == "Lesson" and body.startswith("# Deprecated")
    assert (home / "log.md").read_text().count("**Deprecation**") == 3
    assert "lessons/2026-09-07-1.md" not in (home / "lessons/index.md").read_text()
    assert run("knowledge", "refresh")["tombstoned"] == 0  # tombstones stay tombstones, no new log lines
    # a hand-written concept without sources is kept and reported, never touched
    manual = home / "features/manual.md"
    manual.write_text("---\ntype: Note\ntitle: Manual\n---\n# Manual\nkeep me\n")
    out = run("knowledge", "refresh")
    assert out["unresolved"] == ["features/manual.md"] and manual.read_text().endswith("keep me\n")
    # a hub is derived from the graph, not from its file: one the graph no longer ranks is tombstoned even though the file exists
    (home / "hubs/old.md").write_text(k.dump_frontmatter({"type": "Hub", "title": "old()", "sources": [{"id": "core", "resource": "src/app/core.py"}]}) + "# old\n")
    out = run("knowledge", "refresh")
    assert out["tombstoned"] == 1 and "hubs/old.md" not in out["unresolved"]
    assert k.split_document((home / "hubs/old.md").read_text())[0]["status"] == "deprecated"
    # a module whose files still exist but whose community vanished is kept and reported, not tombstoned
    (home / "modules/ghost.md").write_text(k.dump_frontmatter({"type": "Module", "title": "Ghost", "sources": [{"id": "core", "resource": "src/app/core.py"}]}) + "# Ghost\n")
    out = run("knowledge", "refresh")
    assert "modules/ghost.md" in out["unresolved"] and out["tombstoned"] == 0


def test_publish_only_on_accept_and_never_by_generation(run, repo: Path, knowledge, accepted_plan):
    from sdlc import knowledge as k

    seed_sources(repo)
    run("knowledge", "bootstrap")
    home = repo / "sdlc/knowledge"
    shutil.rmtree(home)  # the fixture's accepts already published; start from a bundle generation alone
    run("knowledge", "refresh")
    assert "human:" not in "".join(f.read_text() for f in home.rglob("*.md"))
    out = k.publish(repo, repo / "sdlc/feat", "Linus McManamey")
    assert out["ok"] and out["actor"] == "human:linus-mcmanamey" and out["status"] == "stable"
    front, _ = k.split_document((home / "features/feat.md").read_text())
    assert front["status"] == "stable" and front["verified"][0]["by"] == "human:linus-mcmanamey"
    assert front["verified"][0]["at"] <= k.now_iso()
    assert "verified by human:linus-mcmanamey" in (home / "log.md").read_text()
    # unchanged sources: refresh keeps the file, so verified and stable survive
    run("knowledge", "refresh")
    front, _ = k.split_document((home / "features/feat.md").read_text())
    assert front["status"] == "stable" and len(front["verified"]) == 1
    # a process actor adds a verification event but never promotes
    out = k.publish(repo, repo / "sdlc/feat", "process:sdlc-test")
    front, _ = k.split_document((home / "features/feat.md").read_text())
    assert [v["by"] for v in front["verified"]] == ["human:linus-mcmanamey", "process:sdlc-test"]
    (home / "features/feat.md").write_text((home / "features/feat.md").read_text().replace("status: stable", "status: draft"))
    k.publish(repo, repo / "sdlc/feat", "process:sdlc-test")
    front, _ = k.split_document((home / "features/feat.md").read_text())
    assert front["status"] == "draft" and len(front["verified"]) == 3
    # a source change keeps the history but the concept is a draft again until the next human accept
    intent = repo / "sdlc/feat/intent.md"
    intent.write_text(intent.read_text().replace("## Constraints\nc", "## Constraints\nc2", 1))
    commit_all(repo, "intent")
    run("knowledge", "refresh")
    front, _ = k.split_document((home / "features/feat.md").read_text())
    assert front["status"] == "draft" and len(front["verified"]) == 3
    k.publish(repo, repo / "sdlc/feat", "human:someone")
    front, _ = k.split_document((home / "features/feat.md").read_text())
    assert front["status"] == "stable" and len(front["verified"]) == 4
    # publish before any bundle exists generates it first
    shutil.rmtree(home)
    assert k.publish(repo, repo / "sdlc/feat", "Linus McManamey")["ok"] and (home / "features/feat.md").exists()


def test_check_separates_conformance_policy_trust(run, repo: Path, knowledge, accepted_plan):
    from sdlc import knowledge as k

    seed_sources(repo)
    run("knowledge", "bootstrap")
    run("knowledge", "refresh")
    home = repo / "sdlc/knowledge"
    assert run("knowledge", "check")["ok"]
    # tolerated by the spec: unknown type, unknown keys, broken links
    (home / "features/odd.md").write_text(
        k.dump_frontmatter({"type": "Runbook Thing", "title": "Odd", "mystery": 3, "generated": {"by": "x/1", "at": "2026-01-01T00:00:00Z"}, "source_commit": "abc"}) + "\n# Odd\nsee [gone](/features/nowhere.md)\n"
    )
    # conformance failures: no frontmatter, unparseable frontmatter, empty type
    (home / "features/bare.md").write_text("# no frontmatter\n")
    (home / "features/broken.md").write_text("---\n[[[\n---\nbody\n")
    (home / "features/notype.md").write_text("---\ntype: \ntitle: T\n---\nbody\n")
    # policy failures: draft with a human verified event; stable with stale_after in the past; missing title
    (home / "features/forged.md").write_text(
        k.dump_frontmatter({"type": "Feature", "title": "Forged", "status": "draft", "generated": {"by": "x/1", "at": "2026-01-01T00:00:00Z"}, "verified": [{"by": "human:boss", "at": "2026-01-02T00:00:00Z"}], "source_commit": "abc"})
        + "\nbody\n"
    )
    (home / "features/old.md").write_text(
        k.dump_frontmatter(
            {
                "type": "Feature",
                "title": "Old",
                "status": "stable",
                "generated": {"by": "x/1", "at": "2026-01-01T00:00:00Z"},
                "verified": {"by": "process:ci", "at": "2026-01-02T00:00:00Z"},
                "stale_after": "2026-01-03T00:00:00Z",
                "source_commit": "abc",
            }
        )
        + "\nbody\n"
    )
    (home / "features/untitled.md").write_text("---\ntype: Feature\n---\nbody\n")
    out = run("knowledge", "check")
    assert out["ok"] is False
    assert sorted(x.split(":")[0] for x in out["conformance"]) == ["features/bare.md", "features/broken.md", "features/notype.md"]
    assert not any("odd.md" in x for x in out["conformance"] + out["policy"])
    policy = {x.split(":")[0] for x in out["policy"]}
    assert policy == {"features/forged.md", "features/old.md", "features/untitled.md"}
    assert any("forged.md" in x and "human:" in x for x in out["policy"])
    assert any("old.md" in x and "stale_after" in x for x in out["policy"])
    assert any("untitled.md" in x and "title" in x for x in out["policy"])
    # trust tiers count every conformant concept: 10 generated (feat human-reviewed by the fixture accepts, 9 unverified)
    # plus odd and untitled (unverified), forged (human-reviewed), old (machine-confirmed)
    assert out["trust"] == {"unverified": 11, "machine-confirmed": 1, "human-reviewed": 2}
    assert out["reason"].startswith("3 conformance finding")
    for name in ("bare", "broken", "notype", "forged", "old", "untitled", "odd"):
        (home / f"features/{name}.md").unlink()
    assert run("knowledge", "check")["ok"]


def test_status_reports_behind_skew_and_clean_cadence(run, repo: Path, knowledge, accepted_plan, monkeypatch):
    import os
    import time

    seed_sources(repo)
    run("knowledge", "bootstrap")
    run("knowledge", "refresh")
    out = run("knowledge", "status")
    assert out["ok"] and out["rebuild"] == "incremental" and out["reasons"] == []
    assert out["graph"] == {"commit": head(repo), "behind": 0, "artifacts_agree": True, "last_rebuild": None}
    assert out["bundle"]["commit"] == head(repo) and out["bundle"]["behind"] == 0
    assert out["bundle"]["concepts"] == 10 and out["bundle"]["stale"] == 0 and out["bundle"]["draft"] == 9
    (repo / "src/app/util.py").write_text("# changed\n")
    commit_all(repo, "one")
    out = run("knowledge", "status")
    assert out["ok"] and out["graph"]["behind"] == 1 and out["bundle"]["behind"] == 1  # max_behind = 1
    (repo / "src/app/util.py").write_text("# changed twice\n")
    commit_all(repo, "two")
    out = run("knowledge", "status")
    assert out["ok"] is False and out["rebuild"] == "clean"
    assert any("bundle" in r and "2 commits" in r for r in out["reasons"]) and any("graph" in r for r in out["reasons"])
    assert "graphify-out/graph.json" in out["reason"] or "bundle" in out["reason"]
    # the next refresh rebuilds the graph cleanly and rewrites the bundle from it
    calls_before = len(knowledge.calls())
    out = run("knowledge", "refresh")
    assert out["ok"] and out["rebuild"] == "clean"
    assert "graphify update . --force" in knowledge.calls()[calls_before:]
    state = json.loads((repo / "sdlc/knowledge/.state.json").read_text())
    assert state["updates"] == 1 and state["commit"] == head(repo)
    out = run("knowledge", "status")
    assert out["ok"] and out["graph"]["behind"] == 0 and out["bundle"]["behind"] == 0
    # cadence: clean_every incremental refreshes force the next one clean
    state_path = repo / "sdlc/knowledge/.state.json"
    state_path.write_text(json.dumps({**state, "updates": 5}))
    out = run("knowledge", "status")
    assert out["ok"] is False and out["rebuild"] == "clean" and any("5 refreshes" in r for r in out["reasons"])
    run("knowledge", "refresh")
    assert knowledge.calls()[-1] == "graphify update . --force"
    assert json.loads(state_path.read_text())["updates"] == 1
    # artifact skew and the rebuild log tail
    html = repo / "graphify-out/graph.html"
    late = time.time() + 400
    os.utime(html, (late, late))
    log = repo / "rebuild.log"
    log.write_text("[graphify] rebuilt 12 nodes\n[graphify] done in 0.8s\n")
    monkeypatch.setenv("GRAPHIFY_REBUILD_LOG", str(log))
    out = run("knowledge", "status")
    assert out["graph"]["artifacts_agree"] is False and out["graph"]["last_rebuild"] == "[graphify] done in 0.8s"
    assert out["ok"] and any("skew" in r for r in out["notes"])


def test_hooks_json_registers_session_start_and_post_bash():
    from sdlc import project as p

    spec = json.loads((p.PLUGIN_ROOT / "hooks/hooks.json").read_text())["hooks"]
    start = spec["SessionStart"][0]["hooks"][0]
    assert start["command"].endswith("session-start; fi") and start["timeout"] >= 60
    assert "command -v uv" in start["command"] and "astral.sh/uv/install.sh" in start["command"]
    post = next(h for h in spec["PostToolUse"] if h["matcher"] == "Bash")["hooks"][0]
    assert post["command"].endswith("post-bash; fi") and post["timeout"] <= 10
    every = [h["command"] for event in spec.values() for entry in event for h in entry["hooks"]]
    for c in every:  # uv when present, python3 as the fallback so the guardrails never fail open
        assert 'P="${CLAUDE_PLUGIN_ROOT}/scripts/hook.py"' in c and 'uv run --no-project "$P"' in c and 'python3 "$P"' in c
        assert c.index("uv run") < c.index("python3")
    assert "SDLC_KNOWLEDGE" in start["command"] and "enabled" in start["command"]  # the uv install honours the off switches


def test_linked_worktree_leaves_shared_hook_to_primary(run, repo: Path, knowledge, tmp_path: Path):
    from sdlc import cli
    from sdlc import knowledge as k
    from sdlc import project as p

    run("knowledge", "bootstrap")
    hook = repo / ".git/hooks/post-commit"
    stale = hook.read_text().replace(str(p.PLUGIN_ROOT), "/elsewhere/plugin")
    hook.write_text(stale)
    wt = tmp_path / "wt"
    subprocess.run(["git", "worktree", "add", "-q", "--detach", str(wt), "HEAD"], cwd=repo, check=True)
    try:
        out = cli.main(["knowledge", "bootstrap"], root=wt)
        assert out["ok"], out
        assert states(out)["hooks"] == "present"
        assert hook.read_text() == stale  # a linked worktree never rewrites the shared hook
        import pytest

        from sdlc.project import Blocked

        with pytest.raises(Blocked, match="linked worktree"):
            k.install_hook(wt)
    finally:
        subprocess.run(["git", "worktree", "remove", "--force", str(wt)], cwd=repo, check=True)
    out = run("knowledge", "bootstrap")  # the primary checkout repairs a block that points at a path that is gone
    assert states(out)["hooks"] == "installed" and str(p.PLUGIN_ROOT) in hook.read_text() and "/elsewhere/plugin" not in hook.read_text()


def test_linked_worktree_bootstrap_skips_hooks_and_continues(run, repo: Path, knowledge, tmp_path: Path):
    from sdlc import cli

    wt = tmp_path / "wt2"
    subprocess.run(["git", "worktree", "add", "-q", "--detach", str(wt), "HEAD"], cwd=repo, check=True)
    try:
        out = cli.main(["knowledge", "bootstrap"], root=wt)
        st = states(out)
        assert out["ok"] and st["hooks"] == "skipped" and st["graph"] == "built" and st["bundle"] == "built", out
        assert "primary checkout" in next(s["detail"] for s in out["steps"] if s["name"] == "hooks")
    finally:
        subprocess.run(["git", "worktree", "remove", "--force", str(wt)], cwd=repo, check=True)


def test_status_reports_unknown_history_and_corrupt_state(run, repo: Path, knowledge, accepted_plan):
    from sdlc import hooks

    seed_sources(repo)
    run("knowledge", "bootstrap")
    run("knowledge", "refresh")
    state_path = repo / "sdlc/knowledge/.state.json"
    state = json.loads(state_path.read_text())
    state_path.write_text(json.dumps({**state, "commit": "0123456789abcdef0123456789abcdef01234567"}))
    out = run("knowledge", "status")
    assert out["ok"] is False and out["bundle"]["behind"] is None
    assert any("not in this repository's history" in r for r in out["reasons"])
    state_path.write_text("{not json")
    out = run("knowledge", "status")
    assert out["ok"] is False and any(".state.json" in r and "unreadable" in r for r in out["reasons"])
    assert hooks.post_edit({"tool_name": "Edit", "tool_input": {"file_path": str(repo / "src/web/api.py")}}, repo) is None or True  # no traceback
    assert hooks.session_start({"cwd": str(repo)}, repo)["hookSpecificOutput"]["hookEventName"] == "SessionStart"
    assert run("knowledge", "refresh")["ok"]  # a refresh rewrites the state from scratch
    assert json.loads(state_path.read_text())["commit"] == head(repo)


def test_bundle_setting_is_validated_before_it_reaches_a_hook_or_path(run, repo: Path, knowledge, toml_config):
    from sdlc import knowledge as k

    for bad in ("k'; echo PWNED > /tmp/pwned; :'", "../outside", "/abs/path", 'a"b', "x$y"):
        toml_config(knowledge={"bundle": bad})
        out = run("knowledge", "bootstrap")
        assert out["ok"] is False and "[knowledge] bundle" in out["reason"], bad
        assert not (repo / ".git/hooks/post-commit").exists() or "PWNED" not in (repo / ".git/hooks/post-commit").read_text()
    toml_config(knowledge={"bundle": "docs/knowledge"})
    assert run("knowledge", "bootstrap")["ok"] and (repo / "docs/knowledge/index.md").exists()
    assert "'^docs/knowledge/'" in (repo / ".git/hooks/post-commit").read_text()
    assert k.shell_word('a"b$c`d\\e') == '"a\\"b\\$c\\`d\\\\e"'


def test_hook_block_waits_on_the_graph_commit_not_a_reflog(repo: Path, knowledge):
    from sdlc import knowledge as k

    k.install_hook(repo)
    text = (repo / ".git/hooks/post-commit").read_text()
    assert "logs/HEAD" not in text and "built_at_commit" in text and "git rev-parse HEAD" in text


def test_signature_notices_a_removed_builder_key(run, repo: Path, knowledge, accepted_plan):
    from sdlc import knowledge as k

    seed_sources(repo)
    run("knowledge", "bootstrap")
    run("knowledge", "refresh")
    lessons = repo / "sdlc/lessons.md"
    lessons.write_text(lessons.read_text().replace("- 2026-09-08: rollback rehearsal ran in the working checkout; now fixed by rehearsing in a worktree per deploy.rehearse\n", "- 2026-09-08: something unrelated entirely\n"))
    commit_all(repo, "lesson no longer supersedes")
    run("knowledge", "refresh")
    assert "supersedes" not in k.split_document((repo / "sdlc/knowledge/lessons/2026-09-08-1.md").read_text())[0]


def test_unreadable_frontmatter_is_regenerated_not_published_over(run, repo: Path, knowledge, accepted_plan):
    from sdlc import knowledge as k

    seed_sources(repo)
    run("knowledge", "bootstrap")
    path = repo / "sdlc/knowledge/features/feat.md"
    path.write_text("---\ntype: Feature\n[[[\n---\nbody\n")
    out = run("knowledge", "refresh")  # generation rewrites it (content differs) and drops the unreadable block
    assert out["ok"] and "_raw" not in path.read_text()
    path.write_text("---\ntype: Feature\n[[[\n---\nbody\n")
    out = k.publish(repo, repo / "sdlc/feat", "human:x")  # publish refreshes first, so it never writes _raw back out
    front, _ = k.split_document(path.read_text())
    assert out["ok"] and "_raw" not in front and front["verified"][-1]["by"] == "human:x" and front["status"] == "stable"


def test_bootstrap_archify_step_skips_installs_and_reports(run, repo: Path, knowledge, docs_tools, monkeypatch):
    from conftest import write_fake_node

    def step(out):
        return next(s for s in out["steps"] if s["name"] == "archify")

    out = run("knowledge", "bootstrap")
    assert out["ok"] and step(out) == {"name": "archify", "state": "present", "detail": "Archify skill 2.17.0-dev.1"}
    docs_tools.uninstall("archify", "node")
    out = run("knowledge", "bootstrap")
    assert out["ok"] and step(out)["state"] == "skipped", out
    assert "node >= 18" in step(out)["detail"] and "npx -y skills add tt-a1i/archify" in step(out)["detail"]
    assert states(out)["hooks"] == "present"  # later steps still ran
    write_fake_node(docs_tools.bin)
    out = run("knowledge", "bootstrap", "check")
    assert out["ok"] is False and step(out)["state"] == "missing" and "npx -y skills add tt-a1i/archify" in step(out)["detail"]
    assert not any(c.startswith("npx") for c in docs_tools.calls())
    out = run("knowledge", "bootstrap")
    assert out["ok"] and step(out) == {"name": "archify", "state": "installed", "detail": "Archify skill 2.17.0-dev.1"}
    assert "npx -y skills add tt-a1i/archify --skill archify --agent claude-code --global --copy --yes" in docs_tools.calls()
    assert (docs_tools.skill_dir / "bin/archify.mjs").exists()
    monkeypatch.setenv("SDLC_DOCS", "off")
    out = run("knowledge", "bootstrap")
    assert out["ok"] and step(out) == {"name": "archify", "state": "skipped", "detail": "docs disabled"}


def test_status_reports_archify_version(run, repo: Path, knowledge, accepted_plan, docs_tools, toml_config):
    seed_sources(repo)
    run("knowledge", "bootstrap")
    run("knowledge", "refresh")
    out = run("knowledge", "status")
    assert out["ok"] and out["archify"] == {"installed": True, "version": "2.17.0-dev.1", "min_version": "2.17"}
    assert not any("archify" in n for n in out["notes"])
    toml_config(docs={"min_version": "3.0"})
    out = run("knowledge", "status")
    assert out["ok"] and "archify 2.17.0-dev.1 is older than [docs] min_version 3.0" in out["notes"]
    docs_tools.uninstall("archify")
    out = run("knowledge", "status")
    assert out["archify"] == {"installed": False, "version": None, "min_version": "3.0"} and not any("archify" in n for n in out["notes"])


def test_feature_concept_lists_documents(run, repo: Path, knowledge, accepted_plan, docs_tools):
    seed_sources(repo)
    run("knowledge", "bootstrap")
    run("knowledge", "refresh")
    from sdlc import knowledge as k

    concept = repo / "sdlc/knowledge/features/feat.md"
    assert "# Documents\n- none\n" in concept.read_text()
    humans = [v for v in k.split_document(concept.read_text())[0]["verified"] if v["by"].startswith("human:")]
    (repo / "sdlc/feat/docs").mkdir()
    (repo / "sdlc/feat/docs/plan.json").write_text('{"meta": {"title": "plan"}}\n')
    assert run("docs", "render", "plan")["ok"]
    run("knowledge", "refresh")
    text = concept.read_text()
    assert "# Documents\n- plan: sdlc/feat/docs/plan.html (9/9 showcase, 0 errors, 0 warnings)\n" in text
    front, _ = k.split_document(text)
    assert [v for v in front["verified"] if v["by"].startswith("human:")] == humans  # generation adds no human event
