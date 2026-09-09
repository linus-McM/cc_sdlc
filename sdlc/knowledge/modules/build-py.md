---
type: Module
title: build.py
description: "Graphify community 9: scripts/sdlc/artifacts.py, scripts/sdlc/build.py"
resource: scripts/sdlc
tags: [module, graphify]
status: draft
generated: { by: sdlc/0.2.1, at: "2026-09-09T01:55:17Z" }
stale_after: "2026-09-23T01:55:17Z"
source_commit: 0972bddc57871b4600edb500118b597e83638fbc
sources:
  - { id: artifacts, resource: scripts/sdlc/artifacts.py, last_modified: "2026-09-09T08:32:17+10:00", digest: 3e063b545e7dd897 }
  - { id: build, resource: scripts/sdlc/build.py, last_modified: "2026-09-08T09:22:42+10:00", digest: 3bd6dd8d38860ab6 }
---

# Files
- `scripts/sdlc/artifacts.py`
- `scripts/sdlc/build.py`

# Symbols
- list_items() (scripts/sdlc/artifacts.py:L79)
- Paths from a bulleted or comma-separated section body, annotations stripped. (scripts/sdlc/artifacts.py:L80)
- build.py (scripts/sdlc/build.py:L1)
- Build-stage mechanics: red/green TDD log, plan sync, fix lock. (scripts/sdlc/build.py:L1)
- run_cmd() (scripts/sdlc/build.py:L15)
- cycles() (scripts/sdlc/build.py:L23)
- Completed red->green pairs, matched per step name in order. (scripts/sdlc/build.py:L24)
- tdd() (scripts/sdlc/build.py:L35)
- planned_files() (scripts/sdlc/build.py:L57)
- is_sdlc_owned() (scripts/sdlc/build.py:L62)
- sync() (scripts/sdlc/build.py:L66)
- fix() (scripts/sdlc/build.py:L78)

# Depends on
- [config](/modules/config.md)
- [fail](/modules/fail.md)
- [__init__.py](/modules/init-py.md)
- [project.py](/modules/project-py.md)

# Inferred
- no INFERRED edges; treat any that appear as hints

# Features
- [Graphify and OKF knowledge base integration](/features/graphify-and-okf-knowledge-base-integration.md)
