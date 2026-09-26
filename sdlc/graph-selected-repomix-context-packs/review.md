# Review: graph-selected repomix context packs
Reviewer: sdlc:reviewer agent (two rounds) plus the sdlc:verifier agent. Status: done. Scope: the build commits a8320e7..HEAD, three passes per REVIEW.md. The first round read the stage's own test context pack first (`test-40456e15bfef.xml`, 81 files, ~466k tokens) and went outside it for the git diff, the Repomix 1.18.0 sources and a scratch repo.

## Bugs
- Important: plugin/scripts/sdlc/packs.py:255 an empty selection was refused: `p.changed_files(root)` with no paths listed every dirty file, and an empty stdin makes Repomix pack the whole repository, so a greenfield intent could never pass `plan accept`. Addressed in step `review-important`: the dirty check skips an empty selection and `run_repomix` writes an empty pack without running Repomix (`test_pack_with_no_selected_files_packs_nothing`).
- Important: plugin/scripts/sdlc/packs.py:57 a renamed file (`dir/{old => new}` in numstat) or a git-quoted path could never be seeded or covered, so the test gate was unpassable. Addressed in step `review-important`: `ls-files -z`, `diff --numstat -z --no-renames`, `check-ignore -z` (`test_review_covers_renames_and_lock_files`).
- Important: plugin/templates/knowledge/repomix.config.json:3 Repomix's default ignores dropped a requested `uv.lock`, and a changed symlink or git-ignored file was a permanent refusal. Addressed in step `review-important`: `useDefaultPatterns: false`, and the test gate accounts for symlink and git-ignored exclusions recorded in the manifest (`test_review_covers_renames_and_lock_files`, `test_review_accounts_for_excluded_changes`); the second round narrowed the accounting to those two rules in step `excluded-accounting-3` (`test_review_refuses_a_change_excluded_only_by_uncommitted_state`).

## Security
- Nit: plugin/scripts/sdlc/packs.py:380 paths can now carry a newline (`-z`), but Repomix still gets a newline-joined stdin; this fails closed through the scanner ("left requested files out") without saying why.
- Nit: plugin/scripts/sdlc/packs.py:345 Bandit's file arguments followed the options with no `--`, and plugin/scripts/sdlc/packs.py:101 `secret_rule` was case-sensitive (`SERVER.PEM`). Both fixed in step `review-important` (`test_secret_rules_ignore_case_and_bandit_ends_options`).

## Compliance
- Nit: plugin/scripts/sdlc/packs.py:164 `SDLC_PACKS=off` is a second off switch the accepted spec did not name (Requirement 16); declared as deviation 1 in plan.md Risks and accepted with the plan.
- Nit: plugin/scripts/sdlc/packs.py:240 the reuse key folds the effective budget, not the ladder rung (Requirement 9); declared as deviation 2 in plan.md Risks.
- Nit: plugin/commands/design.md:20 two steps numbered 5; renumbered in step `review-important`.

Nits: 5 of 5 reported. Verifier: 226 tests green after the fixes; ruff check and format clean; both `claude plugin validate --strict` pass; every planned file touched except tests/test_hooks.py (no step assertion needed a `repomix` row); three planned test names differ but cover the same cases (`test_expand_adds_community_members_and_callers`, parametrised `test_bandit_failure_refuses`). Real packs on this repository: build 69 files ~174k tokens, design 53 files ~152k tokens, test 81 files ~466k tokens, nothing in `git status`. The unbudgeted test pack is too large for most agent contexts: set `[knowledge] pack_max_tokens` on large branches.
