---
type: Module
title: config
description: "Graphify community 59: CLAUDE.md, plugin/scripts/sdlc/deploy.py, plugin/scripts/sdlc/hooks.py, plugin/scripts/sdlc/maintain.py, plugin/scripts/sdlc/project.py, sdlc/release-hook-hardening/spec.md"
resource: ""
tags: [module, graphify]
status: draft
generated: { by: sdlc/0.5.0, at: "2026-09-26T06:33:18Z" }
stale_after: "2026-10-10T06:33:18Z"
source_commit: 5c45a37edd0dc635576e390a1174bea9fad6d10b
sources:
  - { id: CLAUDE, resource: CLAUDE.md, last_modified: "2026-09-26T15:59:19+10:00", digest: 9ef0106f03b16707 }
  - { id: deploy, resource: plugin/scripts/sdlc/deploy.py, last_modified: "2026-09-26T16:06:32+10:00", digest: d2d3493a1ed08434 }
  - { id: hooks, resource: plugin/scripts/sdlc/hooks.py, last_modified: "2026-09-19T13:08:30+10:00", digest: 40334c1872956197 }
  - { id: maintain, resource: plugin/scripts/sdlc/maintain.py, last_modified: "2026-09-09T15:02:31+10:00", digest: 3aba25cd9e242550 }
  - { id: project, resource: plugin/scripts/sdlc/project.py, last_modified: "2026-09-26T16:06:32+10:00", digest: 26698ea0d06e1efe }
  - { id: spec, resource: sdlc/release-hook-hardening/spec.md, last_modified: "2026-09-09T15:03:27+10:00", digest: ceec7eaa899c3151 }
---

# Files
- `CLAUDE.md`
- `plugin/scripts/sdlc/deploy.py`
- `plugin/scripts/sdlc/hooks.py`
- `plugin/scripts/sdlc/maintain.py`
- `plugin/scripts/sdlc/project.py`
- `sdlc/release-hook-hardening/spec.md`

# Symbols
- Conventions (CLAUDE.md:L18)
- gated() (plugin/scripts/sdlc/deploy.py:L50)
- Environments at the `gate` tier in a `[deploy]` config table. (plugin/scripts/sdlc/deploy.py:L51)
- release_hit() (plugin/scripts/sdlc/hooks.py:L102)
- What in `cmd` looks like a release to a gated environment, or None. Always: a… (plugin/scripts/sdlc/hooks.py:L103)
- pre_bash() (plugin/scripts/sdlc/hooks.py:L121)
- ingest() (plugin/scripts/sdlc/maintain.py:L113)
- merge() (plugin/scripts/sdlc/project.py:L144)
- config() (plugin/scripts/sdlc/project.py:L154)
- DEFAULT_CONFIG deep-merged with .sdlc.toml, so every key is always present;… (plugin/scripts/sdlc/project.py:L155)
- Design (sdlc/release-hook-hardening/spec.md:L15)

# Depends on
- [build.py](/modules/build-py.md)
- [hooks.py](/modules/hooks-py.md)
- [project.py](/modules/project-py.md)
- [test_hooks.py](/modules/test-hooks-py.md)

# Inferred
- [Blocked](/modules/blocked.md)
- [check](/modules/check.md)
- [test_hooks.py](/modules/test-hooks-py.md)

# Features
- [Archify stage documentation](/features/archify-stage-documentation.md)
- [graph-selected repomix context packs](/features/graph-selected-repomix-context-packs.md)
- [Graphify and OKF knowledge base integration](/features/graphify-and-okf-knowledge-base-integration.md)
