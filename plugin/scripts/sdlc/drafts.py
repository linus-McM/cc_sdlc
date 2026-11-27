"""Mechanical stage-document sources: the build, deploy and maintain documents are a direct mapping of a list or a
TOML table, so Python writes their Archify JSON and no model authors them. `docs.draft` and `docs.render` call `source`;
the plan, design and test documents are a reading of prose and stay with the recipe."""

from __future__ import annotations

from itertools import pairwise
from pathlib import Path

from . import artifacts as a
from . import project as p
from .project import fail

STAGES = ("build", "deploy", "maintain")
MARK = "Drafted by sdlc from"  # first provenance item of a mechanical draft; `docs.render` redrafts a source that still carries it
COLUMNS = {1: [5], 2: [0, 5], 3: [0, 2, 5], 4: [0, 2, 3, 5]}  # node columns the fixed workflow layout holds without overlap
MAX_NODES = max(COLUMNS)
TIER_STATE = {"free": ("active", "record"), "ask": ("decision", "AskUserQuestion"), "gate": ("waiting", "rehearsed + asked")}


def clip(text: str, limit: int) -> str:
    """One line, cut on a word boundary at `limit` characters."""
    text = " ".join(text.split())
    if len(text) <= limit:
        return text
    return text[:limit].rsplit(" ", 1)[0].rstrip(" ,;:-") or text[:limit]


def provenance(root: Path, stage: str, digest: str, *paths: Path) -> dict:
    return {
        "dot": "slate",
        "title": "Provenance",
        "items": [f"{MARK} {stage} sources @ {digest[:12]}; a mechanical draft, the acceptor decides", "Source: " + ", ".join(p.rel(root, path) for path in paths)],
    }


def listed(items: list[str], limit: int, more: str) -> list[str]:
    shown = [clip(item, 64) for item in items[:limit]]
    return [*shown, f"{len(items) - limit} more {more}"] if len(items) > limit else shown


def steps(plan: str) -> list[str]:
    """The list items of plan.md's Order of work, markers stripped."""
    lines = (line.strip() for line in a.sections(plan).get("Order of work", "").splitlines())
    return [a.BULLET.sub("", line).strip() for line in lines if a.BULLET.match(line)]


