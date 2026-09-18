# SUNRISESOFTWARE-SITE-SEED v3.0.0

**Project:** Sunrise Software, company website, the sunrise generation (page V5)
**URL:** https://sunrisesoftware.app/
**Owner:** Petri Korhonen / Sunrise Software Oy
**Created:** 2026-09-18
**Reference:** `docs/mockups/flow-4.html` (accepted by Petri 18.9.2026, adr.sws.013)
**Status:** Accepted as the spec, and built: `index.html` rewritten to it on 18.9.2026 (branch `claude/sw-website-modernization-8676dd`). Production serves V4.5 until the merge.

---

## 0. MAJOR VERSION NOTICE (v2.0.0 to v3.0.0)

A change of direction (adr.sws.010), so a major version. Between v2.0.0 (April 2026) and v3.0.0:

- **Palette replaced.** The cabinet-dark theme had become the default look of AI-made sites. v3 is warm paper and the sunrise over the sea, carried as atmosphere (the way Luviamo carries its birch forest), never as pictures.
- **Type replaced.** Fraunces (the ornate serif every LLM-made site carries) and Inter are out. Familjen Grotesk for display, Public Sans for body, JetBrains Mono kept for the archival labels (adr.sws.012). No italics anywhere; emphasis by colour.
- **Motion added on purpose.** A sky layer whose light follows the reader, a nav sun that rises with scroll, word reveals, parallax plates, drawers pulled out with the mouse, living product plates, a cryo chamber, a shore instead of a footer (adr.sws.011).
- **Content rewritten and re-decided item by item** (`docs/design/copy-v3.md`): the story now leads with people and the present, not with clinics and overclocking. Quaesitor leaves the page; Somnus and Atlas join the products as instruments. The cabinet is seven rows of real products. The SF3D history is a claim, a lead and a cryo chamber behind a button (adr.sws.003 closed by this).
- **Every image is the real product** (`docs/design/apps-v3.md`): a real EQ capture, the real intro video, real captures in the drawers, the Salpa brand mark, the portrait cut out of its studio backdrop. Drawn instruments only where the product has no public surface (Somnus, Atlas, ReviewGlass).
- **The page is dated.** Every status carries a version or a date; the footer carries the revision date and CI checks it (adr.sws.004).

What survives from v2.0.0: the numbered sections, first person singular, restraint (no hero statistics, no generic adjectives, no em dashes), the lightbox, the static single-file delivery (adr.sws.001, adr.sws.008), and the founder data.

---

## 1. VISION AND THE READER

### 1.1 Positioning

Software for people, built by someone who spent twenty years understanding them. The page is one morning: the first ray at the top, clear morning paper for the work, the open sea at the bottom. Its ideology stands in one line near the end: *Imagination is the limit. Build, then enjoy the world.*

### 1.2 The readers

