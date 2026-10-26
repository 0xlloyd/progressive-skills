# Flow

**Design the process the best practitioners would use. Run it. Keep it.**

Flow is an AI skill for big tasks. Instead of pushing every task through the same fixed pipeline, it researches how experts actually do that kind of work, composes a task-specific workflow, runs it with approval gates, and saves the workflow to a library so the next similar task starts from a proven process.

A marketing piece needs references and a copy pass. A video needs a shot list and a review of takes. A business case needs criteria and costings. Flow works out which steps the task needs, and why.

## How a run works

| Step | What happens |
| --- | --- |
| 1. Frame the task | Goal, audience, definition of done, constraints; played back for confirmation |
| 2. Check the flow library | A saved flow that fits is run as the baseline; related ones lend parts |
| 3. Research how the work is best done | Reframe the task as a top professional would, find the bar-setters, and research the stages and checks experts insist on |
| 4. Compose the flow | Start from a six-step spine (Understand, Research, Plan, Execute, Verify, Learn), add modules, give each step a reason, a tool and a "done when" |
| 5. Present the flow | A compact table for the user to approve, edit or reorder |
| 6. Run the flow | Step by step, with a plan gate and options for judgement calls |
| 7. Verify | Always runs: checks against done-when, the flow's checks and skill rules; opens what was made |
| 8. Review the run | After-action review: intended, happened, why, change or repeat |
| 9. Save the flow | One markdown file per task type in a library folder the user owns, merged with a dated changelog |

Say **"just run it"** to skip the check-ins and stop only at the plan.

## Built on

- **Situational method engineering**: compose a method from stored pieces, chosen by the situation, and check it for consistency.
- **Toyota standard work and kaizen**: the saved flow is the baseline; improvements edit the standard itself.
- **After-action review**: four questions, causes not blame, keep what worked.
- **Checklist design**: named pause points, short do-confirm lists of critical, easy-to-miss checks.

## Try it

> Use flow to build a launch campaign for this product brief.

> /flow — I need a business case for replacing our reconciliation tool.

> Use flow to make a 30-second product video. Just run it.

## Install

The skill is the [`skills/flow`](skills/flow) folder. Keep `references/` alongside `SKILL.md`.

- **Claude:** zip the `flow` folder (not the whole repository) and upload it as a custom skill, following Anthropic's [instructions](https://support.claude.com/en/articles/12512180-use-skills-in-claude).
- **Other hosts:** use the host's skill-loading mechanism; the instructions are plain Markdown.

Flow works on its own. If the optional `go-deeper`, `best-in-class` or `session-self-learning` skills are installed, it uses them; otherwise it applies the same approach directly.

## Contents

- [`skills/flow/SKILL.md`](skills/flow/SKILL.md): the operating instructions.
- [`references/flow-template.md`](skills/flow/references/flow-template.md): the format for saved flows.
- [`references/modules.md`](skills/flow/references/modules.md): a menu of common steps to add to the spine.
