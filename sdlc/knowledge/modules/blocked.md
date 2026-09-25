---
type: Module
title: Blocked
description: "Graphify community 6: plugin/scripts/sdlc/deploy.py, plugin/scripts/sdlc/hooks.py, plugin/scripts/sdlc/project.py, sdlc/dogfood-fixes-round-two/intent.md, sdlc/dogfood-fixes-round-two/pr-body.md, sdlc"
resource: ""
tags: [module, graphify]
status: draft
generated: { by: sdlc/0.5.0, at: "2026-09-25T07:29:30Z" }
stale_after: "2026-10-09T07:29:30Z"
source_commit: dc32a5b78bc303376f02bfe7d43360ae82fa4a82
sources:
  - { id: deploy, resource: plugin/scripts/sdlc/deploy.py, last_modified: "2026-09-24T11:36:09+10:00", digest: 99b508f60ff0691d }
  - { id: hooks, resource: plugin/scripts/sdlc/hooks.py, last_modified: "2026-09-19T13:08:30+10:00", digest: 40334c1872956197 }
  - { id: project, resource: plugin/scripts/sdlc/project.py, last_modified: "2026-09-24T11:36:09+10:00", digest: d1e5536892dbd875 }
  - { id: intent, resource: sdlc/dogfood-fixes-round-two/intent.md, last_modified: "2026-09-09T15:03:27+10:00", digest: 5054c3634f2f4d06 }
  - { id: pr-body, resource: sdlc/dogfood-fixes-round-two/pr-body.md, last_modified: "2026-09-09T15:03:27+10:00", digest: dca1d4fe8f9a673a }
  - { id: spec, resource: sdlc/dogfood-fixes-round-two/spec.md, last_modified: "2026-09-09T15:03:27+10:00", digest: 79ecdc49d82b1fc2 }
  - { id: review, resource: sdlc/rehearsal-and-band-nits/review.md, last_modified: "2026-09-09T15:03:27+10:00", digest: 370e4dd8c100bf71 }
---

# Files
- `plugin/scripts/sdlc/deploy.py`
- `plugin/scripts/sdlc/hooks.py`
- `plugin/scripts/sdlc/project.py`
- `sdlc/dogfood-fixes-round-two/intent.md`
- `sdlc/dogfood-fixes-round-two/pr-body.md`
- `sdlc/dogfood-fixes-round-two/spec.md`
- `sdlc/rehearsal-and-band-nits/review.md`

# Symbols
- gated() (plugin/scripts/sdlc/deploy.py:L45)
- Environments at the `gate` tier in a `[deploy]` config table. (plugin/scripts/sdlc/deploy.py:L46)
- hooks.py (plugin/scripts/sdlc/hooks.py:L1)
- Deterministic guardrails. Invoked by hooks/hooks.json: `hook.py <event>` with… (plugin/scripts/sdlc/hooks.py:L1)
- pre_bash() (plugin/scripts/sdlc/hooks.py:L121)
- post_edit() (plugin/scripts/sdlc/hooks.py:L130)
- is_commit() (plugin/scripts/sdlc/hooks.py:L143)
- post_bash() (plugin/scripts/sdlc/hooks.py:L148)
- After a commit: say when an index has fallen further behind than the configured… (plugin/scripts/sdlc/hooks.py:L149)
- session_start() (plugin/scripts/sdlc/hooks.py:L159)
- Session report: the workflow env merge, then the knowledge bootstrap (check-… (plugin/scripts/sdlc/hooks.py:L160)
- workflow_note() (plugin/scripts/sdlc/hooks.py:L165)
- knowledge_note() (plugin/scripts/sdlc/hooks.py:L174)
- main() (plugin/scripts/sdlc/hooks.py:L195)
- deny() (plugin/scripts/sdlc/hooks.py:L26)
- context() (plugin/scripts/sdlc/hooks.py:L36)
- rel_path() (plugin/scripts/sdlc/hooks.py:L40)
- active_feature() (plugin/scripts/sdlc/hooks.py:L53)
- pre_edit() (plugin/scripts/sdlc/hooks.py:L60)
- Blocked (plugin/scripts/sdlc/project.py:L83)
- A gate refused; `.verdict` is the JSON dict the CLI prints. (plugin/scripts/sdlc/project.py:L84)
- .__init__() (plugin/scripts/sdlc/project.py:L86)
- dogfood-fixes-round-two/intent.md (sdlc/dogfood-fixes-round-two/intent.md:L1)
- Intent: Dogfood fixes round two (sdlc/dogfood-fixes-round-two/intent.md:L1)
- Proposed outcome (sdlc/dogfood-fixes-round-two/intent.md:L14)
- Constraints (sdlc/dogfood-fixes-round-two/intent.md:L26)
- Open questions (sdlc/dogfood-fixes-round-two/intent.md:L31)
- Problem (sdlc/dogfood-fixes-round-two/intent.md:L4)
- dogfood-fixes-round-two/pr-body.md (sdlc/dogfood-fixes-round-two/pr-body.md:L1)
- Dogfood fixes round two (sdlc/dogfood-fixes-round-two/pr-body.md:L1)
- Artifacts (sdlc/dogfood-fixes-round-two/pr-body.md:L13)
- Proof (sdlc/dogfood-fixes-round-two/pr-body.md:L18)
- Why (sdlc/dogfood-fixes-round-two/pr-body.md:L3)
- Requirements (sdlc/dogfood-fixes-round-two/spec.md:L4)
- rehearsal-and-band-nits/review.md (sdlc/rehearsal-and-band-nits/review.md:L1)
- Review: Rehearsal and band nits (sdlc/rehearsal-and-band-nits/review.md:L1)
- Compliance (sdlc/rehearsal-and-band-nits/review.md:L12)
- Bugs (sdlc/rehearsal-and-band-nits/review.md:L4)
- Security (sdlc/rehearsal-and-band-nits/review.md:L8)

# Depends on
- [artifacts.py](/modules/artifacts-py.md)
- [deploy.py](/modules/deploy-py.md)
- [fail](/modules/fail.md)
- [__init__.py](/modules/init-py.md)
- [knowledge.py](/modules/knowledge-py.md)
- [Path](/modules/path.md)
- [pathlib](/modules/pathlib.md)
- [project.py](/modules/project-py.md)
- [rehearse](/modules/rehearse.md)
- [status](/modules/status.md)
- [test_build_test.py](/modules/test-build-test-py.md)
- [test_hooks.py](/modules/test-hooks-py.md)
- [watch](/modules/watch.md)

# Inferred
- [Order of work](/modules/order-of-work.md)
- [rehearse](/modules/rehearse.md)
- [test_hooks.py](/modules/test-hooks-py.md)
- [watch](/modules/watch.md)

# Features
- no feature plan names these files
