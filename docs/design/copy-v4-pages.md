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

Skeleton as SEED v4.0.0 section 2.1. The items are numbered `SC.n` so they cannot be mistaken for
the rows of decision round B below.

**Checked on 12.11.2026** from the public repository `github.com/pkorrrhonen-cmd/silent-context`
(README, `docs/CHANGELOG.md`, `docs/hosting.md`, the tag list and the commit list), the removed
retrospective read from the repository's history (`docs/retrospective.md` at `da250e8`), Atlas
`SINCEAI-2026-HACKATHON-TAKEAWAY` v1, the video file itself, and HTTP requests:

- The challenge, in Elisa's words: *Capturing and Linking Human-Generated Contextual Metadata for
  Autonomous Network Operations*. What field engineers and network experts learn stays in their
  conversations and emails; capture it without extra work for those people, tie it to the right
  network entities with its source and period of validity, and let an agent use it the next time a
  similar case appears.
- What it does: capture from unchanged Teams and email exports (nobody writes anything down for the
  system); bind each piece of advice as a claim to graph entities, with its source, the wording of
  its scope and two clocks (when it holds in the world, when it was learned); evidence as dated
  events (told, success, failure, disputed, superseded); in a similar case the agent proposes the
  expert's step before hardware is replaced or a unit rebooted, shows the source, and says when it
  does not know. A policy on who acts: by default the agent proposes and a person acts; a reboot or
  a hardware replacement never goes to the agent; no write path to any device. When it does not
  know, it drafts the question for the person on call, who sends it. A ticket export and a Finnish
  Teams thread become the same kind of claim, in the speaker's own words and language.
- Measured: 160 tests, run without a model or a key from the recorded answers; the truth set of 13
  sources found 13 of 13; the held-out set of 16 synthetic sources the rule author never read, 1 of
  16 confidently wrong in the recorded run and 0, 0, 0, 1, 1 in five repeats. Not tested: extraction
  on real conversations, outcomes from real chat, the class binding on anything but synthetic data.
- Built alone with AI tools at the event, 6 to 8 November 2026; commit 1 (4.11.) is a scaffold made
  before it. The judged commit is `f36d5b1`, tag `submission`, 8.11.2026 09:25. MIT licence.
- The result: Elisa's own top three of fifteen, announced 8.11.2026, Silent context third. The
  reviewers held one bar: usability, linking precision, time validity, overall readiness.
- **The retrospective is no longer in the repository.** It was added on 8.11. evening and removed
  the same evening (`f1b893a`) as material made after the result and not part of the entry. The page
  cannot link it; section SC.12 is written in my own words instead.
- The hosted copy `silent-context.pkorrrhonen.workers.dev` answered 200 and `/health` answered
  `{"status":"ok"}` on 12.11.2026. It runs on Cloudflare Containers (Workers Paid), one shared
  instance kept awake by a cron, recorded answers, no model and no key; about ten seconds to wake.
- The video `sinceai2026/silent-context-third-place-9x16-captions.mp4`: 1080x1920, H.264 and AAC,
  77.8 s, 15.7 MB, captions burnt in, nine scenes. Scene 3 is a photo of the closing ceremony's big
  screen, which shows the three placings **with the other two teams' names and the prize sums**. The
  map of Finland is marked in the picture as "an illustration, not Elisa's network". The photos are
  marked "my photos".
- The event's own site is `sinceai.ai` (answers 200; `sinceai.fi` redirects there).

### SC.1 to SC.4, the head and the title block

| # | Where | Proposal | State |
|---|---|---|---|
| SC.1 | `<title>` and `og:title` | `Silent context, third at Since AI 2026 · Petri Korhonen` | decided 12.11.2026 |
| SC.2 | `description` and `og:description` | `My entry in Elisa's challenge at Since AI 2026: an agent that binds every piece of maintenance advice to the words it came from. Third of fifteen.` | decided 12.11.2026 |
| SC.3 | `og:image` and its alt | an image of its own, made in the media step; alt `Silent context: an agent that knows where its advice came from.` | decided 12.11.2026 |
| SC.4 | Subject mark (mono) | `Since AI 2026 · Elisa's challenge` | decided 12.11.2026 |
| SC.5 | h1 | `An agent that knows where its advice came from.` | decided 12.11.2026 |
| SC.6 | Lede | `Silent context reads what field engineers and network experts write to each other, binds every piece of advice to the words it came from and to the part of the network it is about, and lets an agent use it the next time the same fault appears. I built it alone over three days with AI tools, for Elisa's challenge at Since AI 2026 in Turku.` | decided 12.11.2026 |
| SC.7 | Status line | `Built 6 to 8 Nov 2026 · third of fifteen` | decided 12.11.2026 |

