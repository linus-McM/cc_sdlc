"""Graph-selected Repomix context packs: seeds, one-hop expansion, secret guards, the pack, and its gates."""

import json
from pathlib import Path

import pytest

from sdlc import project as p


def test_pack_config_defaults(repo: Path):
    conf = p.config(repo)["knowledge"]
    assert conf["pack_max_tokens"] == 0 and conf["pack_hops"] == 1 and conf["pack_base"] == "main"


def test_run_cmd_passes_stdin(repo: Path):
    assert p.run_cmd(repo, ["cat"], input="a\nb").stdout == "a\nb"


def test_packs_fixture_fakes_every_tool(repo: Path, packs):
    import os
    import subprocess

    assert "SDLC_PACKS" not in os.environ
    assert subprocess.run(["repomix", "--version"], capture_output=True, text=True).stdout.strip() == "1.18.0"
    subprocess.run(["npm", "update", "-g", "repomix"], check=True)
    assert subprocess.run(["uv", "tool", "run", "--from", "bandit==1.9.4", "bandit", "-q", "-f", "json"], capture_output=True, text=True).stdout.strip() == '{"results": []}'
    assert "npm update -g repomix" in packs.calls() and any(c.startswith("uv tool run") for c in packs.calls())


GRAPH = Path(__file__).parent / "fixtures/graph.json"


def test_expand_is_one_hop_over_calls_plus_community():
    from sdlc import packs

    got = packs.expand(json.loads(GRAPH.read_text()), ["src/web/api.py"], 1)
    assert got == {"src/web/api.py": "seed", "src/app/core.py": "callee", "src/web/views.py": "callee"}  # util.py is two hops; README only mentions


def test_expand_adds_community_members_and_callers():
    from sdlc import packs

    node = lambda i, f, c: {"id": i, "source_file": f, "community": c}  # noqa: E731
    graph = {
        "nodes": [node("a", "a.py", 0), node("b", "b.py", 0), node("c", "c.py", 1), node("d", "d.py", 1), node("e", "e.py", 2)],
        "links": [{"source": "c", "target": "a", "relation": "calls"}, {"source": "d", "target": "c", "relation": "calls"}, {"source": "a", "target": "e", "relation": "relates_to"}],
    }
    assert packs.expand(graph, ["a.py"], 1) == {"a.py": "seed", "c.py": "caller", "b.py": "community"}
    assert packs.expand(graph, ["a.py"], 2)["d.py"] == "caller"


def commit_files(repo: Path, message: str = "x", **files: str) -> str:
    """Write `files` (keys use __ for /) and commit them; return HEAD."""
    import subprocess

    for key, text in files.items():
        path = repo / key.replace("__", "/")
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(text)
    subprocess.run(["git", "add", "-A"], cwd=repo, check=True)
    subprocess.run(["git", "commit", "-qm", message], cwd=repo, check=True)
    return p.head_commit(repo)


def feature_dir(repo: Path, **artifacts_: str) -> Path:
    feature = repo / "sdlc/feat"
    feature.mkdir(parents=True, exist_ok=True)
    for name, text in artifacts_.items():
        (feature / name.replace("_", ".")).write_text(text)
    return feature


SOURCES = {"src__app__core.py": "def run(): pass\n", "src__app__util.py": "u = 1\n", "src__web__api.py": "a = 1\n", "src__web__views.py": "v = 1\n", "docs__guide.md": "g\n"}


