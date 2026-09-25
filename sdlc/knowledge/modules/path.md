---
type: Module
title: Path
description: "Graphify community 13: plugin/scripts/sdlc/knowledge.py"
resource: plugin/scripts/sdlc
tags: [module, graphify]
status: draft
generated: { by: sdlc/0.5.0, at: "2026-09-25T07:29:30Z" }
stale_after: "2026-10-09T07:29:30Z"
source_commit: dc32a5b78bc303376f02bfe7d43360ae82fa4a82
sources:
  - { id: knowledge, resource: plugin/scripts/sdlc/knowledge.py, last_modified: "2026-09-09T15:02:31+10:00", digest: 9f4a8d0ccc4c7375 }
---

# Files
- `plugin/scripts/sdlc/knowledge.py`

# Symbols
- concepts_for() (plugin/scripts/sdlc/knowledge.py:L1011)
- Project-relative module concept paths describing `rel`, from the file map the… (plugin/scripts/sdlc/knowledge.py:L1012)
- state_path() (plugin/scripts/sdlc/knowledge.py:L200)
- read_state() (plugin/scripts/sdlc/knowledge.py:L204)
- `.state.json`, or `{"_error": reason}` when it exists but cannot be read (a… (plugin/scripts/sdlc/knowledge.py:L205)
- write_state() (plugin/scripts/sdlc/knowledge.py:L212)
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
- bundle_present() (plugin/scripts/sdlc/knowledge.py:L358)
- A bundle counts only when it was built from the graph that exists now (an… (plugin/scripts/sdlc/knowledge.py:L359)
- graph_commit() (plugin/scripts/sdlc/knowledge.py:L439)

# Depends on
- [deploy.py](/modules/deploy-py.md)
- [docs.py](/modules/docs-py.md)
- [fail](/modules/fail.md)
- [fill](/modules/fill.md)
- [knowledge.py](/modules/knowledge-py.md)
- [refresh](/modules/refresh.md)
- [status](/modules/status.md)

# Inferred
- [Blocked](/modules/blocked.md)

# Features
- no feature plan names these files
