---
type: Module
title: staleness
description: "Graphify community 79: scripts/sdlc/knowledge.py"
resource: scripts/sdlc
tags: [module, graphify]
status: draft
generated: { by: sdlc/0.2.0, at: "2026-09-09T00:28:56Z" }
stale_after: "2026-09-23T00:28:56Z"
source_commit: e46d381e2f64fa96bbb6eee6115eba30499cfe2e
sources:
  - { id: knowledge, resource: scripts/sdlc/knowledge.py, last_modified: "2026-09-09T10:28:52+10:00", digest: 8da5a1d01eeb439c }
---

# Files
- `scripts/sdlc/knowledge.py`

# Symbols
- bundle_present() (scripts/sdlc/knowledge.py:L383)
- A bundle counts only when it was built from the graph that exists now (an… (scripts/sdlc/knowledge.py:L384)
- graph_commit() (scripts/sdlc/knowledge.py:L455)
- behind() (scripts/sdlc/knowledge.py:L491)
- Commits from `since` to HEAD; None when git cannot resolve `since` (shallow… (scripts/sdlc/knowledge.py:L492)
- staleness() (scripts/sdlc/knowledge.py:L499)
- The cheap part of status: how far each index is behind HEAD and why a clean… (scripts/sdlc/knowledge.py:L500)

# Depends on
- [cfg](/modules/cfg.md)
- [project.py](/modules/project-py.md)
- [read_json](/modules/read-json.md)
- [refresh](/modules/refresh.md)

# Inferred
- no INFERRED edges; treat any that appear as hints

# Features
- [Graphify and OKF knowledge base integration](/features/graphify-and-okf-knowledge-base-integration.md)
