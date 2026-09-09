---
type: Module
title: install_hook
description: "Graphify community 22: scripts/sdlc/knowledge.py"
resource: scripts/sdlc
tags: [module, graphify]
status: draft
generated: { by: sdlc/0.2.1, at: "2026-09-09T02:01:32Z" }
stale_after: "2026-09-23T02:01:32Z"
source_commit: d8d61950c58abafa13a30ef68be4741e547839ef
sources:
  - { id: knowledge, resource: scripts/sdlc/knowledge.py, last_modified: "2026-09-09T10:28:52+10:00", digest: 8da5a1d01eeb439c }
---

# Files
- `scripts/sdlc/knowledge.py`

# Symbols
- shell_word() (scripts/sdlc/knowledge.py:L191)
- `text` as one double-quoted POSIX shell word: backslash, double quote, dollar… (scripts/sdlc/knowledge.py:L192)
- hooks_dir() (scripts/sdlc/knowledge.py:L228)
- Git's hooks directory without spawning git: .git or the worktree's common dir,… (scripts/sdlc/knowledge.py:L229)
- post_commit_path() (scripts/sdlc/knowledge.py:L242)
- hook_block() (scripts/sdlc/knowledge.py:L258)
- our_block_present() (scripts/sdlc/knowledge.py:L263)
- linked_worktree() (scripts/sdlc/knowledge.py:L268)
- A `git worktree` checkout: `.git` is a file pointing at the primary's git dir,… (scripts/sdlc/knowledge.py:L269)
- install_hook() (scripts/sdlc/knowledge.py:L273)
- Idempotent: replaces an existing sdlc block, otherwise appends after everything… (scripts/sdlc/knowledge.py:L274)
- unhook() (scripts/sdlc/knowledge.py:L287)
- StepFailed (scripts/sdlc/knowledge.py:L324)
- StepSkipped (scripts/sdlc/knowledge.py:L328)
- This step does not apply here; later steps still run. (scripts/sdlc/knowledge.py:L329)
- hooks_present() (scripts/sdlc/knowledge.py:L352)
- Both blocks in the post-commit file, read from the file (no subprocess). A… (scripts/sdlc/knowledge.py:L353)
- install_hooks() (scripts/sdlc/knowledge.py:L363)

# Depends on
- [fail](/modules/fail.md)
- [Path](/modules/path.md)
- [refresh](/modules/refresh.md)

# Inferred
- no INFERRED edges; treat any that appear as hints

# Features
- [Archify stage documentation](/features/archify-stage-documentation.md)
- [Graphify and OKF knowledge base integration](/features/graphify-and-okf-knowledge-base-integration.md)
