#!/usr/bin/env python3
"""
lint_deck.py — check that a built .pptx still IS a template document: every
slide on a template layout, text in placeholders, colours and fonts from the
theme, nothing drawn by hand that the owner can't restyle globally.

  python3 lint_deck.py Deck.pptx
  python3 lint_deck.py Deck.pptx --template Template.potx   # also verify layouts/masters match
  python3 lint_deck.py Deck.pptx --allow-fonts "Cinzel,JetBrains Mono" --strict

Findings (E = error, W = warning; exit code 1 when any error, or any warning with --strict):
  E layout-foreign     slide uses a layout/master not in the template
  E rogue-colour       a slide shape carries an explicit sRGB colour (theme colours only)
  E rogue-font         a run names a typeface not in the theme (or --allow-fonts)
  W free-shape         a non-placeholder shape on a slide (text box / autoshape / table)
  W empty-placeholder  a placeholder left with no text (shows its prompt in edit view)
  W overflow           more text than the placeholder box plausibly holds (heuristic)
  W mixed-masters      slides drawn from more than one master (may be intentional)
  W no-notes           slide has no speaker notes (info only unless --notes)
  W prompt-text        a run still contains bracketed prompt text like [Title]

Needs: python-pptx.
"""
from __future__ import annotations
import math
import os
import re
import sys
import tempfile
import zipfile

NS = {"a": "http://schemas.openxmlformats.org/drawingml/2006/main",
      "p": "http://schemas.openxmlformats.org/presentationml/2006/main"}
POTX_CT = "application/vnd.openxmlformats-officedocument.presentationml.template.main+xml"
PPTX_CT = "application/vnd.openxmlformats-officedocument.presentationml.presentation.main+xml"
EMU_IN = 914400


def as_pptx(path):
    if not path.lower().endswith(".potx"):
        return path
    tmp = tempfile.mkdtemp(prefix="deck-")
    out = os.path.join(tmp, os.path.basename(path)[:-5] + ".pptx")
    with zipfile.ZipFile(path) as zin, zipfile.ZipFile(out, "w", zipfile.ZIP_DEFLATED) as zout:
        for item in zin.infolist():
            data = zin.read(item.filename)
            if item.filename == "[Content_Types].xml":
                data = data.replace(POTX_CT.encode(), PPTX_CT.encode())
            zout.writestr(item, data)
    return out


def master_name(m):
    try:
        from lxml import etree
        part = m.part.part_related_by(
            "http://schemas.openxmlformats.org/officeDocument/2006/relationships/theme")
        return etree.fromstring(part.blob).get("name") or m.name or ""
    except Exception:
        return m.name or ""


def theme_fonts(prs):
    fonts = set()
    from lxml import etree
    for m in prs.slide_masters:
        try:
            part = m.part.part_related_by(
                "http://schemas.openxmlformats.org/officeDocument/2006/relationships/theme")
            root = etree.fromstring(part.blob)
            for tag in ("majorFont", "minorFont"):
                el = root.find(f".//a:{tag}/a:latin", NS)
                if el is not None:
                    fonts.add(el.get("typeface"))
        except Exception:
            pass
    return fonts


def layout_fonts(prs):
    """Typefaces the template's own layouts/masters name explicitly (e.g. a wordmark
    face or a code face) — allowed on slides too."""
    fonts = set()
    for m in prs.slide_masters:
        for el in m._element.iter("{%s}latin" % NS["a"]):
            fonts.add(el.get("typeface"))
        for lay in m.slide_layouts:
            for el in lay._element.iter("{%s}latin" % NS["a"]):
                fonts.add(el.get("typeface"))
    fonts.discard(None)
    return fonts


def ph_kind(sh):
    return str(sh.placeholder_format.type).split(".")[-1].split(" ")[0].lower()


def default_size_pt(ph, layout):
    """Best-effort font size for a placeholder: the layout placeholder's first-level
    defRPr sz, else 18."""
    try:
        idx = ph.placeholder_format.idx
        for lph in layout.placeholders:
            if lph.placeholder_format.idx == idx:
                sz = lph._element.find(".//a:lstStyle/a:lvl1pPr/a:defRPr", NS)
                if sz is not None and sz.get("sz"):
                    return int(sz.get("sz")) / 100
                sz = lph._element.find(".//a:p/a:endParaRPr", NS)
                if sz is not None and sz.get("sz"):
                    return int(sz.get("sz")) / 100
    except Exception:
        pass
    return 18.0


