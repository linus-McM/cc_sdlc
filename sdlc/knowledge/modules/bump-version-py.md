---
type: Module
title: bump_version.py
description: "Graphify community 73: scripts/bump_version.py, tests/test_bump.py"
resource: ""
tags: [module, graphify]
status: draft
generated: { by: sdlc/0.2.1, at: "2026-09-09T01:59:02Z" }
stale_after: "2026-09-23T01:59:02Z"
source_commit: e0523eb3d807827869c761a89aea8117eb781e36
sources:
  - { id: bump_version, resource: scripts/bump_version.py, last_modified: "2026-09-09T11:00:05+10:00", digest: 146e5081d9fe864b }
  - { id: test_bump, resource: tests/test_bump.py, last_modified: "2026-09-09T11:00:05+10:00", digest: 236b7aaaf10d9fb4 }
---

# Files
- `scripts/bump_version.py`
- `tests/test_bump.py`

# Symbols
- bump_version.py (scripts/bump_version.py:L1)
- Bump the plugin version in every file that carries it (plugin.json is the… (scripts/bump_version.py:L2)
- parse() (scripts/bump_version.py:L22)
- bump() (scripts/bump_version.py:L29)
- current() (scripts/bump_version.py:L38)
- write() (scripts/bump_version.py:L42)
- Set `version` in plugin.json, marketplace.json and pyproject.toml, keeping each… (scripts/bump_version.py:L43)
- part_from_labels() (scripts/bump_version.py:L53)
- main() (scripts/bump_version.py:L57)
- test_bump.py (tests/test_bump.py:L1)
- tree() (tests/test_bump.py:L12)
- test_bump_parts() (tests/test_bump.py:L20)
- test_write_syncs_every_version_file() (tests/test_bump.py:L28)
- test_main_bumps_only_when_head_equals_base() (tests/test_bump.py:L38)
- test_part_from_labels() (tests/test_bump.py:L48)

# Depends on
- no EXTRACTED edges to other modules

# Inferred
- no INFERRED edges; treat any that appear as hints

# Features
- no feature plan names these files
