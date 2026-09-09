#!/usr/bin/env python3
"""Bump the plugin version in every file that carries it (plugin.json is the source of truth).

    uv run --no-project scripts/bump_version.py --part patch|minor|major [--base <version>] [--root <dir>]

With --base (the version on the target branch): bump only when head equals base, say so when head is
already ahead, exit 1 when head is behind. Used by .github/workflows/ci.yml on pull requests.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

PARTS = ("major", "minor", "patch")
PYPROJECT_VERSION = re.compile(r'^(version\s*=\s*")([^"]+)(")', re.MULTILINE)


def parse(version: str) -> tuple[int, int, int]:
    nums = version.split(".")
    if len(nums) != 3 or not all(n.isdigit() for n in nums):
        raise ValueError(f"not a MAJOR.MINOR.PATCH version: {version!r}")
    return tuple(int(n) for n in nums)  # type: ignore[return-value]


def bump(version: str, part: str) -> str:
    major, minor, patch = parse(version)
    if part == "major":
        return f"{major + 1}.0.0"
    if part == "minor":
        return f"{major}.{minor + 1}.0"
    return f"{major}.{minor}.{patch + 1}"


def current(root: Path) -> str:
    return json.loads((root / "plugin" / ".claude-plugin" / "plugin.json").read_text())["version"]


def write(root: Path, version: str) -> list[Path]:
    """Set `version` in plugin.json, marketplace.json and pyproject.toml, keeping each file's formatting."""
    plugin = root / "plugin" / ".claude-plugin" / "plugin.json"
    plugin.write_text(re.sub(r'("version"\s*:\s*")[^"]+(")', rf"\g<1>{version}\g<2>", plugin.read_text(), count=1))
    market = root / ".claude-plugin" / "marketplace.json"
    market.write_text(re.sub(r'("version"\s*:\s*")[^"]+(")', rf"\g<1>{version}\g<2>", market.read_text()))
    pyproject = root / "pyproject.toml"
    pyproject.write_text(PYPROJECT_VERSION.sub(rf"\g<1>{version}\g<3>", pyproject.read_text(), count=1))
    return [plugin, market, pyproject]


def part_from_labels(labels: list[str]) -> str:
    return next((part for part in PARTS if f"release:{part}" in labels), "patch")


def main(argv: list[str]) -> int:
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--part", choices=PARTS, default="patch")
    ap.add_argument("--base", help="version on the target branch; bump only when head still equals it")
    ap.add_argument("--root", type=Path, default=Path.cwd())
    ns = ap.parse_args(argv)
    head = current(ns.root)
    if ns.base:
        if parse(head) > parse(ns.base):
            print(f"version already ahead of base: {head} > {ns.base}; nothing to do")
            return 0
        if parse(head) < parse(ns.base):
            print(f"version behind base: {head} < {ns.base}; rebase or merge the target branch first")
            return 1
    new = bump(head, ns.part)
    for path in write(ns.root, new):
        print(f"{path.relative_to(ns.root)}: {head} -> {new}")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