### SC.8, the lead medium

| # | Where | Proposal | State |
|---|---|---|---|
| SC.8 | Video block | `media/silent-context-916.mp4`, re-encoded to 720x1280 at 4 to 6 MB, with a poster; captions are in the picture, so no track. Mono caption: `The result in 78 seconds. Captions in the picture; the photos are mine, from Turku.` `aria-label`: `A vertical video: the event in Turku, the challenge, the result on the closing ceremony's screen, and what Silent context does, drawn on a map of Finland.` | decided 12.11.2026 |

### SC.9 to SC.12, the body

| # | Heading | Proposal | State |
|---|---|---|---|
| SC.9 | `What Elisa asked` | `Elisa runs a large part of Finland's telecom network, and more of it runs itself every year. What the field engineers and network experts learn about it stays in their conversations: a chat thread, an email, someone's head. The challenge was to capture that knowledge without giving those people any extra work, tie it to the right part of the network with its source and the time it holds, and let an agent use it the next time a similar case appears.` | decided 12.11.2026 |
| SC.10 | `What Silent context does` | `It reads the Teams and email exports as they are; nobody writes anything down for it. Each piece of advice becomes a claim in the expert's own words and language, tied to the units it is about, with the wording of its scope kept as it was said and two clocks: when it holds in the world, and when it was learned. Evidence arrives as dated events, so a claim can be confirmed, disputed or replaced, and you can ask what was known at any moment.` ¶ `When the same fault appears on another unit, the agent proposes the expert's step before anyone replaces hardware or reboots, shows where the advice came from, and says when it does not know. A policy decides who acts: by default the agent proposes and a person acts, a reboot or a hardware replacement never goes to the agent, and there is no write path to any device. When the agent does not know, it drafts the question for the person on call, who sends it.` | decided 12.11.2026 |
| SC.11 | `What I measured, and what I did not` | `160 tests run without a model or a key, from the recorded answers. On a truth set of 13 sources it found all 13. On a held-out set of 16 sources that the rule author never read, it bound one confidently wrong in the recorded run, and zero or one in each of five repeats. The network and most of the data are synthetic, as the challenge allowed, so none of this shows how it reads real conversations or binds in a real network.` | decided 12.11.2026 |
| SC.12 | `Why third, in my own reading` | `Elisa's reviewers judged usability first, then linking precision, time validity and overall readiness. The two entries ahead of mine each built something a person types into, running live with real models: one answers in a text box, the other lives in the chat thread the engineers already use. Mine was a page of scenes that tells the story but cannot take a question, and it ran on recorded answers so that anyone could run it without a key. I also drew the line too tightly: I built more of the network's automation, the agent that acts under a policy, and they built more of the tool the person on call holds. The jury judged the layer people touch every day. Next time I read the brief from several sides before I draw the line, and I build the live path first.` | decided 12.11.2026, no team names and no links |

### SC.13 and SC.14, evidence and structured data

| # | Where | Proposal | State |
|---|---|---|---|
| SC.13 | Evidence block | Two links, each the name over the address with one line under it. `The code` / `github.com/pkorrrhonen-cmd/silent-context` / `MIT; the tag submission is what was judged`. `Try the demo` / `silent-context.pkorrrhonen.workers.dev` / `Recorded answers, one instance shared by everyone, about ten seconds to wake` | decided 12.11.2026 |
| SC.14 | JSON-LD | a `WebPage` with `isPartOf` the WebSite and `about` the code; a `SoftwareSourceCode` for the repository (`codeRepository`, `license` MIT, `programmingLanguage` Python, `author` the Person), which the front page's graph also gains; a `VideoObject` for the page's own video (`name`, `description`, `thumbnailUrl` the poster, `contentUrl`, `uploadDate`, `duration` `PT1M18S`). adr.sws.019 amended 12.11.2026 to allow a sub-page's own video | decided 12.11.2026 |

