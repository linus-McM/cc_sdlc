---
type: Module
title: Order of work
description: "Graphify community 8: sdlc/graph-selected-repomix-context-packs/plan.md, sdlc/graph-selected-repomix-context-packs/review.md, tests/conftest.py, tests/test_build_test.py, tests/test_packs.py"
resource: ""
tags: [module, graphify]
status: draft
generated: { by: sdlc/0.5.0, at: "2026-09-26T06:33:18Z" }
stale_after: "2026-10-10T06:33:18Z"
source_commit: 5c45a37edd0dc635576e390a1174bea9fad6d10b
sources:
  - { id: plan, resource: sdlc/graph-selected-repomix-context-packs/plan.md, last_modified: "2026-09-26T16:06:32+10:00", digest: bbace73703f81509 }
  - { id: review, resource: sdlc/graph-selected-repomix-context-packs/review.md, last_modified: "2026-09-26T06:33:18Z", digest: 0776a4bbb3c557e7 }
  - { id: conftest, resource: tests/conftest.py, last_modified: "2026-09-26T16:23:50+10:00", digest: 44de9d075d1ea218 }
  - { id: test_build_test, resource: tests/test_build_test.py, last_modified: "2026-09-26T16:31:53+10:00", digest: 72418fccb201e603 }
  - { id: test_packs, resource: tests/test_packs.py, last_modified: "2026-09-26T16:23:50+10:00", digest: c7fcbee4b21b61f3 }
---

# Files
- `sdlc/graph-selected-repomix-context-packs/plan.md`
- `sdlc/graph-selected-repomix-context-packs/review.md`
- `tests/conftest.py`
- `tests/test_build_test.py`
- `tests/test_packs.py`

