---
type: Module
title: Order of work
description: "Graphify community 5: plugin/scripts/sdlc/artifacts.py, plugin/scripts/sdlc/knowledge.py, sdlc/graphify-and-okf-knowledge-base-integration/plan.md, sdlc/graphify-and-okf-knowledge-base-integration/rev"
resource: ""
tags: [module, graphify]
status: draft
generated: { by: sdlc/0.5.0, at: "2026-09-26T06:33:18Z" }
stale_after: "2026-10-10T06:33:18Z"
source_commit: 5c45a37edd0dc635576e390a1174bea9fad6d10b
sources:
  - { id: artifacts, resource: plugin/scripts/sdlc/artifacts.py, last_modified: "2026-09-09T15:02:31+10:00", digest: 3e063b545e7dd897 }
  - { id: knowledge, resource: plugin/scripts/sdlc/knowledge.py, last_modified: "2026-09-26T16:06:32+10:00", digest: 12afb6df19262a3a }
  - { id: plan, resource: sdlc/graphify-and-okf-knowledge-base-integration/plan.md, last_modified: "2026-09-09T15:03:27+10:00", digest: 31d2c88298eefdb1 }
  - { id: review, resource: sdlc/graphify-and-okf-knowledge-base-integration/review.md, last_modified: "2026-09-09T15:03:27+10:00", digest: b6e15f798eacd1f2 }
  - { id: spec, resource: sdlc/graphify-and-okf-knowledge-base-integration/spec.md, last_modified: "2026-09-09T15:03:27+10:00", digest: 18ddccb80477e245 }
  - { id: test_deploy, resource: tests/test_deploy.py, last_modified: "2026-09-19T23:30:10+10:00", digest: dbfb47118be6302a }
  - { id: test_knowledge, resource: tests/test_knowledge.py, last_modified: "2026-09-26T15:55:09+10:00", digest: 0ab3fe945b0c75ae }
---

# Files
- `plugin/scripts/sdlc/artifacts.py`
- `plugin/scripts/sdlc/knowledge.py`
- `sdlc/graphify-and-okf-knowledge-base-integration/plan.md`
- `sdlc/graphify-and-okf-knowledge-base-integration/review.md`
- `sdlc/graphify-and-okf-knowledge-base-integration/spec.md`
- `tests/test_deploy.py`
- `tests/test_knowledge.py`

