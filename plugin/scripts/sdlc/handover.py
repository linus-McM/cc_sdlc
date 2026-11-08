"""Session handover: `cli.main` writes sdlc/<slug>/HANDOVER.md at each stage boundary, before the checkpoint commit,
so the next stage can start from /clear with only this file and the artifact it names."""

from __future__ import annotations

from pathlib import Path

from . import artifacts as a
from . import project as p
from . import stages
from .project import fail

BOUNDARIES = {*((s, "accept") for s in stages.ORDER), ("test", "review"), ("deploy", "record")}
OPEN_ITEMS = {"spec.md": ["Concerns"], "review.md": ["Bugs", "Security", "Compliance"]}  # read best-effort, when present
MAX_ITEMS = 8  # keeps the file under 25 lines


def enabled(root: Path) -> bool:
    return bool(p.config(root)["checkpoint"]["handover"])


def open_items(feature: Path) -> list[str]:
    """Filled, non-"none" lines from spec.md Concerns and the review.md findings sections."""
    items = []
    for name, headings in OPEN_ITEMS.items():
        if not (path := feature / name).exists():
            continue
        found = a.sections(path.read_text())
        for heading in headings:
            for line in found.get(heading, "").splitlines():
                text = a.BULLET.sub("", line.strip()).strip()
                if text and not a.PLACEHOLDER.match(text) and text.strip('".').lower() != "none":
                    items.append(f"- {heading}: {text}" if name == "review.md" else f"- {text}")
    return items[:MAX_ITEMS]


def write(root: Path, stage: str, action: str, verdict: dict) -> str:
    """Overwrite the feature's HANDOVER.md from the verdict; return its path relative to `root`."""
    produced = Path(verdict["path"])
    feature = produced.parent
    intent = feature / "intent.md"
    fields = {
        "title": a.title(intent.read_text()) if intent.exists() else feature.name,
        "stage": stage,
        "action": action,
        "date": p.today(),
        "artifact": p.rel(root, produced),
        "next": verdict.get("next") or stages.next_command(stage),
        "items": "\n".join(open_items(feature)) or "- none",
    }
    path = feature / "HANDOVER.md"
    try:
        path.write_text(a.render(p.TEMPLATES / "handover.md", **fields))
    except OSError as err:
        fail(f"handover not written: {err}")
    return p.rel(root, path)
