---
type: Module
title: build.py
description: "Graphify community 21: plugin/scripts/sdlc/build.py, plugin/scripts/sdlc/evals.py, plugin/scripts/sdlc/project.py, plugin/scripts/sdlc/testing.py"
resource: plugin/scripts/sdlc
tags: [module, graphify]
status: draft
generated: { by: sdlc/0.5.0, at: "2026-09-26T05:22:30Z" }
stale_after: "2026-10-10T05:22:30Z"
source_commit: c5f64f8d3b9b5e3268754f626b7f2e958fd6415e
sources:
  - { id: build, resource: plugin/scripts/sdlc/build.py, last_modified: "2026-09-09T15:02:31+10:00", digest: 3bd6dd8d38860ab6 }
  - { id: evals, resource: plugin/scripts/sdlc/evals.py, last_modified: "2026-09-09T15:02:31+10:00", digest: 6019b83ce814d4df }
  - { id: project, resource: plugin/scripts/sdlc/project.py, last_modified: "2026-09-24T11:36:09+10:00", digest: d1e5536892dbd875 }
  - { id: testing, resource: plugin/scripts/sdlc/testing.py, last_modified: "2026-09-24T11:36:09+10:00", digest: f854f76e33b9b57e }
---

# Files
- `plugin/scripts/sdlc/build.py`
- `plugin/scripts/sdlc/evals.py`
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
- run_eval() (plugin/scripts/sdlc/evals.py:L15)
- read_jsonl() (plugin/scripts/sdlc/project.py:L237)
- run() (plugin/scripts/sdlc/testing.py:L18)
- knowledge_result() (plugin/scripts/sdlc/testing.py:L42)
- The OKF conformance check as one more feedback-loop row; only conformance… (plugin/scripts/sdlc/testing.py:L43)

# Depends on
- [bootstrap](/modules/bootstrap.md)
- [cli.py](/modules/cli-py.md)
- [config](/modules/config.md)
- [fail](/modules/fail.md)
- [fill](/modules/fill.md)
- [pathlib](/modules/pathlib.md)
- [project.py](/modules/project-py.md)
- [refresh](/modules/refresh.md)
- [rehearse](/modules/rehearse.md)

# Inferred
- no INFERRED edges; treat any that appear as hints

# Features
- [graph-selected repomix context packs](/features/graph-selected-repomix-context-packs.md)
