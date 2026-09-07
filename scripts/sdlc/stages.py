"""The ordered stage table, and the new/check/accept lifecycle shared by intent.md, spec.md, plan.md."""

from __future__ import annotations

from pathlib import Path

from . import artifacts as a
from . import deploy
from . import project as p
from .project import fail

# stage -> artifact it writes. Order is the pipeline: each artifact gates the next stage.
ARTIFACTS = {"plan": "intent.md", "design": "spec.md", "build": "plan.md"}
ORDER = list(ARTIFACTS)
COMMANDS = ["/sdlc:" + s for s in (*ORDER, "test", "deploy", "maintain")]


def prerequisite(stage: str) -> str | None:
    i = ORDER.index(stage)
    return ARTIFACTS[ORDER[i - 1]] if i else None


def next_command(stage: str) -> str:
    return COMMANDS[COMMANDS.index("/sdlc:" + stage) + 1]


def accepted(feature: Path, artifact: str) -> bool:
    path = feature / artifact
    return path.exists() and a.status(path.read_text()) == "accepted"


def gated(root: Path, slug: str | None, artifact: str | None) -> Path:
    """The feature directory, provided `artifact` (if any) has been accepted by a human."""
    feature = p.feature(root, slug)
    if artifact and not (feature / artifact).exists():
        return fail(f"{artifact} missing; run the previous stage first")
    if artifact and not accepted(feature, artifact):
        return fail(f"{artifact} is not accepted; a human must accept it before this stage")
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
        fields = {"title": title, "author": p.author(root), "risk": "low"}
    else:
        feature = gated(root, slug, prerequisite(stage))
        intent = (feature / "intent.md").read_text()
        fields = {"title": a.title(intent), "risk": a.meta(intent, "Risk") or "low"}
    path = feature / artifact
    path.write_text(a.render(p.TEMPLATES / artifact, date=p.today(), **fields))
    return {
        "ok": True,
        "slug": feature.name,
        "path": str(path),
        "next": f"fill every section of {artifact}, then `{stage} check`",
    }


def check(stage: str, root: Path, slug: str | None) -> dict:
    artifact = ARTIFACTS[stage]
    feature = gated(root, slug, prerequisite(stage))
    path = feature / artifact
    if not path.exists():
        fail(f"{artifact} missing; run `{stage} new`", slug=feature.name)
    if problems := a.validate(path.read_text(), a.REQUIRED[artifact]):
        fail("; ".join(problems), slug=feature.name, path=str(path), problems=problems)
    return {"ok": True, "slug": feature.name, "path": str(path), "problems": []}


def accept(stage: str, root: Path, slug: str | None) -> dict:
    verdict = check(stage, root, slug)
    path = Path(verdict["path"])
    path.write_text(a.set_meta(path.read_text(), "Status", "accepted"))
    return {**verdict, "status": "accepted", "next": next_command(stage)}


def next_for(feature: Path, state: dict[str, str]) -> str:
    """The one /sdlc command to run next; the deploy gates decide when test and deploy are done."""
    for stage, artifact in ARTIFACTS.items():
        if state[artifact] != "accepted":
            return "/sdlc:" + stage
    if deploy.readiness(feature):
        return "/sdlc:test"
    return "/sdlc:maintain" if deploy.released(feature) else "/sdlc:deploy"


def status(root: Path, slug: str | None) -> dict:
    feature = p.feature(root, slug)
    state = {}
    for name in ARTIFACTS.values():
        path = feature / name
        state[name] = (a.status(path.read_text()) or "draft") if path.exists() else "missing"
    for name in ("test-report.json", "review.md", "deploy.json"):
        state[name] = "present" if (feature / name).exists() else "missing"
    return {"ok": True, "slug": feature.name, "artifacts": state, "next": next_for(feature, state)}
