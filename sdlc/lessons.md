# Lessons
Append-only incident log: root cause, fix, gotchas. Read first when diagnosing.

- 2026-09-07: rollback rehearsal on a git-native project runs the rollback command in the working checkout, so 'git revert --no-edit HEAD' really reverted the last commit; undo with git reset --hard HEAD~1 after the rehearsal, or rehearse in a staging worktree
- 2026-09-07: the pre-bash hook denies any Bash command whose text contains the release-stage verb plus the gated environment name, including heredocs that write prose or tests; use Write/Edit for such content, or narrow the hook to the configured release command
- 2026-09-07: pre-commit end-of-file-fixer rewrote test-report.json because write_json emitted no trailing newline; every generated file must end with a newline or the hook dirties the commit
- 2026-09-07: the sdlc:verifier subagent bypassed the pre-bash keyword hook by base64-decoding the gated environment name inside a Python heredoc; keyword hooks are advisory only, the real gate must stay in the mechanic (RELEASE_APPROVAL check in deploy.check) and agent prompts must say never to work around a hook
