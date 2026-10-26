# progressive-skills

**Research the craft. Approve every step. Keep what you learn.**

Agent skills that build something with you in stages, each step feeding the next, with you approving as it goes. Each one researches how the best practitioners do the work, keeps you as the decision-maker, and ends by improving itself from the session.

| Skill | What it does |
|-------|--------------|
| [progressive-design-system](progressive-design-system/README.md) | Builds a bespoke design system in a few visual rounds of ten directions: W3C tokens, DESIGN.md and a live specimen |
| [progressive-knowledge](progressive-knowledge/README.md) | Sets the standard elite practitioners work to, does the work to it, and saves a knowledge file |
| [progressive-skill-creation](progressive-skill-creation/README.md) | Co-writes a new skill with you, one approved sentence at a time |
| [progressive-voice](progressive-voice/README.md) | Interviews you and builds a voice skill that writes and talks like you |
| [progressive-workflow](progressive-workflow/README.md) | Designs the expert process for a big task, runs it with approval gates, and saves it to a library |
| [progressive-skill-improvement](progressive-skill-improvement/README.md) | Turns what a session taught into edits you approve; every other progressive skill runs it as its closing step |

## Shared format

Every skill follows the same shape, so they read as one set:

- **`SKILL.md`:** frontmatter with `name`, a `description` that says what the skill does and then when to use it, and `metadata` (`category: progressive`, `tags`, `source`). The body opens with **Purpose**, works through plain-named sections, and ends with **Output** and **Close**, where Close runs `progressive-skill-improvement` (which itself ends at Output, so it never runs on itself).
- **`README.md`:** tagline, intro, How it works, What you get, Use, Files, Install, Works with, License.
- **`agents/openai.yaml`:** display name, short description and a suggested prompt.

New skills follow the same shape. `progressive-skill-creation` writes the closing step for you.

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
