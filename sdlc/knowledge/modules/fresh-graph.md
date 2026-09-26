---
type: Module
title: fresh_graph
description: "Graphify community 90: plugin/scripts/sdlc/build.py, plugin/scripts/sdlc/packs.py"
resource: plugin/scripts/sdlc
tags: [module, graphify]
status: draft
generated: { by: sdlc/0.5.0, at: "2026-09-26T06:33:18Z" }
stale_after: "2026-10-10T06:33:18Z"
source_commit: 5c45a37edd0dc635576e390a1174bea9fad6d10b
sources:
  - { id: build, resource: plugin/scripts/sdlc/build.py, last_modified: "2026-09-09T15:02:31+10:00", digest: 3bd6dd8d38860ab6 }
  - { id: packs, resource: plugin/scripts/sdlc/packs.py, last_modified: "2026-09-26T16:31:53+10:00", digest: 976267a001f822d8 }
---

# Files
- `plugin/scripts/sdlc/build.py`
- `plugin/scripts/sdlc/packs.py`

# Symbols
- is_sdlc_owned() (plugin/scripts/sdlc/build.py:L62)
- exemptions() (plugin/scripts/sdlc/packs.py:L207)
- Paths whose change never makes the graph stale: [knowledge] ignore, the SDLC… (plugin/scripts/sdlc/packs.py:L208)
- exempt() (plugin/scripts/sdlc/packs.py:L212)
- fresh_graph() (plugin/scripts/sdlc/packs.py:L216)
- The graph, provided it names a commit and no non-exempt file changed since;… (plugin/scripts/sdlc/packs.py:L217)
- changed_since() (plugin/scripts/sdlc/packs.py:L56)
- Committed text files changed in `spec` (a git range); deleted, binary (numstat… (plugin/scripts/sdlc/packs.py:L57)
- maintain_seeds() (plugin/scripts/sdlc/packs.py:L68)

# Depends on
- [check](/modules/check.md)
- [docs.py](/modules/docs-py.md)
- [fail](/modules/fail.md)
- [git](/modules/git.md)
- [Path](/modules/path-13.md)
- [project.py](/modules/project-py.md)

# Inferred
- no INFERRED edges; treat any that appear as hints

# Features
- [graph-selected repomix context packs](/features/graph-selected-repomix-context-packs.md)
