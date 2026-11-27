# Review instructions

## Passes
Run three passes and tag each finding with its pass:
- Bugs: logic errors, broken edge cases, subtle regressions
- Security: injection risks, authentication gaps, PII in logs
- Compliance: the change matches sdlc/<slug>/spec.md, plan.md and our design principles. Give every numbered spec.md requirement its own line: `- R<n>: met, <test or path:line that proves it>`, or an `Important:` finding that names `R<n>` when it is not met

## What Important means here
Reserve Important for findings that would break behaviour, leak data or breach a policy. Style and naming are nits.

## Cap the nits
Report at most five nits per review; summarise the rest as a count.

## Do not report
Generated files and anything CI already enforces.
