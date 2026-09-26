---
type: Module
title: fail
description: "Graphify community 22: plugin/scripts/sdlc/project.py, plugin/scripts/sdlc/stages.py"
resource: plugin/scripts/sdlc
tags: [module, graphify]
status: draft
generated: { by: sdlc/0.5.0, at: "2026-09-26T06:33:18Z" }
stale_after: "2026-10-10T06:33:18Z"
source_commit: 5c45a37edd0dc635576e390a1174bea9fad6d10b
sources:
  - { id: project, resource: plugin/scripts/sdlc/project.py, last_modified: "2026-09-26T16:06:32+10:00", digest: 26698ea0d06e1efe }
  - { id: stages, resource: plugin/scripts/sdlc/stages.py, last_modified: "2026-09-26T16:06:32+10:00", digest: 3de65600923a55b5 }
---

# Files
- `plugin/scripts/sdlc/project.py`
- `plugin/scripts/sdlc/stages.py`

# Symbols
- fail() (plugin/scripts/sdlc/project.py:L94)
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
- next_for() (plugin/scripts/sdlc/stages.py:L97)
- The one /sdlc command to run next; the deploy gates decide when test and deploy… (plugin/scripts/sdlc/stages.py:L98)

# Depends on
- [append_log](/modules/append-log.md)
- [artifacts.py](/modules/artifacts-py.md)
- [Blocked](/modules/blocked.md)
- [check](/modules/check.md)
- [Components](/modules/components.md)
- [docs.py](/modules/docs-py.md)
- [findings](/modules/findings.md)
- [git](/modules/git.md)
- [hooks.py](/modules/hooks-py.md)
- [knowledge.py](/modules/knowledge-py.md)
- [packs.py](/modules/packs-py.md)
- [pathlib](/modules/pathlib.md)
- [project.py](/modules/project-py.md)
- [test_plan_design.py](/modules/test-plan-design-py.md)

# Inferred
- no INFERRED edges; treat any that appear as hints

# Features
- [graph-selected repomix context packs](/features/graph-selected-repomix-context-packs.md)
