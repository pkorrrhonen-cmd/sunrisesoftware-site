# SUNRISESOFTWARE-SITE-SEED v2.0.0

**Project:** Sunrise Software, Company Website Redesign
**URL:** https://sunrisesoftware.app/
**Owner:** Petri Korhonen / Sunrise Software Oy
**Created:** 2025-03-25
**Last modified:** 2026-04-18
**Status:** Design locked. V4.5 concept approved. Ready for Vite + React build.

---

## 0. MAJOR VERSION NOTICE (v1.1.0 → v2.0.0)

This is a major version bump. Between v1.1.0 and v2.0.0 the entire design direction changed. Key differences from previous SEEDs:

- **Typography system replaced.** Bebas Neue + Exo 2 (v1.1.0) was rejected as belonging to sports/agency aesthetic. Replaced with Fraunces (heritage serif with optical sizes and SOFT axis) + Inter + JetBrains Mono. Fraunces creates deliberate family resemblance to Luviamo.
- **Colour palette replaced.** Neon ember on deep midnight blue (v1.1.0) was too close to SaaS/Twitch dev aesthetic. Replaced with "cabinet dark" palette: warm black base, paper-warm text, brass as single warm accent, oxide blue-grey as technical accent, ember restricted to SF3D section only.
- **Page architecture replaced.** SaaS-style hero + flagship card + product grid (v1.1.0) replaced with editorial, numbered sections (§00-§06) in the style of a research monograph or museum catalogue.
- **Story angle locked.** "Real problems. Real software." (v1.1.0) replaced with a richer synthesis angle: a pattern-recognition practitioner who optimises every system he works with, combining psychophysical physiotherapy, optimisation/tuning, cybersecurity and health-tech development, and software engineering.
- **Trend-informed direction.** 2026 luxury branding research confirmed: the market is rejecting minimalist sans-serif "blanding" in favour of heritage serifs and quiet, craft-led identities. Luxury authority in 2026 is built through restraint and explained process, not feature proof.

v1.1.0 iterations V2 and V3 and the V3-revised concept are superseded.

---

## 1. VISION & PHILOSOPHY

### Core positioning
**The Observatory × The Atelier.** The site is the *cabinet of a scholar-builder*. It is not a studio, not a product page, but an office with instruments from different disciplines, with the connections between them visible. A visitor enters and, within the first ten seconds, understands: here is someone who connects things that are not normally connected, and that connecting is the whole point.

If Luviamo is a birch forest, Sunrise is a cabinet.

### Story angle (locked)
> *"Only a few people have spent twenty years listening to bodies and, at the same time, broken world records by pushing silicon into liquid nitrogen. The same person now builds software. It should not be a surprise that it is a little different."*

This is the narrative core, not the tagline. The tagline is distilled from it. But the idea runs through the entire site — not as repetition but as *structure*. The four disciplines surface in §01 as the method, and are demonstrated through work in §02-§04.

### Design principles
- **Substance before adjectives.** Products speak for themselves. No "innovative tools" generics.
- **Personality from angle, not ornament.** Petri's unique combination (physiotherapy + overclocking + cybersecurity + DSP) is the story.
- **The site itself is a portfolio piece.** Visual quality proves capability.
- **No proof-seeking.** No hero statistics. Confidence, not defence.
- **Not a dry corporate site, not an AI-slop exercise.** Something between: professional but personal.
- **First-person singular.** "I build what I need" rather than "We deliver solutions."

### Opening headline (locked, A1)
> *Twenty years in clinics. Two decades overclocking silicon. Now building software nobody else would think to build.*

Supporting meta: Petri Korhonen · Tampere, Finland · Sunrise Software Oy · Est. 2024.

---

## 2. PAGE ARCHITECTURE (V4.5, locked)

