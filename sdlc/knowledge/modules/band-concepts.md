---
type: Module
title: band_concepts
description: "Graphify community 0: scripts/sdlc/artifacts.py, scripts/sdlc/knowledge.py"
resource: scripts/sdlc
tags: [module, graphify]
status: draft
generated: { by: sdlc/0.2.1, at: "2026-09-09T02:15:57Z" }
stale_after: "2026-09-23T02:15:57Z"
source_commit: 6ea21e5e3cd13550f8e86b9940edfc0da2010101
sources:
  - { id: artifacts, resource: scripts/sdlc/artifacts.py, last_modified: "2026-09-09T08:32:17+10:00", digest: 3e063b545e7dd897 }
  - { id: knowledge, resource: scripts/sdlc/knowledge.py, last_modified: "2026-09-09T12:08:42+10:00", digest: 9f7d0b83d716857f }
---

# Files
- `scripts/sdlc/artifacts.py`
- `scripts/sdlc/knowledge.py`

# Symbols
- slugify() (scripts/sdlc/artifacts.py:L30)
- as_actor() (scripts/sdlc/knowledge.py:L1083)
- OKF actor convention: human:<id>, process:<id> or <producer>/<version>; a bare… (scripts/sdlc/knowledge.py:L1084)
- god_nodes() (scripts/sdlc/knowledge.py:L618)
- The most connected code nodes by degree, from the graph already in memory (what… (scripts/sdlc/knowledge.py:L619)
- concept() (scripts/sdlc/knowledge.py:L629)
- section() (scripts/sdlc/knowledge.py:L642)
- module_concepts() (scripts/sdlc/knowledge.py:L652)
- hub_concepts() (scripts/sdlc/knowledge.py:L732)
- first_sentence() (scripts/sdlc/knowledge.py:L760)
- lesson_concepts() (scripts/sdlc/knowledge.py:L764)
- band_concepts() (scripts/sdlc/knowledge.py:L793)

# Depends on
- [communities](/modules/communities.md)
- [maintain.py](/modules/maintain-py.md)
- [project.py](/modules/project-py.md)

# Inferred
- no INFERRED edges; treat any that appear as hints

# Features
- [Archify stage documentation](/features/archify-stage-documentation.md)
- [Graphify and OKF knowledge base integration](/features/graphify-and-okf-knowledge-base-integration.md)
