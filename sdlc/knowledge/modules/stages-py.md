---
type: Module
title: stages.py
description: "Graphify community 68: scripts/sdlc/artifacts.py, scripts/sdlc/project.py, scripts/sdlc/stages.py"
resource: scripts/sdlc
tags: [module, graphify]
status: draft
generated: { by: sdlc/0.2.1, at: "2026-09-09T02:02:49Z" }
stale_after: "2026-09-23T02:02:49Z"
source_commit: f15b143d1ce08297fc13142247be8dc7f63d478f
sources:
  - { id: artifacts, resource: scripts/sdlc/artifacts.py, last_modified: "2026-09-09T08:32:17+10:00", digest: 3e063b545e7dd897 }
  - { id: project, resource: scripts/sdlc/project.py, last_modified: "2026-09-09T12:02:46+10:00", digest: feb3c46bca8f8281 }
  - { id: stages, resource: scripts/sdlc/stages.py, last_modified: "2026-09-09T12:01:29+10:00", digest: 845847cae3cfdb65 }
---

# Files
- `scripts/sdlc/artifacts.py`
- `scripts/sdlc/project.py`
- `scripts/sdlc/stages.py`

# Symbols
- meta() (scripts/sdlc/artifacts.py:L49)
- status() (scripts/sdlc/artifacts.py:L58)
- attempt() (scripts/sdlc/project.py:L84)
- Run a side mechanic without letting it decide the caller's verdict: a Blocked… (scripts/sdlc/project.py:L85)
- stages.py (scripts/sdlc/stages.py:L1)
- The ordered stage table, and the new/check/accept lifecycle shared by… (scripts/sdlc/stages.py:L1)
- status() (scripts/sdlc/stages.py:L105)
- prerequisite() (scripts/sdlc/stages.py:L18)
- next_command() (scripts/sdlc/stages.py:L23)
- accepted() (scripts/sdlc/stages.py:L27)
- gated() (scripts/sdlc/stages.py:L32)
- The feature directory, provided `artifact` (if any) has been accepted by a… (scripts/sdlc/stages.py:L33)
- create_feature() (scripts/sdlc/stages.py:L42)
- new() (scripts/sdlc/stages.py:L53)
- check() (scripts/sdlc/stages.py:L75)
- accept() (scripts/sdlc/stages.py:L86)
- next_for() (scripts/sdlc/stages.py:L95)
- The one /sdlc command to run next; the deploy gates decide when test and deploy… (scripts/sdlc/stages.py:L96)

# Depends on
- [artifacts.py](/modules/artifacts-py.md)
- [deploy.py](/modules/deploy-py.md)
- [docs.py](/modules/docs-py.md)
- [fail](/modules/fail.md)
- [knowledge.py](/modules/knowledge-py.md)
- [maintain.py](/modules/maintain-py.md)
- [project.py](/modules/project-py.md)
- [refresh](/modules/refresh.md)

# Inferred
- no INFERRED edges; treat any that appear as hints

# Features
- [Archify stage documentation](/features/archify-stage-documentation.md)
- [Graphify and OKF knowledge base integration](/features/graphify-and-okf-knowledge-base-integration.md)
- [Rehearsal and band nits](/features/rehearsal-and-band-nits.md)
- [Release hook hardening](/features/release-hook-hardening.md)
- [Status next pointer](/features/status-next-pointer.md)
