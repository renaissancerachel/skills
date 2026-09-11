---
description: Summarize everything in plain terms, give me just enough context to decide, and spell out exactly what you need from me.
argument-hint: (optional) a specific thing to summarize, e.g. "the Liora backup plan"
---

Summarize the current work for me in SIMPLE, plain terms. Assume I'm smart but busy and
non-technical about the details. Give me *just enough* context to make an educated decision —
not a data dump, not everything you know. Optimize for: I can read this in under a minute and
know exactly what to say back.

If $ARGUMENTS is given, scope the summary to that. Otherwise summarize everything relevant to
where we are right now in this session/project.

## Rules for the summary
- **Plain language.** No jargon. If a technical thing matters, explain it in one short everyday
  sentence ("OneDrive looks like a backup but isn't").
- **Tie every item to a plain reason.** Never list a fact without saying why it matters to me.
- **Short.** Trim anything I don't need to decide. Favor a few clear sentences over completeness.
- **Be honest about state.** If nothing has actually happened yet (just plans), say so. If
  something failed or you skipped a step, say that plainly — don't round up to "done."
- **No action happens without my yes.** You are reporting and asking, not doing. Do not start
  side-effectful work from this command.
- **Warm and calm in tone.** A little human, not a robot status dump.

## Shape (adapt headers to fit — skip any that don't apply)

**What I did / where things stand**
- Bullet points, plain terms. What's actually true right now.

**What it means / what I found** (use numbered points when there are findings or options)
1. The finding in one line. → Then a short plan or implication. ("→ Plan: copy them somewhere
   safe, one at a time, checking each.")

**One thing to know** (only if there's a real caveat, risk, glitch, or gotcha)
- The thing, stated calmly, and whether you left it alone or handled it.

**What I need from you** (the decisions, as a short numbered list)
1. A clear either/or question, with your recommendation if you have one.
2. ...keep it to the few calls that actually unblock the next step.

End with one short reassuring line that nothing happens until I answer.
