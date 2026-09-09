---
type: Module
title: fail
description: "Graphify community 86: scripts/sdlc/project.py, scripts/sdlc/testing.py"
resource: scripts/sdlc
tags: [module, graphify]
status: draft
generated: { by: sdlc/0.2.1, at: "2026-09-09T02:17:09Z" }
stale_after: "2026-09-23T02:17:09Z"
source_commit: 5f6707036a44f201af1092fdfdde11b3cdba2f6f
sources:
  - { id: project, resource: scripts/sdlc/project.py, last_modified: "2026-09-09T12:06:46+10:00", digest: f517b9ce73f6af08 }
  - { id: testing, resource: scripts/sdlc/testing.py, last_modified: "2026-09-09T12:01:29+10:00", digest: 02758dc892eb4b3c }
---

# Files
- `scripts/sdlc/project.py`
- `scripts/sdlc/testing.py`

# Symbols
- fail() (scripts/sdlc/project.py:L80)
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
- [cli.py](/modules/cli-py.md)
- [docs.py](/modules/docs-py.md)
- [hooks.py](/modules/hooks-py.md)
- [maintain.py](/modules/maintain-py.md)
- [Path](/modules/path.md)
- [project.py](/modules/project-py.md)
- [refresh](/modules/refresh.md)
- [run](/modules/run.md)
- [stages.py](/modules/stages-py.md)

# Inferred
- no INFERRED edges; treat any that appear as hints

# Features
- [Archify stage documentation](/features/archify-stage-documentation.md)
- [Graphify and OKF knowledge base integration](/features/graphify-and-okf-knowledge-base-integration.md)
- [Rehearsal and band nits](/features/rehearsal-and-band-nits.md)
- [Release hook hardening](/features/release-hook-hardening.md)
- [Status next pointer](/features/status-next-pointer.md)
