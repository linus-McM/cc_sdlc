export const meta = {
  "name": "release-readiness",
  "description": "Deploy stage: check a release in parallel (PR reviews and CI, rollback scope, PR body against the diff, ordering hazards) and return blockers and warnings; advisory, `sdlc deploy check` stays the gate",
  "whenToUse": "After `sdlc deploy pr` and before `sdlc deploy check <env>` for staging or production. args: {slug, env}",
  "phases": [
    {"title": "Check", "detail": "one agent per release hazard"}
  ]
}

const slug = args && args.slug
if (!slug) throw new Error('args.slug is required (the feature directory under sdlc/)')
const env = (args && args.env) || 'staging'

const GROUND = `Release of sdlc/${slug} to ${env}. Read sdlc/${slug}/plan.md, pr-body.md, deploy.json (when present) and the [deploy] table of .sdlc.toml. ` +
  'Read-only: never edit, commit, push, deploy or roll back; never set RELEASE_APPROVAL. If a hook denies a command, quote the denial.'

const HAZARDS = {
  type: 'object',
  properties: {
    hazards: {
      type: 'array',
      items: {
        type: 'object',
        properties: { blocker: { type: 'boolean' }, hazard: { type: 'string' }, evidence: { type: 'string' }, fix: { type: 'string' } },
        required: ['blocker', 'hazard', 'evidence', 'fix'],
      },
    },
  },
  required: ['hazards'],
}

const CHECKS = [
  { key: 'pr', ask: 'Run `gh pr view --json number,reviewDecision,statusCheckRollup,comments,reviews` for this branch. Unresolved review comments and failing or pending checks are blockers.' },
  { key: 'rollback', ask: 'Is deploy.rollback rehearsed (a passing rehearsal in deploy.json) and scoped to what a rehearsal may touch? Flag remote-mutating steps (git push, tags, kubectl, gh) that the worktree rehearsal did not isolate.' },
  { key: 'pr-body', ask: 'Does pr-body.md match `git diff main...HEAD` and plan.md "Files that change"? Flag changed files it omits and claims the diff does not support.' },
  { key: 'ordering', ask: 'Does the diff contain migrations, config or secret changes, feature flags or API contract changes that need an ordered or staged rollout to this environment?' },
]

phase('Check')
const reports = await parallel(CHECKS.map((c) => () =>
  agent(`${GROUND}\n\nCheck: ${c.key}. ${c.ask}`, { label: `check:${c.key}`, phase: 'Check', schema: HAZARDS, effort: 'low' })
    .then((r) => r && r.hazards.map((h) => ({ check: c.key, ...h })))))
const unchecked = CHECKS.filter((c, i) => !reports[i]).map((c) => c.key)
if (unchecked.length) log(`no report from: ${unchecked.join(', ')}; treat those checks as not run`)
const found = reports.filter(Boolean).flat()

const blockers = found.filter((h) => h.blocker)
return {
  env,
  ready: blockers.length === 0 && unchecked.length === 0,
  unchecked,
  blockers,
  warnings: found.filter((h) => !h.blocker),
  note: 'advisory only: run `sdlc deploy check <env>` for the gate verdict',
}
