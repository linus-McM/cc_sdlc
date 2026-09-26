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
