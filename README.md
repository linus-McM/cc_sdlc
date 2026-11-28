# sdlc

A Claude Code plugin that runs the [AI-native SDLC playbook](https://claude.com/blog/the-ai-native-sdlc-playbook) as six slash commands:

- `/sdlc:plan`
- `/sdlc:design`
- `/sdlc:build`
- `/sdlc:test`
- `/sdlc:deploy` (optional)
- `/sdlc:maintain` (optional)

The loop is plan, design, build, test. You approve once, at `/sdlc:build accept`, with the intent, the numbered requirements and the plan in front of you; Claude builds exactly that plan step by step, and the loop is complete when `/sdlc:test review` passes. Every difference between what you approved and what was built is reported. Deploy and maintain are secondary flows you run when you want them.

See the [six-command workflow diagram](https://linus-mcm.github.io/cc_sdlc/diagrams/sdlc-commands.html) for how the stages connect (source: [`diagrams/sdlc-commands.html`](diagrams/sdlc-commands.html)).

## Project Memory

- The first run of every command calls Graphify, which builds/updates the call graph of the repo.
- From that graph the plugin writes or updates the `./sdlc/knowledge/`
- Each `/sdlc:` command reads sdlc/knowledge/index.md when starting a feature (`new`) and follows links only as deep as needed; the top index lists at most 15 entries per section and links to the full sub-indexes.
- Every stage boundary (plan/design/build `accept`, `test review`, `deploy record`) writes `sdlc/<slug>/HANDOVER.md` into the checkpoint commit, so a fresh session can pick the feature up without the chat history (`[checkpoint] handover = false` turns it off).
- "What calls this" and blast-radius questions go to `graphify query`.
- Each stage's Workflow agents share one Repomix context pack: the files the stage artifact names, one graph hop out, with secrets kept out. `plan accept` and `test review` build the pack themselves when it is missing or behind and report it; a pack never blocks a stage, except that `test review` refuses a changed file excluded as a secret.
- Hooks keep it honest. After an edit, Claude is told which module concepts cover the file.
- The git post-commit hook refreshes the bundle and warns when indexes fall behind HEAD.

## Refactor Your Codebase via the Archify Diagrams

- Every stage can produce a html file built by the Archify skill, on demand (the `docs` section of each command).
- Review the html file and use the `/archify` skill to re-align or explore deeper into any issue.
- Archify compares current state to your future state and can be passed to Claude Code to redesign the stage.
- No stage waits for a diagram: `sdlc docs check <stage>` says whether one is fresh.
- The build, deploy and maintain diagrams map a list or a TOML table, so `sdlc docs draft <stage>` writes their source and no model authors them; a source authored by hand is never overwritten.

## Install

```sh
claude plugin marketplace add linus-McM/cc_sdlc
claude plugin install sdlc@sdlc
```

## Set up a project

Run the first command in any git repository:

```
/sdlc:plan "Add rate limiting to the public API"
```

## The six commands

### 1. `/sdlc:plan` — capture the intent

```
/sdlc:plan "<title>"          # creates sdlc/<slug>/intent.md and interview you
/sdlc:plan check              # validate the artifact
/sdlc:plan accept             # Claude accepts once the check passes; commits the intent
/sdlc:plan status             # which artifacts are accepted, present or missing
```

Claude reads the code the idea touches, asks you only what that leaves open (what cannot be done today, who is affected, what better looks like, what is out of scope) and writes the answers into `intent.md`. `accept` is refused until the artifact validates; Claude runs it and carries on into design, because you read the intent again when you approve the plan.

### 2. `/sdlc:design` — turn the intent into a spec

```
/sdlc:design                  # blocked until intent.md is accepted; writes spec.md
/sdlc:design check
/sdlc:design accept           # Claude accepts once the check passes; commits the spec
```

`spec.md` holds numbered testable requirements traced to the intent (`1.`, `2.`, ... cited everywhere else as `R1`, `R2`), the design (components, data flow, interfaces), a Concerns section listing every policy or security conflict with how the design handles it, and the proof (test files and checks). `check` refuses requirements that are not a numbered list. Claude asks you only about a concern the code and the intent cannot settle.

### 3. `/sdlc:build` — plan, then implement red→green

```
/sdlc:build                   # blocked until spec.md is accepted; writes plan.md in plan mode
/sdlc:build check
/sdlc:build accept            # the one approval: you approve intent, requirements and plan together
/sdlc:build red <step>        # proves the step's test fails before code is written
/sdlc:build green <step>      # proves it passes after the smallest change
/sdlc:build sync              # every edited file must be listed in plan.md, or reverted
/sdlc:build fix on | off      # bug-fix mode: test files are locked while on
```

`plan.md` lists the files that change, the order of work as numbered steps (each names the failing test written first and cites the requirement it delivers), the risks and the proof. `check` refuses a requirement no step delivers and a citation of a requirement the spec does not have. `accept` is where you sign off: Claude shows you the outcome, the requirements, the files and the steps, asks, and on yes pins them with the current commit in `approved.json`. `red`, `green`, `sync`, `simplify` and `fix` are refused until then.

After approval the plan is the contract. Every numbered step is a red→green cycle recorded in `tdd.jsonl` under its step number; `test run` later refuses while a step has none, and while a planned file was never changed. Claude may edit plan.md when the code proves a step wrong: the difference from `approved.json` (files added, files removed, steps changed) is reported by `test run`, `test review` and the PR body, and a change to what you get goes back to you for a new `accept`. `red` and `green` take `--only <test id>`: with `[commands] test_one = "pytest -q {selector}"` set, `red` runs that one test and `green` runs it first and the full suite once it passes. A passing `green` also runs plan sync and commits the step as `build(<slug>): <step>` (`[build] commit_steps = false` turns the commit off). `fix on` reproduces a bug as a failing test, then denies edits to test files until the fix passes, so a fix cannot rewrite the test that caught it. When every step is green the command runs `/simplify` over the branch, then `sdlc build simplify` re-runs the test and lint commands and plan sync, commits the result as `build(<slug>): simplify` and records the pass. `test run` is refused until a pass is recorded after the last green (`[build] require_simplify = false` turns the gate off); the record is Claude's word that the skill ran, Python cannot see it.

### 4. `/sdlc:test` — feedback loop, review and evals

```
/sdlc:test run                # test, lint and build commands from .sdlc.toml; writes test-report.json
/sdlc:test review             # three-pass review (Bugs, Security, Compliance) against REVIEW.md; writes review.md
/sdlc:test evals              # runs evals/*.json through `claude -p` and gates on the pass rate
```

`run` refuses when a plan step has no red→green cycle or a planned file was never changed, reports the deviations from the approved plan, and spawns a fresh-context verifier agent that checks the change matches `plan.md`. `review` runs the review workflow (or the reviewer agent); its Compliance section carries one line per requirement, `- R<n>: met, <evidence>`, and `test review` is refused while a requirement has no verdict or an `Important:` line ends with neither `fixed: <commit>` (after another red→green cycle) nor `wontfix: <reason>` (your decision, never Claude's). After the review passes, Claude runs Claude Code's built-in `/code-review` and `/security-review` over the branch. It merges their findings into Bugs and Security and records one line per skill under `## Built-in review`. `test review` is refused while a skill in `[test] builtin_review` has no line (`builtin_review = []` turns the gate off). As with `/simplify`, the line is Claude's word that the skill ran. A passing `test review` returns `complete: true`: the feature is built, tested and reviewed, and the loop ends here. Add one eval per production incident.

### 5. `/sdlc:deploy` (optional) — PR, tiers, rollback rehearsal

```
/sdlc:deploy pr               # writes pr-body.md from the artifacts and opens the PR with gh
/sdlc:deploy check <env>      # allow | ask | blocked, with reasons
/sdlc:deploy rehearse         # runs [deploy] rollback in a throwaway worktree; required before production
/sdlc:deploy record <env>     # appends env, date and sha to deploy.json
```

Run this stage when you want a PR or a release; the loop is already complete without it. Environments are tiered in `.sdlc.toml`: `free` (Claude deploys), `ask` (Claude asks first) and `gate` (Claude asks first, and only once the rollback is configured and rehearsed). Every tier needs a passing test report and a review with no open Important finding. A hook also puts the release command for a gated environment to you as a permission prompt. Claude never pushes to `main`; branch protection closes the PR. Once the PR is open, type `/steward` to have Claude watch it (failing checks, conflicts, review comments) until it merges. Or type `/ship` to get one more in-session review first; it keeps the PR and its body. Claude cannot start either one. Before a production release, Claude offers `/code-review ultra <PR#>`, a billed cloud review that only you can start.

**Rollback rehearsal.** `deploy rehearse` runs the rollback in a throwaway detached worktree of HEAD, at the project's own path within the repository. Isolated: the checked-out files, the index and the current branch. Not isolated: the shared object store, tags, other branches, remotes (`git push`, `git tag`, `git branch -f`) and anything outside git (`kubectl`, `gh`), which all run for real. Commits the rehearsal makes become dangling objects that git's own gc prunes. A worktree that cannot be removed is reported with its path after the result is recorded.

### 6. `/sdlc:maintain` (optional) — watch production, write the next intent

```
/sdlc:maintain watch [metric]           # tier and action per metric
/sdlc:maintain ingest <metric> --value <v>   # feed a reading from CI or a webhook
/sdlc:maintain propose <metric>         # writes the next intent.md from the evidence
/sdlc:maintain lesson "<text>"          # appends to sdlc/lessons.md
```

Readings land in `sdlc/metrics.jsonl`; bands in `sdlc/bands.toml`. Detection is Western Electric rules on a rolling baseline, pure Python: 1σ logs, 2σ triggers a read-only diagnosis and a three-line SITREP, 3σ writes an intent with the evidence and returns you to `/sdlc:plan`. Claude never acts beyond a PR or the rehearsed rollback; you decide whether to fix now, schedule or dismiss.

**Readings and bands.** `sdlc/metrics.jsonl` holds one `{"metric","value","ts"}` object per line, fed by `sdlc maintain ingest` from CI or a webhook. In `sdlc/bands.toml` set `bad = "high"` or `"low"` per metric so an improvement never counts as a breach. `sdlc knowledge refresh` appends `knowledge_nodes`, `knowledge_communities`, `knowledge_stale`, `knowledge_unverified` and `knowledge_behind` readings, so the `knowledge_stale` and `knowledge_behind` bands in the template watch index freshness like any production signal.

## Guardrails

Hooks run on every session, edit and shell command:

- edits under `[build] protected_paths` are denied, and test files are locked while `fix on`;
- the release command for a `gate` environment asks you first (a permission prompt, not a denial);
- after an edit Claude is told when the file is missing from `plan.md`;
- after a commit Claude is told when the knowledge indexes fall behind `HEAD`.

Each stage boundary commits what it produced: `plan(<slug>): accept — intent.md`, `test(<slug>): review — review.md`, `deploy(<slug>): record <env> — deploy.json`, `maintain(<slug>): propose — intent.md`, `knowledge: refresh — sdlc/knowledge (+N files)`. Only the plugin's own output moves (the `sdlc/` directory plus `[checkpoint] paths`); source code, tests and staged work are left alone, and intermediate output rides along with the next boundary as `(+N files)`.

Off switches: `SDLC_KNOWLEDGE=off`, `SDLC_DOCS=off`, `SDLC_CHECKPOINT=off`, `SDLC_PACKS=off`, `[knowledge] enabled = false`, `[docs] enabled = false`, `[checkpoint] enabled = false`.

## Develop

```sh
uv sync && uv run pytest            # TDD: red test first, then code (runs in parallel, pytest-xdist)
uv run ruff check plugin/scripts scripts tests
claude plugin validate --strict plugin && claude plugin validate --strict .
```

## Acknowledgements

Runtime tools and skills the plugin installs or drives:

- [Claude Code](https://docs.claude.com/en/docs/claude-code) by Anthropic, the host for the commands, agents and hooks, and the [AI-native SDLC playbook](https://claude.com/blog/the-ai-native-sdlc-playbook) the six stages follow.
- [uv](https://github.com/astral-sh/uv) by Astral, which runs every mechanic and hook through `uv run --no-project`.
- [Graphify](https://github.com/Graphify-Labs/graphify) (`graphifyy` on PyPI) by Safi Shamsi and Graphify Labs, the AST knowledge graph behind `graphify-out/` and the call-graph queries.
- [Open Knowledge Format](https://github.com/GoogleCloudPlatform/open-knowledge-format) v0.2 by Google Cloud, the bundle layout of `sdlc/knowledge/`; the articles by Udaykiran Estari on combining Graphify and OKF shaped the trust model and freshness checks.
- [Archify](https://github.com/tt-a1i/archify) by tt-a1i, which renders the stage diagrams, installed through the [skills](https://www.npmjs.com/package/skills) CLI.
- [GitHub CLI](https://cli.github.com/), used by the deploy and maintain stages.

Development tooling: [pytest](https://pytest.org/), [pytest-cov](https://github.com/pytest-dev/pytest-cov), [ruff](https://github.com/astral-sh/ruff), [bandit](https://github.com/PyCQA/bandit), [pre-commit](https://pre-commit.com/) with [pre-commit-hooks](https://github.com/pre-commit/pre-commit-hooks), and [just](https://github.com/casey/just).
