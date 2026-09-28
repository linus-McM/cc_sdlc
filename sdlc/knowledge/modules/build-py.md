---
type: Module
title: build.py
description: "Graphify community 21: plugin/scripts/sdlc/build.py, plugin/scripts/sdlc/testing.py"
resource: plugin/scripts/sdlc
tags: [module, graphify]
status: draft
generated: { by: sdlc/0.8.1, at: "2026-09-28T22:57:53Z" }
stale_after: "2026-10-12T22:57:53Z"
source_commit: 0754d821fc594b90c529849cddaca10dc6109921
sources:
  - { id: build, resource: plugin/scripts/sdlc/build.py, last_modified: "2026-09-09T15:02:31+10:00", digest: 3bd6dd8d38860ab6 }
  - { id: testing, resource: plugin/scripts/sdlc/testing.py, last_modified: "2026-09-26T16:35:55+10:00", digest: 68b187c7a3220c0b }
---

# Files
- `plugin/scripts/sdlc/build.py`
- `plugin/scripts/sdlc/testing.py`

# Symbols
- build.py (plugin/scripts/sdlc/build.py:L1)
- Build-stage mechanics: red/green TDD log, plan sync, fix lock. (plugin/scripts/sdlc/build.py:L1)
- run_cmd() (plugin/scripts/sdlc/build.py:L15)
- cycles() (plugin/scripts/sdlc/build.py:L23)
- Completed red->green pairs, matched per step name in order. (plugin/scripts/sdlc/build.py:L24)
- tdd() (plugin/scripts/sdlc/build.py:L35)
- fix() (plugin/scripts/sdlc/build.py:L78)
- run() (plugin/scripts/sdlc/testing.py:L18)
- knowledge_result() (plugin/scripts/sdlc/testing.py:L42)
- The OKF conformance check as one more feedback-loop row; only conformance… (plugin/scripts/sdlc/testing.py:L43)

# Depends on
- [cfg](/modules/cfg.md)
- [fail](/modules/fail.md)
- [git](/modules/git.md)
- [hooks.py](/modules/hooks-py.md)
- [maintain.py](/modules/maintain-py.md)
- [Order of work](/modules/order-of-work-44.md)
- [Path](/modules/path.md)
- [pathlib](/modules/pathlib.md)
- [project.py](/modules/project-py.md)
- [select](/modules/select.md)

# Inferred
- no INFERRED edges; treat any that appear as hints

# Features
- [graph-selected repomix context packs](/features/graph-selected-repomix-context-packs.md)
