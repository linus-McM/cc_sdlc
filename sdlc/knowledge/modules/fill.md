---
type: Module
title: fill
description: "Graphify community 3: plugin/scripts/sdlc/artifacts.py, plugin/scripts/sdlc/deploy.py, plugin/scripts/sdlc/project.py, plugin/scripts/sdlc/stages.py, plugin/scripts/sdlc/testing.py, sdlc/status-next-p"
resource: ""
tags: [module, graphify]
status: draft
generated: { by: sdlc/0.5.0, at: "2026-09-26T05:22:30Z" }
stale_after: "2026-10-10T05:22:30Z"
source_commit: c5f64f8d3b9b5e3268754f626b7f2e958fd6415e
sources:
  - { id: artifacts, resource: plugin/scripts/sdlc/artifacts.py, last_modified: "2026-09-09T15:02:31+10:00", digest: 3e063b545e7dd897 }
  - { id: deploy, resource: plugin/scripts/sdlc/deploy.py, last_modified: "2026-09-24T11:36:09+10:00", digest: 99b508f60ff0691d }
  - { id: project, resource: plugin/scripts/sdlc/project.py, last_modified: "2026-09-24T11:36:09+10:00", digest: d1e5536892dbd875 }
  - { id: stages, resource: plugin/scripts/sdlc/stages.py, last_modified: "2026-09-09T15:02:31+10:00", digest: 79822cdce593996c }
  - { id: testing, resource: plugin/scripts/sdlc/testing.py, last_modified: "2026-09-24T11:36:09+10:00", digest: f854f76e33b9b57e }
  - { id: plan, resource: sdlc/status-next-pointer/plan.md, last_modified: "2026-09-09T15:03:27+10:00", digest: 0d63041e55ae8191 }
  - { id: review, resource: sdlc/status-next-pointer/review.md, last_modified: "2026-09-09T15:03:27+10:00", digest: f6fa7c95be7b4059 }
  - { id: spec, resource: sdlc/status-next-pointer/spec.md, last_modified: "2026-09-09T15:03:27+10:00", digest: 21a434a2e5ea4acf }
  - { id: conftest, resource: tests/conftest.py, last_modified: "2026-09-24T11:36:09+10:00", digest: 808a9c4cb9a6aeab }
  - { id: test_checkpoint, resource: tests/test_checkpoint.py, last_modified: "2026-09-24T11:36:09+10:00", digest: 1cc385cfc50735e9 }
  - { id: test_plan_design, resource: tests/test_plan_design.py, last_modified: "2026-09-09T07:52:07+10:00", digest: 0ef824c0b5e9bd38 }
---

# Files
- `plugin/scripts/sdlc/artifacts.py`
- `plugin/scripts/sdlc/deploy.py`
- `plugin/scripts/sdlc/project.py`
- `plugin/scripts/sdlc/stages.py`
- `plugin/scripts/sdlc/testing.py`
- `sdlc/status-next-pointer/plan.md`
- `sdlc/status-next-pointer/review.md`
- `sdlc/status-next-pointer/spec.md`
- `tests/conftest.py`
- `tests/test_checkpoint.py`
- `tests/test_plan_design.py`

# Symbols
- list_items() (plugin/scripts/sdlc/artifacts.py:L79)
- Paths from a bulleted or comma-separated section body, annotations stripped. (plugin/scripts/sdlc/artifacts.py:L80)
- knowledge_diff() (plugin/scripts/sdlc/deploy.py:L122)
- `git diff --stat main...HEAD` for the OKF bundle, so reviewers see what the… (plugin/scripts/sdlc/deploy.py:L123)
- pr_body() (plugin/scripts/sdlc/deploy.py:L134)
- state() (plugin/scripts/sdlc/deploy.py:L17)
- released() (plugin/scripts/sdlc/deploy.py:L21)
- readiness() (plugin/scripts/sdlc/deploy.py:L25)
- Reasons the feature is not ready for any environment; empty when ready. (plugin/scripts/sdlc/deploy.py:L26)
- read_json() (plugin/scripts/sdlc/project.py:L247)
- write_json() (plugin/scripts/sdlc/project.py:L256)
- next_command() (plugin/scripts/sdlc/stages.py:L23)
- report() (plugin/scripts/sdlc/testing.py:L14)
- count() (plugin/scripts/sdlc/testing.py:L50)
- Findings tagged `- Important:` / `- Nit:` in a review.md body. (plugin/scripts/sdlc/testing.py:L51)
- findings() (plugin/scripts/sdlc/testing.py:L55)
- review.md validated against REVIEW.md's three passes, with its finding counts. (plugin/scripts/sdlc/testing.py:L56)
- status-next-pointer/plan.md (sdlc/status-next-pointer/plan.md:L1)
- Plan: Status next pointer (sdlc/status-next-pointer/plan.md:L1)
- Order of work (sdlc/status-next-pointer/plan.md:L16)
- Files that change (sdlc/status-next-pointer/plan.md:L4)
- Risks (sdlc/status-next-pointer/plan.md:L44)
- Proof (sdlc/status-next-pointer/plan.md:L52)
- status-next-pointer/review.md (sdlc/status-next-pointer/review.md:L1)
- Review: Status next pointer (sdlc/status-next-pointer/review.md:L1)
- Compliance (sdlc/status-next-pointer/review.md:L11)
- Bugs (sdlc/status-next-pointer/review.md:L4)
- Security (sdlc/status-next-pointer/review.md:L8)
- status-next-pointer/spec.md (sdlc/status-next-pointer/spec.md:L1)
- Spec: Status next pointer (sdlc/status-next-pointer/spec.md:L1)
- Design (sdlc/status-next-pointer/spec.md:L13)
- Concerns (sdlc/status-next-pointer/spec.md:L26)
- Open questions (sdlc/status-next-pointer/spec.md:L29)
- Proof (sdlc/status-next-pointer/spec.md:L32)
- Requirements (sdlc/status-next-pointer/spec.md:L4)
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
- [bootstrap](/modules/bootstrap.md)
- [fail](/modules/fail.md)
- [Order of work](/modules/order-of-work.md)
- [Path](/modules/path.md)
- [pathlib](/modules/pathlib.md)
- [project.py](/modules/project-py.md)
- [refresh](/modules/refresh.md)
- [rehearse](/modules/rehearse.md)
- [test_build_test.py](/modules/test-build-test-py.md)
- [test_maintain.py](/modules/test-maintain-py.md)

# Inferred
- [Blocked](/modules/blocked.md)
- [Order of work](/modules/order-of-work.md)
- [rehearse](/modules/rehearse.md)
- [stages.py](/modules/stages-py.md)

# Features
- [Archify stage documentation](/features/archify-stage-documentation.md)
- [graph-selected repomix context packs](/features/graph-selected-repomix-context-packs.md)
- [Graphify and OKF knowledge base integration](/features/graphify-and-okf-knowledge-base-integration.md)
- [Status next pointer](/features/status-next-pointer.md)
