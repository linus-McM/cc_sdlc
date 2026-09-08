---
type: Module
title: fail
description: "Graphify community 72: scripts/sdlc/project.py, scripts/sdlc/testing.py"
resource: scripts/sdlc
tags: [module, graphify]
status: draft
generated: { by: sdlc/0.2.0, at: "2026-09-08T22:28:38Z" }
stale_after: "2026-09-22T22:28:38Z"
source_commit: 639850475d5980649e4dd44aed6fdad796bd7f4c
sources:
  - { id: project, resource: scripts/sdlc/project.py, last_modified: "2026-09-09T08:13:01+10:00", digest: 15fdd6685d1225c1 }
  - { id: testing, resource: scripts/sdlc/testing.py, last_modified: "2026-09-09T07:52:07+10:00", digest: b3939b3fb17f6e1d }
---

# Files
- `scripts/sdlc/project.py`
- `scripts/sdlc/testing.py`

# Symbols
- read_json() (scripts/sdlc/project.py:L146)
- fail() (scripts/sdlc/project.py:L64)
- testing.py (scripts/sdlc/testing.py:L1)
- Test-stage mechanics: run the feedback loop, write test-report.json, validate… (scripts/sdlc/testing.py:L1)
- report() (scripts/sdlc/testing.py:L14)
- run() (scripts/sdlc/testing.py:L18)
- knowledge_result() (scripts/sdlc/testing.py:L43)
- The OKF conformance check as one more feedback-loop row; only conformance… (scripts/sdlc/testing.py:L44)
- review() (scripts/sdlc/testing.py:L51)

# Depends on
- [artifacts.py](/modules/artifacts-py.md)
- [build.py](/modules/build-py.md)
- [cli.py](/modules/cli-py.md)
- [knowledge.py](/modules/knowledge-py.md)
- [maintain.py](/modules/maintain-py.md)
- [project.py](/modules/project-py.md)

# Inferred
- no INFERRED edges; treat any that appear as hints

# Features
- [Graphify and OKF knowledge base integration](/features/graphify-and-okf-knowledge-base-integration.md)
- [Rehearsal and band nits](/features/rehearsal-and-band-nits.md)
- [Release hook hardening](/features/release-hook-hardening.md)
- [Status next pointer](/features/status-next-pointer.md)
