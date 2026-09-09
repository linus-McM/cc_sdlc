---
type: Module
title: fail
description: "Graphify community 76: scripts/sdlc/build.py, scripts/sdlc/evals.py, scripts/sdlc/project.py"
resource: scripts/sdlc
tags: [module, graphify]
status: draft
generated: { by: sdlc/0.2.0, at: "2026-09-09T00:28:56Z" }
stale_after: "2026-09-23T00:28:56Z"
source_commit: e46d381e2f64fa96bbb6eee6115eba30499cfe2e
sources:
  - { id: build, resource: scripts/sdlc/build.py, last_modified: "2026-09-08T09:22:42+10:00", digest: 3bd6dd8d38860ab6 }
  - { id: evals, resource: scripts/sdlc/evals.py, last_modified: "2026-09-07T12:20:58+10:00", digest: 6019b83ce814d4df }
  - { id: project, resource: scripts/sdlc/project.py, last_modified: "2026-09-09T08:32:17+10:00", digest: 15fdd6685d1225c1 }
---

# Files
- `scripts/sdlc/build.py`
- `scripts/sdlc/evals.py`
- `scripts/sdlc/project.py`

# Symbols
- build.py (scripts/sdlc/build.py:L1)
- Build-stage mechanics: red/green TDD log, plan sync, fix lock. (scripts/sdlc/build.py:L1)
- run_cmd() (scripts/sdlc/build.py:L15)
- cycles() (scripts/sdlc/build.py:L23)
- Completed red->green pairs, matched per step name in order. (scripts/sdlc/build.py:L24)
- tdd() (scripts/sdlc/build.py:L35)
- planned_files() (scripts/sdlc/build.py:L57)
- is_sdlc_owned() (scripts/sdlc/build.py:L62)
- sync() (scripts/sdlc/build.py:L66)
- fix() (scripts/sdlc/build.py:L78)
- evals.py (scripts/sdlc/evals.py:L1)
- Continuous evals: run each evals/*.json prompt non-interactively, then its… (scripts/sdlc/evals.py:L1)
- run_eval() (scripts/sdlc/evals.py:L15)
- run() (scripts/sdlc/evals.py:L32)
- fail() (scripts/sdlc/project.py:L65)

# Depends on
- [artifacts.py](/modules/artifacts-py.md)
- [cli.py](/modules/cli-py.md)
- [maintain.py](/modules/maintain-py.md)
- [project.py](/modules/project-py.md)
- [run](/modules/run.md)

# Inferred
- no INFERRED edges; treat any that appear as hints

# Features
- [Graphify and OKF knowledge base integration](/features/graphify-and-okf-knowledge-base-integration.md)
- [Rehearsal and band nits](/features/rehearsal-and-band-nits.md)
- [Release hook hardening](/features/release-hook-hardening.md)
- [Status next pointer](/features/status-next-pointer.md)
