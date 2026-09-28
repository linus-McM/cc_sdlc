---
type: Module
title: Components
description: "Graphify community 36: plugin/scripts/sdlc/artifacts.py, plugin/scripts/sdlc/knowledge.py, sdlc/graphify-and-okf-knowledge-base-integration/spec.md"
resource: ""
tags: [module, graphify]
status: draft
generated: { by: sdlc/0.8.1, at: "2026-09-28T22:57:53Z" }
stale_after: "2026-10-12T22:57:53Z"
source_commit: 0754d821fc594b90c529849cddaca10dc6109921
sources:
  - { id: artifacts, resource: plugin/scripts/sdlc/artifacts.py, last_modified: "2026-09-09T15:02:31+10:00", digest: 3e063b545e7dd897 }
  - { id: knowledge, resource: plugin/scripts/sdlc/knowledge.py, last_modified: "2026-09-29T08:42:51+10:00", digest: d350848efe5d7fe2 }
  - { id: spec, resource: sdlc/graphify-and-okf-knowledge-base-integration/spec.md, last_modified: "2026-09-09T15:03:27+10:00", digest: 18ddccb80477e245 }
---

# Files
- `plugin/scripts/sdlc/artifacts.py`
- `plugin/scripts/sdlc/knowledge.py`
- `sdlc/graphify-and-okf-knowledge-base-integration/spec.md`

# Symbols
- slugify() (plugin/scripts/sdlc/artifacts.py:L30)
- status() (plugin/scripts/sdlc/artifacts.py:L58)
- as_actor() (plugin/scripts/sdlc/knowledge.py:L1075)
- OKF actor convention: human:<id>, process:<id> or <producer>/<version>; a bare… (plugin/scripts/sdlc/knowledge.py:L1076)
- is_code() (plugin/scripts/sdlc/knowledge.py:L573)
- Graphify tags code, document and rationale nodes; only code communities become… (plugin/scripts/sdlc/knowledge.py:L574)
- communities() (plugin/scripts/sdlc/knowledge.py:L589)
- Graphify code communities big enough for a Module concept, with a stable slug… (plugin/scripts/sdlc/knowledge.py:L590)
- god_nodes() (plugin/scripts/sdlc/knowledge.py:L609)
- The most connected code nodes by degree, from the graph already in memory (what… (plugin/scripts/sdlc/knowledge.py:L610)
- concept() (plugin/scripts/sdlc/knowledge.py:L620)
- section() (plugin/scripts/sdlc/knowledge.py:L633)
- module_concepts() (plugin/scripts/sdlc/knowledge.py:L643)
- review_counts() (plugin/scripts/sdlc/knowledge.py:L674)
- feature_status() (plugin/scripts/sdlc/knowledge.py:L682)
- feature_concepts() (plugin/scripts/sdlc/knowledge.py:L694)
- hub_concepts() (plugin/scripts/sdlc/knowledge.py:L723)
- first_sentence() (plugin/scripts/sdlc/knowledge.py:L751)
- lesson_concepts() (plugin/scripts/sdlc/knowledge.py:L755)
- band_concepts() (plugin/scripts/sdlc/knowledge.py:L784)
- Components (sdlc/graphify-and-okf-knowledge-base-integration/spec.md:L138)

# Depends on
- [check](/modules/check.md)
- [fail](/modules/fail.md)
- [git](/modules/git.md)
- [maintain.py](/modules/maintain-py.md)
- [Order of work](/modules/order-of-work.md)
- [Path](/modules/path.md)
- [pathlib](/modules/pathlib.md)
- [read_json](/modules/read-json.md)
- [refresh](/modules/refresh.md)
- [watch](/modules/watch.md)

# Inferred
- [accept](/modules/accept.md)
- [Blocked](/modules/blocked.md)
- [bootstrap](/modules/bootstrap.md)
- [cfg](/modules/cfg.md)
- [conftest.py](/modules/conftest-py.md)
- [fail](/modules/fail.md)
- [hooks.py](/modules/hooks-py.md)
- [knowledge.py](/modules/knowledge-py.md)
- [maintain.py](/modules/maintain-py.md)
- [parse_frontmatter](/modules/parse-frontmatter.md)
- [Path](/modules/path.md)
- [read_json](/modules/read-json.md)
- [refresh](/modules/refresh.md)
- [watch](/modules/watch.md)

# Features
- [graph-selected repomix context packs](/features/graph-selected-repomix-context-packs.md)
