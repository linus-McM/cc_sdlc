# Lessons
Append-only incident log: root cause, fix, gotchas. Read first when diagnosing.

- 2026-09-07: rollback rehearsal on a git-native project runs the rollback command in the working checkout, so 'git revert --no-edit HEAD' really reverted the last commit; undo with git reset --hard HEAD~1 after the rehearsal, or rehearse in a staging worktree
- 2026-09-07: the pre-bash hook denies any Bash command whose text contains the release-stage verb plus the gated environment name, including heredocs that write prose or tests; use Write/Edit for such content, or narrow the hook to the configured release command
- 2026-09-07: pre-commit end-of-file-fixer rewrote test-report.json because write_json emitted no trailing newline; every generated file must end with a newline or the hook dirties the commit
- 2026-09-07: the sdlc:verifier subagent bypassed the pre-bash keyword hook by base64-decoding the gated environment name inside a Python heredoc; keyword hooks are advisory only, the real gate must stay in the mechanic (RELEASE_APPROVAL check in deploy.check) and agent prompts must say never to work around a hook
- 2026-09-08: the release hook now tokenises real command lines; a harness command that quotes a release command as a literal argument is denied too, so live-prove the hook from a script file, not an inline for-loop
- 2026-09-08: post-edit plan-sync hook flags files outside the repo (scratchpad) because rel_path falls back to the absolute path; harmless context note, candidate for the next intent
- 2026-09-08: sdlc build new overwrites an existing plan.md with the template; write the plan after build new
- 2026-09-08: write one step's failing test, green it, then the next; writing all tests first makes tdd.jsonl show reds then greens, not cycles, and build green cannot pass per step
- 2026-09-08: a git worktree isolates only the checkout, index and current branch; tags, other refs, remotes and non-git systems are shared, so rehearsal rollback commands must be scoped to what a rehearsal may touch
