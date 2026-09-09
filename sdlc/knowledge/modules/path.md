---
type: Module
title: Path
description: "Graphify community 72: scripts/sdlc/knowledge.py"
resource: scripts/sdlc
tags: [module, graphify]
status: draft
generated: { by: sdlc/0.2.0, at: "2026-09-09T00:28:34Z" }
stale_after: "2026-09-23T00:28:34Z"
source_commit: 614af23c7f6ad2aa72305090f08b8c7fff243ba5
sources:
  - { id: knowledge, resource: scripts/sdlc/knowledge.py, last_modified: "2026-09-09T10:18:34+10:00", digest: 8da5a1d01eeb439c }
---

# Files
- `scripts/sdlc/knowledge.py`

# Symbols
- graph_path() (scripts/sdlc/knowledge.py:L187)
- skill_path() (scripts/sdlc/knowledge.py:L191)
- state_path() (scripts/sdlc/knowledge.py:L196)
- read_state() (scripts/sdlc/knowledge.py:L200)
- write_state() (scripts/sdlc/knowledge.py:L204)
- tool() (scripts/sdlc/knowledge.py:L229)
- ran() (scripts/sdlc/knowledge.py:L310)
- Run an install command; StepFailed with its stderr tail when it exits non-zero… (scripts/sdlc/knowledge.py:L311)
- install_graphify() (scripts/sdlc/knowledge.py:L322)
- install_skill() (scripts/sdlc/knowledge.py:L326)
- write_ignore() (scripts/sdlc/knowledge.py:L352)
- build_graph() (scripts/sdlc/knowledge.py:L357)
- bundle_present() (scripts/sdlc/knowledge.py:L361)
- A bundle counts only when it was built from the graph that exists now (an… (scripts/sdlc/knowledge.py:L362)
- build_bundle() (scripts/sdlc/knowledge.py:L366)
- pointer_present() (scripts/sdlc/knowledge.py:L371)
- graph_commit() (scripts/sdlc/knowledge.py:L431)
- artifacts_agree() (scripts/sdlc/knowledge.py:L451)
- behind() (scripts/sdlc/knowledge.py:L467)
- staleness() (scripts/sdlc/knowledge.py:L474)
- The cheap part of status: how far each index is behind HEAD and why a clean… (scripts/sdlc/knowledge.py:L475)

# Depends on
- [post_commit_path](/modules/post-commit-path.md)
- [project.py](/modules/project-py.md)
- [read_json](/modules/read-json.md)
- [refresh](/modules/refresh.md)

# Inferred
- no INFERRED edges; treat any that appear as hints

# Features
- [Graphify and OKF knowledge base integration](/features/graphify-and-okf-knowledge-base-integration.md)
