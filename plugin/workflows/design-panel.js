export const meta = {
  "name": "design-panel",
  "description": "Design stage: three independent designs for an accepted intent plus policy-concern lenses, a judge panel, then one synthesized draft of the spec.md sections",
  "whenToUse": "After `sdlc design new`, when the intent admits more than one reasonable design. args: {slug}",
  "phases": [
    {"title": "Propose", "detail": "three designs from different angles, four concern lenses alongside"},
    {"title": "Judge", "detail": "two judges score every design against the intent"},
    {"title": "Synthesize", "detail": "draft spec.md from the winner, grafting the runners-up's best ideas"}
  ]
}

const slug = args && args.slug
if (!slug) throw new Error('args.slug is required (the feature directory under sdlc/)')

const GROUND = `Read sdlc/${slug}/intent.md (accepted) and CLAUDE.md, then the modules it touches. ` +
  'Start from sdlc/knowledge/index.md when it exists; for call-graph questions run `graphify query "<question>"`. ' +
  'Read-only: never edit, write or commit a file. Cite path:line for claims about existing code.'

const DESIGN = {
  type: 'object',
  properties: {
    summary: { type: 'string' },
    components: { type: 'array', items: { type: 'string' } },
    data_flow: { type: 'string' },
    interfaces: { type: 'array', items: { type: 'string' } },
    requirements: { type: 'array', items: { type: 'string' } },
    tradeoffs: { type: 'string' },
  },
  required: ['summary', 'components', 'data_flow', 'interfaces', 'requirements', 'tradeoffs'],
}
const CONCERNS = {
  type: 'object',
  properties: {
    concerns: {
      type: 'array',
      items: {
        type: 'object',
        properties: { concern: { type: 'string' }, owner: { type: 'string' }, conflict: { type: 'string' } },
        required: ['concern', 'owner', 'conflict'],
      },
    },
  },
  required: ['concerns'],
}

const ANGLES = [
  { key: 'minimal', ask: 'the smallest change to existing code that fully meets the intent' },
  { key: 'risk-first', ask: 'the design that minimises security, data-loss and failure-mode risk first' },
  { key: 'longevity', ask: 'the design with the cleanest interfaces for the next two likely changes' },
]
const LENSES = ['security', 'privacy and compliance', 'UX and accessibility', 'brand and organisation policy (load any matching organisation skills)']

phase('Propose')
const [proposals, concernSets] = await Promise.all([
  parallel(ANGLES.map((angle) => () =>
    agent(`${GROUND}\n\nPropose ${angle.ask}. Requirements must be numbered, testable and traced to the intent.`, { label: `design:${angle.key}`, phase: 'Propose', schema: DESIGN })
      .then((d) => d && { angle: angle.key, ...d }))),
  parallel(LENSES.map((lens) => () =>
    agent(`${GROUND}\n\nAs the ${lens} reviewer, list every policy concern this change raises, its owner, and say plainly where two policies contradict ("none" in conflict when they do not).`, { label: `concern:${lens.split(' ')[0]}`, phase: 'Propose', schema: CONCERNS, effort: 'low' }))),
])
const designs = proposals.filter(Boolean)
if (!designs.length) throw new Error('no design proposal came back')
const concerns = concernSets.filter(Boolean).flatMap((c) => c.concerns)

phase('Judge')
const SCORES = {
  type: 'object',
  properties: { scores: { type: 'array', items: { type: 'object', properties: { angle: { type: 'string' }, score: { type: 'number' }, why: { type: 'string' } }, required: ['angle', 'score', 'why'] } } },
  required: ['scores'],
}
const verdicts = (await parallel(['fit to the intent and testability', 'risk and cost of change'].map((lens) => () =>
  agent(`${GROUND}\n\nScore each design 1-10 on ${lens}; use each design's \`angle\` value verbatim. Designs (JSON):\n${JSON.stringify(designs, null, 2)}`, { label: `judge:${lens.split(' ')[0]}`, phase: 'Judge', schema: SCORES })))).filter(Boolean)
const total = (angle) => verdicts.flatMap((v) => v.scores).filter((s) => s.angle.trim().toLowerCase() === angle).reduce((sum, s) => sum + s.score, 0)
if (!designs.some((d) => total(d.angle) > 0)) log('no judge score matched a design; the winner below is proposal order, not a ranking')
const ranked = [...designs].sort((a, b) => total(b.angle) - total(a.angle))
log(`ranking: ${ranked.map((d) => `${d.angle}=${total(d.angle)}`).join(', ')}`)

phase('Synthesize')
const spec = await agent(
  `${GROUND}\n\nWinning design (JSON):\n${JSON.stringify(ranked[0], null, 2)}\n\nRunners-up:\n${JSON.stringify(ranked.slice(1), null, 2)}\n\n` +
  `Judge notes:\n${JSON.stringify(verdicts, null, 2)}\n\nConcerns:\n${JSON.stringify(concerns, null, 2)}\n\n` +
  'Draft the spec.md sections from the winner, grafting runner-up ideas only where the judges scored them higher. Keep every concern with its owner; merge duplicates. ' +
  'Answer or reassign each open question from intent.md. Proof names the test files and checks.',
  {
    phase: 'Synthesize',
    schema: {
      type: 'object',
      properties: {
        requirements: { type: 'array', items: { type: 'string' } },
        design: { type: 'string' },
        concerns: CONCERNS.properties.concerns,
        open_questions: { type: 'array', items: { type: 'string' } },
        proof: { type: 'string' },
        rejected: { type: 'string' },
      },
      required: ['requirements', 'design', 'concerns', 'open_questions', 'proof', 'rejected'],
    },
  },
)
return spec && { winner: ranked[0].angle, ...spec }
