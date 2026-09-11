---
name: workspace-audit
description: Read-only audit of a project folder that emits a scored, routable findings list. Reach for it to survey a workspace before cleanup, on a health check, or when onboarding an unfamiliar folder.
---

# workspace-audit — read-only sweep of a workspace

Survey one folder and emit a **scored findings list**. This skill is **read-only**: it detects and
reports, and changes nothing. It is the entry point the other cleanup skills consume — every
finding names the sibling skill that owns the fix and the track that fix must run on.

## What each finding carries

Every finding reports five fields — **signal, severity, fix-track label, owner skill, and the
plain-language goal it serves** — so a human can verify without re-deriving and route without
re-reading. The format, the three fix-track
labels (and their gating meaning), and the HIGH/MEDIUM/LOW severity scale are defined once in
[references/findings.md](references/findings.md); emit every finding in that shape.

**One fix-track label per finding, default conservative.** Each finding carries exactly one
fix-track label. When two tracks could apply, flag it and default to the more conservative one —
`propose-only` over `human-gated` over `in-place-reversible-gated` (also stated in
[references/findings.md](references/findings.md)).

## Step 1 — Resolve scope and inventory, read-only

Confirm the target folder (default: current working directory). Take today's date from the harness,
never from a file's timestamp. Build a lightweight inventory with **scoped** search only — globs
and greps confined to this folder. Never run a broad recursive sweep over a whole cloud-synced
home: it hydrates every file it touches and can outlive the session. Identify, from what the folder
actually contains:

