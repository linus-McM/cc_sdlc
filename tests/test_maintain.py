import json
from pathlib import Path

from sdlc import maintain as m


def series(repo: Path, name: str, values: list[float]) -> None:
    lines = [json.dumps({"metric": name, "value": v, "ts": f"2026-09-{i + 1:02d}"}) for i, v in enumerate(values)]
    (repo / "sdlc").mkdir(exist_ok=True)
    (repo / "sdlc/metrics.jsonl").write_text("\n".join(lines) + "\n")


BASE = [10.0, 11.0, 9.0, 10.0, 11.0, 9.0, 10.0, 10.0, 11.0, 9.0]  # mean 10, std ~0.77


def test_western_electric_rules_classify_tiers():
    assert m.tier([*BASE, 10.0]) == 0
    assert m.tier([*BASE, 20.0]) == 3  # one point beyond 3σ
    assert m.tier([*BASE, 12.0, 10.0, 12.0]) == 2  # 2 of 3 beyond 2σ, same side
    assert m.tier([*BASE, 11.5, 11.5, 10.0, 11.5, 11.5]) == 1  # 4 of 5 beyond 1σ
    assert m.tier(BASE + [10.1] * 8) == 1  # 8 consecutive same side


def test_tier_needs_enough_history():
    assert m.tier([1.0, 2.0]) == 0


def test_watch_reads_bands_and_reports_actions(run, repo: Path):
    series(repo, "ci_test_failure_rate", [*BASE, 20.0])
    for v in [*BASE, 10.0]:
        run("maintain", "ingest", "p95_ms", "--value", v)
    out = run("maintain", "watch")
    by_name = {r["metric"]: r for r in out["metrics"]}
    assert by_name["ci_test_failure_rate"]["tier"] == 3
    assert by_name["ci_test_failure_rate"]["action"] == "propose"
    assert by_name["p95_ms"]["tier"] == 0 and by_name["p95_ms"]["action"] == "none"
    assert out["breaches"] == ["ci_test_failure_rate"]


def test_watch_honours_custom_bands(run, repo: Path):
    series(repo, "m", [*BASE, 12.0, 10.0, 12.0])
    (repo / "sdlc/bands.toml").write_text('[metrics.m]\nwindow = 10\ntiers = ["log", "propose", "propose"]\n')
    out = run("maintain", "watch", "m")
    assert out["metrics"][0]["tier"] == 2 and out["metrics"][0]["action"] == "propose"


def test_propose_writes_intent_and_closes_loop(run, repo: Path):
    series(repo, "ci_test_failure_rate", [*BASE, 20.0])
    out = run("maintain", "propose", "ci_test_failure_rate")
    assert out["ok"] and out["next"] == "/sdlc:plan"
    intent = (repo / "sdlc" / out["slug"] / "intent.md").read_text()
    assert intent.startswith("# Intent: Incident: ci_test_failure_rate")
    assert "3σ" in intent or "tier 3" in intent
    assert "Risk: high" in intent
    assert run("plan", "check")["ok"] is False  # human still fills constraints/outcome


def test_propose_refuses_below_threshold(run, repo: Path):
    series(repo, "m", [*BASE, 10.0])
    assert run("maintain", "propose", "m")["ok"] is False


def test_ingest_appends_metric(run, repo: Path):
    assert run("maintain", "ingest", "m", "--value", "4.5")["ok"]
    line = json.loads((repo / "sdlc/metrics.jsonl").read_text().splitlines()[-1])
    assert line["metric"] == "m" and line["value"] == 4.5


def test_lesson_appends_to_lessons_md(run, repo: Path):
    assert run("maintain", "lesson", "cache the claims endpoint")["ok"]
    text = (repo / "sdlc/lessons.md").read_text()
    assert "cache the claims endpoint" in text and text.startswith("# Lessons")