```
/
│
├─ NAV (fixed, blur on scroll)
│
├─ §00 Opening              (full-viewport typography, meta row, no photograph)
├─ §01 The connection       (four disciplines, paragraph intro + four labelled items)
├─ §02 Selected work        (MasterForge, Quaesitor, Luviamo — each with a cover image + body)
├─ §03 The rest of cabinet  (SpectralForge as featured entry with image, then archive table)
├─ §04 Archive · SF3D       (1 intro + portrait, 1 hero image, 2 ventures as text,
│                             4-image proof rail, 4-image bottom row)
├─ §05 Approach             (three rules, typographic)
├─ §06 Correspondence       (email, colophon)
│
└─ FOOTER
```

All sections are numbered § (section mark). The numbering is decorative (establishes archival/editorial tone) but also navigational.

---

## 3. VISUAL DESIGN SYSTEM (locked)

### 3.1 Typography

```
DISPLAY (section titles, product names, opening headline, quotes):
  Fraunces (variable: weight, opsz, SOFT)
  opsz 72-144 for large headlines, 24-48 for medium titles
  SOFT 20-30 for regular weight, SOFT 80-100 for italic
  weight 400 default, 500-600 only where needed

BODY:
  Inter (system fallbacks: system-ui, -apple-system, sans-serif)
  weight 300-400, size 15px, line-height 1.65

MONO (structural/archival: section marks, year labels, status codes, specs):
  JetBrains Mono (fallbacks: SF Mono, Menlo)
  weight 400-500, size 10-12px, letter-spacing 0.04-0.2em

Family resemblance to Luviamo: Fraunces is deliberate shared-family DNA. Luviamo
uses Bodoni Moda (logo) + Fraunces (display) + DM Sans (body); Sunrise uses
Fraunces (display) + Inter (body). Same heritage-serif voice, different
product-voice around it.
```

### 3.2 Palette (cabinet dark)

```
BASE:
  --base:         #0E1114   warm near-black, like ink pool
  --cabinet:      #1A2332   secondary card/section background
  --cabinet-2:    #141A24   tertiary

PAPER & TEXT:
  --paper:        #F4EFE6   warm off-white (used for light backgrounds, product studio cards)
  --text:         #E8E2D6   primary text on dark, paper-toned
  --text-2:       #96908A   secondary text, muted
  --text-meta:    #5A544E   tertiary text, archive metadata only

ACCENTS (disciplined, limited):
  --brass:        #C8A876   single warm accent — italics, highlights, hover
  --brass-deep:   #9E7F4C   archive brass for section marks, labels
  --oxide:        #5B7A8E   technical blue-grey (reserved, not yet used)
  --ember:        #D96B3A   RESTRICTED: SF3D section only, represents LN2 glow

RULES:
  --rule:         rgba(232, 226, 214, 0.08)    standard dividers
  --rule-strong:  rgba(232, 226, 214, 0.18)    emphasised dividers

Ember (#D96B3A) is deliberately confined to §04 SF3D section. It is part of the
story (LN2 vapour, liquid helium glow) and would dilute the palette if used
elsewhere. Brass is the only warm accent used outside §04.
```

### 3.3 Component patterns

**Section head.** `§XX` mark in mono-brass-deep, italicised emphasis word in Fraunces italic (SOFT 80-100), generous whitespace below. Establishes archival rhythm.

**Cover images (§02 products, §03 SpectralForge).** Aspect-ratio 16:8 (or 16:9 for featured), full width, subtle box-shadow, figcaption overlay at bottom with two-line caption (mono label + Fraunces italic subtitle). `cursor: zoom-in` and `data-zoom="true"` for lightbox.

**Portrait (§04).** Aspect-ratio 16:10, max-width 340px, paired with section intro text on larger screens. Different aspect from product covers to differentiate "person" from "product".

**Hero image (§04).** Aspect-ratio 4:5, max-width 420px, the largest single image on the page. Used for the LN2 vapour session image which is the iconic image of the archive.

**Proof rail (§04).** Four equal 4:3 tiles: SuperPi screenshot (paper bg), HWBot league (paper bg), Vegas bench (cabinet dark), Triple Point EVO product (paper bg). All zoomable.

