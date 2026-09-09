---
type: Module
title: run
description: "Graphify community 2: scripts/sdlc/__init__.py, tests/conftest.py, tests/test_build_test.py, tests/test_deploy.py, tests/test_maintain.py, tests/test_plan_design.py"
resource: ""
tags: [module, graphify]
status: draft
generated: { by: sdlc/0.2.0, at: "2026-09-09T00:57:33Z" }
stale_after: "2026-09-23T00:57:33Z"
source_commit: a432e14e93d9df64b84d79b6e6d30b2233332f6e
sources:
  - { id: __init__, resource: scripts/sdlc/__init__.py, last_modified: "2026-09-07T12:20:58+10:00", digest: 0a6aea3cd6840dbf }
  - { id: conftest, resource: tests/conftest.py, last_modified: "2026-09-09T08:32:17+10:00", digest: 17b40c0ad91b947d }
  - { id: test_build_test, resource: tests/test_build_test.py, last_modified: "2026-09-09T07:52:07+10:00", digest: a23e976c32f40b84 }
  - { id: test_deploy, resource: tests/test_deploy.py, last_modified: "2026-09-09T10:28:52+10:00", digest: 56584e3193ae03f8 }
  - { id: test_maintain, resource: tests/test_maintain.py, last_modified: "2026-09-08T15:49:55+10:00", digest: 31af1cddd1d1bc15 }
  - { id: test_plan_design, resource: tests/test_plan_design.py, last_modified: "2026-09-09T07:52:07+10:00", digest: 0ef824c0b5e9bd38 }
---

# Files
- `scripts/sdlc/__init__.py`
- `tests/conftest.py`
- `tests/test_build_test.py`
- `tests/test_deploy.py`
- `tests/test_maintain.py`
- `tests/test_plan_design.py`

# Symbols
- __init__.py (scripts/sdlc/__init__.py:L1)
- sdlc — deterministic gates for the six-stage AI-native SDLC. Stdlib only. (scripts/sdlc/__init__.py:L1)
- conftest.py (tests/conftest.py:L1)
- repo() (tests/conftest.py:L11)
- Fresh git repo with one commit; cwd and SDLC root point at it. (tests/conftest.py:L12)
- FakeTools (tests/conftest.py:L124)
- .__init__() (tests/conftest.py:L125)
- .calls() (tests/conftest.py:L128)
- .skill() (tests/conftest.py:L133)
- .uninstall() (tests/conftest.py:L136)
- knowledge() (tests/conftest.py:L142)
- Knowledge layer on, with fake `uv` and `graphify` on an otherwise bare PATH… (tests/conftest.py:L143)
- run() (tests/conftest.py:L25)
- Invoke the CLI in-process; return its JSON result dict. (tests/conftest.py:L26)
- fill() (tests/conftest.py:L34)
- Replace placeholder bodies under named sections with real text. (tests/conftest.py:L35)
- load() (tests/conftest.py:L42)
- accepted_intent() (tests/conftest.py:L47)
- accepted_spec() (tests/conftest.py:L64)
- accepted_plan() (tests/conftest.py:L78)
- test_build_test.py (tests/test_build_test.py:L1)
- test_test_review_validates_findings_file() (tests/test_build_test.py:L100)
- test_run_adds_knowledge_result_and_process_verified() (tests/test_build_test.py:L109)
- test_build_new_then_accept() (tests/test_build_test.py:L11)
- test_build_red_records_failing_run_and_rejects_passing() (tests/test_build_test.py:L15)
- test_build_green_requires_prior_red_and_passing_tests() (tests/test_build_test.py:L26)
- test_build_sync_flags_unplanned_files() (tests/test_build_test.py:L37)
- test_build_sync_ignores_sdlc_artifacts_and_config() (tests/test_build_test.py:L48)
- test_build_sync_keeps_unstaged_first_line_path_intact() (tests/test_build_test.py:L52)
- ` M path` is the first porcelain line; stripping its leading space mangled the… (tests/test_build_test.py:L53)
- test_build_fix_toggles_lock() (tests/test_build_test.py:L60)
- test_test_run_gated_on_accepted_plan() (tests/test_build_test.py:L67)
- test_build_new_gated_on_accepted_spec() (tests/test_build_test.py:L7)
- test_test_run_requires_tdd_cycle() (tests/test_build_test.py:L71)
- test_test_run_writes_report() (tests/test_build_test.py:L77)
- test_test_run_failure_reported_not_hidden() (tests/test_build_test.py:L90)
- test_deploy.py (tests/test_deploy.py:L1)
- test_deploy_record_appends_history() (tests/test_deploy.py:L108)
- test_deploy_pr_writes_body_from_artifacts() (tests/test_deploy.py:L118)
- test_deploy_unknown_env_rejected() (tests/test_deploy.py:L126)
- tested() (tests/test_deploy.py:L13)
- test_pr_body_has_knowledge_section() (tests/test_deploy.py:L130)
- Feature with a green TDD cycle, passing test-report and review.md. (tests/test_deploy.py:L14)
- test_templates_and_config_carry_knowledge_bands_and_evals() (tests/test_deploy.py:L150)
- test_deploy_check_blocks_without_test_report() (tests/test_deploy.py:L24)
- test_deploy_check_dev_is_free() (tests/test_deploy.py:L29)
- test_deploy_check_staging_asks() (tests/test_deploy.py:L34)
- test_deploy_check_production_gate() (tests/test_deploy.py:L38)
- test_deploy_rehearse_records_rollback() (tests/test_deploy.py:L50)
- test_deploy_rehearse_runs_in_throwaway_worktree() (tests/test_deploy.py:L56)
- test_deploy_rehearse_needs_git() (tests/test_deploy.py:L66)
- test_deploy_rehearse_reports_leftover_worktree() (tests/test_deploy.py:L72)
- test_deploy_rehearse_runs_at_project_path() (tests/test_deploy.py:L87)
- A project that is a subdirectory of the repo rehearses at that same… (tests/test_deploy.py:L88)
- test_maintain.py (tests/test_maintain.py:L1)
- test_lesson_appends_to_lessons_md() (tests/test_maintain.py:L101)
- test_western_electric_rules_classify_tiers() (tests/test_maintain.py:L28)
- test_tier_needs_enough_history() (tests/test_maintain.py:L33)
- test_tier_rejects_unknown_side() (tests/test_maintain.py:L37)
- test_tier_one_sided_bands_ignore_the_good_side() (tests/test_maintain.py:L42)
- test_watch_reads_bad_side_and_rejects_unknown() (tests/test_maintain.py:L50)
- test_watch_reads_bands_and_reports_actions() (tests/test_maintain.py:L60)
- test_watch_honours_custom_bands() (tests/test_maintain.py:L72)
- test_propose_writes_intent_and_closes_loop() (tests/test_maintain.py:L79)
- series() (tests/test_maintain.py:L9)
- test_propose_refuses_below_threshold() (tests/test_maintain.py:L90)
- test_ingest_appends_metric() (tests/test_maintain.py:L95)
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
- [deploy.py](/modules/deploy-py.md)
- [project.py](/modules/project-py.md)
- [test_hooks.py](/modules/test-hooks-py.md)

# Inferred
- [test_hooks.py](/modules/test-hooks-py.md)

# Features
- [Dogfood fixes round two](/features/dogfood-fixes-round-two.md)
- [Graphify and OKF knowledge base integration](/features/graphify-and-okf-knowledge-base-integration.md)
- [Rehearsal and band nits](/features/rehearsal-and-band-nits.md)
- [Status next pointer](/features/status-next-pointer.md)
