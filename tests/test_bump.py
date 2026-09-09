import json
import sys
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
import bump_version as bv


@pytest.fixture
def tree(tmp_path: Path) -> Path:
    (tmp_path / ".claude-plugin").mkdir()
    (tmp_path / "plugin/.claude-plugin").mkdir(parents=True)
    (tmp_path / "plugin/.claude-plugin/plugin.json").write_text('{\n  "name": "sdlc",\n  "version": "0.2.0"\n}\n')
    (tmp_path / ".claude-plugin/marketplace.json").write_text('{"plugins": [{"name": "sdlc", "version": "0.2.0"}]}\n')
    (tmp_path / "pyproject.toml").write_text('[project]\nname = "sdlc-plugin"\nversion = "0.1.0"\nrequires-python = ">=3.11"\n')
    return tmp_path


def test_bump_parts():
    assert bv.bump("0.2.0", "patch") == "0.2.1"
    assert bv.bump("0.2.9", "minor") == "0.3.0"
    assert bv.bump("1.4.2", "major") == "2.0.0"
    with pytest.raises(ValueError):
        bv.bump("0.2", "patch")


def test_write_syncs_every_version_file(tree: Path):
    assert bv.current(tree) == "0.2.0"  # plugin.json is the source of truth
    written = bv.write(tree, "0.2.1")
    assert sorted(p.name for p in written) == ["marketplace.json", "plugin.json", "pyproject.toml"]
    assert json.loads((tree / "plugin/.claude-plugin/plugin.json").read_text())["version"] == "0.2.1"
    assert json.loads((tree / ".claude-plugin/marketplace.json").read_text())["plugins"][0]["version"] == "0.2.1"
    assert 'version = "0.2.1"' in (tree / "pyproject.toml").read_text()
    assert (tree / "plugin/.claude-plugin/plugin.json").read_text().startswith("{\n  ")  # formatting kept


def test_main_bumps_only_when_head_equals_base(tree: Path, capsys):
    assert bv.main(["--root", str(tree), "--base", "0.2.0", "--part", "patch"]) == 0
    assert "0.2.0 -> 0.2.1" in capsys.readouterr().out
    assert bv.current(tree) == "0.2.1"
    assert bv.main(["--root", str(tree), "--base", "0.2.0", "--part", "patch"]) == 0
    assert "already ahead" in capsys.readouterr().out and bv.current(tree) == "0.2.1"
    assert bv.main(["--root", str(tree), "--base", "0.3.0", "--part", "patch"]) == 1  # head behind base: refuse
    assert "behind" in capsys.readouterr().out


def test_part_from_labels():
    assert bv.part_from_labels(["bug", "release:minor"]) == "minor"
    assert bv.part_from_labels(["release:major", "release:minor"]) == "major"
    assert bv.part_from_labels([]) == "patch"
