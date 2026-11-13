"""Capture the five HomeTeam mockup screens at 2x (copy-v4-pages.md rounds Y and AD, adr.sws.020).

Never run it on the hometeam repository itself. First copy `hometeam/mockups/` and
`hometeam/apps/web/public/kuvat/` side by side into a folder OUTSIDE this public repository, then
edit the copy (Y.3, AD.2):
  - 011-comic-kuori.html: the child's greeting becomes the avatar's animal (`Hei, Kettu!`), the
    family-surname line above the adult's greeting is deleted, the three children's tiles and the
    `Vuorossa` line take their avatars' animals (Kettu, Pingviini, Pupu). `Hei, Petri!` stays.
  - 019-pistetaulu.html: the child's N2 tab list loses "Ruoka" (meals are not built; the module is
    off by default in production).
Check the copy for any real name before capturing. Only the name-free PNGs may enter the repository.

usage: python docs/mockups/hometeam-capture.py <copy>/mockups <out-dir> [probe]
needs: playwright (python) and Microsoft Edge
"""
import sys, time, pathlib
from playwright.sync_api import sync_playwright

src = pathlib.Path(sys.argv[1]).resolve()
out = pathlib.Path(sys.argv[2]).resolve(); out.mkdir(parents=True, exist_ok=True)
probe = len(sys.argv) > 3

TRANSPARENT = "html,body{background:transparent !important}"
# the mockups' own outer shadow bleeds into the corners of an element capture; the site draws its own
NOSHADOW = {"005-wallet.html": ".puhelin{box-shadow:none !important}"}
NOSHADOW_DEFAULT = ".puhelin{box-shadow:inset 0 0 0 2px #2b2b2b !important}"

# (name, file, selector index among .puhelin, clicks before capture)
TARGETS = [
    ("ht-today-child", "011-comic-kuori.html", 0, []),
    ("ht-today-adult", "011-comic-kuori.html", 1, []),
    ("ht-wallet", "005-wallet.html", 0, []),
    ("ht-scoreboard", "019-pistetaulu.html", 0, ["text=N2 Tänään-kortti"]),
    ("ht-treasure", "020-aarrearkku.html", 1, []),
]

with sync_playwright() as p:
    b = p.chromium.launch(channel="msedge")
    for name, f, idx, clicks in TARGETS:
        pg = b.new_page(viewport={"width": 1440, "height": 2400}, device_scale_factor=2)
        pg.goto((src / f).as_uri(), wait_until="networkidle")
        for c in clicks:
            try:
                pg.click(c, timeout=3000)
            except Exception as e:
                print("click failed", name, c, e)
        pg.evaluate("document.fonts.ready")
        time.sleep(3.0)
        phones = pg.locator(".puhelin")
        n = phones.count()
        el = phones.nth(idx)
        box = el.bounding_box()
        print(name, "phones", n, "box", {k: round(v) for k, v in box.items()})
        if probe:
            pg.screenshot(path=str(out / f"{name}-page.png"), full_page=False)
        pg.add_style_tag(content=TRANSPARENT + NOSHADOW.get(f, NOSHADOW_DEFAULT))
        el.screenshot(path=str(out / f"{name}.png"), omit_background=True)
        pg.close()
    b.close()
