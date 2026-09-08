---
type: Module
title: Path
description: "Graphify community 22: scripts/sdlc/knowledge.py"
resource: scripts/sdlc
tags: [module, graphify]
status: draft
generated: { by: sdlc/0.2.0, at: "2026-09-08T22:34:52Z" }
stale_after: "2026-09-22T22:34:52Z"
source_commit: 7062fb2891b2220b08230877b6bed905524ab89e
sources:
  - { id: knowledge, resource: scripts/sdlc/knowledge.py, last_modified: "2026-09-09T08:32:17+10:00", digest: 5ed472fa5f0e7275 }
---

# Files
- `scripts/sdlc/knowledge.py`

# Symbols
- cfg() (scripts/sdlc/knowledge.py:L179)
- hooks_dir() (scripts/sdlc/knowledge.py:L211)
- Git's hooks directory without spawning git: .git or the worktree's common dir,… (scripts/sdlc/knowledge.py:L212)
- post_commit_path() (scripts/sdlc/knowledge.py:L225)
- hook_block() (scripts/sdlc/knowledge.py:L240)
- our_block_present() (scripts/sdlc/knowledge.py:L245)
- install_hook() (scripts/sdlc/knowledge.py:L250)
- Idempotent: replaces an existing sdlc block, otherwise appends after everything… (scripts/sdlc/knowledge.py:L251)
- unhook() (scripts/sdlc/knowledge.py:L262)
- hooks_present() (scripts/sdlc/knowledge.py:L323)
- Both blocks in the post-commit file; Graphify's marker is read from the file,… (scripts/sdlc/knowledge.py:L324)
- install_hooks() (scripts/sdlc/knowledge.py:L329)
- write_ignore() (scripts/sdlc/knowledge.py:L338)
- build_bundle() (scripts/sdlc/knowledge.py:L352)
- pointer_present() (scripts/sdlc/knowledge.py:L357)
- bootstrap() (scripts/sdlc/knowledge.py:L384)
- rebuild_log_tail() (scripts/sdlc/knowledge.py:L425)
- Last line of Graphify's rebuild log, read from its tail only (the log is… (scripts/sdlc/knowledge.py:L426)
- concepts_for() (scripts/sdlc/knowledge.py:L968)
- Project-relative module concept paths describing `rel`, from the file map the… (scripts/sdlc/knowledge.py:L969)

# Depends on
- [hooks.py](/modules/hooks-py.md)
- [ran](/modules/ran.md)
- [read_state](/modules/read-state.md)
- [refresh](/modules/refresh.md)

# Inferred
- no INFERRED edges; treat any that appear as hints

# Features
- [Graphify and OKF knowledge base integration](/features/graphify-and-okf-knowledge-base-integration.md)
