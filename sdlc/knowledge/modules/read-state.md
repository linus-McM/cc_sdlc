---
type: Module
title: read_state
description: "Graphify community 76: scripts/sdlc/knowledge.py"
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
- state_path() (scripts/sdlc/knowledge.py:L196)
- read_state() (scripts/sdlc/knowledge.py:L200)
- write_state() (scripts/sdlc/knowledge.py:L204)
- bundle_present() (scripts/sdlc/knowledge.py:L347)
- A bundle counts only when it was built from the graph that exists now (an… (scripts/sdlc/knowledge.py:L348)
- graph_commit() (scripts/sdlc/knowledge.py:L417)
- behind() (scripts/sdlc/knowledge.py:L453)
- staleness() (scripts/sdlc/knowledge.py:L460)
- The cheap part of status: how far each index is behind HEAD and why a clean… (scripts/sdlc/knowledge.py:L461)

# Depends on
- [deploy.py](/modules/deploy-py.md)
- [project.py](/modules/project-py.md)
- [read_json](/modules/read-json.md)
- [refresh](/modules/refresh.md)

# Inferred
- no INFERRED edges; treat any that appear as hints

# Features
- [Graphify and OKF knowledge base integration](/features/graphify-and-okf-knowledge-base-integration.md)