**Bottom photo row (§04).** Four 4:3 tiles: 3DMark benchmark, −234°C display, dual-GPU bench, Critical Point product. Critical Point on paper bg, others on cabinet dark.

**Archive rows (§03).** Mono-only, three-column grid: year | name + status | description. Hover tints name brass.

**Archive featured (§03.0).** Image + body, 1.2fr 1fr grid, bordered below with extra space before the regular archive table.

**Approach items (§05).** Two-column: mono number | Fraunces-sized statement with emphasised italic clause.

### 3.4 Lightbox

All images with `data-zoom="true"` open in a fullscreen modal with:
- Backdrop blur, very dark translucent background
- × close button (paper background, brass on hover, positioned outside image top-right)
- ESC to close, backdrop click to close
- Caption rendered below image (mono, uppercase)
- Scroll lock while open
- Smooth fade + gentle zoom-in animation

Total JS for lightbox is ~50 lines, vanilla, no dependencies. In React build this becomes a small component.

---

## 4. CONTENT (locked)

### 4.1 §01 The connection — four disciplines

Paragraph intro:
> *"Whatever I do — a body, a benchmark, a codebase, a threat model — the work is the same. Find the pattern. Locate the root cause. Optimise until the system gives everything it can, stably."*

Four items (2x2 or 1x4 grid):
1. **Psychophysical physiotherapy** — two decades of clinical work, pattern recognition, root-cause reasoning on systems that cannot declare their own problems.
2. **Optimisation** — from teenage engine tuning to silicon under liquid helium. How much can a system give, and how stably can it give it?
3. **Cybersecurity & health-tech development** — the principal day role. Where understanding of the human body meets the systems that model it. Clinical and regulatory standards.
4. **Software** — the place where all of the above apply at once. Read the system. Find the root cause. Push past specification.

### 4.2 §02 Selected work — three products

Each with a cover image, mono meta column (status, year), Fraunces body (name, tagline, 2-paragraph description, 4-spec strip, single link).

**§02.1 MasterForge** · 2023 → present · Live, Paying customers
- Cover: Pro Master interface with parametric EQ, spectrogram, LUFS/True Peak meters, AI spectral analysis panel.
- Tagline: *"AI music mastering, for problems that didn't exist a year before it shipped."*
- Specs: Real-time DSP engine · ToneMap · 26 controls · Four tiers, Free to Studio · Stripe integration
- Link: masterforge.app

**§02.2 Quaesitor** · 2023 → present · Live, v2.12.11
- Cover: Resonance mode with three parallel streams (Alpha Analyyttinen, Beta Yhdistäjä, Gamma Falsifioija) + Assembler synthesis report.
- Tagline: *"A research engine that thinks, falsifies, and verifies — in code and in arithmetic."*
- Specs: Cognitive stream architecture · Three specialised reasoning lines · Falsify · verify · compute · Information Resistance Engine
- Link: quaesitor.app

**§02.3 Luviamo** · 2026 · Launching within the month
- Cover: landing page on paper background, birch-and-paper identity, "Markkinointi ideasta julkaisuun" headline.
- Tagline: *"One brand voice. The whole marketing lifecycle. Replacing five to eight separate tools."*
- Specs: Brand voice, learned once · Full marketing lifecycle · Solo to enterprise · GDPR-native, Nordic-built
- Link: luviamo.app

### 4.3 §03 The rest of the cabinet

**Featured (§03.0):** **SpectralForge** · 2025 → · Beta (image included, archival-featured treatment)
- Companion to MasterForge. Four-stage pipeline (HPS, Mel Clean, Click Repair, Transient Limiter). Per-band scoring, onset detection, attack-slope measurement. Closest to public release.
- Link: spectral.masterforge.app

**Archive table (7 rows, mono-typographic):**

