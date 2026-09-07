import json
import stat
from pathlib import Path


def fake_claude(repo: Path) -> None:
    bin_dir = repo / "bin"
    bin_dir.mkdir()
    script = bin_dir / "claude"
    script.write_text('#!/bin/sh\necho "$@" > "$CLAUDE_ARGS_LOG"\necho \'{"result": "done"}\'\n')
    script.chmod(script.stat().st_mode | stat.S_IEXEC)


def write_eval(repo: Path, name: str, check: str) -> None:
    (repo / "evals").mkdir(exist_ok=True)
    (repo / "evals" / f"{name}.json").write_text(
        json.dumps({"prompt": f"do {name}", "allowed_tools": ["Read"], "checks": [check]})
    )


def test_evals_run_all_and_gate_on_threshold(run, repo: Path, monkeypatch):
    fake_claude(repo)
    monkeypatch.setenv("SDLC_CLAUDE_BIN", str(repo / "bin/claude"))
    monkeypatch.setenv("CLAUDE_ARGS_LOG", str(repo / "args.log"))
    write_eval(repo, "a", "true")
    write_eval(repo, "b", "false")
    out = run("test", "evals")
    assert out["ok"] is False and out["pass_rate"] == 0.5
    assert [r["name"] for r in out["results"]] == ["a", "b"]
    assert "--allowedTools Read" in (repo / "args.log").read_text()
    report = json.loads((repo / "sdlc/evals-report.json").read_text())
    assert report["pass_rate"] == 0.5


def test_evals_pass_when_all_checks_green(run, repo: Path, monkeypatch):
    fake_claude(repo)
    monkeypatch.setenv("SDLC_CLAUDE_BIN", str(repo / "bin/claude"))
    monkeypatch.setenv("CLAUDE_ARGS_LOG", str(repo / "args.log"))
    write_eval(repo, "a", "true")
    assert run("test", "evals")["ok"] is True


def test_evals_without_suite_is_a_clear_failure(run, repo: Path):
    out = run("test", "evals")
    assert out["ok"] is False and "evals/" in out["reason"]
