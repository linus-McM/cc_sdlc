# Intent: Graphify and OKF knowledge base integration
Author: Linus McManamey. Status: accepted. Risk: high.

## Problem
Every sdlc session re-derives the shape of the codebase from raw file reads. Nothing persists
between stages or sessions except the markdown artifacts under `sdlc/<slug>/`, and those are
not indexed, cross-linked or queryable. Concretely, today:

1. Graphify (`graphifyy` 0.9.53, `~/.local/bin/graphify`) is installed on this machine but the
   plugin does not know it exists: no `graphify-out/graph.json` in the project, no Claude skill
   registered (`~/.claude/skills/graphify/` absent), no git hook (`graphify hook status` reports
   nothing). A graph built by hand would drift from the code on the next commit, and a stale
   structural graph gives high-confidence wrong answers with no signal that it is wrong
   (articles 4 and 7: silent hook failures, ghost nodes surviving `--update`, "already clean"
   false negatives).
2. There is no Open Knowledge Format (OKF) bundle. The knowledge the pipeline already produces
   (intent, spec, plan, review, `sdlc/lessons.md`, `sdlc/bands.toml`, `sdlc/metrics.jsonl`) is
   the curated narrative layer OKF exists to hold, but it has no `type` frontmatter, no
   `index.md` for progressive disclosure, no `log.md`, no provenance or freshness fields, so an
   agent cannot load it selectively and cannot tell current from stale or superseded.
3. Nothing bootstraps tooling when the plugin is first used in a project. A user running
   `/sdlc:plan new` in a fresh repo gets `.sdlc.toml` and nothing else; missing tools are
   discovered one at a time, by hand.
4. No mechanic re-indexes after a commit. The build stage commits every red-green step and the
   accept actions commit artifacts, yet none of those commits refresh any index, and nothing
   would tell anyone if a refresh had silently not happened.
5. Tooling gaps found while writing this intent: Graphify's Claude skill and git hooks not
   installed; plugin `hooks/hooks.json` has no `SessionStart` entry; the `graphify export
   --format okf` command article 4 describes does not exist in the installed 0.9.53 (no OKF
   exporter in `graphify/exporters/`; only `--wiki`), so OKF generation has to be ours; the
   superops `okf` Go CLI (`okf lint`, 13 rules) and `kiso` (OKF static publisher) are not
   installed; OpenWiki (Node, LLM-backed) is a possible alternative producer, not installed.

Affected: anyone running `/sdlc:*` in this or any other project (Linus today; whoever installs
the plugin later), and the reviewer and verifier agents that currently grep the tree cold.

## Proposed outcome
1. Bootstrap on first use. A new mechanic (working name `knowledge bootstrap`, exposed through
   `cli.py` like every other mechanic) runs from a new `SessionStart` hook in `hooks/hooks.json`
   and from the top of every stage command. Idempotent, returns one JSON verdict listing what it
   found, installed or skipped, as separate steps. It checks and, when missing, does: `uv tool
   install graphifyy`; `graphify install --platform claude` (skill registered for Claude Code);
   `graphify hook install` (git post-commit, post-checkout, merge driver); first build `graphify
   update .` when `graphify-out/graph.json` is absent; first OKF bundle generation when the
   bundle is absent. When everything is present it costs one config read and a few `stat` calls,
   no git, no LLM.
2. Re-index after every commit. Graphify's own post-commit hook (installed above) rebuilds
   `graphify-out/` detached, no LLM, logging to `~/.cache/graphify-rebuild.log`. The plugin adds
   its own step on the same trigger so the OKF bundle is regenerated from the fresh `graph.json`
   plus the sdlc artifacts, and `log.md` gets a dated entry. Which trigger the plugin owns (a
   marker-delimited block in the git post-commit hook next to Graphify's, or a `PostToolUse`
   Bash matcher on `git commit`) is a design decision; the outcome is that no commit made by any
   stage leaves either index stale without a visible record.