def test_seeds_per_stage(repo: Path):
    import subprocess

    from sdlc import packs

    commit_files(repo, **SOURCES)
    feature = feature_dir(
        repo,
        intent_md="# Intent: Feat\n\n## Affected users and systems\n- `src/app/core.py:12`, the `src/web/` package and `docs/*.md`\n",
        spec_md="# Spec: Feat\n\n## Design\nReuses `src/app/util.py`.\n",
        plan_md="# Plan: Feat\n\n## Files that change\n- src/app/core.py\n- tests/test_new.py (new)\n",
    )
    assert packs.seeds(repo, feature, "plan") == (["docs/guide.md", "src/app/core.py", "src/web/api.py", "src/web/views.py"], [])
    assert "src/app/util.py" in packs.seeds(repo, feature, "design")[0]
    assert packs.seeds(repo, feature, "build") == (["src/app/core.py"], ["tests/test_new.py"])
    subprocess.run(["git", "checkout", "-qb", "feat"], cwd=repo, check=True)
    commit_files(repo, **{"src__app__core.py": "def run(): return 1\n", "sdlc__feat__review.md": "r\n"})
    assert packs.seeds(repo, feature, "test") == (["src/app/core.py"], [])
    (feature / "deploy.json").write_text(json.dumps({"deployments": [{"env": "production", "sha": p.head_commit(repo)}]}))
    commit_files(repo, **{"src__web__api.py": "a = 2\n"})
    assert packs.seeds(repo, feature, "maintain") == (["src/web/api.py"], [])


def test_unresolved_tokens_are_listed_not_guessed(repo: Path):
    from sdlc import packs

    commit_files(repo, **SOURCES)
    assert packs.resolve(repo, ["src/app/cor.py", "src/app/core.py", "--max-tokens", "src/"]) == (
        ["src/app/core.py", "src/app/util.py", "src/web/api.py", "src/web/views.py"],
        ["src/app/cor.py", "--max-tokens"],
    )


def test_exclude_list_applies_after_expansion(repo: Path):
    import subprocess

    from sdlc import packs

    secrets = {".env.local": "K=1\n", "keys__id_rsa": "k\n", "x.pem": "k\n", ".npmrc": "t\n", "my_credentials.json": "{}\n", ".claude__settings.local.json": "{}\n"}
    commit_files(repo, **SOURCES, **secrets, **{".gitignore": "ignored.txt\ngraphify-out/\n"})
    for name in ("ignored.txt", "graphify-out/x"):
        (repo / name).parent.mkdir(exist_ok=True)
        (repo / name).write_text("i\n")
        subprocess.run(["git", "add", "-f", name], cwd=repo, check=True)
    (repo / "link.py").symlink_to("src/app/core.py")
    commit_files(repo)
    (repo / "new.py").write_text("n\n")
    names = ["src/app/core.py", ".env.local", "keys/id_rsa", "x.pem", ".npmrc", "my_credentials.json", ".claude/settings.local.json", "graphify-out/x", "ignored.txt", "link.py", "new.py"]
    admitted, excluded = packs.admit(repo, names)
    assert admitted == ["src/app/core.py"]
    rules = {e["path"]: e["rule"] for e in excluded}
    assert set(rules) == set(names) - {"src/app/core.py"}
    assert rules["new.py"] == "untracked" and rules["link.py"] == "symlink" and rules["ignored.txt"] == "git-ignored"
    assert rules[".env.local"] == ".env*" and rules["keys/id_rsa"] == "id_rsa*" and rules["graphify-out/x"] == "graphify-out/**"


def test_exclude_list_is_frozen(repo: Path):
    from sdlc import packs

    assert isinstance(packs.EXCLUDE, tuple) and all(isinstance(rule, str) for rule in packs.EXCLUDE)
    assert not [key for key in p.config(repo)["knowledge"] if "exclude" in key]


INTENT = "# Intent: Feat\nAuthor: t. Status: draft. Risk: low.\n\n## Affected users and systems\n- `src/web/api.py`\n"


def ready(run, repo: Path) -> Path:
    """Sources and a feature committed, then the knowledge layer bootstrapped: graph.json is fresh at HEAD."""
    (repo / ".git/info/exclude").write_text("bin/\nhome/\nclaude/\n")  # the tool sandbox lives beside the repo files
    commit_files(repo, **SOURCES, **{"sdlc__feat__intent.md": INTENT})
    assert run("knowledge", "bootstrap")["ok"]
    commit_files(repo, "bootstrap output")  # .graphifyignore, CLAUDE.md and the bundle: all exempt from freshness
    return repo / "sdlc/feat"


