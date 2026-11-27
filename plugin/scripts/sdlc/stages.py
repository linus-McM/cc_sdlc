"""The ordered stage table, and the new/check/accept lifecycle shared by intent.md, spec.md, plan.md."""

from __future__ import annotations

import functools
from pathlib import Path

from . import artifacts as a
from . import build, deploy, knowledge, packs
from . import project as p
from .project import fail

# stage -> artifact it writes. Order is the pipeline: each artifact gates the next stage.
ARTIFACTS = {"plan": "intent.md", "design": "spec.md", "build": "plan.md"}
ORDER = list(ARTIFACTS)
COMMANDS = ["/sdlc:" + s for s in (*ORDER, "test", "deploy", "maintain")]
APPROVAL = "build"  # the one acceptance the user gives: it covers intent.md, spec.md and plan.md; the earlier accepts only record that a check passed
COMPLETE = "complete"  # the loop ends when the test stage is done; deploy and maintain are optional follow-ups


def prerequisite(stage: str) -> str | None:
    i = ORDER.index(stage)
    return ARTIFACTS[ORDER[i - 1]] if i else None


def next_command(stage: str) -> str:
    return COMMANDS[COMMANDS.index("/sdlc:" + stage) + 1]


def accepted(feature: Path, artifact: str) -> bool:
    path = feature / artifact
    return path.exists() and a.status(path.read_text()) == "accepted"


def gated(root: Path, slug: str | None, artifact: str | None) -> Path:
    """The feature directory, provided `artifact` (if any) has been accepted."""
    feature = p.feature(root, slug)
    if artifact and not (feature / artifact).exists():
        return fail(f"{artifact} missing; run the previous stage first")
    if artifact and not accepted(feature, artifact):
        stage = next(s for s, name in ARTIFACTS.items() if name == artifact)
        return fail(f"{artifact} is not accepted; run `sdlc {stage} accept` before this stage")
    return feature


def create_feature(root: Path, title: str) -> Path:
    if not title:
        fail("plan new needs a title")
    feature = p.home(root) / a.slugify(title)
    if (feature / "intent.md").exists():
        fail(f"{feature / 'intent.md'} already exists", slug=feature.name)
    feature.mkdir(parents=True)
    p.ensure_config(root)
    return feature


def new(stage: str, root: Path, title: str | None, slug: str | None) -> dict:
    artifact = ARTIFACTS[stage]
    if stage == "plan":
        feature = create_feature(root, title or "")
        fields = {"title": title, "author": p.author(root)}
    else:
        feature = gated(root, slug, prerequisite(stage))
        fields = {"title": a.title((feature / "intent.md").read_text())}
    path = feature / artifact
    path.write_text(a.render(p.TEMPLATES / artifact, date=p.today(), **fields))
    verdict = {
        "ok": True,
        "slug": feature.name,
        "path": str(path),
        "next": f"fill every section of {artifact}, then `{stage} check`",
    }
    if stage == "plan":
        verdict["knowledge"] = knowledge.brief(p.attempt(functools.partial(knowledge.bootstrap, update=True), root))  # install, and update tools already present
    return verdict


def check(stage: str, root: Path, slug: str | None) -> dict:
    artifact = ARTIFACTS[stage]
    feature = gated(root, slug, prerequisite(stage))
    path = feature / artifact
    if not path.exists():
        fail(f"{artifact} missing; run `{stage} new`", slug=feature.name)
    text = path.read_text()
    if problems := a.validate(text, a.REQUIRED[artifact]) or trace(stage, feature, text):
        fail("; ".join(problems), slug=feature.name, path=str(path), problems=problems)
    return {"ok": True, "slug": feature.name, "path": str(path), "problems": []}


def trace(stage: str, feature: Path, text: str) -> list[str]:
    """Problems with the chain requirement -> step: spec.md numbers its requirements, plan.md numbers its steps and every requirement is cited by one."""
    found = a.sections(text)
    if stage == "design":
        return [] if a.requirement_ids(text) else ["Requirements must be a numbered list (`1. ...`): plan.md and review.md cite each one as R1, R2, ..."]
    if stage != "build":
        return []
    problems = [] if a.numbered(found["Order of work"]) else ["Order of work must be numbered steps (`1. ...`): `build red|green <n>` records each one"]
    wanted, cited = a.requirement_ids((feature / "spec.md").read_text()), a.cited(found["Order of work"])
    if wanted:  # a spec written before requirements were numbered asks for nothing here
        if missing := [f"R{n}" for n in wanted if n not in cited]:
            problems.append(f"no Order of work step delivers {', '.join(missing)}; cite each spec.md requirement in the step that builds it")
        if unknown := [f"R{n}" for n in sorted(cited - set(wanted))]:
            problems.append(f"Order of work cites {', '.join(unknown)}, which spec.md does not define")
    return problems


def accept(stage: str, root: Path, slug: str | None) -> dict:
    verdict = check(stage, root, slug)
    path = Path(verdict["path"])
    feature = path.parent
    pack = {"pack": p.attempt(packs.require, root, feature, stage)} if stage in packs.GATED else {}  # advice for the workflow agents, never a refusal
    path.write_text(a.set_meta(path.read_text(), "Status", "accepted"))
    approved = {"approved": build.approve(root, feature)} if stage == APPROVAL else {}
    published = p.attempt(knowledge.publish, root, feature, p.author(root) if stage == APPROVAL else f"process:sdlc-{stage}")
    return {**verdict, "status": "accepted", "knowledge": published, **pack, **approved, "next": next_command(stage)}


def next_for(feature: Path, state: dict[str, str]) -> str:
    """The one /sdlc command to run next, or COMPLETE once the test stage is done (deploy readiness is that definition)."""
    for stage, artifact in ARTIFACTS.items():
        if state[artifact] != "accepted":
            return "/sdlc:" + stage
    return "/sdlc:test" if deploy.readiness(feature) else COMPLETE


def status(root: Path, slug: str | None) -> dict:
    feature = p.feature(root, slug)
    state = {}
    for name in ARTIFACTS.values():
        path = feature / name
        state[name] = (a.status(path.read_text()) or "draft") if path.exists() else "missing"
    for name in ("test-report.json", "review.md", "deploy.json"):
        state[name] = "present" if (feature / name).exists() else "missing"
    verdict = {"ok": True, "slug": feature.name, "artifacts": state, "next": next_for(feature, state)}
    if verdict["next"] == COMPLETE:
        verdict["optional"] = "/sdlc:maintain" if deploy.released(feature) else "/sdlc:deploy"
    return verdict
