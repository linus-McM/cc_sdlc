# sdlc-knowledge-start
# Regenerates the OKF bundle after Graphify's rebuild. Installed by: sdlc knowledge bootstrap
[ "${GRAPHIFY_SKIP_HOOK:-0}" = "1" ] && exit 0
command -v uv >/dev/null 2>&1 || exit 0
_SK_GITDIR=$(cd "$(git rev-parse --git-dir 2>/dev/null)" 2>/dev/null && pwd)
_SK_COMMONDIR=$(cd "$(git rev-parse --git-common-dir 2>/dev/null)" 2>/dev/null && pwd)
if [ -n "$_SK_COMMONDIR" ] && [ "$_SK_GITDIR" != "$_SK_COMMONDIR" ]; then exit 0; fi
if [ -d "$_SK_GITDIR/rebase-merge" ] || [ -d "$_SK_GITDIR/rebase-apply" ] || [ -f "$_SK_GITDIR/MERGE_HEAD" ]; then exit 0; fi
_SK_CHANGED=$(git diff --name-only HEAD~1 HEAD 2>/dev/null || git diff --name-only HEAD 2>/dev/null)
echo "$_SK_CHANGED" | grep -qv -e '^__BUNDLE__/' -e '^graphify-out/' || exit 0
_SK_LOG="${HOME}/.cache/sdlc-knowledge.log"
mkdir -p "$(dirname "$_SK_LOG")"
(
  _SK_HEAD=$(git rev-parse HEAD); _SK_I=0
  mkdir -p "$_SK_GITDIR/sdlc" && echo "$_SK_HEAD" >"$_SK_GITDIR/sdlc/refresh-pending"
  while [ "$_SK_I" -lt 30 ] && ! grep -Eq "\"built_at_commit\": *\"$_SK_HEAD\"" graphify-out/graph.json 2>/dev/null; do sleep 2; _SK_I=$((_SK_I + 1)); done
  if [ "$(cat "$_SK_GITDIR/sdlc/refresh-pending" 2>/dev/null)" != "$_SK_HEAD" ]; then echo "[sdlc knowledge] refresh after ${_SK_HEAD} superseded by a newer commit"; exit 0; fi
  echo "[sdlc knowledge] $(date -u +%Y-%m-%dT%H:%M:%SZ) refresh after ${_SK_HEAD} (waited $((_SK_I * 2))s for graph.json)"
  uv run --no-project __SDLC_PY__ knowledge refresh
) >>"$_SK_LOG" 2>&1 &
# sdlc-knowledge-end
