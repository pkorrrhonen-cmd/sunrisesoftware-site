"""ReviewGlass's mockup: its own windows, drawn by its own code, over a staged screen.

Decided with Petri on 14.11.2026, round AE (adr.sws.021). The glass, its halo and the
finder exclude themselves from every capture (WDA_EXCLUDEFROMCAPTURE, ReviewGlass
adr.rg.025), so no screenshot can show them. Instead ReviewGlass's own SvelteKit pages
(glass, diffwin, dock, halo) run in Edge with `reviewglass/tauri-mock.js` standing in for
the Rust core, and every answer the core would give is staged:

  - the glass's frames are cut from a staged screen at 1:1 around a staged pointer and
    zoomed by the page's own canvas, as the core cuts them from the real screen;
  - the screen is two session panes whose text is written for the picture: a re-enactment
    of this site's session 6 (11.11.2026), the version guard that never fired, with the
    real diff of its fix, commit 2aef4d2 of this public repository (AE.2);
  - the diff window shows that commit's first hunk through ReviewGlass's own Diff view;
  - the windows use Windows's light theme (AE.4): in the dark theme ReviewGlass draws the
    latest edit's rows with light text on its yellow mark, measured #ececec on #fff1a8.

Nothing here is a capture of a real session, and no file outside this public repository's
history and ReviewGlass's public source goes into the picture.

Setup, once (outside this repository; RG_SRC defaults to %TEMP%/rg-mockup/src):

    python docs/mockups/reviewglass-mockup.py --setup
    # then, in its own terminal, the copy's dev server on 127.0.0.1:5179:
    cd %TEMP%/rg-mockup/src && node node_modules/vite/bin/vite.js dev

Run (writes to RG_WORK, default %TEMP%/rg-mockup/work; nothing is written in this repo):

    python docs/mockups/reviewglass-mockup.py

Environment: RG_REPO (the ReviewGlass checkout, default E:/projects/sunrisesoftware/reviewglass),
RG_SRC, RG_WORK. The copy is made from RG_REPO's origin/main; the image names that commit.
"""
import html, json, os, pathlib, shutil, subprocess, sys, tempfile, time

from PIL import Image
from playwright.sync_api import sync_playwright

HERE = pathlib.Path(__file__).resolve().parent
REPO = HERE.parent.parent
TMP = pathlib.Path(tempfile.gettempdir()) / "rg-mockup"
RG_REPO = pathlib.Path(os.environ.get("RG_REPO", "E:/projects/sunrisesoftware/reviewglass"))
RG_SRC = pathlib.Path(os.environ.get("RG_SRC", TMP / "src"))
WORK = pathlib.Path(os.environ.get("RG_WORK", TMP / "work"))
URL = "http://127.0.0.1:5179"
MOCK_JS = HERE / "reviewglass" / "tauri-mock.js"

DPR = 2
SCREEN = (1600, 900)  # CSS px of the staged screen
GLASS = (1060, 380)   # the glass window, its tab below the corner included
TAB = 26
DIFF = (500, GLASS[1] - TAB)
ZOOM = 2.0
FIX = "2aef4d2"       # this repo's commit whose first hunk is the edit on screen
POINT = "-const versionHit"  # the pointer sits on the edit's line that contains this text: the
                             # broken line, so the glass shows it, the fix's comments and the new
                             # pattern, and none of the self-test's version strings (round AG.4)

VITE_CONFIG = """// Written by docs/mockups/reviewglass-mockup.py (sunrisesoftware-site): the app's own
// config on another port, with the linked node_modules allowed. Not committed anywhere.
import { defineConfig } from "vite";
import { sveltekit } from "@sveltejs/kit/vite";
export default defineConfig(() => ({
  plugins: [sveltekit()],
  clearScreen: false,
  server: {
    port: 5179, strictPort: true, host: "127.0.0.1",
    fs: { allow: [".", %s] },
    watch: { ignored: ["**/src-tauri/**"] },
  },
}));
"""


