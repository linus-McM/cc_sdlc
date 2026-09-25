---
type: Module
title: status
description: "Graphify community 10: plugin/scripts/sdlc/deploy.py, plugin/scripts/sdlc/knowledge.py, sdlc/graphify-and-okf-knowledge-base-integration/review.md, sdlc/graphify-and-okf-knowledge-base-integration/spe"
resource: ""
tags: [module, graphify]
status: draft
generated: { by: sdlc/0.5.0, at: "2026-09-25T07:29:30Z" }
stale_after: "2026-10-09T07:29:30Z"
source_commit: dc32a5b78bc303376f02bfe7d43360ae82fa4a82
sources:
  - { id: deploy, resource: plugin/scripts/sdlc/deploy.py, last_modified: "2026-09-24T11:36:09+10:00", digest: 99b508f60ff0691d }
  - { id: knowledge, resource: plugin/scripts/sdlc/knowledge.py, last_modified: "2026-09-09T15:02:31+10:00", digest: 9f4a8d0ccc4c7375 }
  - { id: review, resource: sdlc/graphify-and-okf-knowledge-base-integration/review.md, last_modified: "2026-09-09T15:03:27+10:00", digest: b6e15f798eacd1f2 }
  - { id: spec, resource: sdlc/graphify-and-okf-knowledge-base-integration/spec.md, last_modified: "2026-09-09T15:03:27+10:00", digest: 18ddccb80477e245 }
---

# Files
- `plugin/scripts/sdlc/deploy.py`
- `plugin/scripts/sdlc/knowledge.py`
- `sdlc/graphify-and-okf-knowledge-base-integration/review.md`
- `sdlc/graphify-and-okf-knowledge-base-integration/spec.md`

# Symbols
- knowledge_diff() (plugin/scripts/sdlc/deploy.py:L122)
- `git diff --stat main...HEAD` for the OKF bundle, so reviewers see what the… (plugin/scripts/sdlc/deploy.py:L123)
- enabled() (plugin/scripts/sdlc/knowledge.py:L159)
- cfg() (plugin/scripts/sdlc/knowledge.py:L174)
- The [knowledge] table; `bundle` is validated here because it becomes a path, a… (plugin/scripts/sdlc/knowledge.py:L175)
- shell_word() (plugin/scripts/sdlc/knowledge.py:L183)
- `text` as one double-quoted POSIX shell word: backslash, double quote, dollar… (plugin/scripts/sdlc/knowledge.py:L184)
- bootstrap() (plugin/scripts/sdlc/knowledge.py:L403)
- rebuild_log_tail() (plugin/scripts/sdlc/knowledge.py:L447)
- Last line of Graphify's rebuild log, read from its tail only (the log is… (plugin/scripts/sdlc/knowledge.py:L448)
- artifacts_agree() (plugin/scripts/sdlc/knowledge.py:L459)
- behind() (plugin/scripts/sdlc/knowledge.py:L475)
- Commits from `since` to HEAD; None when git cannot resolve `since` (shallow… (plugin/scripts/sdlc/knowledge.py:L476)
- staleness() (plugin/scripts/sdlc/knowledge.py:L483)
- The cheap part of status: how far each index is behind HEAD and why a clean… (plugin/scripts/sdlc/knowledge.py:L484)
- status() (plugin/scripts/sdlc/knowledge.py:L520)
- signature() (plugin/scripts/sdlc/knowledge.py:L802)
- Content identity: the builder's keys (present on either side) plus the body;… (plugin/scripts/sdlc/knowledge.py:L803)
- graphify-and-okf-knowledge-base-integration/review.md (sdlc/graphify-and-okf-knowledge-base-integration/review.md:L1)
- Review: Graphify and OKF knowledge base integration (sdlc/graphify-and-okf-knowledge-base-integration/review.md:L1)
- Compliance (sdlc/graphify-and-okf-knowledge-base-integration/review.md:L16)
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
- [Components](/modules/components.md)
- [docs.py](/modules/docs-py.md)
- [fail](/modules/fail.md)
- [knowledge.py](/modules/knowledge-py.md)
- [Order of work](/modules/order-of-work.md)
- [Order of work](/modules/order-of-work-5.md)
- [Path](/modules/path.md)
- [project.py](/modules/project-py.md)
- [refresh](/modules/refresh.md)
- [rehearse](/modules/rehearse.md)

# Inferred
- [artifacts.py](/modules/artifacts-py.md)
- [Blocked](/modules/blocked.md)
- [deploy.py](/modules/deploy-py.md)
- [docs.py](/modules/docs-py.md)
- [fail](/modules/fail.md)
- [knowledge.py](/modules/knowledge-py.md)
- [Order of work](/modules/order-of-work.md)
- [Order of work](/modules/order-of-work-5.md)
- [Path](/modules/path.md)
- [pathlib](/modules/pathlib.md)
- [refresh](/modules/refresh.md)
- [test_hooks.py](/modules/test-hooks-py.md)

# Features
- no feature plan names these files
