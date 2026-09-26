---
type: Module
title: project.py
description: "Graphify community 19: plugin/scripts/sdlc/__init__.py, plugin/scripts/sdlc/evals.py, plugin/scripts/sdlc/project.py, plugin/scripts/sdlc/workflows.py"
resource: plugin/scripts/sdlc
tags: [module, graphify]
status: draft
generated: { by: sdlc/0.5.0, at: "2026-09-26T05:22:30Z" }
stale_after: "2026-10-10T05:22:30Z"
source_commit: c5f64f8d3b9b5e3268754f626b7f2e958fd6415e
sources:
  - { id: __init__, resource: plugin/scripts/sdlc/__init__.py, last_modified: "2026-09-09T15:02:31+10:00", digest: 0a6aea3cd6840dbf }
  - { id: evals, resource: plugin/scripts/sdlc/evals.py, last_modified: "2026-09-09T15:02:31+10:00", digest: 6019b83ce814d4df }
  - { id: project, resource: plugin/scripts/sdlc/project.py, last_modified: "2026-09-24T11:36:09+10:00", digest: d1e5536892dbd875 }
  - { id: workflows, resource: plugin/scripts/sdlc/workflows.py, last_modified: "2026-09-19T23:30:10+10:00", digest: e4eefc8f967a3373 }
---

# Files
- `plugin/scripts/sdlc/__init__.py`
- `plugin/scripts/sdlc/evals.py`
- `plugin/scripts/sdlc/project.py`
- `plugin/scripts/sdlc/workflows.py`

# Symbols
- __init__.py (plugin/scripts/sdlc/__init__.py:L1)
- sdlc — deterministic gates for the six-stage AI-native SDLC. Stdlib only. (plugin/scripts/sdlc/__init__.py:L1)
- evals.py (plugin/scripts/sdlc/evals.py:L1)
- Continuous evals: run each evals/*.json prompt non-interactively, then its… (plugin/scripts/sdlc/evals.py:L1)
- project.py (plugin/scripts/sdlc/project.py:L1)
- Project-level state: config schema, artifact home, git and JSONL helpers, the… (plugin/scripts/sdlc/project.py:L1)
- append_jsonl() (plugin/scripts/sdlc/project.py:L241)
- workflows.py (plugin/scripts/sdlc/workflows.py:L1)
- Stage workflows: the catalog of plugin Workflow scripts and the env that turns… (plugin/scripts/sdlc/workflows.py:L1)
- meta() (plugin/scripts/sdlc/workflows.py:L36)
- The script's `export const meta` literal (written as JSON so Python can read… (plugin/scripts/sdlc/workflows.py:L37)

# Depends on
- [Blocked](/modules/blocked.md)
- [build.py](/modules/build-py.md)
- [cli.py](/modules/cli-py.md)
- [config](/modules/config.md)
- [docs.py](/modules/docs-py.md)
- [fail](/modules/fail.md)
- [fill](/modules/fill.md)
- [knowledge.py](/modules/knowledge-py.md)
- [Path](/modules/path.md)
- [refresh](/modules/refresh.md)
- [rehearse](/modules/rehearse.md)
- [sdlc — AI-native SDLC plugin for Claude Code](/modules/sdlc-ai-native-sdlc-plugin-for-claude-code.md)
- [StepSkipped](/modules/stepskipped.md)
- [when_enabled](/modules/when-enabled.md)

# Inferred
- no INFERRED edges; treat any that appear as hints

# Features
- [graph-selected repomix context packs](/features/graph-selected-repomix-context-packs.md)
