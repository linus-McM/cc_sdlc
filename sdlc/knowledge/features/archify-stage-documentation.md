---
type: Feature
title: Archify stage documentation
description: "Every sdlc stage ends with a human accepting a markdown artifact (intent.md, spec.md, plan.md,"
resource: sdlc/archify-stage-documentation
tags: [feature, accepted]
status: draft
generated: { by: sdlc/0.2.2, at: "2026-09-09T04:39:18Z" }
verified:
  - { by: "human:linus-mcmanamey", at: "2026-09-09T01:29:56Z" }
  - { by: "human:linus-mcmanamey", at: "2026-09-09T01:48:10Z" }
  - { by: "human:linus-mcmanamey", at: "2026-09-09T01:52:55Z" }
  - { by: "process:sdlc-test", at: "2026-09-09T02:33:31Z" }
  - { by: "process:sdlc-test", at: "2026-09-09T02:45:24Z" }
  - { by: "process:sdlc-test", at: "2026-09-09T03:02:28Z" }
stale_after: "2026-09-23T04:39:18Z"
source_commit: fa36f67b2362d73bcbf588271a14e115f96d2a3d
sources:
  - { id: intent, resource: sdlc/archify-stage-documentation/intent.md, last_modified: "2026-09-09T11:30:11+10:00", digest: 58b7f8942bd9219b }
  - { id: spec, resource: sdlc/archify-stage-documentation/spec.md, last_modified: "2026-09-09T13:02:29+10:00", digest: 6c2e2d1606d0fe5e }
  - { id: plan, resource: sdlc/archify-stage-documentation/plan.md, last_modified: "2026-09-09T13:02:29+10:00", digest: c94b9c651a152ddc }
  - { id: review, resource: sdlc/archify-stage-documentation/review.md, last_modified: "2026-09-09T13:02:29+10:00", digest: c333272d4dfcf4c6 }
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
Traced to intent.md Proposed outcome items (PO1..PO4). "Verdict" means the one JSON dict
`cli.main` returns. "Skill dir" means `$CLAUDE_CONFIG_DIR/skills/archify` (default
`~/.claude/skills/archify`), the same base `knowledge.skill_path` uses.

1. (PO1) `[docs]` is a new table in `project.DEFAULT_CONFIG`: `enabled = true`, `dir = "docs"`
   (per-feature subdirectory), `quality = "showcase"`, `open = true` (open the HTML locally at
   accept time), `min_node = 18`, `min_version = "2.17"` (lowest Archify skill version the
   authoring guidance in `commands/*.md` was written against), `types` mapping stage to
   diagram type: `plan = "architecture"`, `design = "dataflow"`, `build = "workflow"`,
   `test = "sequence"`, `deploy = "lifecycle"`, `maintain = "lifecycle"`. `[docs] enabled =
   false` or `SDLC_DOCS=off` turns every `docs` mechanic into `{"ok": true, "skipped": "docs
   disabled"}` and removes every gate below (mirrors `knowledge.when_enabled`).
2. (PO1) `knowledge.STEPS` gains one step named `archify`, placed after `skill` and before
   `hooks`. Present when `<skill dir>/bin/archify.mjs` exists. Its present-check may raise
   `StepSkipped`: when docs are disabled (detail `docs disabled`) or when `node` is absent or
   `node --version` reports a major below `[docs] min_node` (detail names the found version and
   the install command). `bootstrap` treats a `StepSkipped` from a present-check as state
   `skipped` in both `check` and install mode, and later steps still run. In `check` mode a
   missing skill is state `missing` with the install command in `detail`; in install mode the
   step runs `npx -y skills add tt-a1i/archify --skill archify --agent claude-code --global
   --copy --yes` through `project.ran` only when `[knowledge] auto_install` is true (reconciled
   during test to the supply-chain concern: otherwise `skipped` naming the command and the
   setting) and is `installed` only when `bin/archify.mjs` exists afterwards, else `failed`
   with the stderr tail. `detail` of a present or installed step is
   `Archify skill <version>` where version is read from `<skill dir>/skill-release.json`
   (`unknown` when unreadable). The SessionStart hook needs no change: it prints the step list.
