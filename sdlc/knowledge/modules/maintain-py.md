---
type: Module
title: maintain.py
description: "Graphify community 34: plugin/commands/maintain.md, plugin/scripts/sdlc/artifacts.py, plugin/scripts/sdlc/cli.py, plugin/scripts/sdlc/maintain.py, plugin/scripts/sdlc/project.py"
resource: plugin
tags: [module, graphify]
status: draft
generated: { by: sdlc/0.8.1, at: "2026-09-28T22:57:53Z" }
stale_after: "2026-10-12T22:57:53Z"
source_commit: 0754d821fc594b90c529849cddaca10dc6109921
sources:
  - { id: maintain, resource: plugin/commands/maintain.md, last_modified: "2026-09-26T16:35:55+10:00", digest: 4fd77c3502ccf132 }
  - { id: artifacts, resource: plugin/scripts/sdlc/artifacts.py, last_modified: "2026-09-09T15:02:31+10:00", digest: 3e063b545e7dd897 }
  - { id: cli, resource: plugin/scripts/sdlc/cli.py, last_modified: "2026-09-29T08:42:51+10:00", digest: 08531c81958e1bbe }
  - { id: maintain, resource: plugin/scripts/sdlc/maintain.py, last_modified: "2026-09-09T15:02:31+10:00", digest: 3aba25cd9e242550 }
  - { id: project, resource: plugin/scripts/sdlc/project.py, last_modified: "2026-09-29T08:42:51+10:00", digest: f89b1e9a47bc69d8 }
---

# Files
- `plugin/commands/maintain.md`
- `plugin/scripts/sdlc/artifacts.py`
- `plugin/scripts/sdlc/cli.py`
- `plugin/scripts/sdlc/maintain.py`
- `plugin/scripts/sdlc/project.py`

# Symbols
- maintain.md (plugin/commands/maintain.md:L1)
- watch (plugin/commands/maintain.md:L16)
- docs  (the bands document; never gates a watch) (plugin/commands/maintain.md:L22)
- propose <metric> (plugin/commands/maintain.md:L25)
- lesson "<text>" (plugin/commands/maintain.md:L28)
- set_section() (plugin/scripts/sdlc/artifacts.py:L44)
- set_meta() (plugin/scripts/sdlc/artifacts.py:L54)
- lifecycle() (plugin/scripts/sdlc/cli.py:L18)
- new/check/accept for an artifact stage; only `plan new` takes the positional… (plugin/scripts/sdlc/cli.py:L19)
- maintain.py (plugin/scripts/sdlc/maintain.py:L1)
- Maintain-stage mechanics: deterministic control bands that close the loop back… (plugin/scripts/sdlc/maintain.py:L1)
- ingest() (plugin/scripts/sdlc/maintain.py:L113)
- lesson() (plugin/scripts/sdlc/maintain.py:L121)
- readings() (plugin/scripts/sdlc/maintain.py:L64)
- propose() (plugin/scripts/sdlc/maintain.py:L99)
- today() (plugin/scripts/sdlc/project.py:L236)
- read_jsonl() (plugin/scripts/sdlc/project.py:L240)
- append_jsonl() (plugin/scripts/sdlc/project.py:L244)

# Depends on
- [docs.py](/modules/docs-py.md)
- [fail](/modules/fail.md)
- [pathlib](/modules/pathlib.md)
- [project.py](/modules/project-py.md)
- [watch](/modules/watch.md)

# Inferred
- [accept](/modules/accept.md)
- [Order of work](/modules/order-of-work-8.md)

# Features
- [graph-selected repomix context packs](/features/graph-selected-repomix-context-packs.md)
