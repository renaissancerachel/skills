# Writing / deepening a deep doc

Read after `../SKILL.md` (doctrine) and `../personal.md` (author bindings). If the topic has no
source map, run [`brainstorm.md`](brainstorm.md) first. This file carries the source rubric and the
writing workflow.

## Source rubric

- **Deepening starts at home.** A depth pass re-mines **the author's own material first**; reaching
  for external primaries is the second move, not the first. Re-mine on *every* pass, including
  deepening passes — not just the first draft.
- **Build or consult the source-navigation map** before writing (paths in `../personal.md`). A map
  is an agent-facing line-number index of a heavy source — jump to a passage instead of re-reading
  the whole thing. If a topic has a map, start there; if it doesn't, run
  [`brainstorm.md`](brainstorm.md), then build one.
- **External primaries only for what the author's material genuinely lacks.** Fact-check at writing
  time (web search), cite exact IDs (author/year, arXiv or DOI). Invent nothing; flag a genuine gap
  rather than pad.
- **Deliver the planned sources and definitions.** The stream README (and the doc's own Sources
  plan) may map specific concepts to intended sources — a definition to a named reference, a claim
  to a primary. Consult that map *while drafting* and pull each one in; a definition or source the
  plan slated that never lands in the body is a gap, not an option. This is a deep doc: it defines
  its core terms outright rather than assuming the reader holds them. If the plan names a source you
  choose to swap (e.g. a different public definition), that is fine — just deliver a definition, and
  record the source you used.
- **Attribution asymmetry:**
  - *The author's own work* → quote **verbatim** only when the exact wording is the asset (a
    signature line, a spoken moment a paraphrase would flatten, an already-public line, a canonical
    definition). Otherwise absorb and re-voice with no "she/he says" scaffolding — the substrate
    *is* their material, so running self-attribution is obnoxious, and naming the author in the
    third person in the body ("Rachel," "her book," "her glossary") breaks the first-person voice
    the doc is written in. Mark verbatim-eligible sources by
    the author's verbatim rule (see `../personal.md`) in the Sources list; no running inline
    citation. **Self-quotes are a substrate device — strip them when adapting down to Layer 2.**
  - *External primaries* → the reverse: don't quote them, re-voice the claim and cite (author, year).
- **First-person lines trace to the author's own material.** Any "I" line about what the author
  says, teaches, or has said ("I used to suggest…", "In earlier talks I've described…") needs a
  line reference to the author's own material. Never turn third-party or internal material into the
  author's first person, and never blend it into their words.
- **Verify provenance labels; don't inherit them.** A source map or registry can mislabel a saved
  third-party file as the author's own. Before treating a source as the author's voice, confirm the
  label (ask the author when unsure); every doc that uses a mislabeled source inherits the error.
- **An imported author line must fit the doc's terms.** When a verbatim or near-verbatim author line
  comes in, check its terms against the doc's own definitions (a book's loose "the system learned"
  can contradict a doc that defines "system" as model plus app). Re-voice the term, not the idea.
- **Perishable specifics go to the living layer.** Provider settings, durations, defaults, and which
  models support what change month to month. The body states the durable principle with its
  qualification ("on many models…"); the dated, sourced specifics live in the stream's living files.
- **Never-cite parents are situational, not standing.** Sometimes a topic has an internal parent
  that must never be cited (a licensed guide, a partner's deck) — re-voice, and trace every claim to
  a public primary. Note it when it applies; it isn't a permanent feature of every doc.

## Writing workflow

1. **Map-first.** Read the source map(s). Scope a bounded extraction subagent by line-range when
   pulling new material.
2. **Ground, then build.** Define each load-bearing noun in-doc before leaning on it. Order the
   beats so each earns the next; the opening functions as an on-ramp within the doc's own level.
   **Every section stands on its own:** never point to another section ("mentioned above," "more
   on that below," "described in 'X'"); when a term or example returns, restate what it is in a
   short clause. Terms reused by name and a top-of-doc roadmap are fine.
3. **Use the author's existing bridges.** Pull their analogies, orderings, and framings from their
   material. Author new connective tissue only where theirs has a real gap — and flag the gap.
4. **Defer out loud.** Deferring detail is fine; do it explicitly, with a hook, to a *named* sibling
   doc — never a silent gesture at an unnamed concept.
5. **Write for adaptation.** Keep the provenance and figure notes the substrate needs; know they'll
   be stripped downward.

When the draft is done, open [`reviewing.md`](reviewing.md).
