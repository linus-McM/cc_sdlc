---
type: Module
title: __init__.py
description: "Graphify community 68: scripts/sdlc/__init__.py, tests/test_artifacts.py, tests/test_maintain.py"
resource: ""
tags: [module, graphify]
status: draft
generated: { by: sdlc/0.2.1, at: "2026-09-09T03:05:50Z" }
stale_after: "2026-09-23T03:05:50Z"
source_commit: f99c31fe37e72ede2fd21532a6ffb7137b40bc9e
sources:
  - { id: __init__, resource: scripts/sdlc/__init__.py, last_modified: "2026-09-07T12:20:58+10:00", digest: 0a6aea3cd6840dbf }
  - { id: test_artifacts, resource: tests/test_artifacts.py, last_modified: "2026-09-09T07:44:17+10:00", digest: de801493819374a5 }
  - { id: test_maintain, resource: tests/test_maintain.py, last_modified: "2026-09-08T15:49:55+10:00", digest: 31af1cddd1d1bc15 }
---

# Files
- `scripts/sdlc/__init__.py`
- `tests/test_artifacts.py`
- `tests/test_maintain.py`

# Symbols
- __init__.py (scripts/sdlc/__init__.py:L1)
- sdlc — deterministic gates for the six-stage AI-native SDLC. Stdlib only. (scripts/sdlc/__init__.py:L1)
- test_artifacts.py (tests/test_artifacts.py:L1)
- test_meta_roundtrip() (tests/test_artifacts.py:L13)
- test_set_section_replaces_only_that_body() (tests/test_artifacts.py:L20)
- test_glob_semantics() (tests/test_artifacts.py:L26)
- test_validate_reports_missing_and_placeholder_sections() (tests/test_artifacts.py:L34)
- test_slugify_collapses_punctuation_and_case() (tests/test_artifacts.py:L4)
- test_validate_passes_complete_document() (tests/test_artifacts.py:L40)
- test_list_items_parses_bullets_and_commas() (tests/test_artifacts.py:L45)
- test_list_items_keeps_dotfile_paths() (tests/test_artifacts.py:L50)
- test_sections_parse_headings_to_bodies() (tests/test_artifacts.py:L8)
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
- no EXTRACTED edges to other modules

# Inferred
- [run](/modules/run.md)

# Features
- [Dogfood fixes round two](/features/dogfood-fixes-round-two.md)
- [Graphify and OKF knowledge base integration](/features/graphify-and-okf-knowledge-base-integration.md)
- [Rehearsal and band nits](/features/rehearsal-and-band-nits.md)
