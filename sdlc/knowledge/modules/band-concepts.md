---
type: Module
title: band_concepts
description: "Graphify community 75: scripts/sdlc/artifacts.py, scripts/sdlc/knowledge.py"
resource: scripts/sdlc
tags: [module, graphify]
status: draft
generated: { by: sdlc/0.2.0, at: "2026-09-08T22:34:52Z" }
stale_after: "2026-09-22T22:34:52Z"
source_commit: 7062fb2891b2220b08230877b6bed905524ab89e
sources:
  - { id: artifacts, resource: scripts/sdlc/artifacts.py, last_modified: "2026-09-09T08:32:17+10:00", digest: 3e063b545e7dd897 }
  - { id: knowledge, resource: scripts/sdlc/knowledge.py, last_modified: "2026-09-09T08:32:17+10:00", digest: 5ed472fa5f0e7275 }
---

# Files
- `scripts/sdlc/artifacts.py`
- `scripts/sdlc/knowledge.py`

# Symbols
- slugify() (scripts/sdlc/artifacts.py:L30)
- as_actor() (scripts/sdlc/knowledge.py:L1017)
- OKF actor convention: human:<id>, process:<id> or <producer>/<version>; a bare… (scripts/sdlc/knowledge.py:L1018)
- god_nodes() (scripts/sdlc/knowledge.py:L562)
- The most connected code nodes by degree, from the graph already in memory (what… (scripts/sdlc/knowledge.py:L563)
- concept() (scripts/sdlc/knowledge.py:L573)
- section() (scripts/sdlc/knowledge.py:L586)
- module_concepts() (scripts/sdlc/knowledge.py:L596)
- hub_concepts() (scripts/sdlc/knowledge.py:L675)
- first_sentence() (scripts/sdlc/knowledge.py:L703)
- lesson_concepts() (scripts/sdlc/knowledge.py:L707)
- band_concepts() (scripts/sdlc/knowledge.py:L736)

# Depends on
- [maintain.py](/modules/maintain-py.md)
- [project.py](/modules/project-py.md)
- [read_json](/modules/read-json.md)

# Inferred
- no INFERRED edges; treat any that appear as hints

# Features
- [Graphify and OKF knowledge base integration](/features/graphify-and-okf-knowledge-base-integration.md)
