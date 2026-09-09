---
type: Module
title: bump_version.py
description: "Graphify community 73: scripts/bump_version.py, scripts/sdlc/knowledge.py, tests/test_bump.py"
resource: ""
tags: [module, graphify]
status: draft
generated: { by: sdlc/0.2.1, at: "2026-09-09T01:29:56Z" }
stale_after: "2026-09-23T01:29:56Z"
source_commit: b6e8d5897548ac1aeadd713c4fd9bf19fac3d435
sources:
  - { id: bump_version, resource: scripts/bump_version.py, last_modified: "2026-09-09T11:00:05+10:00", digest: 146e5081d9fe864b }
  - { id: knowledge, resource: scripts/sdlc/knowledge.py, last_modified: "2026-09-09T10:28:52+10:00", digest: 8da5a1d01eeb439c }
  - { id: test_bump, resource: tests/test_bump.py, last_modified: "2026-09-09T11:00:05+10:00", digest: 236b7aaaf10d9fb4 }
---

# Files
- `scripts/bump_version.py`
- `scripts/sdlc/knowledge.py`
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
- read_flow() (scripts/sdlc/knowledge.py:L107)
- parse_frontmatter() (scripts/sdlc/knowledge.py:L124)
- The subset reader; on any line it cannot read, `_raw` holds the block and… (scripts/sdlc/knowledge.py:L125)
- Unparseable (scripts/sdlc/knowledge.py:L36)
- The YAML subset reader met a line it does not understand. (scripts/sdlc/knowledge.py:L37)
- read_scalar() (scripts/sdlc/knowledge.py:L72)
- split_flow() (scripts/sdlc/knowledge.py:L88)
- Top-level comma split that respects quotes and nested brackets. (scripts/sdlc/knowledge.py:L89)
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
- [Graphify and OKF knowledge base integration](/features/graphify-and-okf-knowledge-base-integration.md)
