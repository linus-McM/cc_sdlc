"""Graph-selected Repomix context packs: seeds, one-hop expansion, secret guards, the pack, and its gates."""

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
    import json

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