3. Freshness is observable, not assumed (article 4). A `knowledge status` mechanic compares
   `graph.json`'s `built_at_commit` and the bundle's recorded source commit against `HEAD`, checks
   the three Graphify artifacts agree with each other, reads the rebuild log's last line, and
   reports a staleness verdict in commits and hours. The bundle records an update counter; after
   a configurable number of incremental updates (default 5, article 7's 3-5) or when staleness
   exceeds a configurable age, the next bootstrap forces a clean rebuild instead of an
   incremental one and says so.
4. An OKF v0.2 bundle lives in the target project's repository beside the code, never in the
   plugin checkout and never in `CLAUDE.md`. Root is the project root every `sdlc` call already
   uses (cwd for commands, the hook payload's `cwd` for hooks), so it is the same place whether
   the user or Claude runs the command. Paths: bundle at `<project>/sdlc/knowledge/` (proposed,
   `[knowledge] bundle` in `.sdlc.toml`; see Open questions), committed; Graphify output at
   `<project>/graphify-out/` (Graphify's fixed path), proposed ignored; git hooks in the
   project's `.git/hooks/`; skill and tool under `~/.claude/skills/graphify/` and
   `~/.local/share/uv/tools/graphifyy`; rebuild log `~/.cache/graphify-rebuild.log`. Optionally
   one marker-delimited pointer line in the project's `CLAUDE.md` (OpenWiki's pattern) so
   sessions that never run `/sdlc:*` still find `sdlc/knowledge/index.md`.
   Conformance per SPEC.md §11: every concept has parseable frontmatter with a
   non-empty `type`; `index.md` and `log.md` follow §8 and §9. Concepts:
   - one per sdlc feature (`type: Feature`) synthesised from intent, spec, plan, review;
   - one per Graphify community and god node (`type: Module`, `type: Hub`) from `graph.json`,
     linking to the feature concepts whose `Files that change` touch them;
   - `type: Lesson` per entry of `sdlc/lessons.md`; `type: Control Band` per band in
     `sdlc/bands.toml`.
   Frontmatter: `generated: { by: sdlc/<plugin version>, at }`, `status: draft`, `sources`
   naming the source paths and the source commit (`source_commit` documented as an
   organisational extension), `stale_after` set from the next expected regeneration.
   Bundle-relative links form the graph. Reverse-dependency invalidation (article 7): on
   regeneration, any concept whose `sources` paths changed since its `source_commit` is marked
   `status: draft` again, not silently kept. Concepts for deleted or renamed things become
   `status: deprecated` tombstones with a replacement link; eviction fails closed (a concept is
   only tombstoned when its source path is confirmed absent).
5. Trust boundary (articles 3 and 8). The agent only drafts: it never writes a `verified` event
   with a `human:` actor. A human `accept` (plan, design, build) is the publisher event: the
   accept mechanic derives `verified: { by: human:<git author>, at }` for the matching Feature
   concept and promotes it to `status: stable`. Deterministic checks may add `process:` events.
   Official conformance, organisational policy (title, generated, source_commit required) and
   trust/freshness are reported as three separate lists in one verdict, never conflated.
   Lesson concepts carry scope (repository, feature, source commit) and a `supersedes` link so a
   later lesson demotes an earlier one instead of both being served as current.
6. Every stage consumes the knowledge before it reads raw files: stage commands read
   `index.md` first and prefer `graphify query` / `graphify affected` over grep for "what calls
   what" questions, respecting EXTRACTED versus INFERRED edge tags; the build post-edit hook names
   the concepts a changed file affects; test review runs the OKF conformance check and fails on
   official-conformance violations; deploy's PR body links the knowledge diff; maintain ingests
   graph and bundle metrics (node count, community count, stale-concept count, unverified-concept
   count, staleness in commits) into `metrics.jsonl` so the bands can watch knowledge freshness
   like any other production signal and write the next intent when it drifts.
7. Success measure: after `/sdlc:plan new` in a fresh clone the bootstrap verdict is `ok`, both
   `graphify-out/graph.json` and the bundle exist, `graphify hook status` reports installed, and
   after any stage commit both indexes carry that commit's hash. `knowledge status` reports a
   stale graph within one commit of it going stale. The conformance check passes on the bundle
   this repo generates for its own five features. A fixed set of five codebase questions answered
   from the bundle plus `graphify query` uses fewer input tokens than the same questions answered
   by raw reads, measured on the same commit, then again after a rename and a deletion (articles
   3 and 7's honest-measurement protocol); the result is recorded, not assumed.

## Affected users and systems
Linus and future plugin users; the `sdlc:reviewer` and `sdlc:verifier` agents.
Files: `hooks/hooks.json` (new `SessionStart`, possibly `PostToolUse` Bash), `scripts/sdlc/hooks.py`,
new `scripts/sdlc/knowledge.py` (bootstrap, status, bundle generation, invalidation, conformance
check, metrics), `scripts/sdlc/cli.py`, `scripts/sdlc/project.py` (new `[knowledge]` config table
with tool paths, bundle dir, rebuild cadence, opt-outs), `scripts/sdlc/stages.py` (accept publishes
`verified`), `scripts/sdlc/testing.py`, `scripts/sdlc/deploy.py`, `scripts/sdlc/maintain.py`,
`commands/*.md` (read index first, call bootstrap), `templates/` (OKF concept, index, log
skeletons), `tests/`, `README.md`, `.gitignore`, `.sdlc.toml`, `.pre-commit-config.yaml`
(large-file limit if `graph.json` is committed).
External systems: `uv tool` (installs `graphifyy`), the user's `~/.claude/skills/`, the
repository's `.git/hooks/` (or `core.hooksPath`), `.gitattributes` (Graphify merge driver),
`~/.cache/graphify-rebuild.log`.
Reference material for the design stage: `references/okf-repomix.md` (SPEC.md v0.2, README,
reference agent, sample bundles) and `references/article-notes.md` (nine articles, listed in
`references/README.md`).

## Constraints
- Plugin stays stdlib-only Python 3.11+. Graphify and any other tool are invoked as
  subprocesses through `project.run_git`-style helpers; no import of `graphify`. `uv` is the
  only installer assumed; when `uv` is absent the bootstrap reports it and stops, it does not
  try `pip`.
- No LLM call anywhere in a hook path. `graphify update` is AST-only; community labelling
  (`graphify label`) is never run by a hook. The bundle generator is deterministic Python.
- Hooks stay cheap. `SessionStart` bootstrap on a healthy project must finish well under the
  hook timeout with no git subprocess; post-commit work runs detached, as Graphify's does.
- Never route around a hook. Opt-outs are explicit config or env (`GRAPHIFY_SKIP_HOOK=1` is
  honoured; a `[knowledge] enabled = false` table switch turns the whole feature off).
- Installs touch the user's machine (`~/.local/share/uv/tools`, `~/.claude/skills`, the repo's
  git hooks). Bootstrap prints what it is about to install before it does, and each install is a
  separate reported step so a partial failure is visible.
- OKF v0.2 official conformance is the floor (`type`, parseable frontmatter, reserved files).
  Stricter rules are labelled organisational policy. Consumers written here MUST tolerate
  unknown types, unknown keys and broken links, per SPEC.md §11.
- The agent never authors a `human:` verification event and never edits the verdict logic.
- This repository has 159 files, under the ~500-file threshold where articles 4 and 5 say the
  graph pays for itself. The plugin is built for other projects too, so the feature ships on by
  default but must be cheap enough that the tooling tax on a small repo is a few seconds per
  commit, and it must be honest in `knowledge status` about what it measured.
- Existing behaviour of every current mechanic and hook is unchanged when `[knowledge]` is off;
  all current tests keep passing.
- Budget: one feature through the six stages; no new runtime dependencies, no paid services,
  no LLM-backed producers (OpenWiki, `graphify label`) in the mandatory path.

## Open questions
1. Bundle location: `sdlc/knowledge/` (next to the artifacts it derives from) versus
   `docs/knowledge/` or `.well-known/okf/` (article 2's suggestion). Proposal: `sdlc/knowledge/`,
   configurable.
2. Commit `graphify-out/graph.json` or leave `graphify-out/` ignored and rebuild on checkout?
   Graphify installs a post-checkout hook and a union merge driver, which suggests committing
   `graph.json` (and ignoring `graph.html`); article 4 warns a tracked `graphify-out/` dirties the
   tree on every regeneration. Proposal: ignore `graphify-out/`, commit only the OKF bundle, and
   let the post-checkout hook rebuild.
3. Post-commit trigger ownership: append a plugin block to the git post-commit hook (works for
   commits made outside Claude too) or a `PostToolUse` Bash matcher (only commits Claude makes,
   but no git-hook surgery). Proposal: git hook, marker-delimited like Graphify's own.
4. Install the superops `okf` Go CLI for `okf lint` (13 rules, stricter than the spec) or write
   the three official conformance rules in stdlib Python and treat `okf lint` as optional
   organisational policy when present? Proposal: stdlib checker, `okf` optional.
5. Graphify skill scope: user-level (`graphify install --platform claude`) or per project
   (`--project`, which also writes a PreToolUse hook into `.claude/settings.json`)?
6. Should the reviewer and verifier agents be given `graphify query` in their allowed tools?
7. Clean-rebuild cadence default (article 7 says every 3-5 incrementals): 5, or age-based?
8. Should bootstrap add a marker-delimited pointer to `sdlc/knowledge/index.md` in the
   project's `CLAUDE.md` (opt-out in config), or leave `CLAUDE.md` untouched and rely on stage
   commands alone? Proposal: add the pointer, opt-out.
