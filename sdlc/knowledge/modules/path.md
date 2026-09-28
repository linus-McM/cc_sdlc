---
type: Module
title: Path
description: "Graphify community 13: plugin/scripts/sdlc/knowledge.py"
resource: plugin/scripts/sdlc
tags: [module, graphify]
status: draft
generated: { by: sdlc/0.8.1, at: "2026-09-28T22:57:53Z" }
stale_after: "2026-10-12T22:57:53Z"
source_commit: 0754d821fc594b90c529849cddaca10dc6109921
sources:
  - { id: knowledge, resource: plugin/scripts/sdlc/knowledge.py, last_modified: "2026-09-29T08:42:51+10:00", digest: d350848efe5d7fe2 }
---

# Files
- `plugin/scripts/sdlc/knowledge.py`

# Symbols
- concept_files() (plugin/scripts/sdlc/knowledge.py:L1020)
- check() (plugin/scripts/sdlc/knowledge.py:L1033)
- Three separate lists: official OKF v0.2 conformance (the only one that fails),… (plugin/scripts/sdlc/knowledge.py:L1034)
- bundle_dir() (plugin/scripts/sdlc/knowledge.py:L188)
- graph_path() (plugin/scripts/sdlc/knowledge.py:L192)
- state_path() (plugin/scripts/sdlc/knowledge.py:L200)
- read_state() (plugin/scripts/sdlc/knowledge.py:L204)
- `.state.json`, or `{"_error": reason}` when it exists but cannot be read (a… (plugin/scripts/sdlc/knowledge.py:L205)
- write_state() (plugin/scripts/sdlc/knowledge.py:L212)
- build_graph() (plugin/scripts/sdlc/knowledge.py:L364)
- bundle_present() (plugin/scripts/sdlc/knowledge.py:L368)
- A bundle counts only when it was built from the graph that exists now (an… (plugin/scripts/sdlc/knowledge.py:L369)
- graph_commit() (plugin/scripts/sdlc/knowledge.py:L453)
- artifacts_agree() (plugin/scripts/sdlc/knowledge.py:L473)
- verified_events() (plugin/scripts/sdlc/knowledge.py:L479)
- `verified` as a list: the spec lets a single event be written as a bare mapping. (plugin/scripts/sdlc/knowledge.py:L480)
- staleness() (plugin/scripts/sdlc/knowledge.py:L497)
- The cheap part of status: how far each index is behind HEAD and why a clean… (plugin/scripts/sdlc/knowledge.py:L498)
- bundle_counts() (plugin/scripts/sdlc/knowledge.py:L522)
- status() (plugin/scripts/sdlc/knowledge.py:L534)
- load_graph() (plugin/scripts/sdlc/knowledge.py:L569)
- community_labels() (plugin/scripts/sdlc/knowledge.py:L580)

# Depends on
- [bootstrap](/modules/bootstrap.md)
- [cfg](/modules/cfg.md)
- [docs.py](/modules/docs-py.md)
- [knowledge.py](/modules/knowledge-py.md)
- [Order of work](/modules/order-of-work-44.md)
- [packs.py](/modules/packs-py.md)
- [project.py](/modules/project-py.md)
- [read_json](/modules/read-json.md)
- [refresh](/modules/refresh.md)

# Inferred
- [Blocked](/modules/blocked.md)

# Features
- [graph-selected repomix context packs](/features/graph-selected-repomix-context-packs.md)
