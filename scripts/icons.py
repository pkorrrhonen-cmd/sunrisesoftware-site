"""Site icons from the sun mark that is already the favicon's inline SVG.

Run by hand when the mark changes; the results are committed.

    python scripts/icons.py

Writes, at the site root so a crawler and a phone find them where they look:

    favicon.ico             16, 32 and 48 px, the zoomed mark
    icon-192.png            192 px, the mark edge to edge
    icon-512.png            512 px
    icon-maskable-512.png   512 px, the mark inside the central 80 % circle
    apple-touch-icon.png    180 px

The mark, in a 32 x 32 box (adr.sws.002's palette): paper background, a sun disc
centred at (16, 23) with radius 8 clipped to everything above the horizon at
y = 19, and the horizon drawn over it. Only the disc's top arc shows, which is the
sunrise the whole page is built on. Drawn at eight times the size and reduced, so
the edges are smooth without a rasteriser.

Needs Pillow, which the machine already has; no new dependency is added to the
site itself, which stays a static page with no build step.
"""

from pathlib import Path

from PIL import Image, ImageDraw

ROOT = Path(__file__).resolve().parent.parent

PAPER = (249, 247, 241, 255)   # --base  #F9F7F1
SUN = (232, 165, 78, 255)      # --sun   #E8A54E
HORIZON = (32, 48, 60, 128)    # --text  #20303C at 50 %

SS = 8  # supersampling factor


def draw_mark(size, zoom=1.0, radius=0.0, inset=0.0):
    """The mark on a square canvas of `size` px.

    zoom   scales the 32-box geometry about the horizon's midpoint (16, 19), so a
           16 px favicon still reads as a sunrise.
    radius corner radius as a fraction of the side (0 = square, for maskable and
           apple-touch icons, which the platform masks itself).
    inset  fraction of the side left empty around the mark, for the maskable icon
           whose content must sit inside the central 80 % circle.
    """
    n = size * SS
    img = Image.new("RGBA", (n, n), (0, 0, 0, 0))
    d = ImageDraw.Draw(img)

    if radius:
        d.rounded_rectangle([0, 0, n - 1, n - 1], radius=radius * n, fill=PAPER)
    else:
        d.rectangle([0, 0, n, n], fill=PAPER)

    # 32-box coordinates to pixels, zoomed about (16, 19) and inset.
    span = n * (1 - 2 * inset)
    k = span / 32 * zoom
    ox = n / 2 - 16 * k
    oy = n * (0.5 + inset * 0) - 19 * k  # keep the horizon on the middle line

    def px(x, y):
        return ox + x * k, oy + y * k

    # The sun, clipped to above the horizon: drawn on its own layer and cut.
    sun = Image.new("RGBA", (n, n), (0, 0, 0, 0))
    sd = ImageDraw.Draw(sun)
    cx, cy = px(16, 23)
    r = 8 * k
    sd.ellipse([cx - r, cy - r, cx + r, cy + r], fill=SUN)
    horizon_y = px(16, 19)[1]
    sd.rectangle([0, horizon_y, n, n], fill=(0, 0, 0, 0))
    img.alpha_composite(sun)

    # The horizon line over it.
    x1, y1 = px(5, 19)
    x2, _ = px(27, 19)
    w = max(1, round(1.5 * k))
    line = Image.new("RGBA", (n, n), (0, 0, 0, 0))
    ImageDraw.Draw(line).rectangle([x1, y1 - w / 2, x2, y1 + w / 2], fill=HORIZON)
    img.alpha_composite(line)

    # Keep the rounded corners transparent after the composites.
    if radius:
        mask = Image.new("L", (n, n), 0)
        ImageDraw.Draw(mask).rounded_rectangle(
            [0, 0, n - 1, n - 1], radius=radius * n, fill=255
        )
        img.putalpha(mask)

    return img.resize((size, size), Image.LANCZOS)


def flatten(img):
    """On paper, for formats that carry no alpha well on old platforms."""
    out = Image.new("RGB", img.size, PAPER[:3])
    out.paste(img, mask=img.split()[3])
    return out


def main():
    # The mark spans x = 5 to 27 of the 32-box, which is 69 % of the side. The
    # zooms below take it to about 85 % on the plain icons, and leave the
    # maskable one inside the central 80 % circle the platforms mask to.
    jobs = [
        ("icon-192.png", draw_mark(192, zoom=1.24)),
        ("icon-512.png", draw_mark(512, zoom=1.24)),
        ("icon-maskable-512.png", draw_mark(512, zoom=1.05)),
        ("apple-touch-icon.png", flatten(draw_mark(180, zoom=1.24))),
    ]
    for name, img in jobs:
        img.save(ROOT / name)
        print(f"wrote {name} ({img.size[0]} px)")

    ico = [draw_mark(s, zoom=1.45, radius=0.1875) for s in (48, 32, 16)]
    ico[0].save(ROOT / "favicon.ico", sizes=[(48, 48), (32, 32), (16, 16)])
    print("wrote favicon.ico (48, 32, 16 px)")


if __name__ == "__main__":
    main()
