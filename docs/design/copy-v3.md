# Copy v3: every text on the page, one numbered item each

**Purpose:** the whole page's copy as a list Petri edits item by item. When every item is
marked `OK`, the copy is done and it goes into SEED v3.0.0. **Status 18.9.2026: every item is
decided (OK, edit, drop) except the ones marked `later`, which belong to the app-view round
(plate captions, the Atlas schematic's labels, the Open pill, alt texts, structured data).** Source: the copy in
`docs/mockups/flow-2.html` on 18.9.2026 (placeholder copy from the v2.1.0 content draft, dated
facts checked 17.9.2026). Type: Familjen Grotesk (display) + Public Sans (body) + JetBrains Mono
(labels), adr.sws.012.

**How to edit:** reply with the item number and the new text, or `OK`, or `drop`. Items marked
`[apps]` are the product entries; their set, order and descriptions are reworked in the
application-view round that follows this one (which apps are lifted, which are dropped: at least
kal.app and HomeTeam go), so those can wait unless a text is wrong already.

**Status legend:** `draft` (this list's proposal) · `OK` (Petri) · `edit` (Petri gave new text)
· `drop` · `later` (decided in the app-view round).

**Rules that apply to every item:** English, first person singular, no em dashes, no relative
time ("recently", "coming soon"), every status carries a version or a date, no hero statistics,
no generic adjectives, the company name only in 0.3, 0.9 and the footer.

---

## 0. Frame: nav, hero, meta

| # | Where | Text | Status |
|---|---|---|---|
| 0.1 | Browser title | `Sunrise Software · Petri Korhonen` | OK |
| 0.2 | Meta description (search and link previews) | `Software for people, built in Tampere, Finland by someone who spent twenty years understanding them: MasterForge, Quaesitor, Luviamo, Atlas and more.` | OK (edit 18.9.) |
| 0.3 | Nav wordmark | `Sunrise Software` | OK |
| 0.4 | Nav links | `Products · Approach · Contact` (Cabinet dropped from the nav; the cabinet follows the products in the same section) | OK (edit 18.9.) |
| 0.5 | Nav primary button | `GitHub ↗` | OK |
| 0.6 | Hero kicker (small line above the headline) | `Sunrise Software · Tampere, Finland · Est. 2024` (no company form) | OK (edit 18.9.) |
| 0.7 | **Headline** (the coloured clause is the emphasis) | `Understand the human first. **Then build the better product for them.**` (Petri's direction 18.9.: software for people, understanding the user, twenty years with people, not coding in a basement; version A1 chosen) | OK (edit 18.9.) |
| 0.7 alt | Rejected alternatives, kept for the record | `Software built by one person, shipped early and kept alive in production.` / `One builder, a fleet of agents, and a control plane that keeps them honest.` / `Twenty years reading bodies. Now reading systems.` / `Software for people, built by someone who spent twenty years listening to them.` / `One logic behind every product.` / `Twenty years with people, not in a basement.` | drop |
| 0.8 | Hero lede (one sentence under the headline) | `The world is open. Wherever better software is needed, from audio to public health, I build it.` (Petri's direction: broad range, open and innovative) | OK (edit 18.9.) |
| 0.9 | Meta row, four cells | `Founder · Petri Korhonen` / `Location · Tampere, Finland` / `Code · github.com/pkorrrhonen-cmd ↗` / `Latest release · MasterForge 4.44 · 16 Sep 2026` | OK (edit 18.9.: Founder) |
| 0.10 | Portrait caption | `Petri Korhonen` | OK (edit 18.9.) |

## 1. §01 The connection

| # | Where | Text | Status |
|---|---|---|---|
| 1.1 | Section mark | `§01 · The connection` | OK |
| 1.2 | Title | `Four disciplines. One shared method.` | OK |
| 1.3 | Intro | `Whatever I work on, a person, a benchmark, a codebase, a threat model, the work is the same. Understand the system first. Find the root cause. Then optimise until the system gives its best results.` (Petri 18.9.: understand the system, not the whole; no "stably") | OK (edit 18.9.) |
| 1.4 | Item 01 label | `01 · Psychophysical physiotherapy` | OK |
| 1.5 | Item 01 text | `Twenty years of clinical work with people. A human is **one system, not a collection of parts**, and understanding how they communicate is half the work.` | OK (edit 18.9.) |
| 1.6 | Item 02 label | `02 · Optimisation` | OK |
| 1.7 | Item 02 text | `Engines, then silicon at cryogenic temperatures, now inference on a GPU box in the next room. **How much can a system give, and how well can it hold it?**` (Petri 18.9.: "stably" is an irritating word to a Finn; version A) | OK (edit 18.9.) |
| 1.8 | Item 03 label | `03 · Cybersecurity & health-tech` | OK |
| 1.9 | Item 03 text | `Day work: **digital health software to clinical and regulatory standards.**` (employer not named, adr.sws.006) | OK |
| 1.10 | Item 04 label | `04 · Software` | OK |
| 1.11 | Item 04 text | `Where all of it applies at once. **Read the system. Find the root cause. Push past specification.**` (Petri 18.9.: without the agents line) | OK (edit 18.9.) |

## 2. §02 Products `[apps]`

**Structure decided 18.9.2026 (Petri):** two groups. **Commercial products:** MasterForge, then
Luviamo. **Tools and research instruments:** Somnus (the local AI server, the core of the
scientific projects, takes part in all the work; mention the AMD collaboration) and Atlas.
**Quaesitor is no longer developed and leaves the page** (its ideas live on inside Somnus). The
group labels are `Commercial products` and `Tools and research instruments` (Petri 18.9.); the
order inside them is confirmed in the app-view round. Texts below are per product.

| # | Where | Text | Status |
|---|---|---|---|
| 2.1 | Section mark | `§02 · Products` | OK (edit 18.9.) |
| 2.2 | Title | `Products people pay for, and the instruments behind them.` (Petri 18.9. evening: "control plane" was the old Atlas wording and had not been decided together; replaced) | OK (edit 18.9.) |
| **MasterForge** | | | |
| 2.3 | Plate caption (over the living cover) | `Pro Master · live meters` | later (app-view round) |
| 2.4 | Status line | `Live · v4.44 · paying customers · 2023 →` | OK |
| 2.5 | Name | `MasterForge` | OK |
| 2.6 | Tagline | `Mastering built for AI-generated music.` | OK (edit 18.9.) |
| 2.7 | Body (one paragraph) | `AI-generated music carries a brittleness microphones never had: codec artifacts, harsh transients, collapsed stereo, a dull low end. MasterForge was built for that gap, and in September 2026 its free tier was rebuilt to measure the track first and derive the whole chain from what it hears.` | OK (edit 18.9.: the two paragraphs merged) |
| 2.9 | Spec strip | `Free · Starter · Pro` / `One-click or full control` / `Runs in the browser` (no tech names) | OK (edit 18.9.) |
| 2.10 | Button | `masterforge.app →` | OK |
| **Quaesitor** | | | |
| 2.11–2.18 | The whole Quaesitor entry | (as in Flow 2) | drop (Petri 18.9.: no longer developed; Somnus is the research core now) |
| **Somnus** (new, replaces Quaesitor; group: tools and research instruments) | | | |
| 2.11 | Plate caption | `Somnus · local AI server · always on` | later |
| 2.12 | Status line | `In use · 2026 → · home AMD box` | OK |
| 2.13 | Name | `Somnus` | OK |
| 2.14 | Tagline | `The local AI server. Always on, in the next room, and part of every project.` | OK (18.9.) |
| 2.15 | Body | `Somnus runs on a machine at home: two AMD GPUs, local models, always on. It is the core of the scientific projects and takes part in all the work: it generates candidates, screens them locally for almost nothing, and hands only the best to the expensive models. What survives is remembered.` | OK (18.9.) |
| 2.16 | AMD mention | on the spec strip: `AMD R9700 sample program · white paper in progress` (exact wording, promises nothing beyond the facts) | OK (18.9.) |
| 2.17 | Spec strip | `Two AMD GPUs · 52 GB` / `Three-tier funnel · local first` / `AMD R9700 sample program · white paper in progress` | OK (18.9.) |
| 2.18 | Button (link) | `Lab notes · sf3d.fi →` | OK (edit 18.9.) |
| **Luviamo** | | | |
| 2.19 | Plate caption | `Intro · luviamo.app · muted` | later (app-view round) |
| 2.20 | Status line | `Live · v0.385 · in production since summer 2026` | OK |
| 2.21 | Name | `Luviamo` | OK |
| 2.22 | Tagline | `One brand voice. The whole marketing lifecycle. Replacing five to eight separate tools.` | OK |
| 2.23 | Body | `Five rooms: ideate, plan, produce, publish, track. A single platform that learns the brand voice and carries it through the whole lifecycle, publishing to Facebook, Instagram and newsletters. Built for Nordic small businesses.` | OK (edit 18.9.: no billing mention) |
| 2.24 | Spec strip | `Brand voice, learned once` / `Facebook · Instagram · newsletters` / `Solo · Team · Business` (no tech names) | OK (edit 18.9.) |
| 2.25 | Button | `luviamo.app →` | OK |
| **Atlas** | | | |
| 2.26 | Plate: the schematic's labels | `THE MODEL · SOURCE OF TRUTH` / `systems · modules · connections · decisions` / `19 systems · 208 modules · 175 connections · 116 ADRs` / `VALIDATED IN CI · 7.9.2026` / `every module a contract · every decision a record` / `DOOR 1 · CLAUDE CHAT` / `remote MCP · OAuth 2.1 · scoped` / `DOOR 2 · CLAUDE CODE` / `proposes, never promotes` / `DOOR 3 · ATLAS CONNECT` / `the phone app for partners` / `messages · workspace · decisions` / `policy · fail-closed` / `proposal → human → git` / `same log, same gate` / system names along the bottom | later |
| 2.27 | Status line | `In production · v0.9 · 2026 →` | OK |
| 2.28 | Name | `Atlas` | OK |
| 2.29 | Tagline | `The backbone of the work: every project, every partner and every decision in one place, so nothing drifts from what matters.` (Petri's direction 18.9.: project management and teamwork, situational awareness, library and second memory, tools to validate and build ideas, structure against drift, the link between all parties) | OK (edit 18.9.) |
| 2.30 | Body 1 | `Atlas is how the work is run. Partners and projects work inside it: who is doing what, what is waiting on whom, which decisions are open and which are made, all in one place, on the phone as well.` | OK (edit 18.9.) |
| 2.31 | Body 2 | `It is also the library and the second memory: everything built, with the reasons behind it, kept beside the code. And it carries its own tools for validating an idea and building it, so a project stays on its core instead of drifting.` | OK (edit 18.9.) |
| 2.32 | Spec strip | `Projects · partners · decisions` / `The library of everything built` / `Ideas validated before they are built` | OK (edit 18.9.) |
| 2.33 | In place of a button | `Access-protected · shown to partners` | OK |
| 2.34 | Shared micro-copy on every plate | `Open ↗` (the pill on hover) | later (with the plates) |

## 3. §03 Also in production `[apps]`

**Row set decided 18.9.2026 (Petri), to be checked once more in the app-view round:** Virustutka,
Ultra Gravel, TilastoSilta, SF3D AI Lab, ReviewGlass, Salpa Defence, SpectralForge (added; a
production tool, no longer beta). **Dropped:** Kalastus, HomeTeam, Quaesitor Security, VitalTrack.
Somnus moved up to §02. **Internal tools:** not listed (Petri 18.9.: the page shows only what others can use or read).
Each row has: year, name, status tag, one-line description, drawer paragraph, facts, link.

| # | Where | Text | Status |
|---|---|---|---|
| 3.1 | Section mark | `§03 · Also in production` | OK (edit 18.9.) |
| 3.2 | Title | `More products, tools and instruments.` (Petri 18.9. evening: "Smaller" was not decided together; "instruments" covers SpectralForge as a callable service in the MasterForge ecosystem, Salpa and the lab, same word as the §02 group) | OK (edit 18.9.) |
| **Virustutka** | | | |
| 3.3 | Row | `2026 → · Virustutka · live · v0.24 · Open, login-free respiratory-virus situation monitor for Finland.` | OK |
| 3.4 | Drawer | `Thirteen pathogens across twenty-three wellbeing regions from THL clinical and wastewater signals, a traffic-light state per region, opt-in email alerts. The light was redefined in September 2026 from a four-season backtest. Installable, works offline.` | OK |
| 3.5 | Facts | `13 pathogens · 23 regions` / `Email alerts for your region` / `Works offline, installable` | OK (edit 18.9.: no tech) |
| 3.6 | Link | `virustutka.app ↗` | OK |
| **Ultra Gravel** | | | |
| 3.7 | Row | `2026 → · Ultra Gravel · live · Finland-wide gravel route planner and navigator on authoritative data.` | OK |
| 3.8 | Drawer | `Built on MML Maastotietokanta and Digiroad rather than OSM, so gravel and small forest roads are known across the whole country. Turn-by-turn with Finnish voice guidance, GPX and FIT export, loop planning, hill-aware routing.` | OK |
| 3.9 | Facts | `Whole of Finland` / `Finnish voice guidance` / `GPX and FIT export` | OK (edit 18.9.: no tech) |
| 3.10 | Link | `ultragravel.app ↗` | OK |
| **TilastoSilta** | | | |
| 3.11 | Row | `2024 → · TilastoSilta · live · Free Finnish statistics visualisation from eight-plus public sources.` | OK |
| 3.12 | Drawer | `Semantic search over eight-plus public sources, shareable SVG, CSV and PNG export. No login, no ads.` | OK (edit 18.9.: no cutover mention) |
| 3.13 | Facts | `Eight-plus sources` / `Semantic search` / `No login, no ads` | OK (edit 18.9.: no tech) |
| 3.14 | Link | `tilastosilta.fi ↗` | OK |
| **SF3D AI Lab** | | | |
| 3.15 | Row | `2026 → · SF3D AI Lab · live · Independent research lab site: multi-agent cognition on AMD RDNA4.` | OK |
| 3.16 | Drawer | `Lab notes, an autonomous news agent under a hard cost cap, and the SF3D heritage: from world records to world models.` | OK |
| 3.17 | Facts | `Lab notes` / `Curated AI research feed` / `From world records to world models` | OK (edit 18.9.: no tech) |
| 3.18 | Link | `sf3d.fi ↗` | OK |
| **Somnus** | | | |
| 3.19 | Row | (Somnus) | moved to §02 (2.11 to 2.18) |
| **ReviewGlass** | | | |
| 3.22 | Row | `2026 → · ReviewGlass · pre-alpha · daily use · Windows desktop companion for AI-assisted coding sessions.` | OK |
| 3.23 | Drawer | `A magnifier over any part of the screen, a panel of every running coding session with its quota and burn rate, and the agent's edits as a live diff. Built for my own daily use; open source once the name is cleared.` | OK (edit 18.9.: no tech) |
| 3.24 | Facts | `Magnifier · sessions · live diff` / `Nothing leaves the machine` / `Open source, soon` | OK (edit 18.9.) |
| **Salpa Defence** | | | |
| 3.25 | Row | `2026 → · Salpa Defence · venture · Local AI appliance for environments cloud services cannot legally reach.` | OK |
| 3.26 | Drawer | `Finnish defence subcontractors first. The vendor never touches the customer's classified material. Sales demo in production since August 2026; product core under way.` | OK |
| 3.27 | Facts | `Runs inside the customer's network` / `No outbound connection` / `The vendor never sees inside` | OK (edit 18.9.: no tech) |
| **Kalastus (kal.app)** | | | |
| 3.28 | Row, drawer, facts | (as in Flow 2) | drop (Petri 18.9.: not in use) |
| **Quaesitor Security** | | | |
| 3.29–3.31 | Quaesitor Security row, drawer, facts | (as in Flow 2) | drop (Petri 18.9.) |
| **HomeTeam** | | | |
| 3.32 | Row and drawer | (as in Flow 2) | drop (Petri 18.9.: not in use) |
| **VitalTrack** | | | |
| 3.33 | VitalTrack row and drawer | (as in Flow 2) | drop (Petri 18.9.) |
| **Internal tools** | | | |
| 3.34 | Row | `Internal tools · production · Command Center, BreathForge Studio, MasterVideo 3D, MasterPromo, PhotoMaster, VideoForge, SongForge.` | drop (Petri 18.9.: the page shows only what others can use or read) |
| 3.35 | Drawer | `Built for daily use; not for sale.` | drop |
| **SpectralForge** (not in Flow 2's rows; was featured in V4.5) | | | |
| 3.36 | Row (added) | `2025 → · SpectralForge · production · v2.0 · Spectral repair for AI-generated and codec-damaged audio, companion to MasterForge.` (Petri 18.9.: a production tool, not beta) | OK |
| 3.37 | Drawer | `Repairs what AI generation and codecs break in audio, before mastering. Four repair stages and a Surgical De-tone panel for stubborn artifacts.` | OK (edit 18.9.: shorter) |
| 3.38 | Facts | `Companion to MasterForge` / `Four-stage repair pipeline` / `Surgical De-tone` | OK |
| 3.39 | Link | `spectral.masterforge.app ↗` | OK |

## 4. Before the software: SF3D and the cryo chamber

| # | Where | Text | Status |
|---|---|---|---|
| 4.1 | Section mark | `Before the software · SF3D · 2006–2016` | OK |
| 4.2 | **Heading** (visible before the button) | `Before software, I pushed silicon past its limits with liquid helium. A handful of people in the world have done that.` | OK (edit 18.9.: as a claim) |
| 4.3 | Lead (visible) | `World records, top spots in world rankings, an LN₂ cooling product line with EK Water Blocks, pre-overclocked PCs for customers. What it left is the intuition for where a system holds and where it breaks, the same one I use on software today.` (Petri's own text 18.9., grammar checked) | OK (edit 18.9.) |
| 4.4 | Button | `Open the cryo chamber` (no temperature on the button) | OK (edit 18.9.) |
| 4.5 | Chamber label | `Cryo chamber · archive` | OK |
| 4.6 | Chamber close | `Close` | OK |
| 4.7 | Chamber title | `Silicon at temperatures it was never designed for.` | OK |
| 4.8 | Chamber text, two paragraphs | (1) `Extreme overclocking is about breaking limits. Under the alias SF3D I spent ten years chasing world records with liquid nitrogen and then liquid helium at −269 °C, in competition with the best in the world, sponsored by the manufacturers and representing them at events around the world.` (2) `It was never a hobby on the side. The power delivery on today's motherboards and much of what reached the market in that decade was shaped by what we demanded of the hardware. And no desktop processor sold today runs at the 7 GHz we reached in 2010. The full story lives at sf3d.fi.` (Petri's direction 18.9. evening: breaking limits, records and competition, the technology the industry built because of us, representing the sponsors, the 7 GHz no stock desktop matches) | OK (edit 18.9.) |
| 4.9 | Records, three | `2006 – 2016 · Multiple world records in 3D and calculation benchmarks` / `2010 · First 7 GHz quad-core CPU, cooled with liquid helium` / `2012 · SuperPi 32M world record, Ivy Bridge class` | OK |
| 4.10 | Readouts, four | `Coolant · Liquid helium` / `Lowest reading · −234 °C` (measured on the chip; helium's boiling point −269 °C is in the text) / `HWBot Pro League · World #3 · 1335.90 pts` / `Principal sponsors · Intel · AMD · Asus · ASRock · Foxconn · G.Skill · Kingston · Gigabyte · MSI` | OK |
| 4.11 | Photo captions, eight | `LN₂ session` / `−234 °C` / `SuperPi 32M · 2012` / `HWBot · world #3` / `Taiwan` / `Las Vegas` / `Triple Point EVO` / `Critical Point` | OK |

## 5. §04 Approach

| # | Where | Text | Status |
|---|---|---|---|
| 5.1 | Section mark | `§04 · Approach` | OK |
| 5.2 | Title | `How the work gets done.` | OK (edit 18.9.) |
| 5.3 | Rule 01 | `Understand the person before the problem. **Every product starts with someone, not a feature list.**` | OK (edit 18.9.: rules rewritten, set A) |
| 5.4 | Rule 02 | `Get the most out of the system. **Then make it feel effortless to the person using it.**` | OK (edit 18.9.) |
| 5.5 | Rule 03 | `If it is not better than what exists, it does not ship. **Sameness is not a business model.**` | OK (edit 18.9.) |
| 5.6 | **The creed** (the big centred line) | `Imagination is the limit. Build, then enjoy the world.` (Petri's own words in Finnish 17.9.: mielikuvitus on raja, rakenna ja nauti maailmasta) | OK (18.9.) |
| 5.7 | Creed sub-line | removed | OK |
| 5.8 | Method: Build | `Claude Code sessions in git worktrees, one branch and one pull request each, squash-merged. The agent types; I read, decide and merge.` | OK |
| 5.9 | Method: Gate | `CI is the gate, not the prompt: lint, types and tests in every repo, committed drift and render baselines in Atlas, a security lens on a schedule.` | OK |
| 5.10 | Method: Run | `Cloudflare Pages, Workers, D1 and R2 for the web; Hetzner for Python engines and routing; a home AMD box for local inference; Tailscale between them.` | OK |
| 5.11 | Method: Record | `Every repo carries a SEED, a session changelog, machine-readable build info, lessons and decision records. Atlas mirrors them; the repo is the truth.` | OK |

## 6. §05 Correspondence and footer

| # | Where | Text | Status |
|---|---|---|---|
| 6.1 | Section mark | `§05 · Correspondence` | OK |
| 6.2 | Title | `Let's talk.` | OK (edit 18.9.) |
| 6.3 | Body | `If something above resembles what you need, or you have an idea worth building, write to me directly. I am always open to good ideas and new ways of doing things.` (Petri's core idea 18.9., grammar checked; "innovation" rendered as "new ways of doing things" to keep the no-generic-adjectives rule; Petri may prefer "innovation" verbatim) | OK (edit 18.9.) |
| 6.4 | Email | `pete@sunrisesoftware.app` | OK |
| 6.5 | Link list `[apps]` | `MasterForge · masterforge.app` / `Luviamo · luviamo.app` / `SpectralForge · spectral.masterforge.app` / `Virustutka · virustutka.app` / `Ultra Gravel · ultragravel.app` / `TilastoSilta · tilastosilta.fi` / `SF3D AI Lab · sf3d.fi` / `GitHub ↗` (Quaesitor out; Somnus and Atlas have no public address) | OK (edit 18.9.) |
| 6.6 | Footer left | `Sunrise Software Oy · Tampere, Finland` (the official name once on the page) | OK |
| 6.7 | Footer middle | `Est. 2024` | OK (edit 18.9.: no "Independent") |
| 6.8 | Footer right | `Revised 18 Sep 2026` (the date moves with every revision, CI checks it) | OK |

## 7. Not on the page but shipped with it

| # | Where | Text | Status |
|---|---|---|---|
| 7.1 | Open Graph title | `Sunrise Software · Petri Korhonen` | OK |
| 7.2 | Open Graph description | same as 0.2 | OK |
| 7.3 | Image alt texts | written per image when the app-view round fixes the images | later |
| 7.4 | Structured data (Organization, Person, the public products) | derived from the final app set | later |

---

## Open questions the list raises

- 3.x: the app set is decided (seven rows); the app-view round now covers how each is shown (living plates, drawer images, the Atlas schematic) and a final check of the set.
- Labels: JetBrains Mono, decided 18.9.2026 (adr.sws.012 default confirmed).
