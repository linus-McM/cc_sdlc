---
type: Module
title: fail
description: "Graphify community 70: scripts/sdlc/build.py, scripts/sdlc/evals.py, scripts/sdlc/project.py, scripts/sdlc/testing.py"
resource: scripts/sdlc
tags: [module, graphify]
status: draft
generated: { by: sdlc/0.2.1, at: "2026-09-09T02:22:28Z" }
stale_after: "2026-09-23T02:22:28Z"
source_commit: 596440e8a2a56052df06112cb01e32437adfaa8c
sources:
  - { id: build, resource: scripts/sdlc/build.py, last_modified: "2026-09-08T09:22:42+10:00", digest: 3bd6dd8d38860ab6 }
  - { id: evals, resource: scripts/sdlc/evals.py, last_modified: "2026-09-07T12:20:58+10:00", digest: 6019b83ce814d4df }
  - { id: project, resource: scripts/sdlc/project.py, last_modified: "2026-09-09T12:22:23+10:00", digest: 418f9277e7848a02 }
  - { id: testing, resource: scripts/sdlc/testing.py, last_modified: "2026-09-09T12:22:23+10:00", digest: 6ae5daae0d475089 }
---

# Files
- `scripts/sdlc/build.py`
- `scripts/sdlc/evals.py`
- `scripts/sdlc/project.py`
- `scripts/sdlc/testing.py`

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
- merge() (scripts/sdlc/project.py:L131)
- config() (scripts/sdlc/project.py:L141)
- DEFAULT_CONFIG deep-merged with .sdlc.toml, so every key is always present;… (scripts/sdlc/project.py:L142)
- read_jsonl() (scripts/sdlc/project.py:L224)
- append_jsonl() (scripts/sdlc/project.py:L228)
- fail() (scripts/sdlc/project.py:L81)
- run() (scripts/sdlc/testing.py:L18)

# Depends on
- [artifacts.py](/modules/artifacts-py.md)
- [Blocked](/modules/blocked.md)
- [cfg](/modules/cfg.md)
- [conftest.py](/modules/conftest-py.md)
- [__init__.py](/modules/init-py.md)
- [maintain.py](/modules/maintain-py.md)
- [project.py](/modules/project-py.md)
- [stages.py](/modules/stages-py.md)

# Inferred
- no INFERRED edges; treat any that appear as hints

# Features
- [Archify stage documentation](/features/archify-stage-documentation.md)
- [Graphify and OKF knowledge base integration](/features/graphify-and-okf-knowledge-base-integration.md)
- [Rehearsal and band nits](/features/rehearsal-and-band-nits.md)
- [Release hook hardening](/features/release-hook-hardening.md)
- [Status next pointer](/features/status-next-pointer.md)
