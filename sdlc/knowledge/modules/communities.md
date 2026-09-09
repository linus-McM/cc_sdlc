---
type: Module
title: communities
description: "Graphify community 0: scripts/sdlc/artifacts.py, scripts/sdlc/knowledge.py"
resource: scripts/sdlc
tags: [module, graphify]
status: draft
generated: { by: sdlc/0.2.1, at: "2026-09-09T03:02:33Z" }
stale_after: "2026-09-23T03:02:33Z"
source_commit: 7a6549e2e0a57fe6fe0b1257011d2e78bce58136
sources:
  - { id: artifacts, resource: scripts/sdlc/artifacts.py, last_modified: "2026-09-09T08:32:17+10:00", digest: 3e063b545e7dd897 }
  - { id: knowledge, resource: scripts/sdlc/knowledge.py, last_modified: "2026-09-09T13:02:29+10:00", digest: 9f4a8d0ccc4c7375 }
---

# Files
- `scripts/sdlc/artifacts.py`
- `scripts/sdlc/knowledge.py`

# Symbols
- slugify() (scripts/sdlc/artifacts.py:L30)
- as_actor() (scripts/sdlc/knowledge.py:L1060)
- OKF actor convention: human:<id>, process:<id> or <producer>/<version>; a bare… (scripts/sdlc/knowledge.py:L1061)
- is_code() (scripts/sdlc/knowledge.py:L559)
- Graphify tags code, document and rationale nodes; only code communities become… (scripts/sdlc/knowledge.py:L560)
- communities() (scripts/sdlc/knowledge.py:L575)
- Graphify code communities big enough for a Module concept, with a stable slug… (scripts/sdlc/knowledge.py:L576)
- god_nodes() (scripts/sdlc/knowledge.py:L595)
- The most connected code nodes by degree, from the graph already in memory (what… (scripts/sdlc/knowledge.py:L596)
- hub_concepts() (scripts/sdlc/knowledge.py:L709)

# Depends on
- [knowledge.py](/modules/knowledge-py.md)
- [Path](/modules/path.md)

# Inferred
- no INFERRED edges; treat any that appear as hints

# Features
- [Archify stage documentation](/features/archify-stage-documentation.md)
- [Graphify and OKF knowledge base integration](/features/graphify-and-okf-knowledge-base-integration.md)
