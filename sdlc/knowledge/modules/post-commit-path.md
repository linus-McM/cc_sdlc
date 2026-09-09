---
type: Module
title: post_commit_path
description: "Graphify community 22: scripts/sdlc/knowledge.py"
resource: scripts/sdlc
tags: [module, graphify]
status: draft
generated: { by: sdlc/0.2.0, at: "2026-09-08T22:35:57Z" }
stale_after: "2026-09-22T22:35:57Z"
source_commit: c6f9a22e23b0bee7134aa1e1709c5feef8673f82
sources:
  - { id: knowledge, resource: scripts/sdlc/knowledge.py, last_modified: "2026-09-09T08:35:54+10:00", digest: 5ed472fa5f0e7275 }
---

# Files
- `scripts/sdlc/knowledge.py`

# Symbols
- hooks_dir() (scripts/sdlc/knowledge.py:L211)
- Git's hooks directory without spawning git: .git or the worktree's common dir,… (scripts/sdlc/knowledge.py:L212)
- post_commit_path() (scripts/sdlc/knowledge.py:L225)
- hook_block() (scripts/sdlc/knowledge.py:L240)
- our_block_present() (scripts/sdlc/knowledge.py:L245)
- linked_worktree() (scripts/sdlc/knowledge.py:L250)
- A `git worktree` checkout: `.git` is a file pointing at the primary's git dir,… (scripts/sdlc/knowledge.py:L251)
- install_hook() (scripts/sdlc/knowledge.py:L255)
- Idempotent: replaces an existing sdlc block, otherwise appends after everything… (scripts/sdlc/knowledge.py:L256)
- unhook() (scripts/sdlc/knowledge.py:L269)
- StepFailed (scripts/sdlc/knowledge.py:L306)
- hooks_present() (scripts/sdlc/knowledge.py:L330)
- Both blocks in the post-commit file, read from the file (no subprocess). A… (scripts/sdlc/knowledge.py:L331)
- install_hooks() (scripts/sdlc/knowledge.py:L341)

# Depends on
- [ran](/modules/ran.md)
- [refresh](/modules/refresh.md)

# Inferred
- no INFERRED edges; treat any that appear as hints

# Features
- [Graphify and OKF knowledge base integration](/features/graphify-and-okf-knowledge-base-integration.md)
