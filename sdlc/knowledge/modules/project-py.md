---
type: Module
title: project.py
description: "Graphify community 12: plugin/scripts/sdlc/checkpoint.py, plugin/scripts/sdlc/evals.py, plugin/scripts/sdlc/project.py"
resource: plugin/scripts/sdlc
tags: [module, graphify]
status: draft
generated: { by: sdlc/0.8.1, at: "2026-09-28T22:57:53Z" }
stale_after: "2026-10-12T22:57:53Z"
source_commit: 0754d821fc594b90c529849cddaca10dc6109921
sources:
  - { id: checkpoint, resource: plugin/scripts/sdlc/checkpoint.py, last_modified: "2026-09-29T08:42:51+10:00", digest: b2fc74171d8dae0e }
  - { id: evals, resource: plugin/scripts/sdlc/evals.py, last_modified: "2026-09-09T15:02:31+10:00", digest: 6019b83ce814d4df }
  - { id: project, resource: plugin/scripts/sdlc/project.py, last_modified: "2026-09-29T08:42:51+10:00", digest: f89b1e9a47bc69d8 }
---

# Files
- `plugin/scripts/sdlc/checkpoint.py`
- `plugin/scripts/sdlc/evals.py`
- `plugin/scripts/sdlc/project.py`

# Symbols
- checkpoint.py (plugin/scripts/sdlc/checkpoint.py:L1)
- Stage-boundary checkpoints: `cli.main` commits the SDLC home directory and… (plugin/scripts/sdlc/checkpoint.py:L1)
- enabled() (plugin/scripts/sdlc/checkpoint.py:L17)
- evals.py (plugin/scripts/sdlc/evals.py:L1)
- Continuous evals: run each evals/*.json prompt non-interactively, then its… (plugin/scripts/sdlc/evals.py:L1)
- run_eval() (plugin/scripts/sdlc/evals.py:L15)
- run() (plugin/scripts/sdlc/evals.py:L32)
- project.py (plugin/scripts/sdlc/project.py:L1)
- Project-level state: config schema, artifact home, git and JSONL helpers, the… (plugin/scripts/sdlc/project.py:L1)
- merge() (plugin/scripts/sdlc/project.py:L144)
- config() (plugin/scripts/sdlc/project.py:L154)
- DEFAULT_CONFIG deep-merged with .sdlc.toml, so every key is always present;… (plugin/scripts/sdlc/project.py:L155)

# Depends on
- [Blocked](/modules/blocked.md)
- [bootstrap](/modules/bootstrap.md)
- [build](/modules/build.md)
- [build.py](/modules/build-py.md)
- [check](/modules/check.md)
- [docs.py](/modules/docs-py.md)
- [fail](/modules/fail.md)
- [git](/modules/git.md)
- [hooks.py](/modules/hooks-py.md)
- [maintain.py](/modules/maintain-py.md)
- [Order of work](/modules/order-of-work-44.md)
- [packs.py](/modules/packs-py.md)
- [pathlib](/modules/pathlib.md)
- [read_json](/modules/read-json.md)
- [refresh](/modules/refresh.md)
- [Requirements](/modules/requirements.md)
- [StepSkipped](/modules/stepskipped.md)
- [watch](/modules/watch.md)
- [when_enabled](/modules/when-enabled.md)

# Inferred
- no INFERRED edges; treat any that appear as hints

# Features
- [graph-selected repomix context packs](/features/graph-selected-repomix-context-packs.md)
