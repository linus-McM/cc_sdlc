---
type: Module
title: band_concepts
description: "Graphify community 0: scripts/sdlc/artifacts.py, scripts/sdlc/knowledge.py"
resource: scripts/sdlc
tags: [module, graphify]
status: draft
generated: { by: sdlc/0.2.1, at: "2026-09-09T03:02:28Z" }
stale_after: "2026-09-23T03:02:28Z"
source_commit: 5f197b911461521ad08675a63cc179623564938a
sources:
  - { id: artifacts, resource: scripts/sdlc/artifacts.py, last_modified: "2026-09-09T08:32:17+10:00", digest: 3e063b545e7dd897 }
  - { id: knowledge, resource: scripts/sdlc/knowledge.py, last_modified: "2026-09-09T12:22:23+10:00", digest: 9f4a8d0ccc4c7375 }
---

# Files
- `scripts/sdlc/artifacts.py`
- `scripts/sdlc/knowledge.py`

# Symbols
- slugify() (scripts/sdlc/artifacts.py:L30)
- as_actor() (scripts/sdlc/knowledge.py:L1054)
- OKF actor convention: human:<id>, process:<id> or <producer>/<version>; a bare… (scripts/sdlc/knowledge.py:L1055)
- is_code() (scripts/sdlc/knowledge.py:L553)
- Graphify tags code, document and rationale nodes; only code communities become… (scripts/sdlc/knowledge.py:L554)
- community_labels() (scripts/sdlc/knowledge.py:L560)
- communities() (scripts/sdlc/knowledge.py:L569)
- Graphify code communities big enough for a Module concept, with a stable slug… (scripts/sdlc/knowledge.py:L570)
- god_nodes() (scripts/sdlc/knowledge.py:L589)
- The most connected code nodes by degree, from the graph already in memory (what… (scripts/sdlc/knowledge.py:L590)
- concept() (scripts/sdlc/knowledge.py:L600)
- section() (scripts/sdlc/knowledge.py:L613)
- module_concepts() (scripts/sdlc/knowledge.py:L623)
- hub_concepts() (scripts/sdlc/knowledge.py:L703)
- first_sentence() (scripts/sdlc/knowledge.py:L731)
- lesson_concepts() (scripts/sdlc/knowledge.py:L735)
- band_concepts() (scripts/sdlc/knowledge.py:L764)

# Depends on
- [config](/modules/config.md)
- [docs.py](/modules/docs-py.md)
- [Path](/modules/path.md)
- [project.py](/modules/project-py.md)

# Inferred
- no INFERRED edges; treat any that appear as hints

# Features
- [Archify stage documentation](/features/archify-stage-documentation.md)
- [Graphify and OKF knowledge base integration](/features/graphify-and-okf-knowledge-base-integration.md)
