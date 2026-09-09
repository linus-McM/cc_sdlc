---
type: Module
title: test_hooks.py
description: "Graphify community 5: tests/conftest.py, tests/test_build_test.py, tests/test_hooks.py"
resource: tests
tags: [module, graphify]
status: draft
generated: { by: sdlc/0.2.1, at: "2026-09-09T01:05:41Z" }
stale_after: "2026-09-23T01:05:41Z"
source_commit: 84e34c7e5ba9bdec7e2f26ef69f1f509c15b7046
sources:
  - { id: conftest, resource: tests/conftest.py, last_modified: "2026-09-09T08:32:17+10:00", digest: 17b40c0ad91b947d }
  - { id: test_build_test, resource: tests/test_build_test.py, last_modified: "2026-09-09T07:52:07+10:00", digest: a23e976c32f40b84 }
  - { id: test_hooks, resource: tests/test_hooks.py, last_modified: "2026-09-09T10:28:52+10:00", digest: 3649685b5ab2c487 }
---

# Files
- `tests/conftest.py`
- `tests/test_build_test.py`
- `tests/test_hooks.py`

# Symbols
- toml_config() (tests/conftest.py:L94)
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
- test_test_run_failure_reported_not_hidden() (tests/test_build_test.py:L90)
- test_hooks.py (tests/test_hooks.py:L1)
- no_release_approval() (tests/test_hooks.py:L10)
- test_pre_bash_denies_configured_release_command() (tests/test_hooks.py:L101)
- test_pre_bash_gated_names_come_from_config_only() (tests/test_hooks.py:L114)
- test_pre_bash_survives_bad_release_command_config() (tests/test_hooks.py:L120)
- test_post_edit_warns_when_file_not_in_plan() (tests/test_hooks.py:L129)
- test_main_reads_stdin_and_prints_json() (tests/test_hooks.py:L136)
- edit() (tests/test_hooks.py:L14)
- test_session_start_context_lists_steps() (tests/test_hooks.py:L144)
- test_session_start_silent_when_disabled() (tests/test_hooks.py:L167)
- test_post_bash_flags_stale_after_commit() (tests/test_hooks.py:L171)
- bash() (tests/test_hooks.py:L18)
- test_post_edit_names_module_concepts() (tests/test_hooks.py:L189)
- denied() (tests/test_hooks.py:L22)
- test_pre_edit_allows_ordinary_file() (tests/test_hooks.py:L26)
- test_hooks_ignore_paths_outside_root() (tests/test_hooks.py:L30)
- test_hooks_judge_symlinks_by_their_in_repo_name() (tests/test_hooks.py:L40)
- test_pre_edit_blocks_protected_path() (tests/test_hooks.py:L48)
- test_pre_edit_blocks_tests_only_while_fix_lock() (tests/test_hooks.py:L55)
- test_pre_bash_production_gate() (tests/test_hooks.py:L64)
- test_pre_bash_ignores_prose_and_heredocs() (tests/test_hooks.py:L71)
- test_pre_bash_scans_every_command_line_outside_heredocs() (tests/test_hooks.py:L80)
- test_pre_bash_fallback_matches_tokens_not_text() (tests/test_hooks.py:L92)

# Depends on
- [fail](/modules/fail.md)
- [run](/modules/run.md)

# Inferred
- [run](/modules/run.md)

# Features
- [Dogfood fixes round two](/features/dogfood-fixes-round-two.md)
- [Graphify and OKF knowledge base integration](/features/graphify-and-okf-knowledge-base-integration.md)
- [Rehearsal and band nits](/features/rehearsal-and-band-nits.md)
- [Release hook hardening](/features/release-hook-hardening.md)
- [Status next pointer](/features/status-next-pointer.md)
