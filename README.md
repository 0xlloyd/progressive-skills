# progressive-skills

Agent skills that build something with you in stages, each step feeding the next, with you approving as it goes.

| Skill | What it does |
|-------|--------------|
| [progressive-workflow](progressive-workflow/SKILL.md) | Designs an expert workflow for a big task, runs it with approval gates, saves it to a library |
| [progressive-skill](progressive-skill/SKILL.md) | Co-writes a new skill one approved sentence at a time |
| [progressive-knowledge](progressive-knowledge/SKILL.md) | Sets the elite-practitioner standard for a task, does the work to it, saves a knowledge file |
| [progressive-voice](progressive-voice/SKILL.md) | Interviews you and builds a voice skill that writes and talks like you |
| [progressive-skill-improvement](progressive-skill-improvement/SKILL.md) | After a session, proposes evidence-backed edits to the skill that was used; every other progressive skill runs it as its closing step |

## Install

```bash
git clone https://github.com/0xlloyd/progressive-skills.git ~/progressive-skills
~/progressive-skills/install.sh
```

`install.sh` symlinks each skill into `~/.claude/skills` and adds a `SessionStart` hook to `~/.claude/settings.json` that pulls this repo at the start of every Claude session. Re-running it is safe.

## Keeping machines in sync

GitHub is the source of truth. Edit the skills in `~/progressive-skills`, then push:

```bash
~/progressive-skills/sync.sh "describe the change"
```

Every other machine picks the change up at its next Claude session. Run `sync.sh` with no message to pull by hand.

If you edited on two machines without syncing in between, `sync.sh "..."` rebases your commit onto the other one before pushing. A conflict stops it, and you finish with `git rebase --continue`.

## License

MIT. See [LICENSE](LICENSE).
