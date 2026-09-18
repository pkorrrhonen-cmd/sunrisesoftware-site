# SUNRISESOFTWARE-SITE-SEED v2.1.0 (DRAFT)

**Project:** Sunrise Software, company website, September 2026 revision (page V4.6)
**URL:** https://sunrisesoftware.app/
**Owner:** Petri Korhonen / Sunrise Software Oy
**Based on:** SEED v2.0.0 (2026-04-18, page V4.5, design locked)
**Created:** 2026-09-17
**Status:** DRAFT. Waiting for Petri's decisions (section 7). The page is edited only together with Petri after this plan is agreed. Until then SEED v2.0.0 remains the page's spec.

---

## 0. VERSION NOTICE (v2.0.0 to v2.1.0)

A minor version: the design direction (Observatory × Atelier, Fraunces + Inter, cabinet dark, numbered sections, first person) stays as locked in v2.0.0. What changes is the content and the section hierarchy, because the page is five months behind the work:

- **Every product state is stale.** Luviamo has been in production since summer 2026 (v0.385.0 verified 16.9.2026) but the page says "Launching within the month". Quaesitor is 2.13.34 in production (9.9.2026), the page says 2.12.11. MasterForge is 4.44.0 with Starter v2 shipped 16.9.2026 and three tiers plus a service; the page describes four tiers. SpectralForge is 2.0 with a De-tone panel.
- **Atlas is absent.** Since July 2026 Atlas is the control plane of the whole family and, with the workspace and Atlas Connect (in partner use since 7.9.2026), the collaboration tool for projects. Petri named it on 17.9.2026 as the thing to show.
- **Six systems are missing** from the cabinet (Virustutka, Ultra Gravel, ReviewGlass, Salpa Defence, Somnus, Kalastus, SF3D AI Lab), while two rows (an employer application, an employer application) must go (adr.sws.006) and two (HEIJASTE, BrightFeed) have no trace in any repo.
- **The SF3D history is the largest section** on the page. Petri's instruction: its role and visibility are redesigned, smaller and further back, not removed. The shape is chosen from mockups (section 4.4). The heritage also lives at sf3d.fi.
- **No GitHub link.** The public profile is being completed in the same package (adr.sws.007).
- **No meta, no Open Graph, no structured data, no favicon.** Planned in v2.0.0 §5.3, never done.

The queued fix from v2.0.0 §7 (SF3D years 2008 to 2016 should read 2006 to 2016) is applied in whatever shape SF3D gets.

**Process rule (Petri, 17.9.2026):** nothing on the page is decided before mockup images of the change have been looked at together. Mockups are separate HTML files under `docs/mockups/`, never the live page, viewed in the browser pane at desktop and phone width and kept as screenshots. A portrait of Petri (`images/Petri.jpg`, taken 16.8.2026, added 17.9.2026) is to be used on the page; its placement is one of the things the mockups show.

---

## 1. VISION, PHILOSOPHY AND THE READER

### 1.1 Positioning (unchanged)

The Observatory × The Atelier: the cabinet of a scholar-builder. Substance before adjectives, personality from angle not ornament, the site itself a portfolio piece, no proof-seeking, first person singular.

### 1.2 The story angle (revised, proposed)

v2.0.0 opened with "Twenty years in clinics. Two decades overclocking silicon. Now building software nobody else would think to build." The clinic stays as one of the four disciplines in §01; the overclocking keeps a smaller place later on the page. The angle now leads with the present:

> *One person builds and runs a family of products with a fleet of agents doing the typing and a control plane of his own keeping every system honest. The first version ships; the product is then kept alive in production. Audio, research, marketing, public health, routing, and the machinery that holds them together.*

### 1.3 The reader we design for (new)

Two readers, the second one new:

1. **A serious buyer or collaborator** (as in v2.0.0): reads §01 and §02, writes an email.
2. **A technical reader from an execution-focused event.** Since AI (Turku) runs its 2026 hackathon on 6 to 8 November: 72 hours, over a thousand builders, partner challenges from Google for Developers, Bayer, Sandvik, Kongsberg and Valmet, and the rule "working demos only, no slide decks, no mockups". The family already prepares for it on the Atlas side (SUNRISE-KOKONAISKUVA v3 plans a reachability-graph decision before the event). A representative of such an event, or a partner company's engineer, gives the page ten seconds and asks: *what has this person shipped, is it live, can I open it, is there code, how is the work done.*

