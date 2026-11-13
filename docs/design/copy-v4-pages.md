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
- What it is: the family's shared Today view (tasks, calendar, meals, shopping list; **corrected
  13.11.2026: meals and the shopping list are not built**, see section E), an economy
  each family sets for itself (HomeCoin or euro, weekly allowance, loan, rewards, savings goal) and
  an optional game layer. Adults sign in with an email code; children use nickname profiles on
  devices an adult has paired. Installable web app. Changes appear on the other devices at once.
- Data lives in the EU (D1 in the EU, the family's room in the EU jurisdiction). Private repository.

| # | Where | Proposal | State |
|---|---|---|---|
| 3.40 | Year | `2026 →` | decided 11.11.2026 |
| 3.41 | Name and status | `HomeTeam` · `in use · my own family` | decided 11.11.2026 |
| 3.42 | One-line description | `The application my family runs the week on.` | decided 11.11.2026 |
| 3.43 | Body | `A shared Today view for the day's tasks and the family calendar, and an economy each family sets for itself: HomeCoin or euros, a weekly allowance, a loan, rewards, a savings goal. Adults sign in with a code sent to their address; children use nickname profiles on devices an adult has paired. A change appears on the other devices at once.` | decided 11.11.2026; amended 13.11.2026 (Z.1): meals and the shopping list are not built, so they left the text |
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

Skeleton as SEED v4.1.0 section 2.1. The items are numbered `R.n`; the decision rounds for this page
are K onwards, after `/silent-context/`'s E to J.

**Checked on 13.11.2026**, in this session and not from memory:

- **The four articles**, read from the lab repository's `origin/main` (`site/content/12` to `15`) and
  each answering 200 at `sf3d.fi/blog/<slug>`:
  - `the-room-that-disagreed`, *The Room That Disagreed With Me*, 24.10.2026: the article of the
    page's video. Room R-G (`huo_52e72a47d72a441e`), 17.10.2026: the owner chose which secret scanner
    the coding workbench's security gate uses, and from its final release; the room had the scanner's
    releases page fetched, found that release did not exist yet (only a release candidate), and chose
    the same scanner on a condition (pin the release candidate and its rule file's hash together, the
    gate fails closed on anything it cannot read, move to the final release only after an acceptance
    test and a Windows measurement), at maximin `0.15` under the bar `0.6` declared in its
    pre-registration three hours before; `2 min 10 s`; the owner took the condition 41 minutes after
    the close (row 98); the gate's first commit the next day pinned the release candidate and the
    rule file's hash and fails closed (checked from the workbench repository's `origin/main`,
    commit `c392dfb`, 18.10.2026). Seats Claude and GPT, judge Jev from TypeSafe scoring arguments
    and not votes, Clef a second judge on trial and not counted.
  - `decision-rooms-in-a-minute`, 25.10.2026: the one-minute explainer, told with another room
    (R-F, 16.10.2026: plan A at `0.50` before the room, `0.03` in it, the room's condition at `0.80`;
    the maximin rule, Wald 1950).
  - `why-i-built-atlas`, 29.10.2026: Atlas as the shared record AI sessions write in and read from;
    the rooms behind its counts.
  - `blind-to-anything-taken-away`, 27.8.2026, tag `somnus`: **not about the rooms.** It is the
    Somnus audio detector that misses faults which take something away. It came into the list on
    11.11.2026 by its title; see K.3.
- **The vocabulary**, Atlas `ATLAS-HUONEET-KAR-ARV-20261031` v1 (31.10.2026, 28 sources), read in
  full: multi-agent debate, where published comparisons find debate often no better than asking one
  model several times and mixed model families doing better (Smit et al. 2024; Zhang et al. 2025);
  sycophancy and conformity as the failure; sealed first votes as Atlas's control against
  conformity; devil's advocate and dialectical inquiry better than plain consensus (Schweiger,
  Sandberg & Ragan 1986), and an assigned devil's advocate bolstering the view it attacks while a
  genuine minority did better (Nemeth, Brown & Rogers 2001); judges lenient and using a narrowed
  scale (Thakur et al. 2024; Mukherjee et al. 2026); maximin as an aggregator unlike the mean. **The
  word Delphi is not in it**, so the page does not use it (SEED section 2.3).
- **How a room is built**, from Atlas's decisions: the room with sealed first votes, pseudonymous
  seats, maximin and a separate judges' table (`adr.atlas.043`, 22.9.2026); the first measured
  confirmation room and the protocol switched on, so every recorded decision that is hard to reverse
  goes to a room, and a room that deviates sends the decision back to the owner with its reasons
  (`adr.atlas.072`, 15.10.2026); the challenger, a third seat that never votes, writes up to three
  challenges against the leading option each round, the judges read whether each bears, every seat
  answers a bearing one before its final vote, and it is the same model family as the Claude seat and
  shares its blind spots (`adr.atlas.116`, 30.10.2026; a room takes one when its queue row asks).
- **The counts**, `atlas_decision_calibration` (limit 500) read 13.11.2026 about 11.15 local: over all
  closed queue rows, rooms returned a choice on `335` decisions, confirmed `245` and deviated on
  `90` (about one in four; on 24.10.2026 it was `30` of `147`, about one in five). The first
  pre-registered check (H1, `ATLAS-HUONE-KALIBRAATIO-HYPOTEESI` v2) has read its 20 world outcomes:
  15 inside its confidence range and 5 outside, none overturned in either group, so its prediction
  did not hold and it could not separate them. The stricter H1 v4, locked 27.10.2026, counts only
  30-day outcomes recorded after the lock and had `0` of `20`; Atlas's status of 13.11. expects its
  first phase about 22.11.2026. The judges over 69 rooms with a challenger and 309 challenges: Jev
  read `272` as bearing, Clef `238`, their readings correlate at `0.28`. **These numbers are read
  again on the day the page is built**, and the page carries that day's date.
- **The videos**, ffprobe 13.11.2026. **The path in SEED section 5.2 and `BUILD_INFO.next` was
  short a folder** (both corrected 13.11.2026): the renders are `sf3d-ai-lab/media/publish/rooms/rooms-en.mp4` and
  `.../rooms/rooms-en-916.mp4`, and `media/` is ignored by the lab's git (`.gitignore` line 26), so
  they are local renders, also served at `sf3d-media.pages.dev/rooms/` (200, `video/mp4`).
  - `rooms-en.mp4`: 1920x1080, H.264 High 4.0, 30 fps, AAC 48 kHz stereo, 118.08 s (1:58),
    6 448 529 bytes.
  - `rooms-en-916.mp4`: 1080x1920, the same codecs and length, 5 855 181 bytes, the scenes laid out
    again for the vertical frame, not a crop.
  - No captions in the picture. The lab ships `site/public/video/rooms-en.vtt` (27 cues, the
    narration word for word, numbers spelled as spoken: "zero point one five").
  - Recorded 24.10.2026: room R-G replayed from its own record at four times speed, the real room in
    Atlas Connect (held in Finnish), narration in Petri's own voice generated with HeyGen from the
    script. The workbench's name **AvoQ** is on screen and in the narration; AvoQ is not on the site
    (`BUILD_INFO.next`, review-2026-11 A4); see K.4. The picture's counts (147 and 30, the first check
    at 9 of 20) are dated 24.10.2026 in the picture.
