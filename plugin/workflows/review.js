export const meta = {
  "name": "review",
  "description": "Test stage: review the branch diff in three parallel passes (Bugs, Security, Compliance), adversarially verify every finding, and return review.md ready to write",
  "whenToUse": "During `/sdlc:test review`, in place of a single reviewer agent. args: {slug, base?}",
  "phases": [
    {"title": "Find", "detail": "one reviewer per pass"},
    {"title": "Verify", "detail": "two skeptics per finding"}
  ]
}

const slug = args && args.slug
if (!slug) throw new Error('args.slug is required (the feature directory under sdlc/)')
const base = (args && args.base) || 'main'

const GROUND = `Read REVIEW.md (else the plugin template), sdlc/${slug}/intent.md, spec.md, plan.md and \`git diff ${base}...HEAD\`. ` +
  'Start from sdlc/knowledge/index.md when it exists; for call-graph questions run `graphify query "<question>"`. ' +
  'Skip generated paths and anything CI already enforces. Read-only: never edit, write or commit a file. ' +
  'If a hook denies a command, quote the denial; never rewrite a command to get past a hook.'

const FINDINGS = {
  type: 'object',
  properties: {
    findings: {
      type: 'array',
      items: {
        type: 'object',
        properties: {
          severity: { type: 'string', enum: ['Important', 'Nit'] },
          problem: { type: 'string' },
          path: { type: 'string' },
          line: { type: 'integer' },
        },
        required: ['severity', 'problem', 'path', 'line'],
      },
    },
  },
  required: ['findings'],
}
const VERDICT = {
  type: 'object',
  properties: { refuted: { type: 'boolean' }, why: { type: 'string' } },
  required: ['refuted', 'why'],
}

const PASSES = [
  { key: 'Bugs', ask: 'behaviour that breaks: wrong results, crashes, races, missed edge cases, tests that do not test what they claim' },
  { key: 'Security', ask: 'injection, secrets, authn/authz gaps, unsafe subprocess or path handling, data leaks' },
  { key: 'Compliance', ask: 'breaches of REVIEW.md, CLAUDE.md conventions, spec.md requirements and plan.md scope' },
]
const LENSES = ['does it reproduce from the code as written', 'is it in scope of this diff and not already handled elsewhere']
const NITS = 5

const passes = await pipeline(
  PASSES,
  (pass) => agent(`${GROUND}\n\nPass: ${pass.key} — ${pass.ask}. Important is reserved for findings that would break behaviour, leak data or breach a policy.`, { label: `find:${pass.key}`, phase: 'Find', schema: FINDINGS }),
  (found, pass) => parallel((found ? found.findings : []).map((f) => () =>
    parallel(LENSES.map((lens) => () =>
      agent(`${GROUND}\n\nTry to refute this ${pass.key} finding through one lens: ${lens}. Default to refuted=true when the code does not support it.\n${JSON.stringify(f, null, 2)}`, { label: `verify:${f.path}:${f.line}`, phase: 'Verify', schema: VERDICT, effort: 'low' })))
      .then((votes) => {
        const refuted = votes.filter((v) => v && v.refuted).length
        const upheld = votes.filter((v) => v && !v.refuted).length
        if (refuted === LENSES.length) return null
        return refuted || !upheld ? { ...f, severity: 'Nit' } : f // one refutation or no verdict downgrades, two drop
      }))),
)

const kept = PASSES.map((pass, i) => (passes[i] || []).filter(Boolean))
const nits = kept.flat().filter((f) => f.severity === 'Nit')
const shown = new Set(nits.slice(0, NITS))
if (nits.length > NITS) log(`${nits.length - NITS} nit(s) beyond the review-wide cap of ${NITS} summarised as a count`)
const sections = PASSES.map((pass, i) => {
  const listed = kept[i].filter((f) => f.severity === 'Important' || shown.has(f))
  const bullets = listed.map((f) => `- ${f.severity}: ${f.problem} (${f.path}:${f.line})`)
  return `## ${pass.key}\n${bullets.length ? bullets.join('\n') : '- none'}`
})
const more = nits.length > NITS ? `\n\n${nits.length - NITS} more nit(s) not listed.` : ''
return {
  counts: Object.fromEntries(PASSES.map((pass, i) => [pass.key, {
    important: kept[i].filter((f) => f.severity === 'Important').length,
    nits: kept[i].filter((f) => f.severity === 'Nit').length,
  }])),
  markdown: sections.join('\n\n') + more + '\n',
}
