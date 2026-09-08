# sdlc-knowledge-start
# Regenerates the OKF bundle after Graphify's rebuild. Installed by: sdlc knowledge bootstrap
[ "${GRAPHIFY_SKIP_HOOK:-0}" = "1" ] && exit 0
command -v python3 >/dev/null 2>&1 || exit 0
_SK_GITDIR=$(cd "$(git rev-parse --git-dir 2>/dev/null)" 2>/dev/null && pwd)
_SK_COMMONDIR=$(cd "$(git rev-parse --git-common-dir 2>/dev/null)" 2>/dev/null && pwd)
if [ -n "$_SK_COMMONDIR" ] && [ "$_SK_GITDIR" != "$_SK_COMMONDIR" ]; then exit 0; fi
if [ -d "$_SK_GITDIR/rebase-merge" ] || [ -d "$_SK_GITDIR/rebase-apply" ] || [ -f "$_SK_GITDIR/MERGE_HEAD" ]; then exit 0; fi
_SK_CHANGED=$(git diff --name-only HEAD~1 HEAD 2>/dev/null || git diff --name-only HEAD 2>/dev/null)
echo "$_SK_CHANGED" | grep -qv -e '^__BUNDLE__/' -e '^graphify-out/' || exit 0
_SK_LOG="${HOME}/.cache/sdlc-knowledge.log"
mkdir -p "$(dirname "$_SK_LOG")"
(
  _SK_MARK="$_SK_GITDIR/logs/HEAD"; _SK_I=0
  while [ "$_SK_I" -lt 30 ] && ! [ graphify-out/graph.json -nt "$_SK_MARK" ]; do sleep 2; _SK_I=$((_SK_I + 1)); done
  echo "[sdlc knowledge] $(date -u +%Y-%m-%dT%H:%M:%SZ) refresh after $(git rev-parse --short HEAD) (waited $((_SK_I * 2))s for graph.json)"
  python3 "__PLUGIN_ROOT__/scripts/sdlc.py" knowledge refresh --quiet
) >>"$_SK_LOG" 2>&1 &
# sdlc-knowledge-end
