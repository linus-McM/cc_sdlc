---
type: Module
title: config
description: "Graphify community 84: plugin/scripts/sdlc/deploy.py, plugin/scripts/sdlc/hooks.py, plugin/scripts/sdlc/project.py, sdlc/graph-selected-repomix-context-packs/intent.md, sdlc/release-hook-hardening/int"
resource: ""
tags: [module, graphify]
status: draft
generated: { by: sdlc/0.5.0, at: "2026-09-26T05:22:30Z" }
stale_after: "2026-10-10T05:22:30Z"
source_commit: c5f64f8d3b9b5e3268754f626b7f2e958fd6415e
sources:
  - { id: deploy, resource: plugin/scripts/sdlc/deploy.py, last_modified: "2026-09-24T11:36:09+10:00", digest: 99b508f60ff0691d }
  - { id: hooks, resource: plugin/scripts/sdlc/hooks.py, last_modified: "2026-09-19T13:08:30+10:00", digest: 40334c1872956197 }
  - { id: project, resource: plugin/scripts/sdlc/project.py, last_modified: "2026-09-24T11:36:09+10:00", digest: d1e5536892dbd875 }
  - { id: intent, resource: sdlc/graph-selected-repomix-context-packs/intent.md, last_modified: "2026-09-25T17:58:30+10:00", digest: 119529ab975a409b }
  - { id: intent, resource: sdlc/release-hook-hardening/intent.md, last_modified: "2026-09-09T15:03:27+10:00", digest: ed3ebb9b592952e4 }
  - { id: spec, resource: sdlc/release-hook-hardening/spec.md, last_modified: "2026-09-09T15:03:27+10:00", digest: ceec7eaa899c3151 }
---

# Files
- `plugin/scripts/sdlc/deploy.py`
- `plugin/scripts/sdlc/hooks.py`
- `plugin/scripts/sdlc/project.py`
- `sdlc/graph-selected-repomix-context-packs/intent.md`
- `sdlc/release-hook-hardening/intent.md`
- `sdlc/release-hook-hardening/spec.md`

# Symbols
- approver() (plugin/scripts/sdlc/deploy.py:L40)
- The named release manager from RELEASE_APPROVAL, or empty. (plugin/scripts/sdlc/deploy.py:L41)
- gated() (plugin/scripts/sdlc/deploy.py:L45)
- Environments at the `gate` tier in a `[deploy]` config table. (plugin/scripts/sdlc/deploy.py:L46)
- pre_bash() (plugin/scripts/sdlc/hooks.py:L121)
- deny() (plugin/scripts/sdlc/hooks.py:L26)
- merge() (plugin/scripts/sdlc/project.py:L141)
- config() (plugin/scripts/sdlc/project.py:L151)
- DEFAULT_CONFIG deep-merged with .sdlc.toml, so every key is always present;… (plugin/scripts/sdlc/project.py:L152)
- Constraints (sdlc/graph-selected-repomix-context-packs/intent.md:L48)
- Affected users and systems (sdlc/release-hook-hardening/intent.md:L20)
- Design (sdlc/release-hook-hardening/spec.md:L15)

# Depends on
- [Order of work](/modules/order-of-work-45.md)

# Inferred
- [Order of work](/modules/order-of-work-45.md)

# Features
- [graph-selected repomix context packs](/features/graph-selected-repomix-context-packs.md)
