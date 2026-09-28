---
type: Module
title: test_plan_design.py
description: "Graphify community 3: sdlc/status-next-pointer/spec.md, tests/test_plan_design.py"
resource: ""
tags: [module, graphify]
status: draft
generated: { by: sdlc/0.8.1, at: "2026-09-28T22:57:53Z" }
stale_after: "2026-10-12T22:57:53Z"
source_commit: 0754d821fc594b90c529849cddaca10dc6109921
sources:
  - { id: spec, resource: sdlc/status-next-pointer/spec.md, last_modified: "2026-09-09T15:03:27+10:00", digest: 21a434a2e5ea4acf }
  - { id: test_plan_design, resource: tests/test_plan_design.py, last_modified: "2026-09-26T16:35:55+10:00", digest: 6b8c86fb373332d6 }
---

# Files
- `sdlc/status-next-pointer/spec.md`
- `tests/test_plan_design.py`

# Symbols
- Proof (sdlc/status-next-pointer/spec.md:L32)
- test_plan_design.py (tests/test_plan_design.py:L1)
- test_status_next_agrees_with_deploy_gate_on_failed_report() (tests/test_plan_design.py:L128)
- test_status_reports_corrupt_json_as_verdict_not_traceback() (tests/test_plan_design.py:L134)
- test_accept_publishes_feature_concept() (tests/test_plan_design.py:L141)
- planned_with_graph() (tests/test_plan_design.py:L157)
- A filled intent naming `src/web/api.py`, sources committed, graph.json fresh at… (tests/test_plan_design.py:L158)
- test_plan_accept_needs_a_pack_at_head() (tests/test_plan_design.py:L164)
- test_plan_accept_needs_repomix() (tests/test_plan_design.py:L177)
- test_plan_gate_skipped_visibly_when_off() (tests/test_plan_design.py:L184)
- test_plan_new_refuses_duplicate() (tests/test_plan_design.py:L25)
- test_plan_check_fails_on_placeholders_then_passes() (tests/test_plan_design.py:L30)
- test_plan_accept_requires_valid_intent_and_sets_status() (tests/test_plan_design.py:L46)
- test_design_gate_blocks_until_intent_accepted() (tests/test_plan_design.py:L64)
- test_design_new_blocked_without_accepted_intent() (tests/test_plan_design.py:L72)
- test_design_accept_flow() (tests/test_plan_design.py:L78)
- test_plan_new_creates_intent_from_template() (tests/test_plan_design.py:L8)
- test_status_reports_stage_progress() (tests/test_plan_design.py:L92)

# Depends on
- [conftest.py](/modules/conftest-py.md)
- [Order of work](/modules/order-of-work-44.md)
- [Order of work](/modules/order-of-work-8.md)
- [pathlib](/modules/pathlib.md)
- [project.py](/modules/project-py.md)

# Inferred
- [read_json](/modules/read-json.md)

# Features
- [graph-selected repomix context packs](/features/graph-selected-repomix-context-packs.md)
- [Graphify and OKF knowledge base integration](/features/graphify-and-okf-knowledge-base-integration.md)
- [Status next pointer](/features/status-next-pointer.md)
