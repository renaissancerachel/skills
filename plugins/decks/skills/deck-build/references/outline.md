# Outline format for `build_deck.py`

YAML (or JSON with the same keys). One file per deck; the user edits it and rebuilds.

```yaml
template: ../RR-Luminous-Course.potx      # relative to this file, or absolute
master: Luminous · Indigo · Light         # default master — full name or a unique substring
out: lesson-01.pptx                       # relative to this file; folders are created

defaults:                                 # applied on every slide whose layout has the slot
  Epistemic label: I know this

slides:
  - layout: Cover                         # layout name from DECK-SYSTEM.md (case-insensitive)
    Eyebrow: AI foundations · Free series
    Title: Stay the one who decides
    Subtitle: A short course on using AI tools without outsourcing your judgment.
    notes: Speaker notes. Plain text.

  - layout: Content
    Title: Three zones
    Body:                                 # a list = one bullet per item
      - Green — use freely
      - Yellow — use with a rule
      - {text: A sub-point, level: 1}     # indent level (0 = top)
    Epistemic label: I practice this      # overrides the default on this slide

  - layout: Definition
    Title: Internal technology
    Definition: |                         # a block string = paragraphs split on newlines
      The capacities you build inside yourself.
      **They compound.** Tools do not.

  - layout: Image right
    master: Luminous · Rose · Light       # per-slide master override
    Picture: images/owl.jpg               # relative to this file; goes into the picture slot
    Title: Seeing before deciding
    Body: One line under the image.

  - layout: Blank
    keep_empty: true                      # keep unfilled placeholders (default: remove them)
```

## Rules

- **Keys are placeholder names** as listed in `DECK-SYSTEM.md`. Matching ignores case, spaces,
  underscores and dashes (`left column` = `Left column` = `left_column`). `idx:N` also works
  when a template's placeholders are unnamed.
- **Unknown keys are errors.** The script lists the layout's real placeholder names; fix the
  outline.
- `layout`, `master`, `notes`, `keep_empty` are the only reserved keys.
- Text is plain. `**bold**` is the only inline styling; size, face and colour are inherited
  from the layout, always.
- Any string value ending in an image extension goes in as a picture; into a `picture` slot
  directly, into any other slot fitted inside its bounds.
- Unfilled placeholders are removed from that slide, so prompt text never survives.
- A `.pptx` can be the template too; its existing slides are dropped before building.
