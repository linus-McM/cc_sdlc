---
type: Module
title: bash
description: "Graphify community 56: sdlc/release-hook-hardening/review.md, sdlc/release-hook-hardening/spec.md, tests/test_hooks.py"
resource: ""
tags: [module, graphify]
status: draft
generated: { by: sdlc/0.5.0, at: "2026-09-26T05:22:30Z" }
stale_after: "2026-10-10T05:22:30Z"
source_commit: c5f64f8d3b9b5e3268754f626b7f2e958fd6415e
sources:
  - { id: review, resource: sdlc/release-hook-hardening/review.md, last_modified: "2026-09-09T15:03:27+10:00", digest: ed3f8ea859e0a2fd }
  - { id: spec, resource: sdlc/release-hook-hardening/spec.md, last_modified: "2026-09-09T15:03:27+10:00", digest: ceec7eaa899c3151 }
  - { id: test_hooks, resource: tests/test_hooks.py, last_modified: "2026-09-09T12:06:46+10:00", digest: 9dc3aa8cb5a97b01 }
---

# Files
- `sdlc/release-hook-hardening/review.md`
- `sdlc/release-hook-hardening/spec.md`
- `tests/test_hooks.py`

# Symbols
- Security (sdlc/release-hook-hardening/review.md:L9)
- Proof (sdlc/release-hook-hardening/spec.md:L34)
- test_pre_bash_denies_configured_release_command() (tests/test_hooks.py:L101)
- test_pre_bash_gated_names_come_from_config_only() (tests/test_hooks.py:L114)
- test_pre_bash_survives_bad_release_command_config() (tests/test_hooks.py:L120)
- bash() (tests/test_hooks.py:L18)
- denied() (tests/test_hooks.py:L22)
- test_pre_bash_production_gate() (tests/test_hooks.py:L64)
- test_pre_bash_ignores_prose_and_heredocs() (tests/test_hooks.py:L71)
- test_pre_bash_scans_every_command_line_outside_heredocs() (tests/test_hooks.py:L80)
- test_pre_bash_fallback_matches_tokens_not_text() (tests/test_hooks.py:L92)

# Depends on
- no EXTRACTED edges to other modules

# Inferred
- [Order of work](/modules/order-of-work-45.md)

# Features
- [Archify stage documentation](/features/archify-stage-documentation.md)
- [Dogfood fixes round two](/features/dogfood-fixes-round-two.md)
- [graph-selected repomix context packs](/features/graph-selected-repomix-context-packs.md)
- [Graphify and OKF knowledge base integration](/features/graphify-and-okf-knowledge-base-integration.md)
- [Rehearsal and band nits](/features/rehearsal-and-band-nits.md)
- [Release hook hardening](/features/release-hook-hardening.md)
