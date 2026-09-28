---
type: Module
title: fail
description: "Graphify community 22: plugin/scripts/sdlc/docs.py, plugin/scripts/sdlc/packs.py, plugin/scripts/sdlc/project.py, plugin/scripts/sdlc/stages.py"
resource: plugin/scripts/sdlc
tags: [module, graphify]
status: draft
generated: { by: sdlc/0.8.1, at: "2026-09-28T22:57:53Z" }
stale_after: "2026-10-12T22:57:53Z"
source_commit: 0754d821fc594b90c529849cddaca10dc6109921
sources:
  - { id: docs, resource: plugin/scripts/sdlc/docs.py, last_modified: "2026-09-09T15:02:31+10:00", digest: 10270177466cde0a }
  - { id: packs, resource: plugin/scripts/sdlc/packs.py, last_modified: "2026-09-26T16:35:55+10:00", digest: 976267a001f822d8 }
  - { id: project, resource: plugin/scripts/sdlc/project.py, last_modified: "2026-09-29T08:42:51+10:00", digest: f89b1e9a47bc69d8 }
  - { id: stages, resource: plugin/scripts/sdlc/stages.py, last_modified: "2026-09-26T16:35:55+10:00", digest: 3de65600923a55b5 }
---

# Files
- `plugin/scripts/sdlc/docs.py`
- `plugin/scripts/sdlc/packs.py`
- `plugin/scripts/sdlc/project.py`
- `plugin/scripts/sdlc/stages.py`

# Symbols
- target() (plugin/scripts/sdlc/docs.py:L140)
- The directory that owns the stage document: the feature, or `sdlc/` for the… (plugin/scripts/sdlc/docs.py:L141)
- exemptions() (plugin/scripts/sdlc/packs.py:L207)
- Paths whose change never makes the graph stale: [knowledge] ignore, the SDLC… (plugin/scripts/sdlc/packs.py:L208)
- fresh_graph() (plugin/scripts/sdlc/packs.py:L216)
- The graph, provided it names a commit and no non-exempt file changed since;… (plugin/scripts/sdlc/packs.py:L217)
- home() (plugin/scripts/sdlc/project.py:L174)
- features() (plugin/scripts/sdlc/project.py:L181)
- Every feature directory (one holding an intent.md), sorted by name. (plugin/scripts/sdlc/project.py:L182)
- feature() (plugin/scripts/sdlc/project.py:L187)
- The named feature directory, or the most recently modified one; Blocked when… (plugin/scripts/sdlc/project.py:L188)
- fail() (plugin/scripts/sdlc/project.py:L94)
- status() (plugin/scripts/sdlc/stages.py:L107)
- accepted() (plugin/scripts/sdlc/stages.py:L28)
- gated() (plugin/scripts/sdlc/stages.py:L33)
- The feature directory, provided `artifact` (if any) has been accepted by a… (plugin/scripts/sdlc/stages.py:L34)
- create_feature() (plugin/scripts/sdlc/stages.py:L43)
- check() (plugin/scripts/sdlc/stages.py:L76)

# Depends on
- [Blocked](/modules/blocked.md)
- [check](/modules/check.md)
- [Components](/modules/components.md)
- [git](/modules/git.md)
- [Path](/modules/path.md)
- [pathlib](/modules/pathlib.md)
- [read_json](/modules/read-json.md)
- [select](/modules/select.md)

# Inferred
- no INFERRED edges; treat any that appear as hints

# Features
- [graph-selected repomix context packs](/features/graph-selected-repomix-context-packs.md)
