# Intent: graph-selected repomix context packs
Author: Linus McManamey. Status: accepted. Risk: high.

## Problem
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

## Proposed outcome
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

## Affected users and systems
- Claude agents: the stage commands and the read-only Workflow agents that consume packs. The
  reviewer and verifier agents may also be given the pack.
- Engineers and product owners: only indirectly, through better-grounded drafts.
- Code: `plugin/scripts/sdlc/knowledge.py` (the pack mechanic, file selection from the graph, and
  a new bootstrap step), `cli.py` (the `knowledge pack` action), `project.py` (`[knowledge]` pack
  config and the ignore list), `plugin/commands/*.md` and `plugin/workflows/*.js` (passing and
  reading the pack path), and `tests/conftest.py` (a fake `repomix` on PATH).

## Constraints
- Python stays stdlib only. Repomix runs as a subprocess through the existing runners, like
  Graphify. Bootstrap installs it globally with `npm i -g repomix` when it is missing, and updates
  it (`npm update -g repomix`) when it is present. Node is already required for Archify.
- Secrets (the reason for Risk: high): a pack copies file contents into one blob, so:
  - Repomix's secret check is always on.
  - A fixed exclude list always applies, whatever the graph selects: `.env*`,
    `.claude/settings.local.json`, credential and key files, and anything `.gitignore`'d.
  - A pack that trips the secret check is refused, not written.
  - Bandit also scans the Python files in the set, as a subprocess. Its hardcoded-password findings
    (B105 to B107) refuse the pack. Bandit reads only Python source, so it adds to the Repomix check
    and the exclude list and does not replace them.
- Pack output never enters the Graphify input. An earlier Repomix pack became the top god node
  (`sdlc/graphify-and-okf-knowledge-base-integration/spec.md`).
- The layer is off under `SDLC_KNOWLEDGE=off` or `[knowledge] enabled = false`, and then the pack
  gates do not apply. With the layer on, a missing Repomix blocks `plan accept` and `test review`,
  and the reason names the install command. In the advisory stages the pack step is reported as
  skipped and the stage continues.
- Tests never reach the real Repomix. Config is read only through `project.config()`.
- Success measure: replay one past dogfood feature's design-panel and review Workflows with and
  without packs. The target is fewer subagent tokens and tool calls, with the same or better
  findings.
- Out of scope: packing remote or external repositories, which stays manual, and a Deploy-stage
  pack, because the PR body's knowledge diff is enough there.

## Open questions
none
