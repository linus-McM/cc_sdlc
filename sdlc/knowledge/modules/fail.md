---
type: Module
title: fail
description: "Graphify community 12: plugin/scripts/sdlc/build.py, plugin/scripts/sdlc/project.py, plugin/scripts/sdlc/testing.py"
resource: plugin/scripts/sdlc
tags: [module, graphify]
status: draft
generated: { by: sdlc/0.5.0, at: "2026-09-25T07:29:30Z" }
stale_after: "2026-10-09T07:29:30Z"
source_commit: dc32a5b78bc303376f02bfe7d43360ae82fa4a82
sources:
  - { id: build, resource: plugin/scripts/sdlc/build.py, last_modified: "2026-09-09T15:02:31+10:00", digest: 3bd6dd8d38860ab6 }
  - { id: project, resource: plugin/scripts/sdlc/project.py, last_modified: "2026-09-24T11:36:09+10:00", digest: d1e5536892dbd875 }
  - { id: testing, resource: plugin/scripts/sdlc/testing.py, last_modified: "2026-09-24T11:36:09+10:00", digest: f854f76e33b9b57e }
---

# Files
- `plugin/scripts/sdlc/build.py`
- `plugin/scripts/sdlc/project.py`
- `plugin/scripts/sdlc/testing.py`

# Symbols
- build.py (plugin/scripts/sdlc/build.py:L1)
- Build-stage mechanics: red/green TDD log, plan sync, fix lock. (plugin/scripts/sdlc/build.py:L1)
- run_cmd() (plugin/scripts/sdlc/build.py:L15)
- cycles() (plugin/scripts/sdlc/build.py:L23)
- Completed red->green pairs, matched per step name in order. (plugin/scripts/sdlc/build.py:L24)
- tdd() (plugin/scripts/sdlc/build.py:L35)
- planned_files() (plugin/scripts/sdlc/build.py:L57)
- is_sdlc_owned() (plugin/scripts/sdlc/build.py:L62)
- sync() (plugin/scripts/sdlc/build.py:L66)
- fix() (plugin/scripts/sdlc/build.py:L78)
- read_jsonl() (plugin/scripts/sdlc/project.py:L237)
- fail() (plugin/scripts/sdlc/project.py:L91)
- testing.py (plugin/scripts/sdlc/testing.py:L1)
- Test-stage mechanics: run the feedback loop, write test-report.json, validate… (plugin/scripts/sdlc/testing.py:L1)
- report() (plugin/scripts/sdlc/testing.py:L14)
- run() (plugin/scripts/sdlc/testing.py:L18)
- knowledge_result() (plugin/scripts/sdlc/testing.py:L42)
- The OKF conformance check as one more feedback-loop row; only conformance… (plugin/scripts/sdlc/testing.py:L43)
- count() (plugin/scripts/sdlc/testing.py:L50)
- Findings tagged `- Important:` / `- Nit:` in a review.md body. (plugin/scripts/sdlc/testing.py:L51)
- findings() (plugin/scripts/sdlc/testing.py:L55)
- review.md validated against REVIEW.md's three passes, with its finding counts. (plugin/scripts/sdlc/testing.py:L56)

# Depends on
- [artifacts.py](/modules/artifacts-py.md)
- [Blocked](/modules/blocked.md)
- [deploy.py](/modules/deploy-py.md)
- [docs.py](/modules/docs-py.md)
- [fill](/modules/fill.md)
- [__init__.py](/modules/init-py.md)
- [maintain.py](/modules/maintain-py.md)
- [pathlib](/modules/pathlib.md)
- [project.py](/modules/project-py.md)
- [refresh](/modules/refresh.md)
- [status](/modules/status.md)

# Inferred
- no INFERRED edges; treat any that appear as hints

# Features
- no feature plan names these files