1. **A serious buyer or collaborator**: reads the headline, §01 and the products, writes an email.
2. **A technical reader from an execution-focused event** (Since AI, Turku, 6 to 8 November 2026: working demos only). In ten seconds the page answers: what is shipped and live (dated statuses, links), is there code (GitHub in the nav and the meta row), how is the work done (§04's method block), and what the instruments behind it are (Somnus, Atlas).

### 1.3 Principles

- One glance and the understanding comes without reading: every product plate shows the product doing its thing.
- Nothing on the page that is not the real product, except a drawn instrument where the product has no public surface.
- Interactions are inviting and responsive: things grow as the pointer nears, previews park where the hand is, drawers pull.
- Dated, never relative: no "coming soon", "recently", "within the month".

---

## 2. PAGE ARCHITECTURE (V5)

```
/
├─ SKY (fixed layer)            dawn gradient + drifting orbs at the top; the reading light; the sea rising at the end
├─ NAV (fixed, blur on scroll)  Sunrise Software (sun mark rises with scroll) · Products · Approach · Contact · GitHub ↗
├─ HERO                         kicker · headline · lede · meta row (Founder, Location, Code, Latest release) · portrait cutout
├─ §01 The connection           title · intro · four disciplines
├─ §02 Products                 title · group "Commercial products": MasterForge, Luviamo
│                               · group "Tools and research instruments": Somnus, Atlas
├─ §03 Also in production       title · seven drawers: Virustutka, Ultra Gravel, TilastoSilta, SF3D AI Lab,
│                               ReviewGlass, Salpa Defence, SpectralForge
├─ Before the software · SF3D   claim · lead · button "Open the cryo chamber" · the chamber (unfolds)
├─ §04 Approach                 title · three rules · the creed · method (Build, Gate, Run, Record)
├─ §05 Correspondence           "Let's talk." · body · email · link list
└─ FOOTER (inside the shore)    company · Est. 2024 · Revised <date>
```

Every section is a `<section class="sec">` on `z-index:1` over the fixed sky. Section marks stay decorative and navigational.

---

## 3. VISUAL DESIGN SYSTEM

### 3.1 Palette A′ (adr.sws.010, exactly as in Flow 4)

```
PAPER
  --base        #F9F7F1   page paper
  --paper       #FFFDF9   cards, pills, lifted surfaces
  --paper-2     #F1ECE3   plates behind images, drawer images

TEXT (the sea, deep)
  --text        #20303C   primary
  --text-2      #50606C   body
  --text-meta   #8B96A0   labels, years, captions

RULES
  --rule        rgba(32,48,60,.10)
  --rule-strong rgba(32,48,60,.22)

SUN (one warm accent family)
  --sun         #E8A54E   the mark, live dots on dark, the hover glow, the nav sun
  --sun-deep    #C57A2C   emphasis in headlines and rules, links, section marks, buttons on paper
  --sun-soft    rgba(232,165,78,.16)

SEA (secondary, cool)
  --sea         #627F92   secondary accent, infra status dots
  --sea-mid     #3D5A6C   the shore's mid tone, html background below the page
  --sea-shore   #6F8FA3   the water at the shore
  --sea-deep    #243B4A   lightbox backdrop

LIGHT
  --glow        rgba(244,186,116,.42)   the hero light
  --live        #4E987C   live status dot
  --ember       #D96B3A   SF3D only (the section mark before the chamber)

CRYO (the chamber only)
  --cryo        #0B1520   --cryo-2 #122233   --ice #8FD8FF   --ice-dim #3E93BD   --frost #DFF3FF

DARK PLATES (MasterForge, Somnus, drawer captures on dark): #0F171F base, ice and sun accents.
SALPA (its own brand, the drawer only): Kuusi #0A1810 background, Messinki #C9A227 stamp.
```

### 3.2 Typography (adr.sws.012)

```
DISPLAY:  Familjen Grotesk 400 (500 for the wordmark), tracking -0.03em, no italics.
          h1 clamp(36px,5vw,66px) lh 1.02 · h2 clamp(28px,3.4vw,48px) lh 1.06 · h3 clamp(28px,3.2vw,42px) lh 1.02
          §01 items 18px · rules clamp(20px,2.3vw,28px) · the creed clamp(32px,4.6vw,60px), centred, max 22ch
          the email in §05 clamp(22px,2.6vw,30px)
BODY:     Public Sans 300 (paragraphs) / 400 / 500 (nav, buttons) / 600; 15 to 17px, lh 1.55
LABELS:   JetBrains Mono 400/500, 10 to 12px, tracking .12 to .2em, uppercase:
          section marks, group labels, kicker, meta row, status lines, spec strips, facts, years, captions, footer
EMPHASIS: colour only (--sun-deep); the coloured clause inside a heading or a rule is the emphasis.
Google Fonts: Familjen+Grotesk:wght@400;500;600, Public+Sans:wght@300;400;500;600, JetBrains+Mono:wght@400;500.
```

### 3.3 The sky and the light (motion system)

- **Sky layer** (`.sky`, fixed, z 0): a dawn gradient `#FBF4EA → #F7ECDD → rgba(232,234,232,.7) → --base`, three blurred orbs left of the portrait drifting on 24 to 38 s loops, all multiplied by `--dawn = clamp(0, 1 - p·2.2, 1)` where `p` is scroll progress. A sea overlay fades in over the last quarter: `--seao = clamp(0, (p - .74)/.26, 1)`.
- **The reading light**: a 1500×1100 warm ellipse (blur 44px, opacity `1 - dawn`) that eases toward the heading of the section nearest 42 % of the viewport. The mist parts and the sun lights what is read.
- **The cursor light** (fine pointers only): an 880 px warm radial that follows the pointer with lag in the hero, and switches off over the portrait column.
- **The nav sun**: a 22 px SVG; the disc sits below a horizon line and rises with `p` (translateY −11px at the bottom of the page) with a growing glow. On the shore the nav darkens (`.on-sea`).
- **Reveals**: `[data-reveal]` fades and rises 20 px; headings split into words that rise one by one (40 to 50 ms stagger); §01 items draw their top rule; rules draw their bottom line. The first screen never waits for the observer.
- **Parallax**: the portrait moves at 3 % of scroll; each plate's media at ±22 px around the viewport centre, scaled 1.06.
- **Reduced motion**: everything visible, nothing moves, videos do not autoplay (`.reduced`). Static capture mode (`?static=1`) does the same for screenshots.

### 3.4 Components

**Hero.** Grid 1.2fr / .8fr, min-height 88vh. Left: kicker, headline (the second clause coloured), lede, a four-cell meta row over a hairline. Right: the portrait cutout (`petri-cutout.webp`, 4:5, max 440 px), `object-fit: contain`, a soft warm radial glow behind the shoulders, the body fading into the paper at the bottom (the cutout's own alpha), caption under it in mono. No mask, no blend, no overlay (Petri: the whole person visible).

**Section head.** Mono section mark in `--sun-deep`, display title max 22ch, optional intro (Public Sans 300, 16.5px, max 52ch).

**§01 grid.** Four columns (two at 900 px, one at 520 px). Each item: a 2 px sun rule drawn on reveal, mono label, an 18 px display sentence with the coloured clause.

**Plate (§02).** Grid 1.05fr / .95fr, alternating sides (`.flip`). The frame: 16:10, radius 8, `--paper-2`, a long soft shadow, hover lifts the shadow and shows the pill. Inside: a canvas sketch and, for clip plates, a `<video>` over it that fades in on `canplay` and plays only in view (`.frame.clip`). Caption top-left in mono. Pill bottom-right: `Visit ↗` on paper, or the quiet `Access-protected` pill (Atlas). Beside it: status line (mono, a live or infra dot), h3 name, tagline in `--sun-deep`, body, spec strip (mono, three items, no technology names), button (dark pill, arrow slides on hover) or the quiet button.

**Group label (§02).** Mono, `--text-meta`, over a hairline, 44 px above the first plate of the group.

**Drawer (§03).** A row: year (mono) · name + mono status tag · one-line description · the plus. The row slides 12 px right on hover. The plus is a 48 px disc that scales from 0.62 to 1.4 as the pointer nears (within 320 px) and gets a paper disc and a shadow when near. On hover a 540 px preview parks at the row's right edge beside the plus (never follows the pointer), showing the product's real capture or its living canvas. Click opens the body (`grid-template-rows` 0fr → 1fr): paragraph, three facts, link, and one big image or canvas (16:9, max 820 px). One drawer open at a time.

**Cryo chamber.** Above it: the section mark in `--ember`, the claim (h2), the lead, and the button (a dark pill with a pulsing ice dot, `Open the cryo chamber`). The chamber unfolds below: `--cryo` gradient, ice hairlines, a fog canvas (drifting radial gradients), a top bar with the label and Close, the title, two paragraphs, three records (ice left rules), four readouts (Coolant, Lowest reading, HWBot Pro League, Principal sponsors), then a draggable strip of eight 4:3 photo cards in a cold treatment (desaturated, ice captions), each opening the lightbox.

**Approach.** Title, three rules (mono index left, display sentence with the coloured clause, a line drawn on reveal), the creed (centred, 200/400 weights, the second sentence coloured), then the method: four columns (Build, Gate, Run, Record) with mono labels and 14 px body.

**The shore (§05 and footer).** No box: a gradient from transparent through `rgba(111,143,163,.35)` and `--sea-shore` to `--sea-mid`, three animated glints and a sun path on the water above the text, 30vh of water before the content. Left: section mark in `#FFD79A`, title, body, the email. Right: the link list in two columns (name over address, hairlines). The footer line inside the shore: company · Est. 2024 · Revised date, mono. `html` background is `--sea-mid` so the page ends in the sea.

**Lightbox.** Dark cryo backdrop with blur, image max 86vh, mono caption, close on backdrop click or Escape.

**Strips.** Horizontal, scroll-snap, dragged with the mouse (pointer capture; a drag over 4 px suppresses the click).

### 3.5 The living plates and the drawn instruments (`docs/design/apps-v3.md`)

| Plate | Media | Fallback |
|---|---|---|
| MasterForge | `media/masterforge-eq.mp4` (the Pro Master EQ capture, 12.5 s, 3.4 MB, muted, loop, poster from the clip) | the meters-and-EQ canvas sketch |
| Luviamo | the intro video from luviamo.app with its poster; muted autoplay in view; click restarts with sound | the poster |
| Somnus | the rack panel canvas: two GPU load meters, a six-row live job list (AUDIO SEPARATION, RESEARCH FUNNEL, ATLAS COMPUTE, SALPA PROCESSOR, LOCAL INFERENCE, RESEARCH ENGINE), `LOCAL AI SERVER · ALWAYS ON · COST ≈ 0 €` | the same, static frame |
| Atlas | the workspace board canvas: Projects, Waiting on, Decided columns with cards sliding in, the partner's phone, the library shelf | the same, static frame |

Drawers: Virustutka (map capture, preview and drawer), Ultra Gravel (Petri's planned-loop captures), TilastoSilta and SF3D AI Lab (front-page captures), ReviewGlass (the interface mockup canvas: blurred columns, the reading frame, the glass), Salpa Defence (the horizontal brand mark on Kuusi; `ACCESS DENIED` stamp in Messinki on hover), SpectralForge (the UI screenshot).

---

## 4. CONTENT

The copy is decided item by item in **`docs/design/copy-v3.md`**, which is the source of every text on the page; this section indexes it.

| Part | What | Source items |
|---|---|---|
| Frame | title, meta description, nav, kicker, headline `Understand the human first. Then build the better product for them.`, lede `The world is open. Wherever better software is needed, from audio to public health, I build it.`, meta row (Founder · Location · Code · Latest release), portrait caption | 0.1 to 0.10 |
| §01 | `Four disciplines. One shared method.`, intro, four items | 1.1 to 1.11 |
| §02 | `Products people pay for, and the instruments behind them.`, groups, MasterForge, Luviamo, Somnus, Atlas | 2.1 to 2.34 |
| §03 | `More products, tools and instruments.`, seven rows | 3.1 to 3.39 |
| SF3D | claim, lead, button, chamber label, title, two paragraphs, records, readouts, captions | 4.1 to 4.11 |
| §04 | `How the work gets done.`, three rules, the creed, method | 5.1 to 5.11 |
| §05 and footer | `Let's talk.`, body, email, link list, footer | 6.1 to 6.8 |
| Shipped with the page | OG title and description | 7.1 to 7.2 |

Rules for copy: English, first person singular, no em dashes, no relative time, every status dated, no hero statistics, no generic adjectives, the company name only in the footer and the structured data, no employer's product names (adr.sws.006), no technology names in spec strips.

---

## 5. TECHNICAL

### 5.1 Stack

Static `index.html` with inline CSS and JS (about 600 lines of JS: reveals, the sky, the nav sun, plates, drawers, the chamber, strips, the lightbox, the sketches), `images/` and `media/`, Google Fonts. Cloudflare Pages with Git integration (adr.sws.001; the React migration is off the roadmap, adr.sws.008).

### 5.2 Assets shipped with the page

| Asset | Source | Page file |
|---|---|---|
| Portrait cutout | `images/Petri.jpg` (16.8.2026), cut out 18.9.2026 | `images/petri-cutout.webp` + `.png` fallback, two sizes (880 and 440 px wide) |
| MasterForge EQ clip | `masterforge/data/video creation/captures/eq/eq.mp4` | `media/masterforge-eq.mp4` (3.4 MB) + poster `media/masterforge-eq.jpg` |
| Luviamo video | streamed from `https://luviamo.app/media/luviamo-esittely-v2.mp4` | poster `images/luviamo-poster.jpg` |
| Drawer captures | `docs/mockups/shots/` | `images/shot-virustutka.webp`, `shot-ultragravel.webp`, `shot-ultragravel-preview.webp`, `shot-tilastosilta.webp`, `shot-sf3d.webp`, each with a JPG fallback |
| SpectralForge | `images/product-spectralforge.webp` (exists) | as is |
| Salpa mark | `salpa defence/docs/salpa-brand/logo/` | `images/salpa-defence-logo-horizontal-dark.svg` |
| SF3D photographs | `images/sf3d-*` (exist, all ten kept) | as is |
| OG image | generated: the headline on sunrise paper with the sun mark, 1200×630 | `images/og-cover.jpg` |
| Favicon | inline SVG data URI: a sun disc rising over a horizon line | in `<head>` |
| Removed | `images/product-quaesitor.*`, `images/product-masterforge.*` (replaced by the clip), `images/product-luviamo.*` (replaced by the poster) | git history keeps them |

### 5.3 Head, SEO, sharing

`<meta name="description">`, canonical, `theme-color #F9F7F1`, Open Graph and Twitter card, JSON-LD for **Organization and Person only** (Petri 18.9.), `robots.txt` (allow all; disallow `/docs/`, `/source-assets/`, `/scripts/`), `sitemap.xml` (one URL, lastmod = the revision date), `_headers` (nosniff, frame deny, referrer policy, permissions policy). Alt text on every image describes the screen.

### 5.4 Performance

Targets: Lighthouse 95+, LCP under 2 s, CLS under 0.05. The page weight: about 1.2 MB of images plus the 3.4 MB clip loaded only when its plate nears the viewport (`preload="metadata"`), fonts from Google. All images `loading="lazy"` except the portrait; WebP first with JPG fallback via `<picture>`. Canvas sketches run on one animation frame loop and skip off-screen canvases; the fallback timer keeps a hidden tab's first frame drawn.

### 5.5 Accessibility

Reduced motion honoured; every interactive element (drawer heads, the chamber button, pills, cards) is a button or a link with `aria-expanded` where it opens something; `:focus-visible` outline in `--sun`; the lightbox is a dialog closed by Escape; colour contrast of body text on paper 8.9:1, of `--sun-deep` on paper 3.6:1 (used at 17 px and above only).

### 5.6 Analytics

Cloudflare Web Analytics, once the token is fetched from the dashboard (open in BUILD_INFO).

### 5.7 CI

`scripts/check-site.mjs` on pull requests and `main`: local file references exist, required head elements, no em dashes in copy, forbidden strings (the employer's product names, `2008–2016`, "Launching within the month", "coming soon", "within the month", "recently"), footer `data-revised` equals `BUILD_INFO.updated`, the GitHub link appears at least four times.

---

## 6. FOUNDER DATA (authoritative)

```
Name:       Petri Korhonen
Role:       Founder, Sunrise Software Oy, Tampere, Finland, est. 2024
Email:      pete@sunrisesoftware.app
GitHub:     github.com/pkorrrhonen-cmd
Alias:      SF3D (extreme overclocking 2006 to 2016; SF3D AI Lab, sf3d.fi, 2026)
Day work:   digital health software to clinical and regulatory standards
```

---

## 7. DESIGN ITERATION LOG

| Version | Date | Key changes | Status |
|---|---|---|---|
| V4.5 | 2026-04-18 | cabinet dark, Fraunces, SF3D section (SEED v2.0.0) | published, superseded |
| Look 1 | 2026-09-17 | three sunrise palettes on one screen; A shifted toward C chosen (adr.sws.010) | done |
| Flow 1 | 2026-09-17 | elements, motion, flow; "exactly the right direction" (adr.sws.011) | done |
| Flow 2 | 2026-09-18 | Petri's answers applied: tighter, cutout portrait, reading light, parked previews, growing plus, lighter shore, cryo chamber, living plates; three fixes | done |
| Type 1 | 2026-09-18 | six pairs; Familjen Grotesk + Public Sans chosen (adr.sws.012) | done |
| Flow 3 | 2026-09-18 | the decided copy (copy-v3.md); two headings and the cryo text re-decided | done |
| Flow 4 | 2026-09-18 | the decided app views (apps-v3.md): real EQ clip, video, rack panel, workspace board, real captures, Salpa mark, ReviewGlass mockup | **accepted (adr.sws.013)** |
| **V5** | 2026-09-18 | `index.html` rewritten to Flow 4 with the page assets, together with Petri; check-site green | **built, awaiting commit and merge** |

---

## 8. NEXT STEPS

1. Rewrite `index.html` to Flow 4 together: the mockup's markup and code become the page, absolute media paths, the page assets of 5.2, head of 5.3, `data-revised` in the footer.
2. `node scripts/check-site.mjs` green; the Pages preview looked at on desktop and phone; Lighthouse.
3. Archive SEED v2.0.0 and v2.1.0; `BUILD_INFO.version` 5.0.0; CHANGELOG; commit and PR when Petri says.
4. Mirror to Atlas: `sw-sivusto.STATUS`, proposals for adr.sws.003 to 013.
5. GitHub profile filled in the same package; Cloudflare Web Analytics token.

---

## 9. DOCUMENT RULES

- Author name always "Petri Korhonen"; the company name only in the footer and the structured data.
- No em dashes in copy or documents; en dashes only in year ranges.
- Copy lives in `docs/design/copy-v3.md`, app views in `docs/design/apps-v3.md`; this SEED indexes them and holds the design system.
- The page is edited only together with Petri (CLAUDE.md); a change to the design system is a new SEED version.
