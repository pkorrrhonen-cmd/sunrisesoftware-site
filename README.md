# Sunrise Software site

Source of **https://sunrisesoftware.app/**, the company site of Petri Korhonen / Sunrise
Software Oy. One self-contained static page (`index.html`, inline CSS and about fifty lines of
vanilla JS) plus `images/`. The only external dependency is Google Fonts. There is no build
step (adr.sws.001). Working practices are in `CLAUDE.md`; the design and content spec is the
SEED in `docs/`.

## Status

Page **V5** (the sunrise generation, SEED v3.0.0) is built in `index.html` on the branch
`claude/sw-website-modernization-8676dd` (18.9.2026) and passes `scripts/check-site.mjs`. It
replaces V4.5 (cabinet dark, April 2026) once the branch is merged; until then production still
serves V4.5. Design system, content index and assets: `docs/SEED-v3.0.0.md`, with every text in
`docs/design/copy-v3.md` and every image in `docs/design/apps-v3.md`. Machine-readable state and
the open items: `docs/BUILD_INFO.json`.

## Layout

```
index.html              the entire page (inline CSS + JS: the sky, reveals, plates, drawers, the chamber, the lightbox)
images/                 page images, WebP first with JPG or PNG fallback; og-cover.jpg
media/                  the MasterForge EQ capture clip and its poster
source-assets/          original product screenshots, the sources of images/
scripts/check-site.mjs  the check CI runs (no dependencies)
.github/workflows/      CI: node scripts/check-site.mjs on pull requests and main
CLAUDE.md               working practices for Claude Code sessions
docs/
  SEED-v3.0.0.md        the spec of V5: design system, content index, assets, technical
  design/               copy-v3.md (every text, decided), apps-v3.md (every image, decided), look brief
  mockups/              the mockup rounds (look, flow, type) with captures; flow-4.html is the reference
  CHANGELOG.md          what each session changed and why (newest first, Finnish)
  BUILD_INFO.json       state, sources checked, next items (the only open-items list)
  LESSONS.md            mistakes and the rule each one produced (Finnish)
  decisions/            one file per decision, Atlas record shape, ids adr.sws.NNN
  archive/              superseded concepts and SEEDs (v2.0.0, the v2.1.0 draft, concept-v3)
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

Sunrise Software Oy · Tampere, Finland · private repository
