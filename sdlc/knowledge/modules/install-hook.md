---
type: Module
title: install_hook
description: "Graphify community 13: plugin/scripts/sdlc/knowledge.py, sdlc/graphify-and-okf-knowledge-base-integration/review.md"
resource: ""
tags: [module, graphify]
status: draft
generated: { by: sdlc/0.5.0, at: "2026-09-25T23:27:53Z" }
stale_after: "2026-10-09T23:27:53Z"
source_commit: 1348ec2a58c87325a8bcaacd936bc4bc9473c870
sources:
  - { id: knowledge, resource: plugin/scripts/sdlc/knowledge.py, last_modified: "2026-09-09T15:02:31+10:00", digest: 9f4a8d0ccc4c7375 }
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
- hooks_present() (plugin/scripts/sdlc/knowledge.py:L327)
- Both blocks in the post-commit file, read from the file (no subprocess). A… (plugin/scripts/sdlc/knowledge.py:L328)
- install_hooks() (plugin/scripts/sdlc/knowledge.py:L338)
- signature() (plugin/scripts/sdlc/knowledge.py:L802)
- Content identity: the builder's keys (present on either side) plus the body;… (plugin/scripts/sdlc/knowledge.py:L803)
- Compliance (sdlc/graphify-and-okf-knowledge-base-integration/review.md:L16)

# Depends on
- [fail](/modules/fail.md)
- [knowledge.py](/modules/knowledge-py.md)
- [Path](/modules/path.md)
- [StepSkipped](/modules/stepskipped.md)

# Inferred
- [fail](/modules/fail.md)
- [Order of work](/modules/order-of-work-5.md)
- [Path](/modules/path.md)
- [post_edit](/modules/post-edit.md)
- [test_hooks.py](/modules/test-hooks-py.md)

# Features
- no feature plan names these files
