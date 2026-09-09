---
type: Module
title: knowledge.py
description: "Graphify community 0: scripts/sdlc/artifacts.py, scripts/sdlc/knowledge.py"
resource: scripts/sdlc
tags: [module, graphify]
status: draft
generated: { by: sdlc/0.2.1, at: "2026-09-09T02:17:09Z" }
stale_after: "2026-09-23T02:17:09Z"
source_commit: 5f6707036a44f201af1092fdfdde11b3cdba2f6f
sources:
  - { id: artifacts, resource: scripts/sdlc/artifacts.py, last_modified: "2026-09-09T08:32:17+10:00", digest: 3e063b545e7dd897 }
  - { id: knowledge, resource: scripts/sdlc/knowledge.py, last_modified: "2026-09-09T12:08:42+10:00", digest: 9f7d0b83d716857f }
---

# Files
- `scripts/sdlc/artifacts.py`
- `scripts/sdlc/knowledge.py`

# Symbols
- slugify() (scripts/sdlc/artifacts.py:L30)
- knowledge.py (scripts/sdlc/knowledge.py:L1)
- Knowledge layer: Graphify graph (graphify-out/) plus an OKF v0.2 bundle… (scripts/sdlc/knowledge.py:L1)
- as_actor() (scripts/sdlc/knowledge.py:L1083)
- OKF actor convention: human:<id>, process:<id> or <producer>/<version>; a bare… (scripts/sdlc/knowledge.py:L1084)
- scalar() (scripts/sdlc/knowledge.py:L43)
- flow() (scripts/sdlc/knowledge.py:L53)
- is_code() (scripts/sdlc/knowledge.py:L582)
- Graphify tags code, document and rationale nodes; only code communities become… (scripts/sdlc/knowledge.py:L583)
- communities() (scripts/sdlc/knowledge.py:L598)
- Graphify code communities big enough for a Module concept, with a stable slug… (scripts/sdlc/knowledge.py:L599)
- dump_frontmatter() (scripts/sdlc/knowledge.py:L61)
- god_nodes() (scripts/sdlc/knowledge.py:L618)
- The most connected code nodes by degree, from the graph already in memory (what… (scripts/sdlc/knowledge.py:L619)
- concept() (scripts/sdlc/knowledge.py:L629)
- link() (scripts/sdlc/knowledge.py:L638)
- section() (scripts/sdlc/knowledge.py:L642)
- head_first() (scripts/sdlc/knowledge.py:L646)
- `front` with the recommended keys first, then `overrides` in order, then… (scripts/sdlc/knowledge.py:L647)
- module_concepts() (scripts/sdlc/knowledge.py:L652)
- review_counts() (scripts/sdlc/knowledge.py:L683)
- feature_status() (scripts/sdlc/knowledge.py:L691)
- feature_concepts() (scripts/sdlc/knowledge.py:L703)
- hub_concepts() (scripts/sdlc/knowledge.py:L732)
- first_sentence() (scripts/sdlc/knowledge.py:L760)
- lesson_concepts() (scripts/sdlc/knowledge.py:L764)
- band_concepts() (scripts/sdlc/knowledge.py:L793)
- render_concept() (scripts/sdlc/knowledge.py:L864)
- Frontmatter plus body; `reset` (a source changed) drops the concept back to… (scripts/sdlc/knowledge.py:L865)
- reconcile() (scripts/sdlc/knowledge.py:L913)
- Concept files nothing generated any more: tombstone when every source is… (scripts/sdlc/knowledge.py:L914)

# Depends on
- [artifacts.py](/modules/artifacts-py.md)
- [build.py](/modules/build-py.md)
- [bump_version.py](/modules/bump-version-py.md)
- [cli.py](/modules/cli-py.md)
- [deploy.py](/modules/deploy-py.md)
- [Digests](/modules/digests.md)
- [docs.py](/modules/docs-py.md)
- [fail](/modules/fail.md)
- [hooks.py](/modules/hooks-py.md)
- [install_hook](/modules/install-hook.md)
- [maintain.py](/modules/maintain-py.md)
- [Path](/modules/path.md)
- [project.py](/modules/project-py.md)
- [ran](/modules/ran.md)
- [refresh](/modules/refresh.md)
- [stages.py](/modules/stages-py.md)
- [status](/modules/status.md)

# Inferred
- [install_hook](/modules/install-hook.md)
- [Path](/modules/path.md)
- [ran](/modules/ran.md)
- [refresh](/modules/refresh.md)

# Features
- [Archify stage documentation](/features/archify-stage-documentation.md)
- [Graphify and OKF knowledge base integration](/features/graphify-and-okf-knowledge-base-integration.md)
