# The profile README against the page (session 12, side thread, 15.11.2026)

The GitHub profile README (`github.com/pkorrrhonen-cmd`, repository `pkorrrhonen-cmd/pkorrrhonen-cmd`,
last pushed 24.9.2026, `9d00a67`) read line by line against the live page and its four sub-pages,
and every state checked from the product's own repository or live site on 15.11.2026. Petri
15.11.2026: "siivotaan tämä, katsotaan tekstit yhdessä läpi ennen muokkausta", and on adr.sws.014:
"kyllä, tee tämä". This file is the list; the answers are recorded under it as they are taken.

This repository is public, so the employer's applications are never named here (adr.sws.006): the
rows say "the employer's applications".

## What was checked (15.11.2026)

| Product | Source read | Fact |
|---|---|---|
| MasterForge | masterforge.app (200), its pricing block | Free, Starter (4.99/mo), Pro (9.99/mo) and pay-per-run credits: three tiers, not four |
| SpectralForge | spectral.masterforge.app (200), the served bundle; repository `src/pages/BetaGatePage.tsx` | "SpectralForge is in closed beta": a closed beta, not a beta |
| Quaesitor | quaesitor `docs/BUILD_INFO.json` (origin/main 6a00d3e, 11.10.2026); quaesitor.app (200) | in production since 1.10.2026; the page dropped it on 18.9.2026 ("no longer developed") |
| Somnus | somnus `README.md` (origin/main 19d8bb5, 14.11.2026) | "Quaesitor V2's local, always-on cognition layer" on the home box, two AMD cards |
| Luviamo | luviamo.app (200); `docs/BUILD_INFO.json` (origin/main f8ba9fc7) | live |
| Virustutka | virustutka `README.md` (origin/main d3679ba, 12.11.2026); virustutka.app (200) | THL (clinical and wastewater) and ECDC ERVISS ingests: the README's "THL and ECDC open data" holds |
| Ultra Gravel | ultragravel `docs/BUILD_INFO.json` (origin/main 1811e2d); ultragravel.app (200) | live at ultragravel.app; the README's "Where" says only "app" |
| Salpa Defence | salpa-demo `docs/BUILD_INFO.json` (origin/main ce7828a) | the sales demo in production since August 2026 behind Access; the page says "venture" |
| kal.app | kalastus origin/main 20a7888 (1.9.2026) | not released; the page dropped it on 18.9.2026 |
| ReviewGlass | the site's check of 13.11. and 14.11.2026 (ReviewGlass 2654ab4) | the live diff is built; pre-alpha, daily use, Apache-2.0 |
| HomeTeam | the site's check of 13.11.2026; app.hometeam.fi (200) | in production for my own family since 10.10.2026; on the page since 13.11.2026, not in the README |
| VitalTrack | health.sunrisesoftware.app (200, "VitalTrack", the first version); vitaltrack `docs/BUILD_INFO.json` (origin/main d0a8c96, 12.11.2026) | the first version answers; the repository is the second version's plan since 22.10.2026, no application code |
| TilastoSilta, SF3D AI Lab | tilastosilta.fi, sf3d.fi (200) | live, as both surfaces say |
| The family map | Atlas `packages/orchestration/src/portfolio*.ts` (origin/main b9c9693, 14.11.2026); `model/systems/` | the model holds 25 systems (the README's map says 21, 24.9.2026); `pnpm portfolio --exclude` names every excluded system in its counts line and in the poster, by design |

## The list

| # | Where in the README | Now | State |
|---|---|---|---|
| GH.1 | (adr.sws.014) where the shared facts live, and in what format | nowhere: both surfaces typed by hand | open |
| GH.2 | (adr.sws.014) what the generator writes into the README | nothing is generated except the family map | open |
| GH.3 | (adr.sws.014) what `check-site` checks against the facts | nothing; the README is checked by hand each session | open |
| GH.4 | `The family, drawn from the model`: the counts line, `family-map.svg`, the system table | measured 24.9.2026 (21 systems); one table row and the counts line name the employer's applications | open |
| GH.5 | `What I build`, the closing paragraph: `Day work: ...` | names the employer's two applications | open |
| GH.6 | Quaesitor row, kal.app row, `Also live: VitalTrack` | in the README, not on the page (dropped 18.9.2026 by decision) | open |
| GH.7 | HomeTeam | on the page since 13.11.2026 (drawer and `/hometeam/`), no row in the README | open |
| GH.8 | Since AI 2026 and the AMD hackathon | on the page (section 04, `/silent-context/`), not in the README | open |
| GH.9 | MasterForge row | `AI music mastering built for the artifacts of neural-network audio. Real-time DSP engine, four tiers, paying customers since 2024.` | open |
| GH.10 | SpectralForge row | `Companion to MasterForge: diagnoses and repairs the spectral deficiencies of AI-generated and codec-damaged audio. Beta.` | open |
| GH.11 | ReviewGlass row | `Open source (Apache-2.0). A Windows 11 desktop companion for AI-assisted coding sessions: a magnifier glass over the session, a panel of every running session with the account quota, and later a live diff. Tauri v2, Rust core.` | open |
| GH.12 | Ultra Gravel and Salpa Defence rows | Ultra Gravel's `Where` is `app` (no link); Salpa: `Demo running, product in design.` | open |
| GH.13 | The second paragraph | `Two decades of extreme overclocking under the alias SF3D.` The README's own `Before software` says 2006 to 2016, and the page says ten years | open |
| GH.14 | `How I work`, the first sentence | `The whole family is held in **Atlas**, a control plane of my own:` ("control plane" is the old Atlas word, LESSONS 18.9.2026; the page says "the backbone of the work") | open |
| GH.15 | `Infrastructure`, the Somnus line | `an always-on cognition layer for Quaesitor` (follows GH.6) | open |

## Decisions

Recorded here as they are taken, one row per answer.

### Round GH-A, the big lines (15.11.2026)

| # | Question | Decision |
|---|---|---|
| GH.1 | Where the shared facts live, and in what format | `docs/facts.json` in this repository, JSON: the site's CI runs without a network and sees the file directly; JSON needs no parser, so `check-site` stays dependency-free. Never the employer's applications, as the repository is public (as recommended) |
| GH.2 | What the generator writes | the whole product table of the README between two markers: `Product · What it is · State · Where`, the same products in the same groups as the page (and any README-only row GH.6 keeps), the state in the page's own words, the descriptions from the facts file; the rest of the README stays hand-written (as recommended). So GH.7 is answered: HomeTeam gets a row, and so do Somnus and Atlas, as the page carries them; their words go to a text round |
| GH.3 | What `check-site` checks | CI: every product's status on the front page (section 02 plates, section 03 drawers) and on its sub-page matches its fact (state, year, address), and no product on the page lacks a fact. The session routine: `--readme <path>` compares the README's generated block with what the generator would write (as recommended) |
| GH.4 | The family map section | out of the README now; a session in Atlas makes a withheld system counted but not named ("2 withheld"); then the map is regenerated and comes back (as recommended) |

GH.2 changes the list: the table's rows come from the page, so four rows are added for the text rounds.

| # | Where in the README | Now | State |
|---|---|---|---|
| GH.16 | The product table's layout | one table, no groups, no state column | open |
| GH.17 | Luviamo row | `... replacing five to eight separate tools. In production.` (the state moves to the State column) | open |
| GH.18 | HomeTeam row (new) | none | open |
| GH.19 | Somnus row (new; the page's Tools and research instruments) | none; Somnus is described only under `Infrastructure` | open |
| GH.20 | Atlas row (new) | none; Atlas is described only under `How I work` | open |

### Round GH-B, what the README carries (15.11.2026)

| # | Question | Decision |
|---|---|---|
| GH.5 | The `Day work` sentence | `Day work: development manager at a rehabilitation company, building digital health software to clinical and regulatory standards.` (the page's section 01, item 03; my proposal, chosen) |
| GH.6 | Quaesitor, kal.app, `Also live: VitalTrack` | all three leave the README, so it carries the same products as the page; the Somnus line under `Infrastructure` is reworded in GH.15 (as recommended) |
| GH.8 | Since AI 2026 and the AMD hackathon | a `## Recent` section after the product table, two lines, verbatim: `- 8 Nov 2026: third of fifteen at Since AI 2026, Elisa's challenge in Turku, built alone over three days: [Silent context](https://sunrisesoftware.app/silent-context/), [the code](https://github.com/pkorrrhonen-cmd/silent-context).` and `- 18 Oct 2026: As Prescribed, for the AMD Developer Hackathon: a physiotherapy session turned into the patient's home program, every line traced back to the session. Synthetic data only, never opened to the public.` (my proposal, chosen) |
| GH.13 | The SF3D years in the second paragraph | `Twenty years in clinical physiotherapy. A decade of extreme overclocking under the alias SF3D.` and the rest of the paragraph unchanged (my proposal, chosen) |

### Round GH-C, the table and the first rows (15.11.2026)

| # | Question | Decision |
|---|---|---|
| GH.16 | The table's layout | three tables under `###` headings in the page's group names (`Commercial products`, `Tools and research instruments`, `Also in production`), each in the page's order, columns `Product · What it is · State · Where`, the state in the page's words and the address as a link (as recommended) |
| GH.9 | MasterForge row | `AI music mastering built for the artifacts of neural-network audio. Real-time DSP engine, three tiers: Free, Starter and Pro.` (my proposal, chosen). And a correction of fact, in Petri's words: "Vuosiluku laittava tähän ja myös tilastosiltaan 2026 ja nuoli eteenpäin. Kaupalliset toiminnot tai julkaisut on 2026 puolella joten käytetään sitä vuosilukuna. Kaikki tuotteet on siis 2026 puolelta." So every product's year is `2026 →`: MasterForge's state is `Live · paying customers · 2026 →`, TilastoSilta's `Live · 2026 →`, SpectralForge's `Closed beta · 2026 →`. The page still says 2024 (MasterForge, TilastoSilta) and 2025 (SpectralForge); the page is not edited in this thread, so the difference is recorded (GH.21) |
| GH.10, GH.17 | SpectralForge and Luviamo rows | the state words leave the descriptions, the rest unchanged: `Companion to MasterForge: diagnoses and repairs the spectral deficiencies of AI-generated and codec-damaged audio.` and `Marketing lifecycle platform for Nordic SMBs: one brand voice carried from ideation to publication and measurement, replacing five to eight separate tools.` (as recommended) |
| GH.11 | ReviewGlass row | `Open source (Apache-2.0). A Windows 11 desktop companion for AI-assisted coding sessions: a magnifier glass over the session, a panel of every running session with the account quota, and the agent's edits as a live diff. Tauri v2, Rust core.` (my proposal, chosen) |

GH.9's correction adds a row:

| # | Where | Now | State |
|---|---|---|---|
| GH.21 | `check-site` against the page while the page still carries the old years | the page says `2024 →` for MasterForge and TilastoSilta and `2025 →` for SpectralForge; the facts say `2026 →` | open |

### Round GH-D, the page's old years and three rows (15.11.2026)

| # | Question | Decision |
|---|---|---|
| GH.21 | How the facts check treats the page's old years | a pending difference, guarded: `docs/facts.json` records for the three products what the page says now and the decision the fix waits for (GH.9); `check-site` accepts only that old value, prints the difference on every run, and fails once the page is fixed while the record stays. The page is fixed later together with Petri (`BUILD_INFO.next`) (as recommended). On the page: `index.html` the MasterForge plate's status, the TilastoSilta and SpectralForge drawers' years; the company's `Est. 2024` and `foundingDate` are the company's and stay |
| GH.12 | Salpa Defence row | `A local AI appliance and software layer for environments cloud services cannot legally reach. Sales demo in production since August 2026; product core under way.` State `Venture · 2026 →`, Where `private demo` (my proposal, chosen) |
| GH.18 | HomeTeam row | `The application my family runs the week on: a shared Today view for the day's tasks and the family calendar, and an economy each family sets for itself.` State `In use · my own family · 2026 →`, Where `sunrisesoftware.app/hometeam` (my proposal, chosen) |
| GH.19 | Somnus row | not decided; a direction, in Petri's words: "Kuvaus on vanha ehdotuksessa ja laatassa - myös tähän somnus serverin nykykäyttö eli sama mitä jo aiemmin mietittiin listana. se on palvelin eri käyttötarpeisiin." The page's Somnus plate (its text and its drawn job list) is old as well: a page item for later. The current use read from somnus `docs/TOPOLOGIA.md` (origin/main 19d8bb5, checked on the box 14.11.2026): a Finnish language model of my own trained and served on it (the standing service on the 7900 XT, the data and training jobs on both cards); the work queue that runs the other projects' GPU jobs from Atlas between 08 and 22; the Linux CI runner for the family's repositories (since 20.10.2026); local model lanes for Atlas's decision rooms, on demand; power and heat measured on both cards. The research funnel (Tier 0 and Tier 1) was stopped on 25.10.2026 when its candidate pairs ran out. Refined in round GH-E |

### Round GH-E, Somnus and Atlas (15.11.2026)

| # | Question | Decision |
|---|---|---|
| GH.19 | Somnus row, refined | `The home server for whatever needs a GPU or an always-on machine: a Finnish language model of my own, trained and served on it; GPU jobs queued from the other projects; Linux CI for the family's repositories; local models for the decision rooms.` State `In use · home AMD box · 2026 →`, Where `sf3d.fi (lab notes)`. The language model is not named: its name is not public (my proposal, chosen) |
| GH.15 | `Infrastructure`, the Somnus line | `**Somnus**, the home node: two AMD GPUs, a Radeon AI PRO R9700 (32 GB) and a Radeon RX 7900 XT (20 GB), running llama.cpp on ROCm, reached over Tailscale. It serves whatever needs a GPU or an always-on machine, and its power and throughput are measured rather than assumed.` (my proposal, chosen) |
| GH.20 | Atlas row | `The backbone of the work: every project, every partner and every decision in one place, so nothing drifts from what matters.` (the page's plate line) State `In use · 2026 →`, Where `Access-protected · how the decision rooms work` linking `/rooms/` (as recommended) |
| GH.14 | `How I work`, the first sentence | `The whole family is held in **Atlas**, a workspace of my own: one machine-readable model of every system, module, connection and decision, and every view derived from it.` (my proposal, chosen) |

### Round GH-F, after the rebase (15.11.2026)

The rebase onto `origin/main` brought session 12's round AK, where Petri had already listed Somnus's use
today (`copy-v4-pages.md` AK.3): CI checks, audio development that moves into MasterForge, the language
factory that produces training material, a research platform for local models. That is the list his
GH-D answer meant ("sama mitä jo aiemmin mietittiin listana"). Read against `TOPOLOGIA.md` again, the
GH-E row's last clause overstated: Atlas's rooms run on Claude and Codex by default, and Somnus's local
lanes are only on demand and in trial.

| # | Question | Decision |
|---|---|---|
| GH.19 | Somnus row, again | `The home server for the computing, checking and work of every project: CI for the family's repositories, audio development that moves into MasterForge, a language factory that produces training material for a Finnish language model of my own, and a research platform for local models.` (my proposal from AK.3's words, chosen; replaces the GH-E row) |
| GH.22 | How the README reaches the profile repository | pushed to its `main` after this repository's pull request is merged, so the README's marker never names a facts file that is not on `main` (as recommended) |

### Round GH-G, Somnus against what runs (15.11.2026)

The main session read Somnus's use the same day for the Somnus video (B1) and sent it here before the
push; the two claims that mattered were read again from the repositories (somnus `TOPOLOGIA.md`: the CI
runner sees only the approved repositories and runs 08 to 22, as does the work queue; spectralforge-api
`tools/v19/README.md`: the audio instruments were copied from Somnus on 29.8.2026 and Somnus does not
develop them further, and Smart Preparation runs on SpectralForge's server). GH-F's row put the audio work
in the present and the CI over every repository; GH-E's Infrastructure line said "always-on".

| # | Question | Decision |
|---|---|---|
| GH.19 | Somnus row, a third time | `The home server for the work that needs a GPU: a language factory that produces Finnish training material, a research platform for small local models, and CI and security scans for part of the family's repositories. The audio research behind MasterForge's Smart Preparation was done on it in September 2026.` (my proposal, chosen; replaces the GH-F row) |
| GH.15 | `Infrastructure`, the Somnus line, again | `**Somnus**, the home node: two AMD GPUs, a Radeon AI PRO R9700 (32 GB) and a Radeon RX 7900 XT (20 GB), running llama.cpp on ROCm, reached over Tailscale. It runs the work that needs a GPU by day, from 8 to 22, and its power and throughput are measured rather than assumed.` (my proposal, chosen) |

The rows not named above keep their words, and their state moves to the State column: Virustutka,
Ultra Gravel (its Where becomes the link `ultragravel.app`, GH.16), TilastoSilta and SF3D AI Lab, all
`Live · 2026 →`.

## For the page, later, together with Petri

The page is not edited in this thread. Three things this list found on the page side:

1. The years (GH.9, GH.21): the MasterForge plate `Live · paying customers · 2024 →`, the TilastoSilta
   drawer `2024 →` and the SpectralForge drawer `2025 →` become `2026 →`. `docs/facts.json` carries
   them as pending until then.
2. The Somnus plate (GH.19): its text and its drawn job list describe the research funnel of
   September; the server's use today is the list in GH.19.
3. Quaesitor's reason for leaving the page (18.9.2026, "no longer developed") no longer matches its
   repository (in production since 1.10.2026, worked on until 11.10.2026). Nothing changes on either
   surface; the reason is recorded here so it is not read as a fact.
