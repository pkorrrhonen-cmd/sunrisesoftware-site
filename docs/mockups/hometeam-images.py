"""Turn the name-free 2x captures of hometeam-capture.py into the site's images (rounds Y and AD):
images/hometeam-*.webp and .png (720 px wide), source-assets/HomeTeam * mockup 2x.png, and the front
page drawer's 16:9 image images/shot-hometeam.webp and .jpg (the child's Today on --paper-2, AD.4).

usage: python docs/mockups/hometeam-images.py <shots-dir> <site-root>
"""
import sys, pathlib, shutil
from PIL import Image, ImageFilter

shots = pathlib.Path(sys.argv[1]); site = pathlib.Path(sys.argv[2])
img_dir = site / "images"; src_dir = site / "source-assets"

NAMES = {
    "ht-today-child": "hometeam-today-child",
    "ht-today-adult": "hometeam-today-adult",
    "ht-wallet": "hometeam-wallet",
    "ht-scoreboard": "hometeam-scoreboard",
    "ht-treasure": "hometeam-treasure",
}

for cap, name in NAMES.items():
    im = Image.open(shots / f"{cap}.png").convert("RGBA")
    # the page shows a phone at most 380 px wide; 2x of that is enough
    target_w = 720
    if im.width != target_w:
        im = im.resize((target_w, round(im.height * target_w / im.width)), Image.LANCZOS)
    im.save(img_dir / f"{name}.webp", "WEBP", quality=86, method=6)
    im.save(img_dir / f"{name}.png", "PNG", optimize=True)
    shutil.copyfile(shots / f"{cap}.png", src_dir / f"HomeTeam {name[9:]} mockup 2x.png")

# the front page's drawer: 16:9 at 2x of 820x461, the child's Today centred on the drawer's paper
W, H = 1640, 922
bg = Image.new("RGBA", (W, H), (241, 236, 227, 255))  # --paper-2
phone = Image.open(shots / "ht-today-child.png").convert("RGBA")
ph = 846
phone = phone.resize((round(phone.width * ph / phone.height), ph), Image.LANCZOS)
x, y = (W - phone.width) // 2, (H - ph) // 2 + 6
# a soft shadow under the phone, as the page's frames have
shadow = Image.new("RGBA", (W, H), (0, 0, 0, 0))
mask = phone.getchannel("A").point(lambda a: 70 if a > 128 else 0)
shadow.paste((32, 48, 60, 255), (x, y + 26), mask)
shadow = shadow.filter(ImageFilter.GaussianBlur(28))
bg = Image.alpha_composite(bg, shadow)
bg.alpha_composite(phone, (x, y))
rgb = bg.convert("RGB")
rgb.save(img_dir / "shot-hometeam.webp", "WEBP", quality=84, method=6)
rgb.save(img_dir / "shot-hometeam.jpg", "JPEG", quality=84, optimize=True, progressive=True)

for f in sorted(img_dir.glob("*hometeam*")):
    print(f.name, f.stat().st_size)