def setup():
    """Export ReviewGlass's origin/main to RG_SRC and link its node_modules."""
    if REPO in RG_SRC.resolve().parents:
        sys.exit("RG_SRC must be outside this repository")
    if RG_SRC.exists():
        shutil.rmtree(RG_SRC, ignore_errors=True)
        subprocess.run(["cmd", "/c", "rmdir", str(RG_SRC / "node_modules")], capture_output=True)
        shutil.rmtree(RG_SRC, ignore_errors=True)
    RG_SRC.mkdir(parents=True)
    subprocess.run(["git", "-C", str(RG_REPO), "fetch", "-q", "origin"], check=True)
    archive = subprocess.run(["git", "-C", str(RG_REPO), "archive", "origin/main"],
                             check=True, capture_output=True).stdout
    subprocess.run(["tar", "-x", "-C", str(RG_SRC)], input=archive, check=True)
    subprocess.run(["cmd", "/c", "mklink", "/J", str(RG_SRC / "node_modules"),
                    str(RG_REPO / "node_modules")], check=True, capture_output=True)
    nm = json.dumps(str(RG_REPO / "node_modules").replace("\\", "/"))
    (RG_SRC / "vite.config.js").write_text(VITE_CONFIG % nm, encoding="utf-8")
    subprocess.run(["node", "node_modules/@sveltejs/kit/svelte-kit.js", "sync"], cwd=RG_SRC, check=True)
    head = subprocess.run(["git", "-C", str(RG_REPO), "rev-parse", "--short", "origin/main"],
                          check=True, capture_output=True, text=True).stdout.strip()
    (RG_SRC / "RG_COMMIT").write_text(head, encoding="utf-8")
    print(f"ReviewGlass origin/main {head} exported to {RG_SRC}; start its dev server next")


# ---- the staged screen --------------------------------------------------------------

def first_hunk():
    out = subprocess.run(["git", "-C", str(REPO), "show", FIX, "--", "scripts/check-site.mjs"],
                         check=True, capture_output=True, text=True, encoding="utf-8").stdout
    lines = out[out.index("diff --git"):].splitlines()
    starts = [i for i, l in enumerate(lines) if l.startswith("@@")]
    return "\n".join(lines[: starts[1]] if len(starts) > 1 else lines) + "\n"


def screen_html(hunk):
    body = [l for l in hunk.splitlines() if l[:1] in (" ", "+", "-") and not l.startswith(("+++", "---"))]
    def row(l):
        cls = {"+": "add", "-": "del"}.get(l[0], "ctx")
        return f'<span class="{cls}">{html.escape(l.replace(chr(8), ""))}</span>'
    diff = "".join(row(l) for l in body)
    return f"""<!doctype html>
<html><head><meta charset="utf-8"><title>staged screen</title>
<style>
  html,body{{margin:0;background:#1f1e1c}}
  body{{width:{SCREEN[0]}px;height:{SCREEN[1]}px;font:13px/1.5 "Segoe UI",system-ui,sans-serif;color:#d8d4cc;display:flex;gap:2px;overflow:hidden}}
  .pane{{flex:1;background:#262522;padding:18px 26px;box-sizing:border-box;overflow:hidden;position:relative;min-width:0;display:flex;flex-direction:column;justify-content:flex-end}}
  .pane.right{{flex:0 0 640px;background:#24231f}}
  .top{{position:absolute;top:18px;left:26px;right:26px;font-size:12px;color:#8f8a80;border-bottom:1px solid #34322d;padding-bottom:8px;display:flex;justify-content:space-between}}
  .you{{background:#33312c;border-radius:10px;padding:9px 13px;margin:6px 0 14px auto;max-width:76%;width:fit-content}}
  p{{margin:0 0 10px}}
  .tool{{font:12px/1.5 "Cascadia Mono",Consolas,monospace;color:#a7a196;margin:8px 0}}
  .tool b{{color:#d9cfae;font-weight:600}}
  pre{{font:11.5px/1.55 "Cascadia Mono",Consolas,monospace;background:#1c1b19;border:1px solid #34322d;border-radius:6px;padding:9px 12px;margin:6px 0 12px;white-space:pre;overflow:hidden}}
  .del{{color:#e08f7f;background:rgba(224,143,127,.08);display:block}}
  .add{{color:#9fcf8e;background:rgba(159,207,142,.08);display:block}}
  .ctx{{color:#8f8a80;display:block}}
  code{{font:12px "Cascadia Mono",Consolas,monospace;background:#1c1b19;padding:1px 4px;border-radius:3px;color:#e3d9b9}}
</style></head>
<body>
<div class="pane left">
  <div class="top"><span>sunrisesoftware-site · version guard</span><span>working</span></div>
  <div class="you">The version guard in check-site has never failed once. Can you find out why?</div>
  <p>I'll read the guard line by line instead of trusting the green runs.</p>
  <div class="tool"><b>Read</b> scripts/check-site.mjs</div>
  <p>Found it. The escapes in the pattern were eaten when it was written: <code>\\b</code> became a backspace character and <code>\\d</code> became the letter d. The pattern can match nothing, so every page has passed since 20 September.</p>
  <p>I'll restore the pattern and give it a self-test in the same file: strings it must catch and strings it must not.</p>
  <div class="tool"><b>Edit</b> scripts/check-site.mjs</div>
<pre>{diff}</pre>
  <div class="tool"><b>Bash</b> node scripts/check-site.mjs</div>
<pre><span class="ctx">check-site: ok</span></pre>
  <p>The guard fires now: a page with a version number fails the run. The lesson goes into LESSONS: a guard whose failure looks like success is not a guard.</p>
</div>
<div class="pane right">
  <div class="top"><span>reviewglass · main</span><span>waiting</span></div>
  <div class="you">Is the diff window still glued to the glass after a resize?</div>
  <p>Yes. It shares the glass's edge and follows its Moved and Resized events, so a resize carries it along.</p>
  <div class="tool"><b>Bash</b> cargo test --quiet</div>
<pre><span class="ctx">test result: ok. 171 passed; 0 failed</span></pre>
  <p>All tests pass. Nothing to commit.</p>
</div>
</body></html>
"""


