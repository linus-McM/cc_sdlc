---
type: Module
title: install_hook
description: "Graphify community 17: plugin/README.md, plugin/scripts/sdlc/knowledge.py"
resource: plugin
tags: [module, graphify]
status: draft
generated: { by: sdlc/0.5.0, at: "2026-09-26T06:33:18Z" }
stale_after: "2026-10-10T06:33:18Z"
source_commit: 5c45a37edd0dc635576e390a1174bea9fad6d10b
sources:
  - { id: README, resource: plugin/README.md, last_modified: "2026-09-26T16:24:05+10:00", digest: 816c28888fc35408 }
  - { id: knowledge, resource: plugin/scripts/sdlc/knowledge.py, last_modified: "2026-09-26T16:06:32+10:00", digest: 12afb6df19262a3a }
---

# Files
- `plugin/README.md`
- `plugin/scripts/sdlc/knowledge.py`

# Symbols
- Knowledge (Graphify + OKF) (plugin/README.md:L36)
- hooks_dir() (plugin/scripts/sdlc/knowledge.py:L219)
- Git's hooks directory without spawning git: .git or the worktree's common dir,… (plugin/scripts/sdlc/knowledge.py:L220)
- post_commit_path() (plugin/scripts/sdlc/knowledge.py:L233)
- hook_block() (plugin/scripts/sdlc/knowledge.py:L249)
- our_block_present() (plugin/scripts/sdlc/knowledge.py:L254)
- linked_worktree() (plugin/scripts/sdlc/knowledge.py:L259)
- A `git worktree` checkout: `.git` is a file pointing at the primary's git dir,… (plugin/scripts/sdlc/knowledge.py:L260)
- install_hook() (plugin/scripts/sdlc/knowledge.py:L264)
- Idempotent: replaces an existing sdlc block, otherwise appends after everything… (plugin/scripts/sdlc/knowledge.py:L265)
- unhook() (plugin/scripts/sdlc/knowledge.py:L278)
- hooks_present() (plugin/scripts/sdlc/knowledge.py:L327)
- Both blocks in the post-commit file, read from the file (no subprocess). A… (plugin/scripts/sdlc/knowledge.py:L328)
- install_hooks() (plugin/scripts/sdlc/knowledge.py:L338)

# Depends on
- [docs.py](/modules/docs-py.md)
- [fail](/modules/fail.md)
- [Order of work](/modules/order-of-work.md)
- [packs.py](/modules/packs-py.md)
- [refresh](/modules/refresh.md)
- [status](/modules/status.md)

# Inferred
- [refresh](/modules/refresh.md)

# Features
- [graph-selected repomix context packs](/features/graph-selected-repomix-context-packs.md)
