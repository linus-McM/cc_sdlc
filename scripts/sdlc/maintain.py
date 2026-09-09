"""Maintain-stage mechanics: deterministic control bands that close the loop back to Plan."""

from __future__ import annotations

import statistics
import tomllib
from pathlib import Path

from . import artifacts as a
from . import docs, stages
from . import project as p
from .project import fail

DEFAULT_BAND = {
    "window": 30,
    "tiers": ["log", "diagnose", "propose"],
    "bad": "both",
}  # tiers[i] = action at (i+1) sigma; bad = which side of the mean counts as a breach
SIDES = {"high": (1,), "low": (-1,), "both": (1, -1)}
MIN_HISTORY = 5
SPAN = 8  # longest rule span; the baseline excludes these trailing points when history allows


def tier(values: list[float], window: int = 30, bad: str = "both") -> int:
    """Western Electric rules on the trailing points against a rolling baseline.

    3: one point beyond 3σ. 2: two of three beyond 2σ, same side. 1: four of five beyond 1σ
    same side, or eight consecutive on one side of the mean. 0: in control or too little history.
    Only the `bad` side of the mean counts (`high`, `low` or `both`).
    """
    if len(values) <= MIN_HISTORY:
        return 0
    signs = SIDES[bad]
    head = values[:-SPAN] if len(values) - SPAN >= MIN_HISTORY else values[:-1]
    baseline = head[-window:]
    mean, std = statistics.mean(baseline), statistics.pstdev(baseline)
    if std == 0:
        return 3 if any((values[-1] - mean) * s > 0 for s in signs) else 0
    z = [(v - mean) / std for v in values[-SPAN:]]

    def beyond(n: int, k: int, limit: float) -> bool:
        tail = z[-n:]
        return len(tail) == n and any(sum(x * s > limit for x in tail) >= k for s in signs)

    if beyond(1, 1, 3):
        return 3
    if beyond(3, 2, 2):
        return 2
    if beyond(5, 4, 1) or beyond(SPAN, SPAN, 0):
        return 1
    return 0


def bands(root: Path) -> dict:
    """Per-metric bands from sdlc/bands.toml, validated at the config boundary."""
    path = p.home(root) / "bands.toml"
    metrics = tomllib.loads(path.read_text()).get("metrics", {}) if path.exists() else {}
    for name, band in metrics.items():
        if band.get("bad", "both") not in SIDES:
            fail(f"bands.toml metrics.{name}.bad must be one of {sorted(SIDES)}, not {band['bad']!r}")
    return metrics


def readings(root: Path, metric: str | None) -> dict[str, list[float]]:
    out: dict[str, list[float]] = {}
    for row in p.read_jsonl(root / p.config(root)["maintain"]["metrics"]):
        if metric is None or row["metric"] == metric:
            out.setdefault(row["metric"], []).append(float(row["value"]))
    return out


def watch(root: Path, metric: str | None) -> dict:
    cfg = bands(root)
    results = []
    for name, values in readings(root, metric).items():
        band = {**DEFAULT_BAND, **cfg.get(name, {})}
        level = tier(values, band["window"], band["bad"])
        action = "none" if level == 0 else band["tiers"][level - 1]
        results.append(
            {
                "metric": name,
                "tier": level,
                "action": action,
                "latest": values[-1],
                "n": len(values),
            }
        )
    verdict = {
        "ok": True,
        "metrics": results,
        "breaches": [r["metric"] for r in results if r["action"] == "propose"],
    }
    document = p.attempt(docs.check, root, p.home(root), "maintain")  # never gates a watch; the acceptor sees why the document is behind
    if not document["ok"]:
        verdict["docs"] = document["reason"]
    return verdict


def propose(root: Path, metric: str) -> dict:
    found = watch(root, metric)["metrics"]
    if not found:
        fail(f"no readings for metric {metric!r}")
    rep = found[0]
    if rep["action"] != "propose":
        fail(f"{metric} is at tier {rep['tier']} ({rep['action']}); propose needs the propose tier")
    created = stages.new("plan", root, f"Incident: {metric} breach {p.today()}", None)
    path = Path(created["path"])
    evidence = f"Control band breach: {metric} at tier {rep['tier']}, latest={rep['latest']} over n={rep['n']} readings."
    path.write_text(a.set_section(a.set_meta(path.read_text(), "Risk", "high"), "Problem", evidence))
    return {**created, "next": "/sdlc:plan"}


def ingest(root: Path, metric: str, value: float) -> dict:
    p.append_jsonl(
        root / p.config(root)["maintain"]["metrics"],
        {"metric": metric, "value": value, "ts": p.today()},
    )
    return {"ok": True, "metric": metric, "value": value}


def lesson(root: Path, text: str) -> dict:
    path = p.home(root, create=True) / "lessons.md"
    if not path.exists():
        path.write_text("# Lessons\nAppend-only incident log: root cause, fix, gotchas. Read first when diagnosing.\n\n")
    with path.open("a") as fh:
        fh.write(f"- {p.today()}: {text}\n")
    return {"ok": True, "path": str(path)}
