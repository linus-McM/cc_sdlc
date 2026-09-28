---
type: Module
title: pre_bash
description: "Graphify community 59: plugin/scripts/sdlc/deploy.py, plugin/scripts/sdlc/hooks.py, sdlc/release-hook-hardening/review.md, sdlc/release-hook-hardening/spec.md"
resource: ""
tags: [module, graphify]
status: draft
generated: { by: sdlc/0.8.1, at: "2026-09-28T22:57:53Z" }
stale_after: "2026-10-12T22:57:53Z"
source_commit: 0754d821fc594b90c529849cddaca10dc6109921
sources:
  - { id: deploy, resource: plugin/scripts/sdlc/deploy.py, last_modified: "2026-09-26T16:35:55+10:00", digest: d2d3493a1ed08434 }
  - { id: hooks, resource: plugin/scripts/sdlc/hooks.py, last_modified: "2026-09-26T15:09:04+10:00", digest: ddf52a8e990d343f }
  - { id: review, resource: sdlc/release-hook-hardening/review.md, last_modified: "2026-09-09T15:03:27+10:00", digest: ed3f8ea859e0a2fd }
  - { id: spec, resource: sdlc/release-hook-hardening/spec.md, last_modified: "2026-09-09T15:03:27+10:00", digest: ceec7eaa899c3151 }
---

# Files
- `plugin/scripts/sdlc/deploy.py`
- `plugin/scripts/sdlc/hooks.py`
- `sdlc/release-hook-hardening/review.md`
- `sdlc/release-hook-hardening/spec.md`

# Symbols
- approver() (plugin/scripts/sdlc/deploy.py:L45)
- The named release manager from RELEASE_APPROVAL, or empty. (plugin/scripts/sdlc/deploy.py:L46)
- gated() (plugin/scripts/sdlc/deploy.py:L50)
- Environments at the `gate` tier in a `[deploy]` config table. (plugin/scripts/sdlc/deploy.py:L51)
- release_hit() (plugin/scripts/sdlc/hooks.py:L102)
- What in `cmd` looks like a release to a gated environment, or None. Always: a… (plugin/scripts/sdlc/hooks.py:L103)
- pre_bash() (plugin/scripts/sdlc/hooks.py:L121)
- deny() (plugin/scripts/sdlc/hooks.py:L26)
- command_lines() (plugin/scripts/sdlc/hooks.py:L78)
- Logical command lines: backslash continuations joined, heredoc bodies dropped. (plugin/scripts/sdlc/hooks.py:L79)
- tokens() (plugin/scripts/sdlc/hooks.py:L91)
- Shell tokens of every command line; quoted prose stays one token, unbalanced… (plugin/scripts/sdlc/hooks.py:L92)
- Compliance (sdlc/release-hook-hardening/review.md:L14)
- Design (sdlc/release-hook-hardening/spec.md:L15)

# Depends on
- [project.py](/modules/project-py.md)

# Inferred
- [project.py](/modules/project-py.md)

# Features
- [graph-selected repomix context packs](/features/graph-selected-repomix-context-packs.md)
