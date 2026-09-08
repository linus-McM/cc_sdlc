---
type: Module
title: deploy.py
description: "Graphify community 69: scripts/sdlc/deploy.py, scripts/sdlc/project.py, scripts/sdlc/testing.py"
resource: scripts/sdlc
tags: [module, graphify]
status: draft
generated: { by: sdlc/0.2.0, at: "2026-09-08T22:34:52Z" }
stale_after: "2026-09-22T22:34:52Z"
source_commit: 7062fb2891b2220b08230877b6bed905524ab89e
sources:
  - { id: deploy, resource: scripts/sdlc/deploy.py, last_modified: "2026-09-09T08:32:17+10:00", digest: 658f105def75d241 }
  - { id: project, resource: scripts/sdlc/project.py, last_modified: "2026-09-09T08:32:17+10:00", digest: 15fdd6685d1225c1 }
  - { id: testing, resource: scripts/sdlc/testing.py, last_modified: "2026-09-09T08:32:17+10:00", digest: b3939b3fb17f6e1d }
---

# Files
- `scripts/sdlc/deploy.py`
- `scripts/sdlc/project.py`
- `scripts/sdlc/testing.py`

# Symbols
- deploy.py (scripts/sdlc/deploy.py:L1)
- Deploy-stage mechanics: per-environment tiers, rollback rehearsal, release… (scripts/sdlc/deploy.py:L1)
- record() (scripts/sdlc/deploy.py:L102)
- knowledge_diff() (scripts/sdlc/deploy.py:L120)
- `git diff --stat main...HEAD` for the OKF bundle, so reviewers see what the… (scripts/sdlc/deploy.py:L121)
- pr_body() (scripts/sdlc/deploy.py:L130)
- state() (scripts/sdlc/deploy.py:L17)
- released() (scripts/sdlc/deploy.py:L21)
- readiness() (scripts/sdlc/deploy.py:L25)
- Reasons the feature is not ready for any environment; empty when ready. (scripts/sdlc/deploy.py:L26)
- approver() (scripts/sdlc/deploy.py:L40)
- The named release manager from RELEASE_APPROVAL, or empty. (scripts/sdlc/deploy.py:L41)
- check() (scripts/sdlc/deploy.py:L50)
- rehearse() (scripts/sdlc/deploy.py:L76)
- Run deploy.rollback in a throwaway detached worktree of HEAD; the checkout… (scripts/sdlc/deploy.py:L77)
- write_json() (scripts/sdlc/project.py:L182)
- report() (scripts/sdlc/testing.py:L14)

# Depends on
- [artifacts.py](/modules/artifacts-py.md)
- [cli.py](/modules/cli-py.md)
- [fail](/modules/fail.md)
- [hooks.py](/modules/hooks-py.md)
- [knowledge.py](/modules/knowledge-py.md)
- [maintain.py](/modules/maintain-py.md)
- [Path](/modules/path.md)
- [project.py](/modules/project-py.md)
- [read_json](/modules/read-json.md)

# Inferred
- [cli.py](/modules/cli-py.md)

# Features
- [Dogfood fixes round two](/features/dogfood-fixes-round-two.md)
- [Graphify and OKF knowledge base integration](/features/graphify-and-okf-knowledge-base-integration.md)
- [Rehearsal and band nits](/features/rehearsal-and-band-nits.md)
- [Release hook hardening](/features/release-hook-hardening.md)
- [Status next pointer](/features/status-next-pointer.md)
