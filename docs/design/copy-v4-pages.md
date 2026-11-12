# Copy for V6: the new texts (11.11.2026)

Every text that SEED v4.0.0 adds, one numbered item each, decided with Petri through decision
boxes (`decision-method.md`), four a round. **This file is the truth, the conversation is not.**
Each row carries its state: `draft` (written here, not asked yet), `decided` (the row says what),
`edit` (decided otherwise, the row says how), `dropped`.

`docs/design/copy-v3.md` stays the source of every text already on the front page. This file holds
only what is new, and when a V6 text replaces a V3 one the row names the item it replaces.

Order follows SEED v4.0.0 section 8: the front page first (PR B), then one sub-page per pull
request. The sub-page sections below carry the checked facts and the page's skeleton; their prose
is drafted in the round that builds them, from those facts and not from memory.

Rules, unchanged and binding on every page: English, first person singular, no em dashes, no
relative time, every status dated and no product version numbers, one status scale (Live, In use,
Closed beta, Pre-alpha, Venture), no hero statistics, no generic adjectives, the company name only
in the footer and the structured data, no employer's product names (adr.sws.006).

---

## A. The front page (PR B)

### A1. The nav and the head

| # | Where | Now | Proposal | State |
|---|---|---|---|---|
| 0.11 | Nav | `Sunrise Software · Products · Approach · Contact · GitHub ↗` | `Sunrise Software · Products · Recent · Approach · Contact · GitHub ↗`, Recent linking `#recent` | decided 11.11.2026 |
| 0.12 | `<head>` icons | the inline SVG data URI only | the data URI first, then `/favicon.ico`, `/icon-192.png`, `/apple-touch-icon.png`, `/site.webmanifest` | decided 11.11.2026 (the files shipped in PR A) |
| 0.13 | `<head>` robots | absent | `<meta name="robots" content="index, follow, max-image-preview:large, max-snippet:-1, max-video-preview:-1">` | decided 11.11.2026 |
| 0.14 | `og:image:alt` | absent | `Sunrise Software: Understand the human first. Then build the better product for them.` | decided 11.11.2026 |

### A2. Section 04 Recent

| # | Where | Proposal | State |
|---|---|---|---|
| 4.1 | Section mark | `§04 Recent` | decided 11.11.2026 |
| 4.2 | Section title (h2) | `What I have been building, with dates.` | decided 11.11.2026 |
| 4.3 | Section intro | none. The entries carry themselves, and an intro would repeat the title | decided 11.11.2026 |
| 4.4 | Entry 1, date | `8 Nov 2026` | decided 11.11.2026 |
| 4.5 | Entry 1, name (h3) | `Third of fifteen at Since AI 2026` | decided 11.11.2026 |
| 4.6 | Entry 1, body | `Elisa's challenge in Turku, built alone over three days with AI tools. Silent context reads a maintenance conversation and binds every claim to the words it came from, with two clocks on each one, so you can ask what was known at any moment. The code is public.` | decided 11.11.2026 |
| 4.7 | Entry 1, link | pill `Read the whole thing ↗` to `/silent-context/`; the repository link lives on that page | decided 11.11.2026, lands with that page |
| 4.8 | Entry 2, date | `18 Oct 2026` | decided 11.11.2026 |
| 4.9 | Entry 2, name (h3) | `As Prescribed, for the AMD Developer Hackathon` | decided 11.11.2026 |
| 4.10 | Entry 2, body | `Five days on the health track. It turns a physiotherapy session into the patient's home program in the patient's own language, and it checks the therapist's prescription rather than the patient: every line is traced back to the words in the session, checked against the restrictions already on file, and translated back before anyone sees it. A conflict stops the program. Synthetic data only, and it was never opened to the public.` | decided 11.11.2026 |
| 4.11 | Entry 2, link | none: there is no public surface and no public repository | decided 11.11.2026 |

Checked for 4.4 to 4.11 on 11.11.2026, from Atlas `SINCEAI-2026-HACKATHON-TAKEAWAY` v1 and the
`as-prescribed` system description, and from GitHub:

- Since AI 2026, Turku, 6 to 8 November 2026. Elisa's own top three of fifteen teams: 1. Kaiku,
  2. Knownstate, 3. Silent context. The result came on 8.11.2026. The judging criteria were
  usability, binding accuracy, time validity and overall readiness.
