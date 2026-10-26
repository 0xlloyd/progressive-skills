---
name: progressive-design-system
description: 'Co-design a new, bespoke design system with the user from scratch in a few visual rounds of ten rendered directions, where they choose by looking and nothing enters the system until they approve it, then deliver W3C design tokens, a DESIGN.md guide, a live specimen and, where available, a Claude Design System artifact. Use when the user wants a new design system, look and feel or visual identity (colour, type, motion, imagery) for a brand, website, social content, slides or an app, wants to see directions and choose, says "design system with me", "step by step" or "progressive design system", or shares a new inspiration (a website, image or screenshot) to fold into an existing system, even if they don''t say "design system". Not for a system that already lives in code (extracting, auditing, migrating or documenting tokens and components), which `design-kit-design-system` handles, or a logo on its own, which `design-kit-brand-identity` handles.'
metadata:
  category: progressive
  tags: [design, design-system]
  source: https://github.com/0xlloyd/progressive-skills
---

# Progressive Design System

## Purpose

This skill keeps the user as the designer: it researches, shows rendered directions and records decisions, but nothing enters the design system until the user has chosen it or asked the skill to decide.
Left to themselves, AI tools produce the statistical average of what they've seen (Inter, purple–indigo gradients, a centred hero with three rounded cards), and asking them to avoid it just shifts them to the next most common choice, such as warm cream with a terracotta accent.
So the skill works the way a design studio presents: a few rounds of complete, rendered directions, with the most predictable one labelled as the AI default and every other traced to the brief, an inspiration or research, so the user chooses by looking rather than by answering questions.
Keep questions few, because a long run of narrow questions tires the user and fragments the system; derive the small details from the big choices instead.

## Modes

Start by working out whether the user is creating a new design system or updating an existing one with a new inspiration; if the request makes it clear (for example, a new inspiration shared alongside a DESIGN.md), say which mode you're in rather than asking.
For an update, ask for the existing system's files (tokens, DESIGN.md or a link) before anything else.
A new system runs every section below in order, while an update reads the existing files first and then follows Update mode.

## Brief

Gather the brief in one short round of questions, taking anything the conversation already answers: what the system is for, who it's for, every medium it must serve (website, social posts and carousels, video, slides, app, print), the feeling it should give, and any constraints such as existing logos or colours, paid versus free fonts, and accessibility targets.
Ask for real copy the system will carry (a headline, a paragraph, a number), and if there is none, draft some in the user's voice, because choices judged on placeholder text hide real problems.
Play the answers back as a short brief and get the user's confirmation, since every later direction is judged against it.

## Inspirations

Invite the user to share anything whose look or feel they like (websites, screenshots, photos, packaging, posters, film, places), noting that inspirations from outside design galleries usually give the most distinctive results.
For each one, extract its usable qualities layer by layer (colour with values, type or its closest free match, layout and density, shapes, components, motion, imagery and tone) and tag each with its source.
Ask which qualities drew the user to each inspiration and keep only those, because an inspiration is a source of qualities to adapt, not a design to copy.
When a site can't be reached, ask for screenshots or a screen recording (for motion); when a typeface can't be identified with confidence, offer the closest matches rather than guessing.
If an inspiration brings something the standard layers don't cover, such as a texture, an unusual grid or an illustration style, add it as an extra layer for the rounds ahead.

## Research

Before showing any directions, research the way a senior designer would, following `references/research-standard.md`: the subject's own story, the category, type chosen from purpose and checked for licence and language coverage, colour built in OKLCH for each medium, and the art of the possible.
Start with the subject's own story (its history, place, era, materials and audience), because that's where ideas nobody else can copy come from.
Map four to eight others in the category, name the conventions they share, and treat breaking them as the default stance, so the system traces its own trail; following a convention must be a deliberate choice the user makes, with its reason logged.
Then research what today's technology makes possible in each medium the brief names (for example variable fonts, wide-gamut colour, scroll-driven and view-transition animation on the web, animated carousels and video for social, generative patterns, 3D and live data), and carry the most promising into the rounds as options rather than extras.
Share the findings as a short visual summary with sources and get the user's reactions before the first round.
If web search isn't available, research from what you already know and say which facts need checking, especially font licences.

## Design principles

From the brief, inspirations and research, propose three to five design principles, each a short statement of a choice the system makes and what it gives up, such as "Dense over airy: show more data per screen, even if it feels less calm".
Revise them until the user approves, then use them as the yardstick for every direction, saying which principle each one serves.

## How a round works

