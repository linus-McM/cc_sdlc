---
type: Module
title: Order of work
description: "Graphify community 5: plugin/scripts/sdlc/artifacts.py, sdlc/graphify-and-okf-knowledge-base-integration/plan.md, sdlc/graphify-and-okf-knowledge-base-integration/review.md, sdlc/graphify-and-okf-know"
resource: ""
tags: [module, graphify]
status: draft
generated: { by: sdlc/0.5.0, at: "2026-09-26T05:22:30Z" }
stale_after: "2026-10-10T05:22:30Z"
source_commit: c5f64f8d3b9b5e3268754f626b7f2e958fd6415e
sources:
  - { id: artifacts, resource: plugin/scripts/sdlc/artifacts.py, last_modified: "2026-09-09T15:02:31+10:00", digest: 3e063b545e7dd897 }
  - { id: plan, resource: sdlc/graphify-and-okf-knowledge-base-integration/plan.md, last_modified: "2026-09-09T15:03:27+10:00", digest: 31d2c88298eefdb1 }
  - { id: review, resource: sdlc/graphify-and-okf-knowledge-base-integration/review.md, last_modified: "2026-09-09T15:03:27+10:00", digest: b6e15f798eacd1f2 }
  - { id: spec, resource: sdlc/graphify-and-okf-knowledge-base-integration/spec.md, last_modified: "2026-09-09T15:03:27+10:00", digest: 18ddccb80477e245 }
  - { id: test_deploy, resource: tests/test_deploy.py, last_modified: "2026-09-19T23:30:10+10:00", digest: dbfb47118be6302a }
  - { id: test_knowledge, resource: tests/test_knowledge.py, last_modified: "2026-09-09T13:24:37+10:00", digest: a817e8df2c2f4e96 }
---

# Files
- `plugin/scripts/sdlc/artifacts.py`
- `sdlc/graphify-and-okf-knowledge-base-integration/plan.md`
- `sdlc/graphify-and-okf-knowledge-base-integration/review.md`
- `sdlc/graphify-and-okf-knowledge-base-integration/spec.md`
- `tests/test_deploy.py`
- `tests/test_knowledge.py`

# Symbols
- first_line() (plugin/scripts/sdlc/artifacts.py:L74)
- The first filled line of a section body, skipping template placeholders. (plugin/scripts/sdlc/artifacts.py:L75)
- Order of work (sdlc/graphify-and-okf-knowledge-base-integration/plan.md:L50)
- graphify-and-okf-knowledge-base-integration/review.md (sdlc/graphify-and-okf-knowledge-base-integration/review.md:L1)
- Review: Graphify and OKF knowledge base integration (sdlc/graphify-and-okf-knowledge-base-integration/review.md:L1)
- Security (sdlc/graphify-and-okf-knowledge-base-integration/review.md:L11)
- Bugs (sdlc/graphify-and-okf-knowledge-base-integration/review.md:L4)
- Proof (sdlc/graphify-and-okf-knowledge-base-integration/spec.md:L330)
- test_pr_body_has_knowledge_section() (tests/test_deploy.py:L130)
- test_knowledge.py (tests/test_knowledge.py:L1)
- test_bootstrap_healthy_project_makes_no_calls() (tests/test_knowledge.py:L104)
- boom() (tests/test_knowledge.py:L112)
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
- test_commands_call_sdlc_through_uv_run() (tests/test_knowledge.py:L537)
- test_linked_worktree_leaves_shared_hook_to_primary() (tests/test_knowledge.py:L547)
- test_linked_worktree_bootstrap_skips_hooks_and_continues() (tests/test_knowledge.py:L575)
- test_status_reports_unknown_history_and_corrupt_state() (tests/test_knowledge.py:L589)
- test_bundle_setting_is_validated_before_it_reaches_a_hook_or_path() (tests/test_knowledge.py:L610)
- test_hook_block_waits_on_the_graph_commit_not_a_reflog() (tests/test_knowledge.py:L624)
- test_signature_notices_a_removed_builder_key() (tests/test_knowledge.py:L632)
- test_unreadable_frontmatter_is_regenerated_not_published_over() (tests/test_knowledge.py:L645)
- test_bootstrap_archify_step_skips_installs_and_reports() (tests/test_knowledge.py:L660)
- step() (tests/test_knowledge.py:L663)
- states() (tests/test_knowledge.py:L69)
- test_status_reports_archify_version() (tests/test_knowledge.py:L695)
- test_feature_concept_lists_documents() (tests/test_knowledge.py:L710)
- test_bootstrap_installs_in_order_and_reports_steps() (tests/test_knowledge.py:L73)

# Depends on
- [Order of work](/modules/order-of-work.md)
- [project.py](/modules/project-py.md)
- [test_build_test.py](/modules/test-build-test-py.md)
- [test_hooks.py](/modules/test-hooks-py.md)

# Inferred
- [Blocked](/modules/blocked.md)
- [bootstrap](/modules/bootstrap.md)
- [build.py](/modules/build-py.md)
- [cli.py](/modules/cli-py.md)
- [Components](/modules/components.md)
- [config](/modules/config.md)
- [docs.py](/modules/docs-py.md)
- [fail](/modules/fail.md)
- [fill](/modules/fill.md)
- [hooks.py](/modules/hooks-py.md)
- [knowledge.py](/modules/knowledge-py.md)
- [Order of work](/modules/order-of-work.md)
- [parse_frontmatter](/modules/parse-frontmatter.md)
- [Path](/modules/path.md)
- [Path](/modules/path-13.md)
- [post_edit](/modules/post-edit.md)
- [reconcile](/modules/reconcile.md)
- [refresh](/modules/refresh.md)
- [rehearse](/modules/rehearse.md)
- [StepSkipped](/modules/stepskipped.md)
- [test_build_test.py](/modules/test-build-test-py.md)
- [test_hooks.py](/modules/test-hooks-py.md)

# Features
- [Archify stage documentation](/features/archify-stage-documentation.md)
- [Dogfood fixes round two](/features/dogfood-fixes-round-two.md)
- [graph-selected repomix context packs](/features/graph-selected-repomix-context-packs.md)
- [Graphify and OKF knowledge base integration](/features/graphify-and-okf-knowledge-base-integration.md)
- [Rehearsal and band nits](/features/rehearsal-and-band-nits.md)