What the V4.5 page answers in those ten seconds, read on 17.9.2026 (screenshots at desktop width): a strong typographic opening about clinics and overclocking, then three products, one of them "launching within the month", then a full-height liquid-nitrogen archive with ten photographs. Nothing dated, no code link, no method, no Atlas. The reader concludes: a designer with a hobby past, status unknown.

What V4.6 must answer: four things live with links and versions, twelve more in a dated table, a GitHub link in the nav, a method block that names the toolchain and the gates, and a revision date in the footer.

### 1.4 Design review of V4.5 (17.9.2026)

**Keep.** The visual system holds up in September 2026: the Fraunces display with optical sizes, the cabinet-dark palette with a single brass accent, the numbered editorial sections, the grain and vignette, the restrained hover states, the lightbox. It does not look like a SaaS template or an AI-generated landing page, which is rarer now than in April. A re-skin would be a major version (v2.0.0 §0 rule) and nothing in the review asks for one.

**Change (hierarchy and content, not skin).**

| Finding | Effect on the reader | Change |
|---|---|---|
| The SF3D section is the largest block: 10 images, ember glow, two venture stories | The hobby reads as the main event; the page's weight (about 4 MB) is mostly there | Role and placement redesigned from mockups: smaller, later, still present (adr.sws.003, section 4.4) |
| The opening headline leads with clinics and overclocking | Ten seconds spent on the past | New headline leading with the present (section 4.1; Petri chooses between options) |
| No date anywhere except the copyright year | Staleness is invisible | Every status carries a version or a date; footer carries the revision date; CI checks it (adr.sws.004) |
| Atlas missing | The most distinctive current work is not on the page | §02.4 with a drawn schematic cover (adr.sws.005) |
| No GitHub | The technical reader has no door to the code | Nav primary link, meta row, §05, structured data (adr.sws.007) |
| No method | "How is the work done" is not answered | A "How the work is done" block under the three rules (section 4.5) |
| Mobile nav shows only "MasterForge" | On a phone the page has no navigation | Keep "Work" and "GitHub" visible at phone width |
| No meta description, OG, JSON-LD, favicon | Links shared to the page show nothing | Section 5.3 |
| Reveal animation ignores `prefers-reduced-motion` | Accessibility gap (the Atlas render harness caught the same in MasterForge) | One media query |
| §02 spec strips describe features only | The technical reader looks for the stack | Each product's strip gains one stack line |

---

## 2. PAGE ARCHITECTURE (V4.6, proposed)

```
/
├─ NAV (fixed, blur on scroll)        Work · Cabinet · Approach · Contact · GitHub ↗ (primary)
├─ §00 Opening                        headline, meta row (Principal, Location, Code, Latest release)
├─ §01 The connection                 four disciplines, one shared method (lightly revised)
├─ §02 Selected work                  MasterForge · Quaesitor · Luviamo · Atlas (new)
├─ §03 The rest of the cabinet        SpectralForge featured · twelve dated rows
├─ SF3D                               placement and shape open: alternatives A, B, C in 4.4 (mockups)
├─ §04 Approach                       three rules · How the work is done (new)
├─ §05 Correspondence                 email · elsewhere (GitHub, sf3d.fi) · colophon links
└─ FOOTER                             company, est., typeset, revised <date>, ©
```

The SF3D block moves and shrinks; whether it keeps its own section number depends on the alternative chosen (4.4). The section marks stay decorative and navigational. The portrait's place (opening or §01) is shown in the mockups.

---

## 3. VISUAL DESIGN SYSTEM

**Unchanged and normative:** SEED v2.0.0 §3.1 (typography), §3.2 (palette), §3.3 (component patterns for section heads, covers, archive rows, approach items), §3.4 (lightbox). Ember (`#D96B3A`) stays with SF3D wherever it lands, and nowhere else.

**Additions (proposed):**