# ---- the staged core ----------------------------------------------------------------

def staged(hunk, cursor):
    now_ms = int(time.time() * 1000)
    now = now_ms // 1000
    glass_state = {
        "visible": True, "zoom": ZOOM, "frozen": False, "lens": False, "halo": True,
        "ui_scale": 1, "pane_lock": True, "pane_fit": True, "pinned": False,
        "see_through": True, "see_through_pct": 45, "fit_max_pct": 60, "pane_width": 958,
        "build": "", "follow_log": False, "follow_log_path": None, "follow_log_since": None,
        "follow_log_lines": 0, "config": "loaded",
    }
    frame = {"locked": True, "title": "sunrisesoftware-site", "own_window": False,
             "covered_by": None, "in_app": True, "note": None}
    view = {
        "path": "C:/src/sunrisesoftware-site/scripts/check-site.mjs",
        "display_path": "scripts/check-site.mjs", "place": "sunrisesoftware-site/scripts",
        "aside": False, "repo_root": "C:/src/sunrisesoftware-site", "status": "changed",
        "baseline": "head", "unified": hunk, "added": 9, "removed": 1,
        "fresh": list(range(40, 49)), "fresh_from_previous": False, "at_ms": now_ms - 40_000,
        "session_id": "s-guard", "tool": "Edit", "reason": None,
    }
    saw = {"title": "version guard", "session_id": "s-guard", "name": "version guard", "live": True}
    follow = {"on": True, "active": True, "saw": saw, "reads": 12, "last_read_ms": now_ms - 2000,
              "unavailable": None}
    return {
        "glass": {"label": "glass", "state": glass_state, "frame": frame, "scheme": "light",
                  "cursor": {"x": cursor[0] * DPR, "y": cursor[1] * DPR}, "sourceUrl": "/mock-source.png"},
        "diffwin": {"label": "diffwin", "scheme": "light", "answers": {
            "follow_session_state": follow, "diffwin_attached": "right",
            "panel_diffs": {"views": [view], "sessions": [{"id": "s-guard", "name": "version guard", "live": True}],
                            "hook_installed": True, "unreadable": 0},
            "panel_worktree": None}},
        "dock": {"label": "dock", "scheme": "light", "answers": {
            "glass_state": {"visible": True, "frozen": False, "lens": False, "build": "", "hotkey_toggle": "Ctrl+Alt+G"},
            "dock_state": {"open": False, "corner": "bottom-right", "drawer_width": 560, "drawer_height": 420, "drawer_tab": "diff"},
            "panel_usage": {"quota": {
                "five_hour": {"used_percentage": 38, "resets_at": now + 2 * 3600 + 1200, "burn_per_hour": 9.5, "hours_to_limit": 6.5, "stale": False},
                "seven_day": {"used_percentage": 21, "resets_at": now + 4 * 86400, "burn_per_hour": None, "hours_to_limit": None, "stale": False},
                "absence": None, "source_session": None},
                "sessions": [], "collector_installed": True, "unreadable": 0, "mixed_basis": False},
            "follow_session_state": {"on": True, "active": False, "saw": None, "reads": 0, "last_read_ms": None, "unavailable": None}}},
        "halo": {"label": "halo", "scheme": "light"},
    }