| Year   | Name          | Status                          | Description |
|--------|---------------|---------------------------------|-------------|
| 2023 → | Premius Plus  | clinical platform               | Clinical wellness and rehabilitation platform. Programmes for migraine, tension headache, hip osteoarthritis, jaw & bite, men's pelvic floor, wellness assessment. Biopsychosocial methodology. |
| 2024   | TilastoSilta  | live                            | Finnish statistics aggregator across seven sources, with semantic AI search. tilastosilta.fi |
| 2025   | HEIJASTE      | entering public distribution    | Psychophysical self-reflection card system. Forty cards, five dimensions, three clinical editions including a veteran/PTSD branch. |
| 2023   | HomeTeam      | beta                            | Gamified family task system. HomeCoin economy, streaks, push notifications. home.sunrisesoftware.app |
| 2025   | VitalTrack    | beta                            | Personal training and health platform. TSS, NP, HR zones, PMC chart, Garmin sync. health.sunrisesoftware.app |
| 2025   | BrightFeed    | coming                          | News aggregation without engagement manipulation. Curated, clean, slow. |
| —      | Internal tools| production                      | BreathForge Studio, MasterVideo 3D, MasterPromo, PhotoMaster, VideoForge, SongForge, Command Center, Sunrise Marketing Planner, Premius Planner. Built for daily use; not for sale. |

### 4.4 §04 Archive · SF3D · 2006–2016 (note: currently says 2008–2016, to be corrected)

Intro text: *"Under the alias SF3D I spent ten years in the extreme overclocking scene — pouring liquid nitrogen, then liquid helium, onto silicon to see what it could do at temperatures it was never designed for. The intuition built there — pressure, tolerance, the line between working and failing — is the same intuition applied now to audio DSP, to machine-learning outputs, and to clinical reasoning."*

Section title: *"Before the software, liquid helium."*

Portrait: Taiwan / GALAX OC Carnival.

**Selected records:**
- 2006–2016 — Multiple world records in 3D and calculation benchmarks
- 2010 — First 7 GHz quad-core CPU, cooled with liquid helium
- 2012 — SuperPi 32M world record, Ivy Bridge class

**Principal sponsors (9):** Intel, AMD, Asus, ASRock, Foxconn, G.Skill, Kingston, Gigabyte, MSI.

**Proof rail (4 tiles):**
- §04a SuperPi 32M screenshot (paper bg) — "SuperPi 32M, 4m 47.031s · i7 3770K @ 6.90 GHz · 2012"
- §04b HWBot ranking (paper bg) — "HWBot Pro League, world #3 · SF3D · 1335.90 pts"
- §04c Vegas bench (cabinet bg) — "AMD world record event · Las Vegas · three-point thermal"
- §04d Triple Point EVO (paper bg) — "SF3D × EK Water Blocks · CPU LN₂ pot"

**Ventures (text only, 2 columns):**
- 2008 → 2013 · SF3D OC · Pre-overclocked systems. Jimm's PC Store. SF3D.fi storefront until 2013.
- 2010s · SF3D × EK Water Blocks · LN₂ product lines. Triple Point EVO (CPU) and Critical Point (GPU). International distribution.

**Bottom photo row (4 tiles):**
- Benchmark session · 3DMark
- Liquid helium · −234 °C
- Dual-GPU bench
- Critical Point · SF3D × EK (paper bg)

### 4.5 §05 Approach — three rules
1. *"I do not prototype. The first version ships. If a product is not worth releasing, it is not worth building."*
2. *"Every tool I build is one I use daily. The customer and the developer are the same person, separated only by time."*
3. *"If it is not better than what exists, I do not publish it. Sameness is not a business model."*

### 4.6 §06 Correspondence
- Header: "For serious conversations only."
- Body: "If the work above resembles something you need, or something you would like to see done properly, write directly. No forms, no calendars. A sentence or two is enough."
- Email: **pete@sunrisesoftware.app**
- Colophon links: MasterForge, Quaesitor, Luviamo, TilastoSilta, HomeTeam
- No GitHub (no public repos yet), no LinkedIn (no profile yet)

