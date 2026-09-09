---
type: Module
title: run
description: "Graphify community 2: scripts/sdlc/project.py, tests/conftest.py, tests/test_build_test.py, tests/test_deploy.py, tests/test_knowledge.py, tests/test_plan_design.py"
resource: ""
tags: [module, graphify]
status: draft
generated: { by: sdlc/0.2.1, at: "2026-09-09T01:29:56Z" }
stale_after: "2026-09-23T01:29:56Z"
source_commit: b6e8d5897548ac1aeadd713c4fd9bf19fac3d435
sources:
  - { id: project, resource: scripts/sdlc/project.py, last_modified: "2026-09-09T08:32:17+10:00", digest: 15fdd6685d1225c1 }
  - { id: conftest, resource: tests/conftest.py, last_modified: "2026-09-09T08:32:17+10:00", digest: 17b40c0ad91b947d }
  - { id: test_build_test, resource: tests/test_build_test.py, last_modified: "2026-09-09T07:52:07+10:00", digest: a23e976c32f40b84 }
  - { id: test_deploy, resource: tests/test_deploy.py, last_modified: "2026-09-09T11:03:29+10:00", digest: dd03cc571d88f162 }
  - { id: test_knowledge, resource: tests/test_knowledge.py, last_modified: "2026-09-09T11:03:29+10:00", digest: 592cb88234e9c2f8 }
  - { id: test_plan_design, resource: tests/test_plan_design.py, last_modified: "2026-09-09T07:52:07+10:00", digest: 0ef824c0b5e9bd38 }
---

# Files
- `scripts/sdlc/project.py`
- `tests/conftest.py`
- `tests/test_build_test.py`
- `tests/test_deploy.py`
- `tests/test_knowledge.py`
- `tests/test_plan_design.py`

# Symbols
- write_json() (scripts/sdlc/project.py:L182)
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
- test_test_run_writes_report() (tests/test_build_test.py:L77)
- test_deploy.py (tests/test_deploy.py:L1)
- test_deploy_rehearse_fails_when_no_rollback_configured() (tests/test_deploy.py:L103)
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
- test_knowledge.py (tests/test_knowledge.py:L1)
- test_bootstrap_healthy_project_makes_no_calls() (tests/test_knowledge.py:L103)
- test_bootstrap_installs_uv_when_missing() (tests/test_knowledge.py:L120)
- test_bootstrap_uv_installer_failure_fails_closed() (tests/test_knowledge.py:L134)
- test_uv_install_command_is_gated_by_operating_system() (tests/test_knowledge.py:L148)
- test_bootstrap_check_mode_installs_nothing() (tests/test_knowledge.py:L159)
- test_hook_block_idempotent_and_removable() (tests/test_knowledge.py:L171)
- seed_sources() (tests/test_knowledge.py:L201)
- Code files the fixture graph names, plus lessons, bands and one metric reading. (tests/test_knowledge.py:L202)
- head() (tests/test_knowledge.py:L217)
- bundle_files() (tests/test_knowledge.py:L221)
- test_refresh_builds_bundle_from_graph_and_artifacts() (tests/test_knowledge.py:L226)
- test_defaults_and_disabled_verdicts() (tests/test_knowledge.py:L24)
- test_refresh_is_idempotent() (tests/test_knowledge.py:L307)
- commit_all() (tests/test_knowledge.py:L319)
- test_refresh_invalidates_changed_sources_and_tombstones_deleted() (tests/test_knowledge.py:L324)
- test_frontmatter_subset_round_trip() (tests/test_knowledge.py:L34)
- test_publish_only_on_accept_and_never_by_generation() (tests/test_knowledge.py:L372)
- test_check_separates_conformance_policy_trust() (tests/test_knowledge.py:L414)
- test_status_reports_behind_skew_and_clean_cadence() (tests/test_knowledge.py:L468)
- test_hooks_json_registers_session_start_and_post_bash() (tests/test_knowledge.py:L519)
- test_linked_worktree_leaves_shared_hook_to_primary() (tests/test_knowledge.py:L535)
- test_linked_worktree_bootstrap_skips_hooks_and_continues() (tests/test_knowledge.py:L563)
- test_status_reports_unknown_history_and_corrupt_state() (tests/test_knowledge.py:L577)
- test_bundle_setting_is_validated_before_it_reaches_a_hook_or_path() (tests/test_knowledge.py:L598)
- test_hook_block_waits_on_the_graph_commit_not_a_reflog() (tests/test_knowledge.py:L612)
- test_signature_notices_a_removed_builder_key() (tests/test_knowledge.py:L620)
- test_unreadable_frontmatter_is_regenerated_not_published_over() (tests/test_knowledge.py:L633)
- states() (tests/test_knowledge.py:L69)
- test_bootstrap_installs_in_order_and_reports_steps() (tests/test_knowledge.py:L73)
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
- [fail](/modules/fail.md)
- [project.py](/modules/project-py.md)
- [test_hooks.py](/modules/test-hooks-py.md)

# Inferred
- [cli.py](/modules/cli-py.md)
- [test_hooks.py](/modules/test-hooks-py.md)

# Features
- [Dogfood fixes round two](/features/dogfood-fixes-round-two.md)
- [Graphify and OKF knowledge base integration](/features/graphify-and-okf-knowledge-base-integration.md)
- [Rehearsal and band nits](/features/rehearsal-and-band-nits.md)
- [Release hook hardening](/features/release-hook-hardening.md)
- [Status next pointer](/features/status-next-pointer.md)
