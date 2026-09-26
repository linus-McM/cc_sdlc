---
type: Module
title: Blocked
description: "Graphify community 60: plugin/scripts/sdlc/project.py, sdlc/graphify-and-okf-knowledge-base-integration/spec.md, sdlc/rehearsal-and-band-nits/plan.md, sdlc/rehearsal-and-band-nits/review.md, sdlc/rehe"
resource: ""
tags: [module, graphify]
status: draft
generated: { by: sdlc/0.5.0, at: "2026-09-26T05:22:30Z" }
stale_after: "2026-10-10T05:22:30Z"
source_commit: c5f64f8d3b9b5e3268754f626b7f2e958fd6415e
sources:
  - { id: project, resource: plugin/scripts/sdlc/project.py, last_modified: "2026-09-24T11:36:09+10:00", digest: d1e5536892dbd875 }
  - { id: spec, resource: sdlc/graphify-and-okf-knowledge-base-integration/spec.md, last_modified: "2026-09-09T15:03:27+10:00", digest: 18ddccb80477e245 }
  - { id: plan, resource: sdlc/rehearsal-and-band-nits/plan.md, last_modified: "2026-09-09T15:03:27+10:00", digest: 688912ed38722c04 }
  - { id: review, resource: sdlc/rehearsal-and-band-nits/review.md, last_modified: "2026-09-09T15:03:27+10:00", digest: 370e4dd8c100bf71 }
  - { id: spec, resource: sdlc/rehearsal-and-band-nits/spec.md, last_modified: "2026-09-09T15:03:27+10:00", digest: b81cd9d3882a7703 }
  - { id: test_deploy, resource: tests/test_deploy.py, last_modified: "2026-09-19T23:30:10+10:00", digest: dbfb47118be6302a }
  - { id: test_maintain, resource: tests/test_maintain.py, last_modified: "2026-09-24T11:36:09+10:00", digest: 5e6dbf325688ebe8 }
---

# Files
- `plugin/scripts/sdlc/project.py`
- `sdlc/graphify-and-okf-knowledge-base-integration/spec.md`
- `sdlc/rehearsal-and-band-nits/plan.md`
- `sdlc/rehearsal-and-band-nits/review.md`
- `sdlc/rehearsal-and-band-nits/spec.md`
- `tests/test_deploy.py`
- `tests/test_maintain.py`

# Symbols
- Blocked (plugin/scripts/sdlc/project.py:L83)
- A gate refused; `.verdict` is the JSON dict the CLI prints. (plugin/scripts/sdlc/project.py:L84)
- .__init__() (plugin/scripts/sdlc/project.py:L86)
- Changes to existing behaviour (sdlc/graphify-and-okf-knowledge-base-integration/spec.md:L270)
- rehearsal-and-band-nits/plan.md (sdlc/rehearsal-and-band-nits/plan.md:L1)
- Plan: Rehearsal and band nits (sdlc/rehearsal-and-band-nits/plan.md:L1)
- Order of work (sdlc/rehearsal-and-band-nits/plan.md:L15)
- Files that change (sdlc/rehearsal-and-band-nits/plan.md:L4)
- Risks (sdlc/rehearsal-and-band-nits/plan.md:L43)
- Proof (sdlc/rehearsal-and-band-nits/plan.md:L54)
- rehearsal-and-band-nits/review.md (sdlc/rehearsal-and-band-nits/review.md:L1)
- Review: Rehearsal and band nits (sdlc/rehearsal-and-band-nits/review.md:L1)
- Compliance (sdlc/rehearsal-and-band-nits/review.md:L12)
- Bugs (sdlc/rehearsal-and-band-nits/review.md:L4)
- Security (sdlc/rehearsal-and-band-nits/review.md:L8)
- Proof (sdlc/rehearsal-and-band-nits/spec.md:L26)
- test_deploy_rehearse_needs_git() (tests/test_deploy.py:L66)
- test_deploy_rehearse_reports_leftover_worktree() (tests/test_deploy.py:L72)
- flaky() (tests/test_deploy.py:L75)
- test_deploy_rehearse_runs_at_project_path() (tests/test_deploy.py:L87)
- A project that is a subdirectory of the repo rehearses at that same… (tests/test_deploy.py:L88)
- test_tier_rejects_unknown_side() (tests/test_maintain.py:L28)

# Depends on
- [Order of work](/modules/order-of-work.md)
- [rehearse](/modules/rehearse.md)

# Inferred
- [bash](/modules/bash.md)
- [build.py](/modules/build-py.md)
- [cli.py](/modules/cli-py.md)
- [fail](/modules/fail.md)
- [fill](/modules/fill.md)
- [Order of work](/modules/order-of-work.md)
- [post_edit](/modules/post-edit.md)
- [rehearse](/modules/rehearse.md)
- [test_maintain.py](/modules/test-maintain-py.md)

# Features
- [Dogfood fixes round two](/features/dogfood-fixes-round-two.md)
- [graph-selected repomix context packs](/features/graph-selected-repomix-context-packs.md)
- [Graphify and OKF knowledge base integration](/features/graphify-and-okf-knowledge-base-integration.md)
- [Rehearsal and band nits](/features/rehearsal-and-band-nits.md)
