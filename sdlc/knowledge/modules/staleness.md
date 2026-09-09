---
type: Module
title: staleness
description: "Graphify community 81: scripts/sdlc/knowledge.py"
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
- bundle_present() (scripts/sdlc/knowledge.py:L358)
- A bundle counts only when it was built from the graph that exists now (an… (scripts/sdlc/knowledge.py:L359)
- graph_commit() (scripts/sdlc/knowledge.py:L433)
- behind() (scripts/sdlc/knowledge.py:L469)
- Commits from `since` to HEAD; None when git cannot resolve `since` (shallow… (scripts/sdlc/knowledge.py:L470)
- staleness() (scripts/sdlc/knowledge.py:L477)
- The cheap part of status: how far each index is behind HEAD and why a clean… (scripts/sdlc/knowledge.py:L478)

# Depends on
- [Path](/modules/path.md)
- [project.py](/modules/project-py.md)
- [refresh](/modules/refresh.md)
- [status](/modules/status.md)

# Inferred
- no INFERRED edges; treat any that appear as hints

# Features
- [Archify stage documentation](/features/archify-stage-documentation.md)
- [Graphify and OKF knowledge base integration](/features/graphify-and-okf-knowledge-base-integration.md)