- **Not written on the page:** model version names (the families only, adr.sws.015's reason), the
  scanner's version numbers (the version guard would also catch them), token counts and costs.

### R.1 to R.7, the head and the title block

| # | Where | Proposal | State |
|---|---|---|---|
| R.1 | `<title>` and `og:title` | `Atlas decision rooms: a second opinion from AI models · Petri Korhonen` | decided 13.11.2026 (M.4) |
| R.2 | `description` and `og:description` | `Before I settle how my software is built, two AI agents from two model families argue the decision blind, two judging models score them, and I decide.` | decided 13.11.2026 (M.4) |
| R.3 | `og:image` and its alt | an image of its own, the subject mark and the h1 on the dawn sky in `og-cover.jpg`'s build (as I.2), made in the media step; alt `Atlas decision rooms: before I settle how my software is built, I ask a panel of AI models for a second opinion.` | decided 13.11.2026 (N.2) |
| R.4 | Subject mark (mono) | `Atlas · decision rooms` | decided 13.11.2026 (N.1) |
| R.5 | h1 | `Before I settle how my software is built, I ask a panel of AI models for a second opinion.` | decided 13.11.2026 (L.1) |
| R.6 | Lede | `When I have to decide how a feature or a part of my software is built, and the choice would be hard to undo, I ask my judging panel. Two AI agents from two different model families get the facts and the options, but never my choice. Each seals its first vote before it reads the other's, they argue in rounds, and two judging models score the arguments. If the panel disagrees with me, the decision comes back with its reasons, and I decide again. In Atlas, the shared record of everything I build, a panel is called a room.` | decided 13.11.2026 (L.2) |
| R.7 | Status line | `In use · 2026 →`, the sea dot of infrastructure, the same line as the Atlas plate in §02 | decided 13.11.2026 (K.2) |

### R.8, the lead medium

| # | Where | Proposal | State |
|---|---|---|---|
| R.8 | Video block | `media/rooms-en.mp4` (16:9) with a poster, `media/rooms-en-916.mp4` in the 9:16 frame on a phone, captions `media/rooms-en.vtt` from the lab as `<track kind="captions" srclang="en" label="English">`. Mono caption: `One room in two minutes: R-G of 17 Oct 2026, replayed from its own record at four times speed, with the real room in Atlas Connect. Recorded 24 Oct 2026; the narration is my voice, generated from my script.` `aria-label`: `A video: a decision about which secret scanner a security gate should use, the blind room it went to, two AI agents voting and arguing in two rounds, the room's answer on a condition, the code that followed it, and the decisions the rooms had checked by 24 Oct 2026.` | decided 13.11.2026 (M.3, the video as it is and the caption; O.1, the `aria-label`; O.3, the lab's `.vtt` as it is) |

### R.9 to R.12, the body

| # | Heading | Proposal | State |
|---|---|---|---|
| R.9 | `How a room is built` | `A room is a multi-agent debate with rules against the way such debates go wrong. Language models in a panel tend to agree with each other instead of checking each other, which the field calls sycophancy and conformity, and published comparisons find that a debate often does no better than asking one model several times, with mixed model families doing better. So the two seats come from two families, Claude and GPT, and each seals its first vote before it can read the other's; the votes are revealed together. Then come two rounds of arguments, in which a seat can have a web page fetched and kept as evidence. Between the rounds two judging models score the arguments, not the votes: Jev, a fast judging model from TypeSafe, whose score counts, and Clef, on trial, whose readings are kept but not counted.` ¶ `The room does not average its seats. It reads each option at the seat that supports it least and picks the option whose weakest support is highest. That is the maximin rule (Wald, 1950): one enthusiastic seat cannot carry an option the other barely accepts, and a low value is the room saying it is unsure.` | decided 13.11.2026 (L.3) |
| R.10 | `The room in the video` | `On 17 Oct 2026 I decided which secret scanner the security gate of my coding workbench should use, and from which release. The room had the scanner's releases page fetched and found that the release I had chosen did not exist yet, only a release candidate. It chose the same scanner on a condition: pin the release candidate and its rule file together, and let the gate refuse anything it cannot read. Its value was only 0.15, far under the bar of 0.6 written down before the room ran, so I read it as a warning rather than as the room knowing better. I took the condition 41 minutes after the room closed, and the gate's first code, the next day, was pinned exactly as the room asked.` | decided 13.11.2026 (L.4; the workbench unnamed, K.4) |
| R.11 | `The challenger` | `Since 30 Oct 2026 a room can take a third agent that never votes. Each round this challenger writes up to three objections to the option in the lead, the judges read whether each one carries weight, and both agents have to answer every one that does before their final vote. It is the devil's advocate, close to dialectical inquiry, two devices that group-decision research found better than plain consensus (Schweiger, Sandberg and Ragan, 1986). The same research carries a warning I keep in view: an assigned devil's advocate can harden the view it attacks, and a genuine minority did better (Nemeth, Brown and Rogers, 2001). My challenger also comes from the same family as one of the agents and shares its blind spots, so whether it helps is measured over the rooms, not assumed.` | decided 13.11.2026 (M.1) |
| R.12 | `What the record shows, and what it cannot` | `Every room leaves a record, and every decision it checks is counted. By 13 Nov 2026 the rooms had checked 335 of my decisions and disagreed with me on 90, about one in four. Who was right shows only when the world answers, so each outcome is recorded as it arrives. The first test I pre-registered has read its twenty outcomes: none of those decisions was overturned, so it could not tell a confident room from an unsure one. A stricter test, locked on 27 Oct 2026, counts only outcomes thirty days old, and on 13 Nov 2026 it had none. The judges need the same scrutiny: Jev found weight in 272 of 309 objections, the leniency known from work on LLM-as-a-judge, so that reading separates little. Until the outcomes come in, a room is a second opinion I can show, not one I can prove right.` (the numbers and their date read again on the build day) | decided 13.11.2026 (M.2) |

### R.13 to R.15, evidence, structured data and the front page

| # | Where | Proposal | State |
|---|---|---|---|
| R.13 | Evidence block | Two links, each the name over the address with one line under it. `The Room That Disagreed With Me` / `sf3d.fi/blog/the-room-that-disagreed` / `The room in the video, its arithmetic and its record, 24 Oct 2026`. `Decision Rooms in a Minute` / `sf3d.fi/blog/decision-rooms-in-a-minute` / `Another room in one minute, 25 Oct 2026`. Not `why-i-built-atlas` (Atlas gets a page of its own later) and not `blind-to-anything-taken-away` (Somnus, not the rooms). Atlas itself is not linked: it is access-protected | decided 13.11.2026 (K.3, the two articles; N.3, the lines) |
| R.14 | JSON-LD | a `WebPage` with `isPartOf` the WebSite and `author` the Person; a `VideoObject` for the page's own video (`name` `The Room That Disagreed With Me`, the title it was published under on sf3d.fi; `description` the decided `aria-label`; `thumbnailUrl` the poster; `contentUrl`; `uploadDate` the day the file comes to this site, as J.4; `duration` `PT1M58S`). No `SoftwareApplication`: Atlas has none on the front page (round C.3) | decided 13.11.2026 (O.2) |
| R.15 | The front page's link to this page | the plates' dark button `How the decision rooms work →` (the arrow in its `arr` span, as `Lab notes · sf3d.fi →` on Somnus) on the Atlas plate in §02, before the quiet `Access-protected · shown to partners`, which stays; the plate's own text does not change. check-site fails a sub-page the front page does not link | decided 13.11.2026 (N.4) |

## D. `/reviewglass/` (PR E)

Skeleton as SEED v4.1.0 section 2.1. The items are numbered `RG.n` (not `G.n`, which would read as
round G of `/silent-context/`). The rounds for this page are S onwards; R is skipped, because `R.n`
are the items of `/rooms/`.

**Checked on 13.11.2026**, in this session and not from memory, from the repository's `origin/main`
(`README.md`, `docs/BUILD_INFO.json` session 10 of 12.11.2026, `docs/CHANGELOG.md`, `docs/NAME-CLEARANCE.md`,
the ADR files), the GitHub API and Atlas `reviewglass.STATUS` v38 (12.11.2026):

- **What it is**, in the README's words: a Windows 11 desktop companion for Claude Code sessions. The
  glass is an always-on-top magnifier, 150 to 400 %, pixels only and no OCR (adr.rg.006), with Follow
  (a halo marks the cursor), click-lock to a Code pane (read from the app's UI Automation tree; the
  arrow keys step to the next pane), Lock here (the glass keeps its place across restarts), Lens (the
  glass rides on the cursor) and Still (the picture stops). The dock is a small always-on-top strip
  with the quota gauge and the glass's switches; its drawer holds Sessions (every running session,
  Desktop tab or terminal), Quota (the account-wide 5-hour and 7-day quota with the burn rate and a
  Windows notification before a set threshold; account quota and per-session share are never blended,
  adr.rg.007) and Diff (the agent's edits as a live `git diff` per file, grouped by session, the whole
  file around a hunk, the latest edit's lines highlighted). The diff window shows the locked pane's
  session's diff beside the glass (glued to a side of it since adr.rg.034, 11.11.2026). Explain, off by
  default, explains one selected diff hunk with a local model or a remote API and the user's own key.
- **The privacy posture**, from the README: screen pixels are read, scaled and shown, never kept or
  sent; session data comes only from files Claude Code already writes on the machine, opened
  read-only; the hook records which file an edit touched, never its content; only session state is
  read from a transcript, never the conversation; it never writes into a session, a repository or a
  transcript; no network listener, no localhost port, no IPC socket; no analytics and no accounts.
  **The front page's fact `Nothing leaves the machine` is true only while Explain's remote backend is
  off**: that backend is the one path out, triggered per hunk, with the exact payload shown before
  the first send and only the hunk and its immediate context sent.
- **Where it stands:** pre-alpha, in daily use by its author, no installer or release, no tags on
  GitHub. Phases built: the magnifier, the session panel, threshold alerts, the live diff with a
  whole-file view, the glass locked to a pane, Explain; started: the glass in other applications
  (P9, read for structure only, adr.rg.032). 36 decisions (adr.rg.001 to 036), 172 tests (CHANGELOG,
  12.11.2026). The latest three decisions (adr.rg.034 to 036, 11. and 12.11.2026) are "not yet seen by
  the owner".
- **GitHub:** `Sunrisesoftware-app/reviewglass` public, Apache-2.0, language Rust, created 11.9.2026,
  last pushed 2026-11-12T14:05Z, no releases and no tags. When it went public is recorded twice and
  differently: the repository's own README and CHANGELOG say 17.9.2026 (the owner's decision in the
  Atlas thread that day), this site's LESSONS of 19.9.2026 says the evening of 18.9.2026. The page
  needs no date for it.
- **Two open questions that bear on the page** (the repository's `BUILD_INFO.next`):
  - **The name** (adr.rg.008, still *proposed*; `docs/NAME-CLEARANCE.md` of 4.10.2026): trademark
    registers clear, but two unrelated e-commerce review services trade as ReviewGlass and hold the
    `.com` and the `.app`. Keep it, rename before the public release, or a professional search
    first is the owner's call. The release (installer, bundle id) waits for it; the source does not.
  - **AvoQ** (the owner, 11.11.2026): ReviewGlass may merge partly into AvoQ, which has already taken
    its Diff view as its own copy; the boundary is to be decided before more is built.
- **The README's independence line:** "ReviewGlass is an independent project. It is not made,
  endorsed or supported by Anthropic." It names Claude Code because it reads only the files Claude
  Code writes.
- **What the front page says today** (copy-v3 3.22 to 3.24b): row `2026 → · ReviewGlass · pre-alpha ·
  daily use · Windows desktop companion for AI-assisted coding sessions.`; body `A magnifier over any
  part of the screen, a panel of every running coding session with its quota and burn rate, and the
  agent's edits as a live diff. Built for my own daily use. Open source, Apache-2.0.`; facts `Magnifier
  · sessions · live diff` / `Nothing leaves the machine` / `Open source, Apache-2.0`; the repository
  link. Its image is a drawn instrument (apps-v3 B.5: a real capture would need every line blurred).

### RG.1 to RG.7, the head and the title block

| # | Where | Proposal | State |
|---|---|---|---|
| RG.1 | `<title>` and `og:title` | `ReviewGlass: a reading glass for AI coding sessions · Petri Korhonen` | decided 13.11.2026 (U.3) |
| RG.2 | `description` and `og:description` | `A Windows companion I built for my own Claude Code sessions: a glass that magnifies the pane I read, every session and the quota in one place, and the agent's edits as a live diff. Open source.` | decided 13.11.2026 (U.3) |
| RG.3 | `og:image` and its alt | an image of its own in I.2's build (the subject mark and the h1 on the dawn sky), made in the media step; alt `ReviewGlass: a glass for reading what the AI agent writes, while it is writing.` | decided 13.11.2026 (V.2) |
| RG.4 | Subject mark (mono) | `ReviewGlass · open source` | decided 13.11.2026 (U.4) |
| RG.5 | h1 | `A glass for reading what the AI agent writes, while it is writing.` | decided 13.11.2026 (T.1) |
| RG.6 | Lede | `When an AI agent writes code for me in Claude Code, its output runs in a narrow pane in small text that keeps moving, often in several sessions side by side. ReviewGlass sits on top of them on Windows: a glass that magnifies the pane I am reading, a small dock with every running session and how much of the account's quota is left, and each change the agent makes as a live diff. I built it for my own daily use, and the code is open.` | decided 13.11.2026 (T.2) |
| RG.7 | Status line | `Pre-alpha · daily use · 2026 →`, the sea dot, as the drawer | decided 13.11.2026 (U.1) |

### RG.8, the lead medium

| # | Where | Proposal | State |
|---|---|---|---|
| RG.8 | The lead medium | (S.3: the drawing) the §03 drawn instrument (apps-v3 B.5: blurred text columns, the reading frame, the glass) enlarged in a 16:9 frame, until a capture exists. Mono caption: `A drawing, not a capture: a real picture of the glass would show my code and my conversation.` `aria-label`: `A drawing of ReviewGlass: two columns of blurred text, a reading frame over the left one, and the glass moving along it at 220 percent.` | decided 13.11.2026 (S.3, the drawing; V.1, its caption and label) |

### RG.9 to RG.11, the body

| # | Heading | Proposal | State |
|---|---|---|---|
| RG.9 | `What it does` | `The glass is a magnifier that stays on top of everything, at 150 to 400 percent. It shows pixels and reads no text. It can follow the pointer, ride on it as a lens, or lock to one coding pane with a single click, and a button keeps it where I put it; a still keeps an instruction on screen while I work elsewhere.` ¶ `The dock is a small strip with the quota gauge and the glass's switches. Its drawer holds every running session in one table, the account's quota with its burn rate and a warning before a limit I set, and the agent's edits as a live diff, grouped by session, with the latest edit's lines marked. The locked pane's diff can also sit in its own window, glued to the side of the glass.` | decided 13.11.2026 (T.3) |
| RG.10 | `What it keeps, and what it does not` | `The pixels on the screen are read, scaled and shown, never kept or sent. Everything else comes from files the coding tool already writes on this machine, opened read-only: which file an edit touched, never the edit itself, and the state of a session, never the conversation. ReviewGlass never writes into a session or a repository, opens no network port and has no analytics or accounts. The one way out is an explanation of a single change, off by default: with a model on the same machine nothing leaves it, and with a remote one only the change I picked is sent, and the first time I see exactly what will go.` | decided 13.11.2026 (T.4) |
| RG.11 | `Where it stands` | `Pre-alpha: I use it every day, and there is no installer or release. The code is open under the Apache-2.0 licence, with every design decision and a changelog of what was measured. It works with Claude Code only, and it is my own project: Anthropic does not make, endorse or support it.` | decided 13.11.2026 (U.2) |

### RG.12 to RG.14, evidence, structured data and the front page

| # | Where | Proposal | State |
|---|---|---|---|
| RG.12 | Evidence block | One link, the name over the address with one line under it: `The code` / `github.com/Sunrisesoftware-app/reviewglass` / `Apache-2.0; the README says what it reads and what it never keeps` | decided 13.11.2026 (V.3) |
| RG.13 | JSON-LD | a `WebPage` with `isPartOf` the WebSite and `about` the code; a `SoftwareSourceCode` `#reviewglass` (`name` ReviewGlass, `description` the h1, `codeRepository`, `license` `https://www.apache.org/licenses/LICENSE-2.0`, `programmingLanguage` Rust and Svelte, `author` the Person), which the front page's graph also gains, as with Silent context | decided 13.11.2026 (W.1) |
| RG.14 | The front page's link to this page | in the ReviewGlass drawer, before the repository link, a link `How the glass works →` to `/reviewglass/`, in the words of the Atlas plate's button; the drawer's text does not change | decided 13.11.2026 (V.4) |
| RG.15 | The front page's drawer fact (copy-v3 3.24) | `Nothing leaves the machine` becomes `Screen pixels never leave the machine`, which holds without an exception; lands with this page | decided 13.11.2026 (S.4) |

## E. `/hometeam/` (PR F)

Skeleton as SEED v4.1.0 section 2.1, the frame of `/reviewglass/`. The items are numbered `HT.n` (not `H.n`,
which would read as round H of `/silent-context/`). The rounds for this page are Y onwards, then
AA, AB and so on.

**Checked on 13.11.2026**, in this session and not from memory, from the hometeam repository's
`origin/main` `1c98b23` (last changed 10.10.2026): `docs/BUILD_INFO.json` (`prod_state`, verified
10.10.2026), `docs/product.md`, `docs/v1-reference.md`, `docs/BACKLOG.md`, `docs/architecture.md`,
`mockups/README.md`, and the code (`apps/web/src/routes.tsx`, `moduleOptions.ts`, `i18n.ts`,
`apps/api/src/family/index.ts`); the hosts `app.hometeam.fi` and `hometeam.fi` answer 200.

- **In production** at `app.hometeam.fi` since 29.9.2026, the current build deployed 10.10.2026 by
  Petri's decision. Only allowed addresses can sign in (`ALLOWED_EMAILS`). Private repository.
- **Built and in production:** sign-in with an email code, the family's guided set-up, a second
  adult by invitation or QR code, a child's phone paired by QR code (nickname, avatar, colour, no
  PIN); tasks with a weekly rhythm and flexible turns, a child's own task, the child's Today as large
  cards (a tap and a confirmation, two taps); Wallet with HomeCoins that carry a euro value or plain
  euros (chosen at set-up), withdrawal to euros, a loan paid back from half of the earnings, rewards,
  a weekly allowance, a savings goal, extra work; the adult's "waiting for you"; changes on the other
  devices at once; Web Push notifications; 13 themes and two shells (Kliini and Comic); the calendar
  with week numbers, repeats, reminders and a child's entry waiting for an adult's approval
  (6.10.2026); the electricity price card (6.10.2026); the amusement park with the wheel, once a day
  (6.10.2026); the weekly scoreboard with the adults' work (8.10.2026); the treasure island
  (8.10.2026); the bridge: a parent's message to the children from ready-made blocks, mood and the
  family's mood map (8.10.2026).
- **Not built:** meals and the shopping list. `/ruoka` is a "coming soon" placeholder in the router,
  the shopping list has a module switch but no page, and both are in the backlog under "later"
  (KOORD-2, KOORD-3). **The front page's drawer (3.43, live since 12.11.2026) named both**: the A3
  check of 11.11. read the product description, which is the plan, and not what is built.
  Corrected the same day in its own pull request (Z.1; LESSONS 13.11.2026).
- **Why it exists** (`product.md`, `v1-reference.md`): an earlier version, V1, ran the family's
  tasks, wallet and calendar until 24.9.2026, when it was taken down because it was open without
  sign-in. What V1 taught: the children lost interest in collecting coins after about two months, so
  V2 rests on what keeps its value (real money, a shared goal, content that changes, being useful
  beyond points); small lists and icons and a muddled structure made V1 heavy to use, so V2 caps a
  routine entry at two taps and every interface change starts as a mockup. The first nine mockups
  went to the family as clickable prototypes on their own phones (27.9.2026), and every member
  answered, the children included; later mockups were decided by Petri.
- **Data:** the directory database and each family's room are in the EU jurisdiction.

### HT.1 to HT.7, the head and the title block

| # | Where | Proposal | State |
|---|---|---|---|
| HT.1 | `<title>` and `og:title` | `HomeTeam: the application my family runs the week on · Petri Korhonen` | decided 13.11.2026 (AB.1) |
| HT.2 | `description` and `og:description` | `A family application I built for my own family: the day's tasks and the calendar in one Today view, and children's money that works like money, with a weekly allowance, a loan and a savings goal. In use since September 2026.` | decided 13.11.2026 (AB.2) |
| HT.3 | `og:image` and its alt | an image of its own in the build of the other pages (the subject mark and the h1 on the dawn sky); alt the h1 | decided 13.11.2026 (AC.1) |
| HT.4 | Subject mark (mono) | `HomeTeam · my own family` | decided 13.11.2026 (AB.3) |
| HT.5 | h1 | `The application my family runs the week on. My children voted on how it looks.` | decided 13.11.2026 (Z.2) |
| HT.6 | Lede | `HomeTeam keeps my family's week in one place. The children see what needs doing today and what it earns them, the adults see the whole week, and the children's money works like money: a weekly allowance, a loan to pay back, a goal to save for. I built it for my own family, and the family tried the first designs on their own phones and voted on them.` | decided 13.11.2026 (Z.3) |
| HT.7 | Status line | `In use · my own family · 2026 →`, as the drawer | decided 11.11.2026 (B.1) |

### HT.8, the lead medium

| # | Where | Proposal | State |
|---|---|---|---|
| HT.8 | The lead medium | (Y.1) the child's Today and the adult's Today side by side, cut from mockup 011 (Comic). Mono caption: `Design mockups, not captures: a child's Today and a parent's, in Finnish as the application is. A capture would show my family's own week.` Alt, child: `A phone screen in a comic style: a greeting, a progress bar and six task cards on coloured notes, each with its coin value.` Alt, adult: `A phone screen in the same style: the children's progress as three cards and the day's tasks with their check marks.` | decided 13.11.2026 (Z.4) |

### HT.9 to HT.12, the body

| # | Heading | Proposal | State |
|---|---|---|---|
| HT.9 | `What it does` | `Today is the first screen. A child sees the day's tasks as large cards: a tap and a confirmation mark one done, and its coins go straight to the child's wallet. A parent sees how far each child has got and what is waiting for an adult. The calendar holds the family's week with week numbers, and an entry a child adds waits for a parent's approval.` ¶ `Each family sets its own economy: coins with a euro value or plain euros, a weekly allowance, a loan paid back from earnings, rewards to save for and a savings goal. On top sits a game layer the family can switch on: a weekly scoreboard where the adults' housework counts too, a treasure island that rises from the sand as tasks get done, and a wheel to spin once a day.` | decided 13.11.2026 (AA.1) |
| HT.10 | `Why it exists` | `HomeTeam replaced an earlier version my family used. Two lessons from it shaped this one. The children lost interest in collecting points after about two months, so this version rests on things that keep their value: real money, a shared goal and content that changes. And small lists and icons made the old one heavy to use, so here a routine task takes two taps, and every screen starts as a mockup.` ¶ `The first designs went to the family as clickable prototypes on their own phones, and everyone voted, the children included.` | decided 13.11.2026 (AA.2) |
| HT.11 | `Where it stands` | `In use by my family since 29 September 2026. Only the addresses I have allowed can sign in, so there is no public way in, and the code is in a private repository. The family's data is kept in the EU. The application is in Finnish.` | decided 13.11.2026 (AA.3) |
| HT.12 | The row of three (Y.1), a mono caption under each | Wallet (005): `Wallet: the balance in coins and euros, a savings goal, every coin in and out.` Scoreboard (019): `The week's scoreboard: the whole family on one podium, the adults included.` Treasure island (020): `The treasure island: a chest rises from the sand as the tasks get done.` Alts describe each screen | decided 13.11.2026 (AA.4) |

### HT.13 to HT.16, evidence, structured data, credits and the front page

| # | Where | Proposal | State |
|---|---|---|---|
| HT.13 | Evidence block | No link. One line in the block's place: `No public link: the application admits only my family's addresses, and its code is private.` | decided 13.11.2026 (AB.4) |
| HT.14 | JSON-LD | a `WebPage` with `isPartOf` the WebSite, and nothing else: HomeTeam gets no `SoftwareApplication` (C.3), as no reader can open it | decided 13.11.2026 (AC.2) |
| HT.15 | The front page | the drawer gains a link `How my family uses it →` to `/hometeam/`, in the words of `How the glass works →`; its drawing becomes screen 1 (Y.4) with the caption `hometeam · a child's today, a design mockup`; the image's alt as the page's lead (HT.8, the child's screen); its body (3.43) already corrected on 13.11.2026 in its own pull request (Z.1) | decided 13.11.2026 (AC.3) |
| HT.16 | Credits | one mono line under the row of three: `Typefaces in the mockups: Bangers, Gochi Hand, Patrick Hand (SIL Open Font License). 3D images: Microsoft Fluent Emoji (MIT).` The name `Microsoft Fluent Emoji` links to `github.com/microsoft/fluentui-emoji` (MIT, read 13.11.2026) | decided 13.11.2026 (AC.4) |

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

