---
type: Module
title: fail
description: "Graphify community 22: plugin/scripts/sdlc/project.py, plugin/scripts/sdlc/stages.py, plugin/scripts/sdlc/workflows.py"
resource: plugin/scripts/sdlc
tags: [module, graphify]
status: draft
generated: { by: sdlc/0.5.0, at: "2026-09-25T23:27:53Z" }
stale_after: "2026-10-09T23:27:53Z"
source_commit: 1348ec2a58c87325a8bcaacd936bc4bc9473c870
sources:
  - { id: project, resource: plugin/scripts/sdlc/project.py, last_modified: "2026-09-24T11:36:09+10:00", digest: d1e5536892dbd875 }
  - { id: stages, resource: plugin/scripts/sdlc/stages.py, last_modified: "2026-09-09T15:02:31+10:00", digest: 79822cdce593996c }
  - { id: workflows, resource: plugin/scripts/sdlc/workflows.py, last_modified: "2026-09-19T23:30:10+10:00", digest: e4eefc8f967a3373 }
---

# Files
- `plugin/scripts/sdlc/project.py`
- `plugin/scripts/sdlc/stages.py`
- `plugin/scripts/sdlc/workflows.py`

# Symbols
- fail() (plugin/scripts/sdlc/project.py:L91)
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
- meta() (plugin/scripts/sdlc/workflows.py:L36)
- The script's `export const meta` literal (written as JSON so Python can read… (plugin/scripts/sdlc/workflows.py:L37)

# Depends on
- [accept](/modules/accept.md)
- [artifacts.py](/modules/artifacts-py.md)
- [Blocked](/modules/blocked.md)
- [docs.py](/modules/docs-py.md)
- [feature_concepts](/modules/feature-concepts.md)
- [fill](/modules/fill.md)
- [hooks.py](/modules/hooks-py.md)
- [knowledge.py](/modules/knowledge-py.md)
- [maintain.py](/modules/maintain-py.md)
- [project.py](/modules/project-py.md)
- [read_json](/modules/read-json.md)
- [render](/modules/render.md)

# Inferred
- no INFERRED edges; treat any that appear as hints

# Features
- no feature plan names these files
