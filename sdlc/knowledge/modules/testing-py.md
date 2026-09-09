---
type: Module
title: testing.py
description: "Graphify community 86: scripts/sdlc/testing.py"
resource: scripts/sdlc
tags: [module, graphify]
status: draft
generated: { by: sdlc/0.2.1, at: "2026-09-09T02:06:51Z" }
stale_after: "2026-09-23T02:06:51Z"
source_commit: 7470298f4fecfcb461736faefdc6244e8983e4de
sources:
  - { id: testing, resource: scripts/sdlc/testing.py, last_modified: "2026-09-09T12:01:29+10:00", digest: 02758dc892eb4b3c }
---

# Files
- `scripts/sdlc/testing.py`

# Symbols
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
- [cfg](/modules/cfg.md)
- [deploy.py](/modules/deploy-py.md)
- [docs.py](/modules/docs-py.md)
- [fail](/modules/fail.md)
- [hooks.py](/modules/hooks-py.md)
- [maintain.py](/modules/maintain-py.md)
- [project.py](/modules/project-py.md)
- [stages.py](/modules/stages-py.md)

# Inferred
- no INFERRED edges; treat any that appear as hints

# Features
- [Archify stage documentation](/features/archify-stage-documentation.md)
- [Graphify and OKF knowledge base integration](/features/graphify-and-okf-knowledge-base-integration.md)
