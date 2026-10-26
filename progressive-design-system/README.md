# Progressive Design System

**See ten directions. Choose by looking. Get a system that isn't the AI default.**

Builds or updates a complete, bespoke design system in a few visual rounds, from your brief, your inspirations and designer-style research. The result fits what it's for, uses what today's technology makes possible, and doesn't read as AI-made.

## How it works

1. **Brief:** one short round of questions on what the system is for, who it's for and every medium it serves (website, social, video, slides, app, print), played back for your confirmation.
2. **Inspirations:** it extracts only the qualities you like from each inspiration, layer by layer, and tags each with its source.
3. **Research:** the subject's own story, a map of the category (breaking its conventions is the default), type chosen from purpose with licence checks, colour built in OKLCH, and what each medium now makes possible.
4. **Design principles:** three to five statements of what the system chooses and what it gives up, used to judge every direction.
5. **Six visual rounds of ten directions:** direction, foundations, components, motion, imagery and voice, data and infographics. Each is rendered on real elements with your real copy, and the most predictable one is labelled as the AI default.
6. **Update mode:** add a new inspiration to an existing system and see a before-and-after of the whole system before anything changes.
7. **Final check:** contrast and grayscale on colours that must be told apart, reduced motion, and the specimen rendered at phone, desktop and feed size.

## What you get

- `tokens.json` in the W3C Design Tokens format (2025.10), importable with Tokens Studio, Style Dictionary or Terrazzo
- `DESIGN.md`: principles, rules with their reasons, and a full decision log
- `specimen.html`: every component in use with your real copy and live motion
- A Claude Design System artifact, where available

## Use

> I'm launching a small ceramics studio and need a visual identity: colours, fonts, the lot.

> Here's a site I love. Add what works about it to our design system. [attach DESIGN.md]

## Files

```
progressive-design-system/
  SKILL.md                         the workflow
  assets/DESIGN.md                 guide and decision-log template
  assets/specimen.html             specimen page shell
  assets/tokens.json               W3C token skeleton
  references/ai-defaults.md        common AI defaults, used to label directions
  references/decision-map.md       the six rounds and their decisions, with modules per medium
  references/research-standard.md  eight criteria for designer-style research
  scripts/color_check.py           WCAG and APCA contrast, gamut, grayscale and OKLCH ramps (standard library only)
  agents/openai.yaml               display metadata and a suggested prompt
```

## Install

Part of [progressive-skills](../README.md). To install all six and keep them in sync across machines:

```bash
git clone https://github.com/0xlloyd/progressive-skills.git ~/progressive-skills
~/progressive-skills/install.sh
```

To install only this skill, run `npx skills add 0xlloyd/progressive-skills --skill progressive-design-system`, or copy the `progressive-design-system/` folder into your skills directory (`~/.claude/skills/` for Claude Code). For Claude, you can also zip the folder and upload it as a custom skill.

## Works with

For a system that already lives in code (extracting, auditing, migrating or documenting tokens and components), use the design kit's `design-kit-design-system` instead. Works on its own. Web search makes the research stronger; without it, the skill researches from what the model knows and says which facts, especially font licences, need checking. It closes every run with [progressive-skill-improvement](../progressive-skill-improvement/README.md), which proposes evidence-backed edits to this skill for you to approve. If that skill isn't installed, it suggests the improvements directly.

## License

MIT. See [LICENSE](../LICENSE). Created by [Lloyd Bizaoui](https://github.com/0xlloyd).