**Not in this page's text:** the prize money, the other teams' names and repositories, and the
session cost figures. The video plays as it is: its scene 3 is my photo of the closing ceremony's
screen, which shows the three placings with the names and the sums (round G, G.1).

**Lands with this page:** the pill `Read the whole thing ↗` on the front page's entry 1 (item 4.7),
and the page's `<url>` in `sitemap.xml`.

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

### Round E, `/silent-context/`: the frame (12.11.2026)

| # | Question | Decision |
|---|---|---|
| E.1 | The h1 (SC.5) | **`An agent that knows where its advice came from.`**, what it does rather than its name or its placing. The name is in the lede and the placing in the status line |
| E.2 | The status line (SC.7) | **`Built 6 to 8 Nov 2026 · third of fifteen`**, as the skeleton had it: a result, so no word from the product scale |
| E.3 | The section on why third (SC.12) | **My own reading, no team names and no links**, as proposed. The retrospective left the repository on 8.11., so the page says it in its own words instead of pointing at it |
| E.4 | The hosted demo | **Linked**, as `Try the demo` with its limits said. The link binds the site: when the demo is switched off, the link goes in the same pull request |

### Round F, `/silent-context/`: the body (12.11.2026)

| # | Question | Decision |
|---|---|---|
| F.1 | The lede (SC.6) | **As proposed**, the name, three verbs, and who built it where and how |
| F.2 | What Elisa asked (SC.9) | **As proposed**, three sentences with Elisa's network in the first |
| F.3 | What Silent context does (SC.10) | **As proposed, two paragraphs**: what it reads and how a claim is bound; what the agent does and who acts |
| F.4 | What I measured (SC.11) | **As proposed**, the repeats included |

Round A's row A.4, and section B's evidence line as written on 11.11., said the retrospective is in
the `silent-context` repository. Both were copied from the Atlas takeaway ("the permanent version is
in the repository") and were already untrue: the file left the repository on 8.11. (`f1b893a`), eleven
minutes after the takeaway was written. The decision in A.4 stands; only its pointer was wrong
(LESSONS 12.11.2026).

### Round G, `/silent-context/`: the video and the head (12.11.2026)

| # | Question | Decision |
|---|---|---|
| G.1 | The closing ceremony's screen in the video's scene 3, with the other teams' names and the sums | **The video plays as it is.** It is my own video, published on my own channels, and the screen is the event's own. The page's text still names neither the teams nor the money |
| G.2 | The video's caption (SC.8) | **As proposed, in sentences**: `The result in 78 seconds. Captions in the picture; the photos are mine, from Turku.` |
| G.3 | `<title>` and `description` (SC.1, SC.2) | **As proposed, the result in the title**, so a search for the name or the event meets it |
| G.4 | The subject mark (SC.4) | **`Since AI 2026 · Elisa's challenge`**, as on the video's end card |

### Round H, `/silent-context/`: the share image, the evidence and the structured data (12.11.2026)

| # | Question | Decision |
|---|---|---|
| H.1 | The share image (SC.3) | **The subject mark and the h1 on the dawn sky**, in the style of the front page's image; alt `Silent context: an agent that knows where its advice came from.`, which is what the image says |
| H.2 | The evidence block (SC.13) | **The code and the demo**, each its name over its address with one line under it. The event's own site is not linked |
| H.3 | The structured data (SC.14) | **The page, the code and the video**: `WebPage`, `SoftwareSourceCode` (also on the front page) and `VideoObject`. adr.sws.019 amended so that a sub-page may describe its own video |

**`/silent-context/` is now fully decided** (SC.1 to SC.14), and ready to build as PR C once its
media exist: the video re-encoded to 720x1280 at 4 to 6 MB with a poster, and the share image.
