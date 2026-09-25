# Reviewing a deep doc

Read after `../SKILL.md` (doctrine) and `../personal.md` (author bindings). This file carries the
gated review checklist and the anti-patterns the fresh reviewer hunts for.

## The rule that makes the rest real: gates leave evidence, not assertions

Every failure this review has ever had came from one move — writing "gate passed" instead of
running the gate. A verification step with no artifact collapses into a claim, and the claim is
always cheaper than the work.

- **A gate is done only when it has produced EVIDENCE** — a tool call, a skill invocation, a
  subagent result you actually received. Writing "voice check: done," "nothing fabricated," or "all
  five gates run" with nothing behind it **is a skip**. It is the skip that keeps happening, and a
  tidy changelog is where it hides.
- **Invoking the named tools MUST happen.** Where a gate names a skill or a search, running that
  skill or search *is* the gate. A read "against the rules in my head," a grep, or "I relied on what
  I know" is a **proxy, not the gate** — it does not count and must not be reported as if it did.
- **The review is not complete until the gate ledger is emitted** (bottom of this file), one line
  per gate, each carrying its evidence. Until then the doc is not "reviewed": do not say so to the
  author, in a commit message, or in `STATUS.md` / `CHANGELOG.md`. The status/commit line is written
  **from** the ledger, so it can never claim a gate the ledger cannot back.
- **Hold-for-sign-off is not the finish line.** It comes AFTER the ledger, not instead of it.
  "Waiting on your sign-off" with gates unrun is a premature stop dressed up as a handoff.

## Review checklist (ordered, gated)

Do your own reading and fixing first — structure, grounding, prose. Catch the obvious seams yourself
in gate 2 so the terminal cold read rarely has to force a big reorder. The fresh cold read is the
**last** gate on purpose: it validates the FINAL text, after every other edit is in.

1. **Source-fidelity [gate].** Every load-bearing claim traces to a source; **the author's material
   was re-mined THIS pass** — an actual read or extraction this pass, not "I remember it" — for both
   what the doc cites and what it *should* draw on but doesn't; **every external primary is
   fact-checked THIS pass with a live WebSearch**, exact IDs recorded (author/year + arXiv/DOI);
   nothing fabricated. *Gate: a claim with no trace, or an external ID not actually searched this
   pass, stops the pass.* **Evidence:** the re-mine (subagent id, or the files read this pass) and
   the list of IDs searched. (Full rule set: [`writing.md`](writing.md) source rubric.)

2. **Grounding, leveling & premise.** Every load-bearing noun grounded in-doc; mechanism depth
   reaches the ceiling set for this concept; every deferral explicit and pointed at a named sibling.
   A core term the stream planned to define (per the README's source/attribution map) but the body
   never defines is a gap, not an omission to wave through — this is a deep doc, it defines its terms.
   **Deliver on the premise, both directions:** first map *each* core question to the section that
   answers it, by name — a question with no home is a gap; then run the reverse pass — every section
   must earn its place against a core question or the premise, so flag anything extraneous (depth
   piling onto a side-topic, a passage that serves no question) for cut or relocation to a named
   sibling. **Precise terminology:** name each load-bearing concept with its exact term on first use,
   reuse that term, and revisit prior-lesson terms by name. **Lands on "Why it matters":** the
   explanation closes with the standard Why-it-matters beat — one human-level takeaway that gathers
   the doc's threads; a doc that trails off on a deferral or a pointer has under-landed. Every "thing
   people miss" is delivered in a section or that close, never stranded or duplicated in the
   misconceptions sidebar. **Evidence:** the question→section map and the list of extraneous flags.

3. **Voice + Claudism.** **Invoking MUST happen.** First load the author's voice-lessons ledger (see
   `../personal.md`) and apply its accumulated rules. Then **run the author's voice tools by invoking
   the skills named in `../personal.md`** (`voice-enforcement` and `loe-writing-review`) on the
   current text — a manual em-dash / "not"-language sweep is a proxy, not this gate. Three filters
   run before hunting vocab and punctuation:
   - **Every clause earns its place.** Read sentence by sentence; cut any clause that only restates
     what the sentence already said (a tail like "continuous with everything before it"). A dead
     clause built from clean words is still dead — this catches what a vocab sweep misses, so it
     runs first.
   - **The doc speaks in the author's first-person voice.** The author is never named in the third
     person in the body ("Rachel," "her book," "her glossary"), and no source is attributed inline.
     Verbatim-eligible lines are the author's own words, marked only in the Sources list (see
     `../personal.md`).
   - **Metaphors and comparatives are established before use.** If a section leans on a figure
     ("fill in the blank"), the body names it before building on it; never write "the modern /
     newer version" unless an older one was actually established.
   Then the Claudism pass: strip "it's worth noting," "worth naming," "deserves naming,"
   reflective-hedge openers, mood-softeners, packaged-summary last sentences, and any self-cite
   scaffolding beyond genuine verbatim. **Evidence:** the two skill invocations and the fixes applied.

4. **Governance.** Never-cite parents intact (when applicable); self-quotes substrate-appropriate;
   attribution asymmetry correct. **Evidence:** the checks run.