def render(b, route, size, mock, out):
    pg = b.new_page(viewport={"width": size[0], "height": size[1]}, device_scale_factor=DPR,
                    color_scheme=mock.get("scheme", "light"))
    pg.add_init_script("window.__RG_MOCK__ = " + json.dumps(mock) + ";")
    pg.add_init_script(path=str(MOCK_JS))
    errors = []
    pg.on("pageerror", lambda e: errors.append(str(e)))
    pg.goto(f"{URL}/{route}", wait_until="networkidle")
    pg.wait_for_timeout(1500)
    pg.screenshot(path=str(out), omit_background=True)
    pg.close()
    if errors:
        sys.exit(f"{route}: {errors}")


def main():
    if "--setup" in sys.argv:
        return setup()
    if not (RG_SRC / "RG_COMMIT").exists():
        sys.exit("run --setup first, then start the copy's dev server")
    WORK.mkdir(parents=True, exist_ok=True)
    hunk = first_hunk()
    (WORK / "screen.html").write_text(screen_html(hunk), encoding="utf-8")

    with sync_playwright() as p:
        b = p.chromium.launch(channel="msedge")
        pg = b.new_page(viewport={"width": SCREEN[0], "height": SCREEN[1]}, device_scale_factor=DPR)
        pg.goto((WORK / "screen.html").as_uri())
        pg.wait_for_timeout(300)
        pg.screenshot(path=str(WORK / "screen.png"))
        # The pointer: on the line of the edit that contains POINT (RG_POINT overrides), so the
        # glass reads the story.
        point = os.environ.get("RG_POINT", POINT)
        box = pg.evaluate("""(point) => {
          const s = [...document.querySelectorAll('.left pre span')].find(e => e.textContent.includes(point));
          const r = s.getBoundingClientRect(); return {x: r.x, y: r.y, h: r.height};
        }""", point)
        pg.close()
        # The picture starts at the pane's text: half the picture's source width past x 30.
        cursor = (int(30 + (GLASS[0] - 6) / ZOOM / 2), int(box["y"] + box["h"] / 2))
        (RG_SRC / "static").mkdir(exist_ok=True)
        shutil.copy(WORK / "screen.png", RG_SRC / "static" / "mock-source.png")

        s = staged(hunk, cursor)
        render(b, "glass", GLASS, s["glass"], WORK / "glass.png")
        render(b, "diffwin", DIFF, s["diffwin"], WORK / "diffwin.png")
        render(b, "dock", (420, 60), s["dock"], WORK / "dock.png")
        render(b, "halo", (90, 90), s["halo"], WORK / "halo.png")
        b.close()

    # As Windows lays them out: the glass where it was put at the top, the diff window
    # sharing its left edge, the halo centred on the pointer, the dock in its corner.
    desk = Image.open(WORK / "screen.png").convert("RGBA")
    def put(name, x, y):
        desk.alpha_composite(Image.open(WORK / name).convert("RGBA"), (int(x * DPR), int(y * DPR)))
    gx, gy = SCREEN[0] - GLASS[0] - 14, 36
    put("glass.png", gx, gy)
    put("diffwin.png", gx - DIFF[0], gy)
    put("halo.png", cursor[0] - 45, cursor[1] - 45)
    put("dock.png", SCREEN[0] - 420 - 10, SCREEN[1] - 60 - 6)
    desk.save(WORK / "desk.png")
    desk.convert("RGB").resize((1640, 922), Image.LANCZOS).save(WORK / "desk-1640.jpg", quality=90)
    commit = (RG_SRC / "RG_COMMIT").read_text(encoding="utf-8").strip()
    print(f"wrote {WORK / 'desk.png'} (ReviewGlass {commit}, pointer {cursor})")


if __name__ == "__main__":
    main()
