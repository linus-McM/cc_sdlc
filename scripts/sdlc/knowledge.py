"""Knowledge layer: Graphify graph (graphify-out/) plus an OKF v0.2 bundle (sdlc/knowledge/).

Public mechanics: bootstrap, status, refresh, check, publish, unhook. Every one is a no-op verdict
when the layer is off (`[knowledge] enabled = false` or SDLC_KNOWLEDGE=off). Graphify and uv are
subprocesses; nothing here imports them or calls an LLM.
"""

from __future__ import annotations

import json
import os
import re
from pathlib import Path

from . import project as p

SKIPPED = {"ok": True, "skipped": "knowledge disabled"}
FENCE = "---"
BAD = re.compile(r"[:#\[\]{}\",']|^\s|\s$|^[-?&*!|>%@`]")


class Unparseable(ValueError):
    """The YAML subset reader met a line it does not understand."""


# --- YAML subset: scalars, flat lists, {k: v} maps and lists of maps; everything OKF emits ---


def scalar(value) -> str:
    if isinstance(value, bool):
        return "true" if value else "false"
    if isinstance(value, int):
        return str(value)
    text = str(value)
    plain = text and not BAD.search(text) and not NUMBERISH.match(text) and text not in ("true", "false", "null")
    return text if plain else json.dumps(text)


NUMBERISH = re.compile(r"^[-+]?(\d[\d_]*\.?\d*([eE][-+]?\d+)?|\.\d+)$")


def flow(value) -> str:
    if isinstance(value, dict):
        return "{ " + ", ".join(f"{key}: {scalar(v)}" for key, v in value.items()) + " }"
    if isinstance(value, list):
        return "[" + ", ".join(flow(v) for v in value) + "]"
    return scalar(value)


def dump_frontmatter(data: dict) -> str:
    lines = [FENCE]
    for key, value in data.items():
        if isinstance(value, list) and value and all(isinstance(v, dict) for v in value):
            lines.append(f"{key}:")
            lines += [f"  - {flow(v)}" for v in value]
        else:
            lines.append(f"{key}: {flow(value)}")
    return "\n".join([*lines, FENCE]) + "\n"


def read_scalar(text: str):
    text = text.strip()
    if text.startswith('"'):
        try:
            return json.loads(text)
        except json.JSONDecodeError as err:
            raise Unparseable(text) from err
    if text.startswith("'") and text.endswith("'") and len(text) >= 2:
        return text[1:-1]
    if text in ("true", "false"):
        return text == "true"
    if re.fullmatch(r"[-+]?\d+", text):
        return int(text)
    return text


def split_flow(text: str) -> list[str]:
    """Top-level comma split that respects quotes and nested brackets."""
    parts, depth, quote, start = [], 0, None, 0
    for i, ch in enumerate(text):
        if quote:
            quote = None if ch == quote else quote
        elif ch in "\"'":
            quote = ch
        elif ch in "[{":
            depth += 1
        elif ch in "]}":
            depth -= 1
        elif ch == "," and depth == 0:
            parts.append(text[start:i])
            start = i + 1
    parts.append(text[start:])
    return [part for part in (part.strip() for part in parts) if part]


def read_flow(text: str):
    text = text.strip()
    if text.startswith("{") and text.endswith("}"):
        out = {}
        for item in split_flow(text[1:-1]):
            key, sep, value = item.partition(":")
            if not sep:
                raise Unparseable(item)
            out[key.strip()] = read_flow(value)
        return out
    if text.startswith("[") and text.endswith("]"):
        return [read_flow(item) for item in split_flow(text[1:-1])]
    if text.startswith(("[", "{")):
        raise Unparseable(text)
    return read_scalar(text)


def parse_frontmatter(block: str) -> dict:
    """The subset reader; on any line it cannot read, `_raw` holds the block and `type` survives if present."""
    out: dict = {}
    try:
        key = None
        for line in block.splitlines():
            if not line.strip() or line.lstrip().startswith("#"):
                continue
            if line.startswith("  - ") and key:
                out.setdefault(key, []).append(read_flow(line[4:]))
                continue
            name, sep, value = line.partition(":")
            if not sep or name != name.strip() or not name:
                raise Unparseable(line)
            key = name
            if value.strip():
                out[key] = read_flow(value)
            else:
                out[key] = []
    except Unparseable:
        found = re.search(r"^type:\s*(.+)$", block, re.MULTILINE)
        return {"_raw": block, **({"type": read_scalar(found.group(1))} if found else {})}
    return out


def split_document(text: str) -> tuple[dict, str]:
    if not text.startswith(FENCE + "\n"):
        return {}, text
    end = text.find("\n" + FENCE + "\n", len(FENCE))
    if end < 0:
        return {}, text
    return parse_frontmatter(text[len(FENCE) + 1 : end + 1]), text[end + len(FENCE) + 2 :]


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