def overflow_ratio(sh, layout):
    """Estimated lines needed / lines available. >1.15 = probable overflow."""
    if not sh.has_text_frame or sh.width == 0 or sh.height == 0:
        return 0.0
    tf = sh.text_frame
    text_paras = [p for p in tf.paragraphs]
    if not any(p.text.strip() for p in text_paras):
        return 0.0
    size = default_size_pt(sh, layout)
    for p in text_paras:
        for r in p.runs:
            if r.font.size:
                size = r.font.size.pt; break
    w_in = sh.width / EMU_IN - 0.2   # insets
    h_in = sh.height / EMU_IN - 0.1
    char_w_in = size * 0.5 / 72        # avg glyph ≈ 0.5 em
    line_h_in = size * 1.25 / 72
    chars_per_line = max(1, int(w_in / char_w_in))
    lines = sum(max(1, math.ceil(len(p.text) / chars_per_line)) for p in text_paras)
    avail = max(1, int(h_in / line_h_in))
    return lines / avail


PROMPT = re.compile(r"\[(?:Title|Body|Text|Eyebrow|Subtitle|Caption|Image|Picture|Quote|Name|Date)[^\]]*\]", re.I)


def lint(path, template=None, allow_fonts=(), want_notes=False):
    from pptx import Presentation
    prs = Presentation(as_pptx(path))
    E, W = [], []
    tfonts = theme_fonts(prs) | layout_fonts(prs) | set(allow_fonts)
    tmpl_layouts = None
    if template:
        tp = Presentation(as_pptx(template))
        tmpl_layouts = {(master_name(m), l.name) for m in tp.slide_masters for l in m.slide_layouts}
    masters_used = set()
    for n, slide in enumerate(prs.slides, 1):
        lay = slide.slide_layout
        mname = master_name(lay.slide_master)
        masters_used.add(mname)
        if tmpl_layouts is not None and (mname, lay.name) not in tmpl_layouts:
            E.append(("layout-foreign", n, f"'{lay.name}' on master '{mname}' is not in the template"))
        if want_notes and not (slide.has_notes_slide and slide.notes_slide.notes_text_frame.text.strip()):
            W.append(("no-notes", n, "no speaker notes"))
        lay_names = {lp.placeholder_format.idx: lp.name for lp in lay.placeholders}
        for sh in slide.shapes:
            if sh.is_placeholder:
                # report the layout's name for the slot, not python-pptx's clone name
                sh_name = lay_names.get(sh.placeholder_format.idx, sh.name)
                k = ph_kind(sh)
                if k in ("slide_number", "picture", "object"):
                    if k == "picture" and sh.shape_type is None:
                        pass
                    continue
                if sh.has_text_frame and not sh.text_frame.text.strip():
                    W.append(("empty-placeholder", n, f"'{sh_name}' is empty"))
                    continue
                r = overflow_ratio(sh, lay)
                if r > 1.15:
                    W.append(("overflow", n, f"'{sh_name}' needs ~{r:.1f}× its box (shorten or split the slide)"))
            else:
                kind = str(sh.shape_type).split(".")[-1].split(" ")[0] if sh.shape_type else "shape"
                if kind not in ("PICTURE",):
                    W.append(("free-shape", n, f"{kind.lower()} '{sh.name}' is not a placeholder — the owner can't restyle it from the master"))
            # explicit colours / fonts inside this shape's XML
            for el in sh._element.iter("{%s}srgbClr" % NS["a"]):
                parent = el.getparent()
                # a picture's own fill/effects are fine; text and shape fills are not
                E.append(("rogue-colour", n, f"'{sh.name}' sets #{el.get('val')} directly — use a theme colour"))
                break
            for el in sh._element.iter("{%s}latin" % NS["a"]):
                face = el.get("typeface")
                if face and face not in tfonts and not face.startswith("+"):
                    E.append(("rogue-font", n, f"'{sh.name}' names '{face}' — theme fonts are {sorted(tfonts)}"))
                    break
            if sh.has_text_frame and PROMPT.search(sh.text_frame.text or ""):
                W.append(("prompt-text", n, f"'{sh.name}' still contains prompt text"))
    if len(masters_used) > 1:
        W.append(("mixed-masters", 0, "slides use " + " · ".join(sorted(masters_used))))
    return E, W, len(prs.slides._sldIdLst)


def main(argv):
    if len(argv) < 2 or argv[1] in ("-h", "--help"):
        print(__doc__); return 0
    args = argv[1:]
    def opt(name):
        if name in args:
            i = args.index(name); v = args[i + 1]; del args[i:i + 2]; return v
    template = opt("--template"); fonts = opt("--allow-fonts")
    strict = "--strict" in args; notes = "--notes" in args
    args = [a for a in args if not a.startswith("--")]
    E, W, n = lint(args[0], template, [f.strip() for f in fonts.split(",")] if fonts else (), notes)
    print(f"# deck-check · {os.path.basename(args[0])} · {n} slides · {len(E)} errors · {len(W)} warnings\n")
    for tag, s, msg in E:
        print(f"- **E {tag}** · slide {s} · {msg}")
    for tag, s, msg in W:
        print(f"- W {tag} · slide {s or '—'} · {msg}")
    if not E and not W:
        print("Clean: every slide is on a template layout, text lives in placeholders, colours and fonts come from the theme.")
    return 1 if E or (strict and W) else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