- **Atlas plate (§02.4 cover).** An inline SVG in the 16:8 cover frame, drawn in the page's palette: a hairline grid, the model as a bordered plate in the middle with its figures and their date, three door boxes around it (Claude chat over remote MCP with OAuth 2.1; Claude Code over stdio and bearer; Atlas Connect, the phone app), the gates written on the connecting lines (`access/policy.json`, fail-closed; proposals, human promote, git), and a shelf of system names along the bottom. Mono labels, brass border, no fill. The lightbox learns to enlarge an inline SVG (clone the node instead of loading an image). A cleared screenshot may replace it later.
- **SF3D block.** Component depends on the alternative chosen in 4.4; each alternative is mocked up with the existing photographs and the existing `.sf3d-*` patterns from v2.0.0 §3.3.
- **Portrait.** `images/Petri.jpg` (4:3 landscape source, 16.8.2026) in the opening or beside §01; treatment as the v2.0.0 portrait pattern (16:10, subtle saturation cut, mono caption). Mocked up in both places.
- **Method block (§04, under the rules).** Four items in a two-column grid at desktop, one column at phone width: a mono label (Build, Gate, Run, Record) and one or two sentences in Inter, `--text-2`. Hairline above and below, same rhythm as the rules.
- **Status semantics.** `live` green dot (as now), `beta` and `venture` brass dot, `internal` and `service` `--text-meta` dot. Each status text carries a version or a date.
- **Reduced motion.** `@media (prefers-reduced-motion: reduce)`: reveal elements are visible with no transition; hover transforms off.
- **Focus.** `:focus-visible` outline in brass, 3 px offset, on links and the lightbox button.
- **Mobile nav.** At most 640 px: "Work" and the primary "GitHub ↗" stay visible; the rest hide as now.

---

## 4. CONTENT (proposed copy, complete)

House rules for copy: English, first person singular, no em dashes, no hero statistics, no generic adjectives, every status dated. Facts below were checked on 17.9.2026 (BUILD_INFO `sources_checked_2026_09_17`).

### 4.1 §00 Opening

Section mark: `§00   Sunrise Software Oy   /   Est. 2024   /   Revised September 2026`

Headline, three options for Petri (the italic clause is brass, Fraunces SOFT 100):

- **A (recommended):** *One builder, a fleet of* agents, *and a control plane that keeps them honest. Shipped as first versions, kept alive in production.*
- **B:** *Twenty years reading bodies. Now reading* systems, *and shipping the software they need.*
- **C:** Petri's own line.

Meta row (four cells): **Principal** Petri Korhonen · **Location** Tampere, Finland · **Code** github.com/pkorrrhonen-cmd ↗ · **Latest release** MasterForge 4.44 · 16 Sep 2026 (the last cell is updated each session; Petri decides whether to keep it, section 7 item 9).

### 4.2 §01 The connection

Title: *Four disciplines.* One shared method.

Intro: "Whatever I work on, a body, a benchmark, a codebase, a threat model, the work is the same. Find the pattern. Locate the root cause. Optimise until the system gives everything it can, stably."

1. **Psychophysical physiotherapy.** Twenty years of clinical work. A human is *one system, not a collection of parts.* Pattern recognition and root-cause reasoning are the core of clinical thinking. (unchanged)
2. **Optimisation.** First engines as a teenager, then silicon at cryogenic temperatures, now inference on a GPU box in the next room. *How much can a system give, and how stably can it give it?* Same question, different substrates. (revised: one clause on the cryogenic past, the present added)
3. **Cybersecurity & health-tech development.** My day work: *digital health software, built to clinical and regulatory standards.* Where an understanding of the human body meets an understanding of the systems that model it. (unchanged; the employer is not named, adr.sws.006)
4. **Software.** The place where all of the above applies at once, and since 2026 the place where *agents do the typing and gates do the judging.* Read the system. Find the root cause. Push past specification. (revised)

### 4.3 §02 Selected work

Title: *Four pieces of work.* Three products in production, and the control plane that runs them.

**§02.1 MasterForge** · Live · v4.44 · paying customers · 2023 → 2026
Cover: Pro Master (unchanged image).
Tagline: *AI music mastering, for problems that didn't exist a year before it shipped.*
Body 1 (unchanged): When Suno and its contemporaries arrived, the outputs carried a specific kind of brittleness: codec artifacts in the upper mids, harsh transients, collapsed stereo, a dull low end. Existing mastering tools were built for recordings from microphones, not from neural networks. They could not solve it.
Body 2 (revised): MasterForge is built around that gap. A real-time DSP engine, ToneMap with 26 driven controls, AI artifact suppression, vocal clarity stages, multiband compression, mid/side processing, stem-aware cleanup. In September 2026 the free tier was rebuilt as Starter v2: it measures the track first and derives the whole mastering chain from what it hears, with loudness-matched A/B and a mastering report on every download.
Strip: Free · Starter · Pro · one-off service | Real-time DSP in the browser | Tracks to 15 minutes, files to 400 MB | Cloudflare Pages · Stripe
Link: masterforge.app