Re-checked on 13.11.2026 for PR C: the README is unchanged since 24.9.2026 (last push) and still names neither
Silent context nor Since AI 2026, while the page has had section 04 since 12.11. and now has `/silent-context/`.
F6 is therefore the README's side alone. No page change; it waits for the next README session.

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

### Round I, `/silent-context/`: the media and the video's place (13.11.2026)

Shown with `docs/mockups/silent-context/round-I-media.jpg` (the three poster frames and the share
image draft side by side).

| # | Question | Decision |
|---|---|---|
| I.1 | The video's poster (SC.8) | **B, the opening frame at 1.5 s**: my photo of the hall in Turku under the video's own title `What I built at Since AI`. It reads as a video and invites the press. Its burnt-in caption is mid-sentence, as the video's captions always are. Not A (the end card repeats the title block and looks empty in a 420 px frame), not C (small text) |
| I.2 | The share image (SC.3) | **As drafted**: the wordmark, the subject mark in its own mono, the h1 with its second clause `where its advice came from.` in `--sun-deep`, and the address `sunrisesoftware.app/silent-context/` at the foot, on the dawn sky, exactly the build of `og-cover.jpg`. Rendered with the site's own fonts (Familjen Grotesk, JetBrains Mono); the front page's image was made with Bahnschrift as a stand-in on 18.9.2026. Source `docs/mockups/og-silent-context.html` |
| I.3 | The video block's layout | **9:16 at every width**: the vertical frame at most 420 px wide, centred in the 820 px column under the title block, the mono caption under it. A 16:9 frame would shrink a vertical video to a strip between black bars. SEED v4.0.0 section 3.6 already gives a phone this frame; on this page the desktop gets it too, because there is no 16:9 cut |
| I.4 | The front page's entry 1 | **The pill only**, as item 4.7 decided. SEED section 3.6 is narrowed: an entry shows a 16:9 poster only when its video is 16:9; a vertical video gets no thumbnail on the front page, and section 04 stays a column of text rows |

