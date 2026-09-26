---
type: Module
title: check
description: "Graphify community 83: plugin/scripts/sdlc/deploy.py, plugin/scripts/sdlc/project.py, plugin/scripts/sdlc/testing.py, sdlc/rehearsal-and-band-nits/intent.md, sdlc/release-hook-hardening/intent.md, sdl"
resource: ""
tags: [module, graphify]
status: draft
generated: { by: sdlc/0.5.0, at: "2026-09-26T06:33:18Z" }
stale_after: "2026-10-10T06:33:18Z"
source_commit: 5c45a37edd0dc635576e390a1174bea9fad6d10b
sources:
  - { id: deploy, resource: plugin/scripts/sdlc/deploy.py, last_modified: "2026-09-26T16:06:32+10:00", digest: d2d3493a1ed08434 }
  - { id: project, resource: plugin/scripts/sdlc/project.py, last_modified: "2026-09-26T16:06:32+10:00", digest: 26698ea0d06e1efe }
  - { id: testing, resource: plugin/scripts/sdlc/testing.py, last_modified: "2026-09-26T15:51:45+10:00", digest: 68b187c7a3220c0b }
  - { id: intent, resource: sdlc/rehearsal-and-band-nits/intent.md, last_modified: "2026-09-09T15:03:27+10:00", digest: 5fbfef41a758468b }
  - { id: intent, resource: sdlc/release-hook-hardening/intent.md, last_modified: "2026-09-09T15:03:27+10:00", digest: ed3ebb9b592952e4 }
  - { id: pr-body, resource: sdlc/release-hook-hardening/pr-body.md, last_modified: "2026-09-09T15:03:27+10:00", digest: 7567eba92600a80f }
  - { id: spec, resource: sdlc/release-hook-hardening/spec.md, last_modified: "2026-09-09T15:03:27+10:00", digest: ceec7eaa899c3151 }
  - { id: review, resource: sdlc/status-next-pointer/review.md, last_modified: "2026-09-09T15:03:27+10:00", digest: f6fa7c95be7b4059 }
  - { id: spec, resource: sdlc/status-next-pointer/spec.md, last_modified: "2026-09-09T15:03:27+10:00", digest: 21a434a2e5ea4acf }
---

# Files
- `plugin/scripts/sdlc/deploy.py`
- `plugin/scripts/sdlc/project.py`
- `plugin/scripts/sdlc/testing.py`
- `sdlc/rehearsal-and-band-nits/intent.md`
- `sdlc/release-hook-hardening/intent.md`
- `sdlc/release-hook-hardening/pr-body.md`
- `sdlc/release-hook-hardening/spec.md`
- `sdlc/status-next-pointer/review.md`
- `sdlc/status-next-pointer/spec.md`

# Symbols
- record() (plugin/scripts/sdlc/deploy.py:L107)
- knowledge_diff() (plugin/scripts/sdlc/deploy.py:L127)
- `git diff --stat main...HEAD` for the OKF bundle, so reviewers see what the… (plugin/scripts/sdlc/deploy.py:L128)
- pr_body() (plugin/scripts/sdlc/deploy.py:L139)
- state() (plugin/scripts/sdlc/deploy.py:L17)
- production() (plugin/scripts/sdlc/deploy.py:L21)
- The feature's production deployments, oldest first. (plugin/scripts/sdlc/deploy.py:L22)
- released() (plugin/scripts/sdlc/deploy.py:L26)
- readiness() (plugin/scripts/sdlc/deploy.py:L30)
- Reasons the feature is not ready for any environment; empty when ready. (plugin/scripts/sdlc/deploy.py:L31)
- check() (plugin/scripts/sdlc/deploy.py:L55)
- read_json() (plugin/scripts/sdlc/project.py:L250)
- report() (plugin/scripts/sdlc/testing.py:L14)
- Constraints (sdlc/rehearsal-and-band-nits/intent.md:L33)
- release-hook-hardening/intent.md (sdlc/release-hook-hardening/intent.md:L1)
- Intent: Release hook hardening (sdlc/release-hook-hardening/intent.md:L1)
- Proposed outcome (sdlc/release-hook-hardening/intent.md:L12)
- Affected users and systems (sdlc/release-hook-hardening/intent.md:L20)
- Constraints (sdlc/release-hook-hardening/intent.md:L25)
- Open questions (sdlc/release-hook-hardening/intent.md:L31)
- Problem (sdlc/release-hook-hardening/intent.md:L4)
- release-hook-hardening/pr-body.md (sdlc/release-hook-hardening/pr-body.md:L1)
- Release hook hardening (sdlc/release-hook-hardening/pr-body.md:L1)
- Artifacts (sdlc/release-hook-hardening/pr-body.md:L11)
- Proof (sdlc/release-hook-hardening/pr-body.md:L16)
- Why (sdlc/release-hook-hardening/pr-body.md:L3)
- release-hook-hardening/spec.md (sdlc/release-hook-hardening/spec.md:L1)
- Spec: Release hook hardening (sdlc/release-hook-hardening/spec.md:L1)
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
- [config](/modules/config.md)
- [docs.py](/modules/docs-py.md)
- [fail](/modules/fail.md)
- [findings](/modules/findings.md)
- [git](/modules/git.md)
- [hooks.py](/modules/hooks-py.md)
- [project.py](/modules/project-py.md)
- [review](/modules/review.md)
- [status](/modules/status.md)
- [test_hooks.py](/modules/test-hooks-py.md)
- [test_plan_design.py](/modules/test-plan-design-py.md)

# Inferred
- [Blocked](/modules/blocked.md)
- [build](/modules/build.md)
- [config](/modules/config.md)
- [fail](/modules/fail.md)
- [git](/modules/git.md)
- [test_plan_design.py](/modules/test-plan-design-py.md)

# Features
- [graph-selected repomix context packs](/features/graph-selected-repomix-context-packs.md)