**§02.2 Quaesitor** · Live · v2.13 · 2023 → 2026
Cover: Resonance + Assembler (unchanged image).
Tagline: *A research engine that thinks, falsifies, and verifies, in code and in arithmetic.*
Body 1 (unchanged, em dash removed): Quaesitor is built around an original mode I call the *cognitive stream*: an agent runs its own chain of thought autonomously, then falsifies its claims, verifies them with code and with computation, and refuses to repeat a question it cannot answer more strongly than before.
Body 2 (revised): The engine runs three specialised streams in parallel with a neutral assembler, falsification memory and an information-resistance engine keeping the conversation moving. Crystal Memory (PostgreSQL and pgvector) carries verified facts across sessions and an Elo tournament ranks hypotheses. Since summer 2026 a local cognition layer, Somnus, runs beside it on a home AMD GPU box over Tailscale: a generator, a falsifier, and human-gated escalation.
Strip: Resonance · three streams and an assembler | Crystal Memory · Elo tournaments | Somnus · local cognition on RDNA4 | FastAPI · Anthropic API · Hetzner
Link: quaesitor.app

**§02.3 Luviamo** · Live · v0.385 · in production since summer 2026 · 2026
Cover: landing page (unchanged image; the caption "launching within the month" changes to "Marketing, from idea to publication · live since 2026").
Tagline (unchanged): *One brand voice. The whole marketing lifecycle. Replacing five to eight separate tools.*
Body 1 (unchanged): Most businesses stitch marketing together from a growing pile of separate apps: one for planning, one for content, one for social, one for email, one for analytics, one for brand assets, one for the campaign calendar. Each one has its own login, its own subscription, and its own idea of what the brand sounds like.
Body 2 (revised): Luviamo replaces that pile with five rooms: ideate, plan, produce, publish, track. A single platform that learns the brand voice and carries it through the whole lifecycle. In production since summer 2026, billing live since August, with a marketing professional working in it daily, publishing to Facebook, Instagram and newsletters; Meta's app review for organic insights passed in August 2026 and the one for ad analytics was submitted on 17 September. Plans from Solo to Business; more channels queued. The quiet identity (birch, paper, rising sun) is deliberate: the tool should disappear into the work.
Strip: Brand voice, learned once | Facebook · Instagram · email | Solo · Team · Business | React 19 · Hono on Cloudflare Workers · D1 · R2
Link: luviamo.app
(Petri decides how much of the Meta review detail to keep, section 7 item 8.)

**§02.4 Atlas** · In production · v0.9 · 2026 → (new)
Cover: the Atlas plate (section 3).
Tagline: *The control plane. One model of every system, three doors into it, and a human gate on every change.*
Body 1: Nineteen systems is more than one head or one context window can hold. Atlas holds them as one machine-readable model: every system, module and connection with its rationale, every major decision as a record, validated in CI. A viewer renders it without spending a token. Claude Code and Claude chat read it over MCP and propose changes; a human promotes them into git.
Body 2: Since summer 2026 it is also how partners work with me. Atlas Teamwork gives a collaborator's own Claude a scoped, code-free window into their projects. Atlas Connect puts the same log on their phone: messages, a workspace with the timeline, the decisions and what is waiting on whom, shared documents, notifications within a minute. No WhatsApp, no email thread, one gate for every read and write. It has been the project channel with a partner since September 2026.
Strip: One model · 208 modules · 116 decisions (7.9.2026) | Proposals · artifacts · decisions | Teamwork · Connect | TypeScript · MCP · Cloudflare Workers · D1 · R2
Link: none public. A mono line in the link's place: "Access-protected · shown to partners".

### 4.4 §03 The rest of the cabinet

Title: *Twelve more, in brief.*

**Featured §03.0 SpectralForge** · Beta · v2.0 · 2025 →
Cover unchanged. Body (revised): Companion to MasterForge. Diagnoses and repairs the spectral deficiencies that AI-generated and codec-damaged audio carries: stuck transients, rounded attacks, missing harmonics, noise bed. A four-stage pipeline (HPS, Mel Clean, Click Repair, Transient Limiter) with per-band scoring, onset detection and attack-slope measurement, and since June 2026 a Surgical De-tone panel for standalone artifact removal. React front end on Cloudflare, FastAPI engine on Hetzner. Beta at *spectral.masterforge.app*.

