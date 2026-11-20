# Efficiency review: token use and compute

Date: 2026-11-20. Reviewed at `dev` (`9e90177`, plugin 0.9.1). Scope: `plugin/` (commands, hooks, workflows, mechanics), tests and CI.

Token figures are estimates at 4 characters per token. Timings were measured on this machine (WSL2), 20 runs each.

## Summary

The mechanics are already cheap. A hook call costs about 50 ms and a verdict is usually under 300 characters. The large costs are elsewhere:

1. **Workflow agents re-read the context pack.** Every agent, including each low-effort skeptic, is told to read a pack of up to 60,000 tokens. A review with six findings starts 15 agents.
2. **`build red` and `build green` run the whole test suite.** That is two full runs per step, plus a third in `test run`.
3. **Stage documents are authored by the model** even when the source is a list or a TOML table that Python could convert.
4. **Each command repeats a 1,000-character preamble** that tells Claude to make two CLI calls the mechanics could make themselves.

Recommendations are ordered by expected saving within each section. Nothing here has been implemented.

## Measurements

| What | Result |
|---|---|
| `python3 -c pass` | 12 ms |
| `uv run --no-project python -c pass` | 20 ms |
| Hook via `uv run --no-project` (pre-edit, pre-bash, post-edit, post-bash) | 47 to 52 ms |
| Same hook via `python3` | 40 to 43 ms |
| `import sdlc.hooks` (of the above) | 35 ms |
| `sdlc status` | 52 ms |
| `sdlc workflows gate build` | 65 ms |
| Shell guard when there is no `.sdlc.toml` | under 1 ms |
| `uv run pytest` (260 tests) | 38 s; slowest single test 0.57 s |

| File group | Size | Tokens (est.) |
|---|---|---|
| `plugin/commands/*.md` (6 files) | 3.5 to 4.4 KB each | 870 to 1,100 each |
| Shared preamble inside each command | about 1,000 chars | 250 each |
| `plugin/workflows/*.js` (6 files) | 3.0 to 5.8 KB each | not loaded into the main context |
| Default pack budget (`pack_max_tokens`) | 60,000 tokens | per agent that reads it |

## Token use

### T1. Stop skeptics reading the pack and the full ground (high)

`plugin/workflows/review.js` and `plan-critic.js` build one `GROUND` string and give it to every agent. `GROUND` starts with `PACK_NOTE` ("read it first") and then lists REVIEW.md, intent.md, spec.md, plan.md, the whole branch diff and the knowledge index. The Verify agents run at `effort: 'low'` on Sonnet but get the same instructions.

In `review.js` each finding gets two skeptics, and the number of findings per pass is not capped. Six findings means 3 finders plus 12 skeptics. At a 60,000-token pack that is up to 900,000 input tokens, most of it spent by agents whose job is to check one `path:line`.

Recommended changes:
- Give Verify agents a narrow ground: the finding JSON, the instruction to read `git diff <base>...HEAD -- <path>` and the file around the line, and the read-only rules. No pack, no artifacts unless the pass is Compliance.
- Verify only `Important` findings with two skeptics. A `Nit` cannot be downgraded further, so one skeptic (drop or keep) is enough, or none.
- Cap findings per pass in the `FINDINGS` schema (`maxItems`), for example 8.
- Apply the same narrow ground to the Verify phase of `plan-critic.js` and `diagnose.js`.

### T2. Do not read the review inputs twice (high)

`plugin/commands/test.md` `review` step 1 has the main session read REVIEW.md, intent.md, spec.md, plan.md and `git diff main...HEAD`. Step 2 then runs `sdlc:review`, whose agents read the same files. When the workflow runs, the main session only needs the workflow's `markdown` result.

Recommended change: move step 1 under the "Without workflows" branch. The diff alone can be tens of thousands of tokens held in the main context for the rest of the stage.

### T3. Shrink the command preamble (medium)

All six commands carry the same three paragraphs (992 to 1,011 characters, about 250 tokens). The whole command file is loaded on every slash invocation, including one-line actions such as `/sdlc:build sync`.

