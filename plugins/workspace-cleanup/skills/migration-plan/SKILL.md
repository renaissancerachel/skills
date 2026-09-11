---
name: migration-plan
description: Turn misplacement, fragile-path, and unversioned-source-of-truth findings into a human-executed, step-by-step move/version-control checklist — propose-only, moving nothing itself. Reach for it when regenerable or binary trees are syncing or under version control where they shouldn't be, when paths are fragile (deep nesting, spaces, collisions), or when an important directory has no version control.
---

# migration-plan — a human-executed move/versioning checklist

Turn placement and versioning problems into a plan a human can execute safely. This skill owns the
audit's misplacement/sprawl, fragile-path, and unversioned-source-of-truth findings. It is
**`human-gated` and `propose-only` throughout** (`human-gated`: a file move, rename, deletion, or
version-control operation a skill may only propose while a human executes; `propose-only`: advisory,
no skill acts and a human decides; the full finding taxonomy is defined once in the
`workspace-audit` skill's `references/findings.md`): it drafts the plan and never moves a file,
empties anything, or runs a history-rewriting version-control operation itself.

## Step 1 — Gather the misplacement, path, and versioning signals

Scoped reads only, inside the target folder. From the audit findings (or by detecting them here),
collect:

- **Misplacement / sprawl** — regenerable or binary trees (dependency dirs, caches, build output,
  downloaded tooling, scratch, conflicted-copy files) living inside a synced or version-controlled
  tree where they cause churn or cross-machine breakage. Size each tree.
- **Fragile paths** — very deep nesting near an OS path-length limit, spaces or typos in folder
  names, a name that collides with a real one.
- **Unversioned source of truth** — an important code or content directory that is the single
  source of truth but has no version control and lives only in a sync folder (a single point of
  failure with no history).

Re-read any doc whose rule gates a move (a storage-placement policy, for example) immediately
before you apply it — a cloud-synced read taken earlier may be stale.

## Step 2 — Draft the checklist

Turn the findings into an **ordered, human-executed checklist**. Each step is reversible and
independently verifiable. Frame any large move, or an unversioned-source-of-truth → version-control
cutover, as **expand → migrate → contract**: copy-new → verify → repoint → remove-old, never a
single risky move — so the old location survives until the new one is proven. Each step states:

- the exact before/after location for a move, or the exact version-control setup steps for an
  unversioned dir;
- how to verify the step succeeded before moving to the next;
- **why the step matters** — sync churn, cross-machine breakage, single point of failure — so the
  human can prioritize.

Group the steps so safe mechanical moves are visibly separate from moves that need care and from
any version-control cutover. Explain the destination rule you applied.

## Placement policy — one home per thing

Every move proposal answers to one rule: each file has exactly **one home, chosen by what the file
is**. One home per thing is what ends the scatter — the failure mode where copies land wherever is
convenient and the same thing spreads across several homes, so no copy is authoritative. This is the
concrete rule behind the project goal "the right home for each thing" (stated in the project's
own `GOALS.md`).

Route by type:

- **Version-worthy source** — code, and any content whose history matters → **version control**, one
  repo per real codebase.
- **Live docs and status edited across devices** → **the cross-device sync layer**, kept in sync so
  every machine sees the current copy.
- **Large regenerable artifacts** — renders, video, mockups, caches, build output, downloaded
  tooling, scratch → **out-of-sync local storage**, so they stop bloating the sync layer and
  churning across machines.

State the rule by category and let the project supply the specifics: which version-control host,
which sync service, which local path all come from the project's `GOALS.md` and setup. As everywhere
in this skill, applying the policy stays **propose-only** — you draft the placement plan into the
checklist, a human executes it.

## Step 3 — Present and stop

Present the checklist and STOP. A human executes each step and confirms it. This skill proposes;
it never executes.

## Safety specific to this skill

Beyond the family boundaries (stated centrally in the plugin's top-level `README.md`): this skill is **propose-only** — it **never
moves a file, empties or deletes anything, or runs a history-rewriting version-control operation**.
File moves and storage migration are a human-gated track; the plan is the deliverable, a human is
the executor. **Re-read any placement-governing doc immediately before applying its rule**
(stale-read rule).

## Done when

The misplacement, fragile-path, and unversioned-source-of-truth signals in scope were gathered;
each was turned into an ordered, reversible, independently verifiable checklist step with an exact
before/after location or exact version-control setup steps and a stated reason it matters; safe
moves, careful moves, and version-control cutover are grouped visibly apart; the checklist was
presented; and nothing was moved, emptied, deleted, or committed by this skill.
