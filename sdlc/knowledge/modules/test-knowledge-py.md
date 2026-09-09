---
type: Module
title: test_knowledge.py
description: "Graphify community 67: tests/test_knowledge.py"
resource: tests
tags: [module, graphify]
status: draft
generated: { by: sdlc/0.2.1, at: "2026-09-09T02:08:45Z" }
stale_after: "2026-09-23T02:08:45Z"
source_commit: 0794a80b6291964cd26930a809a8678a9c9b1311
sources:
  - { id: test_knowledge, resource: tests/test_knowledge.py, last_modified: "2026-09-09T12:08:42+10:00", digest: 263cff832f579528 }
---

# Files
- `tests/test_knowledge.py`

# Symbols
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
- test_status_reports_archify_version() (tests/test_knowledge.py:L675)
- states() (tests/test_knowledge.py:L69)
- test_feature_concept_lists_documents() (tests/test_knowledge.py:L690)
- test_bootstrap_installs_in_order_and_reports_steps() (tests/test_knowledge.py:L73)

# Depends on
- [cli.py](/modules/cli-py.md)

# Inferred
- [run](/modules/run.md)

# Features
- [Archify stage documentation](/features/archify-stage-documentation.md)
- [Graphify and OKF knowledge base integration](/features/graphify-and-okf-knowledge-base-integration.md)
