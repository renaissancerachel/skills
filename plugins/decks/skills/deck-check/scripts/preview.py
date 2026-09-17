#!/usr/bin/env python3
"""
preview.py — render a .pptx/.potx to PNGs plus one contact sheet, for a visual
pass without opening PowerPoint. Uses LibreOffice (headless) → PDF → pdftoppm.

  python3 preview.py Deck.pptx                 # → Deck-previews/slide-NN.png + contact-sheet.png
  python3 preview.py Deck.pptx --out dir --dpi 96 --cols 4

Needs: LibreOffice (soffice on PATH or the macOS app), poppler's pdftoppm, and
Pillow for the contact sheet. LibreOffice substitutes fonts it can't find and
renders some gradients/alpha differently — treat these as a layout check, not
a colour proof. PowerPoint is the target renderer.
"""
from __future__ import annotations
import glob
import os
import shutil
import subprocess
import sys
import tempfile

SOFFICE = ["soffice", "/Applications/LibreOffice.app/Contents/MacOS/soffice",
           r"C:\Program Files\LibreOffice\program\soffice.exe"]


def find_soffice():
    for c in SOFFICE:
        p = shutil.which(c) or (c if os.path.exists(c) else None)
        if p:
            return p
    sys.exit("LibreOffice not found (install it, or add soffice to PATH).")


def render(path, out=None, dpi=72, cols=4):
    out = out or os.path.splitext(path)[0] + "-previews"
    os.makedirs(out, exist_ok=True)
    for f in glob.glob(os.path.join(out, "*.png")):
        os.remove(f)
    tmp = tempfile.mkdtemp(prefix="preview-")
    src = path
    if path.lower().endswith(".potx"):
        # LibreOffice opens .potx fine, but name the PDF after the deck
        src = os.path.join(tmp, os.path.basename(path)[:-5] + ".potx")
        shutil.copy(path, src)
    subprocess.run([find_soffice(), "--headless", "--convert-to", "pdf", "--outdir", tmp, src],
                   check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    pdf = glob.glob(os.path.join(tmp, "*.pdf"))[0]
    if not shutil.which("pdftoppm"):
        sys.exit("pdftoppm not found (brew install poppler).")
    subprocess.run(["pdftoppm", "-r", str(dpi), "-png", pdf, os.path.join(out, "slide")], check=True)
    # normalise names to slide-NN.png
    pngs = sorted(glob.glob(os.path.join(out, "slide-*.png")))
    for i, p in enumerate(pngs, 1):
        os.rename(p, os.path.join(out, f"slide-{i:02d}.png"))
    pngs = sorted(glob.glob(os.path.join(out, "slide-*.png")))
    try:
        from PIL import Image, ImageDraw
    except ImportError:
        print(f"Rendered {len(pngs)} slides → {out} (no contact sheet: pip install pillow)")
        return out
    ims = [Image.open(p) for p in pngs]
    if not ims:
        sys.exit("No pages rendered.")
    w, h = ims[0].size
    tw = max(1, int(w * (640 / w))); th = int(h * tw / w)
    gap, label = 12, 18
    rows = (len(ims) + cols - 1) // cols
    sheet = Image.new("RGB", (cols * tw + (cols + 1) * gap, rows * (th + label) + (rows + 1) * gap), "white")
    d = ImageDraw.Draw(sheet)
    for i, im in enumerate(ims):
        x = gap + (i % cols) * (tw + gap); y = gap + (i // cols) * (th + label + gap)
        sheet.paste(im.resize((tw, th)), (x, y))
        d.text((x, y + th + 3), f"{i + 1}", fill=(90, 90, 90))
    sheet.save(os.path.join(out, "contact-sheet.png"))
    print(f"Rendered {len(pngs)} slides → {out}/slide-NN.png + contact-sheet.png")
    return out


def main(argv):
    if len(argv) < 2 or argv[1] in ("-h", "--help"):
        print(__doc__); return 0
    args = argv[1:]
    def opt(name, default=None):
        if name in args:
            i = args.index(name); v = args[i + 1]; del args[i:i + 2]; return v
        return default
    out = opt("--out"); dpi = int(opt("--dpi", 72)); cols = int(opt("--cols", 4))
    render(args[0], out, dpi, cols)
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
