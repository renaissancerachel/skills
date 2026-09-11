# FINDINGS — shared finding taxonomy

Agent-facing reference for the workspace-cleanup family. This is the **single store** for the
cross-cutting definitions every skill shares: the finding format, the fix-track labels, and the
severity scale. `workspace-audit` emits findings in this shape; each owner skill acts on the track
named here. Define these terms **here only**; elsewhere, gist the one track a skill uses and point
back to this file by name (sibling skills cannot link across skill folders once installed).

(This is agent reference, not the human-facing family overview. For that, see the plugin's
top-level `README.md`.)

## Five-field finding format

Every finding reports five things, so a human can verify without re-deriving and route without
re-reading:

1. **Signal** — the concrete evidence detected (a missing file, a size threshold crossed, a
   pointer that resolves to nothing, a duplicated fact, an asset with no second copy), with the
   path and the observed value.
2. **Severity** — impact if left unaddressed (see the scale below).
3. **Fix-track label** — exactly one of the three tracks below.
4. **Owner skill** — which sibling handles it: `doc-diet`, `config-bootstrap`, `asset-reconcile`,
   or `migration-plan`. (Some `propose-only` findings have no owner skill — they are flagged for a
   human directly.)
5. **Serves (goal)** — the plain-language end-state goal, from the project's `GOALS.md`, that
   acting on this finding advances (e.g. "backups you can trust", "a map of where things
   live"). One short phrase, in the user's terms. A finding that advances no stated goal is
   noise — say so and drop it rather than reporting it.

## Severity scale

- **HIGH** — real data-loss risk, or a decision made on stale information.
- **MEDIUM** — silent degradation or recurring toil.
- **LOW** — noise / cosmetic.

## Fix-track labels

Each label names how far a skill may go on its own before a human takes over:

- **`in-place-reversible-gated`** — a bounded edit a fix skill may make after one confirm, behind a
  reversible archive written and verified first.
- **`human-gated`** — a file move, rename, deletion, or version-control operation; a skill may only
  propose it, and a human executes.
- **`propose-only`** — advisory; no skill acts, a human decides (architecture, published outputs).

**One label per finding, default conservative.** Each finding carries exactly one fix-track label.
When two could apply, flag it and default to the more conservative track — `propose-only` over
`human-gated` over `in-place-reversible-gated`.