**Archive table** (year | name · status | description; the name links where a public address exists):

| Year | Name · status | Description |
|---|---|---|
| 2026 → | Virustutka · live · v0.24 | Open, login-free respiratory-virus situation monitor for Finland: thirteen pathogens across twenty-three wellbeing regions from THL clinical and wastewater signals, a traffic-light state per region, opt-in email alerts. The light was redefined in September 2026 from a four-season backtest; the autumn season is on the map. Installable, works offline. virustutka.app |
| 2026 → | Ultra Gravel · live | Finland-wide gravel route planner and navigator on authoritative MML and Digiroad data rather than OSM: turn-by-turn with Finnish voice guidance, GPX and FIT export, loop planning, hill-aware routing. ultragravel.app |
| 2024 → | TilastoSilta · live | Free Finnish statistics visualisation from eight-plus public sources: semantic search, shareable SVG, CSV and PNG export. No login, no ads. Version 2 has passed its release gates; the cutover from v1 is pending. tilastosilta.fi |
| 2026 → | SF3D AI Lab · live | Independent research lab site: multi-agent cognition on AMD RDNA4, lab notes, an autonomous news agent under a hard cost cap. Carries the SF3D heritage. sf3d.fi |
| 2026 → | ReviewGlass · pre-alpha, in daily use | Windows desktop companion for AI-assisted coding sessions: a magnifier glass over any screen region, a panel of every running Claude Code session with quota and burn rate, live diff. Tauri v2, Rust. Open source (Apache-2.0) once the name is cleared. |
| 2026 → | Salpa Defence · venture | Local AI appliance and software layer for environments cloud services cannot legally reach, Finnish defence subcontractors first. The vendor never touches the customer's classified material. Sales demo in production since August 2026; product core under way. |
| 2026 → | Somnus · service | Always-on local cognition layer for Quaesitor on a home dual-GPU AMD box over Tailscale: a generator, a falsifier, Crystal Memory access and a tiered escalation pipeline with human-gated ignition. |
| 2026 → | Kalastus · phase 1 · kal.app | A falsifiable state model for stream fishing: the prediction is pre-registered before the trip, the visit is logged even when blank, and the app reports its own hit rate. The first system born inside Atlas, with CI and tests from day one. |
| 2025 → | Quaesitor Security · internal | Verification harness for security findings from any source: declared scope, cross-source deduplication, a verdict that is a function, memory of earlier verdicts. Feeds Atlas's security lens, which runs on a schedule against Luviamo and MasterForge. |
| 2023 → | HomeTeam · beta | Gamified family task system. HomeCoin economy, streaks, push notifications. home.sunrisesoftware.app |
| 2025 → | VitalTrack · beta | Personal training and health platform. TSS, NP, HR zones, PMC chart, Garmin sync. health.sunrisesoftware.app |
| (empty year cell) | Internal tools · production | Sunrise Command Center (double-entry bookkeeping, an AI secretary, service health), BreathForge Studio, MasterVideo 3D, MasterPromo, PhotoMaster, VideoForge, SongForge. Built for daily use; not for sale. |

Removed from v2.0.0: an employer application and an employer application (adr.sws.006); HEIJASTE and BrightFeed (no repo, no trace in any README on 17.9.2026; Petri confirms, section 7 item 4).

**SF3D: three alternatives to mock up (adr.sws.003, open):**

- **A. Footnote** at the end of §03: one small portrait (`sf3d-portrait-taiwan`), one paragraph, link to sf3d.fi. Smallest.
- **B. Compact strip** after §03: title "Before the software, liquid helium", the three records, three or four photographs in one row (hero LN2 session, SuperPi, HWBot, Triple Point), link to sf3d.fi. Keeps the proof, drops the ventures and the bottom row.
- **C. Shortened section** moved after §04 Approach: intro, portrait, records, the proof rail; ventures and the bottom row go. Closest to V4.5, later on the page.

Text for A (also usable as the intro of B and C): "Before the software there was ten years of extreme overclocking under the alias SF3D: liquid nitrogen, then liquid helium, on silicon that was never designed for it. World records in 3D and calculation benchmarks, a top-three ranking in the HWBot Pro League, a pre-overclocked-PC business, and an LN₂ cooling line co-designed with EK Water Blocks. The intuition it left, pressure, tolerance, the line between working and failing, is the one applied to DSP and to model outputs now. The history lives at sf3d.fi."

