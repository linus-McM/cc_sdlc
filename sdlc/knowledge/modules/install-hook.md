---
type: Module
title: install_hook
description: "Graphify community 22: scripts/sdlc/knowledge.py"
resource: scripts/sdlc
tags: [module, graphify]
status: draft
generated: { by: sdlc/0.2.1, at: "2026-09-09T03:05:50Z" }
stale_after: "2026-09-23T03:05:50Z"
source_commit: f99c31fe37e72ede2fd21532a6ffb7137b40bc9e
sources:
  - { id: knowledge, resource: scripts/sdlc/knowledge.py, last_modified: "2026-09-09T13:02:29+10:00", digest: 9f4a8d0ccc4c7375 }
---

# Files
- `scripts/sdlc/knowledge.py`

# Symbols
- shell_word() (scripts/sdlc/knowledge.py:L183)
- `text` as one double-quoted POSIX shell word: backslash, double quote, dollar… (scripts/sdlc/knowledge.py:L184)
- hooks_dir() (scripts/sdlc/knowledge.py:L219)
- Git's hooks directory without spawning git: .git or the worktree's common dir,… (scripts/sdlc/knowledge.py:L220)
- post_commit_path() (scripts/sdlc/knowledge.py:L233)
- hook_block() (scripts/sdlc/knowledge.py:L249)
- our_block_present() (scripts/sdlc/knowledge.py:L254)
- linked_worktree() (scripts/sdlc/knowledge.py:L259)
- A `git worktree` checkout: `.git` is a file pointing at the primary's git dir,… (scripts/sdlc/knowledge.py:L260)
- install_hook() (scripts/sdlc/knowledge.py:L264)
- Idempotent: replaces an existing sdlc block, otherwise appends after everything… (scripts/sdlc/knowledge.py:L265)
- hooks_present() (scripts/sdlc/knowledge.py:L327)
- Both blocks in the post-commit file, read from the file (no subprocess). A… (scripts/sdlc/knowledge.py:L328)
- install_hooks() (scripts/sdlc/knowledge.py:L338)

# Depends on
- [docs.py](/modules/docs-py.md)
- [Path](/modules/path.md)
- [status](/modules/status.md)

# Inferred
- no INFERRED edges; treat any that appear as hints

# Features
- [Archify stage documentation](/features/archify-stage-documentation.md)
- [Graphify and OKF knowledge base integration](/features/graphify-and-okf-knowledge-base-integration.md)