Footer: Sunrise Software Oy · Tampere, Finland · Est. 2024 · Independent · Typeset in Fraunces & Inter · © 2026

---

## 5. TECHNICAL ARCHITECTURE

### 5.1 Stack
```
FRAMEWORK:    Vite + React 19
STYLING:      Plain CSS with custom properties (same tokens as concept HTML)
                → do NOT introduce Tailwind for this project;
                  the custom-properties system is already cohesive
ANIMATIONS:   CSS + IntersectionObserver (already working in V4.5)
LIGHTBOX:     Small React component, same UX as V4.5
HOSTING:      Cloudflare Pages
BUILD:        Static site
DOMAIN:       sunrisesoftware.app
FONTS:        Google Fonts (Fraunces variable, Inter, JetBrains Mono)
IMAGES:       WebP primary, JPG fallback, responsive srcset for hero
```

### 5.2 Performance targets
- Lighthouse Performance 95+
- LCP < 1.8s (current image sizes already suitable: hero ~350 kB WebP, covers <100 kB each)
- CLS < 0.05
- Total page weight: ~4 MB including all images
- All images `loading="lazy"` except §00 and above-the-fold portion of §01

### 5.3 SEO
- Open Graph meta for main page; OG image to be designed (uses cabinet palette + Fraunces opening headline)
- JSON-LD: Organization (Sunrise Software Oy) + Person (Petri Korhonen) + SoftwareApplication entries for MasterForge, Quaesitor, Luviamo, SpectralForge
- Sitemap.xml
- Language: English primary (Finnish secondary version deferred)

### 5.4 Analytics
- Cloudflare Web Analytics (privacy-first, no cookies)

### 5.5 React structure (proposed)
```
src/
  main.jsx
  App.jsx
  components/
    Nav.jsx
    Lightbox.jsx
    SectionHead.jsx
    Opening.jsx          // §00
    Connection.jsx       // §01
    SelectedWork.jsx     // §02 + three WorkItem children
    Archive.jsx          // §03 + featured + rows
    SF3D.jsx             // §04 (largest component, internal sub-structure)
    Approach.jsx         // §05
    Correspondence.jsx   // §06
    Footer.jsx
  styles/
    tokens.css           // CSS custom properties (palette, typography, spacing)
    base.css             // reset, body, typography
    components.css       // all section styles
  content/
    works.js             // product data
    archive.js           // archive rows
    sf3d.js              // records, sponsors, ventures, images
  assets/
    images/              // all webp + jpg
```

Single-file HTML concept (V4.5) serves as the authoritative reference. React implementation should match visual result 1:1.

---

## 6. FOUNDER DATA (authoritative)

```
Name:       Petri Korhonen (NEVER "Pete Hietanen")
Company:    Sunrise Software Oy
Location:   Tampere, Finland
Email:      pete@sunrisesoftware.app

Alias:      SF3D (extreme overclocking scene, 2006-2016)

Roles:
  - Full-stack developer
  - Physiotherapist, twenty years
  - Development Manager (Premius Kuntoutus Oy)
  - Data Protection Officer (Premius Kuntoutus Oy)
  - Founder (Sunrise Software Oy, est. 2024)
```

---

## 7. FIXES QUEUED FOR NEXT BUILD STAGE

Items noted but not yet applied to V4.5 concept; to be corrected during React build:

- **SF3D years:** "2008-2016" → **"2006-2016"** (ten years, not eight). Appears in §04 label and intro text.
- **"Selected records" first row:** "2008-2016" → **"2006-2016"**.

Nothing else pending. All content, structure, and visual design are locked.

---

## 8. DESIGN ITERATION LOG

