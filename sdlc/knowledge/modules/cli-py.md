---
type: Module
title: cli.py
description: "Graphify community 88: scripts/sdlc.py, scripts/sdlc/cli.py"
resource: scripts
tags: [module, graphify]
status: draft
generated: { by: sdlc/0.2.1, at: "2026-09-09T02:01:32Z" }
stale_after: "2026-09-23T02:01:32Z"
source_commit: d8d61950c58abafa13a30ef68be4741e547839ef
sources:
  - { id: sdlc, resource: scripts/sdlc.py, last_modified: "2026-09-07T12:20:58+10:00", digest: cdf9f0d1c1e68580 }
  - { id: cli, resource: scripts/sdlc/cli.py, last_modified: "2026-09-09T12:01:29+10:00", digest: c64f98c69838f2cb }
---

# Files
- `scripts/sdlc.py`
- `scripts/sdlc/cli.py`

# Symbols
- sdlc.py (scripts/sdlc.py:L1)
- Launcher: python3 scripts/sdlc.py <stage> <action> ... (scripts/sdlc.py:L2)
- cli.py (scripts/sdlc/cli.py:L1)
- One entry point: `python3 scripts/sdlc.py <stage> <action> [arg]` prints a JSON… (scripts/sdlc/cli.py:L1)
- lifecycle() (scripts/sdlc/cli.py:L18)
- new/check/accept for an artifact stage; only `plan new` takes the positional… (scripts/sdlc/cli.py:L19)
- parser() (scripts/sdlc/cli.py:L54)
- main() (scripts/sdlc/cli.py:L69)
- entry() (scripts/sdlc/cli.py:L80)

# Depends on
- [deploy.py](/modules/deploy-py.md)
- [docs.py](/modules/docs-py.md)
- [fail](/modules/fail.md)
- [knowledge.py](/modules/knowledge-py.md)
- [maintain.py](/modules/maintain-py.md)
- [project.py](/modules/project-py.md)
- [stages.py](/modules/stages-py.md)
- [testing.py](/modules/testing-py.md)

# Inferred
- no INFERRED edges; treat any that appear as hints

# Features
- [Archify stage documentation](/features/archify-stage-documentation.md)
- [Graphify and OKF knowledge base integration](/features/graphify-and-okf-knowledge-base-integration.md)
