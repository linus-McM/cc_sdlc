---
type: Module
title: stages.py
description: "Graphify community 3: scripts/sdlc/artifacts.py, scripts/sdlc/project.py, scripts/sdlc/stages.py"
resource: scripts/sdlc
tags: [module, graphify]
status: draft
generated: { by: sdlc/0.2.0, at: "2026-09-08T22:28:38Z" }
stale_after: "2026-09-22T22:28:38Z"
source_commit: 639850475d5980649e4dd44aed6fdad796bd7f4c
sources:
  - { id: artifacts, resource: scripts/sdlc/artifacts.py, last_modified: "2026-09-09T07:44:17+10:00", digest: 3e063b545e7dd897 }
  - { id: project, resource: scripts/sdlc/project.py, last_modified: "2026-09-09T08:13:01+10:00", digest: 15fdd6685d1225c1 }
  - { id: stages, resource: scripts/sdlc/stages.py, last_modified: "2026-09-09T07:52:07+10:00", digest: 54e5024a991ef45d }
---

# Files
- `scripts/sdlc/artifacts.py`
- `scripts/sdlc/project.py`
- `scripts/sdlc/stages.py`

# Symbols
- meta() (scripts/sdlc/artifacts.py:L49)
- status() (scripts/sdlc/artifacts.py:L58)
- feature() (scripts/sdlc/project.py:L94)
- The named feature directory, or the most recently modified one; Blocked when… (scripts/sdlc/project.py:L95)
- stages.py (scripts/sdlc/stages.py:L1)
- The ordered stage table, and the new/check/accept lifecycle shared by… (scripts/sdlc/stages.py:L1)
- next_for() (scripts/sdlc/stages.py:L102)
- The one /sdlc command to run next; the deploy gates decide when test and deploy… (scripts/sdlc/stages.py:L103)
- status() (scripts/sdlc/stages.py:L112)
- prerequisite() (scripts/sdlc/stages.py:L18)
- next_command() (scripts/sdlc/stages.py:L23)
- accepted() (scripts/sdlc/stages.py:L27)
- gated() (scripts/sdlc/stages.py:L32)
- The feature directory, provided `artifact` (if any) has been accepted by a… (scripts/sdlc/stages.py:L33)
- create_feature() (scripts/sdlc/stages.py:L42)
- new() (scripts/sdlc/stages.py:L53)
- attempt() (scripts/sdlc/stages.py:L75)
- Run a knowledge mechanic without letting its verdict decide the stage's own; a… (scripts/sdlc/stages.py:L76)
- check() (scripts/sdlc/stages.py:L83)
- accept() (scripts/sdlc/stages.py:L94)

# Depends on
- [artifacts.py](/modules/artifacts-py.md)
- [build.py](/modules/build-py.md)
- [cli.py](/modules/cli-py.md)
- [deploy.py](/modules/deploy-py.md)
- [fail](/modules/fail.md)
- [knowledge.py](/modules/knowledge-py.md)
- [maintain.py](/modules/maintain-py.md)
- [project.py](/modules/project-py.md)

# Inferred
- [cli.py](/modules/cli-py.md)

# Features
- [Graphify and OKF knowledge base integration](/features/graphify-and-okf-knowledge-base-integration.md)
- [Rehearsal and band nits](/features/rehearsal-and-band-nits.md)
- [Release hook hardening](/features/release-hook-hardening.md)
- [Status next pointer](/features/status-next-pointer.md)