# Symbols
- first_line() (plugin/scripts/sdlc/artifacts.py:L74)
- The first filled line of a section body, skipping template placeholders. (plugin/scripts/sdlc/artifacts.py:L75)
- shell_word() (plugin/scripts/sdlc/knowledge.py:L183)
- `text` as one double-quoted POSIX shell word: backslash, double quote, dollar… (plugin/scripts/sdlc/knowledge.py:L184)
- graphify-and-okf-knowledge-base-integration/plan.md (sdlc/graphify-and-okf-knowledge-base-integration/plan.md:L1)
- Plan: Graphify and OKF knowledge base integration (sdlc/graphify-and-okf-knowledge-base-integration/plan.md:L1)
- Proof (sdlc/graphify-and-okf-knowledge-base-integration/plan.md:L232)
- Files that change (sdlc/graphify-and-okf-knowledge-base-integration/plan.md:L4)
- Order of work (sdlc/graphify-and-okf-knowledge-base-integration/plan.md:L50)
- graphify-and-okf-knowledge-base-integration/review.md (sdlc/graphify-and-okf-knowledge-base-integration/review.md:L1)
- Review: Graphify and OKF knowledge base integration (sdlc/graphify-and-okf-knowledge-base-integration/review.md:L1)
- Security (sdlc/graphify-and-okf-knowledge-base-integration/review.md:L11)
- Compliance (sdlc/graphify-and-okf-knowledge-base-integration/review.md:L16)
- Bugs (sdlc/graphify-and-okf-knowledge-base-integration/review.md:L4)
- Proof (sdlc/graphify-and-okf-knowledge-base-integration/spec.md:L330)
- test_pr_body_has_knowledge_section() (tests/test_deploy.py:L130)
- test_knowledge.py (tests/test_knowledge.py:L1)
- test_bootstrap_healthy_project_makes_no_calls() (tests/test_knowledge.py:L108)
- boom() (tests/test_knowledge.py:L116)
- test_bootstrap_installs_uv_when_missing() (tests/test_knowledge.py:L125)
- test_bootstrap_uv_installer_failure_fails_closed() (tests/test_knowledge.py:L139)
- test_uv_install_command_is_gated_by_operating_system() (tests/test_knowledge.py:L153)
- test_bootstrap_check_mode_installs_nothing() (tests/test_knowledge.py:L164)
- test_hook_block_idempotent_and_removable() (tests/test_knowledge.py:L176)
- seed_sources() (tests/test_knowledge.py:L206)
- Code files the fixture graph names, plus lessons, bands and one metric reading. (tests/test_knowledge.py:L207)
- head() (tests/test_knowledge.py:L222)
- bundle_files() (tests/test_knowledge.py:L226)
- test_refresh_builds_bundle_from_graph_and_artifacts() (tests/test_knowledge.py:L231)
- test_defaults_and_disabled_verdicts() (tests/test_knowledge.py:L27)
- test_refresh_is_idempotent() (tests/test_knowledge.py:L312)
- commit_all() (tests/test_knowledge.py:L324)
- test_refresh_invalidates_changed_sources_and_tombstones_deleted() (tests/test_knowledge.py:L329)
- test_frontmatter_subset_round_trip() (tests/test_knowledge.py:L37)
- test_publish_only_on_accept_and_never_by_generation() (tests/test_knowledge.py:L377)
- test_check_separates_conformance_policy_trust() (tests/test_knowledge.py:L419)
- test_status_reports_behind_skew_and_clean_cadence() (tests/test_knowledge.py:L473)
- test_hooks_json_registers_session_start_and_post_bash() (tests/test_knowledge.py:L524)
- test_commands_call_sdlc_through_uv_run() (tests/test_knowledge.py:L541)
- test_linked_worktree_leaves_shared_hook_to_primary() (tests/test_knowledge.py:L551)
- test_linked_worktree_bootstrap_skips_hooks_and_continues() (tests/test_knowledge.py:L579)
- test_status_reports_unknown_history_and_corrupt_state() (tests/test_knowledge.py:L593)
- test_bundle_setting_is_validated_before_it_reaches_a_hook_or_path() (tests/test_knowledge.py:L614)
- test_hook_block_waits_on_the_graph_commit_not_a_reflog() (tests/test_knowledge.py:L628)
- test_signature_notices_a_removed_builder_key() (tests/test_knowledge.py:L636)
- test_unreadable_frontmatter_is_regenerated_not_published_over() (tests/test_knowledge.py:L649)
- test_bootstrap_archify_step_skips_installs_and_reports() (tests/test_knowledge.py:L664)
- step() (tests/test_knowledge.py:L667)
- test_status_reports_archify_version() (tests/test_knowledge.py:L699)
- test_feature_concept_lists_documents() (tests/test_knowledge.py:L714)
- states() (tests/test_knowledge.py:L72)
- test_bootstrap_installs_and_updates_repomix() (tests/test_knowledge.py:L733)
- test_repomix_step_is_optional() (tests/test_knowledge.py:L749)
- test_bootstrap_installs_in_order_and_reports_steps() (tests/test_knowledge.py:L76)

# Depends on
- [Blocked](/modules/blocked.md)
- [conftest.py](/modules/conftest-py.md)
- [Order of work](/modules/order-of-work-8.md)
- [pathlib](/modules/pathlib.md)
- [test_hooks.py](/modules/test-hooks-py.md)

# Inferred
- [append_log](/modules/append-log.md)
- [Blocked](/modules/blocked.md)
- [check](/modules/check.md)
- [Components](/modules/components.md)
- [config](/modules/config.md)
- [conftest.py](/modules/conftest-py.md)
- [docs.py](/modules/docs-py.md)
- [fail](/modules/fail.md)
- [findings](/modules/findings.md)
- [git](/modules/git.md)
- [hooks.py](/modules/hooks-py.md)
- [install_hook](/modules/install-hook.md)
- [knowledge.py](/modules/knowledge-py.md)
- [Order of work](/modules/order-of-work-8.md)
- [packs.py](/modules/packs-py.md)
- [parse_frontmatter](/modules/parse-frontmatter.md)
- [Path](/modules/path-13.md)
- [project.py](/modules/project-py.md)
- [refresh](/modules/refresh.md)
- [status](/modules/status.md)
- [test_hooks.py](/modules/test-hooks-py.md)
- [test_plan_design.py](/modules/test-plan-design-py.md)

# Features
- [Archify stage documentation](/features/archify-stage-documentation.md)
- [Dogfood fixes round two](/features/dogfood-fixes-round-two.md)
- [graph-selected repomix context packs](/features/graph-selected-repomix-context-packs.md)
- [Graphify and OKF knowledge base integration](/features/graphify-and-okf-knowledge-base-integration.md)
- [Rehearsal and band nits](/features/rehearsal-and-band-nits.md)