- `github.com/pkorrrhonen-cmd/silent-context` is public, pushed 8.11.2026; the submitted commit
  `f36d5b1` carries the tag `submission`, and the commits after it (the result, the vertical video,
  the retrospective) do not touch product code.
- As Prescribed: AMD Developer Hackathon ACT III, Health track, built 14. to 18.10.2026. Evaluation
  run 2 passed false alarms, latency and the round gate, and failed recall. Never deployed in
  public; the hosted demo was planned and not built.

Open questions for the boxes: whether the money (250 euros) is named, whether the two beaten-by
teams are named, and whether entry 2 says plainly that its recall gate failed, which the page's
own honesty rule argues for and no reader would ask for.

### A3. The HomeTeam drawer in section 03

Checked 11.11.2026 from the hometeam repository (`docs/BUILD_INFO.json`, `prod_state` verified
10.10.2026) and from the live hosts:

- In production at `app.hometeam.fi` since 29.9.2026, current build deployed 10.10.2026. Every
  production release is manual and by Petri's decision.
- **Sign-in is restricted to allowed addresses** (`ALLOWED_EMAILS`, verified 403 for any other
  address on 29.9.2026), so a visitor cannot use it. `hometeam.fi` is a landing image with
  `noindex`. On the page's scale this is `In use`, not `Live`, exactly as Somnus and Atlas are.
- What it is: the family's shared Today view (tasks, calendar, meals, shopping list), an economy
  each family sets for itself (HomeCoin or euro, weekly allowance, loan, rewards, savings goal) and
  an optional game layer. Adults sign in with an email code; children use nickname profiles on
  devices an adult has paired. Installable web app. Changes appear on the other devices at once.
