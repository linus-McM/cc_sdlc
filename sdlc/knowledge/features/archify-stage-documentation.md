---
type: Feature
title: Archify stage documentation
description: "Every sdlc stage ends with a human accepting a markdown artifact (intent.md, spec.md, plan.md,"
resource: sdlc/archify-stage-documentation
tags: [feature, accepted]
status: stable
generated: { by: sdlc/0.2.1, at: "2026-09-09T01:29:56Z" }
stale_after: "2026-09-23T01:29:56Z"
source_commit: b6e8d5897548ac1aeadd713c4fd9bf19fac3d435
sources:
  - { id: intent, resource: sdlc/archify-stage-documentation/intent.md, last_modified: "2026-09-09T01:29:56Z", digest: 58b7f8942bd9219b }
verified:
  - { by: "human:linus-mcmanamey", at: "2026-09-09T01:29:56Z" }
---

# Problem
Every sdlc stage ends with a human accepting a markdown artifact (intent.md, spec.md, plan.md,
review.md, deploy.json). The acceptor reads raw markdown in a terminal or in a PR diff. Nothing
shows the shape of what is being accepted: which systems an intent touches, how the spec's data
moves, which plan steps depend on which, how the deploy tiers and rollback path chain together.
For anything beyond a small change the product owner cannot see the whole picture, so acceptance
is either slow (read everything) or rubber-stamped (read the summary). Reviewers of the PR see
the same wall of text.

The Archify skill (https://github.com/tt-a1i/archify, MIT) already renders validated
architecture, workflow, sequence, dataflow and lifecycle diagrams as standalone HTML from a small
JSON spec. It is installed on this machine by hand under `~/.claude/skills/archify/`, but the
plugin does not know about it: a fresh clone or another developer's machine has Graphify
installed and reported by the SessionStart hook, and Archify absent and silent. Stage commands
cannot rely on a tool the bootstrap does not guarantee.

Affected today: the product owner and tech lead who accept artifacts, the engineer who explains
them, and anyone reviewing the PR that `/sdlc:deploy` opens.

# Outcome
1. Archify becomes a bootstrap step like Graphify. `sdlc knowledge bootstrap` (and therefore the
   SessionStart hook) checks for `~/.claude/skills/archify/bin/archify.mjs` and Node >= 18; when
   `[knowledge] auto_install` is on and the skill is missing it installs it with the repo's own
   command (`npx skills add tt-a1i/archify -g`, non-interactive form), otherwise reports it as
   `missing` with the command to run. Missing Node never blocks the rest of the bootstrap or any
   stage; it is reported and stage docs are skipped with a reason.
2. Each stage's accept produces a stage document. When `sdlc <stage> check` passes, the stage
   command asks Claude to author one Archify JSON spec from the stage artifact, validates and
   delivers it with `archify.mjs deliver ... --quality showcase --json`, and writes
   `sdlc/<slug>/docs/<stage>.html` plus the JSON source next to it. Suggested diagram per stage
   (the design stage settles this): plan = architecture map of affected users and systems;
   design = dataflow or architecture of the spec; build = workflow of plan steps and their TDD
   gates; test = sequence of the feedback loop and review findings; deploy = lifecycle of tiers,
   gate and rollback; maintain = lifecycle of bands and the intent they write.
3. Acceptance reads the document. `sdlc <stage> accept` is blocked until the stage document
   exists and is newer than the artifact it describes (Python gate, hash of the source artifact
   recorded in the HTML's companion JSON). The accept prompt tells the acceptor where the HTML
   is, opens it locally (`bin/open-artifact.mjs`; no Artifact publishing), and only then asks
   for the yes. Missing Node, missing Archify or a failed `deliver` blocks `accept` with the
   error verbatim while `[docs] enabled = true`; `enabled = false` skips documents and the gate. The PR body
   from `/sdlc:deploy` links every stage document so reviewers get the same view.
4. Reference material for the design stage: `references/archify-repomix.md` (repomix pack of
   the Archify repo: SKILL.md, CLI, schemas, examples, contracts) and `references/README.md`
   (regenerate command, install path, CLI surface).

Better looks like: the acceptor opens one HTML page per stage, sees the diagram and a short
summary card, and says yes or asks for a correction before the gate lets `accept` run.

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
