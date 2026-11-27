"""One entry point: `uv run --no-project scripts/sdlc.py <stage> <action> [arg]` prints a JSON verdict.

COMMANDS maps (stage, action) to (gate, handler). `gate` names the artifact that must already be
accepted (None = no feature needed); the handler receives (root, feature, arg, ns).
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

from . import build, checkpoint, deploy, docs, evals, handover, knowledge, maintain, packs, stages, testing, workflows
from .project import Blocked, attempt


def lifecycle(stage: str, action: str):
    """new/check/accept for an artifact stage; only `plan new` takes the positional title."""
    if action == "new":
        return lambda r, f, x, ns: stages.new(stage, r, x if stage == "plan" else None, ns.slug)
    return lambda r, f, x, ns: getattr(stages, action)(stage, r, ns.slug)


COMMANDS = {
    **{(s, act): (None, lifecycle(s, act)) for s in stages.ORDER for act in ("new", "check", "accept")},
    ("build", "red"): ("plan.md", lambda r, f, x, ns: build.tdd(r, f, "red", x or "unnamed", ns.only)),
    ("build", "green"): ("plan.md", lambda r, f, x, ns: build.tdd(r, f, "green", x or "unnamed", ns.only)),
    ("build", "sync"): ("plan.md", lambda r, f, x, ns: build.sync(r, f)),
    ("build", "simplify"): ("plan.md", lambda r, f, x, ns: build.simplify(r, f)),
    ("build", "fix"): ("plan.md", lambda r, f, x, ns: build.fix(f, x or "on")),
    ("test", "run"): ("plan.md", lambda r, f, x, ns: testing.run(r, f)),
    ("test", "review"): ("plan.md", lambda r, f, x, ns: testing.review(r, f)),
    ("test", "evals"): (None, lambda r, f, x, ns: evals.run(r)),
    ("deploy", "check"): ("plan.md", lambda r, f, x, ns: deploy.check(r, f, x or "dev")),
    ("deploy", "rehearse"): ("plan.md", lambda r, f, x, ns: deploy.rehearse(r, f)),
    ("deploy", "record"): ("plan.md", lambda r, f, x, ns: deploy.record(r, f, x or "dev")),
    ("deploy", "pr"): ("plan.md", lambda r, f, x, ns: deploy.pr_body(r, f)),
    ("maintain", "watch"): (None, lambda r, f, x, ns: maintain.watch(r, x)),
    ("maintain", "propose"): (None, lambda r, f, x, ns: maintain.propose(r, x)),
    ("maintain", "ingest"): (None, lambda r, f, x, ns: maintain.ingest(r, x, ns.value)),
    ("maintain", "lesson"): (None, lambda r, f, x, ns: maintain.lesson(r, x or "")),
    **{("docs", act): (None, docs.mechanic(act)) for act in ("draft", "render", "check", "open")},
    ("knowledge", "bootstrap"): (None, lambda r, f, x, ns: knowledge.bootstrap(r, check=x == "check", update=True)),
    ("knowledge", "status"): (None, lambda r, f, x, ns: knowledge.status(r)),
    ("knowledge", "refresh"): (None, lambda r, f, x, ns: knowledge.refresh(r)),
    ("knowledge", "check"): (None, lambda r, f, x, ns: knowledge.check(r)),
    ("knowledge", "unhook"): (None, lambda r, f, x, ns: knowledge.unhook(r)),
    ("knowledge", "pack"): (None, lambda r, f, x, ns: packs.build(r, ns.slug, x, ns.max_tokens)),
    ("workflows", "list"): (None, lambda r, f, x, ns: workflows.catalog(r)),
    ("workflows", "env"): (None, lambda r, f, x, ns: workflows.env(r)),
    ("workflows", "gate"): (None, lambda r, f, x, ns: workflows.gate(r, x)),
    ("status", None): (None, lambda r, f, x, ns: stages.status(r, ns.slug)),
}

# stage boundaries: after a successful run, checkpoint commits the verdict's `path` with this action label
BOUNDARIES = {
    **{(s, "accept"): "accept" for s in stages.ORDER},
    ("test", "review"): "review",
    ("deploy", "record"): "record {env}",
    ("maintain", "propose"): "propose",
    ("maintain", "lesson"): "lesson",
    ("knowledge", "refresh"): "refresh",
}
# each stage's first mechanic: its verdict carries the workflow gate and any knowledge tool that is missing, so the command asks for neither
ENTRY = {("plan", "new"), ("design", "new"), ("build", "new"), ("test", "run"), ("deploy", "pr"), ("maintain", "watch")}
SILENT = {("knowledge", "refresh")}  # its commit skips the post-commit hooks: they would refresh, commit, and refresh again


def parser() -> argparse.ArgumentParser:
    common = argparse.ArgumentParser(add_help=False)
    common.add_argument("--slug", help="feature slug (default: most recent)")
    common.add_argument("--value", type=float, help="metric value (maintain ingest)")
    common.add_argument("--only", help="test selector for `[commands] test_one` (build red|green), e.g. tests/test_x.py::test_y")
    common.add_argument("--max-tokens", type=int, help="context-pack token budget (knowledge pack); overrides [knowledge] pack_max_tokens")
    ap = argparse.ArgumentParser(prog="sdlc")
    sub = ap.add_subparsers(dest="stage", required=True)
    for stage in dict.fromkeys(s for s, _ in COMMANDS):
        actions = [act for s, act in COMMANDS if s == stage and act]
        st = sub.add_parser(stage, parents=[common])
        if actions:
            st.add_argument("action", choices=actions)
            st.add_argument("arg", nargs="?", help="title | step | on/off | env | metric | text | check | stage")
    return ap


def entry_notes(root: Path, stage: str, result: dict) -> dict:
    """What a stage's first verdict adds: `workflow` (name, run, reason) and, only when a tool is missing or broken, `knowledge`."""
    notes = {}
    gate = attempt(workflows.gate, root, stage)
    if gate["ok"]:
        notes["workflow"] = {"name": gate["workflow"], "run": gate["run"], "reason": gate["reason"]}
    if "knowledge" not in result:  # `plan new` already ran the installing bootstrap
        boot = attempt(knowledge.bootstrap, root, True)
        if not boot["ok"]:
            notes["knowledge"] = {"ok": False, "reason": boot["reason"], "next": "sdlc knowledge bootstrap"}
    return notes


def main(argv: list[str], root: Path) -> dict:
    ns = parser().parse_args(argv)
    key = (ns.stage, getattr(ns, "action", None))
    gate, handler = COMMANDS[key]
    try:
        feature = stages.gated(root, ns.slug, gate) if gate else None
        result = handler(root, feature, getattr(ns, "arg", None), ns)
    except Blocked as blocked:
        result = blocked.verdict
    if result["ok"] and key in ENTRY:
        result = {**result, **entry_notes(root, ns.stage, result)}
    if result["ok"] and "path" in result and (label := BOUNDARIES.get(key)):  # a skipped layer produces no path
        if key in handover.BOUNDARIES and handover.enabled(root):  # written first, so the checkpoint commits it too
            result["handover"] = attempt(handover.write, root, ns.stage, label.format(**result), result)
        result["checkpoint"] = attempt(checkpoint.commit, root, ns.stage, label.format(**result), Path(result["path"]), key in SILENT)
    return {**result, "stage": ns.stage}


def entry() -> int:
    result = main(sys.argv[1:], Path.cwd())
    print(json.dumps(result))  # one line: indentation is a fifth of every verdict's tokens
    return 0 if result["ok"] else 1


if __name__ == "__main__":
    sys.exit(entry())
