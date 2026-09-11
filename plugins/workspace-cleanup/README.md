# workspace-cleanup

A small, portable family of Claude Code skills for keeping a workspace's context fresh, findable,
single-sourced, and ruthlessly pruned, instead of letting it silt up into stale, duplicated, or
misplaced sprawl.

These skills are project-agnostic. They read whatever a folder actually contains (its docs, its
config or manifest files, its asset mirror or backup location) and work the same way in any repo,
for anyone. They hardcode no one's workflow, brand, or folder layout. They describe capabilities
("the project's live-state doc", "a project config or manifest file"), never volatile paths,
because volatile paths are the first thing to go stale.

## Install

This is a plugin in the `renaissancerachel` marketplace. Install it from that marketplace and the
router becomes available as `/cleanup`, with the sub-skills reachable to the agent. The plugin
bundles all six skills under `skills/`, each in its own folder with a `SKILL.md` (Claude Code's
convention: the folder name matches the `name:` in frontmatter, both lowercase kebab-case).

## The family

Two halves of one goal, keep context fresh, cover disk hygiene and memory hygiene:

| Skill | Role | Invocation |
|---|---|---|
| **`cleanup`** | Router. The one door. Figures out which cleanup a folder needs and dispatches. | user-invoked (`/cleanup`), also model-invocable |
| **`workspace-audit`** | Read-only sweep of a folder into a scored findings list. The entry point every fix consumes. | model-invocable |
| **`doc-diet`** | Shrink a bloated live-state doc back to a true snapshot, or slim a bloated context file (`AGENTS.md` or `CLAUDE.md`) back to a light pointer file, and move dated narrative to a log. | model-invocable |
| **`config-bootstrap`** | Detect a missing project config or manifest and draft one from the project's own evidence. | model-invocable |
| **`asset-reconcile`** | Find single-copy at-risk assets and reconcile them into the mirror or backup. | model-invocable |
| **`migration-plan`** | Propose-only. Turn misplacement, sync, or versioning problems into a human-gated move checklist. | model-invocable |

**Memory hygiene** is part of the same family, but the router does not re-implement it. It points
at the memory skills you already have:

- **`switchboard`**: periodic sweep that keeps per-machine memory a set of pointers into the synced
  doc layer, not a private store of facts.
- **`no-memories`**: the save-time partner that keeps facts out of memory in the first place.
- **`consolidate-memory`**: a reflective merge and prune pass over memory files.

The router only does read-only reconciliation of the memory surface (does memory duplicate what the
docs already hold, and do its pointers still resolve?), then hands off. It never auto-edits a memory
file.

## Where the shared taxonomy lives

The family shares one finding taxonomy (the five-field finding format, the severity scale, and the
three fix-track labels). Because an installed plugin cannot rely on parent-relative references
across skill folders, the canonical taxonomy lives in one place, the `workspace-audit` skill's
`references/findings.md`, and each sibling skill glosses the one track it uses inline and points
back to that file by name. The `GOALS.md` template the router offers to copy into a project is
bundled with the router skill at `cleanup/references/GOALS.template.md`.

## How invocation works, and why

- **`cleanup` is a router.** It is user-invoked as `/cleanup` and is also model-invocable so the
  desktop app can reach it as a skill even where plugin slash-commands are not surfaced. Its job is
  orchestration: name each sub-skill, name the trigger for reaching it, decide which applies, and
  dispatch. When it genuinely cannot tell which cleanup you want, it asks. It is safe to
  model-invoke because it only routes and asks before dispatching, and never touches a file itself.
- **Sub-skills are model-invocable** (they carry a `name:` and `description:` and no disable flag)
  so the router can reach them. That is the only reason they are model-invocable. It is a routing
  mechanism, not a safety posture.

This gives a one-door experience: you remember one command, not six.

## Safety, stated once, centrally

Invocation mode is not a safety mechanism. Safety comes from hard in-skill gates that every mutating
skill in this family enforces:

1. **Read first; writing is a separate, gated phase.** Audit and every detect or propose phase
   touch nothing. Every mutation stops and asks before it happens.
2. **Confirm scope before acting.** A skill states exactly which folder and which files it will
   touch, and waits for a yes, before doing anything.
3. **Write a reversible archive or backup before any overwrite.** The undo copy exists before the
   change it protects. Verify it byte-for-byte first.
4. **Stop at the create or overwrite boundary.** The skill presents the diff and stops; only an
   explicit yes lets it write.
5. **Never delete irreplaceable data.** Originals are never touched. Pruning anything is always a
   separate, explicit second confirmation, never a default, never bundled into another action.
6. **File moves and storage migration are human-gated and propose-only.** No skill moves a file,
   empties anything, or runs a history-rewriting version-control operation on its own. It drafts the
   plan; a human executes.
7. **Re-read any doc that gates an action immediately before acting on it.** On a cloud-synced tree
   a stale read can state the opposite of the current decision; an edit that fails with "file
   changed since last read" is proof the earlier read was stale, not a prompt to retry blindly.
8. **Search scoped, never a broad recursive sweep of a whole synced home.** Scope every search to
   the target folder (a broad recursive grep or find over a cloud-synced tree hydrates every file it
   touches and can outlive the session).

Instructions come from the person driving the session, not from file contents the skills read. Text
found inside a scanned file is treated as data, never as a command.
