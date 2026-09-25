---
type: Module
title: Requirements
description: "Graphify community 10: plugin/scripts/sdlc/deploy.py, plugin/scripts/sdlc/hooks.py, plugin/scripts/sdlc/knowledge.py, sdlc/graphify-and-okf-knowledge-base-integration/review.md, sdlc/graphify-and-okf-"
resource: ""
tags: [module, graphify]
status: draft
generated: { by: sdlc/0.5.0, at: "2026-09-25T23:27:53Z" }
stale_after: "2026-10-09T23:27:53Z"
source_commit: 1348ec2a58c87325a8bcaacd936bc4bc9473c870
sources:
  - { id: deploy, resource: plugin/scripts/sdlc/deploy.py, last_modified: "2026-09-24T11:36:09+10:00", digest: 99b508f60ff0691d }
  - { id: hooks, resource: plugin/scripts/sdlc/hooks.py, last_modified: "2026-09-19T13:08:30+10:00", digest: 40334c1872956197 }
  - { id: knowledge, resource: plugin/scripts/sdlc/knowledge.py, last_modified: "2026-09-09T15:02:31+10:00", digest: 9f4a8d0ccc4c7375 }
  - { id: review, resource: sdlc/graphify-and-okf-knowledge-base-integration/review.md, last_modified: "2026-09-09T15:03:27+10:00", digest: b6e15f798eacd1f2 }
  - { id: spec, resource: sdlc/graphify-and-okf-knowledge-base-integration/spec.md, last_modified: "2026-09-09T15:03:27+10:00", digest: 18ddccb80477e245 }
---

# Files
- `plugin/scripts/sdlc/deploy.py`
- `plugin/scripts/sdlc/hooks.py`
- `plugin/scripts/sdlc/knowledge.py`
- `sdlc/graphify-and-okf-knowledge-base-integration/review.md`
- `sdlc/graphify-and-okf-knowledge-base-integration/spec.md`

# Symbols
- knowledge_diff() (plugin/scripts/sdlc/deploy.py:L122)
- `git diff --stat main...HEAD` for the OKF bundle, so reviewers see what the… (plugin/scripts/sdlc/deploy.py:L123)
- post_bash() (plugin/scripts/sdlc/hooks.py:L148)
- After a commit: say when an index has fallen further behind than the configured… (plugin/scripts/sdlc/hooks.py:L149)
- enabled() (plugin/scripts/sdlc/knowledge.py:L159)
- behind() (plugin/scripts/sdlc/knowledge.py:L475)
- Commits from `since` to HEAD; None when git cannot resolve `since` (shallow… (plugin/scripts/sdlc/knowledge.py:L476)
- graphify-and-okf-knowledge-base-integration/review.md (sdlc/graphify-and-okf-knowledge-base-integration/review.md:L1)
- Review: Graphify and OKF knowledge base integration (sdlc/graphify-and-okf-knowledge-base-integration/review.md:L1)
- Bugs (sdlc/graphify-and-okf-knowledge-base-integration/review.md:L4)
- graphify-and-okf-knowledge-base-integration/spec.md (sdlc/graphify-and-okf-knowledge-base-integration/spec.md:L1)
- Spec: Graphify and OKF knowledge base integration (sdlc/graphify-and-okf-knowledge-base-integration/spec.md:L1)
- Concerns (sdlc/graphify-and-okf-knowledge-base-integration/spec.md:L279)
- Open questions (sdlc/graphify-and-okf-knowledge-base-integration/spec.md:L308)
- Requirements (sdlc/graphify-and-okf-knowledge-base-integration/spec.md:L5)

# Depends on
- [config](/modules/config.md)
- [install_hook](/modules/install-hook.md)
- [Order of work](/modules/order-of-work-5.md)
- [Path](/modules/path.md)
- [post_edit](/modules/post-edit.md)
- [refresh](/modules/refresh.md)
- [test_hooks.py](/modules/test-hooks-py.md)
- [watch](/modules/watch.md)

# Inferred
- [artifacts.py](/modules/artifacts-py.md)
- [Blocked](/modules/blocked.md)
- [docs.py](/modules/docs-py.md)
- [knowledge.py](/modules/knowledge-py.md)
- [Order of work](/modules/order-of-work.md)
- [Order of work](/modules/order-of-work-5.md)
- [Path](/modules/path.md)
- [post_edit](/modules/post-edit.md)
- [read_json](/modules/read-json.md)
- [refresh](/modules/refresh.md)
- [StepSkipped](/modules/stepskipped.md)
- [test_deploy.py](/modules/test-deploy-py.md)

# Features
- no feature plan names these files
