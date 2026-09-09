---
type: Module
title: test_maintain.py
description: "Graphify community 1: tests/test_maintain.py"
resource: tests
tags: [module, graphify]
status: draft
generated: { by: sdlc/0.2.0, at: "2026-09-09T01:00:05Z" }
stale_after: "2026-09-23T01:00:05Z"
source_commit: 54c0f199832a483cbfe12eff9d0b86d35ecd49a4
sources:
  - { id: test_maintain, resource: tests/test_maintain.py, last_modified: "2026-09-08T15:49:55+10:00", digest: 31af1cddd1d1bc15 }
---

# Files
- `tests/test_maintain.py`

# Symbols
- test_maintain.py (tests/test_maintain.py:L1)
- test_lesson_appends_to_lessons_md() (tests/test_maintain.py:L101)
- test_western_electric_rules_classify_tiers() (tests/test_maintain.py:L28)
- test_tier_needs_enough_history() (tests/test_maintain.py:L33)
- test_tier_rejects_unknown_side() (tests/test_maintain.py:L37)
- test_tier_one_sided_bands_ignore_the_good_side() (tests/test_maintain.py:L42)
- test_watch_reads_bad_side_and_rejects_unknown() (tests/test_maintain.py:L50)
- test_watch_reads_bands_and_reports_actions() (tests/test_maintain.py:L60)
- test_watch_honours_custom_bands() (tests/test_maintain.py:L72)
- test_propose_writes_intent_and_closes_loop() (tests/test_maintain.py:L79)
- series() (tests/test_maintain.py:L9)
- test_propose_refuses_below_threshold() (tests/test_maintain.py:L90)
- test_ingest_appends_metric() (tests/test_maintain.py:L95)

# Depends on
- [fail](/modules/fail.md)

# Inferred
- [run](/modules/run.md)

# Features
- [Dogfood fixes round two](/features/dogfood-fixes-round-two.md)
- [Rehearsal and band nits](/features/rehearsal-and-band-nits.md)
