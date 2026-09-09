---
type: Module
title: run
description: "Graphify community 67: tests/conftest.py, tests/test_build_test.py, tests/test_deploy.py, tests/test_docs.py, tests/test_knowledge.py"
resource: tests
tags: [module, graphify]
status: draft
generated: { by: sdlc/0.2.1, at: "2026-09-09T02:45:02Z" }
stale_after: "2026-09-23T02:45:02Z"
source_commit: 16ce44221e592819936583be6bb11207ce568f21
sources:
  - { id: conftest, resource: tests/conftest.py, last_modified: "2026-09-09T12:22:23+10:00", digest: 083136847a7b1198 }
  - { id: test_build_test, resource: tests/test_build_test.py, last_modified: "2026-09-09T07:52:07+10:00", digest: a23e976c32f40b84 }
  - { id: test_deploy, resource: tests/test_deploy.py, last_modified: "2026-09-09T11:03:29+10:00", digest: dd03cc571d88f162 }
  - { id: test_docs, resource: tests/test_docs.py, last_modified: "2026-09-09T12:44:58+10:00", digest: 3920a490541297e5 }
  - { id: test_knowledge, resource: tests/test_knowledge.py, last_modified: "2026-09-09T12:44:58+10:00", digest: adda529b77852106 }
---

# Files
- `tests/conftest.py`
- `tests/test_build_test.py`
- `tests/test_deploy.py`
- `tests/test_docs.py`
- `tests/test_knowledge.py`

# Symbols
- run() (tests/conftest.py:L28)
- Invoke the CLI in-process; return its JSON result dict. (tests/conftest.py:L29)
- load() (tests/conftest.py:L45)
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
- test_docs.py (tests/test_docs.py:L1)
- Archify stage documents: [docs] config, render/check/open mechanics and the… (tests/test_docs.py:L1)
- test_defaults_and_disabled_verdicts() (tests/test_docs.py:L12)
- test_review_and_record_require_documents() (tests/test_docs.py:L123)
- test_open_calls_opener_unless_ci_or_disabled() (tests/test_docs.py:L147)
- test_pr_body_lists_documents() (tests/test_docs.py:L170)
- test_maintain_document_is_ungated_and_reported() (tests/test_docs.py:L184)
- test_stage_commands_carry_the_docs_step() (tests/test_docs.py:L206)
- test_accept_keeps_the_document_fresh_and_stays_idempotent() (tests/test_docs.py:L221)
- test_disabled_verdict_precedes_feature_lookup() (tests/test_docs.py:L231)
- test_docs_dir_is_validated_and_validation_line_is_numbers_only() (tests/test_docs.py:L235)
- source() (tests/test_docs.py:L33)
- test_render_delivers_html_and_receipt() (tests/test_docs.py:L40)
- test_render_failures_are_verbatim() (tests/test_docs.py:L61)
- test_check_reports_fresh_missing_and_stale() (tests/test_docs.py:L75)
- test_accept_requires_fresh_document_per_stage() (tests/test_docs.py:L99)
- test_knowledge.py (tests/test_knowledge.py:L1)
- test_bootstrap_healthy_project_makes_no_calls() (tests/test_knowledge.py:L104)
- test_bootstrap_installs_uv_when_missing() (tests/test_knowledge.py:L121)
- test_bootstrap_uv_installer_failure_fails_closed() (tests/test_knowledge.py:L135)
- test_uv_install_command_is_gated_by_operating_system() (tests/test_knowledge.py:L149)
- test_bootstrap_check_mode_installs_nothing() (tests/test_knowledge.py:L160)
- test_hook_block_idempotent_and_removable() (tests/test_knowledge.py:L172)
- seed_sources() (tests/test_knowledge.py:L202)
- Code files the fixture graph names, plus lessons, bands and one metric reading. (tests/test_knowledge.py:L203)
- head() (tests/test_knowledge.py:L218)
- bundle_files() (tests/test_knowledge.py:L222)
- test_refresh_builds_bundle_from_graph_and_artifacts() (tests/test_knowledge.py:L227)
- test_defaults_and_disabled_verdicts() (tests/test_knowledge.py:L24)
- test_refresh_is_idempotent() (tests/test_knowledge.py:L308)
- commit_all() (tests/test_knowledge.py:L320)
- test_refresh_invalidates_changed_sources_and_tombstones_deleted() (tests/test_knowledge.py:L325)
- test_frontmatter_subset_round_trip() (tests/test_knowledge.py:L34)
- test_publish_only_on_accept_and_never_by_generation() (tests/test_knowledge.py:L373)
- test_check_separates_conformance_policy_trust() (tests/test_knowledge.py:L415)
- test_status_reports_behind_skew_and_clean_cadence() (tests/test_knowledge.py:L469)
- test_hooks_json_registers_session_start_and_post_bash() (tests/test_knowledge.py:L520)
- test_linked_worktree_leaves_shared_hook_to_primary() (tests/test_knowledge.py:L536)
- test_linked_worktree_bootstrap_skips_hooks_and_continues() (tests/test_knowledge.py:L564)
- test_status_reports_unknown_history_and_corrupt_state() (tests/test_knowledge.py:L578)
- test_bundle_setting_is_validated_before_it_reaches_a_hook_or_path() (tests/test_knowledge.py:L599)
- test_hook_block_waits_on_the_graph_commit_not_a_reflog() (tests/test_knowledge.py:L613)
- test_signature_notices_a_removed_builder_key() (tests/test_knowledge.py:L621)
- test_unreadable_frontmatter_is_regenerated_not_published_over() (tests/test_knowledge.py:L634)
- test_bootstrap_archify_step_skips_installs_and_reports() (tests/test_knowledge.py:L649)
- test_status_reports_archify_version() (tests/test_knowledge.py:L683)
- states() (tests/test_knowledge.py:L69)
- test_feature_concept_lists_documents() (tests/test_knowledge.py:L698)
- test_bootstrap_installs_in_order_and_reports_steps() (tests/test_knowledge.py:L73)

# Depends on
- [build.py](/modules/build-py.md)
- [conftest.py](/modules/conftest-py.md)
- [project.py](/modules/project-py.md)

# Inferred
- [conftest.py](/modules/conftest-py.md)
- [deploy.py](/modules/deploy-py.md)
- [toml_config](/modules/toml-config.md)

# Features
- [Archify stage documentation](/features/archify-stage-documentation.md)
- [Dogfood fixes round two](/features/dogfood-fixes-round-two.md)
- [Graphify and OKF knowledge base integration](/features/graphify-and-okf-knowledge-base-integration.md)
- [Rehearsal and band nits](/features/rehearsal-and-band-nits.md)
- [Status next pointer](/features/status-next-pointer.md)
