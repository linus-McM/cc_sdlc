---
type: Module
title: cli.py
description: "Graphify community 70: scripts/sdlc.py, scripts/sdlc/cli.py, scripts/sdlc/project.py"
resource: scripts
tags: [module, graphify]
status: draft
generated: { by: sdlc/0.2.1, at: "2026-09-09T01:03:33Z" }
stale_after: "2026-09-23T01:03:33Z"
source_commit: 3cb8b13d02aacc9b51a9fd505374e4b8cf7933a8
sources:
  - { id: sdlc, resource: scripts/sdlc.py, last_modified: "2026-09-07T12:20:58+10:00", digest: cdf9f0d1c1e68580 }
  - { id: cli, resource: scripts/sdlc/cli.py, last_modified: "2026-09-09T08:32:17+10:00", digest: 58b01a04b3db569b }
  - { id: project, resource: scripts/sdlc/project.py, last_modified: "2026-09-09T08:32:17+10:00", digest: 15fdd6685d1225c1 }
---

# Files
- `scripts/sdlc.py`
- `scripts/sdlc/cli.py`
- `scripts/sdlc/project.py`

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
- Blocked (scripts/sdlc/project.py:L57)
- A gate refused; `.verdict` is the JSON dict the CLI prints. (scripts/sdlc/project.py:L58)
- .__init__() (scripts/sdlc/project.py:L60)

# Depends on
- [deploy.py](/modules/deploy-py.md)
- [fail](/modules/fail.md)
- [knowledge.py](/modules/knowledge-py.md)
- [maintain.py](/modules/maintain-py.md)
- [project.py](/modules/project-py.md)
- [stages.py](/modules/stages-py.md)
- [testing.py](/modules/testing-py.md)

# Inferred
- no INFERRED edges; treat any that appear as hints

# Features
- [Graphify and OKF knowledge base integration](/features/graphify-and-okf-knowledge-base-integration.md)
- [Rehearsal and band nits](/features/rehearsal-and-band-nits.md)
- [Release hook hardening](/features/release-hook-hardening.md)
- [Status next pointer](/features/status-next-pointer.md)
