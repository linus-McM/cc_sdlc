---
type: Module
title: fail
description: "Graphify community 7: scripts/sdlc/__init__.py, scripts/sdlc/evals.py, scripts/sdlc/project.py, scripts/sdlc/testing.py"
resource: scripts/sdlc
tags: [module, graphify]
status: draft
generated: { by: sdlc/0.2.0, at: "2026-09-09T01:00:09Z" }
stale_after: "2026-09-23T01:00:09Z"
source_commit: f4b7a7e7c7ca48d51fac20696ba496746da179e6
sources:
  - { id: __init__, resource: scripts/sdlc/__init__.py, last_modified: "2026-09-07T12:20:58+10:00", digest: 0a6aea3cd6840dbf }
  - { id: evals, resource: scripts/sdlc/evals.py, last_modified: "2026-09-07T12:20:58+10:00", digest: 6019b83ce814d4df }
  - { id: project, resource: scripts/sdlc/project.py, last_modified: "2026-09-09T08:32:17+10:00", digest: 15fdd6685d1225c1 }
  - { id: testing, resource: scripts/sdlc/testing.py, last_modified: "2026-09-09T08:32:17+10:00", digest: b3939b3fb17f6e1d }
---

# Files
- `scripts/sdlc/__init__.py`
- `scripts/sdlc/evals.py`
- `scripts/sdlc/project.py`
- `scripts/sdlc/testing.py`

# Symbols
- __init__.py (scripts/sdlc/__init__.py:L1)
- sdlc — deterministic gates for the six-stage AI-native SDLC. Stdlib only. (scripts/sdlc/__init__.py:L1)
- evals.py (scripts/sdlc/evals.py:L1)
- Continuous evals: run each evals/*.json prompt non-interactively, then its… (scripts/sdlc/evals.py:L1)
- run_eval() (scripts/sdlc/evals.py:L15)
- run() (scripts/sdlc/evals.py:L32)
- fail() (scripts/sdlc/project.py:L65)
- testing.py (scripts/sdlc/testing.py:L1)
- Test-stage mechanics: run the feedback loop, write test-report.json, validate… (scripts/sdlc/testing.py:L1)
- run() (scripts/sdlc/testing.py:L18)
- knowledge_result() (scripts/sdlc/testing.py:L42)
- The OKF conformance check as one more feedback-loop row; only conformance… (scripts/sdlc/testing.py:L43)
- count() (scripts/sdlc/testing.py:L50)
- Findings tagged `- Important:` / `- Nit:` in a review.md body. (scripts/sdlc/testing.py:L51)
- review() (scripts/sdlc/testing.py:L55)

# Depends on
- [artifacts.py](/modules/artifacts-py.md)
- [cli.py](/modules/cli-py.md)
- [deploy.py](/modules/deploy-py.md)
- [hooks.py](/modules/hooks-py.md)
- [maintain.py](/modules/maintain-py.md)
- [project.py](/modules/project-py.md)
- [refresh](/modules/refresh.md)
- [run](/modules/run.md)
- [stages.py](/modules/stages-py.md)

# Inferred
- no INFERRED edges; treat any that appear as hints

# Features
- [Graphify and OKF knowledge base integration](/features/graphify-and-okf-knowledge-base-integration.md)
- [Rehearsal and band nits](/features/rehearsal-and-band-nits.md)
- [Release hook hardening](/features/release-hook-hardening.md)
- [Status next pointer](/features/status-next-pointer.md)
