---
type: Module
title: stages.py
description: "Graphify community 22: plugin/scripts/sdlc/stages.py"
resource: plugin/scripts/sdlc
tags: [module, graphify]
status: draft
generated: { by: sdlc/0.5.0, at: "2026-09-25T07:29:30Z" }
stale_after: "2026-10-09T07:29:30Z"
source_commit: dc32a5b78bc303376f02bfe7d43360ae82fa4a82
sources:
  - { id: stages, resource: plugin/scripts/sdlc/stages.py, last_modified: "2026-09-09T15:02:31+10:00", digest: 79822cdce593996c }
---

# Files
- `plugin/scripts/sdlc/stages.py`

# Symbols
- stages.py (plugin/scripts/sdlc/stages.py:L1)
- The ordered stage table, and the new/check/accept lifecycle shared by… (plugin/scripts/sdlc/stages.py:L1)
- status() (plugin/scripts/sdlc/stages.py:L105)
- prerequisite() (plugin/scripts/sdlc/stages.py:L18)
- accepted() (plugin/scripts/sdlc/stages.py:L27)
- gated() (plugin/scripts/sdlc/stages.py:L32)
- The feature directory, provided `artifact` (if any) has been accepted by a… (plugin/scripts/sdlc/stages.py:L33)
- create_feature() (plugin/scripts/sdlc/stages.py:L42)
- new() (plugin/scripts/sdlc/stages.py:L53)
- check() (plugin/scripts/sdlc/stages.py:L75)
- next_for() (plugin/scripts/sdlc/stages.py:L95)
- The one /sdlc command to run next; the deploy gates decide when test and deploy… (plugin/scripts/sdlc/stages.py:L96)

# Depends on
- [append_log](/modules/append-log.md)
- [artifacts.py](/modules/artifacts-py.md)
- [Components](/modules/components.md)
- [deploy.py](/modules/deploy-py.md)
- [docs.py](/modules/docs-py.md)
- [fail](/modules/fail.md)
- [fill](/modules/fill.md)
- [__init__.py](/modules/init-py.md)
- [knowledge.py](/modules/knowledge-py.md)
- [maintain.py](/modules/maintain-py.md)
- [pathlib](/modules/pathlib.md)
- [project.py](/modules/project-py.md)

# Inferred
- no INFERRED edges; treat any that appear as hints

# Features
- no feature plan names these files