| Version | Date | Key changes | Status |
|---------|------|-------------|--------|
| V1 (original) | 2024 Q4 | SaaS-style single-page landing with 4 product cards | Deployed, outdated |
| SEED v1.0 | 2025-03-25 | Initial redesign planning, Playfair + DM Sans, sunrise gold | Planning |
| V2 concept | 2026-04-16 | Instrument Serif + Outfit, editorial tone, first person copy | Reviewed: too conservative |
| V3 concept | 2026-04-16 | Full-bleed hero photo, Syne font, dramatic glow dividers | Reviewed: font too curvy |
| V3 revised | 2026-04-16 | Bebas Neue + Exo 2, photo right 70%, sharper geometry | SEED v1.1.0 |
| **V4 concept** | **2026-04-17** | **Observatory × Atelier. Fraunces + Inter. Cabinet dark palette. Editorial §-sections. SF3D archive with photographs.** | **Direction confirmed** |
| V4.1 | 2026-04-17 | §01 expanded to four disciplines (psychophysical / optimisation / cybersec / software). Quaesitor rewritten around cognitive streams. Luviamo description about the marketing lifecycle. Archive reordered with Premius Plus first. Em-dashes removed from §06. Email to pete@. GitHub/LinkedIn removed. | Content approved |
| V4.2 | 2026-04-17 | First SF3D photographs integrated: hero LN2 session, portrait LN2 pour, three bottom thumbs (3DMark, -234°C, dual-GPU). | Photos approved |
| V4.3 | 2026-04-17 | SuperPi 32M screenshot, HWBot ranking, Taiwan portrait (replacing Finnish portrait), Vegas bench, EK × SF3D product photos (Triple Point EVO, Critical Point with paper-colour background treatment). Venture cards with images. | Photos approved |
| V4.4 | 2026-04-17 | Proof rail as 4-tile row equal to bottom row. Hero LN2 image scaled -15% for text-image balance. Taiwan portrait aspect-ratio corrected (16:10, prevents ear crop). Lightbox implemented for all §04 images (data-zoom=true, ESC/close/backdrop dismiss, scroll lock). | Implementation complete |
| **V4.5** | **2026-04-18** | **§02 product cover images added (MasterForge Pro Master, Quaesitor Resonance + Assembler, Luviamo landing). §03 SpectralForge promoted to featured entry with image. All new images receive data-zoom.** | **LOCKED** |

---

## 9. BUILD_INFO

```
SEED_VERSION:       2.0.0
PREVIOUS_VERSION:   1.1.0 (superseded, major direction change)
CREATED:            2025-03-25
LAST_MODIFIED:      2026-04-18
TOTAL_SESSIONS:     6 (Planning, V2 concept, V3+revised, V4 concept, V4.1-V4.4, V4.5)
STATUS:             Design locked, ready for React build
REFERENCE_FILE:     sunrise-software-concept-v4_5.html
REFERENCE_ZIP:      sunrise-v4-5.zip (contains index.html + images/)
NEXT_PHASE:         Vite + React implementation
PENDING_FIXES:      SF3D years 2008-2016 → 2006-2016
```

---

## 10. NEXT STEPS

1. Fix SF3D year range (2006-2016) as first edit in React build.
2. Scaffold Vite + React 19 project. Install no UI library; use plain CSS with tokens.
3. Port styles/tokens.css directly from the `<style>` block in V4.5 HTML.
4. Build components in section order (§00 → §06). Single Lightbox component used across all zoomable images.
5. Content in separate modules (works.js, archive.js, sf3d.js) so future edits do not touch markup.
6. Add OG image, favicon, meta, JSON-LD.
7. Deploy to Cloudflare Pages. Swap DNS at sunrisesoftware.app.
8. Cloudflare Web Analytics enabled.

---

## 11. DOCUMENT RULES

- **Author name:** Always "Petri Korhonen" (never "Pete Hietanen").
- **Company name:** "Sunrise Software Oy" appears only in footer and founder meta; not otherwise present on site.
- **Dashes:** Em-dashes are used in *design commentary* (this document) but not in on-site copy where it was explicitly removed (§06). In on-site copy, prefer commas, colons, or sentence restructuring.
- **SEED update:** Version + BUILD_INFO updated every session end.
- **Reference file:** sunrise-software-concept-v4_5.html is the authoritative visual reference until React build produces a new one.
