"""Graph-selected Repomix context packs: seeds, one-hop expansion, secret guards, the pack, and its gates."""

from pathlib import Path

from sdlc import project as p


def test_pack_config_defaults(repo: Path):
    conf = p.config(repo)["knowledge"]
    assert conf["pack_max_tokens"] == 0 and conf["pack_hops"] == 1 and conf["pack_base"] == "main"


def test_run_cmd_passes_stdin(repo: Path):
    assert p.run_cmd(repo, ["cat"], input="a\nb").stdout == "a\nb"
