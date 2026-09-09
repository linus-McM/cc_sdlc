---
type: Module
title: deploy.py
description: "Graphify community 71: scripts/sdlc/deploy.py"
resource: scripts/sdlc
tags: [module, graphify]
status: draft
generated: { by: sdlc/0.2.1, at: "2026-09-09T02:46:50Z" }
stale_after: "2026-09-23T02:46:50Z"
source_commit: 5f197b911461521ad08675a63cc179623564938a
sources:
  - { id: deploy, resource: scripts/sdlc/deploy.py, last_modified: "2026-09-09T12:22:23+10:00", digest: 13fece25897d5a38 }
---

# Files
- `scripts/sdlc/deploy.py`

# Symbols
- deploy.py (scripts/sdlc/deploy.py:L1)
- Deploy-stage mechanics: per-environment tiers, rollback rehearsal, release… (scripts/sdlc/deploy.py:L1)
- record() (scripts/sdlc/deploy.py:L102)
- knowledge_diff() (scripts/sdlc/deploy.py:L121)
- `git diff --stat main...HEAD` for the OKF bundle, so reviewers see what the… (scripts/sdlc/deploy.py:L122)
- pr_body() (scripts/sdlc/deploy.py:L133)
- state() (scripts/sdlc/deploy.py:L17)
- released() (scripts/sdlc/deploy.py:L21)
- readiness() (scripts/sdlc/deploy.py:L25)
- Reasons the feature is not ready for any environment; empty when ready. (scripts/sdlc/deploy.py:L26)
- approver() (scripts/sdlc/deploy.py:L40)
- The named release manager from RELEASE_APPROVAL, or empty. (scripts/sdlc/deploy.py:L41)
- check() (scripts/sdlc/deploy.py:L50)
- rehearse() (scripts/sdlc/deploy.py:L76)
- Run deploy.rollback in a throwaway detached worktree of HEAD; the checkout… (scripts/sdlc/deploy.py:L77)

# Depends on
- [artifacts.py](/modules/artifacts-py.md)
- [Blocked](/modules/blocked.md)
- [config](/modules/config.md)
- [conftest.py](/modules/conftest-py.md)
- [docs.py](/modules/docs-py.md)
- [fail](/modules/fail.md)
- [hooks.py](/modules/hooks-py.md)
- [knowledge.py](/modules/knowledge-py.md)
- [project.py](/modules/project-py.md)
- [status](/modules/status.md)
- [testing.py](/modules/testing-py.md)

# Inferred
- [Blocked](/modules/blocked.md)

# Features
- [Archify stage documentation](/features/archify-stage-documentation.md)
- [Dogfood fixes round two](/features/dogfood-fixes-round-two.md)
- [Graphify and OKF knowledge base integration](/features/graphify-and-okf-knowledge-base-integration.md)
- [Rehearsal and band nits](/features/rehearsal-and-band-nits.md)
- [Release hook hardening](/features/release-hook-hardening.md)
- [Status next pointer](/features/status-next-pointer.md)
