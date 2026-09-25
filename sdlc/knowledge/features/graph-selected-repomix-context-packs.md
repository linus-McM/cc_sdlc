---
type: Feature
title: graph-selected repomix context packs
description: "Each stage's parallel Workflow agents (intent-scout, design-panel, plan-critic, review,"
resource: sdlc/graph-selected-repomix-context-packs
tags: [feature, accepted]
status: stable
generated: { by: sdlc/0.5.0, at: "2026-09-25T07:58:30Z" }
stale_after: "2026-10-09T07:58:30Z"
source_commit: dc32a5b78bc303376f02bfe7d43360ae82fa4a82
sources:
  - { id: intent, resource: sdlc/graph-selected-repomix-context-packs/intent.md, last_modified: "2026-09-25T07:58:30Z", digest: 119529ab975a409b }
verified:
  - { by: "human:linus-mcmanamey", at: "2026-09-25T07:58:30Z" }
---

# Problem
Each stage's parallel Workflow agents (intent-scout, design-panel, plan-critic, review,
release-readiness, diagnose) work out their own view of the codebase at run time: each one reads
`sdlc/knowledge/index.md`, runs `graphify query`, then greps and reads files on its own
(`plugin/commands/*.md:8`, `plugin/workflows/*.js`). The same files are re-read by every agent in a
panel, and the agents of one stage are not guaranteed to judge the same code. The graph already
knows which files a change touches, but nothing turns that into a file set, and nothing packs those
files so a panel can share them. Repomix is used only by hand, to pack external reference repos
(`sdlc/archify-stage-documentation/references/README.md`). An earlier measurement found the
knowledge bundle plus `graphify query` cost 1.06x the tokens of raw reads
(`docs/knowledge-measurement.md`), so the map alone has not yet paid for itself.

# Outcome
A mechanic `sdlc knowledge pack <slug> <stage>` builds one Repomix pack per stage, which is a
commit-pinned snapshot that every Workflow agent of that stage shares:
- Seeds come from the stage artifact: the systems named in intent.md, the modules in spec.md, the
  planned files in plan.md, the diff at test, and the files changed since the last deploy at
  maintain.
- The seeds are expanded one hop through `graphify-out/graph.json`: callers, callees and the
  community.
- The file set is packed with Repomix. There is no default token budget. The user may set one as a
  parameter (`--max-tokens`, or `[knowledge] pack_max_tokens`). When a set budget is exceeded, the
  pack moves to `--compress` and then to seeds only, and the verdict reports each step down; files
  are never cut silently.
- Packs are written to `graphify-out/packs/` (ignored, never committed or checkpointed) and keyed
  by HEAD plus the file set, so a repeat call reuses the pack. The mechanic refuses when the graph
  is behind HEAD.
- Stage commands run it after `<stage> new` and pass the pack path to their Workflow. Workflows stay
  read-only.
- The Plan and Test stages depend on a pack. `plan accept` and `test review` are refused until a
  pack for the slug and stage exists and was built at the current HEAD. At `test review` the pack
  is also re-checked against the branch diff: every changed file must be in the pack, or the review
  is refused and names the missing files. The other stages use packs
  as advisory context, and Deploy does not build one.

# Requirements
- spec.md not written yet

# Files
- plan.md not written yet

# Review
- no review yet

# Status
- intent.md: accepted
- spec.md: missing
- plan.md: missing
- test-report: missing or failed
- deployed: nowhere

# Documents
- plan: sdlc/graph-selected-repomix-context-packs/docs/plan.html (9/9 showcase, 0 errors, 0 warnings)
