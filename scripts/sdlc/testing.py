"""Test-stage mechanics: run the feedback loop, write test-report.json, validate review.md."""

from __future__ import annotations

import re
from pathlib import Path

from . import artifacts as a
from . import build, knowledge
from . import project as p
from .project import fail


def report(feature: Path) -> dict | None:
    return p.read_json(feature / "test-report.json")


def run(root: Path, feature: Path) -> dict:
    cfg = p.config(root)
    n_cycles = build.cycles(p.read_jsonl(feature / "tdd.jsonl"))
    if cfg["build"]["require_tdd"] and n_cycles == 0:
        fail("no red->green cycle recorded; run `build red <step>` before implementing")
    results = [{"name": n, **build.run_cmd(root, cmd)} for n in ("test", "lint", "build") if (cmd := cfg["commands"][n])]
    if knowledge.enabled(root):
        results.append(knowledge_result(root))
    failed = [r["name"] for r in results if r["exit"] != 0]
    p.write_json(
        feature / "test-report.json",
        {"passed": not failed, "results": results, "cycles": n_cycles, "ts": p.today()},
    )
    if failed:
        fail("checks failed: fix the code, not the tests", failed=failed, results=results)
    p.attempt(knowledge.publish, root, feature, "process:sdlc-test")
    return {
        "ok": True,
        "failed": [],
        "results": results,
        "next": "write sdlc/<slug>/review.md against REVIEW.md, then `test review`",
    }


def knowledge_result(root: Path) -> dict:
    """The OKF conformance check as one more feedback-loop row; only conformance findings fail it."""
    verdict = knowledge.check(root)
    lines = [*verdict.get("conformance", []), *(f"policy: {x}" for x in verdict.get("policy", []))]
    tail = "\n".join([f"conformance: {len(verdict.get('conformance', []))} policy: {len(verdict.get('policy', []))} trust: {verdict.get('trust')}", *lines[-19:]])
    return {"name": "knowledge", "cmd": "sdlc knowledge check", "exit": 0 if verdict["ok"] else 1, "tail": tail}


def count(text: str, tag: str) -> int:
    """Findings tagged `- Important:` / `- Nit:` in a review.md body."""
    return len(re.findall(rf"^\s*[-*]\s*{tag}:", text, re.MULTILINE))


def review(feature: Path) -> dict:
    path = feature / "review.md"
    if not path.exists():
        fail("review.md missing; run the review passes from REVIEW.md and write the findings")
    text = path.read_text()
    if problems := a.validate(text, a.REQUIRED["review.md"]):
        fail("; ".join(problems), problems=problems)

    return {
        "ok": True,
        "important": count(text, "Important"),
        "nits": count(text, "Nit"),
        "next": "/sdlc:deploy",
    }
