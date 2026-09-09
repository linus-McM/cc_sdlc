---
type: Module
title: communities
description: "Graphify community 88: scripts/sdlc/artifacts.py, scripts/sdlc/knowledge.py"
resource: scripts/sdlc
tags: [module, graphify]
status: draft
generated: { by: sdlc/0.2.1, at: "2026-09-09T01:48:10Z" }
stale_after: "2026-09-23T01:48:10Z"
source_commit: f5370acaa20694aba335e2e3cab1cee4dc0582a5
sources:
  - { id: artifacts, resource: scripts/sdlc/artifacts.py, last_modified: "2026-09-09T08:32:17+10:00", digest: 3e063b545e7dd897 }
  - { id: knowledge, resource: scripts/sdlc/knowledge.py, last_modified: "2026-09-09T10:28:52+10:00", digest: 8da5a1d01eeb439c }
---

# Files
- `scripts/sdlc/artifacts.py`
- `scripts/sdlc/knowledge.py`

# Symbols
- slugify() (scripts/sdlc/artifacts.py:L30)
- as_actor() (scripts/sdlc/knowledge.py:L1072)
- OKF actor convention: human:<id>, process:<id> or <producer>/<version>; a bare… (scripts/sdlc/knowledge.py:L1073)
- is_code() (scripts/sdlc/knowledge.py:L572)
- Graphify tags code, document and rationale nodes; only code communities become… (scripts/sdlc/knowledge.py:L573)
- communities() (scripts/sdlc/knowledge.py:L588)
- Graphify code communities big enough for a Module concept, with a stable slug… (scripts/sdlc/knowledge.py:L589)
- god_nodes() (scripts/sdlc/knowledge.py:L608)
- The most connected code nodes by degree, from the graph already in memory (what… (scripts/sdlc/knowledge.py:L609)
- hub_concepts() (scripts/sdlc/knowledge.py:L721)

# Depends on
- [knowledge.py](/modules/knowledge-py.md)
- [Path](/modules/path.md)

# Inferred
- no INFERRED edges; treat any that appear as hints

# Features
- [Graphify and OKF knowledge base integration](/features/graphify-and-okf-knowledge-base-integration.md)
