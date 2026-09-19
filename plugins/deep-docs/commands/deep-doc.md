---
description: One door for authoring Layer-1 deep docs (concept substrate). Reads the doctrine, personalizes to the author on first run, then dispatches to writing, reviewing, or a no-map brainstorm.
argument-hint: (optional) the concept, the doc to write/review, or the folder that holds the deep docs
---

Run the `deep-doc-authoring` skill in this plugin (`skills/deep-doc-authoring/SKILL.md`) on this
session. You are the router: check for `personal.md` (interview to build it when missing), read the
core doctrine, then open the one task file for what the user wants — writing, reviewing, or (for a
topic with no source map) brainstorming first.

If $ARGUMENTS is given, treat it as the concept, the doc to write or review, or the folder that holds
the deep docs.
