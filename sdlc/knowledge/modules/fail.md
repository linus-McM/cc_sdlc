---
type: Module
title: fail
description: "Graphify community 87: scripts/sdlc/docs.py, scripts/sdlc/project.py"
resource: scripts/sdlc
tags: [module, graphify]
status: draft
generated: { by: sdlc/0.2.1, at: "2026-09-09T01:55:17Z" }
stale_after: "2026-09-23T01:55:17Z"
source_commit: 0972bddc57871b4600edb500118b597e83638fbc
sources:
  - { id: docs, resource: scripts/sdlc/docs.py, last_modified: "2026-09-09T11:55:13+10:00", digest: 2481bc15047e88b5 }
  - { id: project, resource: scripts/sdlc/project.py, last_modified: "2026-09-09T11:55:13+10:00", digest: 83c9a9a7fba6ace5 }
---

# Files
- `scripts/sdlc/docs.py`
- `scripts/sdlc/project.py`

# Symbols
- docs.py (scripts/sdlc/docs.py:L1)
- Stage documents: one Archify HTML diagram per stage, delivered from a Claude-… (scripts/sdlc/docs.py:L1)
- cfg() (scripts/sdlc/docs.py:L28)
- enabled() (scripts/sdlc/docs.py:L32)
- when_enabled() (scripts/sdlc/docs.py:L36)
- stage_of() (scripts/sdlc/docs.py:L44)
- target() (scripts/sdlc/docs.py:L50)
- The feature the document belongs to; maintain documents belong to the project,… (scripts/sdlc/docs.py:L51)
- render() (scripts/sdlc/docs.py:L56)
- check() (scripts/sdlc/docs.py:L61)
- open() (scripts/sdlc/docs.py:L66)
- fail() (scripts/sdlc/project.py:L80)

# Depends on
- [cli.py](/modules/cli-py.md)
- [config](/modules/config.md)
- [__init__.py](/modules/init-py.md)
- [project.py](/modules/project-py.md)

# Inferred
- no INFERRED edges; treat any that appear as hints

# Features
- [Archify stage documentation](/features/archify-stage-documentation.md)
- [Graphify and OKF knowledge base integration](/features/graphify-and-okf-knowledge-base-integration.md)
- [Rehearsal and band nits](/features/rehearsal-and-band-nits.md)
- [Release hook hardening](/features/release-hook-hardening.md)
- [Status next pointer](/features/status-next-pointer.md)
