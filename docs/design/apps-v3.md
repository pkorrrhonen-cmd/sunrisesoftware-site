# Apps v3: how each product is shown

**Purpose:** the application-view round. For every product on the page: what the visitor sees
(the plate, the drawer image, the preview), where the media comes from, and what the drawn
sketch is a stand-in for. Decided item by item with Petri, four at a time, like the copy. When
every item is `OK`, Flow 4 is built with the real media and SEED v3.0.0 can be written.

**Rules from Petri (18.9.):** one glance and the understanding comes without reading anything,
so every plate shows the product doing its thing. And in the drawers nothing that is not the real
product: real captures where the product is public, the brand mark where it is not (Salpa), a
mockup of the real interface where a screenshot would have to be blurred (ReviewGlass). Drawn
sketches remain only on the §02 plates for Somnus and Atlas, which have no public surface.

**Status legend:** `draft` (proposal) · `OK` · `edit` · `drop`. **Status 18.9.2026 evening: every item decided; the Ultra Gravel route capture received from Petri.**

**Media on hand (18.9.2026):**

| Product | What exists | Where |
|---|---|---|
| MasterForge | Pro Master UI screenshot (V4.5 cover); real UI capture clips from the ad-video work: EQ (3.4 MB, 12.5 s), compressor (1.6 MB, 12.3 s), AI artifact suppressor (2.0 MB, 7.5 s), plus vertical cuts; feature screenshots (EQ, limiter, de-esser, report, batch, export) | `images/product-masterforge.webp`; `masterforge/data/video creation/captures/`; `masterforge/images/features/` |
| Luviamo | intro video (5 MB, 16:9) and its poster; product landing screenshot (V4.5 cover) | `luviamo.app/media/luviamo-esittely-v2.mp4`; `images/product-luviamo.webp` |
| Somnus | no public image; four blog figures (U-curve, beta phase, collapse, funnel) in the repo | `somnus/docs/blog/images/` |
| Atlas | viewer and Connect are access-protected; no cleared screenshot | drawn schematic only |
| SpectralForge | UI screenshot (V4.5 featured cover) | `images/product-spectralforge.webp` |
| Virustutka, Ultra Gravel, TilastoSilta, SF3D AI Lab | live-site front-page captures (17.9.2026) | `docs/mockups/shots/` |
| ReviewGlass | nothing public (pre-alpha desktop app) | sketch |
| Salpa Defence | demo behind Cloudflare Access; nothing public | sketch |
| SF3D archive | ten photographs (in git) | `images/sf3d-*` |

---

## A. §02 plates (the four big products)

Each plate: a 16:10 frame that moves, a small caption over it, an "Open ↗" pill on hover, and
the plate's link. The visitor should get the product in one glance.

| # | Product | Now (Flow 3) | Proposal | Status |
|---|---|---|---|---|
| A.1 | MasterForge plate | canvas sketch: gold meters and an EQ curve breathing | **The EQ capture on loop** (`captures/eq/eq.mp4`, 12.5 s, 3.4 MB), muted, cropped to 16:10, autoplays in view, poster frame from the clip; the sketch stays as the fallback. Caption `Pro Master · EQ, live` | OK (18.9.) |
| A.2 | MasterForge plate: alternative | | keep the sketch | drop |
| A.3 | Luviamo plate | the real intro video, muted, plays in view, poster | keep; a click restarts it with sound; caption `Intro · luviamo.app` | OK (18.9.) |
| A.4 | Somnus plate | canvas sketch: formulae drifting inside a box | **Rack panel** (draft 3 of `docs/mockups/somnus-plate.html`, chosen 18.9.): an instrument's front panel on dark: two GPU load meters on the left (GPU 0 R9700 32 GB, GPU 1 7900 XT 20 GB), a six-row live job list on the right, one row running with a percentage, the others queued or done. Rows: AUDIO SEPARATION (stems for MasterForge and SpectralForge), RESEARCH FUNNEL (candidates screened locally), ATLAS COMPUTE (validation runs, ideas tested), SALPA PROCESSOR (local models for defence), LOCAL INFERENCE (every project, day and night), RESEARCH ENGINE (what Quaesitor did, now local). Status line `LOCAL AI SERVER · ALWAYS ON · COST ≈ 0 €`. Petri's direction: Somnus is the workhorse; the funnel is one task among many; clinical style | OK (18.9.) |
| A.5 | Somnus plate: alternative | | the blog funnel figure | drop |
| A.6 | Atlas plate | the SVG schematic (model in the middle, three doors, gates) | **Workspace board**: three columns (Projects, Waiting on, Decided) with cards that slide in, a partner avatar and a phone outline, a small library shelf below; the doors and gates go. Caption `Atlas · the workspace` | OK (18.9.) |
| A.7 | Atlas plate: alternative | | relabelled schematic | drop |
| A.8 | The hover pill | on hover, every plate | `Visit ↗` on the three that link out; on Atlas `Access-protected` | OK (edit 18.9.) |
| A.9 | Plate captions | mono, top-left of the frame | keep; MasterForge `Pro Master · EQ, live`, Luviamo `Intro · luviamo.app`, Somnus `Somnus · local AI server · always on`, Atlas `Atlas · the workspace` | OK |