### 4.5 §04 Approach

Title: *Three rules.* No exceptions. The three rules are unchanged from v2.0.0 §4.5.

**How the work is done** (new block under the rules):

- **Build.** Claude Code sessions in git worktrees, one branch and one pull request each, squash-merged. The agent types; I read, decide and merge.
- **Gate.** CI is the gate, not the prompt: lint, types and tests in every repo, committed drift and render baselines in Atlas, a security lens on a schedule, forbidden strings on this page.
- **Run.** Cloudflare Pages, Workers, D1 and R2 for the web; Hetzner for Python engines and routing; a home AMD box for local inference; Tailscale between them.
- **Record.** Every repo carries a SEED, a session changelog, machine-readable build info, lessons and decision records. Atlas mirrors them; the repo is the truth.

### 4.6 §05 Correspondence

Header and body unchanged ("For serious conversations only." …). Email pete@sunrisesoftware.app.
**Elsewhere** (new, two mono links under the email): GitHub ↗ · SF3D AI Lab ↗
**Colophon links:** MasterForge · Quaesitor · Luviamo · SpectralForge · Virustutka · Ultra Gravel · TilastoSilta · GitHub

### 4.7 Footer

`Sunrise Software Oy · Tampere, Finland` · `Est. 2024 · Independent` · `Typeset in Fraunces & Inter` · `Revised 17 Sep 2026 · © 2026` (the date carries `data-revised="2026-09-17"`; CI compares it to BUILD_INFO).

---

## 5. TECHNICAL

### 5.1 Stack

Static HTML, inline CSS with custom properties, vanilla JS, Cloudflare Pages with Git integration, Google Fonts. The Vite + React migration of v2.0.0 §5.1 and §5.5 leaves the roadmap if adr.sws.008 is accepted; otherwise it stays "planned, not started" as before.

### 5.2 Performance

Targets unchanged (Lighthouse 95+, LCP under 1.8 s, CLS under 0.05). Image weight depends on the SF3D alternative; no image is removed before it is chosen. The portrait is exported as WebP with a JPG fallback at page size (the source is 740 kB). The Atlas plate is inline SVG, no request.

### 5.3 Head, SEO, sharing (all new)

- `<meta name="description">`, `<link rel="canonical">`, `theme-color`.
- Open Graph and Twitter card. OG image 1200×630 in the cabinet palette with the headline; generated with Pillow from Constantia or Cambria as a stand-in for Fraunces until a browser render with the real font is made (section 7 item 10).
- Favicon as an inline SVG data URI: a brass half-sun over a paper hairline on the base colour.
- JSON-LD: Organization (Sunrise Software Oy, Tampere, founded 2024, founder), Person (Petri Korhonen, sameAs GitHub and sf3d.fi), an ItemList of SoftwareApplication entries for the seven public products.
- `robots.txt` (allow all, disallow `/docs/`, `/source-assets/`, `/scripts/`), `sitemap.xml` (one URL with lastmod), `_headers` (nosniff, frame deny, referrer policy, permissions policy). Note that Pages serves the whole repo root, `docs/` included; robots keeps it out of search, not out of reach.

### 5.4 Analytics

Cloudflare Web Analytics still not enabled (needs a token from the dashboard). Open in BUILD_INFO.

### 5.5 Open track: statuses generated from Atlas

