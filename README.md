# Sunrise Software site

Source of **https://sunrisesoftware.app/**, the company site of Petri Korhonen / Sunrise
Software Oy. Self-contained static pages (inline CSS and vanilla JS) plus `images/` and
`media/`. The only external dependency is Google Fonts. There is no build step (adr.sws.001).
Working practices are in `CLAUDE.md`; the design and content spec is the SEED in `docs/`.

## Status

The site is moving from V5 (one page, SEED v3.0.0, live since 18.9.2026) to **V6**, a front page
with its own pages (adr.sws.018). The spec is `docs/SEED-v4.1.0.md`, every new text is in
`docs/design/copy-v4-pages.md`, and the status round that led to it is
`docs/design/review-2026-11.md`.

- **The front page** carries the V6 changes since 12.11.2026 (PR #7): section 04 Recent, the
  HomeTeam drawer, the icon links and the structured data that names the products.
- **`/silent-context/`**, the first sub-page, is live since 13.11.2026 (PR #9): the Since AI 2026
  result with its vertical video, poster and share image.
- `/rooms/`, `/reviewglass/` and `/hometeam/` are specified and not built.

Machine-readable state and the open items: `docs/BUILD_INFO.json`.

## Layout

```
index.html              the front page (inline CSS + JS: the sky, reveals, plates, drawers, the chamber, the lightbox)
silent-context/         a sub-page: index.html with the front page's frame copied in (SEED 2.1); paths start from /
404.html                served for every unknown address (adr.sws.017)
favicon.ico             16, 32 and 48 px, and icon-192.png, icon-512.png, icon-maskable-512.png,
                        apple-touch-icon.png, site.webmanifest: the files a crawler, a browser and
                        a phone ask for by name, all drawn by scripts/icons.py
images/                 page images, WebP first with JPG or PNG fallback; og-cover.jpg and og-<page>.jpg
media/                  the clips and their posters
scc/                    the SCC2 install icons (adr.sws.016), not part of this site's navigation
source-assets/          original product screenshots, the sources of images/
scripts/check-site.mjs  the check CI runs over every page the sitemap names (no dependencies)
scripts/icons.py        draws the icon files from the sun mark; run by hand, output committed (needs Pillow)
.github/workflows/      CI: node scripts/check-site.mjs on pull requests and main
CLAUDE.md               working practices for Claude Code sessions
docs/
  SEED-v4.1.0.md        the spec of V6: the site's pages, design system, content index, assets, technical
  SEED-v3.0.0.md        the spec of V5, which is what production serves; archived when V6 goes live
  design/               copy-v3.md (every text, decided), apps-v3.md (every image, decided), look brief,
                        review-2026-11.md (the status round and its decisions),
                        decision-method.md (how lists are decided: four boxes a round, and why it works)
  mockups/              the mockup rounds (look, flow, type) with captures; flow-4.html is the reference;
                        og-<page>.html are the share images' sources, silent-context/ the sheets of rounds I and J
  CHANGELOG.md          what each session changed and why (newest first, Finnish)
  BUILD_INFO.json       state, sources checked, next items (the only open-items list)
  LESSONS.md            mistakes and the rule each one produced (Finnish)
  decisions/            one file per decision, Atlas record shape, ids adr.sws.NNN
  archive/              superseded concepts and SEEDs (v2.0.0, the v2.1.0 draft, v4.0.0, concept-v3)
  SESSION-CLOSE-*.md    thread close-outs: result, rounds, decisions, lessons, open items (Finnish)
```

## Develop

No build. Serve the folder with any static server; Wrangler mimics the Cloudflare Pages runtime
most closely.

```
npx wrangler pages dev .
```

```
npx serve .
```

Run the checks CI runs (add `--links` to also HEAD-check every external link; CI does not):

```
node scripts/check-site.mjs
```

## Deploy

Production is Cloudflare Pages with Git integration: a push to `main` deploys to
https://sunrisesoftware.app/ and every other branch or pull request gets a preview URL
(`*.pages.dev`). Build command none, output directory `/`. Rollbacks and build logs are in the
Pages dashboard. Manual fallback, rarely needed:

```
npx wrangler pages deploy . --project-name=sunrisesoftware-site
```

CI (`.github/workflows/ci.yml`) is a gate on pull requests and `main`; it does not deploy.

## Documents

- Before editing copy or layout, read SEED v3.0.0. Copy lives in `docs/design/copy-v3.md` and
  images in `docs/design/apps-v3.md`; the SEED indexes them and holds the design system.
- Every status on the page carries a date once adr.sws.004 is accepted; the footer revision
  date must equal `BUILD_INFO.updated` (CI checks).
- Atlas holds a mirror of this repo (`model/systems/sw-sivusto.model.json`, `sw-sivusto.STATUS`).
  The repo is the truth, the mirror follows through the proposals channel.

## Licence

No open-source licence is granted. The site's text, design and images are the property of Sunrise Software Oy and the people pictured; the repository is public so the work can be read, not reused.

---
Sunrise Software Oy · Tampere, Finland
