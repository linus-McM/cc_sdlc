---
type: Module
title: cli.py
description: "Graphify community 70: scripts/sdlc.py, scripts/sdlc/cli.py"
resource: scripts
tags: [module, graphify]
status: draft
generated: { by: sdlc/0.2.0, at: "2026-09-09T00:57:33Z" }
stale_after: "2026-09-23T00:57:33Z"
source_commit: a432e14e93d9df64b84d79b6e6d30b2233332f6e
sources:
  - { id: sdlc, resource: scripts/sdlc.py, last_modified: "2026-09-07T12:20:58+10:00", digest: cdf9f0d1c1e68580 }
  - { id: cli, resource: scripts/sdlc/cli.py, last_modified: "2026-09-09T08:32:17+10:00", digest: 58b01a04b3db569b }
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
- parser() (scripts/sdlc/cli.py:L51)
- main() (scripts/sdlc/cli.py:L66)
- entry() (scripts/sdlc/cli.py:L77)

# Depends on
- [deploy.py](/modules/deploy-py.md)
- [fail](/modules/fail.md)
- [hooks.py](/modules/hooks-py.md)
- [knowledge.py](/modules/knowledge-py.md)
- [maintain.py](/modules/maintain-py.md)
- [project.py](/modules/project-py.md)
- [run](/modules/run.md)
- [stages.py](/modules/stages-py.md)

# Inferred
- [hooks.py](/modules/hooks-py.md)

# Features
- [Graphify and OKF knowledge base integration](/features/graphify-and-okf-knowledge-base-integration.md)
