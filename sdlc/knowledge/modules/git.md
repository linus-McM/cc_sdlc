---
type: Module
title: git
description: "Graphify community 45: plugin/scripts/sdlc/packs.py, plugin/scripts/sdlc/project.py"
resource: plugin/scripts/sdlc
tags: [module, graphify]
status: draft
generated: { by: sdlc/0.5.0, at: "2026-09-26T06:33:18Z" }
stale_after: "2026-10-10T06:33:18Z"
source_commit: 5c45a37edd0dc635576e390a1174bea9fad6d10b
sources:
  - { id: packs, resource: plugin/scripts/sdlc/packs.py, last_modified: "2026-09-26T16:31:53+10:00", digest: 976267a001f822d8 }
  - { id: project, resource: plugin/scripts/sdlc/project.py, last_modified: "2026-09-26T16:06:32+10:00", digest: 26698ea0d06e1efe }
---

# Files
- `plugin/scripts/sdlc/packs.py`
- `plugin/scripts/sdlc/project.py`

# Symbols
- run_bandit() (plugin/scripts/sdlc/packs.py:L349)
- run_cmd() (plugin/scripts/sdlc/project.py:L198)
- Run an external tool without a shell; never raises on a non-zero exit. A… (plugin/scripts/sdlc/project.py:L199)
- run_git() (plugin/scripts/sdlc/project.py:L210)
- git() (plugin/scripts/sdlc/project.py:L214)
- head_commit() (plugin/scripts/sdlc/project.py:L218)
- author() (plugin/scripts/sdlc/project.py:L222)
- changed_files() (plugin/scripts/sdlc/project.py:L226)
- Staged, unstaged and untracked paths in one git call, limited to `paths` when… (plugin/scripts/sdlc/project.py:L227)

# Depends on
- [fail](/modules/fail.md)
- [knowledge.py](/modules/knowledge-py.md)

# Inferred
- no INFERRED edges; treat any that appear as hints

# Features
- [graph-selected repomix context packs](/features/graph-selected-repomix-context-packs.md)