## B. §03 drawers (the seven rows)

Each drawer: on hover a parked preview (540 px) beside the plus; on open a paragraph, three
facts, a link and one big image or living canvas (16:9, up to 820 px).

| # | Product | Now (Flow 3) | Proposal | Status |
|---|---|---|---|---|
| B.1 | Virustutka | live-site capture (the map) in the drawer; sketch (blob map pulsing) as the preview | **Real product only** (Petri 18.9.: nothing that is not the real product): the live map capture in both the preview and the drawer; a fresh capture at drawer size; the sketch dropped | OK (edit 18.9.) |
| B.2 | Ultra Gravel | live-site capture; sketch (a route drawing) as the preview | **Real product only**: Petri's capture of a planned 67 km loop around Tampere (816 m climb, 79 % gravel, elevation profile), 18.9.2026, cropped 16:9 to `docs/mockups/shots/ultragravel.png` (drawer) and `ultragravel-preview.png` (preview) | OK (18.9.) |
| B.3 | TilastoSilta | live-site capture, both | keep; a fresh capture of a chart view rather than the front page if one is reachable by URL | OK |
| B.4 | SF3D AI Lab | live-site capture, both | keep | OK |
| B.5 | ReviewGlass | sketch: a magnifier drifting over text lines | **Mockup of the real thing** (Petri 18.9.: a screenshot would need every line of text blurred): a text pane drawn as blurred lines, a rectangular viewing area (the glass) and the reading frame over the text columns, in the app's own proportions; no real text | OK (edit 18.9.) |
| B.6 | Salpa Defence | sketch: a sealed box, dots that cannot leave | **The brand mark from the Salpa brand guide** (`salpa defence/docs/salpa-brand/logo/`, copied to `docs/mockups/media/`): the horizontal logo on the brand's Kuusi `#0A1810` dark with Messinki `#C9A227` as the accent; on hover an `ACCESS DENIED` stamp appears over it, in the brand's mono register | OK (edit 18.9.) |
| B.7 | SpectralForge | the V4.5 UI screenshot in the drawer; the MasterForge sketch reused as the preview | **Real product only**: the UI screenshot (`images/product-spectralforge.webp`) in both the preview and the drawer; no sketch | OK (edit 18.9.) |
| B.8 | Drawer image size | 16:9, max 820 px | keep | OK |
| B.9 | Preview size and parking | 540 px, parked beside the plus | keep (decided in Flow 2) | OK |

## C. The cryo chamber strip

| # | Item | Now | Proposal | Status |
|---|---|---|---|---|
| C.1 | Photos in the strip | eight: LN₂ session, −234 °C, SuperPi, HWBot, Taiwan, Las Vegas, Triple Point EVO, Critical Point | keep all eight | OK |
| C.2 | Order | as above | LN₂ session, Taiwan, −234 °C, SuperPi, HWBot, Las Vegas, Triple Point EVO, Critical Point | OK |
| C.3 | Treatment | cold: desaturated, blue cast, ice captions | keep | OK |

## D. The SF3D portrait and the hero

| # | Item | Now | Proposal | Status |
|---|---|---|---|---|
| D.1 | Hero portrait | the cutout (`media/petri-cutout.webp`) | keep; export for the page at two sizes (WebP + JPG fallback) | OK |
| D.2 | Taiwan portrait | in the cryo strip only | keep it there | OK |

## E. What ships with the images

| # | Item | Proposal | Status |
|---|---|---|---|
| E.1 | Alt texts | one per image, describing the screen (rule in CLAUDE.md); written with the page edit | OK |
| E.2 | Structured data | Organization and Person only (Petri 18.9.: no SoftwareApplication entries) | OK (edit 18.9.) |
| E.3 | Open Graph image | 1200×630: the headline on the sunrise paper with the sun mark, no portrait; generated with the page assets | OK |
| E.4 | Clip weight | any clip on the page is under 4 MB, muted, autoplay only in view, with a poster; the MasterForge EQ capture (3.4 MB) fits and is copied to `docs/mockups/media/masterforge-eq.mp4` | OK |

---

## Open questions the list raises

- All decided 18.9.2026, captures in hand. Next: Flow 4 with the real plates and drawer images, reviewed as a whole page, then SEED v3.0.0.
