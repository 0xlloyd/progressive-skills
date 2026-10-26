#!/bin/zsh
# Install the progressive skills on this machine. Safe to re-run.
#
# 1. Symlinks every skill folder in this repo into ~/.claude/skills, so Claude reads them live from here.
# 2. Adds a SessionStart hook to ~/.claude/settings.json that pulls this repo at the start of every
#    Claude session, so improvements pushed from another machine are picked up automatically.

setopt null_glob
REPO="${0:A:h}"
TARGET="$HOME/.claude/skills"
mkdir -p "$TARGET"

for md in "$REPO"/*/SKILL.md; do
  src=${md:h} n=${src:t} dest="$TARGET/$n"
  if [[ -L $dest ]]; then
    [[ $(readlink "$dest") == $src ]] && continue
    ln -sfn "$src" "$dest" && echo "relinked  $n"
  elif [[ -e $dest ]]; then
    echo "SKIPPED   $n (something else already exists at $dest)"
  else
    ln -s "$src" "$dest" && echo "linked    $n"
  fi
done

REPO="$REPO" python3 - <<'EOF'
import json, os
path = os.path.expanduser("~/.claude/settings.json")
settings = json.load(open(path)) if os.path.exists(path) else {}
repo = os.environ["REPO"].replace(os.path.expanduser("~"), "$HOME", 1)
cmd = f'git -C "{repo}" pull --ff-only --quiet >/dev/null 2>&1 || true'
entries = settings.setdefault("hooks", {}).setdefault("SessionStart", [])
if any(h.get("command") == cmd for e in entries for h in e.get("hooks", [])):
    print("hook      already installed")
else:
    entries.append({"hooks": [{"type": "command", "command": cmd, "timeout": 15}]})
    with open(path, "w") as f:
        json.dump(settings, f, indent=2)
        f.write("\n")
    print("hook      added SessionStart pull to ~/.claude/settings.json")
EOF