### Round J, `/silent-context/`: the page as built (13.11.2026)

Shown with `docs/mockups/silent-context/round-J-page.jpg` (the built page at 1440 px and at 375 px)
and on the local server. Four choices made while building, none of them in SC.1 to SC.14:

| # | Question | Decision |
|---|---|---|
| J.1 | The shore of a sub-page | **As built**: the water, the pill `← Back to the front page` and the footer line, nothing else. The page ends in its evidence and the way back; the contact is one click away on the front page's shore, and the same text is not written twice |
| J.2 | The layout | **As built**: the 820 px column on the left edge of `.wrap`, on the line of the wordmark and the front page's headings, the video centred in the column. Under 420 px the nav shows only the sun mark, because the wordmark and `← Back to the front page` do not fit on one row; the mark still goes home and rises as the page scrolls |
| J.3 | The status line's dot | **The sun** (`--sun` with a `--sun-soft` ring). The line is a result, not a word from the product scale (E.2), so it does not wear the green dot of a live product |
| J.4 | The video's structured data | **As built**: `name` `What I built at Since AI`, the video's own title card; `description` the decided `aria-label`; `uploadDate` `2026-11-13`, the day the file comes to this site (to be moved if the merge moves) |

### How PR C was built (13.11.2026)

- The media: `media/silent-context-916.mp4` re-encoded from
  `sinceai2026/silent-context-third-place-9x16-captions.mp4` with ffmpeg (720x1280, H.264 High 3.1,
  CRF 25, BT.709, AAC 128 kb/s, faststart): 5.55 MB for 77.8 s. Small mono labels in the picture
  checked readable at this size. The poster `media/silent-context-916-poster.jpg` is the source frame at
  1.5 s scaled to 720x1280 (I.1). The share image `images/og-silent-context.jpg` is
  `docs/mockups/og-silent-context.html` rendered by `docs/mockups/shoot.py` at 1200x630 (I.2).
