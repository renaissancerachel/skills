---
name: asset-reconcile
description: Find durable, hard-to-regenerate assets that exist in only one location and reconcile them into a mirror/backup, verifying byte-for-byte. Reach for it to check whether assets are single-copy, before a cross-machine handoff, or before retiring or wiping a machine.
---

# asset-reconcile — get single-copy assets safely mirrored

Protect durable, hard-to-regenerate assets by making sure each canonical one has a byte-identical
twin in the mirror/backup. This skill owns the audit's single-copy-at-risk-asset finding. It works
in a **read-only inventory/propose phase first**; **copy-in is `human-gated`**, and **pruning is a
separate `human-gated` second confirmation** (the `human-gated` track: a file move, rename,
deletion, or version-control operation a skill may only propose while a human executes; the full
finding taxonomy is defined once in the `workspace-audit` skill's `references/findings.md`).
Originals are sacred — this skill never deletes or moves a source asset under any branch.

## Step 1 — Inventory the durable assets in scope

Scoped reads only, inside the target folder. Inventory the durable, reusable assets — the ones
that would need manual re-approval to regenerate (referenced media, canonical exports, covers,
reference clips). Skip regenerable/derivable artifacts by design; only durable assets are at risk.

## Step 2 — Classify referenced vs unreferenced

For each asset, determine whether the project actually loads it:

- **Referenced / canonical** — loaded by the project (named in its registry/config/source). These
  are the ones worth protecting.
- **Unreferenced** — present but not loaded (rejected alternates, auditions, leftovers).

## Step 3 — Check each for a byte-identical twin

For each asset, check the mirror/backup location for a byte-identical copy (compare by content
hash, not by name — a same-bytes file under a different name still counts as a twin). A canonical
asset with no byte-identical twin in the mirror is **single-copy at-risk**.

## Step 4 — Propose reconciliation as a human-gated checklist

Present a checklist that separates, visibly:

- **canonical at-risk assets to copy into the mirror** (the reconciliation action);
- **duplicates** (same bytes, other name) — already safe, no action;
- **unreferenced alternates** — listed apart, with no bundled action.

Copying is human-gated: on an explicit yes, copy each canonical at-risk asset into the mirror,
then re-hash the mirror copy and confirm it is byte-for-byte identical. Local originals are never
touched.

## Step 5 — Pruning is a separate, explicit second confirmation

Removing unreferenced alternates is **never** bundled into the copy-in. It is a distinct action a
human must ask for explicitly and confirm on its own — never a default, never a follow-on assumed
from Step 4. Even then, pruning removes only unreferenced, non-source copies; a source asset is
never deleted.

## Safety specific to this skill

Beyond the family boundaries (stated centrally in the plugin's top-level `README.md`): **copy-in and prune are two separate
human-gated confirmations** — never merge them. **Verify byte-for-byte after any copy.** **Never
delete or move an original / source asset** under any branch — this family's hardest rule is that
originals are sacred; local copies are always left untouched.

## Done when

Durable assets in scope were inventoried and classified referenced vs unreferenced; each canonical
asset was checked for a byte-identical mirror twin by content; single-copy at-risk canonical assets
were presented as a human-gated copy-in checklist with duplicates and unreferenced alternates
listed separately; any copy performed on the user's yes was re-verified byte-for-byte; pruning was
offered (if at all) only as a separate explicit second confirmation; and no original or source
asset was deleted or moved.
