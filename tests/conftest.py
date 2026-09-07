import json
import subprocess
from pathlib import Path

import pytest

from sdlc import artifacts, cli


@pytest.fixture
def repo(tmp_path: Path, monkeypatch) -> Path:
    """Fresh git repo with one commit; cwd and SDLC root point at it."""
    subprocess.run(["git", "init", "-q", "-b", "main"], cwd=tmp_path, check=True)
    subprocess.run(["git", "config", "user.email", "t@t"], cwd=tmp_path, check=True)
    subprocess.run(["git", "config", "user.name", "t"], cwd=tmp_path, check=True)
    (tmp_path / "README.md").write_text("x\n")
    subprocess.run(["git", "add", "-A"], cwd=tmp_path, check=True)
    subprocess.run(["git", "commit", "-qm", "init"], cwd=tmp_path, check=True)
    monkeypatch.chdir(tmp_path)
    return tmp_path


@pytest.fixture
def run(repo: Path):
    """Invoke the CLI in-process; return its JSON result dict."""

    def _run(*argv: str) -> dict:
        return cli.main([str(a) for a in argv], root=repo)

    return _run


def fill(path: Path, **sections: str) -> None:
    """Replace placeholder bodies under named sections with real text."""
    text = path.read_text()
    for heading, body in sections.items():
        text = artifacts.set_section(text, heading, body)
    path.write_text(text)


def load(path: Path) -> dict:
    return json.loads(path.read_text())


@pytest.fixture
def accepted_intent(run, repo: Path) -> str:
    run("plan", "new", "Feat")
    fill(
        repo / "sdlc/feat/intent.md",
        **{
            "Problem": "p",
            "Proposed outcome": "o",
            "Affected users and systems": "u",
            "Constraints": "c",
            "Open questions": "none",
        },
    )
    assert run("plan", "accept")["ok"]
    return "feat"


@pytest.fixture
def accepted_spec(run, repo: Path, accepted_intent) -> str:
    run("design", "new")
    fill(
        repo / "sdlc/feat/spec.md",
        Requirements="r",
        Design="d",
        Concerns="none",
        **{"Open questions": "none", "Proof": "tests/test_feat.py"},
    )
    assert run("design", "accept")["ok"]
    return "feat"


@pytest.fixture
def accepted_plan(run, repo: Path, accepted_spec) -> str:
    run("build", "new")
    fill(
        repo / "sdlc/feat/plan.md",
        **{
            "Files that change": "- src/feat.py (new)\n- tests/test_feat.py (new)",
            "Order of work": "1. failing test\n2. implement",
            "Risks": "none",
            "Proof": "tests/test_feat.py passes",
        },
    )
    assert run("build", "accept")["ok"]
    return "feat"


@pytest.fixture
def toml_config(repo: Path):
    def _write(**tables) -> None:
        lines = []
        for table, values in tables.items():
            lines.append(f"[{table}]")
            for k, v in values.items():
                lines.append(f"{k} = {v!r}" if isinstance(v, str) else f"{k} = {v}".replace("'", '"'))
        (repo / ".sdlc.toml").write_text("\n".join(lines) + "\n")

    return _write
