---
type: Module
title: propose
description: "Graphify community 34: plugin/commands/deploy.md, plugin/commands/maintain.md, plugin/scripts/sdlc/artifacts.py, plugin/scripts/sdlc/cli.py, plugin/scripts/sdlc/maintain.py"
resource: plugin
tags: [module, graphify]
status: draft
generated: { by: sdlc/0.5.0, at: "2026-09-26T06:33:18Z" }
stale_after: "2026-10-10T06:33:18Z"
source_commit: 5c45a37edd0dc635576e390a1174bea9fad6d10b
sources:
  - { id: deploy, resource: plugin/commands/deploy.md, last_modified: "2026-09-24T11:36:09+10:00", digest: d0459d52d6b53867 }
  - { id: maintain, resource: plugin/commands/maintain.md, last_modified: "2026-09-26T15:57:51+10:00", digest: 4fd77c3502ccf132 }
  - { id: artifacts, resource: plugin/scripts/sdlc/artifacts.py, last_modified: "2026-09-09T15:02:31+10:00", digest: 3e063b545e7dd897 }
  - { id: cli, resource: plugin/scripts/sdlc/cli.py, last_modified: "2026-09-26T16:06:32+10:00", digest: 87213d99f94df3bf }
  - { id: maintain, resource: plugin/scripts/sdlc/maintain.py, last_modified: "2026-09-09T15:02:31+10:00", digest: 3aba25cd9e242550 }
---

# Files
- `plugin/commands/deploy.md`
- `plugin/commands/maintain.md`
- `plugin/scripts/sdlc/artifacts.py`
- `plugin/scripts/sdlc/cli.py`
- `plugin/scripts/sdlc/maintain.py`

# Symbols
- docs  (the stage document; required before `deploy record`) (plugin/commands/deploy.md:L29)
- maintain.md (plugin/commands/maintain.md:L1)
- watch (plugin/commands/maintain.md:L16)
- docs  (the bands document; never gates a watch) (plugin/commands/maintain.md:L22)
- propose <metric> (plugin/commands/maintain.md:L25)
- lesson "<text>" (plugin/commands/maintain.md:L28)
- set_section() (plugin/scripts/sdlc/artifacts.py:L44)
- set_meta() (plugin/scripts/sdlc/artifacts.py:L54)
- lifecycle() (plugin/scripts/sdlc/cli.py:L18)
- new/check/accept for an artifact stage; only `plan new` takes the positional… (plugin/scripts/sdlc/cli.py:L19)
- propose() (plugin/scripts/sdlc/maintain.py:L99)

# Depends on
- [fail](/modules/fail.md)
- [project.py](/modules/project-py.md)
- [watch](/modules/watch.md)

# Inferred
- [Order of work](/modules/order-of-work-8.md)

# Features
- [graph-selected repomix context packs](/features/graph-selected-repomix-context-packs.md)
