---
type: Module
title: build
description: "Graphify community 30: plugin/scripts/sdlc/packs.py, sdlc/graph-selected-repomix-context-packs/spec.md"
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
- build() (plugin/scripts/sdlc/packs.py:L230)
- Select, guard and pack the files a stage's agents need; see the module… (plugin/scripts/sdlc/packs.py:L231)
- write_pack() (plugin/scripts/sdlc/packs.py:L267)
- Walk the ladder into a temp file, then write the manifest and move the pack… (plugin/scripts/sdlc/packs.py:L268)
- verdict_of() (plugin/scripts/sdlc/packs.py:L301)
- prune() (plugin/scripts/sdlc/packs.py:L337)
- graph-selected-repomix-context-packs/spec.md (sdlc/graph-selected-repomix-context-packs/spec.md:L1)
- Spec: graph-selected repomix context packs (sdlc/graph-selected-repomix-context-packs/spec.md:L1)
- Concerns (sdlc/graph-selected-repomix-context-packs/spec.md:L186)
- Open questions (sdlc/graph-selected-repomix-context-packs/spec.md:L254)

# Depends on
- [check](/modules/check.md)
- [config](/modules/config.md)
- [conftest.py](/modules/conftest-py.md)
- [fail](/modules/fail.md)
- [fresh_graph](/modules/fresh-graph.md)
- [git](/modules/git.md)
- [packs.py](/modules/packs-py.md)
- [Path](/modules/path.md)
- [project.py](/modules/project-py.md)
- [refresh](/modules/refresh.md)
- [require](/modules/require.md)
- [review](/modules/review.md)
- [run_repomix](/modules/run-repomix.md)
- [test_plan_design.py](/modules/test-plan-design-py.md)

# Inferred
- [conftest.py](/modules/conftest-py.md)

# Features
- [graph-selected repomix context packs](/features/graph-selected-repomix-context-packs.md)
