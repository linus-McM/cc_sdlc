---
type: Module
title: install_hook
description: "Graphify community 17: plugin/scripts/sdlc/knowledge.py, sdlc/graphify-and-okf-knowledge-base-integration/review.md"
resource: ""
tags: [module, graphify]
status: draft
generated: { by: sdlc/0.8.1, at: "2026-09-28T22:57:53Z" }
stale_after: "2026-10-12T22:57:53Z"
source_commit: 0754d821fc594b90c529849cddaca10dc6109921
sources:
  - { id: knowledge, resource: plugin/scripts/sdlc/knowledge.py, last_modified: "2026-09-29T08:42:51+10:00", digest: d350848efe5d7fe2 }
  - { id: review, resource: sdlc/graphify-and-okf-knowledge-base-integration/review.md, last_modified: "2026-09-09T15:03:27+10:00", digest: b6e15f798eacd1f2 }
---

# Files
- `plugin/scripts/sdlc/knowledge.py`
- `sdlc/graphify-and-okf-knowledge-base-integration/review.md`

# Symbols
- shell_word() (plugin/scripts/sdlc/knowledge.py:L183)
- `text` as one double-quoted POSIX shell word: backslash, double quote, dollar… (plugin/scripts/sdlc/knowledge.py:L184)
- hooks_dir() (plugin/scripts/sdlc/knowledge.py:L219)
- Git's hooks directory without spawning git: .git or the worktree's common dir,… (plugin/scripts/sdlc/knowledge.py:L220)
- post_commit_path() (plugin/scripts/sdlc/knowledge.py:L233)
- hook_block() (plugin/scripts/sdlc/knowledge.py:L249)
- our_block_present() (plugin/scripts/sdlc/knowledge.py:L254)
- linked_worktree() (plugin/scripts/sdlc/knowledge.py:L259)
- A `git worktree` checkout: `.git` is a file pointing at the primary's git dir,… (plugin/scripts/sdlc/knowledge.py:L260)
- install_hook() (plugin/scripts/sdlc/knowledge.py:L264)
- Idempotent: replaces an existing sdlc block, otherwise appends after everything… (plugin/scripts/sdlc/knowledge.py:L265)
- repoint_hook() (plugin/scripts/sdlc/knowledge.py:L277)
- Rewrite an sdlc block that names another plugin path (moved or upgraded) to… (plugin/scripts/sdlc/knowledge.py:L278)
- hooks_present() (plugin/scripts/sdlc/knowledge.py:L337)
- Both blocks in the post-commit file, read from the file (no subprocess). A… (plugin/scripts/sdlc/knowledge.py:L338)
- install_hooks() (plugin/scripts/sdlc/knowledge.py:L348)
- signature() (plugin/scripts/sdlc/knowledge.py:L816)
- Content identity: the builder's keys (present on either side) plus the body;… (plugin/scripts/sdlc/knowledge.py:L817)
- Compliance (sdlc/graphify-and-okf-knowledge-base-integration/review.md:L16)

# Depends on
- [cfg](/modules/cfg.md)
- [fail](/modules/fail.md)
- [packs.py](/modules/packs-py.md)
- [StepSkipped](/modules/stepskipped.md)

# Inferred
- [fail](/modules/fail.md)
- [hooks.py](/modules/hooks-py.md)
- [Order of work](/modules/order-of-work.md)
- [Path](/modules/path.md)
- [test_hooks.py](/modules/test-hooks-py.md)

# Features
- [graph-selected repomix context packs](/features/graph-selected-repomix-context-packs.md)
