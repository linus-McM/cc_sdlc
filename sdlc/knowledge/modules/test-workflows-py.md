---
type: Module
title: test_workflows.py
description: "Graphify community 4: tests/test_deploy.py, tests/test_workflows.py"
resource: tests
tags: [module, graphify]
status: draft
generated: { by: sdlc/0.5.0, at: "2026-09-26T05:22:30Z" }
stale_after: "2026-10-10T05:22:30Z"
source_commit: c5f64f8d3b9b5e3268754f626b7f2e958fd6415e
sources:
  - { id: test_deploy, resource: tests/test_deploy.py, last_modified: "2026-09-19T23:30:10+10:00", digest: dbfb47118be6302a }
  - { id: test_workflows, resource: tests/test_workflows.py, last_modified: "2026-09-19T23:30:10+10:00", digest: a006d4dbeef09c2e }
---

# Files
- `tests/test_deploy.py`
- `tests/test_workflows.py`

# Symbols
- test_deploy.py (tests/test_deploy.py:L1)
- test_deploy_rehearse_fails_when_no_rollback_configured() (tests/test_deploy.py:L103)
- test_deploy_record_appends_history() (tests/test_deploy.py:L108)
- test_deploy_pr_writes_body_from_artifacts() (tests/test_deploy.py:L118)
- test_deploy_unknown_env_rejected() (tests/test_deploy.py:L126)
- tested() (tests/test_deploy.py:L13)
- Feature with a green TDD cycle, passing test-report and review.md. (tests/test_deploy.py:L14)
- test_templates_and_config_carry_knowledge_bands_and_evals() (tests/test_deploy.py:L150)
- test_deploy_check_blocks_without_test_report() (tests/test_deploy.py:L24)
- test_deploy_check_dev_is_free() (tests/test_deploy.py:L29)
- test_deploy_check_staging_asks() (tests/test_deploy.py:L34)
- test_deploy_check_production_gate() (tests/test_deploy.py:L38)
- test_deploy_rehearse_records_rollback() (tests/test_deploy.py:L50)
- test_workflows.py (tests/test_workflows.py:L1)
- test_env_off_switches() (tests/test_workflows.py:L104)
- test_session_start_sets_workflow_env_once() (tests/test_workflows.py:L114)
- test_env_leaves_projects_without_sdlc_config_alone() (tests/test_workflows.py:L122)
- test_env_refuses_keys_outside_the_workflow_namespace() (tests/test_workflows.py:L129)
- test_every_plugin_source_file_is_tracked() (tests/test_workflows.py:L136)
- test_session_start_reports_unreadable_settings_without_failing() (tests/test_workflows.py:L142)
- workflows_on() (tests/test_workflows.py:L17)
- settings() (tests/test_workflows.py:L22)
- test_every_stage_ships_one_workflow_script() (tests/test_workflows.py:L26)
- test_workflow_meta_is_a_literal_whose_phases_match_the_body() (tests/test_workflows.py:L34)
- test_workflow_script_parses_as_an_es_module() (tests/test_workflows.py:L46)
- test_each_stage_command_calls_its_workflow() (tests/test_workflows.py:L55)
- test_list_reports_the_catalog() (tests/test_workflows.py:L61)
- test_env_writes_workflow_variables_into_local_settings() (tests/test_workflows.py:L67)
- test_env_keeps_existing_settings_and_user_values() (tests/test_workflows.py:L75)
- test_env_refuses_to_overwrite_unreadable_settings() (tests/test_workflows.py:L87)
- test_env_exports_to_the_session_env_file() (tests/test_workflows.py:L95)

# Depends on
- [Blocked](/modules/blocked.md)
- [Order of work](/modules/order-of-work.md)
- [Order of work](/modules/order-of-work-5.md)
- [post_edit](/modules/post-edit.md)
- [project.py](/modules/project-py.md)

# Inferred
- no INFERRED edges; treat any that appear as hints

# Features
- [Dogfood fixes round two](/features/dogfood-fixes-round-two.md)
- [graph-selected repomix context packs](/features/graph-selected-repomix-context-packs.md)
- [Graphify and OKF knowledge base integration](/features/graphify-and-okf-knowledge-base-integration.md)
- [Rehearsal and band nits](/features/rehearsal-and-band-nits.md)
