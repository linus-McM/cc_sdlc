---
type: Module
title: build.py
description: "Graphify community 21: plugin/scripts/sdlc/build.py, plugin/scripts/sdlc/evals.py, plugin/scripts/sdlc/project.py"
resource: plugin/scripts/sdlc
tags: [module, graphify]
status: draft
generated: { by: sdlc/0.5.0, at: "2026-09-26T06:33:18Z" }
stale_after: "2026-10-10T06:33:18Z"
source_commit: 5c45a37edd0dc635576e390a1174bea9fad6d10b
sources:
  - { id: build, resource: plugin/scripts/sdlc/build.py, last_modified: "2026-09-09T15:02:31+10:00", digest: 3bd6dd8d38860ab6 }
  - { id: evals, resource: plugin/scripts/sdlc/evals.py, last_modified: "2026-09-09T15:02:31+10:00", digest: 6019b83ce814d4df }
  - { id: project, resource: plugin/scripts/sdlc/project.py, last_modified: "2026-09-26T16:06:32+10:00", digest: 26698ea0d06e1efe }
---

# Files
- `plugin/scripts/sdlc/build.py`
- `plugin/scripts/sdlc/evals.py`
- `plugin/scripts/sdlc/project.py`

# Symbols
- build.py (plugin/scripts/sdlc/build.py:L1)
- Build-stage mechanics: red/green TDD log, plan sync, fix lock. (plugin/scripts/sdlc/build.py:L1)
- run_cmd() (plugin/scripts/sdlc/build.py:L15)
- cycles() (plugin/scripts/sdlc/build.py:L23)
- Completed red->green pairs, matched per step name in order. (plugin/scripts/sdlc/build.py:L24)
- tdd() (plugin/scripts/sdlc/build.py:L35)
- fix() (plugin/scripts/sdlc/build.py:L78)
- evals.py (plugin/scripts/sdlc/evals.py:L1)
- Continuous evals: run each evals/*.json prompt non-interactively, then its… (plugin/scripts/sdlc/evals.py:L1)
- run_eval() (plugin/scripts/sdlc/evals.py:L15)
- run() (plugin/scripts/sdlc/evals.py:L32)
- append_jsonl() (plugin/scripts/sdlc/project.py:L244)

# Depends on
- [artifacts.py](/modules/artifacts-py.md)
- [Blocked](/modules/blocked.md)
- [config](/modules/config.md)
- [fail](/modules/fail.md)
- [fresh_graph](/modules/fresh-graph.md)
- [pathlib](/modules/pathlib.md)
- [project.py](/modules/project-py.md)
- [review](/modules/review.md)
- [test_plan_design.py](/modules/test-plan-design-py.md)

# Inferred
- no INFERRED edges; treat any that appear as hints

# Features
- [graph-selected repomix context packs](/features/graph-selected-repomix-context-packs.md)
