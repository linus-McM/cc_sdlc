---
type: Module
title: fill
description: "Graphify community 3: plugin/scripts/sdlc/artifacts.py, plugin/scripts/sdlc/project.py, plugin/scripts/sdlc/stages.py, sdlc/status-next-pointer/plan.md, sdlc/status-next-pointer/spec.md, tests/conftes"
resource: ""
tags: [module, graphify]
status: draft
generated: { by: sdlc/0.5.0, at: "2026-09-25T23:27:53Z" }
stale_after: "2026-10-09T23:27:53Z"
source_commit: 1348ec2a58c87325a8bcaacd936bc4bc9473c870
sources:
  - { id: artifacts, resource: plugin/scripts/sdlc/artifacts.py, last_modified: "2026-09-09T15:02:31+10:00", digest: 3e063b545e7dd897 }
  - { id: project, resource: plugin/scripts/sdlc/project.py, last_modified: "2026-09-24T11:36:09+10:00", digest: d1e5536892dbd875 }
  - { id: stages, resource: plugin/scripts/sdlc/stages.py, last_modified: "2026-09-09T15:02:31+10:00", digest: 79822cdce593996c }
  - { id: plan, resource: sdlc/status-next-pointer/plan.md, last_modified: "2026-09-09T15:03:27+10:00", digest: 0d63041e55ae8191 }
  - { id: spec, resource: sdlc/status-next-pointer/spec.md, last_modified: "2026-09-09T15:03:27+10:00", digest: 21a434a2e5ea4acf }
  - { id: conftest, resource: tests/conftest.py, last_modified: "2026-09-24T11:36:09+10:00", digest: 808a9c4cb9a6aeab }
  - { id: test_checkpoint, resource: tests/test_checkpoint.py, last_modified: "2026-09-24T11:36:09+10:00", digest: 1cc385cfc50735e9 }
  - { id: test_plan_design, resource: tests/test_plan_design.py, last_modified: "2026-09-09T07:52:07+10:00", digest: 0ef824c0b5e9bd38 }
---

# Files
- `plugin/scripts/sdlc/artifacts.py`
- `plugin/scripts/sdlc/project.py`
- `plugin/scripts/sdlc/stages.py`
- `sdlc/status-next-pointer/plan.md`
- `sdlc/status-next-pointer/spec.md`
- `tests/conftest.py`
- `tests/test_checkpoint.py`
- `tests/test_plan_design.py`

# Symbols
- list_items() (plugin/scripts/sdlc/artifacts.py:L79)
- Paths from a bulleted or comma-separated section body, annotations stripped. (plugin/scripts/sdlc/artifacts.py:L80)
- write_json() (plugin/scripts/sdlc/project.py:L256)
- next_command() (plugin/scripts/sdlc/stages.py:L23)
- status-next-pointer/plan.md (sdlc/status-next-pointer/plan.md:L1)
- Plan: Status next pointer (sdlc/status-next-pointer/plan.md:L1)
- Order of work (sdlc/status-next-pointer/plan.md:L16)
- Files that change (sdlc/status-next-pointer/plan.md:L4)
- Risks (sdlc/status-next-pointer/plan.md:L44)
- Proof (sdlc/status-next-pointer/plan.md:L52)
- Proof (sdlc/status-next-pointer/spec.md:L32)
- fill() (tests/conftest.py:L47)
- Replace placeholder bodies under named sections with real text. (tests/conftest.py:L48)
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
- test_plan_new_refuses_duplicate() (tests/test_plan_design.py:L25)
- test_plan_check_fails_on_placeholders_then_passes() (tests/test_plan_design.py:L30)
- test_plan_accept_requires_valid_intent_and_sets_status() (tests/test_plan_design.py:L46)
- test_design_gate_blocks_until_intent_accepted() (tests/test_plan_design.py:L64)
- test_design_new_blocked_without_accepted_intent() (tests/test_plan_design.py:L72)
- test_design_accept_flow() (tests/test_plan_design.py:L78)
- test_plan_new_creates_intent_from_template() (tests/test_plan_design.py:L8)
- test_status_reports_stage_progress() (tests/test_plan_design.py:L92)

# Depends on
- [hooks.py](/modules/hooks-py.md)
- [Order of work](/modules/order-of-work.md)
- [project.py](/modules/project-py.md)
- [test_build_test.py](/modules/test-build-test-py.md)
- [test_maintain.py](/modules/test-maintain-py.md)

# Inferred
- [fail](/modules/fail.md)
- [Order of work](/modules/order-of-work.md)
- [read_json](/modules/read-json.md)
- [watch](/modules/watch.md)

# Features
- [Archify stage documentation](/features/archify-stage-documentation.md)
- [Graphify and OKF knowledge base integration](/features/graphify-and-okf-knowledge-base-integration.md)
- [Status next pointer](/features/status-next-pointer.md)