- Data lives in the EU (D1 in the EU, the family's room in the EU jurisdiction). Private repository.

| # | Where | Proposal | State |
|---|---|---|---|
| 3.40 | Year | `2026 →` | decided 11.11.2026 |
| 3.41 | Name and status | `HomeTeam` · `in use · my own family` | decided 11.11.2026 |
| 3.42 | One-line description | `The application my family runs the week on.` | decided 11.11.2026 |
| 3.43 | Body | `A shared Today view for tasks, the calendar, meals and the shopping list, and an economy each family sets for itself: HomeCoin or euros, a weekly allowance, a loan, rewards, a savings goal. Adults sign in with a code sent to their address; children use nickname profiles on devices an adult has paired. A change appears on the other devices at once.` | decided 11.11.2026 |
| 3.44 | Three facts | `Installable, works on every device` · `Children sign in without an address` · `The family's data stays in the EU` | decided 11.11.2026 |
| 3.45 | Link | none. The application is behind a list of allowed addresses, and `hometeam.fi` is a landing image | decided 11.11.2026 |
| 3.46 | Image | A **drawn instrument** in the §03 style (the Today view with its coins), as with ReviewGlass and Somnus. No real family data, nothing to keep up to date, and the rule allows it where the product has no public surface | decided 11.11.2026 |

---

## B. `/silent-context/` (PR C)

Skeleton as SEED v4.0.0 section 2.1. The facts below are checked; the prose is drafted in this
page's own round.

- **Status line:** `Built 6 to 8 Nov 2026 · third of fifteen` with a date, not a state from the
  product scale: this is a result, not a product.
- **Lead medium:** `media/silent-context-916.mp4`, the vertical cut re-encoded from
  `sinceai2026/silent-context-third-place-9x16-captions.mp4` (1080x1920, 77.8 s, 15.7 MB) to
  720x1280 at 4 to 6 MB, with a poster and its burnt-in captions.
- **Body sections:** what the challenge asked; what Silent context does (a claim bound to the words
  it came from, two clocks on each claim, evidence as dated events, a policy on who may act, no
  write path to any device); what was measured (160 tests, the truth set 13 of 13, the held-out set
  one of sixteen wrong); what the winners did differently and what that taught, which is the part
  of this page that is worth more than the placing.
- **Evidence:** `github.com/pkorrrhonen-cmd/silent-context` (tag `submission`), and the
  retrospective in that repository's `docs/retrospective.md`.
- **Not on this page:** the money, the other teams' repositories, and the session cost figures.

## C. `/rooms/` (PR D)

- **Status line:** `In use · 2026 →`, because the rooms run daily in Atlas.
- **Lead medium:** `media/rooms-en.mp4` copied from `sf3d-ai-lab/media/publish/rooms-en.mp4`
  (6.2 MB, 16:9), with `rooms-en-916.mp4` (5.6 MB) for narrow layouts.
- **The names, from Atlas `ATLAS-HUONEET-KAR-ARV-20261031` v1 (31.10.2026, 28 sources):**
  multi-agent debate and model heterogeneity for the setting; blind sealed first votes, revealed
  together, then rounds; devil's advocate and dialectical inquiry for the challenger's seat
  (Schweiger, Sandberg & Ragan 1986; Schwenk 1990; Nemeth, Brown & Rogers 2001); LLM-as-a-judge and
  judge calibration, with the known leniency said plainly; pre-registration; maximin for the room's
  value; sycophancy and conformity for the failure the setting is built against.
- **The word Delphi does not appear** until a source for it is recorded in SEED v4.0.0 section 2.3
  (decided 11.11.2026), although sealed first votes revealed together and iterated rounds are that
  method's shape.
- **The honest part:** a room disagreed with the owner on about one decision in five, and the
  measurement of whether those disagreements were right is pre-registered and still waiting for
  outcomes. The page says that it waits rather than claiming a result.
- **Evidence:** the sf3d.fi articles `decision-rooms-in-a-minute`, `the-room-that-disagreed`,
  `blind-to-anything-taken-away` and `why-i-built-atlas`. The long text and the transcript stay
  there; this page does not repeat them.

## D. `/reviewglass/` (PR E)

- **Status line:** `Pre-alpha · daily use · 2026 →`, as in the drawer today.
- **Lead medium:** the §03 canvas instrument enlarged, until a capture exists.
- **Body:** the magnifier over any part of the screen, the panel of every running coding session
  with its quota and burn rate, the agent's edits as a live diff, and that the glass now knows
  which window is in front (`adr.rg.033`, 8.10.2026). Nothing leaves the machine.
- **Evidence:** `github.com/Sunrisesoftware-app/reviewglass`, Apache-2.0.

## E. `/hometeam/` (PR F)

- **Status line:** `In use · my own family · 2026 →`.
- **Lead medium:** open, the same question as item 3.46.
- **Body:** from the facts under A3, plus what the page can say about why it exists: it was built
  for one family and it runs that family's week.
- **Evidence:** none public. The page says so rather than linking a door the reader cannot open.

---

## F. The profile README, checked against the page on 11.11.2026

The session routine requires this and it has not been done since 19.9.2026. The README
(`github.com/pkorrrhonen-cmd`, last pushed 24.9.2026) differs from the page in six places. None of
them is a page change; they are listed here so the next README session has them.

| # | Difference | Which side is wrong |
|---|---|---|
| F1 | The README names the employer and two of its applications in `Day work`. The page's CI forbids the name across the whole file (adr.sws.006) | the README, and the decision is Petri's. Open since 19.9.2026 |
| F2 | The README's product table has no HomeTeam row, although HomeTeam is in its family map | the README, once the drawer lands |
| F3 | The README says `Also live: VitalTrack`. Atlas has VitalTrack founded 22.10.2026 with its architecture plan in progress, and `health.sunrisesoftware.app` answers 200 | unclear: the host answers, the Atlas record describes planning. To be settled before either surface repeats the word |
| F4 | The README carries Quaesitor; the page dropped it on 18.9.2026 by decision | neither: a decided divergence, worth a line in the next README session so it is not read as drift |
| F5 | The README's family map says 21 systems, measured 24.9.2026. Atlas listed 25 on 11.11.2026 | the README: regenerate with `pnpm portfolio` |
| F6 | Neither surface mentions Since AI 2026 or the AMD hackathon | both, until PR B lands and the README is regenerated |

---

## Decisions

Recorded here as they are taken, one row per answer.

### Round A, section 04 (11.11.2026)

| # | Question | Decision |
|---|---|---|
| A.1 | The section's heading (4.2) | **`What I have been building, with dates.`** as proposed. The mark stays `§04 Recent` |
| A.2 | Entry 1, Since AI (4.6) | **As proposed, three sentences.** The placing is in the heading and the text does not repeat it; the measured numbers stay on `/silent-context/` |
| A.3 | Entry 2, As Prescribed (4.10) | **As proposed, and the failed recall gate is not named on the front page.** The entry says what the work does; the evaluation's detail belongs to a page of its own if one is ever made |
| A.4 | The prize money and the winning teams | **Neither is named.** The placing is enough on the front page; both are in the retrospective in the `silent-context` repository |

Items 4.1 to 4.11 move from `draft` to `decided`, except 4.7 (the link to `/silent-context/`),
which stands as written and lands with that page.

### Round B, the HomeTeam drawer (11.11.2026)

| # | Question | Decision |
|---|---|---|
| B.1 | The status tag (3.41) | **`in use · my own family`**. The scale's word plus who uses it, which also says why there is no link |
| B.2 | The description and the body (3.42, 3.43) | **As proposed**, three sentences, the economy included |
| B.3 | The image (3.46) | **A drawn instrument**, the Today view with its coins, in the style of ReviewGlass and Somnus. A real capture would carry the family's own data, and a staged one would need keeping up |
| B.4 | The link (3.45) | **None.** `app.hometeam.fi` answers 403 to any address not on the list and `hometeam.fi` is a landing image, so the reader is not sent to a door they cannot open. The same answer as Salpa Defence |

### Round C, the frame and the structured data (11.11.2026)

| # | Question | Decision |
|---|---|---|
| C.1 | The nav's new item (0.11) | **`Recent`**, the same word as the section mark |
| C.2 | `og:image:alt` (0.14) | **The headline itself**: `Sunrise Software: Understand the human first. Then build the better product for them.` It is what the image says |
| C.3 | Which products get a `SoftwareApplication` entity (adr.sws.019) | **The six anyone can open**: MasterForge, Luviamo, Virustutka, Ultra Gravel, TilastoSilta, SF3D AI Lab. The entity promises an application, and the promise holds only for these. SpectralForge (closed beta), ReviewGlass (a repository), Somnus, Atlas, Salpa Defence and HomeTeam get none |
| C.4 | Where HomeTeam's drawer sits (3.40 to 3.46) | **After ReviewGlass**, so §03 keeps running from the open services to the ones built for my own use, and the two drawers without a link sit beside Salpa Defence |

**Section 04 and the HomeTeam drawer are now fully decided and ready to build as PR B**, together
with items 0.11 to 0.14 and the structured data of adr.sws.019. Nothing in section B to E of this
file has been asked yet.

### Round D, while building PR B (12.11.2026)

| # | Question | Decision |
|---|---|---|
| D.1 | SF3D AI Lab in the structured data | **`WebSite`, not `SoftwareApplication`.** Round C.3 had it as an application on my recommendation, but sf3d.fi is a research lab site and the page itself calls it one; an application entity would claim something the page does not, which adr.sws.019 forbids. Five applications remain: MasterForge, Luviamo, Virustutka, Ultra Gravel, TilastoSilta |
| D.2 | Three additions not on the list | **All three accepted:** `twitter:image:alt` with the same text as `og:image:alt`; `Organization.logo` pointing at `/icon-512.png`; `publisher` on each application pointing at the Organization, beside `author` pointing at the Person |

### How PR B was built (12.11.2026)

- Section marks keep the page's house style with a middle dot: `§04 · Recent`, and Approach and
  Correspondence renumbered to `§05 · Approach` and `§06 · Correspondence`.
- Entry 1 has no pill yet. Item 4.7 links `/silent-context/`, which does not exist until its own
  pull request, and a link to it now would answer 404. The pill lands with the page.
- Neither entry shows a poster. SEED v4.0.0 section 3.6 gives an entry with a video a poster frame,
  but the video plays on the entry's own page, which is not built yet.
- The HomeTeam instrument (item 3.46) draws a Today card with five generic tasks (no names) ticking
  off one by one, each sending a coin to a wallet with a HomeCoin count and a savings-goal bar.
  Labels in English, as the page is; the application itself is in Finnish. Its canvas carries an
  `aria-label` that describes the drawing.

