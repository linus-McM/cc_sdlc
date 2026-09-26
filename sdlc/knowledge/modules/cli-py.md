---
type: Module
title: cli.py
description: "Graphify community 71: plugin/scripts/sdlc.py, plugin/scripts/sdlc/cli.py, plugin/scripts/sdlc/project.py"
resource: plugin/scripts
tags: [module, graphify]
status: draft
generated: { by: sdlc/0.5.0, at: "2026-09-26T05:22:30Z" }
stale_after: "2026-10-10T05:22:30Z"
source_commit: c5f64f8d3b9b5e3268754f626b7f2e958fd6415e
sources:
  - { id: sdlc, resource: plugin/scripts/sdlc.py, last_modified: "2026-09-09T15:02:31+10:00", digest: 17708c9e2035a5ee }
  - { id: cli, resource: plugin/scripts/sdlc/cli.py, last_modified: "2026-09-24T11:36:09+10:00", digest: 6cee45ef1d7a0ebb }
  - { id: project, resource: plugin/scripts/sdlc/project.py, last_modified: "2026-09-24T11:36:09+10:00", digest: d1e5536892dbd875 }
---

# Files
- `plugin/scripts/sdlc.py`
- `plugin/scripts/sdlc/cli.py`
- `plugin/scripts/sdlc/project.py`

# Symbols
- sdlc.py (plugin/scripts/sdlc.py:L1)
- Launcher: uv run --no-project scripts/sdlc.py <stage> <action> ... (plugin/scripts/sdlc.py:L2)
- cli.py (plugin/scripts/sdlc/cli.py:L1)
- One entry point: `uv run --no-project scripts/sdlc.py <stage> <action> [arg]`… (plugin/scripts/sdlc/cli.py:L1)
- parser() (plugin/scripts/sdlc/cli.py:L63)
- main() (plugin/scripts/sdlc/cli.py:L78)
- entry() (plugin/scripts/sdlc/cli.py:L92)
- attempt() (plugin/scripts/sdlc/project.py:L133)
- Run a side mechanic without letting it decide the caller's verdict: a Blocked… (plugin/scripts/sdlc/project.py:L134)

# Depends on
- [Blocked](/modules/blocked.md)
- [build.py](/modules/build-py.md)
- [checkpoint.py](/modules/checkpoint-py.md)
- [docs.py](/modules/docs-py.md)
- [fail](/modules/fail.md)
- [knowledge.py](/modules/knowledge-py.md)
- [pathlib](/modules/pathlib.md)
- [project.py](/modules/project-py.md)
- [stages.py](/modules/stages-py.md)

# Inferred
- [Blocked](/modules/blocked.md)

# Features
- [graph-selected repomix context packs](/features/graph-selected-repomix-context-packs.md)
