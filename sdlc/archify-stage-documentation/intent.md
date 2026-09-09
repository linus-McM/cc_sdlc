# Intent: Archify stage documentation
Author: Linus McManamey. Status: accepted. Risk: low.

## Problem
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

## Proposed outcome
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

## Affected users and systems
- Product owner / tech lead: accept prompts now point at a document; nothing else changes.
- Engineer: one more generated artifact per stage; regenerated on demand, never edited by hand.
- PR reviewers: links to the stage documents in the PR body.
- `scripts/sdlc/knowledge.py` STEPS table (new `archify` step), `hooks.py` session_start report,
  `stages.py` accept gate, `deploy.py` PR body, `commands/*.md` (call the mechanic, report the
  verdict), `templates/`, `tests/` (new fixture that puts fake `node`/`npx`/archify on PATH).
- `.sdlc.toml`: new `[docs]` table (`enabled`, `open` on/off) alongside `[knowledge]`.
- Runtime: Node >= 18 becomes an optional dependency of the plugin; Python stays stdlib-only.

## Constraints
- Python does the gating; markdown only says which mechanic to call. No verdict logic in prose.
- Generated documents are drafts: they never carry a `human:` verification and never write into
  `sdlc/knowledge/` concepts; only `accept` publishes.
- Tests never reach the real `npx`, `node` or Archify: a fixture stubs them like the `knowledge`
  fixture stubs `uv` and `graphify`; suites run with `SDLC_DOCS=off` unless they take it.
- Installing a third-party npm package from a SessionStart hook is a supply-chain decision: it
  only happens when `[knowledge] auto_install = true` (this repo dogfoods it); default is
  check-only with the command printed. The install command is the one the upstream README
  documents (`npx -y skills add tt-a1i/archify --skill archify --agent claude-code --global
  --copy --yes`); the skills CLI has no version flag, so bootstrap records the installed
  `skill-release.json` version and status reports drift instead of pinning.
- Archify's delivery contract is the acceptance bar: a non-zero `deliver` exit is a failed
  document, reported verbatim, never described as success; showcase profile, zero warnings.
- Stage documents live under `sdlc/<slug>/docs/`, are committed with the stage artifact, and
  are excluded from the Graphify graph (`.graphifyignore`) like `references/`.
- Keep stage runtime small: one diagram per stage, at most 12 primary nodes; the summary card
  comes from the artifact's own sections, not new prose.
- Hooks stay under the existing timeouts; document generation runs in the stage command, not in
  a hook.

## Open questions
None. Closed with the originator on 2026-09-09:
- Display: local standalone HTML under `sdlc/<slug>/docs/`, opened through Archify's
  `bin/open-artifact.mjs`; the PR body links it. No Claude Code Artifact publishing.
- Missing Node/Archify or a failed `deliver`: `accept` is blocked with the error verbatim while
  `[docs] enabled = true`; `[docs] enabled = false` skips documents and the gate entirely.
- Version pin: `npx skills add` (skills CLI 1.5.25) has no version flag, so the install takes
  latest; bootstrap records the installed `skill-release.json` version in its report and
  `sdlc knowledge status` flags drift from the version recorded in `references/README.md`.
