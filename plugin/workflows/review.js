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
        if (refuted === LENSES.length) return null
        return refuted ? { ...f, severity: 'Nit' } : f // one refutation downgrades, two drop
      }))),
)

const sections = PASSES.map((pass, i) => {
  const kept = (passes[i] || []).filter(Boolean)
  const important = kept.filter((f) => f.severity === 'Important')
  const nits = kept.filter((f) => f.severity === 'Nit')
  if (nits.length > NITS) log(`${pass.key}: ${nits.length - NITS} nit(s) beyond the cap of ${NITS} summarised as a count`)
  const bullets = [...important, ...nits.slice(0, NITS)].map((f) => `- ${f.severity}: ${f.problem} (${f.path}:${f.line})`)
  if (nits.length > NITS) bullets.push(`- Nit: ${nits.length - NITS} more nit(s) not listed`)
  return { pass: pass.key, important: important.length, nits: nits.length, text: `## ${pass.key}\n${bullets.length ? bullets.join('\n') : '- none'}` }
})
return {
  counts: Object.fromEntries(sections.map((s) => [s.pass, { important: s.important, nits: s.nits }])),
  markdown: sections.map((s) => s.text).join('\n\n') + '\n',
}