def build(root: Path, owner: Path, digest: str) -> dict:
    """Workflow: the Order of work as one rail (grouped to four nodes at most), and the red, green, sync + commit loop every step runs."""
    plan = owner / "plan.md"
    todo = steps(plan.read_text()) if plan.exists() else []
    if not todo:
        fail("plan.md 'Order of work' has no list items to draft the build document from; write the steps as a list")
    size = -(-len(todo) // MAX_NODES)
    groups = [todo[i : i + size] for i in range(0, len(todo), size)]
    nodes = []
    for i, group in enumerate(groups):
        first = i * size + 1
        label = f"Step {first}" if len(group) == 1 else f"Steps {first}-{first + len(group) - 1}"
        nodes.append({"id": f"s{i + 1}", "lane": "work", "col": COLUMNS[len(groups)][i], "type": "backend", "label": label, "sublabel": clip(group[0], 20)})
    ids = [n["id"] for n in nodes]
    loop = [
        {"id": "red", "lane": "loop", "col": 0, "type": "security", "label": "build red", "sublabel": "test fails first"},
        {"id": "green", "lane": "loop", "col": 2, "type": "backend", "label": "build green", "sublabel": "smallest change"},
        {"id": "commit", "lane": "loop", "col": 5, "type": "database", "label": "sync + commit", "sublabel": "plan.md in step"},
    ]
    edges = [{"from": x, "to": y} for x, y in pairwise(ids)]
    edges.append({"from": ids[-1], "to": "commit", "label": "all green", "route": "drop", "fromSide": "bottom", "toSide": "top", "variant": "emphasis"})
    edges.append({"from": "red", "to": "green", "label": "fix", "variant": "security"})
    title = a.title(plan.read_text())
    return {
        "schema_version": 1,
        "diagram_type": "workflow",
        "meta": {
            "title": clip(f"{title}: build order", 60),
            "views": [
                {"id": "order", "label": "Order of work", "focus": ids, "note": clip(f"{len(todo)} steps from plan.md, in order; each names the failing test written first.", 140)},
                {"id": "loop", "label": "Red to green", "focus": ["red", "green", "commit"], "note": "Every step: failing test, build red, smallest change, build green, plan sync, commit."},
            ],
        },
        "lanes": [{"id": "work", "label": "Order of work"}, {"id": "loop", "label": "Per step", "variant": "exception"}],
        "mainPath": [*ids, "commit"],
        "nodes": [*nodes, *loop],
        "edges": edges,
        "cards": [provenance(root, "build", digest, plan), {"dot": "emerald", "title": "Order of work", "items": listed(todo, 6, "steps in plan.md")}],
    }


def deploy(root: Path, owner: Path, digest: str) -> dict:
    """Lifecycle: one state per environment tier from `[deploy.environments]`, the approval gate, and the rehearsed rollback."""
    conf = p.config(root)["deploy"]
    envs = list(conf["environments"].items())
    if not 1 <= len(envs) <= 3:
        fail(f"the deploy draft lays out one to three environments, not {len(envs)}; author the document by the recipe")
    if unknown := [f"{env} = {tier!r}" for env, tier in envs if tier not in TIER_STATE]:
        fail(f"unknown tier in [deploy.environments]: {', '.join(unknown)}")
    rail = [{"id": "pr", "type": "start", "label": "PR open", "sublabel": "review + CI", "lane": "main", "col": 0, "step": "01", "tag": "babysit"}]
    for i, (env, tier) in enumerate(envs, 1):
        kind, tag = TIER_STATE[tier]
        rail.append({"id": f"env{i}", "type": kind, "label": clip(env, 14), "sublabel": f"tier {tier}", "lane": "main", "col": i, "step": f"{i + 1:02d}", "tag": tag})
    rail.append({"id": "live", "type": "success", "label": "Live", "sublabel": "maintain watches", "lane": "main", "col": 4, "step": f"{len(envs) + 2:02d}", "tag": "/sdlc:maintain"})
    gates = [i for i, (_, tier) in enumerate(envs, 1) if tier == "gate"]
    if gates[:1] == [1]:
        fail(f"the deploy draft has no layout for a gate on the first environment ({envs[0][0]}); author the document by the recipe")
    before = f"env{gates[0] - 1}" if gates else f"env{len(envs)}"  # the rollback is rehearsed in the tier before the first gate
    side = [
        {"id": "rehearsal", "type": "active", "label": "Rehearsal", "sublabel": "throwaway worktree", "lane": "recovery", "col": 0, "tag": "deploy rehearse"},
        {"id": "rollback", "type": "active", "label": "Rolling back", "sublabel": "same command, live", "lane": "recovery", "col": 2, "tag": "3-sigma breach"},
        {"id": "restored", "type": "success", "label": "Restored", "sublabel": "previous release", "lane": "terminal", "col": 2, "tag": "terminal"},
    ]
    moves = [
        {"from": before, "to": "rehearsal", "variant": "emphasis"},
        {"from": "live", "to": "rollback", "variant": "dashed"},
        {"from": "rollback", "to": "restored", "variant": "emphasis"},
    ]
    if gates:
        side += [
            {"id": "approval", "type": "waiting", "label": "Approval", "sublabel": "the user confirms", "lane": "waiting", "col": 1, "tag": "hook + gate"},
            {"id": "failed", "type": "failure", "label": "Blocked", "sublabel": "reasons quoted", "lane": "terminal", "col": 1, "tag": "never worked around"},
        ]
        moves += [{"from": f"env{gates[0]}", "to": "approval", "variant": "security"}, {"from": "approval", "to": "failed", "variant": "security"}]
    body = owner / "pr-body.md"
    title = body.read_text().splitlines()[0].lstrip("# ").strip() if body.exists() and body.read_text().strip() else owner.name
    gated = [env for env, tier in envs if tier == "gate"]
    release = [clip(title, 64), f"rollback: {clip(conf['rollback'], 50)}" if conf["rollback"] else "rollback: not configured", *(f"{env} asks first, after a rehearsed rollback" for env in gated)]
    return {
        "schema_version": 1,
        "diagram_type": "lifecycle",
        "meta": {
            "title": clip(f"{title}: deploy lifecycle", 60),
            "viewBox": [980, 680],
            "views": [
                {"id": "tiers", "label": "Environment tiers", "focus": [s["id"] for s in rail], "note": clip("; ".join(f"{env} is {tier}" for env, tier in envs) + "; every deploy is recorded in deploy.json.", 140)},
                {
                    "id": "rollback",
                    "label": "Rehearsed rollback",
                    "focus": [before, "rehearsal", "live", "rollback", "restored"],
                    "note": "The rollback is proven in a throwaway worktree before production; maintain calls the same command on a 3-sigma breach.",
                },
            ],
        },
        "lanes": [{"id": "main", "label": "Release rail"}, {"id": "waiting", "label": "Gates + waits"}, {"id": "recovery", "label": "Rollback"}, {"id": "terminal", "label": "Terminal exits"}],
        "states": [*rail, *side],
        "transitions": moves,
        "cards": [provenance(root, "deploy", digest, body), {"dot": "emerald", "title": "This release", "items": release}],
    }


def maintain(root: Path, owner: Path, digest: str) -> dict:
    """Lifecycle: the fixed reading-to-action rail, with the metrics `sdlc/bands.toml` watches on a card."""
    from . import maintain as bands  # maintain imports docs, which imports this module

    metrics = bands.bands(root)
    watched = [f"{name} (bad = {band.get('bad', bands.DEFAULT_BAND['bad'])}, window {band.get('window', bands.DEFAULT_BAND['window'])})" for name, band in metrics.items()]
    down = {"route": "straight", "fromSide": "bottom", "toSide": "top"}
    return {
        "schema_version": 1,
        "diagram_type": "lifecycle",
        "meta": {
            "title": "Maintain: control bands",
            "viewBox": [980, 680],
            "views": [
                {
                    "id": "rail",
                    "label": "Reading to action",
                    "focus": ["ingest", "baseline", "watch", "diagnose", "propose"],
                    "note": "Every reading in metrics.jsonl is scored against a rolling baseline; the tier decides the action, never a model.",
                },
                {"id": "tiers", "label": "Tiers", "focus": ["watch", "log", "diagnose", "sitrep", "propose"], "note": "1-sigma logs, 2-sigma diagnoses read-only with a three-line SITREP, 3-sigma proposes."},
                {
                    "id": "loop",
                    "label": "Closing the loop",
                    "focus": ["propose", "intent", "rollback"],
                    "note": "propose writes the next intent.md and returns to /sdlc:plan; the rehearsed rollback runs only inside a breach window.",
                },
            ],
        },
        "lanes": [{"id": "main", "label": "Watch rail"}, {"id": "waiting", "label": "Tier actions"}, {"id": "terminal", "label": "Outcomes"}],
        "states": [
            {"id": "ingest", "type": "start", "label": "Reading", "sublabel": "metrics.jsonl", "lane": "main", "col": 0, "step": "01", "tag": "ingest / refresh"},
            {"id": "baseline", "type": "active", "label": "Baseline", "sublabel": "rolling window", "lane": "main", "col": 1, "step": "02", "tag": "bands.toml"},
            {"id": "watch", "type": "decision", "label": "Watch", "sublabel": "Western Electric", "lane": "main", "col": 2, "step": "03", "tag": "pure Python"},
            {"id": "diagnose", "type": "waiting", "label": "Diagnose", "sublabel": "2-sigma, read-only", "lane": "main", "col": 3, "step": "04", "tag": "lessons.md first"},
            {"id": "propose", "type": "active", "label": "Propose", "sublabel": "3-sigma", "lane": "main", "col": 4, "step": "05", "tag": "next intent.md"},
            {"id": "log", "type": "neutral", "label": "Log", "sublabel": "1-sigma, do nothing", "lane": "waiting", "col": 0, "tag": "note"},
            {"id": "intent", "type": "external", "label": "Next intent.md", "sublabel": "evidence attached", "lane": "waiting", "col": 2, "tag": "/sdlc:plan"},
            {"id": "sitrep", "type": "neutral", "label": "SITREP", "sublabel": "three lines, no change", "lane": "terminal", "col": 1, "tag": "read, then decide"},
            {"id": "rollback", "type": "success", "label": "Rolled back", "sublabel": "rehearsed command", "lane": "terminal", "col": 2, "tag": "breach window only"},
        ],
        "transitions": [
            {"from": "watch", "to": "log", "variant": "dashed", **down},
            {"from": "diagnose", "to": "sitrep", "variant": "default", **down},
            {"from": "propose", "to": "intent", "variant": "emphasis", **down},
            {"from": "intent", "to": "rollback", "variant": "security", **down},
        ],
        "cards": [
            provenance(root, "maintain", digest, owner / "bands.toml"),
            {"dot": "cyan", "title": "Bands watched here", "items": listed(watched, 6, "metrics in bands.toml") or ["no metrics in sdlc/bands.toml yet"]},
        ],
    }


BUILDERS = {"build": build, "deploy": deploy, "maintain": maintain}


def source(root: Path, owner: Path, stage: str, digest: str, quality: str) -> dict:
    """The Archify JSON source for a drafted stage, carrying the configured quality profile."""
    data = BUILDERS[stage](root, owner, digest)
    data["meta"]["quality_profile"] = quality
    return data
