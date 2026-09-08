---
type: Module
title: maintain.py
description: "Graphify community 71: scripts/sdlc/maintain.py, scripts/sdlc/project.py"
resource: scripts/sdlc
tags: [module, graphify]
status: draft
generated: { by: sdlc/0.2.0, at: "2026-09-08T22:12:23Z" }
stale_after: "2026-09-22T22:12:23Z"
source_commit: b7fff727fc81eeb9a3aa4e92ba2c81caed3a3a56
sources:
  - { id: maintain, resource: scripts/sdlc/maintain.py, last_modified: "2026-09-08T15:49:55+10:00", digest: 75052069898694d5 }
  - { id: project, resource: scripts/sdlc/project.py, last_modified: "2026-09-09T07:32:46+10:00", digest: cd1977e43e9bb660 }
---

# Files
- `scripts/sdlc/maintain.py`
- `scripts/sdlc/project.py`

# Symbols
- maintain.py (scripts/sdlc/maintain.py:L1)
- Maintain-stage mechanics: deterministic control bands that close the loop back… (scripts/sdlc/maintain.py:L1)
- ingest() (scripts/sdlc/maintain.py:L109)
- lesson() (scripts/sdlc/maintain.py:L117)
- tier() (scripts/sdlc/maintain.py:L24)
- Western Electric rules on the trailing points against a rolling baseline. 3:… (scripts/sdlc/maintain.py:L25)
- bands() (scripts/sdlc/maintain.py:L54)
- Per-metric bands from sdlc/bands.toml, validated at the config boundary. (scripts/sdlc/maintain.py:L55)
- readings() (scripts/sdlc/maintain.py:L64)
- watch() (scripts/sdlc/maintain.py:L72)
- propose() (scripts/sdlc/maintain.py:L95)
- today() (scripts/sdlc/project.py:L132)
- home() (scripts/sdlc/project.py:L87)

# Depends on
- [artifacts.py](/modules/artifacts-py.md)
- [build.py](/modules/build-py.md)
- [fail](/modules/fail.md)
- [project.py](/modules/project-py.md)
- [stages.py](/modules/stages-py.md)

# Inferred
- no INFERRED edges; treat any that appear as hints

# Features
- [Dogfood fixes round two](/features/dogfood-fixes-round-two.md)
- [Graphify and OKF knowledge base integration](/features/graphify-and-okf-knowledge-base-integration.md)
- [Rehearsal and band nits](/features/rehearsal-and-band-nits.md)
- [Release hook hardening](/features/release-hook-hardening.md)
- [Status next pointer](/features/status-next-pointer.md)
