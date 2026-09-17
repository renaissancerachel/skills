# Deck system (TEMPLATE)

The `deck` router reads the *project's* `DECK-SYSTEM.md`, not this template — this file is only
the starting shape. Copy it to the project, fill it in (or let `deck-setup` fill it from the
template file), and delete this paragraph. Keep it short: it is a manifest that points at the
template and the design system, not a copy of either.

## Template

- **File:** `path/to/Template.potx` — the only starting point for a new deck; every slide sits on
  one of its layouts.
- **Regenerate:** how the template is rebuilt, if it is generated (script + command), or "hand-made
  in PowerPoint; edits go in the master".
- **Fonts:** which faces the theme uses (major / minor) and any extras the layouts name (a wordmark
  face, a code face). Embedded in the template? yes / no.

## Design system

- **Source of truth:** path or URL of the design system (tokens, type, marks) this template mirrors,
  and the version it is pinned to. When the two disagree, the design system wins and the template
  gets rebuilt.
- **Rules the deck must keep:** the two or three non-negotiables (e.g. "theme colours only" ·
  "one accent per surface" · "sentence case").

## Masters

| Master | Use it for |
|---|---|
| (name as PowerPoint shows it) | when to pick this one |

## Layouts

<!-- paste the output of deck-setup's inventory_template.py here; regenerate when the template changes -->

| Layout | Placeholders (name · kind) |
|---|---|
| … | … |

## Conventions

- **Copy:** where the voice / prose rules live (pointer, not a copy). Sentence case? Max bullets
  per slide? Headline length?
- **Fixed slots:** placeholders every slide should fill (e.g. an epistemic label, a footer tag) and
  their allowed values.
- **Images:** where approved images live; what stays out (stock clichés, etc.).
- **Speaker notes:** required / optional.

## Build and check

- **Environment:** python with `python-pptx` (`pyyaml` for YAML outlines); LibreOffice + poppler
  for previews. Path to the venv if one exists.
- **Outline → deck:** `deck-build` (`scripts/build_deck.py outline.yaml`).
- **Check before handing over:** `deck-check` (`scripts/lint_deck.py Deck.pptx --template …`,
  then `scripts/preview.py`). Clean means zero errors and every warning
  accepted on purpose.
- **Outputs go to:** folder + naming pattern for finished decks and their outlines.

## Gotchas

- Anything a future builder would otherwise rediscover the hard way.
