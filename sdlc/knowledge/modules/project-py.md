---
type: Module
title: project.py
description: "Graphify community 12: plugin/scripts/sdlc/docs.py, plugin/scripts/sdlc/maintain.py, plugin/scripts/sdlc/project.py"
resource: plugin/scripts/sdlc
tags: [module, graphify]
status: draft
generated: { by: sdlc/0.5.0, at: "2026-09-26T06:33:18Z" }
stale_after: "2026-10-10T06:33:18Z"
source_commit: 5c45a37edd0dc635576e390a1174bea9fad6d10b
sources:
  - { id: docs, resource: plugin/scripts/sdlc/docs.py, last_modified: "2026-09-09T15:02:31+10:00", digest: 10270177466cde0a }
  - { id: maintain, resource: plugin/scripts/sdlc/maintain.py, last_modified: "2026-09-09T15:02:31+10:00", digest: 3aba25cd9e242550 }
  - { id: project, resource: plugin/scripts/sdlc/project.py, last_modified: "2026-09-26T16:06:32+10:00", digest: 26698ea0d06e1efe }
---

# Files
- `plugin/scripts/sdlc/docs.py`
- `plugin/scripts/sdlc/maintain.py`
- `plugin/scripts/sdlc/project.py`

# Symbols
- target() (plugin/scripts/sdlc/docs.py:L140)
- The directory that owns the stage document: the feature, or `sdlc/` for the… (plugin/scripts/sdlc/docs.py:L141)
- maintain.py (plugin/scripts/sdlc/maintain.py:L1)
- Maintain-stage mechanics: deterministic control bands that close the loop back… (plugin/scripts/sdlc/maintain.py:L1)
- lesson() (plugin/scripts/sdlc/maintain.py:L121)
- project.py (plugin/scripts/sdlc/project.py:L1)
- Project-level state: config schema, artifact home, git and JSONL helpers, the… (plugin/scripts/sdlc/project.py:L1)
- ensure_config() (plugin/scripts/sdlc/project.py:L168)
- home() (plugin/scripts/sdlc/project.py:L174)
- features() (plugin/scripts/sdlc/project.py:L181)
- Every feature directory (one holding an intent.md), sorted by name. (plugin/scripts/sdlc/project.py:L182)
- feature() (plugin/scripts/sdlc/project.py:L187)
- The named feature directory, or the most recently modified one; Blocked when… (plugin/scripts/sdlc/project.py:L188)
- today() (plugin/scripts/sdlc/project.py:L236)

# Depends on
- [artifacts.py](/modules/artifacts-py.md)
- [Blocked](/modules/blocked.md)
- [build.py](/modules/build-py.md)
- [check](/modules/check.md)
- [config](/modules/config.md)
- [docs.py](/modules/docs-py.md)
- [fail](/modules/fail.md)
- [git](/modules/git.md)
- [hooks.py](/modules/hooks-py.md)
- [packs.py](/modules/packs-py.md)
- [pathlib](/modules/pathlib.md)
- [propose](/modules/propose.md)
- [refresh](/modules/refresh.md)
- [test_plan_design.py](/modules/test-plan-design-py.md)
- [watch](/modules/watch.md)
- [when_enabled](/modules/when-enabled.md)

# Inferred
- no INFERRED edges; treat any that appear as hints

# Features
- [graph-selected repomix context packs](/features/graph-selected-repomix-context-packs.md)