# Symbols
- Order of work (sdlc/graph-selected-repomix-context-packs/plan.md:L34)
- graph-selected-repomix-context-packs/review.md (sdlc/graph-selected-repomix-context-packs/review.md:L1)
- Review: graph-selected repomix context packs (sdlc/graph-selected-repomix-context-packs/review.md:L1)
- Compliance (sdlc/graph-selected-repomix-context-packs/review.md:L13)
- Bugs (sdlc/graph-selected-repomix-context-packs/review.md:L4)
- Security (sdlc/graph-selected-repomix-context-packs/review.md:L9)
- commit_files() (tests/conftest.py:L343)
- Write `files` (keys use __ for /) and commit them; return HEAD. (tests/conftest.py:L344)
- regraph() (tests/conftest.py:L354)
- Commit `files`, then rebuild graph.json at the new HEAD, as the post-commit… (tests/conftest.py:L355)
- test_build_test.py (tests/test_build_test.py:L1)
- test_test_review_validates_findings_file() (tests/test_build_test.py:L101)
- test_run_adds_knowledge_result_and_process_verified() (tests/test_build_test.py:L110)
- test_build_new_then_accept() (tests/test_build_test.py:L12)
- branch_with_change() (tests/test_build_test.py:L129)
- Sources on main, a feat branch committing `changes`, graph.json fresh at HEAD… (tests/test_build_test.py:L130)
- test_review_accepts_a_covering_pack() (tests/test_build_test.py:L141)
- test_review_refused_when_a_changed_file_is_missing_from_the_pack() (tests/test_build_test.py:L150)
- test_review_accounts_for_excluded_changes() (tests/test_build_test.py:L159)
- test_build_red_records_failing_run_and_rejects_passing() (tests/test_build_test.py:L16)
- test_review_covers_renames_and_lock_files() (tests/test_build_test.py:L169)
- test_review_refused_for_a_secret_excluded_change() (tests/test_build_test.py:L179)
- test_review_skips_deleted_binary_and_sdlc_owned_changes() (tests/test_build_test.py:L186)
- test_review_gate_skipped_visibly_when_off() (tests/test_build_test.py:L198)
- test_review_refuses_a_change_excluded_only_by_uncommitted_state() (tests/test_build_test.py:L205)
- test_build_green_requires_prior_red_and_passing_tests() (tests/test_build_test.py:L27)
- test_build_sync_flags_unplanned_files() (tests/test_build_test.py:L38)
- test_build_sync_ignores_sdlc_artifacts_and_config() (tests/test_build_test.py:L49)
- test_build_sync_keeps_unstaged_first_line_path_intact() (tests/test_build_test.py:L53)
- ` M path` is the first porcelain line; stripping its leading space mangled the… (tests/test_build_test.py:L54)
- test_build_fix_toggles_lock() (tests/test_build_test.py:L61)
- test_test_run_gated_on_accepted_plan() (tests/test_build_test.py:L68)
- test_test_run_requires_tdd_cycle() (tests/test_build_test.py:L72)
- test_test_run_writes_report() (tests/test_build_test.py:L78)
- test_build_new_gated_on_accepted_spec() (tests/test_build_test.py:L8)
- test_test_run_failure_reported_not_hidden() (tests/test_build_test.py:L91)
- test_packs.py (tests/test_packs.py:L1)
- Graph-selected Repomix context packs: seeds, one-hop expansion, secret guards,… (tests/test_packs.py:L1)
- test_exclude_list_is_frozen() (tests/test_packs.py:L118)
- test_pack_config_defaults() (tests/test_packs.py:L12)
- ready() (tests/test_packs.py:L128)
- Sources and a feature committed, then the knowledge layer bootstrapped:… (tests/test_packs.py:L129)
- pack() (tests/test_packs.py:L136)
- test_pack_refuses_deploy_and_unknown_stages() (tests/test_packs.py:L142)
- test_pack_refuses_stale_graph_by_content() (tests/test_packs.py:L149)
- test_checkpoint_paths_do_not_stale_the_graph() (tests/test_packs.py:L158)
- test_pack_refuses_missing_graph_and_unignored_graphify_out() (tests/test_packs.py:L164)
- test_run_cmd_passes_stdin() (tests/test_packs.py:L17)
- test_pack_refuses_dirty_admitted_file() (tests/test_packs.py:L177)
- test_missing_repomix_skips_advisory_and_fails_gated() (tests/test_packs.py:L184)
- test_pack_layer_off_is_skipped() (tests/test_packs.py:L194)
- packs_dir() (tests/test_packs.py:L202)
- test_pack_writes_xml_and_manifest() (tests/test_packs.py:L206)
- test_packs_fixture_fakes_every_tool() (tests/test_packs.py:L21)
- test_pack_reuses_same_key() (tests/test_packs.py:L224)
- test_new_commit_rekeys_and_prunes_older_pack() (tests/test_packs.py:L232)
- test_output_scanner_refuses() (tests/test_packs.py:L242)
- test_bandit_finding_refuses_pack() (tests/test_packs.py:L254)
- test_bandit_failure_refuses() (tests/test_packs.py:L263)
- test_bandit_skipped_without_py_files() (tests/test_packs.py:L270)
- repomix_calls() (tests/test_packs.py:L277)
- test_no_budget_runs_once_without_compress() (tests/test_packs.py:L281)
- test_budget_ladder_reports_every_rung() (tests/test_packs.py:L288)
- test_cli_knowledge_pack_row() (tests/test_packs.py:L303)
- test_packs_never_committed_or_checkpointed() (tests/test_packs.py:L312)
- test_pack_content_that_looks_like_a_file_header() (tests/test_packs.py:L324)
- test_seeds_skip_sdlc_owned_files() (tests/test_packs.py:L331)
- test_pack_with_no_selected_files_packs_nothing() (tests/test_packs.py:L339)
- test_secret_rules_ignore_case_and_bandit_ends_options() (tests/test_packs.py:L348)
- test_expand_is_one_hop_over_calls_plus_community() (tests/test_packs.py:L35)
- test_expand_adds_community_members_and_callers() (tests/test_packs.py:L42)
- feature_dir() (tests/test_packs.py:L54)
- test_seeds_per_stage() (tests/test_packs.py:L62)
- test_unresolved_tokens_are_listed_not_guessed() (tests/test_packs.py:L85)
- test_exclude_list_applies_after_expansion() (tests/test_packs.py:L95)

# Depends on
- [conftest.py](/modules/conftest-py.md)
- [docs.py](/modules/docs-py.md)
- [pathlib](/modules/pathlib.md)
- [test_plan_design.py](/modules/test-plan-design-py.md)

# Inferred
- [build](/modules/build.md)
- [conftest.py](/modules/conftest-py.md)
- [docs.py](/modules/docs-py.md)
- [git](/modules/git.md)
- [Order of work](/modules/order-of-work.md)
- [packs.py](/modules/packs-py.md)
- [Path](/modules/path.md)
- [require](/modules/require.md)
- [review](/modules/review.md)
- [run_repomix](/modules/run-repomix.md)
- [test_plan_design.py](/modules/test-plan-design-py.md)
- [test_workflows.py](/modules/test-workflows-py.md)

# Features
- [Archify stage documentation](/features/archify-stage-documentation.md)
- [graph-selected repomix context packs](/features/graph-selected-repomix-context-packs.md)
- [Graphify and OKF knowledge base integration](/features/graphify-and-okf-knowledge-base-integration.md)
- [Status next pointer](/features/status-next-pointer.md)