def pack(repo: Path, stage: str = "plan", max_tokens: int | None = None) -> dict:
    from sdlc import packs

    return p.attempt(packs.build, repo, "feat", stage, max_tokens)


def test_pack_refuses_deploy_and_unknown_stages(run, repo: Path, packs):
    ready(run, repo)
    for stage in ("deploy", "bogus"):
        verdict = pack(repo, stage)
        assert not verdict["ok"] and "Deploy builds no pack" in verdict["reason"]


def test_pack_refuses_stale_graph_by_content(run, repo: Path, packs):
    ready(run, repo)
    commit_files(repo, **{"sdlc__feat__notes.md": "n\n"})
    assert pack(repo)["ok"]  # an sdlc/-only commit leaves the graph fresh
    commit_files(repo, **{"src__app__util.py": "u = 2\n"})
    verdict = pack(repo)
    assert not verdict["ok"] and "src/app/util.py" in verdict["stale"] and "graphify update ." in verdict["reason"]


def test_checkpoint_paths_do_not_stale_the_graph(run, repo: Path, packs):
    ready(run, repo)
    commit_files(repo, **{".sdlc.toml": "[knowledge]\npack_hops = 1\n", ".graphifyignore": (repo / ".graphifyignore").read_text() + "x/\n", "CLAUDE.md": "c\n"})
    assert pack(repo)["ok"]


def test_pack_refuses_missing_graph_and_unignored_graphify_out(run, repo: Path, packs):
    ready(run, repo)
    graph = repo / "graphify-out/graph.json"
    saved = graph.read_text()
    graph.unlink()
    verdict = pack(repo)
    assert not verdict["ok"] and "graph.json" in verdict["reason"]
    graph.write_text(saved)
    (repo / ".graphifyignore").write_text(".venv/\n")
    verdict = pack(repo)
    assert not verdict["ok"] and ".graphifyignore" in verdict["reason"] and "graphify-out/" in verdict["reason"]


def test_pack_refuses_dirty_admitted_file(run, repo: Path, packs):
    ready(run, repo)
    (repo / "src/web/api.py").write_text("a = 3\n")
    verdict = pack(repo)
    assert not verdict["ok"] and verdict["dirty"] == ["src/web/api.py"]


def test_missing_repomix_skips_advisory_and_fails_gated(run, repo: Path, packs):
    ready(run, repo)
    packs.uninstall("repomix")
    advisory = pack(repo, "design")
    assert advisory["ok"] and "npm i -g repomix" in advisory["skipped"]
    for stage in ("plan", "test"):
        gated = pack(repo, stage)
        assert not gated["ok"] and "npm i -g repomix" in gated["reason"]


def test_pack_layer_off_is_skipped(run, repo: Path, packs, monkeypatch):
    ready(run, repo)
    monkeypatch.setenv("SDLC_PACKS", "off")
    assert pack(repo) == {"ok": True, "skipped": "packs disabled (SDLC_PACKS=off)"}
    monkeypatch.setenv("SDLC_KNOWLEDGE", "off")
    assert pack(repo) == {"ok": True, "skipped": "knowledge disabled"}


def packs_dir(repo: Path) -> Path:
    return repo / "graphify-out/packs/feat"


def regraph(repo: Path, **files: str) -> None:
    """Commit `files`, then rebuild graph.json at the new HEAD, as the post-commit hook would."""
    import subprocess

    commit_files(repo, **files)
    subprocess.run(["graphify", "update", "."], cwd=repo, check=True, capture_output=True)