- the **live-state doc** (whatever plays that role here — e.g. a `STATUS.md`, a README "current
  state" section, a top-of-repo notes file),
- any **dated-narrative log** (e.g. a `CHANGELOG.md` or history file),
- **project config/manifest** files (e.g. `AGENTS.md`/`CLAUDE.md`, a `docs/` tree, a build or tool
  manifest, a settings file),
- **assets** the project depends on (referenced media, canonical exports, covers, voice/reference
  files) and any **mirror or backup location** they should also exist in,
- **regenerable/binary trees** (dependency dirs, caches, build output, downloaded tooling, scratch),
- the **version-control state** (is this folder under git; is a shared source-of-truth dir not),
- the **project's goals** (`GOALS.md`, or the goal frame the router passed in) — the end states
  this run serves, so each finding can name the one it advances.

Re-read any doc whose content will gate a finding immediately before you rely on it.

## Step 2 — Run the detectors

Check each finding family below. Report a finding only when its signal actually fires; a family
with nothing to report is a clean pass, not a finding. Detectors must **no-op gracefully** when the
thing they inspect does not exist yet (a brand-new folder with no renderer, no state file, no
assets is not a pile of findings — it is early).

**Staleness**
- Live-state doc's newest content is old relative to recent activity in the folder, OR it carries a
  "don't trust the dates / hand-corrected" style disclaimer (a stale-read hazard baked into the
  primary handoff surface). → severity per how load-bearing the doc is; `in-place-reversible-gated`;
  owner `doc-diet`.
- An item listed as "open" that the current live files show is already resolved (believed-open but
  actually closed). → LOW; `in-place-reversible-gated`; owner `doc-diet`.

**Doc bloat / dated-log drift**
- The live-state doc has grown into an append-only log its own purpose forbids: far larger than
  peer docs, nested "superseded" blocks, dated entries that belong in the history log. → HIGH if it
  has already caused a wrong decision, else MEDIUM; `in-place-reversible-gated`; owner `doc-diet`.

**Context-file bloat / pointer erosion**
- An always-loaded context file (e.g. `AGENTS.md` / `CLAUDE.md`, or whatever the agent loads every
  turn here) has drifted from a light **pointer** file into an accreting store: detail inlined that
  belongs behind a pointer, no-op lines the agent already obeys by default, duplicated facts, or
  volatile paths/code snippets that go stale. Every line here loads on *every* turn, so bloat is a
  standing token tax and a staleness hazard — the file should stay tiny and point to where the
  detail lives. → MEDIUM (HIGH if the bloat has already driven a wrong action);
  `in-place-reversible-gated`; owner `doc-diet`.

**Duplication / multiple sources of truth**
- The same fact is stated in two or more places that can drift apart (e.g. a value in both the
  live-state doc and the config, or repeated across docs). → MEDIUM; `in-place-reversible-gated`;
  owner `doc-diet`.

**Missing project config / manifest**
- The project is actively used but has no config/manifest, so tooling silently falls back to
  generic defaults instead of the project's real identity/settings. → MEDIUM (silent degradation);
  drafting a proposal is safe, but creating it in place is `human-gated`; owner `config-bootstrap`.

**Misplacement / sprawl**
- Regenerable or binary trees (dependency dirs, caches, build output, downloaded tooling, scratch,
  conflicted-copy files) living inside a synced or version-controlled tree where they cause churn or
  cross-machine breakage. → HIGH for active sync churn, else MEDIUM; `human-gated` (file moves);
  owner `migration-plan`.
- Fragile paths: very deep nesting near an OS path-length limit, spaces or typos in folder names,
  a stray folder whose name collides with a real one. → LOW; `human-gated`; owner `migration-plan`.

**Single-copy at-risk assets**
- A durable, reusable asset that would need manual re-approval to regenerate (a referenced media
  file, a canonical export, a cover, a reference clip) exists in only one location, with no
  byte-identical twin in the mirror/backup. Distinguish **referenced/canonical** assets (loaded by
  the project) from **unreferenced** ones (rejected alternates). → HIGH (real, irreversible loss
  risk); copy-in is `human-gated`, pruning is separately `human-gated`; owner `asset-reconcile`.

**Unversioned source of truth**
- A shared/important code or content dir that is the single source of truth but has no version
  control and lives only in a sync folder (single point of failure, no history). → HIGH;
  `human-gated` (version-control setup); owner `migration-plan`.

**Orphaned references**
- A reference (a link, a pointer, a label, a config key) that resolves to nothing — a target that
  was renamed, moved, or removed. Cross-check whether the referencing artifact is already
  published/shipped before recommending any edit. → MEDIUM if it blocks a rebuild, else LOW;
  editing a published-artifact source is `propose-only`, otherwise `in-place-reversible-gated`;
  owner `doc-diet` for doc pointers, else flagged for a human.

**Infrastructure fragility / SPOF**
- Several parts of the project depend on one shared external resource, or the project is pinned to
  one machine via hardcoded absolute paths. → MEDIUM; `propose-only` (architectural — name it, do
  not attempt to fix it); no owner skill.

## Step 3 — Score, order, and emit

Produce the findings list ordered by severity (HIGH → LOW). For each finding give its signal
(with evidence), severity, fix-track label, and owner skill. Name, in plain terms, the goal from
the project's `GOALS.md` that the finding serves; a finding that serves no stated goal is dropped
(or flagged as out-of-frame) rather than listed. Group the `human-gated` and
`propose-only` findings visibly apart from the `in-place-reversible-gated` ones so the reader can
see at a glance what a skill could fix after one confirm versus what only a human should touch.

If asked to save the report, write it to a scratch/review location the user names — never into the
audited folder's live docs, and never overwriting anything. Default is to report in the response.
A saved report **references paths rather than pasting full file bodies**, and **redacts any
secret or credential** surfaced during the scan (show that it exists and where, never its value).
Stamp the top of a saved report with a one-line provenance note, e.g. `Generated by
workspace-cleanup <date> — verify before use.`, taking `<date>` from the harness at run time,
never from a file's mtime.

## Done when

Every finding family in Step 2 has been checked against the resolved scope and either reported with
all five fields — including the goal it serves — or passed clean (a finding that serves no stated
goal is dropped as out-of-frame, not listed); the list is severity-ordered; and nothing in the
audited folder was created, edited, moved, or deleted. This skill only ever reports — the owner skills, each with its
own gates, perform any fix.
