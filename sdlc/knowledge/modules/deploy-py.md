---
type: Module
title: deploy.py
description: "Graphify community 2: plugin/scripts/sdlc/deploy.py, plugin/scripts/sdlc/project.py, sdlc/rehearsal-and-band-nits/intent.md, sdlc/release-hook-hardening/intent.md, sdlc/release-hook-hardening/plan.md,"
resource: ""
tags: [module, graphify]
status: draft
generated: { by: sdlc/0.5.0, at: "2026-09-25T07:29:30Z" }
stale_after: "2026-10-09T07:29:30Z"
source_commit: dc32a5b78bc303376f02bfe7d43360ae82fa4a82
sources:
  - { id: deploy, resource: plugin/scripts/sdlc/deploy.py, last_modified: "2026-09-24T11:36:09+10:00", digest: 99b508f60ff0691d }
  - { id: project, resource: plugin/scripts/sdlc/project.py, last_modified: "2026-09-24T11:36:09+10:00", digest: d1e5536892dbd875 }
  - { id: intent, resource: sdlc/rehearsal-and-band-nits/intent.md, last_modified: "2026-09-09T15:03:27+10:00", digest: 5fbfef41a758468b }
  - { id: intent, resource: sdlc/release-hook-hardening/intent.md, last_modified: "2026-09-09T15:03:27+10:00", digest: ed3ebb9b592952e4 }
  - { id: plan, resource: sdlc/release-hook-hardening/plan.md, last_modified: "2026-09-09T15:03:27+10:00", digest: 27db3b2d8bc6d184 }
  - { id: pr-body, resource: sdlc/release-hook-hardening/pr-body.md, last_modified: "2026-09-09T15:03:27+10:00", digest: 7567eba92600a80f }
  - { id: spec, resource: sdlc/release-hook-hardening/spec.md, last_modified: "2026-09-09T15:03:27+10:00", digest: ceec7eaa899c3151 }
  - { id: review, resource: sdlc/status-next-pointer/review.md, last_modified: "2026-09-09T15:03:27+10:00", digest: f6fa7c95be7b4059 }
  - { id: spec, resource: sdlc/status-next-pointer/spec.md, last_modified: "2026-09-09T15:03:27+10:00", digest: 21a434a2e5ea4acf }
---

# Files
- `plugin/scripts/sdlc/deploy.py`
- `plugin/scripts/sdlc/project.py`
- `sdlc/rehearsal-and-band-nits/intent.md`
- `sdlc/release-hook-hardening/intent.md`
- `sdlc/release-hook-hardening/plan.md`
- `sdlc/release-hook-hardening/pr-body.md`
- `sdlc/release-hook-hardening/spec.md`
- `sdlc/status-next-pointer/review.md`
- `sdlc/status-next-pointer/spec.md`

# Symbols
- deploy.py (plugin/scripts/sdlc/deploy.py:L1)
- Deploy-stage mechanics: per-environment tiers, rollback rehearsal, release… (plugin/scripts/sdlc/deploy.py:L1)
- record() (plugin/scripts/sdlc/deploy.py:L102)
- state() (plugin/scripts/sdlc/deploy.py:L17)
- released() (plugin/scripts/sdlc/deploy.py:L21)
- readiness() (plugin/scripts/sdlc/deploy.py:L25)
- Reasons the feature is not ready for any environment; empty when ready. (plugin/scripts/sdlc/deploy.py:L26)
- approver() (plugin/scripts/sdlc/deploy.py:L40)
- The named release manager from RELEASE_APPROVAL, or empty. (plugin/scripts/sdlc/deploy.py:L41)
- check() (plugin/scripts/sdlc/deploy.py:L50)
- read_json() (plugin/scripts/sdlc/project.py:L247)
- Constraints (sdlc/rehearsal-and-band-nits/intent.md:L33)
- release-hook-hardening/intent.md (sdlc/release-hook-hardening/intent.md:L1)
- Intent: Release hook hardening (sdlc/release-hook-hardening/intent.md:L1)
- Proposed outcome (sdlc/release-hook-hardening/intent.md:L12)
- Affected users and systems (sdlc/release-hook-hardening/intent.md:L20)
- Constraints (sdlc/release-hook-hardening/intent.md:L25)
- Open questions (sdlc/release-hook-hardening/intent.md:L31)
- Problem (sdlc/release-hook-hardening/intent.md:L4)
- release-hook-hardening/plan.md (sdlc/release-hook-hardening/plan.md:L1)
- Plan: Release hook hardening (sdlc/release-hook-hardening/plan.md:L1)
- Files that change (sdlc/release-hook-hardening/plan.md:L4)
- Risks (sdlc/release-hook-hardening/plan.md:L49)
- Proof (sdlc/release-hook-hardening/plan.md:L62)
- release-hook-hardening/pr-body.md (sdlc/release-hook-hardening/pr-body.md:L1)
- Release hook hardening (sdlc/release-hook-hardening/pr-body.md:L1)
- Artifacts (sdlc/release-hook-hardening/pr-body.md:L11)
- Proof (sdlc/release-hook-hardening/pr-body.md:L16)
- Why (sdlc/release-hook-hardening/pr-body.md:L3)
- release-hook-hardening/spec.md (sdlc/release-hook-hardening/spec.md:L1)
- Spec: Release hook hardening (sdlc/release-hook-hardening/spec.md:L1)
- Design (sdlc/release-hook-hardening/spec.md:L15)
- Concerns (sdlc/release-hook-hardening/spec.md:L27)
- Open questions (sdlc/release-hook-hardening/spec.md:L31)
- Requirements (sdlc/release-hook-hardening/spec.md:L4)
- status-next-pointer/review.md (sdlc/status-next-pointer/review.md:L1)
- Review: Status next pointer (sdlc/status-next-pointer/review.md:L1)
- Compliance (sdlc/status-next-pointer/review.md:L11)
- Bugs (sdlc/status-next-pointer/review.md:L4)
- Security (sdlc/status-next-pointer/review.md:L8)
- status-next-pointer/spec.md (sdlc/status-next-pointer/spec.md:L1)
- Spec: Status next pointer (sdlc/status-next-pointer/spec.md:L1)
- Design (sdlc/status-next-pointer/spec.md:L13)
- Concerns (sdlc/status-next-pointer/spec.md:L26)
- Open questions (sdlc/status-next-pointer/spec.md:L29)
- Requirements (sdlc/status-next-pointer/spec.md:L4)

# Depends on
- [artifacts.py](/modules/artifacts-py.md)
- [Blocked](/modules/blocked.md)
- [docs.py](/modules/docs-py.md)
- [fail](/modules/fail.md)
- [fill](/modules/fill.md)
- [__init__.py](/modules/init-py.md)
- [knowledge.py](/modules/knowledge-py.md)
- [maintain.py](/modules/maintain-py.md)
- [project.py](/modules/project-py.md)
- [rehearse](/modules/rehearse.md)
- [status](/modules/status.md)
- [test_hooks.py](/modules/test-hooks-py.md)

# Inferred
- [Blocked](/modules/blocked.md)
- [fill](/modules/fill.md)
- [project.py](/modules/project-py.md)
- [rehearse](/modules/rehearse.md)
- [stages.py](/modules/stages-py.md)

# Features
- no feature plan names these files
