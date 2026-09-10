# sdlc

A Claude Code plugin that runs the [AI-native SDLC playbook](https://claude.com/blog/the-ai-native-sdlc-playbook) as six slash commands:

- `/sdlc:plan`
- `/sdlc:design`
- `/sdlc:build`
- `/sdlc:test`
- `/sdlc:deploy`
- `/sdlc:maintain`

## Project Memory

- The first run of every command calls Graphify, which builds/updates the call graph of the repo.
- From that graph the plugin writes or updates the `./sdlc/knowledge/`
- Each `/sdlc: command` reads sdlc/knowledge/index.md first and follows links only as deep as needed.
- "What calls this" and blast-radius questions go to `graphify query`.
- Hooks keep it honest. After an edit, Claude is told which module concepts cover the file.
- The git post-commit hook refreshes the bundle and warns when indexes fall behind HEAD.

## Refactor the Codebase via the Archify Diagrams

- Every stage ends with a html file built by the Archify skill.
- Review the html file and use the `/archify` skill to re-align or explore deeper into any issue.
- Archify compares current state to your future state and can be passed to Claude Code to redesign the stage.
- accept, test review and deploy records are refused while the diagram is stale.

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
/sdlc:plan accept             # product owner accepts; commits the intent
/sdlc:plan status             # which artifacts are accepted, present or missing
```

Claude interviews you (what cannot be done today, who is affected, what better looks like, what is out of scope) and writes the answers into `intent.md`. Changes touching auth, PII, payments, migrations or infrastructure are marked `Risk: high`. `accept` is refused until the artifact validates and its stage diagram is fresh; only a human accepts.

### 2. `/sdlc:design` — turn the intent into a spec

```
/sdlc:design                  # blocked until intent.md is accepted; writes spec.md
/sdlc:design check
/sdlc:design accept           # product owner accepts; commits the spec
```

`spec.md` holds numbered testable requirements traced to the intent, the design (components, data flow, interfaces), a Concerns section listing every policy conflict with its owner, and the proof (test files and checks). Concerns are walked through with the product owner before engineering sees the spec.

### 3. `/sdlc:build` — plan, then implement red→green

```
/sdlc:build                   # blocked until spec.md is accepted; writes plan.md in plan mode
/sdlc:build check
/sdlc:build accept            # engineer (tech lead for Risk: high) accepts the plan
/sdlc:build red <step>        # proves the step's test fails before code is written
/sdlc:build green <step>      # proves it passes after the smallest change
/sdlc:build sync              # every edited file must be listed in plan.md, or reverted
/sdlc:build fix on | off      # bug-fix mode: test files are locked while on
```

`plan.md` lists the files that change, the order of work (each step names the failing test written first), the risks and the proof. After acceptance every step is a red→green cycle recorded in `tdd.jsonl`; `test run` later refuses without at least one. `fix on` reproduces a bug as a failing test, then denies edits to test files until the fix passes, so a fix cannot rewrite the test that caught it.

### 4. `/sdlc:test` — feedback loop, review and evals

```
/sdlc:test run                # test, lint and build commands from .sdlc.toml; writes test-report.json
/sdlc:test review             # three-pass review (Bugs, Security, Compliance) against REVIEW.md; writes review.md
/sdlc:test evals              # runs evals/*.json through `claude -p` and gates on the pass rate
```

`run` refuses when no red→green cycle was recorded and spawns a fresh-context verifier agent that checks the change matches `plan.md`. `review` spawns the reviewer agent; every `Important:` finding is fixed with another red→green cycle before the review is committed. Add one eval per production incident.

### 5. `/sdlc:deploy` — PR, tiers, rollback rehearsal, production gate

```
/sdlc:deploy pr               # writes pr-body.md from the artifacts and opens the PR with gh
/sdlc:deploy check <env>      # allow | ask | blocked, with reasons
/sdlc:deploy rehearse         # runs [deploy] rollback in a throwaway worktree; required before production
/sdlc:deploy record <env>     # appends env, sha and approver to deploy.json
```

Environments are tiered in `.sdlc.toml`: `free` (Claude deploys), `ask` (Claude asks first) and `gate` (needs a passing report, a review, a rehearsed rollback and `RELEASE_APPROVAL=<name>` in the environment). A hook also denies the release command for a gated environment while `RELEASE_APPROVAL` is unset. Claude never pushes to `main`; branch protection and a code-owner approval close the PR.

### 6. `/sdlc:maintain` — watch production, close the loop

```
/sdlc:maintain watch [metric]           # tier and action per metric
/sdlc:maintain ingest <metric> --value <v>   # feed a reading from CI or a webhook
/sdlc:maintain propose <metric>         # writes the next intent.md from the evidence
/sdlc:maintain lesson "<text>"          # appends to sdlc/lessons.md
```

Readings land in `sdlc/metrics.jsonl`; bands in `sdlc/bands.toml`. Detection is Western Electric rules on a rolling baseline, pure Python: 1σ logs, 2σ triggers a read-only diagnosis and a three-line SITREP, 3σ writes a `Risk: high` intent and returns you to `/sdlc:plan`. Claude never acts beyond a PR or the rehearsed rollback; the on-call engineer triages.

## Guardrails

Hooks run on every session, edit and shell command:

- edits under `[build] protected_paths` are denied, and test files are locked while `fix on`;
- the release command for a `gate` environment is denied until `RELEASE_APPROVAL` names a release manager;
- after an edit Claude is told when the file is missing from `plan.md`;
- after a commit Claude is told when the knowledge indexes fall behind `HEAD`.

Off switches: `SDLC_KNOWLEDGE=off`, `SDLC_DOCS=off`, `[knowledge] enabled = false`, `[docs] enabled = false`.

## Develop

```sh
uv sync && uv run pytest            # TDD: red test first, then code
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
