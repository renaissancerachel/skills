---
name: checkpoint
description: Get the session to a clean stopping point before the context window compacts, so the summary keeps what matters and in-flight work survives the squeeze. Captures the live working picture — the goal, decisions made and why, paths ruled out, the exact next action, and key file paths/IDs/values — into the thread itself (and reflects any finished units into the project's live-state doc). Reach for it when the user says "good stopping place to compact," "prep for compaction," "checkpoint before we compact," or when context is getting full mid-session. This is the mid-session sibling of catchup (cold resume) and handoff (end-of-work audit) — it replaces neither.
---

# checkpoint — brace the session for compaction

Compaction summarizes the thread lossily, and it can land mid-thought. The risk isn't finished
work (a close-of-work / handoff routine already flushes that) — it's the live picture that only
exists in this thread right now: the current plan, the decisions and *why* they were made, the
options already ruled out, and the exact next step. This skill lands the session at a clean
stopping point and writes that picture down where it will survive, so the post-compaction thread
resumes without re-deriving anything. Read-and-write to durable homes only; start no new
side-effectful work.

## Step 1 — Land somewhere safe
Stop at a clean boundary. No half-applied file edit, no command left mid-run, nothing in a state
that a summary could describe wrongly. If something is genuinely mid-flight and can't finish now,
park it cleanly and note *exactly* what was left incomplete and where.

## Step 2 — Write the checkpoint into the thread
This is the core: the thread is what compaction summarizes and what the post-compaction session
reads back, so the checkpoint lives here, not only in a file. Write it plainly and tightly:
- **Goal** — what we're actually trying to achieve this session, in one line.
- **Where we are** — what's done and what's in progress right now.
- **Decisions + why** — the calls already made, each with its one-line reason, so they don't get
  relitigated after the reset.
- **Ruled out** — paths/options already tried or rejected, so they aren't re-attempted.
- **Next action** — the single most important next step, concretely.
- **Open questions / waiting-on-Rachel** — anything blocking.
- **Keep these** — key file paths, IDs, values, and names that would be expensive to re-derive.
- **Don't lose** — explicit flags for anything easy to forget after compaction.
Summarize and cite paths; do **not** paste raw file contents in — that re-bloats the very context
you're trying to compact.

## Step 3 — Reflect finished units into their real home
If a unit of work actually completed, land it in the project's live-state doc (`STATUS.md` or
equivalent) and dated log per the usual close-of-work rule — reuse the homes that already exist,
don't invent a parallel store, and don't duplicate the in-flight reasoning from Step 2 into them
(that stays in the thread). Re-read any doc that gates the next action before relying on it, in
case the synced copy is stale. If there's no live-state doc, skip this step.

## Safety specific to this skill
- Reporting and parking only — do not kick off new side-effectful work while prepping to compact.
- Keep the checkpoint lean; a checkpoint fat with pasted file dumps defeats its purpose.
- Nothing here deletes or overwrites anything except appending/updating the normal state docs.

## Done when
The session sits at a clean boundary with nothing half-applied; the thread holds a lean, plain
checkpoint covering goal, current state, decisions-and-why, ruled-out paths, the single next
action, open questions, and the key paths/IDs to keep; any genuinely completed unit is reflected
in its existing live-state doc without duplicating in-flight reasoning; and the user has been told
it's a clean point to compact — with nothing depending on this skill having been run.
