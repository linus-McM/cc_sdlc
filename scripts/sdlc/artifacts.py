"""Markdown artifact helpers: intent.md, spec.md, plan.md, review.md share one shape.

A document is a `# Kind: Title` line, a metadata line (`Author: x. Status: draft. Risk: low.`),
then `## Section` blocks. A section holding only `<placeholder>` text counts as unfilled.
"""

from __future__ import annotations

import re
from pathlib import Path

PLACEHOLDER = re.compile(r"^\s*<[^>]*>\s*$")
HEADING = re.compile(r"^## (.+?)\s*$", re.MULTILINE)
BULLET = re.compile(r"^(?:[-*]|\d+\.)\s+")  # list marker only, so `.gitignore` keeps its dot

REQUIRED = {
    "intent.md": [
        "Problem",
        "Proposed outcome",
        "Affected users and systems",
        "Constraints",
        "Open questions",
    ],
    "spec.md": ["Requirements", "Design", "Concerns", "Open questions", "Proof"],
    "plan.md": ["Files that change", "Order of work", "Risks", "Proof"],
    "review.md": ["Bugs", "Security", "Compliance"],
}


def slugify(title: str) -> str:
    return re.sub(r"[^a-z0-9]+", "-", title.lower()).strip("-")


def title(md: str) -> str:
    """`# Intent: Claims status` -> `Claims status`."""
    return md.splitlines()[0].lstrip("# ").split(":", 1)[-1].strip()


def sections(md: str) -> dict[str, str]:
    parts = HEADING.split(md)
    return {parts[i]: parts[i + 1].strip() for i in range(1, len(parts) - 1, 2)}


def set_section(md: str, heading: str, body: str) -> str:
    pattern = re.compile(rf"(^## {re.escape(heading)}\s*\n)(.*?)(?=^## |\Z)", re.MULTILINE | re.DOTALL)
    return pattern.sub(lambda m: f"{m.group(1)}{body.rstrip()}\n\n", md, count=1)


def meta(md: str, field: str) -> str | None:
    match = re.search(rf"\b{field}:\s*([A-Za-z-]+)", md)
    return match.group(1).lower() if match else None


def set_meta(md: str, field: str, value: str) -> str:
    return re.sub(rf"\b{field}:\s*[A-Za-z-]+", f"{field}: {value}", md, count=1)


def status(md: str) -> str | None:
    return meta(md, "Status")


def validate(md: str, required: list[str]) -> list[str]:
    """Problems with the document; empty when every required section exists and is filled."""
    found = sections(md)
    problems = []
    for heading in required:
        if heading not in found:
            problems.append(f"missing section: {heading}")
        elif all(PLACEHOLDER.match(line) for line in found[heading].splitlines() or [""]):
            problems.append(f"unfilled section: {heading}")
    return problems


def first_line(body: str) -> str:
    """The first filled line of a section body, skipping template placeholders."""
    return next((line.strip() for line in body.splitlines() if line.strip() and not PLACEHOLDER.match(line)), "")


def list_items(body: str) -> list[str]:
    """Paths from a bulleted or comma-separated section body, annotations stripped."""
    items: list[str] = []
    for line in body.splitlines():
        line = BULLET.sub("", re.sub(r"\([^)]*\)", "", line).strip()).strip()
        items += [p.strip() for p in line.split(",") if p.strip()]
    return items


def render(template: Path, **fields: str) -> str:
    return template.read_text().format(**fields)


def glob_regex(pattern: str) -> re.Pattern:
    """gitignore-style: `**` spans directories, `*` stays in one segment, a bare name matches at any depth."""
    pattern = pattern.removeprefix("**/")
    body = re.escape(pattern).replace(r"\*\*/", "(?:.*/)?").replace(r"\*\*", ".*").replace(r"\*", "[^/]*")
    prefix = "" if "/" in pattern else "(?:.*/)?"
    return re.compile(f"^{prefix}{body}$")


def matches(rel: str, globs: list[str]) -> bool:
    return any(glob_regex(g).match(rel) for g in globs)
