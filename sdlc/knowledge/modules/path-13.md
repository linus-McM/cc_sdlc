---
type: Module
title: Path
description: "Graphify community 13: plugin/README.md, plugin/scripts/sdlc/knowledge.py"
resource: plugin
tags: [module, graphify]
status: draft
generated: { by: sdlc/0.5.0, at: "2026-09-26T05:22:30Z" }
stale_after: "2026-10-10T05:22:30Z"
source_commit: c5f64f8d3b9b5e3268754f626b7f2e958fd6415e
sources:
  - { id: README, resource: plugin/README.md, last_modified: "2026-09-24T11:36:09+10:00", digest: 2e559b282f80c004 }
  - { id: knowledge, resource: plugin/scripts/sdlc/knowledge.py, last_modified: "2026-09-09T15:02:31+10:00", digest: 9f4a8d0ccc4c7375 }
---

# Files
- `plugin/README.md`
- `plugin/scripts/sdlc/knowledge.py`

# Symbols
- Knowledge (Graphify + OKF) (plugin/README.md:L36)
- hooks_dir() (plugin/scripts/sdlc/knowledge.py:L219)
- Git's hooks directory without spawning git: .git or the worktree's common dir,… (plugin/scripts/sdlc/knowledge.py:L220)
- post_commit_path() (plugin/scripts/sdlc/knowledge.py:L233)
- tool() (plugin/scripts/sdlc/knowledge.py:L237)
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
- write_ignore() (plugin/scripts/sdlc/knowledge.py:L349)
- build_bundle() (plugin/scripts/sdlc/knowledge.py:L363)
- pointer_present() (plugin/scripts/sdlc/knowledge.py:L368)
- review_counts() (plugin/scripts/sdlc/knowledge.py:L660)
- feature_status() (plugin/scripts/sdlc/knowledge.py:L668)
- feature_concepts() (plugin/scripts/sdlc/knowledge.py:L680)

# Depends on
- [Components](/modules/components.md)
- [docs.py](/modules/docs-py.md)
- [fail](/modules/fail.md)
- [fill](/modules/fill.md)
- [knowledge.py](/modules/knowledge-py.md)
- [Order of work](/modules/order-of-work-5.md)
- [Path](/modules/path.md)
- [pathlib](/modules/pathlib.md)
- [reconcile](/modules/reconcile.md)
- [refresh](/modules/refresh.md)
- [stages.py](/modules/stages-py.md)
- [StepSkipped](/modules/stepskipped.md)

# Inferred
- [refresh](/modules/refresh.md)

# Features
- [graph-selected repomix context packs](/features/graph-selected-repomix-context-packs.md)
