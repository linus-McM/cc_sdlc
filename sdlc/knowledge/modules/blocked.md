---
type: Module
title: Blocked
description: "Graphify community 79: scripts/sdlc.py, scripts/sdlc/cli.py, scripts/sdlc/project.py"
resource: scripts
tags: [module, graphify]
status: draft
generated: { by: sdlc/0.2.1, at: "2026-09-09T03:02:28Z" }
stale_after: "2026-09-23T03:02:28Z"
source_commit: 5f197b911461521ad08675a63cc179623564938a
sources:
  - { id: sdlc, resource: scripts/sdlc.py, last_modified: "2026-09-07T12:20:58+10:00", digest: cdf9f0d1c1e68580 }
  - { id: cli, resource: scripts/sdlc/cli.py, last_modified: "2026-09-09T12:44:58+10:00", digest: f71285ffa536f9ea }
  - { id: project, resource: scripts/sdlc/project.py, last_modified: "2026-09-09T12:44:58+10:00", digest: cf02479288a1aba5 }
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
- parser() (scripts/sdlc/cli.py:L52)
- main() (scripts/sdlc/cli.py:L67)
- entry() (scripts/sdlc/cli.py:L78)
- Blocked (scripts/sdlc/project.py:L73)
- A gate refused; `.verdict` is the JSON dict the CLI prints. (scripts/sdlc/project.py:L74)
- .__init__() (scripts/sdlc/project.py:L76)

# Depends on
- [artifacts.py](/modules/artifacts-py.md)
- [config](/modules/config.md)
- [deploy.py](/modules/deploy-py.md)
- [docs.py](/modules/docs-py.md)
- [fail](/modules/fail.md)
- [knowledge.py](/modules/knowledge-py.md)
- [project.py](/modules/project-py.md)
- [testing.py](/modules/testing-py.md)

# Inferred
- no INFERRED edges; treat any that appear as hints

# Features
- [Archify stage documentation](/features/archify-stage-documentation.md)
- [Graphify and OKF knowledge base integration](/features/graphify-and-okf-knowledge-base-integration.md)
- [Rehearsal and band nits](/features/rehearsal-and-band-nits.md)
- [Release hook hardening](/features/release-hook-hardening.md)
- [Status next pointer](/features/status-next-pointer.md)
