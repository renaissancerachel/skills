---
description: One door for building presentations from a real PowerPoint template. Finds the project's DECK-SYSTEM.md (creating it via deck-setup when missing), then dispatches to deck-build or deck-check.
argument-hint: (optional) what the deck is about, or which folder holds the deck system
---

Run the `deck` skill in this plugin (`skills/deck/SKILL.md`) on this session. You are the router:
find the project's deck manifest, create it through `deck-setup` when it is missing, dispatch to
`deck-build` or `deck-check`, and show a built deck only after `deck-check` passes.

If $ARGUMENTS is given, treat it as the deck's subject or source document, or as the folder that
holds the manifest.
