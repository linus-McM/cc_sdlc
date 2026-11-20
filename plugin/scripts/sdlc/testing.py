"""Test-stage mechanics: run the feedback loop, write test-report.json, validate review.md."""

from __future__ import annotations

import re
import shutil
from pathlib import Path

from . import artifacts as a
from . import build, docs, knowledge, packs
from . import project as p
from .project import fail


def report(feature: Path) -> dict | None:
    return p.read_json(feature / "test-report.json")


def run(root: Path, feature: Path) -> dict:
    cfg = p.config(root)
    n_cycles = build.cycles(p.read_jsonl(feature / "tdd.jsonl"))
    if cfg["build"]["require_tdd"] and n_cycles == 0:
        fail("no red->green cycle recorded; run `build red <step>` before implementing")
    if build.simplify_required(root) and not build.simplified(p.read_jsonl(feature / "tdd.jsonl")):
        fail("/simplify has not run since the last green step; run `/simplify` over the branch diff, then `sdlc build simplify`", next="sdlc build simplify")
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
    verdict = {
        "ok": True,
        "failed": [],
        "results": [{"name": r["name"], "exit": r["exit"]} for r in results],  # the tails are in test-report.json
        "next": "write sdlc/<slug>/review.md against REVIEW.md, then `test review`",
    }
    if ensure_review_md(root):
        verdict["review_md"] = "REVIEW.md created from the plugin template"
    return verdict


def ensure_review_md(root: Path) -> bool:
    """Copy the template REVIEW.md to the project root when there is none; true when it was created."""
    path = root / "REVIEW.md"
    if path.exists():
        return False
    shutil.copyfile(p.TEMPLATES / "REVIEW.md", path)
    return True


def knowledge_result(root: Path) -> dict:
    """The OKF conformance check as one more feedback-loop row; only conformance findings fail it."""
    verdict = knowledge.check(root)
    lines = [*verdict.get("conformance", []), *(f"policy: {x}" for x in verdict.get("policy", []))]
    tail = "\n".join([f"conformance: {len(verdict.get('conformance', []))} policy: {len(verdict.get('policy', []))} trust: {verdict.get('trust')}", *lines[-19:]])
    return {"name": "knowledge", "cmd": "sdlc knowledge check", "exit": 0 if verdict["ok"] else 1, "tail": tail}


IMPORTANT = re.compile(r"^\s*[-*]\s*Important:.*$", re.MULTILINE)
ACCEPTED = re.compile(r"\baccepted:\s*[^\s,][^,]*,\s*\S")  # a named person and their reason
RESOLVED = re.compile(rf"\bfixed:\s*\S|{ACCEPTED.pattern}")


def count(text: str, tag: str) -> int:
    """Findings tagged `- Important:` / `- Nit:` in a review.md body."""
    return len(re.findall(rf"^\s*[-*]\s*{tag}:", text, re.MULTILINE))


def findings(feature: Path) -> dict:
    """review.md validated against REVIEW.md's three passes, with its finding counts."""
    path = feature / "review.md"
    if not path.exists():
        fail("review.md missing; run the review passes from REVIEW.md and write the findings")
    text = path.read_text()
    if problems := a.validate(text, a.REQUIRED["review.md"]):
        fail("; ".join(problems), problems=problems)
    important = IMPORTANT.findall(text)
    still = [line.strip() for line in important if not RESOLVED.search(line)]
    return {"important": len(important), "nits": count(text, "Nit"), "open": still, "accepted": sum(bool(ACCEPTED.search(line)) for line in important)}


def review(root: Path, feature: Path) -> dict:
    """The test stage's exit: valid findings plus a fresh stage document."""
    counts = findings(feature)
    if still := counts.pop("open"):
        fail(
            f"{len(still)} Important finding(s) still open in review.md; fix each with a red->green cycle and end its line with `fixed: <commit or note>`, or have the person who takes the risk end it with `accepted: <name>, <reason>`",
            open=still,
        )
    docs.check(root, feature, "test")
    pack = packs.require(root, feature, "test")
    return {"ok": True, **counts, "path": str(feature / "review.md"), "pack": pack, "next": "/sdlc:deploy"}
