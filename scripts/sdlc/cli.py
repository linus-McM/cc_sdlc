"""One entry point: `python3 scripts/sdlc.py <stage> <action> [arg]` prints a JSON verdict.

COMMANDS maps (stage, action) to (gate, handler). `gate` names the artifact that must already be
accepted (None = no feature needed); the handler receives (root, feature, arg, ns).
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

from . import build, deploy, evals, knowledge, maintain, stages, testing
from .project import Blocked


def lifecycle(stage: str, action: str):
    """new/check/accept for an artifact stage; only `plan new` takes the positional title."""
    if action == "new":
        return lambda r, f, x, ns: stages.new(stage, r, x if stage == "plan" else None, ns.slug)
    return lambda r, f, x, ns: getattr(stages, action)(stage, r, ns.slug)


COMMANDS = {
    **{(s, act): (None, lifecycle(s, act)) for s in stages.ORDER for act in ("new", "check", "accept")},
    ("build", "red"): ("spec.md", lambda r, f, x, ns: build.tdd(r, f, "red", x or "unnamed")),
    ("build", "green"): ("spec.md", lambda r, f, x, ns: build.tdd(r, f, "green", x or "unnamed")),
    ("build", "sync"): ("spec.md", lambda r, f, x, ns: build.sync(r, f)),
    ("build", "fix"): ("spec.md", lambda r, f, x, ns: build.fix(f, x or "on")),
    ("test", "run"): ("plan.md", lambda r, f, x, ns: testing.run(r, f)),
    ("test", "review"): ("plan.md", lambda r, f, x, ns: testing.review(f)),
    ("test", "evals"): (None, lambda r, f, x, ns: evals.run(r)),
    ("deploy", "check"): ("plan.md", lambda r, f, x, ns: deploy.check(r, f, x or "dev")),
    ("deploy", "rehearse"): ("plan.md", lambda r, f, x, ns: deploy.rehearse(r, f)),
    ("deploy", "record"): ("plan.md", lambda r, f, x, ns: deploy.record(r, f, x or "dev")),
    ("deploy", "pr"): ("plan.md", lambda r, f, x, ns: deploy.pr_body(r, f)),
    ("maintain", "watch"): (None, lambda r, f, x, ns: maintain.watch(r, x)),
    ("maintain", "propose"): (None, lambda r, f, x, ns: maintain.propose(r, x)),
    ("maintain", "ingest"): (None, lambda r, f, x, ns: maintain.ingest(r, x, ns.value)),
    ("maintain", "lesson"): (None, lambda r, f, x, ns: maintain.lesson(r, x or "")),
    ("knowledge", "bootstrap"): (None, lambda r, f, x, ns: knowledge.bootstrap(r, check=x == "check")),
    ("knowledge", "status"): (None, lambda r, f, x, ns: knowledge.status(r)),
    ("knowledge", "refresh"): (None, lambda r, f, x, ns: knowledge.refresh(r)),
    ("knowledge", "check"): (None, lambda r, f, x, ns: knowledge.check(r)),
    ("knowledge", "unhook"): (None, lambda r, f, x, ns: knowledge.unhook(r)),
    ("status", None): (None, lambda r, f, x, ns: stages.status(r, ns.slug)),
}


def parser() -> argparse.ArgumentParser:
    common = argparse.ArgumentParser(add_help=False)
    common.add_argument("--slug", help="feature slug (default: most recent)")
    common.add_argument("--value", type=float, help="metric value (maintain ingest)")
    ap = argparse.ArgumentParser(prog="sdlc")
    sub = ap.add_subparsers(dest="stage", required=True)
    for stage in dict.fromkeys(s for s, _ in COMMANDS):
        actions = [act for s, act in COMMANDS if s == stage and act]
        st = sub.add_parser(stage, parents=[common])
        if actions:
            st.add_argument("action", choices=actions)
            st.add_argument("arg", nargs="?", help="title | step | on/off | env | metric | text | check")
    return ap


def main(argv: list[str], root: Path) -> dict:
    ns = parser().parse_args(argv)
    gate, handler = COMMANDS[(ns.stage, getattr(ns, "action", None))]
    try:
        feature = stages.gated(root, ns.slug, gate) if gate else None
        result = handler(root, feature, getattr(ns, "arg", None), ns)
    except Blocked as blocked:
        result = blocked.verdict
    return {**result, "stage": ns.stage}


def entry() -> int:
    result = main(sys.argv[1:], Path.cwd())
    print(json.dumps(result, indent=2))
    return 0 if result["ok"] else 1


if __name__ == "__main__":
    sys.exit(entry())
