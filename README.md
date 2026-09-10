# sdlc

A Claude Code plugin that runs the [AI-native SDLC playbook](https://claude.com/blog/the-ai-native-sdlc-playbook) as six slash commands: `/sdlc:plan`, `/sdlc:design`, `/sdlc:build`, `/sdlc:test`, `/sdlc:deploy`, `/sdlc:maintain`. Every stage ends by committing an artifact under `sdlc/<feature>/`; the next stage refuses to start until a human has accepted it. The gates are Python, not prose, so Claude cannot talk its way past one.

- Site: [https://linus-mcm.github.io/cc_sdlc/](https://linus-mcm.github.io/cc_sdlc/)
- Architecture diagram: [https://linus-mcm.github.io/cc_sdlc/docs/architecture/sdlc-plugin.html](https://linus-mcm.github.io/cc_sdlc/docs/architecture/sdlc-plugin.html)
- Plugin reference (hooks, knowledge layer, stage documents, config): [`plugin/README.md`](plugin/README.md)
- Workflow diagram of the six commands (participants, order, branches, exceptions): [https://linus-mcm.github.io/cc_sdlc/diagrams/sdlc-commands.html](https://linus-mcm.github.io/cc_sdlc/diagrams/sdlc-commands.html), source in [`diagrams/`](diagrams/)

## Install

```sh
claude plugin marketplace add linus-McM/cc_sdlc
claude plugin install sdlc@sdlc
```

Try a checkout without installing: `claude --plugin-dir ./plugin`.

Requirements: Claude Code, git, Python 3.11+ and [uv](https://docs.astral.sh/uv/) (the plugin installs uv on first use if it is missing). Node 18+ is optional and enables the stage diagrams.

## Set up a project

Run the first command in any git repository:

```
/sdlc:plan new "Add rate limiting to the public API"
```

It creates:

| Path                      | Purpose                                                                                                                                                        |
| ------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `.sdlc.toml`            | project config: test/lint/build commands, protected paths, environment tiers, rollback command, metrics path,`[knowledge]` and `[docs]` tables. Commit it. |
| `sdlc/<slug>/intent.md` | the first artifact;`<slug>` is derived from the title                                                                                                        |
| `sdlc/knowledge/`       | the project knowledge bundle Claude reads before raw files (rebuilt after every commit)                                                                        |

Edit `.sdlc.toml` at least once: set `[commands] test` to the command that must fail on a red test, and fill `[deploy] rollback` before you reach production. Copy `plugin/templates/REVIEW.md` to the repo root to tell the reviewer what "Important" means in your codebase, and `plugin/templates/bands.toml` to `sdlc/` when you reach the maintain stage.

## The six commands

Every command calls the plugin's `sdlc.py` script and acts on a JSON verdict (`ok`, `reason`, `next`). When a gate refuses, Claude quotes the reason and stops; it never edits the verdict logic. [`diagrams/sdlc-commands.html`](diagrams/sdlc-commands.html) shows all six as one workflow: who acts, in what order, where it branches and where it stops.

### 1. `/sdlc:plan` — capture the intent

```
/sdlc:plan new "<title>"      # create sdlc/<slug>/intent.md and interview you
/sdlc:plan check              # validate the artifact
/sdlc:plan accept             # product owner accepts; commits the intent
/sdlc:plan status             # which artifacts are accepted, present or missing
```

Claude interviews the originator (what cannot be done today, who is affected, what better looks like, what is out of scope) and writes the answers into `intent.md`. Changes touching auth, PII, payments, migrations or infrastructure are marked `Risk: high`. `accept` is refused until the artifact validates and its stage diagram is fresh; only a human accepts.

### 2. `/sdlc:design` — turn the intent into a spec

```
/sdlc:design new              # blocked until intent.md is accepted; writes spec.md
/sdlc:design check
/sdlc:design accept           # product owner accepts; commits the spec
```

`spec.md` holds numbered testable requirements traced to the intent, the design (components, data flow, interfaces), a Concerns section listing every policy conflict with its owner, and the proof (test files and checks). Concerns are walked through with the product owner before engineering sees the spec.

### 3. `/sdlc:build` — plan, then implement red→green

```
/sdlc:build new               # blocked until spec.md is accepted; writes plan.md in plan mode
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

## Stage diagrams

Each stage ends with a diagram the acceptor can look at, delivered as standalone HTML under `sdlc/<slug>/docs/` (`plan` architecture, `design` data flow, `build` workflow, `test` sequence, `deploy` lifecycle, plus a project-wide `sdlc/docs/maintain.html` for the bands). Accepting a stage is refused until its diagram is fresh against the artifact. Diagrams need Node 18+ and the [Archify](https://github.com/tt-a1i/archify) skill, installed only when `[knowledge] auto_install = true`; without them the stages continue and the diagram step is skipped. Publish the `docs/` output with GitHub Pages to get a browsable site like the one linked above.

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

The installable package is `plugin/`; the repo root holds the tests, CI and the marketplace manifest. The plugin dogfoods itself on the `dogfood` branch, which GitHub Pages serves.

## Acknowledgements

Runtime tools and skills the plugin installs or drives:

- [Claude Code](https://docs.claude.com/en/docs/claude-code) by Anthropic, the host for the commands, agents and hooks, and the [AI-native SDLC playbook](https://claude.com/blog/the-ai-native-sdlc-playbook) the six stages follow.
- [uv](https://github.com/astral-sh/uv) by Astral, which runs every mechanic and hook through `uv run --no-project`.
- [Graphify](https://github.com/Graphify-Labs/graphify) (`graphifyy` on PyPI) by Safi Shamsi and Graphify Labs, the AST knowledge graph behind `graphify-out/` and the call-graph queries.
- [Open Knowledge Format](https://github.com/GoogleCloudPlatform/open-knowledge-format) v0.2 by Google Cloud, the bundle layout of `sdlc/knowledge/`; the articles by Udaykiran Estari on combining Graphify and OKF shaped the trust model and freshness checks.
- [Archify](https://github.com/tt-a1i/archify) by tt-a1i, which renders the stage diagrams, installed through the [skills](https://www.npmjs.com/package/skills) CLI.
- [GitHub CLI](https://cli.github.com/), used by the deploy and maintain stages.

Development tooling: [pytest](https://pytest.org/), [pytest-cov](https://github.com/pytest-dev/pytest-cov), [ruff](https://github.com/astral-sh/ruff), [bandit](https://github.com/PyCQA/bandit), [pre-commit](https://pre-commit.com/) with [pre-commit-hooks](https://github.com/pre-commit/pre-commit-hooks), and [just](https://github.com/casey/just).
