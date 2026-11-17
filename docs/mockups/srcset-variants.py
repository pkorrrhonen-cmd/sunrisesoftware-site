"""Smaller widths of the images the live checks of 15.11.2026 found served larger than shown (round AV.1).
Each variant is made from the largest file the site already has (or its 2x source), never enlarged, and
gets a new name, so nothing already cached changes:
  images/hometeam-<screen>-360.webp     from source-assets/HomeTeam <screen> mockup 2x.png
  images/reviewglass-mockup-820.webp    from images/reviewglass-mockup.webp (1640 px, the decided crop)
  images/reviewglass-mockup-1240.webp   from the same
  images/petri-cutout-640.webp          from images/petri-cutout.webp (798 px, the cut-out)
  media/rooms-en-poster-1280.jpg        from media/rooms-en-poster.jpg (1920 px; a video poster has no srcset)
  media/rooms-en-916-poster-720.jpg     from media/rooms-en-916-poster.jpg (1080 px)
usage: python docs/mockups/srcset-variants.py   (from the site root)
"""
import pathlib
from PIL import Image

root = pathlib.Path(".")


def resize(src, dst, width, fmt, **opts):
    im = Image.open(root / src)
    if width >= im.width:
        raise SystemExit(f"{src} is {im.width} px wide; {width} would not be smaller")
    out = im.resize((width, round(im.height * width / im.width)), Image.LANCZOS)
    if fmt == "JPEG":
        out = out.convert("RGB")
    out.save(root / dst, fmt, **opts)
    print(dst, out.size, (root / dst).stat().st_size)


for screen in ["today-child", "today-adult", "wallet", "scoreboard", "treasure"]:
    resize(f"source-assets/HomeTeam {screen} mockup 2x.png", f"images/hometeam-{screen}-360.webp", 360, "WEBP", quality=86, method=6)
for w in (820, 1240):
    resize("images/reviewglass-mockup.webp", f"images/reviewglass-mockup-{w}.webp", w, "WEBP", quality=86, method=6)
resize("images/petri-cutout.webp", "images/petri-cutout-640.webp", 640, "WEBP", quality=86, method=6)
resize("media/rooms-en-poster.jpg", "media/rooms-en-poster-1280.jpg", 1280, "JPEG", quality=84, optimize=True, progressive=True)
resize("media/rooms-en-916-poster.jpg", "media/rooms-en-916-poster-720.jpg", 720, "JPEG", quality=84, optimize=True, progressive=True)