3. (PO1) `sdlc knowledge status` adds `archify: {installed: bool, version: str | null,
   min_version: str}` to its verdict and appends a note (not a reason; `ok` is unaffected)
   `archify <version> is older than [docs] min_version <min>` when the installed version tuple
   is lower. No network call is made anywhere in the plugin to learn the latest version.
4. (PO2) New module `scripts/sdlc/docs.py` (stdlib only) owns: `cfg`, `enabled`, `skill_dir`,
   `node_version`, `sources(stage, feature)`, `digest(root, sources)`, `render`, `check`,
   `open`. Sources per stage, relative to the feature directory unless noted:
   `plan: intent.md`; `design: spec.md`; `build: plan.md`; `test: review.md, test-report.json`;
   `deploy: pr-body.md`; `maintain: sdlc/bands.toml` (repo-relative; maintain has no feature).
   `digest` is the sha256 hex of the concatenated source bytes, each prefixed by its path.
5. (PO2) Claude authors the diagram source at `<feature>/<dir>/<stage>.json` (maintain:
   `sdlc/<dir>/maintain.json`) following the Archify skill fast path; `sdlc docs render <stage>
   [--slug]` then runs `node <skill dir>/bin/archify.mjs deliver <type> <stage>.json
   <stage>.html --quality <quality> --json` with `ARCHIFY_UPDATE_CHECK_DISABLED=1` in the
   environment and cwd at the docs directory, parses the receipt JSON from stdout, and writes
   `<stage>.receipt.json` = `{stage, type, sources: [{resource, digest}], source_digest,
   specification_sha256, artifact_sha256, validation, archify_version, delivered_at}`.
   Verdict: `{ok: true, html, receipt, validation}`. Missing `<stage>.json` fails with
   `stage document source missing; author <path> from <sources> (Archify <type>), then rerun`.
   A non-zero `deliver` exit fails with `archify deliver exited <n>: <last 400 chars of stderr
   or stdout>` and `<stage>.html` is left as Archify left it (previous trusted artifact or
   absent); the verdict never calls a failed delivery a success. Absent `node` or skill fails
   with the bootstrap install command in `reason`.
6. (PO3) `docs.check(root, feature, stage)` returns `{ok: true, html, fresh: true}` when
   `<stage>.html` and `<stage>.receipt.json` exist and the receipt's `source_digest` equals the
   digest of the current sources. It fails `stage document missing; author <stage>.json, then
   `sdlc docs render <stage>`` when either file is absent, and `stage document is stale:
   <changed resources> changed since <stage>.html was delivered; rerun `sdlc docs render
   <stage>`` when the digest differs. `sdlc docs check <stage>` exposes it.
7. (PO3) Gates, all through `docs.check` (the skipped verdict when disabled; reconciled during test):
   `stages.accept` for plan, design and build calls it before writing `Status: accepted`;
   `testing.review` calls it for `test` after validating review.md; `deploy.record` calls it
   for `deploy` before appending the deployment. Each blocked verdict carries the `check`
   reason verbatim. `sdlc docs render maintain` has no gate (maintain is a watch loop, not an
   acceptance); `maintain.watch` adds `docs: "<reason>"` to its verdict when the maintain
   document is missing or stale, and nothing else changes.
8. (PO3) `sdlc docs open <stage> [--slug]` runs `node <skill dir>/bin/open-artifact.mjs
   <stage>.html` when `[docs] open` is true and the environment variable `CI` is unset, and
   returns `{ok: true, html, opened: bool, reason?}`; it never fails on an opener error (the
   acceptor still gets the path). `commands/*.md` call it right before the AskUserQuestion that
   asks for acceptance and quote the HTML path in the question.
