"""Knowledge layer: Graphify graph (graphify-out/) plus an OKF v0.2 bundle (sdlc/knowledge/).

Public mechanics: bootstrap, status, refresh, check, publish, unhook. Every one is a no-op verdict
when the layer is off (`[knowledge] enabled = false` or SDLC_KNOWLEDGE=off). Graphify and uv are
subprocesses; nothing here imports them or calls an LLM.
"""

from __future__ import annotations

import os
from pathlib import Path

from . import project as p

SKIPPED = {"ok": True, "skipped": "knowledge disabled"}


def enabled(root: Path) -> bool:
    return os.environ.get("SDLC_KNOWLEDGE") != "off" and bool(p.config(root)["knowledge"]["enabled"])


def bootstrap(root: Path, check: bool = False) -> dict:
    if not enabled(root):
        return SKIPPED
    raise NotImplementedError


def status(root: Path) -> dict:
    if not enabled(root):
        return SKIPPED
    raise NotImplementedError


def refresh(root: Path, quiet: bool = False) -> dict:
    if not enabled(root):
        return SKIPPED
    raise NotImplementedError


def check(root: Path) -> dict:
    if not enabled(root):
        return SKIPPED
    raise NotImplementedError


def publish(root: Path, feature: Path, actor: str) -> dict:
    if not enabled(root):
        return SKIPPED
    raise NotImplementedError


def unhook(root: Path) -> dict:
    if not enabled(root):
        return SKIPPED
    raise NotImplementedError
