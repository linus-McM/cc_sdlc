---
type: Module
title: maintain.py
description: "Graphify community 9: scripts/sdlc/maintain.py, scripts/sdlc/project.py"
resource: scripts/sdlc
tags: [module, graphify]
status: draft
generated: { by: sdlc/0.2.1, at: "2026-09-09T02:11:11Z" }
stale_after: "2026-09-23T02:11:11Z"
source_commit: b6ac2e811acbc23d7c5c8119fd8dd5532b43ccd0
sources:
  - { id: maintain, resource: scripts/sdlc/maintain.py, last_modified: "2026-09-09T12:03:58+10:00", digest: e571d91167dc6c51 }
  - { id: project, resource: scripts/sdlc/project.py, last_modified: "2026-09-09T12:06:46+10:00", digest: f517b9ce73f6af08 }
---

# Files
- `scripts/sdlc/maintain.py`
- `scripts/sdlc/project.py`

# Symbols
- maintain.py (scripts/sdlc/maintain.py:L1)
- Maintain-stage mechanics: deterministic control bands that close the loop back… (scripts/sdlc/maintain.py:L1)
- ingest() (scripts/sdlc/maintain.py:L113)
- lesson() (scripts/sdlc/maintain.py:L121)
- tier() (scripts/sdlc/maintain.py:L24)
- Western Electric rules on the trailing points against a rolling baseline. 3:… (scripts/sdlc/maintain.py:L25)
- bands() (scripts/sdlc/maintain.py:L54)
- Per-metric bands from sdlc/bands.toml, validated at the config boundary. (scripts/sdlc/maintain.py:L55)
- readings() (scripts/sdlc/maintain.py:L64)
- watch() (scripts/sdlc/maintain.py:L72)
- propose() (scripts/sdlc/maintain.py:L99)
- today() (scripts/sdlc/project.py:L177)

# Depends on
- [artifacts.py](/modules/artifacts-py.md)
- [docs.py](/modules/docs-py.md)
- [fail](/modules/fail.md)
- [hooks.py](/modules/hooks-py.md)
- [__init__.py](/modules/init-py.md)
- [project.py](/modules/project-py.md)
- [stages.py](/modules/stages-py.md)

# Inferred
- no INFERRED edges; treat any that appear as hints

# Features
- [Archify stage documentation](/features/archify-stage-documentation.md)
- [Dogfood fixes round two](/features/dogfood-fixes-round-two.md)
- [Graphify and OKF knowledge base integration](/features/graphify-and-okf-knowledge-base-integration.md)
- [Rehearsal and band nits](/features/rehearsal-and-band-nits.md)
- [Release hook hardening](/features/release-hook-hardening.md)
- [Status next pointer](/features/status-next-pointer.md)
