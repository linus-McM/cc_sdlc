---
type: Module
title: knowledge.py
description: "Graphify community 0: scripts/sdlc/artifacts.py, scripts/sdlc/knowledge.py"
resource: scripts/sdlc
tags: [module, graphify]
status: draft
generated: { by: sdlc/0.2.0, at: "2026-09-08T22:35:57Z" }
stale_after: "2026-09-22T22:35:57Z"
source_commit: c6f9a22e23b0bee7134aa1e1709c5feef8673f82
sources:
  - { id: artifacts, resource: scripts/sdlc/artifacts.py, last_modified: "2026-09-09T08:32:17+10:00", digest: 3e063b545e7dd897 }
  - { id: knowledge, resource: scripts/sdlc/knowledge.py, last_modified: "2026-09-09T08:35:54+10:00", digest: 5ed472fa5f0e7275 }
---

# Files
- `scripts/sdlc/artifacts.py`
- `scripts/sdlc/knowledge.py`

# Symbols
- slugify() (scripts/sdlc/artifacts.py:L30)
- knowledge.py (scripts/sdlc/knowledge.py:L1)
- Knowledge layer: Graphify graph (graphify-out/) plus an OKF v0.2 bundle… (scripts/sdlc/knowledge.py:L1)
- as_actor() (scripts/sdlc/knowledge.py:L1031)
- OKF actor convention: human:<id>, process:<id> or <producer>/<version>; a bare… (scripts/sdlc/knowledge.py:L1032)
- scalar() (scripts/sdlc/knowledge.py:L43)
- flow() (scripts/sdlc/knowledge.py:L53)
- is_code() (scripts/sdlc/knowledge.py:L540)
- Graphify tags code, document and rationale nodes; only code communities become… (scripts/sdlc/knowledge.py:L541)
- god_nodes() (scripts/sdlc/knowledge.py:L576)
- The most connected code nodes by degree, from the graph already in memory (what… (scripts/sdlc/knowledge.py:L577)
- concept() (scripts/sdlc/knowledge.py:L587)
- link() (scripts/sdlc/knowledge.py:L596)
- section() (scripts/sdlc/knowledge.py:L600)
- head_first() (scripts/sdlc/knowledge.py:L604)
- `front` with the recommended keys first, then `overrides` in order, then… (scripts/sdlc/knowledge.py:L605)
- dump_frontmatter() (scripts/sdlc/knowledge.py:L61)
- module_concepts() (scripts/sdlc/knowledge.py:L610)
- review_counts() (scripts/sdlc/knowledge.py:L641)
- feature_concepts() (scripts/sdlc/knowledge.py:L661)
- hub_concepts() (scripts/sdlc/knowledge.py:L689)
- first_sentence() (scripts/sdlc/knowledge.py:L717)
- lesson_concepts() (scripts/sdlc/knowledge.py:L721)
- band_concepts() (scripts/sdlc/knowledge.py:L750)
- render_concept() (scripts/sdlc/knowledge.py:L814)
- Frontmatter plus body; `reset` (a source changed) drops the concept back to… (scripts/sdlc/knowledge.py:L815)
- reconcile() (scripts/sdlc/knowledge.py:L863)
- Concept files nothing generated any more: tombstone when every source is… (scripts/sdlc/knowledge.py:L864)

# Depends on
- [artifacts.py](/modules/artifacts-py.md)
- [deploy.py](/modules/deploy-py.md)
- [Digests](/modules/digests.md)
- [fail](/modules/fail.md)
- [hooks.py](/modules/hooks-py.md)
- [maintain.py](/modules/maintain-py.md)
- [parse_frontmatter](/modules/parse-frontmatter.md)
- [Path](/modules/path.md)
- [post_commit_path](/modules/post-commit-path.md)
- [project.py](/modules/project-py.md)
- [ran](/modules/ran.md)
- [refresh](/modules/refresh.md)
- [render](/modules/render.md)
- [stages.py](/modules/stages-py.md)

# Inferred
- [Path](/modules/path.md)
- [post_commit_path](/modules/post-commit-path.md)
- [ran](/modules/ran.md)
- [refresh](/modules/refresh.md)
- [render](/modules/render.md)

# Features
- [Graphify and OKF knowledge base integration](/features/graphify-and-okf-knowledge-base-integration.md)
