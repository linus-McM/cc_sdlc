---
type: Module
title: stages.py
description: "Graphify community 22: plugin/scripts/sdlc/artifacts.py, plugin/scripts/sdlc/stages.py"
resource: plugin/scripts/sdlc
tags: [module, graphify]
status: draft
generated: { by: sdlc/0.5.0, at: "2026-09-26T06:16:29Z" }
stale_after: "2026-10-10T06:16:29Z"
source_commit: def844e9ac23d4fb2eaffa6f82398a364dfbbac4
sources:
  - { id: artifacts, resource: plugin/scripts/sdlc/artifacts.py, last_modified: "2026-09-09T15:02:31+10:00", digest: 3e063b545e7dd897 }
  - { id: stages, resource: plugin/scripts/sdlc/stages.py, last_modified: "2026-09-26T16:06:32+10:00", digest: 3de65600923a55b5 }
---

# Files
- `plugin/scripts/sdlc/artifacts.py`
- `plugin/scripts/sdlc/stages.py`

# Symbols
- meta() (plugin/scripts/sdlc/artifacts.py:L49)
- status() (plugin/scripts/sdlc/artifacts.py:L58)
- stages.py (plugin/scripts/sdlc/stages.py:L1)
- The ordered stage table, and the new/check/accept lifecycle shared by… (plugin/scripts/sdlc/stages.py:L1)
- status() (plugin/scripts/sdlc/stages.py:L107)
- prerequisite() (plugin/scripts/sdlc/stages.py:L19)
- accepted() (plugin/scripts/sdlc/stages.py:L28)
- gated() (plugin/scripts/sdlc/stages.py:L33)
- The feature directory, provided `artifact` (if any) has been accepted by a… (plugin/scripts/sdlc/stages.py:L34)
- create_feature() (plugin/scripts/sdlc/stages.py:L43)
- new() (plugin/scripts/sdlc/stages.py:L54)
- check() (plugin/scripts/sdlc/stages.py:L76)

# Depends on
- [append_log](/modules/append-log.md)
- [artifacts.py](/modules/artifacts-py.md)
- [check](/modules/check.md)
- [docs.py](/modules/docs-py.md)
- [fail](/modules/fail.md)
- [git](/modules/git.md)
- [hooks.py](/modules/hooks-py.md)
- [knowledge.py](/modules/knowledge-py.md)
- [packs.py](/modules/packs-py.md)
- [pathlib](/modules/pathlib.md)
- [project.py](/modules/project-py.md)
- [StepSkipped](/modules/stepskipped.md)
- [test_plan_design.py](/modules/test-plan-design-py.md)

# Inferred
- no INFERRED edges; treat any that appear as hints

# Features
- [graph-selected repomix context packs](/features/graph-selected-repomix-context-packs.md)