Two of the three paragraphs exist only to make Claude run a call and interpret it:
- "Knowledge: run `sdlc knowledge bootstrap`". The SessionStart hook already runs the bootstrap check and `stages.new` already bootstraps on `plan new`. See M1.
- "Workflows: run `sdlc workflows gate <stage>`". See M2.

With M1 and M2 done, the preamble reduces to the first paragraph plus one sentence each on `graphify query` and the `human:` rule. Estimated saving: 150 tokens per invocation and two tool round-trips per stage.

### T4. Return less in successful verdicts (medium)

A passing verdict only needs to say it passed. Several return detail that is only useful on failure:
- `build.tdd` returns the 20-line `tail` on a successful `green` (`plugin/scripts/sdlc/build.py`). Keep the tail for `red` (Claude should see why it fails) and for failures.
- `testing.run` returns `results` with a 20-line tail per command when everything passed. The tails are already in `test-report.json`.
- `build.sync` returns the full `planned` list on success.
- `knowledge.bootstrap` returns every step when all are `present`. Return `"steps": "all present"` in that case, as `hooks.knowledge_note` already does for the session note.

Also print verdicts compactly in `cli.entry` (`json.dumps(result, separators=(",", ":"))` or no indent). Indentation adds 15 to 25 percent to every verdict.

### T5. Trim long reference prose from commands (low)

- `deploy.md` `rehearse` spends about 900 characters on what a worktree does and does not isolate. Keep one sentence and put the rest in the README, or return it in the `rehearse` verdict only when the rollback command contains `push`, `tag`, `kubectl` or `gh`.
- `maintain.md` has a 700-character paragraph on file formats before any action. Move it to the README.
- The review output format (three headings, `Important:`/`Nit:` bullets, five nits) is stated in `test.md`, `agents/reviewer.md`, `workflows/review.js` and `templates/REVIEW.md`. Keep it in the agent and the workflow, and reference it from the command.

### T6. Lower the default pack budget per stage (low)

`pack_max_tokens = 60000` applies to every stage. The plan and design packs feed scouts and designers that need structure, not bodies. A per-stage budget (for example plan 20,000, design 30,000, test 60,000) or starting those stages on the `--compress` rung cuts the multiplier in T1 for the other workflows. `design-panel.js` starts about 10 agents (3 designs, 4 lenses, 2 judges, 1 synthesis), each reading the pack.

## Prose to mechanical

Each item replaces an instruction Claude must read and follow with a mechanic that does the work or enforces it.

### M1. Bootstrap inside the mechanics

Every command says to run `sdlc knowledge bootstrap`. Have `cli.main` (or `stages.new`) run the check itself and attach a `knowledge` key only when something is missing or failed. This removes one CLI call and one verdict per stage.

### M2. Fold the workflow gate into the stage verdict

`sdlc workflows gate <stage>` is a separate call whose only purpose is to tell Claude which branch of the command text to follow. Attach `workflow: {name, run, reason}` to the verdict that precedes the workflow step (`plan new`, `design new`, `build new`, `test run`, `deploy pr`, `maintain watch`).

### M3. One call per build step

A build step is `red`, edit, `green`, `sync`, `git commit`: four tool calls beside the edit. `build green <step>` could run `sync` on success and, when both pass, commit as `build(<slug>): <step>` through the existing checkpoint path. That saves two round-trips per step and removes steps 5 and 6 from `build.md`.

### M4. Rebuild the pack inside the gate

`test.md` step 4 tells Claude to rebuild the pack "immediately before review" because fixes moved HEAD, and `plan.md` step 6 says to build one before accept. `packs.require` already knows when the pack is stale. Have it rebuild when the tree is clean and refuse only when it cannot. This removes two instructions and a common refused-then-retry loop.

### M5. Generate stage documents from structured sources

