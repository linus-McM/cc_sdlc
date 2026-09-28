---
type: Module
title: Order of work
description: "Graphify community 44: plugin/scripts/sdlc/project.py, plugin/scripts/sdlc/stages.py, sdlc/status-next-pointer/plan.md, tests/test_plan_design.py"
resource: ""
tags: [module, graphify]
status: draft
generated: { by: sdlc/0.8.1, at: "2026-09-28T22:57:53Z" }
stale_after: "2026-10-12T22:57:53Z"
source_commit: 0754d821fc594b90c529849cddaca10dc6109921
sources:
  - { id: project, resource: plugin/scripts/sdlc/project.py, last_modified: "2026-09-29T08:42:51+10:00", digest: f89b1e9a47bc69d8 }
  - { id: stages, resource: plugin/scripts/sdlc/stages.py, last_modified: "2026-09-26T16:35:55+10:00", digest: 3de65600923a55b5 }
  - { id: plan, resource: sdlc/status-next-pointer/plan.md, last_modified: "2026-09-09T15:03:27+10:00", digest: 0d63041e55ae8191 }
  - { id: test_plan_design, resource: tests/test_plan_design.py, last_modified: "2026-09-26T16:35:55+10:00", digest: 6b8c86fb373332d6 }
---

# Files
- `plugin/scripts/sdlc/project.py`
- `plugin/scripts/sdlc/stages.py`
- `sdlc/status-next-pointer/plan.md`
- `tests/test_plan_design.py`

# Symbols
- write_json() (plugin/scripts/sdlc/project.py:L259)
- Written to a sibling temp file, then renamed into place: a reader never sees… (plugin/scripts/sdlc/project.py:L260)
- next_command() (plugin/scripts/sdlc/stages.py:L24)
- Order of work (sdlc/status-next-pointer/plan.md:L16)
- test_status_next_points_at_first_unaccepted_stage() (tests/test_plan_design.py:L100)
- test_status_next_before_any_acceptance() (tests/test_plan_design.py:L106)
- test_status_next_after_spec() (tests/test_plan_design.py:L111)
- test_status_next_walks_test_deploy_maintain() (tests/test_plan_design.py:L115)

# Depends on
- [Order of work](/modules/order-of-work-8.md)

# Inferred
- [conftest.py](/modules/conftest-py.md)
- [git](/modules/git.md)
- [read_json](/modules/read-json.md)
- [test_plan_design.py](/modules/test-plan-design-py.md)

# Features
- [graph-selected repomix context packs](/features/graph-selected-repomix-context-packs.md)
- [Graphify and OKF knowledge base integration](/features/graphify-and-okf-knowledge-base-integration.md)
- [Status next pointer](/features/status-next-pointer.md)
