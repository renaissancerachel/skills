---
name: deep-doc-authoring
description: Write, deepen, or review a Layer-1 deep doc (concept substrate). Invoked by hand.
disable-model-invocation: true
---

# deep-doc-authoring — write concept substrate, not a lesson

A deep doc is **substrate, not a lesson**: content, sources, and facts captured at maximal depth so
downstream outputs (a video, a post, a course) can be derived from it later. Governing principle:
**easy to simplify, hard to complexify** — capture the full depth now, because it can't be added
back once it's lost.

This skill is a **router**: this file carries the doctrine every task needs, then sends you to one
task file for the procedure. Read this file, then open the file for your task — not the others.

This skill is generic. Everything specific to one author — their source material, voice tooling,
verbatim rule, live-state docs — lives in `personal.md` beside this file. The task files refer to
"the author," "the author's material," "the author's voice review," and "the source maps";
`personal.md` binds those roles to real paths and tools.

## Step 1 — Personalize (check first, every invocation)

1. Look for `personal.md` in this skill folder. If it exists, load it; it binds every role-noun to
   this author's setup. Then go to Step 2.
2. **If it does not exist, build it before writing anything.** Open
   [`PERSONALIZE.template.md`](PERSONALIZE.template.md) and follow it to interview the author, then
   write their answers to `personal.md` and confirm it back. This is a one-time setup; after it, the
   skill is theirs.

## Step 2 — Core doctrine (read every task)

**Leveling test (the yardstick for every judgment call):** written for **someone who may be new to
the area but likes to go deep — and the concepts connect.** Ground every load-bearing term, order
the beats so each earns the next, carry full mechanism depth, and defer *out loud*. Fundamentals
serve beginners and experts alike — pros drill the basics; experts revisit foundations to reconnect
the base.

**Two layers:** Layer 1 = this substrate; Layer 2 = derived outputs that simplify DOWN. The
substrate over-marks provenance (verbatim self-quotes, `FIGURE (Layer 2)` notes) because those get
stripped on the way down.

**Two axes of depth — both required** (moving one and calling it done is the classic failure):
1. **Mechanism depth** — the real machinery a go-deep reader would want (how the thing works
   underneath). Often sourced to external primaries.
2. **Grounding + bridging depth** — define the load-bearing nouns, connect each beat to the next,
   deliver the arc the title promises. Completeness and coherence, not "dumbing down."

**Register:** expository and example-rich, in the author's voice, from the author's own material.
Reserve "you" for what genuinely applies to everyone; write false-familiar address ("you build a
model for that") in the third person instead.

## Step 3 — Pick your task

| Task | Open | Also |
|---|---|---|
| **Writing or deepening a doc** | [`references/writing.md`](references/writing.md) | If the topic has **no source map**, run [`references/brainstorm.md`](references/brainstorm.md) first, then return to `writing.md`. |
| **Reviewing a doc** | [`references/reviewing.md`](references/reviewing.md) | — |

The task files carry the source rubric, the workflow, the review checklist, and the anti-patterns.
Open only the one you need.
