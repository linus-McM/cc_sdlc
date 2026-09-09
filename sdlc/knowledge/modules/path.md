---
type: Module
title: Path
description: "Graphify community 72: scripts/sdlc/artifacts.py, scripts/sdlc/knowledge.py"
resource: scripts/sdlc
tags: [module, graphify]
status: draft
generated: { by: sdlc/0.2.1, at: "2026-09-09T02:45:02Z" }
stale_after: "2026-09-23T02:45:02Z"
source_commit: 16ce44221e592819936583be6bb11207ce568f21
sources:
  - { id: artifacts, resource: scripts/sdlc/artifacts.py, last_modified: "2026-09-09T08:32:17+10:00", digest: 3e063b545e7dd897 }
  - { id: knowledge, resource: scripts/sdlc/knowledge.py, last_modified: "2026-09-09T12:22:23+10:00", digest: 41ab4ac9324ee352 }
---

# Files
- `scripts/sdlc/artifacts.py`
- `scripts/sdlc/knowledge.py`

# Symbols
- render() (scripts/sdlc/artifacts.py:L88)
- graph_path() (scripts/sdlc/knowledge.py:L192)
- skill_path() (scripts/sdlc/knowledge.py:L196)
- install_graphify() (scripts/sdlc/knowledge.py:L319)
- install_skill() (scripts/sdlc/knowledge.py:L323)
- write_ignore() (scripts/sdlc/knowledge.py:L349)
- build_graph() (scripts/sdlc/knowledge.py:L354)
- bundle_present() (scripts/sdlc/knowledge.py:L358)
- A bundle counts only when it was built from the graph that exists now (an… (scripts/sdlc/knowledge.py:L359)
- pointer_present() (scripts/sdlc/knowledge.py:L368)
- write_pointer() (scripts/sdlc/knowledge.py:L375)
- graph_commit() (scripts/sdlc/knowledge.py:L433)
- artifacts_agree() (scripts/sdlc/knowledge.py:L453)
- behind() (scripts/sdlc/knowledge.py:L469)
- Commits from `since` to HEAD; None when git cannot resolve `since` (shallow… (scripts/sdlc/knowledge.py:L470)
- staleness() (scripts/sdlc/knowledge.py:L477)
- The cheap part of status: how far each index is behind HEAD and why a clean… (scripts/sdlc/knowledge.py:L478)
- load_graph() (scripts/sdlc/knowledge.py:L549)
- index_lines() (scripts/sdlc/knowledge.py:L850)
- `* [Title](link) - description` per concept, sorted by title; sub-indexes link… (scripts/sdlc/knowledge.py:L851)
- write_indexes() (scripts/sdlc/knowledge.py:L857)
- append_log() (scripts/sdlc/knowledge.py:L868)

# Depends on
- [docs.py](/modules/docs-py.md)
- [project.py](/modules/project-py.md)
- [refresh](/modules/refresh.md)
- [status](/modules/status.md)

# Inferred
- no INFERRED edges; treat any that appear as hints

# Features
- [Archify stage documentation](/features/archify-stage-documentation.md)
- [Graphify and OKF knowledge base integration](/features/graphify-and-okf-knowledge-base-integration.md)
