---
type: Module
title: test_deploy.py
description: "Graphify community 25: sdlc/dogfood-fixes-round-two/spec.md, sdlc/rehearsal-and-band-nits/plan.md, sdlc/rehearsal-and-band-nits/review.md, sdlc/rehearsal-and-band-nits/spec.md, tests/conftest.py, test"
resource: ""
tags: [module, graphify]
status: draft
generated: { by: sdlc/0.8.1, at: "2026-09-28T22:57:53Z" }
stale_after: "2026-10-12T22:57:53Z"
source_commit: 0754d821fc594b90c529849cddaca10dc6109921
sources:
  - { id: spec, resource: sdlc/dogfood-fixes-round-two/spec.md, last_modified: "2026-09-09T15:03:27+10:00", digest: 79ecdc49d82b1fc2 }
  - { id: plan, resource: sdlc/rehearsal-and-band-nits/plan.md, last_modified: "2026-09-09T15:03:27+10:00", digest: 688912ed38722c04 }
  - { id: review, resource: sdlc/rehearsal-and-band-nits/review.md, last_modified: "2026-09-09T15:03:27+10:00", digest: 370e4dd8c100bf71 }
  - { id: spec, resource: sdlc/rehearsal-and-band-nits/spec.md, last_modified: "2026-09-09T15:03:27+10:00", digest: b81cd9d3882a7703 }
  - { id: conftest, resource: tests/conftest.py, last_modified: "2026-09-26T16:35:55+10:00", digest: 44de9d075d1ea218 }
  - { id: test_deploy, resource: tests/test_deploy.py, last_modified: "2026-09-19T23:30:10+10:00", digest: dbfb47118be6302a }
  - { id: test_maintain, resource: tests/test_maintain.py, last_modified: "2026-09-24T11:36:09+10:00", digest: 5e6dbf325688ebe8 }
---

# Files
- `sdlc/dogfood-fixes-round-two/spec.md`
- `sdlc/rehearsal-and-band-nits/plan.md`
- `sdlc/rehearsal-and-band-nits/review.md`
- `sdlc/rehearsal-and-band-nits/spec.md`
- `tests/conftest.py`
- `tests/test_deploy.py`
- `tests/test_maintain.py`

# Symbols
- dogfood-fixes-round-two/spec.md (sdlc/dogfood-fixes-round-two/spec.md:L1)
- Spec: Dogfood fixes round two (sdlc/dogfood-fixes-round-two/spec.md:L1)
- Concerns (sdlc/dogfood-fixes-round-two/spec.md:L19)
- Open questions (sdlc/dogfood-fixes-round-two/spec.md:L22)
- Proof (sdlc/dogfood-fixes-round-two/spec.md:L25)
- rehearsal-and-band-nits/plan.md (sdlc/rehearsal-and-band-nits/plan.md:L1)
- Plan: Rehearsal and band nits (sdlc/rehearsal-and-band-nits/plan.md:L1)
- Files that change (sdlc/rehearsal-and-band-nits/plan.md:L4)
- Risks (sdlc/rehearsal-and-band-nits/plan.md:L43)
- Proof (sdlc/rehearsal-and-band-nits/plan.md:L54)
- rehearsal-and-band-nits/review.md (sdlc/rehearsal-and-band-nits/review.md:L1)
- Review: Rehearsal and band nits (sdlc/rehearsal-and-band-nits/review.md:L1)
- Compliance (sdlc/rehearsal-and-band-nits/review.md:L12)
- Bugs (sdlc/rehearsal-and-band-nits/review.md:L4)
- Security (sdlc/rehearsal-and-band-nits/review.md:L8)
- rehearsal-and-band-nits/spec.md (sdlc/rehearsal-and-band-nits/spec.md:L1)
- Spec: Rehearsal and band nits (sdlc/rehearsal-and-band-nits/spec.md:L1)
- Concerns (sdlc/rehearsal-and-band-nits/spec.md:L20)
- Open questions (sdlc/rehearsal-and-band-nits/spec.md:L23)
- Proof (sdlc/rehearsal-and-band-nits/spec.md:L26)
- series() (tests/conftest.py:L61)
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
- test_deploy_rehearse_runs_in_throwaway_worktree() (tests/test_deploy.py:L56)
- test_deploy_rehearse_needs_git() (tests/test_deploy.py:L66)
- test_deploy_rehearse_reports_leftover_worktree() (tests/test_deploy.py:L72)
- flaky() (tests/test_deploy.py:L75)
- test_deploy_rehearse_runs_at_project_path() (tests/test_deploy.py:L87)
- A project that is a subdirectory of the repo rehearses at that same… (tests/test_deploy.py:L88)
- test_maintain.py (tests/test_maintain.py:L1)
- test_western_electric_rules_classify_tiers() (tests/test_maintain.py:L19)
- test_tier_needs_enough_history() (tests/test_maintain.py:L24)
- test_tier_rejects_unknown_side() (tests/test_maintain.py:L28)
- test_tier_one_sided_bands_ignore_the_good_side() (tests/test_maintain.py:L33)
- test_watch_reads_bad_side_and_rejects_unknown() (tests/test_maintain.py:L41)
- test_watch_reads_bands_and_reports_actions() (tests/test_maintain.py:L51)
- test_watch_honours_custom_bands() (tests/test_maintain.py:L63)
- test_propose_writes_intent_and_closes_loop() (tests/test_maintain.py:L70)
- test_propose_refuses_below_threshold() (tests/test_maintain.py:L81)
- test_ingest_appends_metric() (tests/test_maintain.py:L86)
- test_lesson_appends_to_lessons_md() (tests/test_maintain.py:L92)

# Depends on
- [conftest.py](/modules/conftest-py.md)
- [git](/modules/git.md)
- [hooks.py](/modules/hooks-py.md)
- [Order of work](/modules/order-of-work.md)
- [Order of work](/modules/order-of-work-11.md)
- [pathlib](/modules/pathlib.md)
- [project.py](/modules/project-py.md)
- [watch](/modules/watch.md)

# Inferred
- [Blocked](/modules/blocked.md)
- [conftest.py](/modules/conftest-py.md)
- [git](/modules/git.md)
- [test_hooks.py](/modules/test-hooks-py.md)
- [watch](/modules/watch.md)

# Features
- [Archify stage documentation](/features/archify-stage-documentation.md)
- [Dogfood fixes round two](/features/dogfood-fixes-round-two.md)
- [graph-selected repomix context packs](/features/graph-selected-repomix-context-packs.md)
- [Graphify and OKF knowledge base integration](/features/graphify-and-okf-knowledge-base-integration.md)
- [Rehearsal and band nits](/features/rehearsal-and-band-nits.md)