Each round shows ten complete directions at once, more on request, and each direction is a bundle that answers every decision in that round together, so one choice settles many details.
Render every direction on real elements of the user's medium using their real copy (a hero, nav and footer for a website; a cover and content slide for a carousel; a frame sequence for motion), never as names, hex codes or text alone, because design choices can't be judged without seeing them.
Keep every direction cohesive with what's already decided and check it against every earlier rule before showing it, such as contrast, "pastels are never text" or a chosen type scale, so the user is never offered something that breaks the system.
Make one direction the AI default within what's already decided (in the first round, within the brief): the most predictable result an AI tool would produce, checked against `references/ai-defaults.md`; label every other direction bespoke with its source and the principle it serves.
Let the user pick one, mix parts of several, ask for more, or ask you to decide; if none fit, ask what's missing in one question before generating again.
Record each choice in the decision log in DESIGN.md (started from `assets/DESIGN.md`) as soon as it's made, with every detail the bundle settled, its label, source and the user's reason, marking anything the user asked you to decide as "delegated".
After each round, update the specimen page so the user sees the system come together.

## The rounds

Run six rounds in this order, using the modules in `references/decision-map.md` that match the media in the brief, because each round builds on the ones before it:

1. **Direction:** the overall look and feel, shown as ten full mockups that each combine colour, type, shape and motion.
2. **Foundations:** palette with ramps and roles, type family and scale, spacing, radius, borders and elevation, shown as complete specimens.
3. **Components:** the medium's real elements as a kit (for a website: nav, hero, buttons, forms, cards, tables, footer, modals, toasts and their states; for social: cover, content, data and end templates), shown as assembled pages or sequences.
4. **Motion:** how things move in each medium (for a website: micro-interactions, scroll and page transitions; for social: animated carousels, video posts and motion graphics), shown as live animations, with "still" as one direction rather than the default.
5. **Imagery and voice:** photography, illustration, icons, graphic devices and tone of copy, shown in place on the components.
6. **Data and infographics:** charts, diagrams, tables and stat treatments, shown with the user's real numbers.

Add a round for any extra layer the user accepted from an inspiration.
After the rounds, derive the remaining details (exact ramps, states, durations, breakpoints and the like) and show them in one batch for review, so the user can change any of them without answering each one.
If the user only needs some media or rounds, run those and mark the rest "not yet decided" in DESIGN.md for a later session.

## Update mode

Read the existing DESIGN.md, tokens and decision log first, so you know every decision already made, its source and the principles behind it; if there's no decision log, rebuild one from the tokens and guide, mark each source as unknown, and confirm it with the user.
Extract only the qualities the user says drew them to the new inspiration, and adapt them to the existing system rather than copying them in, for example taking an inspiration's warmth by shifting the existing palette's hue rather than replacing it with the inspiration's colours.
Then check every decision against the adapted qualities and show the result as one rendered before-and-after of the whole system, listing what would change and why, because a new colour or motion style can quietly break contrast, states or imagery elsewhere.
For the changes the user wants to explore, run a round of ten directions that includes keeping the current system, and let the user confirm everything that stays the same in one batch.
If the new inspiration conflicts with an approved principle, point it out and ask whether to adapt the inspiration further or revise the principle, rather than letting the system drift.
Add the inspiration and every change it caused to the decision log with the date, so the system's history shows why it looks the way it does.

## Final check

Before delivering, run `scripts/color_check.py` on every text and background pair and on the colours that must be told apart (chart series, status colours, a card against its page), and for anything that fails, offer two or three fixes to choose from.
Then render the specimen at real viewing sizes (a phone, a desktop browser and each social format at feed size) and look at the result: fix layout bugs such as overflow directly, but for anything that needs a decision changed, such as a grid too faint to see, offer two or three fixes, because these problems only show up when rendered.
Check that motion respects reduced-motion settings and that the system still reads in grayscale.
Show the user how many choices are AI defaults or resemble one, so they can confirm each was deliberate, and check that the four outputs use exactly the same values.

## Output

Produce four outputs from the same decisions, so they never disagree: design tokens in the W3C Design Tokens format (2025.10), started from `assets/tokens.json`, including motion tokens; the DESIGN.md guide with principles, rules with their reasons, and the decision log; a specimen page built from `assets/specimen.html` showing every component in use with real copy, with motion running live; and a Claude Design System artifact where that type is available.
Write DESIGN.md so another person or AI tool can apply the system without this conversation, stating each rule with its reason, because a rule without a reason gets broken the first time it's inconvenient.
Where the medium needs ready-to-use files (for example CSS variables for a website or animation presets for video tools), generate them from the tokens rather than writing values by hand.
If the Claude Design System type isn't available, deliver the other three and say that the tokens file imports into design tools and code through token tools such as Tokens Studio or Style Dictionary.

## Close

End by running `progressive-skill-improvement` on this skill so lessons from the session improve the next run; if it isn't installed, suggest any improvements to this skill directly for the user to approve.
