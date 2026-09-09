"""Stage documents: one Archify HTML diagram per stage, delivered from a Claude-authored JSON source.
Public mechanics: render, check, require, open (plus the archify bootstrap step used by knowledge.STEPS).
Every one is a no-op verdict when the layer is off (`[docs] enabled = false` or SDLC_DOCS=off).
Node and Archify are subprocesses; nothing here imports them or calls an LLM.
"""

from __future__ import annotations

import functools
import os
from pathlib import Path

from . import project as p
from .project import fail

SKIPPED = {"ok": True, "skipped": "docs disabled"}
# stage -> files the document describes; relative to the feature directory, except maintain (repo-relative, no feature)
SOURCES = {
    "plan": ["intent.md"],
    "design": ["spec.md"],
    "build": ["plan.md"],
    "test": ["review.md", "test-report.json"],
    "deploy": ["pr-body.md"],
    "maintain": ["sdlc/bands.toml"],
}


def cfg(root: Path) -> dict:
    return p.config(root)["docs"]


def enabled(root: Path) -> bool:
    return os.environ.get("SDLC_DOCS") != "off" and bool(cfg(root)["enabled"])


def when_enabled(fn):
    @functools.wraps(fn)
    def inner(root: Path, *args, **kwargs):
        return fn(root, *args, **kwargs) if enabled(root) else SKIPPED

    return inner


def stage_of(stage: str | None) -> str:
    if stage not in SOURCES:
        fail(f"unknown stage {stage!r}; one of {', '.join(SOURCES)}")
    return stage


def target(root: Path, stage: str | None, slug: str | None) -> Path | None:
    """The feature the document belongs to; maintain documents belong to the project, not a feature."""
    return None if stage_of(stage) == "maintain" else p.feature(root, slug)


@when_enabled
def render(root: Path, feature: Path | None, stage: str) -> dict:
    fail("docs render is not implemented yet")


@when_enabled
def check(root: Path, feature: Path | None, stage: str) -> dict:
    fail("docs check is not implemented yet")


@when_enabled
def open(root: Path, feature: Path | None, stage: str) -> dict:
    fail("docs open is not implemented yet")
