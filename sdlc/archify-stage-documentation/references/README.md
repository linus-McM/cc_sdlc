# References for archify-stage-documentation

- `archify-repomix.md`: repomix pack of https://github.com/tt-a1i/archify (skill v2.17: SKILL.md,
  CLI entry points `bin/*.mjs`, the five JSON schemas, examples, authoring/delivery/viewer-runtime
  contracts, README install matrix; rendered HTML, PNG, SVG, tests and docs site dropped).
  Regenerate from the repo root:
  `cd sdlc/archify-stage-documentation/references && repomix --remote https://github.com/tt-a1i/archify --style markdown --compress --include "**/SKILL.md,README.md,**/package.json,**/skill-release.json,**/schemas/**,**/examples/*.json,**/recipes/**,**/references/**,**/scripts/check-update.mjs,**/bin/*.mjs" --ignore "**/*.html,**/*.png,**/*.svg,**/node_modules/**,**/test/**,**/docs/**" -o archify-repomix.md`
- Install path documented by the repo (README "Install"): `npx skills add tt-a1i/archify -g`
  puts the skill at `~/.claude/skills/archify/` (needs Node >= 18). Non-interactive variant:
  `npx -y skills add tt-a1i/archify --skill archify --agent claude-code --global --copy --yes`.
- CLI surface used by this feature: `node ~/.claude/skills/archify/bin/archify.mjs
  validate|deliver <type> <spec.json> [<out.html>] --quality showcase --json`,
  `guide "<scenario>" --json`, `bin/open-artifact.mjs <out.html>`, `bin/visual-check.mjs`.
