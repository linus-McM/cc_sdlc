---
type: Module
title: Components
description: "Graphify community 15: plugin/scripts/sdlc/artifacts.py, plugin/scripts/sdlc/knowledge.py, sdlc/graphify-and-okf-knowledge-base-integration/spec.md"
resource: ""
tags: [module, graphify]
status: draft
generated: { by: sdlc/0.5.0, at: "2026-09-26T05:22:30Z" }
stale_after: "2026-10-10T05:22:30Z"
source_commit: c5f64f8d3b9b5e3268754f626b7f2e958fd6415e
sources:
  - { id: artifacts, resource: plugin/scripts/sdlc/artifacts.py, last_modified: "2026-09-09T15:02:31+10:00", digest: 3e063b545e7dd897 }
  - { id: knowledge, resource: plugin/scripts/sdlc/knowledge.py, last_modified: "2026-09-09T15:02:31+10:00", digest: 9f4a8d0ccc4c7375 }
  - { id: spec, resource: sdlc/graphify-and-okf-knowledge-base-integration/spec.md, last_modified: "2026-09-09T15:03:27+10:00", digest: 18ddccb80477e245 }
---

# Files
- `plugin/scripts/sdlc/artifacts.py`
- `plugin/scripts/sdlc/knowledge.py`
- `sdlc/graphify-and-okf-knowledge-base-integration/spec.md`

# Symbols
- slugify() (plugin/scripts/sdlc/artifacts.py:L30)
- as_actor() (plugin/scripts/sdlc/knowledge.py:L1060)
- OKF actor convention: human:<id>, process:<id> or <producer>/<version>; a bare… (plugin/scripts/sdlc/knowledge.py:L1061)
- is_code() (plugin/scripts/sdlc/knowledge.py:L559)
- Graphify tags code, document and rationale nodes; only code communities become… (plugin/scripts/sdlc/knowledge.py:L560)
- community_labels() (plugin/scripts/sdlc/knowledge.py:L566)
- communities() (plugin/scripts/sdlc/knowledge.py:L575)
- Graphify code communities big enough for a Module concept, with a stable slug… (plugin/scripts/sdlc/knowledge.py:L576)
- god_nodes() (plugin/scripts/sdlc/knowledge.py:L595)
- The most connected code nodes by degree, from the graph already in memory (what… (plugin/scripts/sdlc/knowledge.py:L596)
- concept() (plugin/scripts/sdlc/knowledge.py:L606)
- section() (plugin/scripts/sdlc/knowledge.py:L619)
- module_concepts() (plugin/scripts/sdlc/knowledge.py:L629)
- hub_concepts() (plugin/scripts/sdlc/knowledge.py:L709)
- first_sentence() (plugin/scripts/sdlc/knowledge.py:L737)
- lesson_concepts() (plugin/scripts/sdlc/knowledge.py:L741)
- band_concepts() (plugin/scripts/sdlc/knowledge.py:L770)
- Components (sdlc/graphify-and-okf-knowledge-base-integration/spec.md:L138)

# Depends on
- [bootstrap](/modules/bootstrap.md)
- [docs.py](/modules/docs-py.md)
- [fail](/modules/fail.md)
- [fill](/modules/fill.md)

# Inferred
- [Blocked](/modules/blocked.md)
- [bootstrap](/modules/bootstrap.md)
- [fail](/modules/fail.md)
- [fill](/modules/fill.md)
- [hooks.py](/modules/hooks-py.md)
- [Order of work](/modules/order-of-work.md)
- [parse_frontmatter](/modules/parse-frontmatter.md)
- [Path](/modules/path-13.md)
- [post_edit](/modules/post-edit.md)
- [reconcile](/modules/reconcile.md)
- [refresh](/modules/refresh.md)
- [rehearse](/modules/rehearse.md)
- [stages.py](/modules/stages-py.md)

# Features
- [graph-selected repomix context packs](/features/graph-selected-repomix-context-packs.md)
