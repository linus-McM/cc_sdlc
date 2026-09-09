---
type: Module
title: config
description: "Graphify community 1: scripts/sdlc/knowledge.py, scripts/sdlc/project.py, scripts/sdlc/testing.py"
resource: scripts/sdlc
tags: [module, graphify]
status: draft
generated: { by: sdlc/0.2.1, at: "2026-09-09T02:45:02Z" }
stale_after: "2026-09-23T02:45:02Z"
source_commit: 16ce44221e592819936583be6bb11207ce568f21
sources:
  - { id: knowledge, resource: scripts/sdlc/knowledge.py, last_modified: "2026-09-09T12:22:23+10:00", digest: 41ab4ac9324ee352 }
  - { id: project, resource: scripts/sdlc/project.py, last_modified: "2026-09-09T12:44:58+10:00", digest: d046c71e8661e436 }
  - { id: testing, resource: scripts/sdlc/testing.py, last_modified: "2026-09-09T12:22:23+10:00", digest: 6ae5daae0d475089 }
---

# Files
- `scripts/sdlc/knowledge.py`
- `scripts/sdlc/project.py`
- `scripts/sdlc/testing.py`

# Symbols
- enabled() (scripts/sdlc/knowledge.py:L159)
- config() (scripts/sdlc/project.py:L141)
- DEFAULT_CONFIG deep-merged with .sdlc.toml, so every key is always present;… (scripts/sdlc/project.py:L142)
- testing.py (scripts/sdlc/testing.py:L1)
- Test-stage mechanics: run the feedback loop, write test-report.json, validate… (scripts/sdlc/testing.py:L1)
- report() (scripts/sdlc/testing.py:L14)
- run() (scripts/sdlc/testing.py:L18)
- knowledge_result() (scripts/sdlc/testing.py:L42)
- The OKF conformance check as one more feedback-loop row; only conformance… (scripts/sdlc/testing.py:L43)
- count() (scripts/sdlc/testing.py:L50)
- Findings tagged `- Important:` / `- Nit:` in a review.md body. (scripts/sdlc/testing.py:L51)
- findings() (scripts/sdlc/testing.py:L55)
- review.md validated against REVIEW.md's three passes, with its finding counts. (scripts/sdlc/testing.py:L56)
- review() (scripts/sdlc/testing.py:L66)
- The test stage's exit: valid findings plus a fresh stage document. (scripts/sdlc/testing.py:L67)

# Depends on
- [artifacts.py](/modules/artifacts-py.md)
- [build.py](/modules/build-py.md)
- [conftest.py](/modules/conftest-py.md)
- [docs.py](/modules/docs-py.md)
- [project.py](/modules/project-py.md)
- [refresh](/modules/refresh.md)

# Inferred
- no INFERRED edges; treat any that appear as hints

# Features
- [Archify stage documentation](/features/archify-stage-documentation.md)
- [Graphify and OKF knowledge base integration](/features/graphify-and-okf-knowledge-base-integration.md)
- [Rehearsal and band nits](/features/rehearsal-and-band-nits.md)
- [Release hook hardening](/features/release-hook-hardening.md)
- [Status next pointer](/features/status-next-pointer.md)
