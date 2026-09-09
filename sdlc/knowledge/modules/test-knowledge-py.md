---
type: Module
title: test_knowledge.py
description: "Graphify community 9: tests/test_knowledge.py"
resource: tests
tags: [module, graphify]
status: draft
generated: { by: sdlc/0.2.0, at: "2026-09-09T01:00:09Z" }
stale_after: "2026-09-23T01:00:09Z"
source_commit: f4b7a7e7c7ca48d51fac20696ba496746da179e6
sources:
  - { id: test_knowledge, resource: tests/test_knowledge.py, last_modified: "2026-09-09T10:28:52+10:00", digest: 1ec63b0274cb5cdb }
---

# Files
- `tests/test_knowledge.py`

# Symbols
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

# Depends on
- [fail](/modules/fail.md)

# Inferred
- [cli.py](/modules/cli-py.md)
- [run](/modules/run.md)

# Features
- [Graphify and OKF knowledge base integration](/features/graphify-and-okf-knowledge-base-integration.md)
