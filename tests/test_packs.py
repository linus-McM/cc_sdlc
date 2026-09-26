"""Graph-selected Repomix context packs: seeds, one-hop expansion, secret guards, the pack, and its gates."""

import json
from pathlib import Path

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
