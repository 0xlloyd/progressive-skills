#!/bin/zsh
# Sync this repo with GitHub.
#
#   sync.sh                       pull the latest skills
#   sync.sh "what you changed"    commit every local change, pull, then push

set -e
cd "${0:A:h}"

if (( $# )); then
  git add -A
  git diff --cached --quiet || git commit -m "$*"
  git pull --rebase --quiet
  git push --quiet
  echo "pushed: $(git log -1 --format='%h %s')"
else
  git pull --ff-only --quiet
  echo "up to date: $(git log -1 --format='%h %s')"
fi