- The page `silent-context/index.html` copies the front page's frame (palette, sky, nav, reveals,
  the reading light, the shore) and only what it uses. Paths to images and media start from the root
  (`/media/...`), so the page needs a server to preview; `file://` does not show its media.
- Every text on the page is SC.1 to SC.14 verbatim. The evidence addresses carry no `↗`, because SC.13
  has none.
- The front page gains the pill on entry 1 (item 4.7, a static pill in the §02 pill's look) and the
  `SoftwareSourceCode` entity, the same `@id` as on the sub-page. Its footer and the sitemap move to
  13.11.2026, and the sitemap names the new page.
- `scripts/check-site.mjs` now checks every page the sitemap names (local files from the page's own
  directory or from the root, the head, a canonical to the page's own address, JSON-LD that parses,
  em dashes, version numbers, forbidden strings, the footer date against the page's own `lastmod`),
  fails when a sub-page on disk is missing from the sitemap or not linked from the front page, and
  wants a sub-page's back button. Tried against a broken copy: it caught all five planted faults.
  `--links` asks with GET when a host refuses HEAD (the demo answers 405 to HEAD, 200 to GET).

### Round K, `/rooms/`: the frame (13.11.2026)

| # | Question | Decision |
|---|---|---|
| K.1 | The h1 (R.5) | **Edit.** Not `Before AI builds something hard to undo, ...`: the page must not read as if the building were done by AI, even where AI writes the code, because the work is done to a structure. The text has to be very easy to grasp. Petri's direction, in his words: before I decide how a feature or a part of the software is to be built, I ask for second opinions from my judging panel, where two agents from different families and two judging models give their opinion. Three versions in round L |
| K.2 | The status line (R.7) | **`In use · 2026 →`**, as the skeleton and the Atlas plate on the front page |
| K.3 | The evidence (R.13) | **The two room articles only**: `the-room-that-disagreed` and `decision-rooms-in-a-minute`. `blind-to-anything-taken-away` is the Somnus audio detector and came into the list on 11.11.2026 by its title; SEED section 2.2 corrected the same day (LESSONS 13.11.2026). `why-i-built-atlas` stays off this page because **Atlas needs a sub-page of its own, and so does Somnus**: on the front page both are listed as products, but their drawn instruments and their stories do not make anyone understand them. Their texts and the products themselves are assessed as a separate piece of work when its time comes (`BUILD_INFO.next`) |
| K.4 | The workbench's name (R.10) | **Not named in the page's text**: `my coding workbench`. The video plays as it is, with AvoQ on screen and in the narration, as with G.1; the name comes to the site only when AvoQ's place on it is decided |

### Round L, `/rooms/`: the h1, the lede and the first two sections (13.11.2026)

| # | Question | Decision |
|---|---|---|
| L.1 | The h1 (R.5), three versions in K.1's direction | **`Before I settle how my software is built, I ask a panel of AI models for a second opinion.`** "Settle" rather than "decide", because the room checks a choice I have already made, blind, and I decide again when it disagrees. Not "every hard decision ..." and not the whole panel in the h1 |
| L.2 | The lede (R.6) | **The panel first**, as proposed: when I ask, who sits on the panel, what they do, what happens when they disagree, and last why the page speaks of rooms |
| L.3 | How a room is built (R.9) | **Two paragraphs with the field's names**, each after a plain sentence: sycophancy and conformity, two model families, sealed first votes, the two judges with Clef said to be on trial and not counted, and the maximin rule (Wald, 1950) |
| L.4 | The room in the video (R.10) | **The whole story**, with the workbench unnamed. The bar is "written down before the room ran" instead of the word pre-registration |

R.1 to R.3 were drafted around the first h1 and are redrafted from L.1 before they are asked.

### Round M, `/rooms/`: the challenger, the record, the video and the head (13.11.2026)

| # | Question | Decision |
|---|---|---|
| M.1 | The challenger (R.11) | **Its own section, with the names and the warning**: what the challenger does, the devil's advocate and dialectical inquiry (Schweiger, Sandberg and Ragan, 1986), Nemeth, Brown and Rogers (2001) on the assigned devil's advocate, and the challenger's own blind spot |
| M.2 | What the record shows (R.12) | **The numbers and their limits**: the counts, the first pre-registered test and why it could not separate, the stricter test, and the judge's leniency in one number. The numbers and the date are read again from Atlas on the day the page is built |
| M.3 | The video's caption (R.8) | **The voice said, the tool not named**: `One room in two minutes: R-G of 17 Oct 2026, replayed from its own record at four times speed, with the real room in Atlas Connect. Recorded 24 Oct 2026; the narration is my voice, generated from my script.` The video plays as it is, although it opens with "AI builds faster than a person can check what it decided", the framing K.1 kept out of the h1 |
| M.4 | `<title>` and `description` (R.1, R.2) | **The name and what it is**: `Atlas decision rooms: a second opinion from AI models · Petri Korhonen`, and the description in one sentence from the h1 |

### Round N, `/rooms/`: the mark, the share image, the evidence lines and the front page (13.11.2026)

| # | Question | Decision |
|---|---|---|
| N.1 | The subject mark (R.4) | **`Atlas · decision rooms`**, the system and the thing, as the title and the address |
| N.2 | The share image (R.3) | **As I.2**: the wordmark, the subject mark, the h1 on the dawn sky and `sunrisesoftware.app/rooms/` at the foot, made in the media step; alt `Atlas decision rooms: before I settle how my software is built, I ask a panel of AI models for a second opinion.`, which is what the image says. Not a frame of the video |
| N.3 | The lines under the evidence links (R.13) | **What the reader finds there, with the date it was published**: `The room in the video, its arithmetic and its record, 24 Oct 2026` and `Another room in one minute, 25 Oct 2026` |
| N.4 | The front page's link (R.15) | **The plates' dark button on the Atlas plate**: `How the decision rooms work →` before the quiet `Access-protected · shown to partners`; the plate's text does not change, and §04 gets no entry |

### Round O, `/rooms/`: the video's label, the structured data and the captions (13.11.2026)

| # | Question | Decision |
|---|---|---|
| O.1 | The video's `aria-label` (R.8) | **Scene by scene, in the panel's words**: `A video: a decision about which secret scanner a security gate should use, the blind room it went to, two AI agents voting and arguing in two rounds, the room's answer on a condition, the code that followed it, and the decisions the rooms had checked by 24 Oct 2026.` |
| O.2 | The structured data (R.14) | **As J.4**: `WebPage` and `VideoObject`, the video's `uploadDate` the day the file comes to this site (schema.org's meaning), not 24.10.2026 when it was first published on sf3d.fi |
| O.3 | The captions track (R.8) | **The lab's `rooms-en.vtt` as it is**, copied beside the video: one source, the same file sf3d.fi serves, so the copy does not drift. Its numbers are spelled as the narration speaks them |

**`/rooms/` is now fully decided** (R.1 to R.15), and ready to build as PR D together with Petri once
its media exist. What the build needs, none of it made in this session:

- **The media:** `media/rooms-en.mp4` and `media/rooms-en-916.mp4` from
  `sf3d-ai-lab/media/publish/rooms/` (re-encoded or as they are, to be decided in the media round, as
  round I did), a poster for each, `media/rooms-en.vtt` from the lab's `site/public/video/rooms-en.vtt`,
  and the share image `images/og-rooms.jpg` from `docs/mockups/og-rooms.html` (N.2).
- **The numbers in R.12** read again from `atlas_decision_calibration` on the build day, and the
  date with them.
- **Lands with this page:** the Atlas plate's button (R.15) and the page's `<url>` in `sitemap.xml`.
  SEED sections 2.2 (the evidence list of K.3) and 5.2 (the renders' path) were corrected the same day.

### Round P, `/rooms/`: the media (13.11.2026)

Shown with `docs/mockups/rooms/round-P-media.jpg` (three poster scenes from each cut and the share
image draft). Checked first: both renders already have `moov` before `mdat` (faststart), and both are
byte for byte the files `sf3d-media.pages.dev/rooms/` serves (SHA-256 compared 13.11.2026).

| # | Question | Decision |
|---|---|---|
| P.1 | The video files (R.8) | **Copied as they are**: `rooms-en.mp4` (1920x1080, 6 448 529 bytes) and `rooms-en-916.mp4` (1080x1920, 5 855 181 bytes), the same bytes and names as the lab's published files, so there is one source. Not re-encoded: they are already the size the silent-context video was brought down to, and a smaller frame would soften the room's small mono text |
| P.2 | The poster (R.8) | **B, the blind task at 0:23**, for both cuts: the queued room's card with the `BLIND` stamp, the task and the options as the room reads them, and the line `Not in the task: the owner's choice, a recommendation.` It says at a glance what the lede says. Not A (the room's result, sf3d.fi's poster scene: dense and small in an 820 px frame), not C (the end card: mostly empty at 16:9, and it shows one judge where the page says two). The workbench's name shows small in the card, as K.4 allows for the video |
| P.3 | The share image (R.3) | **As drafted**: the h1 at 58 px in four lines broken by hand, `Before I settle how my` / `software is built,` / and the second clause `I ask a panel of AI models` / `for a second opinion.` in `--sun-deep`, otherwise exactly I.2's build. Source `docs/mockups/og-rooms.html` |
| P.4 | Captions on or off (R.8) | **On by default** (`<track default>`): the video has no text in the picture, only the narration, so the captions show at once, also on a muted phone, and the viewer can turn them off. The same experience as the silent-context video, whose captions are burnt in |

### How PR D's media were made (13.11.2026)

- `media/rooms-en.mp4` and `media/rooms-en-916.mp4`: copied from `sf3d-ai-lab/media/publish/rooms/`,
  SHA-256 checked equal to the lab's files and to `sf3d-media.pages.dev/rooms/` (P.1).
- `media/rooms-en.vtt`: the lab's `site/public/video/rooms-en.vtt` from its `origin/main`, unchanged
  (27 cues, UTF-8 without BOM, LF), for both cuts, whose narration is the same (O.3, P.4).
- `media/rooms-en-poster.jpg` (1920x1080, 187 KB) and `media/rooms-en-916-poster.jpg` (1080x1920,
  169 KB): the frame at 23 s of each cut, the `BLIND` card (P.2), at the video's own size.
- `images/og-rooms.jpg` (1200x630, 71 KB): `docs/mockups/og-rooms.html` rendered by
  `docs/mockups/shoot.py` and converted with ffmpeg (P.3).
- The page, the Atlas plate's button and the sitemap entry followed the same day (round Q below).

### Round Q, `/rooms/`: the page as built (13.11.2026)

Shown with `docs/mockups/rooms/round-Q-page.jpg` (the built page at 1440 px and at 375 px, and the
Atlas plate) and on the local server. Two choices made while building, none of them in R.1 to R.15:

| # | Question | Decision |
|---|---|---|
| Q.1 | The video block | **As built**: on a desktop the 16:9 cut across the 820 px column on its left edge, the caption on the same edge under it; up to 600 px the 9:16 cut and its poster in a 420 px frame, the caption centred. A short script picks the cut once at load, before anything is fetched (`preload="none"`); without JavaScript the 16:9 cut plays everywhere |
| Q.2 | The Atlas plate's buttons (R.15) | **As built**: the dark `How the decision rooms work →` first and the quiet `Access-protected · shown to partners` beside it, 10 px apart in a `.btns` row that wraps on a phone. The link comes first because it is what the reader can do; the quiet one says why Atlas itself does not open |

### How PR D was built (13.11.2026)

- `rooms/index.html` copies the frame of `silent-context/index.html` (palette, sky, nav, reveals, the
  reading light, the shore) and changes only the status dot (the sea of infrastructure, the front
  page's `infra` look), the video block (Q.1) and one short script for the cut.
- Every text on the page is R.1 to R.14 verbatim. R.12's numbers were read again from
  `atlas_decision_calibration` at about 12.30 local on the build day and had not moved: 335 and 90,
  the first test 20 of 20 with none overturned, the stricter one 0 of 20, Jev 272 of 309.
- The vertical cut and its poster sit on the `<video>` as `data-src` and `data-poster`, so
  `check-site.mjs` checks that both files exist like any other reference. The captions are a
  `<track kind="captions" srclang="en" label="English" default>` on the lab's `.vtt` (O.3, P.4); the
  local server sends it as `text/vtt` and the browser shows its cues.
- The front page gains the Atlas plate's `.btns` row (Q.2) and one CSS rule for it; its text is
  unchanged. The sitemap names three addresses, all with `lastmod` 2026-11-13.
- Checked locally: at 1440 px the page has no horizontal scroll, no console errors, the three fonts
  load, JSON-LD parses to `WebPage` and `VideoObject`, the 16:9 video plays at 1920x1080 with its
  first cue showing; at 375 px with device emulation `scrollWidth` 375, nothing past the edge, the
  9:16 cut and its poster chosen, the nav showing only the sun mark; on the front page at 375 px the
  two Atlas buttons stack. Seeking was not tried locally, because Python's server does not answer
  range requests; it is checked on the preview.

### Round S, `/reviewglass/`: the big lines (13.11.2026)

| # | Question | Decision |
|---|---|---|
| S.1 | Build the page now, with the name and the AvoQ boundary open in the repository's records? | **Now, today's state.** Petri: the name ReviewGlass is kept and stays; the record that it is unresolved (adr.rg.008 *proposed*, `docs/NAME-CLEARANCE.md`, the repository's `BUILD_INFO.next`) is old. So the page does not say that a release waits for the name, and AvoQ is not named (K.4) |
| S.2 | Name Claude Code on the page? | **Named, with the independence said**: the lede says `in Claude Code`, and RG.11 ends `It works with Claude Code only, and it is my own project: Anthropic does not make, endorse or support it.`, as the README does |
| S.3 | The lead medium (RG.8) | **The drawing enlarged**, as CLAUDE.md and apps-v3 B.5 have it: a real capture would show code and a conversation, and a staged one would need keeping up |
| S.4 | The front page's fact `Nothing leaves the machine` (copy-v3 3.24) | **`Screen pixels never leave the machine`**, which holds without an exception; the old line was untrue while Explain's remote backend is on. Lands with this page (RG.15) |

### Round T, `/reviewglass/`: the h1, the lede and the first two sections (13.11.2026)

| # | Question | Decision |
|---|---|---|
| T.1 | The h1 (RG.5) | **`A glass for reading what the AI agent writes, while it is writing.`**, what it is in one picture, as proposed. Not the first-person variant, not the problem first |
| T.2 | The lede (RG.6) | **The problem, the three things it does, who it is for**, with Claude Code named (S.2) |
| T.3 | What it does (RG.9) | **Two paragraphs**: the glass and its ways; the dock and its drawer, the diff window last |
| T.4 | What it keeps, and what it does not (RG.10) | **The whole principle**: pixels, files, no writes, no network, and the one way out said plainly |

### Round U, `/reviewglass/`: the status line, where it stands, the head and the mark (13.11.2026)

| # | Question | Decision |
|---|---|---|
| U.1 | The status line (RG.7) | **`Pre-alpha · daily use · 2026 →`**, as the drawer, with the sea dot |
| U.2 | Where it stands (RG.11) | **Three sentences**: the state, the open code and what the repository carries, and the independence from Anthropic |
| U.3 | `<title>` and `description` (RG.1, RG.2) | **The kind in the title, the tool in the description**: `ReviewGlass: a reading glass for AI coding sessions · Petri Korhonen`, so the title does not read as Anthropic's product, and the description names Claude Code |
| U.4 | The subject mark (RG.4) | **`ReviewGlass · open source`**, the name and what sets it apart from the site's other products |

### Round V, `/reviewglass/`: the drawing's words, the share image, the evidence and the front page (13.11.2026)

| # | Question | Decision |
|---|---|---|
| V.1 | The lead medium's caption and label (RG.8) | **The drawing said to be one, and why**: caption `A drawing, not a capture: a real picture of the glass would show my code and my conversation.`; `aria-label` `A drawing of ReviewGlass: two columns of blurred text, a reading frame over the left one, and the glass moving along it at 220 percent.`, which is what the canvas draws |
| V.2 | The share image (RG.3) | **As the rooms' (N.2)**: I.2's build with the subject mark and the h1; alt `ReviewGlass: a glass for reading what the AI agent writes, while it is writing.`, what the image says. Made in the media step |
| V.3 | The evidence line (RG.12) | **The licence and the README**: `The code` / `github.com/Sunrisesoftware-app/reviewglass` / `Apache-2.0; the README says what it reads and what it never keeps`, so the reader knows where RG.10's promises can be checked |
| V.4 | The front page's link (RG.14) | **`How the glass works →`** in the drawer, before the repository link, in the words of the Atlas plate's button; the drawer's text does not change |

### Round W, `/reviewglass/`: the structured data (13.11.2026)

| # | Question | Decision |
|---|---|---|
| W.1 | The structured data (RG.13) | **`WebPage` and `SoftwareSourceCode`**, as for Silent context: the code entity `#reviewglass` with the h1 as its description, the Apache-2.0 licence and the languages Rust and Svelte (GitHub's measure on 13.11.2026: Rust 581 kB, Svelte 168 kB, TypeScript 10 kB), also in the front page's graph. Still no `SoftwareApplication` (C.3: there is no installer) |

**`/reviewglass/` is now fully decided** (RG.1 to RG.15), in five rounds (S to W, 18 questions), and
ready to build as PR E together with Petri. What the build needs, none of it made in this session:

- **The media:** only the share image `images/og-reviewglass.jpg` from `docs/mockups/og-reviewglass.html`
  (V.2). The lead medium is the §03 drawing, enlarged by the page's own copy of its canvas code (S.3).
- **Lands with this page:** the drawer's link `How the glass works →` (RG.14), the drawer's fact
  `Screen pixels never leave the machine` (RG.15, replacing copy-v3 3.24's second fact), the
  `SoftwareSourceCode` entity in the front page's graph (RG.13), and the page's `<url>` in `sitemap.xml`.
- **Read again on the build day:** the repository's README and `BUILD_INFO.json`, so that RG.9 to RG.11
  still hold (the glass's ways and the privacy posture move with the product).
- **Outside this site, done the same day:** Petri's word (S.1) that the name is kept was recorded in
  the ReviewGlass repository and in Atlas on 13.11.2026: adr.rg.008 accepted in the model (Atlas #673,
  `a757696`, both Atlas workers deployed), and the repository's README, CLAUDE.md, BUILD_INFO and
  NAME-CLEARANCE no longer say a release waits on the name (reviewglass `2654ab4`). Its spec follows
  with spec v0.5.

### Round X, `/reviewglass/`: the page as built (13.11.2026)

Shown with `docs/mockups/reviewglass/round-X-page.jpg` (the built page at 1440 px and at 375 px, the
front page's drawer at both widths, and the share image) and on the local server. Three choices made
while building, none of them in RG.1 to RG.15:

| # | Question | Decision |
|---|---|---|
| X.1 | The lead medium (RG.8) | **As built**: the front page's drawing in a 16:9 frame across the 820 px column, drawn by the page's own copy of the front page's canvas code; the front page's still at once, the glass moving only while the frame is on screen, the still alone under reduced motion or `?static=1`. On a phone the same drawing smaller, its mono labels decoration; the caption says what it is |
| X.2 | The drawer's links (RG.14) | **As built**: `How the glass works →` before the repository link, in the drawer's own link style, in one row: side by side 24 px apart on a desktop, stacked on a phone |
| X.3 | The share image (RG.3) | **As built**: the h1 at 58 px in three lines broken by hand, `A glass for reading` / `what the AI agent writes,` / and `while it is writing.` in `--sun-deep`, otherwise exactly the rooms' build (P.3). Source `docs/mockups/og-reviewglass.html` |

### How PR E was built (13.11.2026)

- `reviewglass/index.html` copies the frame of `rooms/index.html` (itself `silent-context`'s frame): the
  status dot was already the sea; the video block became the drawing block (X.1) and the cut script
  became the drawing's script.
- Every text on the page is RG.1 to RG.14 verbatim: the build script read them from this file's section
  D and stopped on any row not marked decided.
- Read again on the build day: the ReviewGlass repository's `origin/main` `2654ab4`, whose only change
  since the copy round (`45609db`) is the name record of the same day; its README (the glass at 150 to
  400 %, Follow, Lens, Still, the dock and its drawer, Explain off by default, the privacy posture, the
  independence line) and `BUILD_INFO` (session 11); GitHub: public, Apache-2.0, no releases and no
  tags, Rust 581 138 and Svelte 167 759 bytes. RG.9 to RG.11 hold as written.
- `images/og-reviewglass.jpg` (1200x630, 72 KB): `docs/mockups/og-reviewglass.html` rendered by
  `docs/mockups/shoot.py` and converted with ffmpeg at the rooms' quality (X.3).
- The front page: the drawer's second fact is `Screen pixels never leave the machine` (RG.15); the
  drawer's two links sit in a `.dlinks` row with two CSS rules (RG.14, X.2); the graph gains the
  `SoftwareSourceCode` `#reviewglass` (RG.13). Its other texts are unchanged. The sitemap names four
  addresses, all with `lastmod` 2026-11-13.
- Checked locally: at 1440 px no horizontal scroll, no console errors, the fonts load, JSON-LD parses
  to `WebPage` and `SoftwareSourceCode`, the drawing fills its 820x461 frame; at 375 px with device
  emulation `scrollWidth` 375, nothing past the edge, the nav showing only the sun mark; on the front
  page the drawer's links side by side at 1440 px and stacked at 375 px. `check-site` green over four
  pages.
- The comparison image's phone column comes from the browser pane. A first try took it with
  `shoot.py` at 375 px, which crops a wider layout (LESSONS 13.11.2026); it was caught before the round
  and `shoot.py` now refuses widths under 500 px.
- The profile README (`pkorrrhonen-cmd`, pushed 24.9.2026) still says ReviewGlass will have "later a
  live diff"; the live diff is built and the page says so. The README is Petri's; the difference is in
  `BUILD_INFO.next`.

**Petri at the close of 13.11.2026:** real mockups of the applications have to get onto the pages. For
ReviewGlass it has to be built some other way than a screen capture, because the glass vanishes from
one: the glass, its halo and the finder exclude themselves from capture (`WDA_EXCLUDEFROMCAPTURE`, so
the glass never captures itself), and only the dock and its drawer are visible to it (ReviewGlass
adr.rg.025). RG.8's drawing stays until that mockup exists; how it is made is decided with Petri.

### Round Y, `/hometeam/`: the mockups as its images (13.11.2026)

Petri opened the `/hometeam/` thread on 13.11.2026: the hometeam repository holds many mockups, so they
illustrate the page. Read in the session from the hometeam repository (`origin/main` `1c98b23`, last
changed 10.10.2026, so the facts under A3, checked 11.11., still hold): `mockups/README.md` and its
table of 21 mockups, each a self-contained page with the options A, B, C and the one Petri chose. Ten
were rendered at 1440 px and nine candidate screens cut from the chosen options into a contact sheet
(kept outside the repository, because some screens carry real names): 1 the child's Today (Comic,
011), 2 the adult's Today (Comic, 011), 3 Wallet (005), 4 the weekly scoreboard (019), 5 the treasure
island (020), 6 mood and the family map (021), 7 the amusement park (012), 8 the electricity card
(013), 9 the living HomeCoin (018).

Found before the round: the screens are in Finnish and the site is in English; screens 1, 2 and 8
carry `Hei, Petri!`, the family's surname and three children's first names, while the others use
nicknames (Kettu, Pöllö, Panda, Äiti, Isä); a mockup is the plan the application was built from, not
a capture of production (mood moved behind the settings on 8.10.2026, hometeam PR #35, after
mockup 021 was drawn).

| # | Question | Decision |
|---|---|---|
| Y.1 | Which screens, in what form | **The pair and a row of three**: the lead is the child's and the adult's Today side by side (1, 2); after the body, a row of Wallet, the weekly scoreboard and the treasure island (3, 4, 5). Stills cut from the chosen options at 2x, WebP with a PNG fallback |
| Y.2 | The language of the screens | **Finnish as they are, an English caption under each**, and one line on the page saying the application is in Finnish. Nothing staged |
| Y.3 | Names in the screens | **`Hei, Petri!` may stay**, as the name is already on the page. The family's surname and every child's name become the mockups' own nicknames in the copy that is captured (screen 1 `HEI, KETTU!`, screen 2 the children's tiles and `Vuorossa` line in nicknames, the surname line gone or a nickname). No screen or source file with a surname or a child's name enters this repository, which is public |
| Y.4 | The front page's drawer (3.46, B.3) | **The mockup replaces the drawing**: the drawer shows screen 1 in PR F, together with the page. adr.sws.020 records the rule's change |

**For the build:** the captures are taken from a copy of the mockup files outside this repository,
with the names replaced (Y.3) and the chosen option set, at 2x; `source-assets/` gets the name-free
captures only. **For the copy round (Z):** the captions' words (Y.2), the line saying the application
is in Finnish, and how the page says that these are the design mockups the application was built
from rather than captures of production; the fonts (OFL) and the 3D images (Microsoft Fluent Emoji,
MIT) in the screens, and whether the page credits them.

### Round Z, `/hometeam/`: the front page's error, the h1, the lede and the lead caption (13.11.2026)

Before the round, the facts of section E were read from the hometeam repository and its code. The
drawer's body (3.43, live since 12.11.2026) names meals and the shopping list, which are not built:
`/ruoka` is a "coming soon" placeholder and the shopping list has a module switch but no page
(KOORD-2 and KOORD-3 under "later").

| # | Question | Decision |
|---|---|---|
| Z.1 | The drawer's body (3.43) | **Corrected at once, in its own pull request**: `A shared Today view for the day's tasks and the family calendar, and an economy each family sets for itself: HomeCoin or euros, a weekly allowance, a loan, rewards, a savings goal. Adults sign in with a code sent to their address; children use nickname profiles on devices an adult has paired. A change appears on the other devices at once.` The rest of the drawer waits for PR F |
| Z.2 | The h1 (HT.5) | **As proposed**: `The application my family runs the week on. My children voted on how it looks.` |
| Z.3 | The lede (HT.6) | **As proposed** |
| Z.4 | The lead caption (HT.8) | **As proposed**: `Design mockups, not captures: a child's Today and a parent's, in Finnish as the application is. A capture would show my family's own week.`, in the shape of `/reviewglass/`'s `A drawing, not a capture` |
| Z.5 | The drawing in the drawer (asked while checking the preview of Z.1) | **Corrected in the same pull request**: its footer `TASKS · CALENDAR · MEALS · SHOPPING · HOMECOIN` becomes `TASKS · CALENDAR · WALLET · HOMECOIN`, and the tasks `Tacos for dinner` and `Milk, bread, apples` become `Take out the rubbish` and `Make the bed`. The drawing gives way to the mockup in PR F (Y.4) |

Open for the next rounds (AA onwards): HT.1 to HT.4, HT.9 to HT.16.

### Round AA, `/hometeam/`: the body and the row's captions (13.11.2026)

Each claim was read from the hometeam repository the same day (section E's two lists).

| # | Question | Decision |
|---|---|---|
| AA.1 | `What it does` (HT.9) | **As proposed**, two paragraphs, the game layer included |
| AA.2 | `Why it exists` (HT.10) | **As proposed**, the two lessons of the first version and the family's vote |
| AA.3 | `Where it stands` (HT.11) | **As proposed**, without the date of the latest release, which would age |
| AA.4 | The row's captions (HT.12) | **As proposed** |

### Round AB, `/hometeam/`: the head, the subject mark and the evidence (13.11.2026)

| # | Question | Decision |
|---|---|---|
| AB.1 | `<title>` and `og:title` (HT.1) | **As proposed**: `HomeTeam: the application my family runs the week on · Petri Korhonen` |
| AB.2 | `description` and `og:description` (HT.2) | **As proposed** |
| AB.3 | The subject mark (HT.4) | **`HomeTeam · my own family`**, the word of the status line and the drawer's tag |
| AB.4 | The evidence block (HT.13) | **A line in the link's place**: `No public link: the application admits only my family's addresses, and its code is private.` |

### Round AC, `/hometeam/`: the share image, the structured data, the front page and the credits (13.11.2026)

| # | Question | Decision |
|---|---|---|
| AC.1 | The share image (HT.3) | **The build of the other pages**: the subject mark and the h1 in two lines on the dawn sky, no screen; alt the h1 |
| AC.2 | The structured data (HT.14) | **A `WebPage` only**, with `isPartOf` the WebSite and `author` the Person. C.3 stands, and the front page's graph does not change |
| AC.3 | The front page (HT.15) | **`How my family uses it →`**; the drawer's image is screen 1 with the caption `hometeam · a child's today, a design mockup` |
| AC.4 | The credits (HT.16) | **One mono line under the row of three**, the Fluent Emoji name linking to its repository, where the MIT licence is |

**Every item of `/hometeam/` (HT.1 to HT.16) is now decided**, with the images of round Y. PR F builds
the page: the screens cut from a copy of the mockups outside this repository with the names swapped
(Y.3), the share image, the front page's drawer (its image, link and caption), the sitemap entry and
its own `check-site` pass.
