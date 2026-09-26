---
type: Module
title: conftest.py
description: "Graphify community 0: CLAUDE.md, plugin/README.md, sdlc/archify-stage-documentation/spec.md, sdlc/graph-selected-repomix-context-packs/plan.md, sdlc/graph-selected-repomix-context-packs/spec.md, tests"
resource: ""
tags: [module, graphify]
status: draft
generated: { by: sdlc/0.5.0, at: "2026-09-26T06:33:18Z" }
stale_after: "2026-10-10T06:33:18Z"
source_commit: 5c45a37edd0dc635576e390a1174bea9fad6d10b
sources:
  - { id: CLAUDE, resource: CLAUDE.md, last_modified: "2026-09-26T15:59:19+10:00", digest: 9ef0106f03b16707 }
  - { id: README, resource: plugin/README.md, last_modified: "2026-09-26T16:24:05+10:00", digest: 816c28888fc35408 }
  - { id: spec, resource: sdlc/archify-stage-documentation/spec.md, last_modified: "2026-09-09T15:03:27+10:00", digest: 6c2e2d1606d0fe5e }
  - { id: plan, resource: sdlc/graph-selected-repomix-context-packs/plan.md, last_modified: "2026-09-26T16:06:32+10:00", digest: bbace73703f81509 }
  - { id: spec, resource: sdlc/graph-selected-repomix-context-packs/spec.md, last_modified: "2026-09-26T09:27:53+10:00", digest: 39b0915a5020a08c }
  - { id: conftest, resource: tests/conftest.py, last_modified: "2026-09-26T16:23:50+10:00", digest: 44de9d075d1ea218 }
  - { id: test_maintain, resource: tests/test_maintain.py, last_modified: "2026-09-24T11:36:09+10:00", digest: 5e6dbf325688ebe8 }
---

# Files
- `CLAUDE.md`
- `plugin/README.md`
- `sdlc/archify-stage-documentation/spec.md`
- `sdlc/graph-selected-repomix-context-packs/plan.md`
- `sdlc/graph-selected-repomix-context-packs/spec.md`
- `tests/conftest.py`
- `tests/test_maintain.py`

# Symbols
- CLAUDE.md (CLAUDE.md:L1)
- sdlc plugin (CLAUDE.md:L1)
- Architecture (CLAUDE.md:L12)
- Things Claude gets wrong (CLAUDE.md:L24)
- Commands (CLAUDE.md:L5)
- Context packs (Repomix) (plugin/README.md:L50)
- Proof (sdlc/archify-stage-documentation/spec.md:L187)
- graph-selected-repomix-context-packs/plan.md (sdlc/graph-selected-repomix-context-packs/plan.md:L1)
- Plan: graph-selected repomix context packs (sdlc/graph-selected-repomix-context-packs/plan.md:L1)
- Risks (sdlc/graph-selected-repomix-context-packs/plan.md:L149)
- Proof (sdlc/graph-selected-repomix-context-packs/plan.md:L182)
- Files that change (sdlc/graph-selected-repomix-context-packs/plan.md:L4)
- Proof (sdlc/graph-selected-repomix-context-packs/spec.md:L265)
- conftest.py (tests/conftest.py:L1)
- toml_config() (tests/conftest.py:L105)
- _write() (tests/conftest.py:L106)
- FakeTools (tests/conftest.py:L135)
- Handle on the sandbox: `bin/` holds the fake tools and their call log,… (tests/conftest.py:L136)
- .__init__() (tests/conftest.py:L138)
- repo() (tests/conftest.py:L14)
- .calls() (tests/conftest.py:L141)
- .skill() (tests/conftest.py:L146)
- Fresh git repo with one commit; cwd and SDLC root point at it. (tests/conftest.py:L15)
- .skill_dir() (tests/conftest.py:L150)
- .uninstall() (tests/conftest.py:L153)
- sandbox() (tests/conftest.py:L162)
- A bare PATH (a temp `bin/` plus git and the system dirs), temp HOME and… (tests/conftest.py:L163)
- knowledge() (tests/conftest.py:L175)
- Knowledge layer on, with fake `uv` and `graphify` in the sandbox. (tests/conftest.py:L176)
- install_fake_archify() (tests/conftest.py:L216)
- write_fake_node() (tests/conftest.py:L225)
- docs_tools() (tests/conftest.py:L236)
- Stage documents on, with fake `node` and `npx` in the sandbox and a fake… (tests/conftest.py:L237)
- packs() (tests/conftest.py:L326)
- Context packs on (knowledge layer on too), with fake `repomix`, `npm` and `uv… (tests/conftest.py:L327)
- checkpoint_on() (tests/conftest.py:L33)
- Stage-boundary checkpoints on; list it before any `accepted_*` fixture so their… (tests/conftest.py:L34)
- run() (tests/conftest.py:L40)
- Invoke the CLI in-process; return its JSON result dict. (tests/conftest.py:L41)
- _run() (tests/conftest.py:L43)
- series() (tests/conftest.py:L61)
- accepted_intent() (tests/conftest.py:L81)
- accepted_spec() (tests/conftest.py:L89)
- accepted_plan() (tests/conftest.py:L97)
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
- [config](/modules/config.md)
- [docs.py](/modules/docs-py.md)
- [Order of work](/modules/order-of-work-25.md)
- [Order of work](/modules/order-of-work-8.md)
- [pathlib](/modules/pathlib.md)
- [test_plan_design.py](/modules/test-plan-design-py.md)

# Inferred
- [Blocked](/modules/blocked.md)
- [check](/modules/check.md)
- [docs.py](/modules/docs-py.md)
- [fail](/modules/fail.md)
- [hooks.py](/modules/hooks-py.md)
- [packs.py](/modules/packs-py.md)
- [pathlib](/modules/pathlib.md)
- [refresh](/modules/refresh.md)
- [require](/modules/require.md)
- [review](/modules/review.md)
- [watch](/modules/watch.md)

# Features
- [Archify stage documentation](/features/archify-stage-documentation.md)
- [Dogfood fixes round two](/features/dogfood-fixes-round-two.md)
- [graph-selected repomix context packs](/features/graph-selected-repomix-context-packs.md)
- [Graphify and OKF knowledge base integration](/features/graphify-and-okf-knowledge-base-integration.md)
- [Rehearsal and band nits](/features/rehearsal-and-band-nits.md)