Each stage tells Claude to read the Archify schemas and an example, then author `<stage>.json`. Three of the six documents are a direct mapping:
- **build**: one node per Order of work step, with its test as the gate. `build.py` already parses plan.md sections.
- **deploy**: one state per environment tier from `[deploy.environments]`.
- **maintain**: one state per tier from `sdlc/bands.toml`.

A `docs draft <stage>` mechanic could write these JSON sources directly. Claude would only author plan, design and test documents. This saves a schema read, an example read and an authoring pass in three stages per feature.

### M6. Enforce what the review step asks for

`test.md` says to address every Important finding and cap nits at five. `testing.review` only counts them. Refusing when `important > 0` (or when nits exceed five) makes the instruction unnecessary. This is a behaviour change to the gate and needs a decision on how a resolved finding is marked.

### M7. Smaller items

- `test.md`: "copy `/templates/REVIEW.md` if absent". `test run` can copy it.
- `plan.md`: "Set `Risk: high` when the change touches auth, PII, payments, migrations or infra". `plan check` can flag those words in intent.md when Risk is lower.
- `deploy.md` `pr`: `deploy pr` could return the exact `gh pr create` command in `next`.
- The automatic `/simplify` step on `feat/auto-simplify` is prose only. Python cannot call a skill, but `test run` could refuse until a `build(<slug>): simplify` commit or an explicit skip marker exists.

## Compute

### C1. Scope red and green runs to the step (high)

`build.tdd` runs `[commands] test` in full for both phases. In this repository that is 38 s twice per step, and a third time in `test run`. Add an optional selector, for example `sdlc build red <step> -- tests/test_x.py::test_y`, appended to a new `[commands] test_one` template. `green` should run the selector first and the full suite once after it passes. `test run` stays the full gate.

### C2. Run the test suite in parallel (high for this repo)

260 tests take 38 s but the slowest is 0.57 s, so the time is per-test fixture setup (git repositories and sandboxes). Adding `pytest-xdist` as a dev dependency and running `-n auto` should cut this by the core count. Session-scoped or copied template repositories in `tests/conftest.py` would reduce it further.

### C3. Filter hooks in the shell before starting Python (medium)

Two hooks run on every Bash call and two on every edit, at about 50 ms each. Two of them almost always return nothing:
- **post-bash** only acts on `git commit`. The shell guard can read stdin and exit unless it contains `commit`.
- **pre-bash** only acts when a token named `deploy` or the configured `deploy.command` appears, and never when `RELEASE_APPROVAL` is set. The guard can exit early when `deploy.command` is empty and the input has no `deploy`.

This removes about 100 ms from nearly every Bash call. The shell filter must be a superset of the Python rule so no release command is missed.

### C4. Import lazily in `hooks.py` (medium)

Importing `sdlc.hooks` takes 35 ms of the 50 ms, because it loads `knowledge` (1,119 lines), `deploy`, `build`, `workflows`, `subprocess`, `shutil` and `tempfile` for every event. `pre_edit` needs only `project` and `artifacts`. Move the other imports into the handlers that use them.

### C5. Debounce the post-commit knowledge refresh (medium)

`templates/knowledge/post-commit.sh` starts a background job on every commit that polls `graph.json` for up to 60 s, then runs `knowledge refresh`, which itself commits. A build stage that commits once per step starts one job per commit, and they overlap. Use a lock file so a new commit replaces the pending job, and refresh only for the latest HEAD.

### C6. CI (low)

- `npx --yes @anthropic-ai/claude-code` is downloaded on every run. Cache npm or pin and cache the package.
- `.pre-commit-config.yaml` runs ruff, and the "Lint and format" step runs it again. Keep one.
- `actions/setup-node` and the manifest validation can run as a separate job in parallel with the tests.

### C7. Minor

- `project.config` deep-copies the merged config on every call. Most callers only read it. Return a read-only view, or copy only in the few callers that mutate.
- `uv run --no-project` costs about 10 ms over `python3`. It guarantees Python 3.11+, so keep it.

## Suggested order