The site's Atlas status of 26.7.2026 recorded a pending track: generating the site's product states from Atlas `<system>.STATUS` data, and that status round was the first fill of the data source. Since then every system carries `.STATUS` and the workspace projects `.BUILD` (version in production, date verified). Two ways to keep the dated statuses of adr.sws.004 true: by hand each session (this SEED's default), or a small script that reads the Atlas facts over the connector and writes a status block into `index.html` before a commit, with CI checking that the block is not older than the newest BUILD fact. The second removes the April-to-September failure mode structurally. To decide with the plan, not before the page revision.

### 5.6 CI

`scripts/check-site.mjs` runs on pull requests and `main`: local image references exist; the required head elements exist; no em dashes in copy; forbidden strings absent (the employer, Pete Hietanen, 2008–2016, "launching within the month", "coming soon", "within the month", "recently"); footer `data-revised` equals `BUILD_INFO.updated`; the GitHub link appears at least four times. `--links` HEAD-checks external links locally. Red on V4.5 by design.

---

## 6. FOUNDER DATA (authoritative)

```
Name:       Petri Korhonen
Company:    Sunrise Software Oy, Tampere, Finland, est. 2024
Email:      pete@sunrisesoftware.app
GitHub:     github.com/pkorrrhonen-cmd (assumed; confirm)
Alias:      SF3D (extreme overclocking, 2006 to 2016; SF3D AI Lab, sf3d.fi, 2026)
Roles:      founder and principal, Sunrise Software Oy · full-stack developer ·
            physiotherapist, twenty years · development manager and data protection
            officer in digital health (employer not named on the page, adr.sws.006)
```

---

## 7. DECISIONS FOR PETRI (before the page is edited)

Recommended default in bold; "ok defaults" is a complete answer.

1. **Opening headline:** **A** (agents and control plane) · B (clinic-led, no overclocking) · C (your line).
2. **SF3D shape:** A footnote · B compact strip · C shortened section after Approach. Decided from the mockups, no default.
3. **Atlas cover:** **drawn SVG plate** · a cleared screenshot (viewer or Connect; you provide) · text-only entry without a cover.
4. **Archive rows:** **the twelve in 4.4** · remove some (Salpa Defence as a venture in progress, Somnus, Kalastus as a one-user phase 1, Quaesitor Security as internal, HomeTeam and VitalTrack if no longer maintained) · confirm that HEIJASTE and BrightFeed are dropped.
5. **GitHub address:** **github.com/pkorrrhonen-cmd** · the organisation Sunrisesoftware-app (all repos private today) · both.
6. **Photographs the chosen SF3D shape does not use:** decided with item 2, not before.
7. **adr.sws.008, React migration:** **accept, static stays** · keep planned.
8. **Luviamo wording:** **as in 4.3 with the Meta review dates** · shorter, no review detail · name the partner (not recommended without asking her).
9. **"Latest release" cell in the meta row:** **keep (updated each session)** · drop.
10. **OG image:** **Pillow stand-in now, real-font render later** · wait for the real-font render.
11. **Revision date** in the section mark of §00 as well as the footer: **both** · footer only.
12. **Portrait placement:** opening (beside the headline) · §01 (beside the four disciplines). Decided from the mockups.

---

## 8. DESIGN ITERATION LOG (continued from v2.0.0 §8)

| Version | Date | Key changes | Status |
|---|---|---|---|
| V4.5 | 2026-04-18 | Product covers, SpectralForge featured. | LOCKED, published |
| V4.6 | planned | Current product states dated; Atlas as §02.4 with a drawn plate; SF3D redesigned (shape from mockups); the portrait; twelve archive rows; method block; GitHub; head, OG, JSON-LD, favicon; reduced motion; mobile nav; CI-checked footer date. | Planned in this SEED; mockups first, then section 7, then edited together |

---

## 9. BUILD_INFO

Machine-readable state, sources checked and the open-items list live in `docs/BUILD_INFO.json`; this section only points there.

---

## 10. NEXT STEPS

1. Initial investigations finish: Atlas read once the connector works, the portrait looked at, product states as checked.
2. Mockups under `docs/mockups/` (SF3D A, B, C; portrait in the opening and in §01; the Atlas plate), looked at together in the browser pane; screenshots kept.
3. Petri answers section 7.
4. Edit `index.html` together per the accepted answers; run `node scripts/check-site.mjs`; look at the Pages preview at desktop and phone width.
5. In the same package: unused photographs (per the SF3D choice), OG image, `_headers`, `robots.txt`, `sitemap.xml`; footer date; BUILD_INFO `version` 4.6.0 and `updated`; archive SEED v2.0.0; mark this SEED "accepted, as built".
6. Mirror to Atlas: `sw-sivusto.STATUS`, proposal with adr.sws.003 to 009.
7. Fill the GitHub profile in the same package.

---

## 11. DOCUMENT RULES (from v2.0.0, still in force)

- Author name always "Petri Korhonen".
- The company name appears on the page only in the footer, the meta row and the structured data.
- No em dashes in on-site copy; en dashes only in year ranges.
- SEED version and BUILD_INFO updated at every session end.
- The page is edited only together with Petri, after planning is concluded (17.9.2026).
