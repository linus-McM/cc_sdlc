---
type: Module
title: fail
description: "Graphify community 70: scripts/sdlc/__init__.py, scripts/sdlc/evals.py, scripts/sdlc/project.py"
resource: scripts/sdlc
tags: [module, graphify]
status: draft
generated: { by: sdlc/0.2.1, at: "2026-09-09T02:06:51Z" }
stale_after: "2026-09-23T02:06:51Z"
source_commit: 7470298f4fecfcb461736faefdc6244e8983e4de
sources:
  - { id: __init__, resource: scripts/sdlc/__init__.py, last_modified: "2026-09-07T12:20:58+10:00", digest: 0a6aea3cd6840dbf }
  - { id: evals, resource: scripts/sdlc/evals.py, last_modified: "2026-09-07T12:20:58+10:00", digest: 6019b83ce814d4df }
  - { id: project, resource: scripts/sdlc/project.py, last_modified: "2026-09-09T12:06:46+10:00", digest: f517b9ce73f6af08 }
---

# Files
- `scripts/sdlc/__init__.py`
- `scripts/sdlc/evals.py`
- `scripts/sdlc/project.py`

# Symbols
- __init__.py (scripts/sdlc/__init__.py:L1)
- sdlc — deterministic gates for the six-stage AI-native SDLC. Stdlib only. (scripts/sdlc/__init__.py:L1)
- evals.py (scripts/sdlc/evals.py:L1)
- Continuous evals: run each evals/*.json prompt non-interactively, then its… (scripts/sdlc/evals.py:L1)
- run_eval() (scripts/sdlc/evals.py:L15)
- run() (scripts/sdlc/evals.py:L32)
- fail() (scripts/sdlc/project.py:L80)

# Depends on
- [cli.py](/modules/cli-py.md)
- [deploy.py](/modules/deploy-py.md)
- [hooks.py](/modules/hooks-py.md)
- [maintain.py](/modules/maintain-py.md)
- [project.py](/modules/project-py.md)

# Inferred
- no INFERRED edges; treat any that appear as hints

# Features
- [Archify stage documentation](/features/archify-stage-documentation.md)
- [Graphify and OKF knowledge base integration](/features/graphify-and-okf-knowledge-base-integration.md)
- [Rehearsal and band nits](/features/rehearsal-and-band-nits.md)
- [Release hook hardening](/features/release-hook-hardening.md)
- [Status next pointer](/features/status-next-pointer.md)
