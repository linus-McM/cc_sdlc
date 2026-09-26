---
type: Module
title: Order of work
description: "Graphify community 45: plugin/scripts/sdlc/hooks.py, sdlc/release-hook-hardening/plan.md, sdlc/release-hook-hardening/review.md"
resource: ""
tags: [module, graphify]
status: draft
generated: { by: sdlc/0.5.0, at: "2026-09-26T05:22:30Z" }
stale_after: "2026-10-10T05:22:30Z"
source_commit: c5f64f8d3b9b5e3268754f626b7f2e958fd6415e
sources:
  - { id: hooks, resource: plugin/scripts/sdlc/hooks.py, last_modified: "2026-09-19T13:08:30+10:00", digest: 40334c1872956197 }
  - { id: plan, resource: sdlc/release-hook-hardening/plan.md, last_modified: "2026-09-09T15:03:27+10:00", digest: 27db3b2d8bc6d184 }
  - { id: review, resource: sdlc/release-hook-hardening/review.md, last_modified: "2026-09-09T15:03:27+10:00", digest: ed3f8ea859e0a2fd }
---

# Files
- `plugin/scripts/sdlc/hooks.py`
- `sdlc/release-hook-hardening/plan.md`
- `sdlc/release-hook-hardening/review.md`

# Symbols
- release_hit() (plugin/scripts/sdlc/hooks.py:L102)
- What in `cmd` looks like a release to a gated environment, or None. Always: a… (plugin/scripts/sdlc/hooks.py:L103)
- command_lines() (plugin/scripts/sdlc/hooks.py:L78)
- Logical command lines: backslash continuations joined, heredoc bodies dropped. (plugin/scripts/sdlc/hooks.py:L79)
- tokens() (plugin/scripts/sdlc/hooks.py:L91)
- Shell tokens of every command line; quoted prose stays one token, unbalanced… (plugin/scripts/sdlc/hooks.py:L92)
- Order of work (sdlc/release-hook-hardening/plan.md:L14)
- release-hook-hardening/review.md (sdlc/release-hook-hardening/review.md:L1)
- Review: Release hook hardening (sdlc/release-hook-hardening/review.md:L1)
- Compliance (sdlc/release-hook-hardening/review.md:L14)
- Bugs (sdlc/release-hook-hardening/review.md:L4)

# Depends on
- [bash](/modules/bash.md)

# Inferred
- [bash](/modules/bash.md)
- [config](/modules/config.md)

# Features
- no feature plan names these files
