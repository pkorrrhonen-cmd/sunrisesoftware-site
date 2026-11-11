# adr.sws.017: the site answers for itself, with a 404 page and real icon files

| | |
|---|---|
| Status | accepted (Petri, 11.11.2026, round 1 of the status review: "Kaksi PR:ää, tekniset ensin") |
| Date | 2026-11-11 |
| Decided by | Petri Korhonen |
| Links | sws.site |

## Context

Measured from production on 11.11.2026: `/favicon.ico`, `/apple-touch-icon.png`,
`/site.webmanifest` and `/nonexistent-xyz.html` all answered `200 text/html` with 94 886
bytes, which is `index.html`. The repository had no `404.html`, so Cloudflare Pages served
the front page for every unknown address. Two things follow. A search engine reads those
addresses as soft 404s, which spends crawl budget on one page served many times. And anything
that asks for an icon by name, which is what Google Search, a browser's bookmark list and a
phone's home screen do, receives HTML instead of an image: the site has had no icon anywhere
outside a browser tab, because the only one it had was an inline SVG data URI in `<head>`
(SEED v3.0.0 section 5.2), and a data URI cannot be fetched.

Virustutka met the same fault and fixed it on its own side in ADR-0029 (every address returned
the same empty shell with status 200).

The SCC2 install icons already live in this repository under `/scc/` (adr.sws.016) and are
generated in the scc2 repository, so the pattern and the mark were both to hand.

## Decision

The site ships `404.html` at the root, styled in the page's own palette with system fonts so
it costs nothing to serve, carrying the sun mark, the error, one sentence and a button back
to the front page. Cloudflare Pages serves it with status 404 for every unknown address.

The icons a crawler, a browser and a phone ask for by name become real files at the root:
`favicon.ico` (16, 32 and 48 px), `icon-192.png`, `icon-512.png`, `icon-maskable-512.png`,
`apple-touch-icon.png` and `site.webmanifest`. They are drawn from the same sun mark that is
already the inline favicon, by `scripts/icons.py`, which is run by hand when the mark changes
and whose output is committed. The inline SVG data URI stays as the first `<link rel="icon">`,
because it is the sharpest thing a modern browser can use.

`_headers` caches the icons for a week and the manifest for a day, and declares the manifest's
content type. `scripts/check-site.mjs` fails when any of these files is missing.

## Consequences

An unknown address now costs a 404 and a small page instead of the whole front page, and the
site can be found with its icon. The manifest names no `display`, so the site does not offer
itself for installation; it exists for the icons.

The icon files are generated art committed to the repository, so a change to the mark is two
steps: edit `scripts/icons.py` and commit what it writes. `scripts/icons.py` needs Pillow,
which the machine has and CI does not; CI only checks that the files exist, so the generator
is never run in the gate and the site keeps its no-build-step rule (adr.sws.001).

Nothing on the page changed in the pull request that did this, so the footer date and
`BUILD_INFO.updated` stay at 2026-09-20. The icon links in `<head>` are a page change and wait
for the page round (adr.sws.018's PR B).
