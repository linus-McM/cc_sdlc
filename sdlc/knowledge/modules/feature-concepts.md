---
type: Module
title: feature_concepts
description: "Graphify community 0: scripts/sdlc/artifacts.py, scripts/sdlc/knowledge.py"
resource: scripts/sdlc
tags: [module, graphify]
status: draft
generated: { by: sdlc/0.2.1, at: "2026-09-09T02:11:11Z" }
stale_after: "2026-09-23T02:11:11Z"
source_commit: b6ac2e811acbc23d7c5c8119fd8dd5532b43ccd0
sources:
  - { id: artifacts, resource: scripts/sdlc/artifacts.py, last_modified: "2026-09-09T08:32:17+10:00", digest: 3e063b545e7dd897 }
  - { id: knowledge, resource: scripts/sdlc/knowledge.py, last_modified: "2026-09-09T12:08:42+10:00", digest: 9f7d0b83d716857f }
---

# Files
- `scripts/sdlc/artifacts.py`
- `scripts/sdlc/knowledge.py`

# Symbols
- slugify() (scripts/sdlc/artifacts.py:L30)
- first_line() (scripts/sdlc/artifacts.py:L74)
- The first filled line of a section body, skipping template placeholders. (scripts/sdlc/artifacts.py:L75)
- as_actor() (scripts/sdlc/knowledge.py:L1083)
- OKF actor convention: human:<id>, process:<id> or <producer>/<version>; a bare… (scripts/sdlc/knowledge.py:L1084)
- is_code() (scripts/sdlc/knowledge.py:L582)
- Graphify tags code, document and rationale nodes; only code communities become… (scripts/sdlc/knowledge.py:L583)
- communities() (scripts/sdlc/knowledge.py:L598)
- Graphify code communities big enough for a Module concept, with a stable slug… (scripts/sdlc/knowledge.py:L599)
- god_nodes() (scripts/sdlc/knowledge.py:L618)
- The most connected code nodes by degree, from the graph already in memory (what… (scripts/sdlc/knowledge.py:L619)
- concept() (scripts/sdlc/knowledge.py:L629)
- section() (scripts/sdlc/knowledge.py:L642)
- module_concepts() (scripts/sdlc/knowledge.py:L652)
- review_counts() (scripts/sdlc/knowledge.py:L683)
- feature_status() (scripts/sdlc/knowledge.py:L691)
- feature_concepts() (scripts/sdlc/knowledge.py:L703)
- hub_concepts() (scripts/sdlc/knowledge.py:L732)
- first_sentence() (scripts/sdlc/knowledge.py:L760)
- lesson_concepts() (scripts/sdlc/knowledge.py:L764)
- band_concepts() (scripts/sdlc/knowledge.py:L793)

# Depends on
- [artifacts.py](/modules/artifacts-py.md)
- [deploy.py](/modules/deploy-py.md)
- [docs.py](/modules/docs-py.md)
- [fail](/modules/fail.md)
- [knowledge.py](/modules/knowledge-py.md)
- [maintain.py](/modules/maintain-py.md)
- [Path](/modules/path.md)
- [project.py](/modules/project-py.md)
- [stages.py](/modules/stages-py.md)

# Inferred
- no INFERRED edges; treat any that appear as hints

# Features
- [Archify stage documentation](/features/archify-stage-documentation.md)
- [Graphify and OKF knowledge base integration](/features/graphify-and-okf-knowledge-base-integration.md)
