---
type: Module
title: StepSkipped
description: "Graphify community 10: plugin/scripts/sdlc/artifacts.py, plugin/scripts/sdlc/deploy.py, plugin/scripts/sdlc/knowledge.py, plugin/scripts/sdlc/project.py, sdlc/archify-stage-documentation/plan.md, sdlc"
resource: ""
tags: [module, graphify]
status: draft
generated: { by: sdlc/0.5.0, at: "2026-09-26T06:16:29Z" }
stale_after: "2026-10-10T06:16:29Z"
source_commit: def844e9ac23d4fb2eaffa6f82398a364dfbbac4
sources:
  - { id: artifacts, resource: plugin/scripts/sdlc/artifacts.py, last_modified: "2026-09-09T15:02:31+10:00", digest: 3e063b545e7dd897 }
  - { id: deploy, resource: plugin/scripts/sdlc/deploy.py, last_modified: "2026-09-26T16:06:32+10:00", digest: d2d3493a1ed08434 }
  - { id: knowledge, resource: plugin/scripts/sdlc/knowledge.py, last_modified: "2026-09-26T16:06:32+10:00", digest: 12afb6df19262a3a }
  - { id: project, resource: plugin/scripts/sdlc/project.py, last_modified: "2026-09-26T16:06:32+10:00", digest: 26698ea0d06e1efe }
  - { id: plan, resource: sdlc/archify-stage-documentation/plan.md, last_modified: "2026-09-09T15:03:27+10:00", digest: c94b9c651a152ddc }
  - { id: spec, resource: sdlc/archify-stage-documentation/spec.md, last_modified: "2026-09-09T15:03:27+10:00", digest: 6c2e2d1606d0fe5e }
  - { id: review, resource: sdlc/graphify-and-okf-knowledge-base-integration/review.md, last_modified: "2026-09-09T15:03:27+10:00", digest: b6e15f798eacd1f2 }
  - { id: spec, resource: sdlc/graphify-and-okf-knowledge-base-integration/spec.md, last_modified: "2026-09-09T15:03:27+10:00", digest: 18ddccb80477e245 }
---

# Files
- `plugin/scripts/sdlc/artifacts.py`
- `plugin/scripts/sdlc/deploy.py`
- `plugin/scripts/sdlc/knowledge.py`
- `plugin/scripts/sdlc/project.py`
- `sdlc/archify-stage-documentation/plan.md`
- `sdlc/archify-stage-documentation/spec.md`
- `sdlc/graphify-and-okf-knowledge-base-integration/review.md`
- `sdlc/graphify-and-okf-knowledge-base-integration/spec.md`

# Symbols
- title() (plugin/scripts/sdlc/artifacts.py:L34)
- `# Intent: Claims status` -> `Claims status`. (plugin/scripts/sdlc/artifacts.py:L35)
- knowledge_diff() (plugin/scripts/sdlc/deploy.py:L127)
- `git diff --stat main...HEAD` for the OKF bundle, so reviewers see what the… (plugin/scripts/sdlc/deploy.py:L128)
- pr_body() (plugin/scripts/sdlc/deploy.py:L139)
- write_ignore() (plugin/scripts/sdlc/knowledge.py:L349)
- pointer_present() (plugin/scripts/sdlc/knowledge.py:L368)
- bootstrap() (plugin/scripts/sdlc/knowledge.py:L405)
- behind() (plugin/scripts/sdlc/knowledge.py:L479)
- Commits from `since` to HEAD; None when git cannot resolve `since` (shallow… (plugin/scripts/sdlc/knowledge.py:L480)
- staleness() (plugin/scripts/sdlc/knowledge.py:L487)
- The cheap part of status: how far each index is behind HEAD and why a clean… (plugin/scripts/sdlc/knowledge.py:L488)
- StepSkipped (plugin/scripts/sdlc/project.py:L102)
- This step does not apply here; later steps still run. (plugin/scripts/sdlc/project.py:L103)
- StepFailed (plugin/scripts/sdlc/project.py:L98)
- An install step exited non-zero or left its expected result missing. (plugin/scripts/sdlc/project.py:L99)
- Risks (sdlc/archify-stage-documentation/plan.md:L144)
- Requirements (sdlc/archify-stage-documentation/spec.md:L4)
- graphify-and-okf-knowledge-base-integration/review.md (sdlc/graphify-and-okf-knowledge-base-integration/review.md:L1)
- Review: Graphify and OKF knowledge base integration (sdlc/graphify-and-okf-knowledge-base-integration/review.md:L1)
- Bugs (sdlc/graphify-and-okf-knowledge-base-integration/review.md:L4)
- graphify-and-okf-knowledge-base-integration/spec.md (sdlc/graphify-and-okf-knowledge-base-integration/spec.md:L1)
- Spec: Graphify and OKF knowledge base integration (sdlc/graphify-and-okf-knowledge-base-integration/spec.md:L1)
- Design (sdlc/graphify-and-okf-knowledge-base-integration/spec.md:L136)
- Interfaces (sdlc/graphify-and-okf-knowledge-base-integration/spec.md:L217)
- Concerns (sdlc/graphify-and-okf-knowledge-base-integration/spec.md:L279)
- Open questions (sdlc/graphify-and-okf-knowledge-base-integration/spec.md:L308)
- Requirements (sdlc/graphify-and-okf-knowledge-base-integration/spec.md:L5)

# Depends on
- [artifacts.py](/modules/artifacts-py.md)
- [Blocked](/modules/blocked.md)
- [cfg](/modules/cfg.md)
- [check](/modules/check.md)
- [docs.py](/modules/docs-py.md)
- [git](/modules/git.md)
- [hooks.py](/modules/hooks-py.md)
- [knowledge.py](/modules/knowledge-py.md)
- [Order of work](/modules/order-of-work.md)
- [Path](/modules/path-13.md)
- [pathlib](/modules/pathlib.md)
- [publish](/modules/publish.md)
- [refresh](/modules/refresh.md)

# Inferred
- [Blocked](/modules/blocked.md)
- [cfg](/modules/cfg.md)
- [check](/modules/check.md)
- [conftest.py](/modules/conftest-py.md)
- [docs.py](/modules/docs-py.md)
- [fail](/modules/fail.md)
- [git](/modules/git.md)
- [hooks.py](/modules/hooks-py.md)
- [install_uv](/modules/install-uv.md)
- [Order of work](/modules/order-of-work.md)
- [Path](/modules/path-13.md)
- [post_edit](/modules/post-edit.md)
- [project.py](/modules/project-py.md)
- [publish](/modules/publish.md)
- [refresh](/modules/refresh.md)
- [require](/modules/require.md)

# Features
- [graph-selected repomix context packs](/features/graph-selected-repomix-context-packs.md)
