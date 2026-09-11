---
description: Get the session to a clean stopping point before compaction — write the live working picture into the thread so it survives the summary, and reflect any finished work into its real home.
argument-hint: (optional) a note on what to emphasize, e.g. "focus on the render steps"
---

Brace this session for compaction. The context window is about to be summarized (lossily, maybe
mid-thought), so land at a clean stopping point and write down the live picture that only exists
in this thread right now. Reporting and parking only — start no new side-effectful work.

If $ARGUMENTS is given, weight the checkpoint toward that.

## Step 1 — Land somewhere safe
Stop at a clean boundary: no half-applied edit, no command mid-run, nothing a summary could
describe wrongly. If something can't finish now, park it and note exactly what's incomplete.

## Step 2 — Write the checkpoint into the thread
The thread is what compaction summarizes and what the reset session reads back, so put it here,
lean and plain:
- **Goal** — what we're trying to achieve this session (one line).
- **Where we are** — done vs in progress.
- **Decisions + why** — calls made, each with its reason, so they don't get relitigated.
- **Ruled out** — options already tried/rejected, so they aren't re-attempted.
- **Next action** — the single most important next step, concretely.
- **Open questions / waiting on you.**
- **Keep these** — key paths, IDs, values, names expensive to re-derive.
- **Don't lose** — anything easy to forget after the reset.
Summarize and cite paths; do NOT paste raw file contents (that re-bloats the context).

## Step 3 — Reflect finished units into their real home
If a unit actually completed, update the project's live-state doc (STATUS.md or equivalent) and
dated log as usual — reuse existing homes, don't invent a new store, don't duplicate the in-flight
reasoning from Step 2. Re-read any doc that gates the next action before relying on it. No
live-state doc → skip.

End by telling me it's a clean point to compact.