| Order | Item | Effort | Saving |
|---|---|---|---|
| 1 | T1 narrow skeptic ground, cap findings | small (3 workflow files) | largest token saving |
| 2 | T2 skip duplicate review reads | one line in `test.md` | large, main context |
| 3 | C1 step-scoped red/green | medium (config key, CLI arg, tests) | largest wall-clock saving |
| 4 | M1 + M2 + T3 preamble | medium | two calls per stage, 150 tokens per invocation |
| 5 | T4 quieter verdicts | small | small per call, many calls |
| 6 | C3 + C4 hooks | small | about 100 ms per Bash call |
| 7 | M3 one call per step | medium | two round-trips per step |
| 8 | M5 generated documents | larger | one authoring pass in three stages |
| 9 | C2, C5, C6, M4, M6, M7, T5, T6 | varied | incremental |

## Implementation status

Implemented on `chore/efficiency-report` after the review. Measured where a number is given.

| Item | Status | Note |
|---|---|---|
| T1 | done | Skeptics get a narrow ground (the finding, its file, the diff for that path) and no pack. Findings are capped: 8 in `review.js`, 6 in `plan-critic.js`, 4 in `diagnose.js`. A Nit gets one skeptic, an Important finding two. |
| T2 | done | `test.md` no longer reads REVIEW.md, the artifacts or the diff in the main session. |
| T3 | partly | The preamble is about the same length. The saving is the two CLI calls per stage that M1 and M2 removed. |
| T4 | done | Compact JSON output; `test run` returns name and exit per command (tails stay in `test-report.json`); a green returns no tail; `plan new` collapses the bootstrap steps when all are present. |
| T5 | done | Rollback rehearsal and band reference text moved from `deploy.md` and `maintain.md` to the README. |
| T6 | done | `[knowledge.pack_stage_tokens]` caps plan at 20000 and design at 30000; it lowers the budget, never raises it. |
| M1 | done | Stage entry verdicts carry `knowledge` only when a tool is missing. |
| M2 | done | Stage entry verdicts carry `workflow: {name, run, reason}`. |
| M3 | done | `build green` runs the plan sync and, with `[build] commit_steps` (default true), commits the step. |
| M4 | done | `packs.require` builds a missing or behind pack and refuses only when that build fails. |
| M5 | done | `sdlc docs draft build|deploy|maintain` writes the Archify source. Checked against the real renderer: 9/9 showcase for 1 to 40 plan steps, five environment layouts and the maintain rail. A gate on the first environment has no layout and falls back to the recipe. |
| M6 | done | `test review` is refused while an `Important:` line ends with neither `fixed: <commit>` nor `accepted: <name>, <reason>`. |
| M7 | partly | REVIEW.md is copied by `test run`; `plan check` returns `risk_hint`; `deploy pr` already returned the `gh` command. `sdlc build simplify` runs the checks, plan sync and the commit, and records the pass; `test run` is refused without one since the last green (`[build] require_simplify`). The record is the engineer's word: Python cannot see the skill run. |
| C1 | done | `build red|green --only <test id>` with `[commands] test_one`; a green still runs the full suite afterwards. |
| C2 | done | `pytest-xdist`, `-n auto`: 38 s to 15 s on this machine. |
| C3 | done | The Bash hooks start Python only when the input mentions a commit (post) or a deploy, or `[deploy] command` is set (pre). |
| C4 | done | `sdlc.hooks` imports only `artifacts` and `project` at load. |
| C5 | done | The post-commit job refreshes only when its commit is still the newest. |
| C6 | done | One lint pass (pre-commit); the manifest check is its own job with an npm cache. |
| C7 | skipped | The config deep copy is not measurable next to process start. |

## Not measured

- Real token counts per stage. The figures above are size-based estimates. `sdlc/metrics.jsonl` on the `dogfood` branch could carry a per-stage token reading if the stage commands recorded one.
- Workflow agent counts in practice. The count for `review.js` depends on how many findings the finders return.
- Hook cost with the knowledge layer on. It is off on `dev`, so `post-edit` and `session-start` were timed without the bundle state read.
