# Progressive Workflow

**Design the process the best practitioners would use. Run it. Keep it.**

For big tasks. Instead of pushing every task through the same fixed pipeline, it researches how experts do that kind of work, composes a task-specific workflow (a flow), runs it with approval gates, and saves it to a library so the next similar task starts from a proven process.

## How it works

1. **Frame the task:** goal, audience, definition of done and constraints, played back for your confirmation.
2. **Check the flow library:** a saved flow that fits is run as the baseline; related ones lend parts.
3. **Research how the work is best done:** reframe the task as a top professional would, find the bar-setters, and research the stages and checks they insist on.
4. **Compose the flow:** from a six-step spine (Understand, Research, Plan, Execute, Verify, Learn), each step with a reason, a tool and a "done when".
5. **Present the flow:** a compact table for you to approve, edit or reorder.
6. **Run the flow:** step by step, with a plan gate and options for judgement calls.
7. **Verify:** always runs: checks against each "done when", the flow's checks and the rules of every skill used, and opens what was made.
8. **Review the run:** what was intended, what happened, why, and what to change or repeat.
9. **Save the flow:** one file per task type in a library you own, merged with a dated changelog.

## What you get

- The work itself
- A saved flow per task type, such as `Flows/business-case.md`, that improves after every run

## Use

> Use flow to build a launch campaign for this product brief.

> /flow I need a business case for replacing our reconciliation tool.

> Use flow to make a 30-second product video. Just run it.

## Files

```
progressive-workflow/
  SKILL.md                     the workflow
  references/flow-template.md  the format for saved flows
  references/modules.md        a menu of common steps to add to the spine
  agents/openai.yaml           display metadata and a suggested prompt
```

## Install

Part of [progressive-skills](../README.md). To install all six and keep them in sync across machines:

```bash
git clone https://github.com/0xlloyd/progressive-skills.git ~/progressive-skills
~/progressive-skills/install.sh
```

To install only this skill, run `npx skills add 0xlloyd/progressive-skills --skill progressive-workflow`, or copy the `progressive-workflow/` folder into your skills directory (`~/.claude/skills/` for Claude Code). For Claude, you can also zip the folder and upload it as a custom skill.

## Works with

Say **"just run it"** to skip the check-ins and stop only at the plan. Uses `go-deeper` and [progressive-knowledge](../progressive-knowledge/README.md) for the research when they're installed, and applies the same approach directly when they aren't. It closes every run with [progressive-skill-improvement](../progressive-skill-improvement/README.md), which proposes evidence-backed edits to this skill for you to approve. If that skill isn't installed, it suggests the improvements directly.

## License

MIT. See [LICENSE](../LICENSE). Created by [Lloyd Bizaoui](https://github.com/0xlloyd).
