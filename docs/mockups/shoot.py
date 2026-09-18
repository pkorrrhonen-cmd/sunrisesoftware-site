"""Headless screenshots for mockup work (Edge or Chrome, one throwaway profile per shot).

  python docs/mockups/shoot.py url  https://virustutka.app docs/mockups/shots/virustutka.png 1280 800
  python docs/mockups/shoot.py file docs/mockups/flow-1.html docs/mockups/flow-1-desktop.png 1440 7200 static=1
"""
from __future__ import annotations

import os
import shutil
import subprocess
import sys
import tempfile
import time
from pathlib import Path

BROWSERS = [
    r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe",
    r"C:\Program Files\Microsoft\Edge\Application\msedge.exe",
    r"C:\Program Files\Google\Chrome\Application\chrome.exe",
]


def browser() -> str:
    for b in BROWSERS + [shutil.which("msedge") or "", shutil.which("chrome") or ""]:
        if b and os.path.exists(b):
            return b
    raise SystemExit("no headless browser found")


def wait_for(png: Path, seconds: float = 45.0) -> bool:
    """Edge returns before the screenshot is written; wait until the file exists and stops growing."""
    deadline = time.time() + seconds
    last = -1
    while time.time() < deadline:
        if png.exists():
            size = png.stat().st_size
            if size > 0 and size == last:
                return True
            last = size
        time.sleep(0.5)
    return png.exists() and png.stat().st_size > 0


def shoot(target: str, png: Path, width: int, height: int, budget_ms: int = 9000) -> None:
    profile = tempfile.mkdtemp(prefix="shot-")
    cmd = [
        browser(), "--headless=new", f"--user-data-dir={profile}", "--disable-gpu",
        "--hide-scrollbars", "--no-first-run", "--no-default-browser-check",
        f"--window-size={width},{height}", f"--virtual-time-budget={budget_ms}",
        f"--screenshot={png.resolve()}", target,
    ]
    subprocess.run(cmd, check=False, capture_output=True, timeout=180)
    wait_for(png)
    shutil.rmtree(profile, ignore_errors=True)
    ok = png.exists() and png.stat().st_size > 20_000
    print(("ok   " if ok else "FAIL ") + f"{png} ({png.stat().st_size if png.exists() else 0} bytes)")


def main(argv: list[str]) -> None:
    kind, src, out = argv[0], argv[1], Path(argv[2])
    width = int(argv[3]) if len(argv) > 3 else 1440
    height = int(argv[4]) if len(argv) > 4 else 900
    query = argv[5] if len(argv) > 5 else ""
    if kind == "url":
        target = src
    else:
        target = Path(src).resolve().as_uri() + (f"?{query}" if query else "")
    out.parent.mkdir(parents=True, exist_ok=True)
    shoot(target, out, width, height)


if __name__ == "__main__":
    main(sys.argv[1:])
