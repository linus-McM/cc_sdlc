---
type: Module
title: Blocked
description: "Graphify community 14: plugin/scripts/sdlc/cli.py, plugin/scripts/sdlc/project.py, plugin/scripts/sdlc/testing.py, sdlc/graphify-and-okf-knowledge-base-integration/plan.md, sdlc/graphify-and-okf-knowl"
resource: ""
tags: [module, graphify]
status: draft
generated: { by: sdlc/0.5.0, at: "2026-09-26T06:33:18Z" }
stale_after: "2026-10-10T06:33:18Z"
source_commit: 5c45a37edd0dc635576e390a1174bea9fad6d10b
sources:
  - { id: cli, resource: plugin/scripts/sdlc/cli.py, last_modified: "2026-09-26T16:06:32+10:00", digest: 87213d99f94df3bf }
  - { id: project, resource: plugin/scripts/sdlc/project.py, last_modified: "2026-09-26T16:06:32+10:00", digest: 26698ea0d06e1efe }
  - { id: testing, resource: plugin/scripts/sdlc/testing.py, last_modified: "2026-09-26T15:51:45+10:00", digest: 68b187c7a3220c0b }
  - { id: plan, resource: sdlc/graphify-and-okf-knowledge-base-integration/plan.md, last_modified: "2026-09-09T15:03:27+10:00", digest: 31d2c88298eefdb1 }
  - { id: spec, resource: sdlc/graphify-and-okf-knowledge-base-integration/spec.md, last_modified: "2026-09-09T15:03:27+10:00", digest: 18ddccb80477e245 }
  - { id: review, resource: sdlc/rehearsal-and-band-nits/review.md, last_modified: "2026-09-09T15:03:27+10:00", digest: 370e4dd8c100bf71 }
---

# Files
- `plugin/scripts/sdlc/cli.py`
- `plugin/scripts/sdlc/project.py`
- `plugin/scripts/sdlc/testing.py`
- `sdlc/graphify-and-okf-knowledge-base-integration/plan.md`
- `sdlc/graphify-and-okf-knowledge-base-integration/spec.md`
- `sdlc/rehearsal-and-band-nits/review.md`

# Symbols
- parser() (plugin/scripts/sdlc/cli.py:L64)
- main() (plugin/scripts/sdlc/cli.py:L80)
- read_jsonl() (plugin/scripts/sdlc/project.py:L240)
- Blocked (plugin/scripts/sdlc/project.py:L86)
- A gate refused; `.verdict` is the JSON dict the CLI prints. (plugin/scripts/sdlc/project.py:L87)
- .__init__() (plugin/scripts/sdlc/project.py:L89)
- run() (plugin/scripts/sdlc/testing.py:L18)
- knowledge_result() (plugin/scripts/sdlc/testing.py:L42)
- The OKF conformance check as one more feedback-loop row; only conformance… (plugin/scripts/sdlc/testing.py:L43)
- Risks (sdlc/graphify-and-okf-knowledge-base-integration/plan.md:L206)
- Changes to existing behaviour (sdlc/graphify-and-okf-knowledge-base-integration/spec.md:L270)
- rehearsal-and-band-nits/review.md (sdlc/rehearsal-and-band-nits/review.md:L1)
- Review: Rehearsal and band nits (sdlc/rehearsal-and-band-nits/review.md:L1)
- Compliance (sdlc/rehearsal-and-band-nits/review.md:L12)
- Security (sdlc/rehearsal-and-band-nits/review.md:L8)

# Depends on
- [build.py](/modules/build-py.md)
- [config](/modules/config.md)
- [fail](/modules/fail.md)
- [hooks.py](/modules/hooks-py.md)
- [Order of work](/modules/order-of-work-25.md)
- [project.py](/modules/project-py.md)
- [refresh](/modules/refresh.md)
- [test_plan_design.py](/modules/test-plan-design-py.md)

# Inferred
- [check](/modules/check.md)
- [conftest.py](/modules/conftest-py.md)
- [fail](/modules/fail.md)
- [hooks.py](/modules/hooks-py.md)
- [install_hook](/modules/install-hook.md)
- [test_hooks.py](/modules/test-hooks-py.md)
- [watch](/modules/watch.md)

# Features
- [graph-selected repomix context packs](/features/graph-selected-repomix-context-packs.md)
