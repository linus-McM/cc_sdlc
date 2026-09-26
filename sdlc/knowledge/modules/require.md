---
type: Module
title: require
description: "Graphify community 11: plugin/scripts/sdlc/packs.py, sdlc/graph-selected-repomix-context-packs/spec.md"
resource: ""
tags: [module, graphify]
status: draft
generated: { by: sdlc/0.5.0, at: "2026-09-26T06:33:18Z" }
stale_after: "2026-10-10T06:33:18Z"
source_commit: 5c45a37edd0dc635576e390a1174bea9fad6d10b
sources:
  - { id: packs, resource: plugin/scripts/sdlc/packs.py, last_modified: "2026-09-26T16:31:53+10:00", digest: 976267a001f822d8 }
  - { id: spec, resource: sdlc/graph-selected-repomix-context-packs/spec.md, last_modified: "2026-09-26T09:27:53+10:00", digest: 39b0915a5020a08c }
---

# Files
- `plugin/scripts/sdlc/packs.py`
- `sdlc/graph-selected-repomix-context-packs/spec.md`

# Symbols
- expand() (plugin/scripts/sdlc/packs.py:L139)
- {path: seed|caller|callee|community}: files `hops` `calls` links from a seed,… (plugin/scripts/sdlc/packs.py:L140)
- packs_dir() (plugin/scripts/sdlc/packs.py:L324)
- store() (plugin/scripts/sdlc/packs.py:L328)
- packs_dir, created with a `*` .gitignore on first use so nothing in it is ever… (plugin/scripts/sdlc/packs.py:L329)
- latest() (plugin/scripts/sdlc/packs.py:L415)
- The newest manifest for a slug and stage whose pack file still exists. (plugin/scripts/sdlc/packs.py:L416)
- require() (plugin/scripts/sdlc/packs.py:L422)
- The gate for a stage in GATED: ok (visibly skipped) when packs are off;… (plugin/scripts/sdlc/packs.py:L423)
- Design (sdlc/graph-selected-repomix-context-packs/spec.md:L121)

# Depends on
- [check](/modules/check.md)
- [fail](/modules/fail.md)
- [git](/modules/git.md)
- [packs.py](/modules/packs-py.md)
- [Path](/modules/path.md)
- [Path](/modules/path-13.md)

# Inferred
- [build](/modules/build.md)
- [conftest.py](/modules/conftest-py.md)
- [docs.py](/modules/docs-py.md)
- [packs.py](/modules/packs-py.md)
- [Path](/modules/path.md)
- [Path](/modules/path-13.md)
- [review](/modules/review.md)

# Features
- [graph-selected repomix context packs](/features/graph-selected-repomix-context-packs.md)
