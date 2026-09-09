---
type: Module
title: Path
description: "Graphify community 22: scripts/sdlc/knowledge.py"
resource: scripts/sdlc
tags: [module, graphify]
status: draft
generated: { by: sdlc/0.2.1, at: "2026-09-09T03:02:28Z" }
stale_after: "2026-09-23T03:02:28Z"
source_commit: 5f197b911461521ad08675a63cc179623564938a
sources:
  - { id: knowledge, resource: scripts/sdlc/knowledge.py, last_modified: "2026-09-09T12:22:23+10:00", digest: 9f4a8d0ccc4c7375 }
---

# Files
- `scripts/sdlc/knowledge.py`

# Symbols
- shell_word() (scripts/sdlc/knowledge.py:L183)
- `text` as one double-quoted POSIX shell word: backslash, double quote, dollar… (scripts/sdlc/knowledge.py:L184)
- graph_path() (scripts/sdlc/knowledge.py:L192)
- skill_path() (scripts/sdlc/knowledge.py:L196)
- hooks_dir() (scripts/sdlc/knowledge.py:L219)
- Git's hooks directory without spawning git: .git or the worktree's common dir,… (scripts/sdlc/knowledge.py:L220)
- post_commit_path() (scripts/sdlc/knowledge.py:L233)
- hook_block() (scripts/sdlc/knowledge.py:L249)
- our_block_present() (scripts/sdlc/knowledge.py:L254)
- linked_worktree() (scripts/sdlc/knowledge.py:L259)
- A `git worktree` checkout: `.git` is a file pointing at the primary's git dir,… (scripts/sdlc/knowledge.py:L260)
- install_hook() (scripts/sdlc/knowledge.py:L264)
- Idempotent: replaces an existing sdlc block, otherwise appends after everything… (scripts/sdlc/knowledge.py:L265)
- unhook() (scripts/sdlc/knowledge.py:L278)
- install_skill() (scripts/sdlc/knowledge.py:L323)
- hooks_present() (scripts/sdlc/knowledge.py:L327)
- Both blocks in the post-commit file, read from the file (no subprocess). A… (scripts/sdlc/knowledge.py:L328)
- install_hooks() (scripts/sdlc/knowledge.py:L338)
- build_graph() (scripts/sdlc/knowledge.py:L354)
- artifacts_agree() (scripts/sdlc/knowledge.py:L453)
- load_graph() (scripts/sdlc/knowledge.py:L549)

# Depends on
- [docs.py](/modules/docs-py.md)
- [fail](/modules/fail.md)
- [project.py](/modules/project-py.md)
- [status](/modules/status.md)

# Inferred
- no INFERRED edges; treat any that appear as hints

# Features
- [Archify stage documentation](/features/archify-stage-documentation.md)
- [Graphify and OKF knowledge base integration](/features/graphify-and-okf-knowledge-base-integration.md)