def test_pack_writes_xml_and_manifest(run, repo: Path, packs):
    ready(run, repo)
    verdict = pack(repo)
    assert verdict["ok"] and verdict["reused"] is False and verdict["over_budget"] is False
    manifest = json.loads(Path(verdict["manifest"]).read_text())
    key = manifest["key"]
    assert verdict["path"] == str(packs_dir(repo) / f"plan-{key[:12]}.xml") and Path(verdict["path"]).exists()
    assert manifest["head"] == p.head_commit(repo) and manifest["stage"] == "plan" and manifest["repomix_version"] == "1.18.0"
    assert set(verdict["files"]) == {"src/web/api.py", "src/app/core.py", "src/web/views.py"} and verdict["seeds"] == ["src/web/api.py"]
    assert verdict["tokens"] == manifest["tokens"] > 0 and [s["rung"] for s in verdict["steps"]] == ["full"]
    config = str(p.PLUGIN_ROOT / "templates/knowledge/repomix.config.json")
    call = next(c for c in packs.calls() if c.startswith("repomix "))
    assert f"--stdin --config {config} --style xml --output" in call and "--no-security-check" not in call and "--compress" not in call
    assert json.loads(Path(config).read_text())["security"]["enableSecurityCheck"] is True
    assert (repo / "graphify-out/packs/.gitignore").read_text() == "*\n"
    assert sorted((packs.bin / "stdin.log").read_text().split()) == sorted(verdict["files"])


def test_pack_reuses_same_key(run, repo: Path, packs):
    ready(run, repo)
    first = pack(repo)
    calls = len(packs.calls())
    again = pack(repo)
    assert again["reused"] is True and again["path"] == first["path"] and len(packs.calls()) == calls


def test_new_commit_rekeys_and_prunes_older_pack(run, repo: Path, packs):
    ready(run, repo)
    first = pack(repo)
    regraph(repo, **{"src__web__api.py": "a = 5\n"})
    second = pack(repo)
    assert second["ok"] and second["path"] != first["path"] and not Path(first["path"]).exists() and not Path(first["manifest"]).exists()
    assert sorted(f.name for f in packs_dir(repo).iterdir()) == sorted([Path(second["path"]).name, Path(second["manifest"]).name])


@pytest.mark.parametrize("marker", ["FAKE_SECRET", "FAKE_DROP", "FAKE_EXTRA", "exit"])
def test_output_scanner_refuses(run, repo: Path, packs, monkeypatch, marker):
    ready(run, repo)
    if marker == "exit":
        monkeypatch.setenv("FAKE_REPOMIX_EXIT", "3")
    else:
        regraph(repo, **{"src__web__api.py": f"token = '{marker} value'\n"})
    verdict = pack(repo)
    assert not verdict["ok"] and "value" not in json.dumps(verdict)
    named = {"FAKE_SECRET": "src/web/api.py", "FAKE_DROP": "src/web/api.py", "FAKE_EXTRA": "unrequested.txt", "exit": "exited 3"}[marker]
    assert named in json.dumps(verdict)
    assert not packs_dir(repo).exists() or list(packs_dir(repo).iterdir()) == []


def test_bandit_finding_refuses_pack(run, repo: Path, packs):
    ready(run, repo)
    regraph(repo, **{"src__web__api.py": "a = 1\npw = 'FAKE_PASSWORD hunter2'\n"})
    verdict = pack(repo)
    assert not verdict["ok"] and verdict["findings"] == ["src/web/api.py:2 B105"] and "hunter2" not in json.dumps(verdict)
    assert any("bandit==" in c for c in packs.calls()) and not any(c.startswith("repomix ") for c in packs.calls())


@pytest.mark.parametrize("marker", ["FAKE_BANDIT_CRASH", "FAKE_BANDIT_GARBAGE"])
def test_bandit_failure_refuses(run, repo: Path, packs, marker):
    ready(run, repo)
    regraph(repo, **{"src__web__api.py": f"# {marker}\n"})
    verdict = pack(repo)
    assert not verdict["ok"] and "bandit" in verdict["reason"]


def test_bandit_skipped_without_py_files(run, repo: Path, packs):
    ready(run, repo)
    commit_files(repo, **{"sdlc__feat__intent.md": INTENT.replace("src/web/api.py", "docs/guide.md")})
    verdict = pack(repo)
    assert verdict["ok"] and not any("bandit==" in c for c in packs.calls())  # the tmp path holds the test name
