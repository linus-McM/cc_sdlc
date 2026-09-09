---
type: Module
title: knowledge.py
description: "Graphify community 0: scripts/sdlc/artifacts.py, scripts/sdlc/knowledge.py"
resource: scripts/sdlc
tags: [module, graphify]
status: draft
generated: { by: sdlc/0.2.1, at: "2026-09-09T02:02:49Z" }
stale_after: "2026-09-23T02:02:49Z"
source_commit: f15b143d1ce08297fc13142247be8dc7f63d478f
sources:
  - { id: artifacts, resource: scripts/sdlc/artifacts.py, last_modified: "2026-09-09T08:32:17+10:00", digest: 3e063b545e7dd897 }
  - { id: knowledge, resource: scripts/sdlc/knowledge.py, last_modified: "2026-09-09T10:28:52+10:00", digest: 8da5a1d01eeb439c }
---

# Files
- `scripts/sdlc/artifacts.py`
- `scripts/sdlc/knowledge.py`

# Symbols
- slugify() (scripts/sdlc/artifacts.py:L30)
- knowledge.py (scripts/sdlc/knowledge.py:L1)
- Knowledge layer: Graphify graph (graphify-out/) plus an OKF v0.2 bundle… (scripts/sdlc/knowledge.py:L1)
- as_actor() (scripts/sdlc/knowledge.py:L1072)
- OKF actor convention: human:<id>, process:<id> or <producer>/<version>; a bare… (scripts/sdlc/knowledge.py:L1073)
- scalar() (scripts/sdlc/knowledge.py:L43)
- flow() (scripts/sdlc/knowledge.py:L53)
- is_code() (scripts/sdlc/knowledge.py:L572)
- Graphify tags code, document and rationale nodes; only code communities become… (scripts/sdlc/knowledge.py:L573)
- communities() (scripts/sdlc/knowledge.py:L588)
- Graphify code communities big enough for a Module concept, with a stable slug… (scripts/sdlc/knowledge.py:L589)
- god_nodes() (scripts/sdlc/knowledge.py:L608)
- The most connected code nodes by degree, from the graph already in memory (what… (scripts/sdlc/knowledge.py:L609)
- dump_frontmatter() (scripts/sdlc/knowledge.py:L61)
- concept() (scripts/sdlc/knowledge.py:L619)
- link() (scripts/sdlc/knowledge.py:L628)
- section() (scripts/sdlc/knowledge.py:L632)
- head_first() (scripts/sdlc/knowledge.py:L636)
- `front` with the recommended keys first, then `overrides` in order, then… (scripts/sdlc/knowledge.py:L637)
- module_concepts() (scripts/sdlc/knowledge.py:L642)
- review_counts() (scripts/sdlc/knowledge.py:L673)
- feature_status() (scripts/sdlc/knowledge.py:L681)
- feature_concepts() (scripts/sdlc/knowledge.py:L693)
- hub_concepts() (scripts/sdlc/knowledge.py:L721)
- first_sentence() (scripts/sdlc/knowledge.py:L749)
- lesson_concepts() (scripts/sdlc/knowledge.py:L753)
- band_concepts() (scripts/sdlc/knowledge.py:L782)
- render_concept() (scripts/sdlc/knowledge.py:L853)
- Frontmatter plus body; `reset` (a source changed) drops the concept back to… (scripts/sdlc/knowledge.py:L854)
- reconcile() (scripts/sdlc/knowledge.py:L902)
- Concept files nothing generated any more: tombstone when every source is… (scripts/sdlc/knowledge.py:L903)

# Depends on
- [artifacts.py](/modules/artifacts-py.md)
- [bump_version.py](/modules/bump-version-py.md)
- [cfg](/modules/cfg.md)
- [deploy.py](/modules/deploy-py.md)
- [Digests](/modules/digests.md)
- [fail](/modules/fail.md)
- [hooks.py](/modules/hooks-py.md)
- [install_hook](/modules/install-hook.md)
- [maintain.py](/modules/maintain-py.md)
- [Path](/modules/path.md)
- [project.py](/modules/project-py.md)
- [ran](/modules/ran.md)
- [refresh](/modules/refresh.md)
- [stages.py](/modules/stages-py.md)
- [testing.py](/modules/testing-py.md)

# Inferred
- [install_hook](/modules/install-hook.md)
- [Path](/modules/path.md)
- [ran](/modules/ran.md)
- [refresh](/modules/refresh.md)

# Features
- [Archify stage documentation](/features/archify-stage-documentation.md)
- [Graphify and OKF knowledge base integration](/features/graphify-and-okf-knowledge-base-integration.md)