9. (PO3) `deploy.pr_body` adds a `### Documents` section listing every `<feature>/<dir>/*.html`
   present, one bullet `- <stage>: sdlc/<slug>/<dir>/<stage>.html (<validation>)` from the
   matching receipt, or `- none` when the directory is empty.
10. (PO2) Authoring guidance lives in `commands/*.md`, not in Python: each stage command gains a
    `docs` step that names the diagram type, the artifact sections to read, the node budget (at
    most 12 primary nodes), the required summary card `Generated by sdlc from <source> @
    <first 12 of source_digest>; drafts are Claude's reading of the artifact, the acceptor
    decides`, `meta.quality_profile: "showcase"`, and the command sequence `sdlc docs render
    <stage>` then `sdlc docs open <stage>`. The per-stage reading: plan = affected users and
    systems from Affected users and systems plus Problem (architecture); design = data flow
    between the components named in Design (dataflow); build = Order of work steps with their
    red/green tests (workflow); test = the run, verifier and reviewer exchange with finding
    counts (sequence); deploy = environments, gates, rehearsal and rollback (lifecycle);
    maintain = band tiers and the actions they trigger (lifecycle). A `deliver` failure is
    repaired in the JSON source only, at most two rounds, then reported.
11. (PO4) `[knowledge] ignore` default gains `sdlc/*/docs/` and `sdlc/docs/`, so `write_ignore`
    keeps generated HTML out of the Graphify graph; `knowledge.refresh` treats the docs
    directory like `references/` (no concept, no source). `features/<slug>.md` concepts gain a
    `# Documents` section listing the delivered stage documents (path plus validation) when the
    directory exists; empty otherwise. Generation still never writes a `human:` event.
12. (PO4) `README.md` documents the `[docs]` table, the `archify` bootstrap step, the gate, the
    off switches (`[docs] enabled = false`, `SDLC_DOCS=off`, `CI` suppresses opening) and the
    supply-chain note; `CLAUDE.md` Architecture lists `docs.py`; `hooks/hooks.json` is unchanged.

# Files
- `.pre-commit-config.yaml`
- `CLAUDE.md`
- `README.md`
- `commands/build.md`
- `commands/deploy.md`
- `commands/design.md`
- `commands/maintain.md`
- `commands/plan.md`
- `commands/test.md`
- `scripts/sdlc/cli.py` in [project.py](/modules/project-py.md)
- `scripts/sdlc/deploy.py` in [docs.py](/modules/docs-py.md)
- `scripts/sdlc/docs.py` in [docs.py](/modules/docs-py.md)
- `scripts/sdlc/hooks.py` in [hooks.py](/modules/hooks-py.md)
- `scripts/sdlc/knowledge.py` in [Path](/modules/path.md)
- `scripts/sdlc/maintain.py` in [project.py](/modules/project-py.md)
- `scripts/sdlc/project.py` in [Path](/modules/path.md)
- `scripts/sdlc/stages.py` in [docs.py](/modules/docs-py.md)
- `scripts/sdlc/testing.py` in [docs.py](/modules/docs-py.md)
- `sdlc/archify-stage-documentation/docs/`
- `tests/conftest.py` in [run](/modules/run.md)
- `tests/test_docs.py` in [test_docs.py](/modules/test-docs-py.md)
- `tests/test_hooks.py` in [toml_config](/modules/toml-config.md)
- `tests/test_knowledge.py` in [run](/modules/run.md)

# Review
- Important: 5, Nit: 11

# Status
- intent.md: accepted
- spec.md: accepted
- plan.md: accepted
- test-report: passed
- deployed: dev, staging

# Documents
- build: sdlc/archify-stage-documentation/docs/build.html (9/9 showcase, 0 errors, 0 warnings)
- deploy: sdlc/archify-stage-documentation/docs/deploy.html (9/9 showcase, 0 errors, 0 warnings)
- design: sdlc/archify-stage-documentation/docs/design.html (9/9 showcase, 0 errors, 0 warnings)
- test: sdlc/archify-stage-documentation/docs/test.html (9/9 showcase, 0 errors, 0 warnings)
