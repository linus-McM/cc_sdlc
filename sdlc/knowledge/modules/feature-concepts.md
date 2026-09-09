---
type: Module
title: feature_concepts
description: "Graphify community 0: scripts/sdlc/artifacts.py, scripts/sdlc/knowledge.py"
resource: scripts/sdlc
tags: [module, graphify]
status: draft
generated: { by: sdlc/0.2.1, at: "2026-09-09T01:29:56Z" }
stale_after: "2026-09-23T01:29:56Z"
source_commit: b6e8d5897548ac1aeadd713c4fd9bf19fac3d435
sources:
  - { id: artifacts, resource: scripts/sdlc/artifacts.py, last_modified: "2026-09-09T08:32:17+10:00", digest: 3e063b545e7dd897 }
  - { id: knowledge, resource: scripts/sdlc/knowledge.py, last_modified: "2026-09-09T10:28:52+10:00", digest: 8da5a1d01eeb439c }
---

# Files
- `scripts/sdlc/artifacts.py`
- `scripts/sdlc/knowledge.py`

# Symbols
- slugify() (scripts/sdlc/artifacts.py:L30)
- first_line() (scripts/sdlc/artifacts.py:L74)
- The first filled line of a section body, skipping template placeholders. (scripts/sdlc/artifacts.py:L75)
- as_actor() (scripts/sdlc/knowledge.py:L1072)
- OKF actor convention: human:<id>, process:<id> or <producer>/<version>; a bare… (scripts/sdlc/knowledge.py:L1073)
- is_code() (scripts/sdlc/knowledge.py:L572)
- Graphify tags code, document and rationale nodes; only code communities become… (scripts/sdlc/knowledge.py:L573)
- god_nodes() (scripts/sdlc/knowledge.py:L608)
- The most connected code nodes by degree, from the graph already in memory (what… (scripts/sdlc/knowledge.py:L609)
- concept() (scripts/sdlc/knowledge.py:L619)
- section() (scripts/sdlc/knowledge.py:L632)
- module_concepts() (scripts/sdlc/knowledge.py:L642)
- review_counts() (scripts/sdlc/knowledge.py:L673)
- feature_concepts() (scripts/sdlc/knowledge.py:L693)
- hub_concepts() (scripts/sdlc/knowledge.py:L721)
- first_sentence() (scripts/sdlc/knowledge.py:L749)
- lesson_concepts() (scripts/sdlc/knowledge.py:L753)
- band_concepts() (scripts/sdlc/knowledge.py:L782)

# Depends on
- [artifacts.py](/modules/artifacts-py.md)
- [deploy.py](/modules/deploy-py.md)
- [maintain.py](/modules/maintain-py.md)
- [project.py](/modules/project-py.md)
- [refresh](/modules/refresh.md)
- [testing.py](/modules/testing-py.md)

# Inferred
- no INFERRED edges; treat any that appear as hints

# Features
- [Graphify and OKF knowledge base integration](/features/graphify-and-okf-knowledge-base-integration.md)
