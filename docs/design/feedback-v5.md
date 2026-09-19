# Feedback round on the V5 live page (18.9.2026)

Source: Atlas artifact `SW-SIVUSTO-MSG-PALAUTE-V5` (art_cbd6dba3d59a4f8b, chat's reading of the
live page and the GitHub profile, 14 items). Every claim was checked against the product repos
and the live services in session 3 (19.9.2026) before this list was written. Decisions are taken
with Petri through decision boxes (`decision-method.md`), four a round; each row carries its
state: `open`, `decided`, `not a page change`, `dropped`.

| # | Item | Current | Checked fact | Proposal | State |
|---|---|---|---|---|---|
| 1 | ReviewGlass status (A1) | "open source once the name is cleared" | Repo public since 18.9.2026 16:51Z, Apache-2.0, pre-alpha | "Built for my own daily use. Open source, Apache-2.0." plus the repo link | decided 19.9.2026 |
| 2 | SpectralForge status (A3) | "production · v2.0" | v2.0.0 live; users without access meet a "Closed Beta" gate | "closed beta · v2.0" | decided 19.9.2026 |
| 3 | SF3D years (A2) | Page 2006–2016 | Page carries the corrected value (LESSONS 17.9.2026); the profile README says 2008 | Fix the README (github-profile repo), not the page | decided 19.9.2026, README fix in this session |
| 4 | Employer's names in the README (A4) | CI forbids them on the page | The profile README names them | Petri's call for the README; not touched in this session | not a page change |
| 5 | Quaesitor absent from the page (A5) | Not on the page | Decided 18.9.2026: Somnus is the research core | No change | dropped |
| 6 | Two `<img>` without `src` (B6) | `#peek img`, `#lightboxImg`; JS sets `src` | Validator warning, both hidden until used | Transparent 1x1 placeholder `src` on both | decided 19.9.2026 |
| 7 | Luviamo video from luviamo.app (B7) | 5.1 MB streamed, `preload="metadata"` | MasterForge clip is local (3.4 MB) | Copy to `media/luviamo-intro.mp4`, `preload="none"` on both clips | decided 19.9.2026 |
| 8 | Status vocabulary (B8) | 7 forms: Live, In use, In production, production · v2.0, pre-alpha · daily use, venture, live | Ultra Gravel has no version on the live site (repo 0.1.0) | One scale: Live / In use / Closed beta / Pre-alpha / Venture, version right after the state; Luviamo "Live · v0.385 · 2026 →", Atlas "In use · v0.9 · 2026 →" | decided 19.9.2026 |
| 9 | "Est. 2024" vs MasterForge "2023 →" (C9) | Both on the page | Petri 19.9.2026: the years must match and 2023 cannot stay | MasterForge status "Live · v4.44 · paying customers · 2024 →"; the profile README ("since 2023") joins the README fixes | decided 19.9.2026 |
| 10 | −269 °C vs −234 °C (C10) | Body: liquid helium at −269 °C; stat: Lowest reading −234 °C | Boiling point vs probe reading | "Lowest probe reading"; the card caption stays | decided 19.9.2026 |
| 11 | §01 item 03 one sentence (C11) | "Day work: digital health software to clinical and regulatory standards." | Others have two or three sentences | Second sentence: "Patient data, audit trails and the security review are part of the product, not a layer added afterwards." | decided 19.9.2026 |
| 12 | Luviamo "five to eight separate tools" (C12) | Unanchored claim | Same wording in the README | "One brand voice. The whole marketing lifecycle: ideation, copy, visuals, scheduling, publishing and measurement in one place." | decided 19.9.2026 |
| 13 | Creed second sentence (C13) | "Imagination is the limit. Build, then enjoy the world." | Pairs with the hero "The world is open" | Keep both sentences; the pair with the hero is intended | decided 19.9.2026, no change |
| 14 | 7 GHz claim (C14) | "no desktop processor sold today runs at the 7 GHz" | True in 9/2026 (boosts about 6.2 GHz), ages silently | "And in 2026 no desktop processor on sale runs at the 7 GHz we reached in 2010." | decided 19.9.2026 |

Structural note from the feedback: items 1 to 5 are content truth kept between two public
surfaces (the page and the profile README). If states, years and licences came to both from one
source, that class of conflict would disappear. Recorded for a later decision, not for this round.
