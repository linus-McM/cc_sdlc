---
type: Module
title: test_plan_design.py
description: "Graphify community 3: plugin/scripts/sdlc/project.py, plugin/scripts/sdlc/stages.py, sdlc/status-next-pointer/plan.md, sdlc/status-next-pointer/spec.md, tests/conftest.py, tests/test_checkpoint.py, te"
resource: ""
tags: [module, graphify]
status: draft
generated: { by: sdlc/0.5.0, at: "2026-09-26T06:33:18Z" }
stale_after: "2026-10-10T06:33:18Z"
source_commit: 5c45a37edd0dc635576e390a1174bea9fad6d10b
sources:
  - { id: project, resource: plugin/scripts/sdlc/project.py, last_modified: "2026-09-26T16:06:32+10:00", digest: 26698ea0d06e1efe }
  - { id: stages, resource: plugin/scripts/sdlc/stages.py, last_modified: "2026-09-26T16:06:32+10:00", digest: 3de65600923a55b5 }
  - { id: plan, resource: sdlc/status-next-pointer/plan.md, last_modified: "2026-09-09T15:03:27+10:00", digest: 0d63041e55ae8191 }
  - { id: spec, resource: sdlc/status-next-pointer/spec.md, last_modified: "2026-09-09T15:03:27+10:00", digest: 21a434a2e5ea4acf }
  - { id: conftest, resource: tests/conftest.py, last_modified: "2026-09-26T16:23:50+10:00", digest: 44de9d075d1ea218 }
  - { id: test_checkpoint, resource: tests/test_checkpoint.py, last_modified: "2026-09-24T11:36:09+10:00", digest: 1cc385cfc50735e9 }
  - { id: test_plan_design, resource: tests/test_plan_design.py, last_modified: "2026-09-26T16:06:32+10:00", digest: 6b8c86fb373332d6 }
---

# Files
- `plugin/scripts/sdlc/project.py`
- `plugin/scripts/sdlc/stages.py`
- `sdlc/status-next-pointer/plan.md`
- `sdlc/status-next-pointer/spec.md`
- `tests/conftest.py`
- `tests/test_checkpoint.py`
- `tests/test_plan_design.py`

# Symbols
- write_json() (plugin/scripts/sdlc/project.py:L259)
- Written to a sibling temp file, then renamed into place: a reader never sees… (plugin/scripts/sdlc/project.py:L260)
- next_command() (plugin/scripts/sdlc/stages.py:L24)
- Order of work (sdlc/status-next-pointer/plan.md:L16)
- Proof (sdlc/status-next-pointer/spec.md:L32)
- fill() (tests/conftest.py:L49)
- Replace placeholder bodies under named sections with real text. (tests/conftest.py:L50)
- test_checkpoint.py (tests/test_checkpoint.py:L1)
- Stage-boundary checkpoints: every accepted artifact lands in its own commit. (tests/test_checkpoint.py:L1)
- test_a_failed_commit_never_fails_the_stage() (tests/test_checkpoint.py:L104)
- test_a_merge_in_progress_defers_the_checkpoint() (tests/test_checkpoint.py:L114)
- subjects() (tests/test_checkpoint.py:L12)
- files_in() (tests/test_checkpoint.py:L16)
- test_plan_accept_commits_the_intent() (tests/test_checkpoint.py:L20)
- test_each_accept_is_its_own_commit() (tests/test_checkpoint.py:L26)
- test_extra_generated_files_ride_along_and_are_counted() (tests/test_checkpoint.py:L34)
- test_source_changes_are_never_swept_in() (tests/test_checkpoint.py:L43)
- test_staged_unrelated_work_stays_staged() (tests/test_checkpoint.py:L52)
- test_review_deploy_and_maintain_are_boundaries() (tests/test_checkpoint.py:L62)
- test_propose_commits_the_next_intent() (tests/test_checkpoint.py:L76)
- test_nothing_to_commit_is_not_an_error() (tests/test_checkpoint.py:L84)
- test_layer_off_never_commits() (tests/test_checkpoint.py:L91)
- test_config_can_disable_the_layer() (tests/test_checkpoint.py:L96)
- test_plan_design.py (tests/test_plan_design.py:L1)
- test_status_next_points_at_first_unaccepted_stage() (tests/test_plan_design.py:L100)
- test_status_next_before_any_acceptance() (tests/test_plan_design.py:L106)
- test_status_next_after_spec() (tests/test_plan_design.py:L111)
- test_status_next_walks_test_deploy_maintain() (tests/test_plan_design.py:L115)
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
- [Order of work](/modules/order-of-work-8.md)
- [pathlib](/modules/pathlib.md)
- [project.py](/modules/project-py.md)

# Inferred
- [check](/modules/check.md)
- [conftest.py](/modules/conftest-py.md)
- [fail](/modules/fail.md)
- [git](/modules/git.md)

# Features
- [Archify stage documentation](/features/archify-stage-documentation.md)
- [graph-selected repomix context packs](/features/graph-selected-repomix-context-packs.md)
- [Graphify and OKF knowledge base integration](/features/graphify-and-okf-knowledge-base-integration.md)
- [Status next pointer](/features/status-next-pointer.md)
