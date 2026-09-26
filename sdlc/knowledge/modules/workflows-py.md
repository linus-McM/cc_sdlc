---
type: Module
title: workflows.py
description: "Graphify community 47: plugin/README.md, plugin/scripts/sdlc/workflows.py"
resource: plugin
tags: [module, graphify]
status: draft
generated: { by: sdlc/0.5.0, at: "2026-09-26T06:33:18Z" }
stale_after: "2026-10-10T06:33:18Z"
source_commit: 5c45a37edd0dc635576e390a1174bea9fad6d10b
sources:
  - { id: README, resource: plugin/README.md, last_modified: "2026-09-26T16:24:05+10:00", digest: 816c28888fc35408 }
  - { id: workflows, resource: plugin/scripts/sdlc/workflows.py, last_modified: "2026-09-19T23:30:10+10:00", digest: e4eefc8f967a3373 }
---

# Files
- `plugin/README.md`
- `plugin/scripts/sdlc/workflows.py`

# Symbols
- Stage workflows (dynamic Workflow scripts) (plugin/README.md:L62)
- workflows.py (plugin/scripts/sdlc/workflows.py:L1)
- Stage workflows: the catalog of plugin Workflow scripts and the env that turns… (plugin/scripts/sdlc/workflows.py:L1)
- enabled() (plugin/scripts/sdlc/workflows.py:L32)
- meta() (plugin/scripts/sdlc/workflows.py:L36)
- The script's `export const meta` literal (written as JSON so Python can read… (plugin/scripts/sdlc/workflows.py:L37)
- catalog() (plugin/scripts/sdlc/workflows.py:L43)
- env() (plugin/scripts/sdlc/workflows.py:L47)
- Merge `[workflows.env]` into the local settings; report which keys were written… (plugin/scripts/sdlc/workflows.py:L48)
- export() (plugin/scripts/sdlc/workflows.py:L71)
- Append `export K=V` lines to the SessionStart env file, once each, so this… (plugin/scripts/sdlc/workflows.py:L72)

# Depends on
- [check](/modules/check.md)
- [config](/modules/config.md)
- [fail](/modules/fail.md)
- [pathlib](/modules/pathlib.md)
- [project.py](/modules/project-py.md)
- [test_plan_design.py](/modules/test-plan-design-py.md)

# Inferred
- no INFERRED edges; treat any that appear as hints

# Features
- [graph-selected repomix context packs](/features/graph-selected-repomix-context-packs.md)
