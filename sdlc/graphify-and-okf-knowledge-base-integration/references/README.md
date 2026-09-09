# References for graphify-and-okf-knowledge-base-integration

- `okf-repomix.md`: repomix pack of https://github.com/GoogleCloudPlatform/open-knowledge-format
  (SPEC.md v0.2, README, reference agent source, sample bundles; generated viz.html dropped).
  Regenerate: `repomix --remote https://github.com/GoogleCloudPlatform/open-knowledge-format --style markdown --compress --ignore "bundles/**/viz.html,**/*.png,LICENSE.md,CODE_OF_CONDUCT.md" -o okf-repomix.md`
- `article-notes.md`: notes from the nine Udaykiran Estari articles (Medium / Towards AI / Level Up Coding, Jul-Aug 2026):
  1. Standardizing Agent Memory: Self-Updating Codebase Knowledge Graph with OKF (pipeline)
  2. Graphify, OKF, or Both? Beyond RAG for Codebases (three layers, decision triggers)
  3. From Self-Updating OKF Wiki to Production Trust System (v0.2 trust model, roles, CI policy)
  4. Production-Grade OKF + Graphify Setup, Not Just a Demo (silent hook failures, freshness observability)
  5. Knowledge-Graph Skills for Claude Code and Codex: Graphify and Rivals Compared (tool selection)
  6. Your Vector DB is Shredding Context. Google OKF is the Fix. (deterministic retrieval, hybrid router)
  7. The Graph That Lied for Three Weeks (cache coherence: hashing, invalidation, tombstones, clean-rebuild cadence)
  8. Your Agent Memory Is a Dependency, Not a Superpower (memory contract, challenge gate)
  9. OpenWiki in 2026 (alternative narrative-layer producer)
