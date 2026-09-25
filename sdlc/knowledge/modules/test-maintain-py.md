---
type: Module
title: test_maintain.py
description: "Graphify community 25: tests/conftest.py, tests/test_maintain.py"
resource: tests
tags: [module, graphify]
status: draft
generated: { by: sdlc/0.5.0, at: "2026-09-25T23:27:53Z" }
stale_after: "2026-10-09T23:27:53Z"
source_commit: 1348ec2a58c87325a8bcaacd936bc4bc9473c870
sources:
  - { id: conftest, resource: tests/conftest.py, last_modified: "2026-09-24T11:36:09+10:00", digest: 808a9c4cb9a6aeab }
  - { id: test_maintain, resource: tests/test_maintain.py, last_modified: "2026-09-24T11:36:09+10:00", digest: 5e6dbf325688ebe8 }
---

# Files
- `tests/conftest.py`
- `tests/test_maintain.py`

# Symbols
- series() (tests/conftest.py:L59)
- test_maintain.py (tests/test_maintain.py:L1)
- test_western_electric_rules_classify_tiers() (tests/test_maintain.py:L19)
- test_tier_needs_enough_history() (tests/test_maintain.py:L24)
- test_watch_reads_bad_side_and_rejects_unknown() (tests/test_maintain.py:L41)
- test_watch_reads_bands_and_reports_actions() (tests/test_maintain.py:L51)
- test_watch_honours_custom_bands() (tests/test_maintain.py:L63)
- test_propose_writes_intent_and_closes_loop() (tests/test_maintain.py:L70)
- test_propose_refuses_below_threshold() (tests/test_maintain.py:L81)
- test_ingest_appends_metric() (tests/test_maintain.py:L86)
- test_lesson_appends_to_lessons_md() (tests/test_maintain.py:L92)

# Depends on
- [hooks.py](/modules/hooks-py.md)
- [Order of work](/modules/order-of-work.md)
- [rel_path](/modules/rel-path.md)

# Inferred
- no INFERRED edges; treat any that appear as hints

# Features
- [Archify stage documentation](/features/archify-stage-documentation.md)
- [Dogfood fixes round two](/features/dogfood-fixes-round-two.md)
- [Graphify and OKF knowledge base integration](/features/graphify-and-okf-knowledge-base-integration.md)
- [Rehearsal and band nits](/features/rehearsal-and-band-nits.md)
