# SUNRISESOFTWARE-SITE-SEED v4.1.0

**Project:** Sunrise Software, company website, the sunrise generation with its own pages (site V6)
**URL:** https://sunrisesoftware.app/
**Owner:** Petri Korhonen / Sunrise Software Oy
**Created:** 2026-11-11 (v4.0.0); v4.1.0 on 2026-11-13, when the first sub-page was built
**Supersedes:** v4.0.0 (11.11.2026, in `docs/archive/`) and v3.0.0 (18.9.2026), which stays in `docs/` until V6 is live and is archived in the session that deploys it
**Status:** The spec for the revision. The front page carries the V6 changes of PR B (12.11.2026); `/silent-context/` is live since 13.11.2026 (PR #9); `/rooms/` is live since 13.11.2026 (PR #11); `/reviewglass/` is live since 13.11.2026 (PR #13); `/hometeam/` is live since 13.11.2026 (PR #16). Nothing here is built until it is built together with Petri (CLAUDE.md).

---

## 0. MINOR VERSION NOTICE (v4.0.0 to v4.1.0)

The first sub-page, `/silent-context/`, was built together with Petri on 13.11.2026 (rounds I and J in `docs/design/copy-v4-pages.md`), and building it narrowed section 3.6 in five places:

- **A vertical video gets a 9:16 frame at every width** when it has no 16:9 cut (I.3), at most 420 px wide and centred in the column.
- **A §04 entry shows a poster only when its video is 16:9** (I.4); an entry whose video is vertical carries the pill alone.
- **A status line that is a result**, not a word from the product scale, carries the sun dot (J.3).
- **The sub-page nav under 420 px** shows the sun mark without the wordmark, because the mark and the back link do not fit on one row (J.2).
- **The foot of a sub-page** is the water, the back pill and the footer line, without the front page's correspondence block (J.1).

CI checks every page the sitemap names (section 5.8). Nothing else changed.

## 0.1 MAJOR VERSION NOTICE (v3.0.0 to v4.0.0)

The site stops being one page (Petri, 11.11.2026, adr.sws.018), so a major version. Between v3.0.0 and v4.0.0:

- **The site has pages.** The front page keeps short pieces and each thing worth presenting gets its own address: `/rooms/`, `/reviewglass/`, `/silent-context/`, `/hometeam/`. Every page carries the same frame and a button back to the front page. Still static files on Cloudflare Pages with no build step (adr.sws.001, adr.sws.008 hold).
- **The site answers for itself** (adr.sws.017). Until 11.11.2026 every unknown address answered `200` with the whole front page, so `/favicon.ico`, `/apple-touch-icon.png` and any typo were soft 404s with HTML in them. There is now a `404.html`, and the icons a crawler, a browser and a phone ask for by name are real files at the root, drawn from the same sun mark by `scripts/icons.py`.
- **A dated section for what happened** (§04 Recent). The page had no place for an event, so two hackathon results had nowhere to go. Entries are dated, newest first, and each may lead to its own page.
- **The structured data names the products** (adr.sws.019, amending the decision of 18.9.2026). `WebSite`, `Organization.sameAs` for the product domains, and a `SoftwareApplication` entity for each product the page marks live, so an answer engine asked what Sunrise Software makes finds a list rather than prose.
- **Video is a form the site uses.** The lab's rule (`adr.sf3d.010`) holds here too: the site plays its own file and embeds no third-party player, and the long evidence stays where it was published.

What survives from v3.0.0: the whole visual design system (section 3, unchanged), the numbered sections, first person singular, restraint (no hero statistics, no generic adjectives, no em dashes), dated statuses with no product version numbers (adr.sws.004, adr.sws.015), the one status scale, the withheld employer names (adr.sws.006), and the founder data.

---

## 1. VISION AND THE READER

### 1.1 Positioning

Software for people, built by someone who spent twenty years understanding them. The page is one morning: the first ray at the top, clear morning paper for the work, the open sea at the bottom. Its ideology stands in one line near the end: *Imagination is the limit. Build, then enjoy the world.*

### 1.2 The readers

1. **A serious buyer or collaborator**: reads the headline, §01 and the products, writes an email.
2. **A technical reader**: in ten seconds the page answers what is shipped and live (dated statuses, links), whether there is code (GitHub in the nav and the meta row), how the work is done (§04's method block) and what the instruments behind it are. From 11.11.2026 that reader can also go one level deeper without leaving the site, because the deep things have their own pages.
3. **A machine answering a question about the company**: finds a `WebSite`, an `Organization` with its product domains, a `Person`, and a `SoftwareApplication` per live product, plus one page per subject with its own title and description.

### 1.3 Principles

- One glance and the understanding comes without reading: every product plate shows the product doing its thing.
- Nothing on the page that is not the real product, except a drawn instrument where the product has no public surface.
- Interactions are inviting and responsive: things grow as the pointer nears, previews park where the hand is, drawers pull.
- Dated, never relative: no "coming soon", "recently", "within the month".
- **The front page stays short.** A subject that needs more than a paragraph gets its own page; the front page says the one line and links to it.
- **The same fact lives in one place.** A page here links to the evidence where it was published rather than copying it.

---

## 2. SITE ARCHITECTURE (V6)

```
/                               the front page (V5's architecture, with §04 added)
├─ SKY (fixed layer)            dawn gradient + drifting orbs; the reading light; the sea rising at the end
├─ NAV (fixed, blur on scroll)  Sunrise Software · Products · Recent · Approach · Contact · GitHub ↗
├─ HERO                         kicker · headline · lede · meta row · portrait cutout
├─ §01 The connection           title · intro · four disciplines
├─ §02 Products                 "Commercial products": MasterForge, Luviamo
│                               "Tools and research instruments": Somnus, Atlas
├─ §03 Also in production       eight drawers: Virustutka, Ultra Gravel, TilastoSilta, SF3D AI Lab,
│                               ReviewGlass, Salpa Defence, SpectralForge, HomeTeam
├─ §04 Recent            NEW    dated entries, newest first; an entry may lead to its own page
├─ Before the software · SF3D   claim · lead · button "Open the cryo chamber" · the chamber (unfolds)
├─ §05 Approach                 title · three rules · the creed · method (Build, Gate, Run, Record)
├─ §06 Correspondence           "Let's talk." · body · email · link list
└─ FOOTER (inside the shore)    company · Est. 2024 · Revised <date>

/rooms/                  NEW    Atlas decision rooms: the video, how a room is built, what is measured
/reviewglass/            NEW    ReviewGlass: the video or the mockup, what it does, the open repository
/silent-context/         NEW    Silent context and Since AI 2026: what it does, the vertical video, the repository
/hometeam/               NEW    HomeTeam: what the family application does, where it runs

/404.html                NEW    served for every unknown address
/favicon.ico /icon-192.png /icon-512.png /icon-maskable-512.png /apple-touch-icon.png /site.webmanifest
/robots.txt /sitemap.xml /_headers
/scc/                           the SCC2 install icons (adr.sws.016), not part of this site's navigation
```

Every section of the front page is a `<section class="sec">` on `z-index:1` over the fixed sky. Section marks stay decorative and navigational.

### 2.1 What a sub-page is

A sub-page is one `index.html` in its own directory, so the address has no `.html` in it and ends in a slash. It is a static file like the front page: inline CSS and JS, no build step, no framework (adr.sws.001, adr.sws.008).

Each sub-page carries, in this order:

1. **The frame**: the same `<head>` rules as the front page (description, canonical to its own address, Open Graph with its own title and image, the icon links, JSON-LD for that subject), the sky layer and the nav, with the wordmark linking home.
2. **A back button**, `Back to the front page`, in the nav row and again at the foot of the page, so the reader never has to use the browser's own button.
3. **A title block**: the mono subject mark, the h1, a one-paragraph lede, and a dated status line on the one scale.
4. **The lead medium**: the video where there is one, played from this site's own file with a poster, `preload="none"`, controls, captions where they exist; otherwise the subject's real capture or its drawn instrument.
5. **The body**: short sections, each a heading and one or two paragraphs. No section without something checked behind it.
6. **Evidence and links**: the repository, the live address, and the longer writing where it was published (for the rooms, the sf3d.fi articles).
7. **The shore and the footer**, as on the front page, with the page's own revision date.

A sub-page carries no hero statistics, no generic adjectives, and no product version numbers, exactly as the front page.

### 2.2 The first four sub-pages

| Page | Subject | Lead medium | Evidence it links to |
|---|---|---|---|
| `/rooms/` | The Atlas decision rooms, told with the names the field uses; **copy decided 13.11.2026** (rounds K to O, R.1 to R.15), media round P, **built 13.11.2026 (PR D)**, round Q | `media/rooms-en.mp4` (16:9) copied from `sf3d-ai-lab/media/publish/rooms/`, with its 9:16 cut where the layout is narrow, and the lab's `rooms-en.vtt` as its captions | the sf3d.fi articles `the-room-that-disagreed` and `decision-rooms-in-a-minute` (13.11.2026, K.3: `blind-to-anything-taken-away` is a Somnus article and had come into this list by its title; `why-i-built-atlas` waits for Atlas's own page) |
| `/reviewglass/` | What the glass does during an AI-assisted coding session; **copy decided 13.11.2026** (rounds S to W, RG.1 to RG.15), **built 13.11.2026 (PR E)**, round X | the ReviewGlass canvas instrument from §03, enlarged by the page's own copy of its code (X.1); from PR G ReviewGlass's own windows, drawn by its own code with a staged core, over a staged screen (round AE, adr.sws.021, 14.11.2026) | `github.com/Sunrisesoftware-app/reviewglass` (Apache-2.0) |
| `/silent-context/` | Silent context and the Since AI 2026 result; **built 13.11.2026 (PR C)** | `media/silent-context-916.mp4`, the vertical cut re-encoded to 720x1280 | `github.com/pkorrrhonen-cmd/silent-context`, tag `submission`; the hosted demo `silent-context.pkorrrhonen.workers.dev` (decided 12.11.2026) |
| `/hometeam/` | The family application in production; **images decided 13.11.2026** (round Y, adr.sws.020), **copy decided 13.11.2026** (rounds Z to AC, HT.1 to HT.16), **built 13.11.2026 (PR F)**, round AD | screens cut from the HomeTeam design mockups: the child's and the adult's Today side by side, then Wallet, the weekly scoreboard and the treasure island; Finnish with English captions; nicknames only, `Hei, Petri!` may stay | none public: `app.hometeam.fi` admits only allowed addresses |

### 2.3 The names the rooms page uses

The vocabulary comes from Atlas `ATLAS-HUONEET-KAR-ARV-20261031` v1 (31.10.2026, 28 sources), which is the record of how the field reads what a room does. The page may use, and must use correctly:

- **multi-agent debate** for the setting, and **model heterogeneity** for why the seats come from two model families
- **blind sealed first votes**, revealed together, then rounds
- **devil's advocate** and **dialectical inquiry** for the challenger's seat (Schweiger, Sandberg & Ragan 1986; Schwenk 1990; Nemeth, Brown & Rogers 2001)
- **LLM-as-a-judge** and **judge calibration** for the judge, with the known leniency and the narrowed scale said plainly
- **pre-registration** for the plan locked before the room opens
- **maximin** for the room's value, the lower of the seats' final weights
- **sycophancy** and **conformity** for the failure the setting is built against

The word **Delphi** does not go on the page until a source for it is recorded here, even though sealed first votes revealed together and iterated rounds are that method's shape (decided 11.11.2026).

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

**Cryo chamber.** Above it: the section mark in `--ember`, the claim (h2), the lead, and the button (a dark pill with a pulsing ice dot, `Open the cryo chamber`). The chamber unfolds below: `--cryo` gradient, ice hairlines, a fog canvas (drifting radial gradients), a top bar with the label and Close, the title, two paragraphs, three records (ice left rules), four readouts (Coolant, Lowest probe reading, HWBot Pro League, Principal sponsors), then a draggable strip of eight 4:3 photo cards in a cold treatment (desaturated, ice captions), each opening the lightbox.

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

Drawers: Virustutka (map capture, preview and drawer), Ultra Gravel (Petri's planned-loop captures), TilastoSilta and SF3D AI Lab (front-page captures), ReviewGlass (the interface mockup canvas: blurred columns, the reading frame, the glass; from PR G its own windows over a staged screen, adr.sws.021), Salpa Defence (the horizontal brand mark on Kuusi; `ACCESS DENIED` stamp in Messinki on hover), SpectralForge (the UI screenshot).

---

---

### 3.6 Components added in v4.0.0

**§04 Recent (front page).** Section head as everywhere. Under it, entries in a single column, newest first, each one a row on a hairline: the date in mono (`8 Nov 2026`, never relative), the event's name as an h3, one or two sentences, and where there is a page for it, the pill `Read the whole thing ↗` in the §02 pill style. An entry whose video is 16:9 shows its poster frame at the left on wide screens, stacked above the text on a phone; an entry whose video is vertical shows no poster and carries the pill alone (decided 13.11.2026, I.4). The video itself plays on the entry's own page, not here. At most five entries on the front page; older ones live on their pages and in the sitemap.

**Sub-page frame.** The sky layer and the nav exactly as the front page, with the wordmark linking to `/`. In the nav row, in place of the section links, a single `← Back to the front page` in the nav's 500 weight. Under 420 px the wordmark's text is hidden and the sun mark alone goes home, because the two do not fit on one row (J.2). The page's content column is `max-width: 820px` inside the usual `.wrap`, narrower than the front page because it is read rather than scanned.

**Sub-page title block.** Mono subject mark in `--sun-deep`, h1 at the front page's h2 size (`clamp(28px,3.4vw,48px)`), the lede in Public Sans 300 at 17px, max 58ch, and the status line in the §02 style with its dot: green for Live, the sea for infrastructure, and the sun when the line is a result rather than a word from the product scale (J.3). The column sits on the left edge of `.wrap`, on the wordmark's line, as the front page's headings do (J.2).

**Video block.** A 16:9 frame in `--paper-2` with radius 8 and the plate's long shadow, holding a `<video controls preload="none" playsinline>` with its poster and, where a `.srt` exists, a `<track kind="captions">` converted to WebVTT. Under it, a mono caption: what it shows and its length. On a phone the vertical cut is used where one exists, in a 9:16 frame at most 420 px wide, centred; on `/rooms/` the phone is a viewport up to 600 px, a short script picks the cut and its poster once at load, and without JavaScript the 16:9 cut plays everywhere (Q.1). The caption sits on the column's left edge under a 16:9 frame and is centred under a 9:16 one. A page whose only video is vertical uses that 9:16 frame at every width, centred in the column (I.3); a 16:9 frame would shrink it to a strip between black bars. On `/reviewglass/` the same 16:9 frame holds the §03 drawing instead of a video (X.1): the page's own copy of the front page's canvas code, the front page's still at once, the glass moving only while the frame is on screen and the still alone under reduced motion or `?static=1`; its mono caption says it is a drawing.

**Evidence block.** A hairline, a mono label `Evidence`, and a list of links in two columns on wide screens: the name over the address, exactly as the shore's link list. This is where a page sends the reader for the long version.

**Foot of a sub-page.** The shore's water, glints and sun path as on the front page, then the back button repeated as a paper pill, then the footer line with the page's own revision date. No correspondence block: the contact is on the front page's shore (J.1).

---

## 4. CONTENT

The front page's copy is decided item by item in **`docs/design/copy-v3.md`**, which stays the source of every text on it; the sub-pages' copy is decided the same way in **`docs/design/copy-v4-pages.md`** when they are built. This section indexes both.

| Part | What | Source items |
|---|---|---|
| Frame | title, meta description, nav, kicker, headline, lede, meta row, portrait caption | copy-v3 0.1 to 0.10 |
| §01 | `Four disciplines. One shared method.`, intro, four items | copy-v3 1.1 to 1.11 |
| §02 | `Products people pay for, and the instruments behind them.`, groups, MasterForge, Luviamo, Somnus, Atlas | copy-v3 2.1 to 2.34 |
| §03 | `More products, tools and instruments.`, eight rows (HomeTeam added in v4) | copy-v3 3.1 to 3.39, copy-v4-pages 3.40 to 3.46 |
| §04 Recent | the section title, the Since AI 2026 entry, the AMD ACT III entry | copy-v4-pages 4.1 to 4.9 |
| SF3D | claim, lead, button, chamber label, title, two paragraphs, records, readouts, captions | copy-v3 4.1 to 4.11 |
| §05 Approach | `How the work gets done.`, three rules, the creed, method | copy-v3 5.1 to 5.11 |
| §06 and footer | `Let's talk.`, body, email, link list, footer | copy-v3 6.1 to 6.8 |
| `/rooms/` | mark, h1, lede, status, video caption, body sections, evidence list, the Atlas plate's button | copy-v4-pages R.1 to R.15 |
| `/reviewglass/` | the same shape, and the drawer's link and fact | copy-v4-pages RG.1 to RG.15, X.1 to X.3 |
| `/silent-context/` | the same shape | copy-v4-pages SC.1 to SC.14 |
| `/hometeam/` | the same shape | copy-v4-pages HT.1 to HT.16 (rounds Y onwards) |
| Shipped with the site | OG title and description per page | copy-v4-pages 7.1 to 7.n |

Rules for copy, on every page of the site: English, first person singular, no em dashes, no relative time, every status dated and no product version numbers (adr.sws.015), one status scale (Live, In use, Closed beta, Pre-alpha, Venture), no hero statistics, no generic adjectives, the company name only in the footer and the structured data, no employer's product names (adr.sws.006), no technology names in spec strips. A claim about another project is checked from that project's repository or its live service in the same session, never from memory.

---

## 5. TECHNICAL

### 5.1 Stack

Static files with inline CSS and JS, `images/`, `media/`, Google Fonts, Cloudflare Pages with Git integration (adr.sws.001; the React migration is off the roadmap, adr.sws.008). The front page is `index.html`; each sub-page is `index.html` in its own directory. No build step and no shared template file: the frame is copied into each page, and `scripts/check-site.mjs` is what keeps the copies honest.

### 5.2 Assets shipped with the site

| Asset | Source | Page file |
|---|---|---|
| Portrait cutout | `images/Petri.jpg` (16.8.2026), cut out 18.9.2026 | `images/petri-cutout.webp` + `.png`, two sizes (880 and 440 px) |
| MasterForge EQ clip | the MasterForge captures | `media/masterforge-eq.mp4` (3.4 MB) + poster |
| Luviamo video | `luviamo.app/media/luviamo-esittely-v2.mp4`, copied 19.9.2026 | `media/luviamo-intro.mp4` (5.1 MB) + poster; both clips `preload="none"` |
| Rooms video | `sf3d-ai-lab/media/publish/rooms/rooms-en.mp4` (1920x1080, 118 s, 6.4 MB) and `rooms/rooms-en-916.mp4` (1080x1920, 5.9 MB), local renders the lab's git ignores; captions `sf3d-ai-lab/site/public/video/rooms-en.vtt` | `media/rooms-en.mp4`, `media/rooms-en-916.mp4` (copied as they are, P.1), `media/rooms-en.vtt` (on by default, P.4) + `media/rooms-en-poster.jpg` and `media/rooms-en-916-poster.jpg`, the `BLIND` card at 23 s (P.2); made 13.11.2026 |
| Silent context video | `sinceai2026/silent-context-third-place-9x16-captions.mp4` (1080x1920, 77.8 s, 15.7 MB) | `media/silent-context-916.mp4` (720x1280, H.264 CRF 25, AAC 128 kb/s, faststart, 5.55 MB, made 13.11.2026) + `media/silent-context-916-poster.jpg`, the frame at 1.5 s (I.1) |
| Drawer captures | `docs/mockups/shots/` | `images/shot-*.webp` with JPG fallbacks |
| HomeTeam | screens cut from its design mockups (adr.sws.020, 13.11.2026, replacing the drawn instrument of 11.11.2026); captured from a copy outside the repository with the names swapped for nicknames | `images/hometeam-*.webp` with PNG fallbacks; the drawer's `images/shot-hometeam.webp` (PR F, 13.11.2026); the canvas sketch removed |
| ReviewGlass | its own windows (the glass, the diff window, the halo, the dock) rendered from its public `main` with a staged core, over a staged screen re-enacting this site's version-guard fix (commit `2aef4d2`), light Windows theme (adr.sws.021, round AE, 14.11.2026); `docs/mockups/reviewglass-mockup.py`, made outside the repository | to be made in PR G: the lead medium of `/reviewglass/` and the §03 drawer's image, WebP with a JPG fallback, the 2x source in `source-assets/`; the canvas sketch removed then |
| SpectralForge, Salpa mark, SF3D photographs | as in v3.0.0 | unchanged |
| OG image, front page | generated 18.9.2026, 1200x630 | `images/og-cover.jpg` |
| OG image, per sub-page | `docs/mockups/og-<page>.html` (the subject mark and the h1 on the dawn sky, in `og-cover.jpg`'s build, with the site's own fonts) rendered by `docs/mockups/shoot.py` | `images/og-<page>.jpg`, 1200x630; `og-silent-context.jpg` made 13.11.2026 (I.2), `og-rooms.jpg` made 13.11.2026 (P.3), `og-reviewglass.jpg` made 13.11.2026 (X.3) |
| Icons | `scripts/icons.py`, drawn from the sun mark | `/favicon.ico` (16, 32, 48), `/icon-192.png`, `/icon-512.png`, `/icon-maskable-512.png`, `/apple-touch-icon.png`, `/site.webmanifest` |
| Favicon, inline | the sun mark as an SVG data URI | kept as the first `<link rel="icon">` in every `<head>` |

### 5.3 Head, SEO and GEO

Every page: `<meta name="description">` written for that page, canonical to its own address, `theme-color #F9F7F1`, Open Graph and Twitter card with that page's title, description and image, `og:image:alt`, and `<meta name="robots" content="index, follow, max-image-preview:large, max-snippet:-1, max-video-preview:-1">`. The icon links come in the order: the SVG data URI, `/favicon.ico`, `/icon-192.png`, `/apple-touch-icon.png`, `/site.webmanifest`.

`robots.txt` allows all and disallows `/docs/`, `/source-assets/` and `/scripts/`. `sitemap.xml` names every page of the site with its own `lastmod`, and CI checks the front page's `lastmod` against `BUILD_INFO.updated`.

Structured data (adr.sws.019, amending the decision of 18.9.2026) in the front page's `@graph`:

- `WebSite` with `name`, `url` and `publisher` pointing at the Organization
- `Organization` as today, with `sameAs` naming `masterforge.app`, `luviamo.app`, `virustutka.app`, `ultragravel.app`, `tilastosilta.fi`, `sf3d.fi` and the GitHub profile
- `Person` as today
- one `SoftwareApplication` per product anyone can open (five: MasterForge, Luviamo, Virustutka, Ultra Gravel, TilastoSilta), each with `name`, `url`, the page's own one-line description, `applicationCategory`, `operatingSystem`, `author` pointing at the Person and `publisher` pointing at the Organization
- SF3D AI Lab as a `WebSite`, because it is a research lab site and not an application
- `logo` on the Organization, the sun mark at `/icon-512.png`

A sub-page carries only what it is about: `WebPage` with `isPartOf` the WebSite, plus the one `SoftwareApplication`, `SoftwareSourceCode` or `CreativeWork` the page describes, and a `VideoObject` for the page's own video where it has one. No entity on a sub-page that the front page does not also know, except that video (adr.sws.019, amended 12.11.2026). `/silent-context/` carries `WebPage`, `SoftwareSourceCode` and `VideoObject`, and the front page's graph gains the same `SoftwareSourceCode`.

### 5.4 The site answers for itself (adr.sws.017)

`404.html` at the root, so Cloudflare Pages answers `404` for an unknown address instead of serving the front page with `200`. The icons and the manifest are real files at the root with their own `_headers` cache rules. `scripts/check-site.mjs` fails when any of them is missing.

### 5.5 Performance

Targets: Lighthouse 95+, LCP under 2 s, CLS under 0.05. No video loads before it is asked for: every clip is `preload="none"` with a poster, and the clips on sub-pages have `controls` rather than autoplay. All images `loading="lazy"` except the portrait; WebP first with a JPG fallback. A sub-page carries only its own media.

### 5.6 Accessibility

Reduced motion honoured. Every interactive element is a button or a link with `aria-expanded` where it opens something; `:focus-visible` outline in `--sun`; the lightbox is a dialog closed by Escape. On a sub-page the back button is a real link to `/`, reachable first by keyboard. A video has captions where a caption file exists, and its caption text says what it shows.

### 5.7 Analytics

Cloudflare Web Analytics, once the token is fetched from the dashboard (open in BUILD_INFO).

### 5.8 CI

`scripts/check-site.mjs` on pull requests and `main`: local file references exist, required head elements, no em dashes in copy, forbidden strings (the employer's product names, `2008-2016`, "Launching within the month", "coming soon", "within the month", "recently"), no product version numbers (with a self-test, so a broken pattern cannot pass silently again), the footer `data-revised` equals `BUILD_INFO.updated`, the GitHub link appears at least four times, `sitemap.xml` `lastmod` equals `BUILD_INFO.updated` and names the canonical address, and the site's own files exist (`404.html`, the five icons, the manifest). Since 13.11.2026 the checks run over every page the sitemap names, each against its own canonical address and its own `lastmod`; a sub-page on disk that the sitemap does not name, or that the front page does not link, fails the gate, and a sub-page must carry its back button.

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

---

## 7. DESIGN ITERATION LOG

| Version | Date | Key changes | Status |
|---|---|---|---|
| V4.5 | 2026-04-18 | cabinet dark, Fraunces, SF3D section (SEED v2.0.0) | published, superseded |
| Look 1 | 2026-09-17 | three sunrise palettes on one screen; A shifted toward C chosen (adr.sws.010) | done |
| Flow 1 | 2026-09-17 | elements, motion, flow; "exactly the right direction" (adr.sws.011) | done |
| Flow 2 | 2026-09-18 | Petri's answers applied: tighter, cutout portrait, reading light, parked previews, growing plus, lighter shore, cryo chamber, living plates | done |
| Type 1 | 2026-09-18 | six pairs; Familjen Grotesk + Public Sans chosen (adr.sws.012) | done |
| Flow 3 | 2026-09-18 | the decided copy (copy-v3.md); two headings and the cryo text re-decided | done |
| Flow 4 | 2026-09-18 | the decided app views (apps-v3.md) | accepted (adr.sws.013) |
| V5 | 2026-09-18 | `index.html` rewritten to Flow 4 with the page assets; check-site green | live 18.9.2026 (PR #1) |
| V5 feedback | 2026-09-19 | 14 items from chat's reading of the live page (`docs/design/feedback-v5.md`) | done, decided with Petri |
| V5 dates | 2026-09-20 | every product version number removed; a status carries a date (adr.sws.015) | live 20.9.2026 (PR #4) |
| Site files | 2026-11-11 | `404.html`, the icon files and the manifest, the sitemap's date, the version guard repaired (adr.sws.017) | **PR A, no page change** |
| V6 spec | 2026-11-11 | the site gains pages (adr.sws.018), §04 Recent, HomeTeam's drawer, the structured data names the products (adr.sws.019) | spec written |
| V6 front page | 2026-11-12 | PR B: §04 Recent with two entries, Approach and Correspondence renumbered, the nav's Recent, HomeTeam's drawer with its drawn instrument, the icon links, `max-image-preview`, `og:image:alt`, the structured data | PR B, live 12.11.2026 (PR #7) |
| V6 /silent-context/ | 2026-11-13 | PR C: the first sub-page, its video, poster and share image; the front page's entry 1 pill and `SoftwareSourceCode`; CI over every page | PR C, live 13.11.2026 (PR #9) |
| **V6 /rooms/** | 2026-11-13 | PR D: the decision rooms page, its two cuts with captions on by default, posters and share image; the Atlas plate's button in §02 | **PR D, live 13.11.2026 (PR #11)** |
| **V6 /reviewglass/** | 2026-11-13 | PR E: the ReviewGlass page with the §03 drawing enlarged and its share image; in §03 the drawer's link to the page and its corrected fact, and the code entity in the front page's graph | **PR E, live 13.11.2026 (PR #13)** |
| **V6 /hometeam/** | 2026-11-13 | PR F: the family application's page with five screens cut from its design mockups (names swapped outside the repository, adr.sws.020) and its share image; the HomeTeam drawer's screen and link in §03 | **PR F, live 13.11.2026 (PR #16)** |
| ReviewGlass mockup | 2026-11-14 | round AE: ReviewGlass's own windows drawn by its own code with a staged core, over a staged screen, replacing the drawing on `/reviewglass/` and in §03 (adr.sws.021) | method decided; copy round AF and PR G next |

---

## 8. NEXT STEPS

The order is the order of the decisions taken on 11.11.2026, and nothing that touches a page is built alone (CLAUDE.md).

1. **Done 11.11.2026, PR A, no page change:** `404.html`, `favicon.ico` and the four PNG icons from `scripts/icons.py`, `site.webmanifest`, the `_headers` rules for them, `sitemap.xml` `lastmod`, the repaired version guard with its self-test, and the two new checks in `check-site.mjs`.
2. **Read before any copy is written:** the `hometeam` repository's README and BUILD_INFO for the drawer and its page, the live SpectralForge beta gate (A7), and the profile README against the page (A10, the session routine).
3. **`docs/design/copy-v4-pages.md`**: every new text as a numbered item, decided with Petri through decision boxes, four a round. The front page's items were decided 11.11.2026 (rounds A to C); `/silent-context/` was decided 12.11.2026 (rounds E to H, items SC.1 to SC.14); `/rooms/` 13.11.2026 (rounds K to O, items R.1 to R.15); `/reviewglass/` 13.11.2026 (rounds S to W, items RG.1 to RG.15).
4. **The media**: done 13.11.2026 for `/silent-context/` (the video, its poster, the share image). Done 13.11.2026 for `/rooms/` (round P: the two cuts and their captions copied, two posters, the share image). Done 13.11.2026 for `/reviewglass/` (round X: the share image; its lead medium is the §03 drawing). **Petri 13.11.2026:** real mockups of the applications have to get onto the pages in place of the drawn instruments, and ReviewGlass's is built some other way than a screen capture, because the glass excludes itself from capture (only the dock and its drawer are visible to one, ReviewGlass adr.rg.025); the method is decided with Petri, one product at a time, and gets a decision file. HomeTeam is the first product under that line (round Y, 13.11.2026, adr.sws.020): screens cut from its design mockups, nicknames only. ReviewGlass is the second (round AE, 14.11.2026, adr.sws.021): its own windows drawn by its own code with a staged core over a staged screen; its copy round (AF) and its build (PR G) are next. Done 13.11.2026 for `/hometeam/` (PR F, round AD): five screens and the drawer's 16:9 image cut from a name-swapped copy outside the repository, and the share image.
5. **Built 12.11.2026, PR B, the page**: §04 Recent with the two entries, the HomeTeam drawer, the nav's Recent link, the icon links and `max-image-preview` in `<head>`, `og:image:alt`, and the structured data of adr.sws.019. Checked on the preview URL at desktop and phone width before merging.
6. **PR C and after, one sub-page at a time**: `/silent-context/` built 13.11.2026 (PR C, with the front page's entry 1 pill), `/rooms/` built 13.11.2026 (PR D, with the Atlas plate's button), `/reviewglass/` built 13.11.2026 (PR E, with the drawer's link and fact), `/hometeam/` built 13.11.2026 (PR F, with the drawer's screen and link), each with its sitemap entry and its own `check-site` pass.
7. **Still open from before:** Cloudflare Web Analytics token, Lighthouse and the HTML validator on the live site, adr.sws.014 (one source for the facts the page shares with the profile README), the Atlas model proposals for adr.sws.003 to 019, the static-bearer removal, and the employer's names in the profile README.

---

## 9. DOCUMENT RULES

- Author name always "Petri Korhonen"; the company name only in the footer and the structured data.
- No em dashes in copy or documents; en dashes only in year ranges.
- Front page copy lives in `docs/design/copy-v3.md`, sub-page copy in `docs/design/copy-v4-pages.md`, app views in `docs/design/apps-v3.md`; this SEED indexes them and holds the design system.
- The site is edited only together with Petri (CLAUDE.md); a change to the design system is a new SEED version.