5. **Final fresh-subagent cold read [terminal gate — blocking].** After every other gate's edits are
   in, spawn a subagent that **did not write it** to read the FINAL text cold **against the leveling
   test** and return a seam list: do the beats connect, does the arc build, does the title's promise
   land, is any thread dropped or picked up cold, does difficulty spike out of place. **Read
   referents cold, not from whole-doc memory.** The failure mode is a reviewer who holds the entire
   doc, hits a back-reference, silently supplies the antecedent from ten paragraphs up, and rates the
   flow "clean." Defeat it: **every section must stand on its own.** Read each section as if it were
   the first thing the reader saw, and check each paragraph against only the section it sits in.
   Flag, even if you personally remember what it means:
   - any pointer to another section of the same doc, by name ("the models from 'What generative AI
     changed'," "described in 'Patterns, not a memory'") or by position ("mentioned above," "more on
     that below," "as described earlier," "the rest of this doc");
   - any back-reference whose antecedent lives in a different section (a demonstrative like "that
     freeze," "those lists," "the same X," or "then," at a section opener). Across paragraphs
     within one section, a reference is fine only if the paragraph just before it supplies it.
   The fix is a short restating clause, never a re-taught section. Reusing a defined term by name,
   [[links]] to other docs, and the top-of-doc roadmap are fine.

   Because this read runs LAST, on the final text, **a reorder cannot strand it** — there is no later
   edit left to invalidate it. Two properties make this gate real:
   - **It is blocking.** Wait for the subagent's result to actually arrive in your context. Do not
     proceed on a launched-but-undelivered agent, and never fill in the seam list yourself under the
     fresh-reviewer banner. **A missing or dropped result is a failed gate — re-run it**, do not
     substitute your own read.
   - **It loops until clean.** If the read returns structural seams, fix them, re-run gate 3 (voice)
     on the changed spans, and re-run this read. The gate is done only when a *delivered* result
     comes back with its seams resolved.

   **Evidence:** the subagent's task id AND a line quoted verbatim from its returned result (that
   quote is the proof the result was received, not dropped or self-authored).

→ **Emit the gate ledger, then hold for the author's sign-off.** `draft → ready` is always theirs.

## Gate ledger (required output before handoff)

Emit this before presenting the doc as reviewed. Every line needs real evidence; a blank, or "done"
with nothing behind it, is a self-marked skip that stops the handoff.

```
Gate 1 source-fidelity : re-mine [subagent id / files read this pass]; external IDs searched [list]
Gate 2 premise         : question→section map [...]; extraneous flagged [...]
Gate 3 voice           : voice-enforcement [invoked ✓]; loe-writing-review [invoked ✓]; fixes [...]
Gate 4 governance      : [checks run]
Gate 5 final cold read : task [id]; delivered-result quote "[verbatim line]"; seams [resolved / none]
```

The `STATUS.md` / `CHANGELOG.md` / commit line is written **from** this ledger and may claim only
what the ledger backs. "Reviewed" means every line above carries evidence.

## Anti-patterns (the seams the fresh reviewer hunts for)

Each is a concrete thing to catch:

- **Asserted, not performed** — "gate passed," "nothing fabricated," "all five gates run" written
  without the tool call, skill invocation, or received subagent result behind it. The skip that
  hides inside a confident changelog.
- **Proxy for the gate** — a manual grep or in-head check standing in for the named voice skills;
  parametric recall ("I relied on what I know") standing in for a live fact-check. The proxy looks
  like the work and is not the work.
- **Fire-and-forget reviewer** — launching the cold read and proceeding without its delivered
  result, or authoring the seam list yourself under the fresh-reviewer banner. The result must land
  in context and be quoted.
- **False completion record** — a `STATUS.md`, `CHANGELOG.md`, or commit line claiming gates that
  did not run. The status line is generated from the ledger precisely so this cannot happen.
- **Deepening outward-only** — reaching for external primaries while skipping the author's material.
- **Silent deferral** — gesturing at an unnamed concept ("the other shape it can take") with no hook.
- **Dropped thread** — opening a door (e.g. "text or images") and never walking through it.
- **Difficulty spike mid-flow** — the most jargon-dense passage wedged where the reader is still
  assembling the basics.
- **Title promise undelivered** — the title names an arc the body buries.
- **Off-premise drift** — depth accumulates on a side-topic while the doc's core questions go
  underserved (e.g. image-generation mechanics crowding a doc about how training works).
- **Ungrounded load-bearing noun** — the piece leans on a word it never defines.
- **One story told as two** — two sections that are the same idea from two angles, never joined.
- **Section that leans on another section** — a pointer to another section ("mentioned above,"
  "described in 'X'," "more on that below") or a back-reference whose antecedent lives in a
  different section ("that freeze," "those lists"). A whole-doc reader supplies it silently; a
  reader who lands on that section cold hits a wall ("what freeze?"). Reorders and voice cuts are
  the usual causes. Every section stands on its own.
- **Planned-but-undefined term** — a concept the README's source map slated for a definition that
  the body leans on but never actually defines. A deep doc that skips its own planned definitions
  has under-delivered, even when the prose reads fine.
