# Sunrise Software — Company Website

Source for **https://sunrisesoftware.app/** — the company site of Petri Korhonen / Sunrise Software Oy.

The current site (design **V4.5**, "cabinet dark" editorial concept) is a **single self-contained static page**: `index.html` with inline CSS/JS, plus an `images/` folder. The only external dependency is Google Fonts. **There is no build step.**

## Structure

```
.
├── index.html          # the entire site (inline CSS + ~50 lines vanilla JS for the lightbox)
├── images/             # all site images (WebP primary + JPG/PNG fallback)
├── docs/
│   ├── SEED-v2.0.0.md   # authoritative design + content spec (read this before editing)
│   └── archive/         # superseded earlier concepts (history)
└── source-assets/      # original product screenshots (sources for the optimised images/)
```

## Local preview

No build needed. Use any static server; Wrangler mimics the Cloudflare Pages runtime most closely:

```bash
npx wrangler pages dev .
# or, simplest:
npx serve .
```

Then open the printed `http://localhost:...` URL.

## Deployment

Production is hosted on **Cloudflare Pages** with **Git integration**:

- **Push to `main` → automatic production deploy** to https://sunrisesoftware.app/
- Every other branch / pull request gets its own **preview URL** (`*.pages.dev`) — use these to review changes before merging.
- Rollbacks and build logs are available in the Cloudflare Pages dashboard.

Build settings in Cloudflare: **build command = (none)**, **output directory = `/`** (repo root).

Manual deploy (fallback, rarely needed):

```bash
npx wrangler pages deploy . --project-name=sunrisesoftware-site
```

## Editing

- `docs/SEED-v2.0.0.md` is the locked spec — colours, typography, section architecture, and content all live there. Read it before changing copy or layout.
- Known queued fix (from the SEED): SF3D year range should read **2006–2016** (not 2008–2016) in §04.

## Roadmap

A migration to **Vite + React 19** (same visual result, componentised) is planned but not started — see SEED §5 and §10. Until then the static `index.html` is the source of truth.

---
Sunrise Software Oy · Tampere, Finland · private repository
