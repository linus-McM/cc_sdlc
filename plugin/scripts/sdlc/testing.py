"""Test-stage mechanics: run the feedback loop, write test-report.json, validate review.md."""

from __future__ import annotations

import os
import re
import shutil
from pathlib import Path

from . import artifacts as a
from . import build, knowledge, packs
from . import project as p
from .project import fail


def report(feature: Path) -> dict | None:
    return p.read_json(feature / "test-report.json")


def run(root: Path, feature: Path) -> dict:
    cfg = p.config(root)
    log = p.read_jsonl(feature / "tdd.jsonl")
    n_cycles = build.cycles(log)
    if cfg["build"]["require_tdd"] and n_cycles == 0:
        fail("no red->green cycle recorded; run `build red <step>` before implementing")
    if cfg["build"]["require_tdd"] and (missing := build.missing_steps(feature, log)):
        fail(f"no red->green cycle for plan.md step(s) {', '.join(missing)}; run `build red <n>` then `build green <n>` for each, or take the step out of plan.md", missing=missing)
    if untouched := build.untouched(root, feature):
        fail("plan.md lists files the build never changed; change them, or take them out of 'Files that change'", untouched=untouched)
    deviations = build.deviations(feature)
    if build.simplify_required(root) and not build.simplified(log):
        fail("/simplify has not run since the last green step; run `/simplify` over the branch diff, then `sdlc build simplify`", next="sdlc build simplify")
    results = [{"name": n, **build.run_cmd(root, cmd)} for n in ("test", "lint", "build") if (cmd := cfg["commands"][n])]
    if knowledge.enabled(root):
        results.append(knowledge_result(root))
    failed = [r["name"] for r in results if r["exit"] != 0]
    p.write_json(
        feature / "test-report.json",
        {"passed": not failed, "results": results, "cycles": n_cycles, "deviations": deviations, "ts": p.today()},
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
    if deviations:
        verdict["deviations"] = deviations  # plan.md no longer matches what was approved: reported, never refused
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


DONE = "complete: the feature is built, tested and reviewed. /sdlc:deploy is optional"
IMPORTANT = re.compile(r"^\s*[-*]\s*Important:.*$", re.MULTILINE)
WONTFIX = re.compile(r"\bwontfix:\s*\S")  # left as it is, with the reason
RESOLVED = re.compile(rf"\bfixed:\s*\S|{WONTFIX.pattern}")


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
    spec = feature / "spec.md"
    wanted = a.requirement_ids(spec.read_text()) if spec.exists() else []
    if missing := [f"R{n}" for n in wanted if n not in a.cited(a.sections(text)["Compliance"])]:
        fail(f"review.md Compliance gives no verdict on {', '.join(missing)}; add one line per spec.md requirement: `- R<n>: met, <evidence>` or `- Important: R<n> ...`", missing=missing)
    important = IMPORTANT.findall(text)
    still = [line.strip() for line in important if not RESOLVED.search(line)]
    return {"important": len(important), "nits": count(text, "Nit"), "open": still, "wontfix": sum(bool(WONTFIX.search(line)) for line in important)}


def builtin_missing(root: Path, feature: Path) -> list[str]:
    """Built-in Claude Code review skills with no line under review.md "## Built-in review". Python cannot see the skill
    run; the line is Claude's record that it ran and its findings were merged into the passes."""
    if os.environ.get("SDLC_BUILTIN_REVIEW") == "off":
        return []
    body = a.sections((feature / "review.md").read_text()).get("Built-in review", "")
    return [f"/{name}" for name in p.config(root)["test"]["builtin_review"] if not re.search(rf"^\s*[-*]\s*/{re.escape(name)}\b", body, re.MULTILINE)]


def review(root: Path, feature: Path) -> dict:
    """The test stage's exit, and the end of the loop: every requirement has a verdict and no Important finding is open."""
    counts = findings(feature)
    if missing := builtin_missing(root, feature):
        fail(
            f"review.md records no {', '.join(missing)} pass; run each skill over the branch, merge its findings into Bugs and Security, and add one line per skill under `## Built-in review`: `- /<skill>: <count> findings, merged` or `- /<skill>: none`",
            missing=missing,
        )
    if still := counts.pop("open"):
        fail(
            f"{len(still)} Important finding(s) still open in review.md; fix each with a red->green cycle and end its line with `fixed: <commit or note>`, or end it with `wontfix: <reason>` when the user decides to leave it",
            open=still,
        )
    pack = p.attempt(packs.require, root, feature, "test")  # the pack itself is advice; a committed secret is not
    if pack.get("secrets"):
        fail(pack["reason"], secrets=pack["secrets"])
    verdict = {"ok": True, **counts, "path": str(feature / "review.md"), "pack": pack, "complete": True, "next": DONE}
    if deviations := build.deviations(feature):
        verdict["deviations"] = deviations
    return verdict
