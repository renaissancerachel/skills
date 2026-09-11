# RUX Simulate - audience estimate

Estimate how the stated audience would likely react to the page. This is a labeled simulation grounded in common behavior patterns, never a stand-in for real user feedback. Read `references/voice.md` for phrasing.

## Before you simulate

Confirm audience, page type, and goal (SKILL.md Setup). The simulation is only as good as the audience definition, so if it is vague, sharpen it first. A "small business owner" reacts differently than "a time-pressed ops lead comparing three vendors." Push for the specific persona.

## Procedure

1. Build a short, concrete persona from the audience: their context, what brought them to the page, what they care about, what they are wary of.
2. Walk the page as that persona, first impression to primary action. Narrate the likely reactions at each step: what catches attention, what confuses, where trust rises or drops, where they hesitate or leave.
3. Tie reactions to the goal: would this persona do the one thing the page is for? Where does the path help or block them?
4. Surface the two or three moments most likely to make or break the visit.

Keep it grounded. Reactions should trace to something actually on the page, not invented drama. Flag where a real reaction genuinely depends on the person and only testing would settle it.

## Output

```
# Simulated audience reaction - [page]
Persona: [one or two lines - who they are, why they are here]

## First impression
[what they notice in the first seconds, and how it lands]

## Walking the page
[likely reactions along the path to the goal]

## Make-or-break moments
- [the few things most likely to convert or lose this persona]

## Would they act?
[honest read on whether they complete the goal, and what most stands in the way]

[simulate disclaimer from voice.md]
[optional CTA {{researcher_offer}} from voice.md - omit entirely if unset]
```

In pro register, drop the warmth and keep it as a research estimate. In friendly register, keep it plain and encouraging, and close with the optional CTA from `voice.md` when one is set.

## Honesty guardrail

A simulation feels authoritative and is easy to over-trust. Say plainly that it is a smart guess pointing toward what to test, and that the real visitors are the ones who confirm it. Do not dress a simulation up as data.
