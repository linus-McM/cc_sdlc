---
type: Module
title: sdlc — AI-native SDLC plugin for Claude Code
description: "Graphify community 47: plugin/README.md, plugin/scripts/sdlc/workflows.py"
resource: plugin
tags: [module, graphify]
status: draft
generated: { by: sdlc/0.5.0, at: "2026-09-26T05:22:30Z" }
stale_after: "2026-10-10T05:22:30Z"
source_commit: c5f64f8d3b9b5e3268754f626b7f2e958fd6415e
sources:
  - { id: README, resource: plugin/README.md, last_modified: "2026-09-24T11:36:09+10:00", digest: 2e559b282f80c004 }
  - { id: workflows, resource: plugin/scripts/sdlc/workflows.py, last_modified: "2026-09-19T23:30:10+10:00", digest: e4eefc8f967a3373 }
---

# Files
- `plugin/README.md`
- `plugin/scripts/sdlc/workflows.py`

# Symbols
- plugin/README.md (plugin/README.md:L1)
- sdlc — AI-native SDLC plugin for Claude Code (plugin/README.md:L1)
- Guardrails (hooks/hooks.json) (plugin/README.md:L16)
- Checkpoints (plugin/README.md:L23)
- Stage documents (Archify) (plugin/README.md:L50)
- Stage workflows (dynamic Workflow scripts) (plugin/README.md:L55)
- Install (plugin/README.md:L69)
- enabled() (plugin/scripts/sdlc/workflows.py:L32)
- catalog() (plugin/scripts/sdlc/workflows.py:L43)
- env() (plugin/scripts/sdlc/workflows.py:L47)
- Merge `[workflows.env]` into the local settings; report which keys were written… (plugin/scripts/sdlc/workflows.py:L48)
- export() (plugin/scripts/sdlc/workflows.py:L71)
- Append `export K=V` lines to the SessionStart env file, once each, so this… (plugin/scripts/sdlc/workflows.py:L72)

# Depends on
- [config](/modules/config.md)
- [fail](/modules/fail.md)
- [fill](/modules/fill.md)
- [Path](/modules/path-13.md)

# Inferred
- [build.py](/modules/build-py.md)
- [fail](/modules/fail.md)
- [Order of work](/modules/order-of-work.md)
- [rehearse](/modules/rehearse.md)

# Features
- [graph-selected repomix context packs](/features/graph-selected-repomix-context-packs.md)
