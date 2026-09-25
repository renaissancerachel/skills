# Reviewing a deep doc

Read after `../SKILL.md` (doctrine) and `../personal.md` (author bindings). This file carries the
gated review checklist and the anti-patterns the fresh reviewer hunts for.

## Review checklist (ordered, gated)

Structural problems first — don't polish prose a bridging fix is about to rework.

1. **Source-fidelity.** Every load-bearing claim traces to a source; **the author's material was
   re-mined this pass**; external primaries fact-checked at writing time with exact IDs; nothing
   fabricated. *Gate: a claim with no trace stops the pass.* (Full rule set:
   [`writing.md`](writing.md) source rubric.)
2. **Grounding, leveling & premise.** Every load-bearing noun grounded in-doc; mechanism depth
   reaches the ceiling set for this concept; every deferral explicit and pointed at a named sibling.
   A core term the stream planned to define (per the README's source/attribution map) but the body
   never defines is a gap, not an omission to wave through — this is a deep doc, it defines its terms.
   **Deliver on the premise, both directions:** first map *each* core question to the section that
   answers it, by name — a question with no home is a gap; then run the reverse pass — every section
   must earn its place against a core question or the premise, so flag anything extraneous (depth
   piling onto a side-topic, a passage that serves no question) for cut or relocation to a named
   sibling. **Precise terminology:** this is a deep doc, so name each load-bearing concept with its
   exact term on first use, reuse that term, and revisit prior-lesson terms by name.
3. **Fresh-subagent bridging review.** A subagent that didn't write it reads cold **against the
   leveling test** and returns a seam list: do the beats connect, does the arc build, does the
   title's promise land, is any thread dropped or picked up cold, does difficulty spike out of
   place. **Read referents cold, not from whole-doc memory.** The failure mode is a reviewer who
   holds the entire doc, hits a back-reference, silently supplies the antecedent from ten paragraphs
   up, and rates the flow "clean." Defeat it: check each section and paragraph *opener* in isolation
   — every back-reference (a demonstrative like "that freeze," "this shift," "those abilities," or
   "the same X") must resolve to something in the *immediately preceding* section. If its antecedent
   sits more than one section back, that is a stale referent — flag it, even if you personally
   remember what it means. **A reorder invalidates this pass:** moving sections breaks
   newly-adjacent transitions and strands back-references, so re-run this step on the *post-reorder*
   text, never on the pre-reorder snapshot. Address seams before step 4.
4. **Voice + Claudism.** First load the author's voice-lessons ledger (see `../personal.md`) and
   apply its accumulated rules. Then run the author's voice review. Three filters run before hunting
   vocab and punctuation:
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
   scaffolding beyond genuine verbatim.
5. **Governance.** Never-cite parents intact (when applicable); self-quotes substrate-appropriate;
   attribution asymmetry correct.

→ **Hold for the author's sign-off.** `draft → ready` is always theirs.

## Anti-patterns (the seams the fresh reviewer hunts for)

Each is a concrete thing to catch:

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
- **Stale referent** — a demonstrative or back-reference ("that freeze," "this shift," "those
  abilities") whose antecedent sits more than one section back. A whole-doc reader supplies it
  silently; a genuinely cold reader hits a wall ("what freeze?"). Reorders are the usual cause.
- **Planned-but-undefined term** — a concept the README's source map slated for a definition that
  the body leans on but never actually defines. A deep doc that skips its own planned definitions
  has under-delivered, even when the prose reads fine.
