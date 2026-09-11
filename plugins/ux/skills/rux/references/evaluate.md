# RUX Evaluate - the scoring procedure

The default command. Score a page against `references/rubric.md` and hand back a report. Read `rubric.md` for the criteria and the math; read `references/voice.md` for how to phrase the output. This file is the procedure and the report templates.

## Before you score

1. Confirm context: audience, page type, primary goal (see SKILL.md Setup). Restate it in one line.
2. Confirm the target and that you actually inspected it. Fetch and screenshot the live page where you can; otherwise score what was pasted and mark unseeable criteria `N/A`.
3. Pick register (pro / friendly) and depth (quick / deep) from the request or the flags. Ask if unclear.

## Deep mode (default)

Score all 30 criteria 0-3 using the anchors in `rubric.md`. For each criterion, hold one plain observation of what you saw, then the score. The observation is what makes the score defensible and lets the user override it.

Then compute per-category `/9`, total `/90`, and the band.

Order the write-up by what helps the owner act: lead with the highest-scoring categories briefly (what is working), then the lowest-scoring criteria as priority fixes. A low score always comes with the specific observation and one concrete fix.

## Quick mode

Skip per-criterion scoring. Read each of the 10 categories, form a judgment, and report one line per category. Use the plain-language category names below so the read stays one-to-one with the engine. In friendly register, each category gets a traffic light; in pro register, each gets its `/9`.

### Plain-language category names (for friendly and quick modes)

| Rubric category | Plain-language name |
|---|---|
| I. Clarity & Visibility | Is it clear where you are and what to do? |
| II. Consistency & Standards | Does it behave the way people expect? |
| III. Feedback & Interaction | Does it respond when you click and type? |
| IV. Control & Flexibility | Can you undo, exit, and move freely? |
| V. Error Prevention & Recovery | Does it stop mistakes and help you fix them? |
| VI. Aesthetic & Purposeful Design | Is it clean and easy on the eye? |
| VII. Accessibility & Inclusivity | Can everyone use it? |
| VIII. Motivation & Emotional Design | Does it connect and earn trust? |
| IX. Learnability & Efficiency | Is it easy to learn and quick to use? |
| X. Relevance & Value | Is the content worth someone's time? |

## Traffic-light mapping

- **Criterion level (deep mode):** 0-1 = 🔴, 2 = 🟡, 3 = 🟢.
- **Category level (quick mode and category summaries):** roll the `/9` up: 7-9 = 🟢, 4-6 = 🟡, 0-3 = 🔴.

## Band-to-plain-language (friendly overall read)

| Total `/90` | Pro label | Friendly read |
|---|---|---|
| 80-90 | Excellent | In great shape. Keep it sharp and watch how it performs. |
| 65-79 | Good | Strong, with some quick wins waiting for you. |
| 50-64 | Fair | A solid base, with real fixes worth making next. |
| Below 50 | Poor | Ready for a fresh foundation, and now you know where to start. |

## Report template - Pro mode, deep

Use this structure.

```
# RUX Evaluation - [page]
Audience: [x] · Page type: [x] · Goal: [x]
Evaluated: [live page / screenshots / pasted copy], [date]

## Score: [total]/90 - [band]
[one-line read tied to the goal]

## By category
### I. Clarity & Visibility - [n]/9
- [criterion]: [0-3] - [one-line observation]
- [criterion]: [0-3] - [observation]
- [criterion]: [0-3] - [observation]
Source: Nielsen (Visibility of System Status), ISO 9241, Rams
[... repeat for II-X ...]

## Working well
- [highest-scoring points, brief]

## Priority fixes (lowest scores first)
1. [criterion, category] - [observation] - Fix: [concrete step]
2. ...

## Limits and next step
[pro-mode limits line from voice.md]
```

## Report template - Friendly mode

Plain language throughout. Traffic lights, not numbers. Voice rules from `voice.md` apply to every line. Findings stay honest; the framing stays in the owner's hands.

```
# Your website checkup - [page]
Looking at: [page], for [audience], built to [goal].

**Overall: [friendly read from the band table]**

Here is how it does, area by area:

🟢/🟡/🔴 **[plain category name]**
[one or two plain sentences: what is happening, and the choice they can make to improve it]
[... all ten categories ...]

**Your best quick wins**
- [the two or three lowest areas, each with one concrete, kind fix]

[evaluate disclaimer from voice.md]
[optional CTA {{researcher_offer}} from voice.md - omit entirely if unset]
```

## Filling the scorecard

When the user wants the structured artifact, fill `assets/RUX_scorecard.csv`: one row per criterion with the 0-3 score and a short comment (the observation). Hand it back as a file. In Claude Code, write it into the project; in chat, save and present it.

## Before/after benchmark

When the user is re-scoring after a redesign, keep the earlier scorecard and show the delta per category and on the `/90` total, so the improvement is visible. This is one of the framework's core uses.
