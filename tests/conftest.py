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
    monkeypatch.setenv("SDLC_KNOWLEDGE", "off")  # existing tests run with the knowledge layer off
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
                lines.append(f"{k} = {json.dumps(v)}")  # JSON scalars and lists are valid TOML values
        (repo / ".sdlc.toml").write_text("\n".join(lines) + "\n")

    return _write


FAKE_UV = """#!/bin/sh
echo "uv $*" >> "$(dirname "$0")/calls.log"
if [ "$1 $2 $3" = "tool install graphifyy" ]; then cp "$(dirname "$0")/graphify.hidden" "$(dirname "$0")/graphify"; fi
"""
FAKE_GRAPHIFY = """#!/bin/sh
BIN=$(dirname "$0")
echo "graphify $*" >> "$BIN/calls.log"
case "$1 $2" in
  "install --platform") mkdir -p "$CLAUDE_CONFIG_DIR/skills/graphify" && echo skill > "$CLAUDE_CONFIG_DIR/skills/graphify/SKILL.md" ;;
  "hook status") if grep -q graphify-hook-start .git/hooks/post-commit 2>/dev/null; then echo "post-commit: installed"; else echo "post-commit: not installed"; fi ;;
  "hook install") mkdir -p .git/hooks; printf '#!/bin/sh\\n# graphify-hook-start\\necho graphify\\n# graphify-hook-end\\n' >> .git/hooks/post-commit; chmod +x .git/hooks/post-commit; echo installed ;;
  "update .") mkdir -p graphify-out; sed "s/__COMMIT__/$(git rev-parse HEAD)/" "$BIN/graph.template.json" > graphify-out/graph.json; : > graphify-out/GRAPH_REPORT.md; : > graphify-out/graph.html; echo updated ;;
  "god-nodes --top") echo '[{"id": "src_app_core_run", "label": "run()", "degree": 3}, {"id": "src_web_api_get", "label": "get()", "degree": 2}]' ;;
  *) echo "fake graphify: $*" >&2; exit 1 ;;
esac
"""


class FakeTools:
    def __init__(self, bin_dir: Path, config_dir: Path):
        self.bin, self.config_dir = bin_dir, config_dir

    def calls(self) -> list[str]:
        log = self.bin / "calls.log"
        return log.read_text().splitlines() if log.exists() else []

    @property
    def skill(self) -> Path:
        return self.config_dir / "skills/graphify/SKILL.md"

    def uninstall(self, *names: str) -> None:
        for name in names:
            (self.bin / name).unlink(missing_ok=True)


@pytest.fixture
def knowledge(repo: Path, tmp_path: Path, monkeypatch) -> FakeTools:
    """Knowledge layer on, with fake `uv` and `graphify` on an otherwise bare PATH (plus git)."""
    monkeypatch.delenv("SDLC_KNOWLEDGE")
    bin_dir, home, config_dir = tmp_path / "bin", tmp_path / "home", tmp_path / "claude"
    bin_dir.mkdir()
    home.mkdir()
    (bin_dir / "uv").write_text(FAKE_UV)
    (bin_dir / "graphify.hidden").write_text(FAKE_GRAPHIFY)
    (bin_dir / "graph.template.json").write_text((Path(__file__).parent / "fixtures/graph.json").read_text())
    for script in ("uv", "graphify.hidden"):
        (bin_dir / script).chmod(0o755)
    git_dir = Path(subprocess.run(["which", "git"], capture_output=True, text=True, check=True).stdout.strip()).parent
    monkeypatch.setenv("PATH", f"{bin_dir}:{git_dir}:/usr/bin:/bin")
    monkeypatch.setenv("HOME", str(home))
    monkeypatch.setenv("CLAUDE_CONFIG_DIR", str(config_dir))
    monkeypatch.setenv("GRAPHIFY_SKIP_HOOK", "1")  # the installed post-commit blocks must not run in the background during tests
    return FakeTools(bin_dir, config_dir)
