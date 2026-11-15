# adr.sws.022: Atlas and Somnus are shown by the sf3d.fi lab's explainer videos

| | |
|---|---|
| Status | accepted (Petri, 15.11.2026, round AK in `docs/design/copy-v4-pages.md`) |
| Date | 2026-11-15 |
| Decided by | Petri Korhonen |
| Amends | the rule on drawn instruments (CLAUDE.md, "Rules for the page"; `docs/design/apps-v3.md` A.4 and A.6); adr.sws.005's cover (a drawn schematic, since 20.9.2026 the workspace board) |
| Links | sws.site; sf3d-ai-lab `docs/VIDEO-SERIES-PLAN.md` v0.2 (the lab's D-40 to D-46, 29.10.2026); adr.sws.020 and adr.sws.021 (the two products before these under the same line) |

## Context

Since 18.9.2026 the §02 plates of Somnus and Atlas have been drawn instruments: the Somnus rack panel
and the Atlas workspace board (apps-v3 A.4 and A.6), because neither has a public surface to capture.
On 13.11.2026 Petri set the line that real mockups replace the drawings, one product at a time, each
with its own decision (HomeTeam, adr.sws.020; ReviewGlass, adr.sws.021), and in round K.3 that the
drawings and stories of Atlas and Somnus do not make anyone understand them.

The sf3d.fi lab makes short explainer videos on its own explainer kit: animated scenes in the lab's
palette, every number exported from a dated record and said on screen with its date, one everyday
metaphor said once, at most 60 s, the owner's own voice. Its series plan of 29.10.2026 has two lines:
A on Atlas, B on Somnus. A1 "Why I Built Atlas" is built and live on sf3d.fi (63.6 s, 16:9 and 9:16);
B1 "Why There Is an AI Server in My Home" is planned and not made. The kit renders any even frame size
since 7.11.2026.

## Decision

The Atlas and Somnus plates show the lab's explainers, each as a cut made for the plate:

- **Atlas first (AK.1, AK.4):** a site cut of A1, rendered again from its own scenes in the lab's
  pipeline: 16:10, a 64 px safe area (LESSONS 14.11.2026), without the lab's eyebrow, its counts read
  again and dated on the day of the render, Petri's voice track as it is.
- **Somnus second (AK.2):** B1, made in the lab as the series' part, with its sources read from Somnus
  on the day, Petri's core sentence before the storyboard, his voice, a lab note on sf3d.fi, and a
  16:10 site cut for the plate.
- **What Somnus is shown as (AK.3):** the machine as it runs now: the server for the computing, checking
  and work of the projects, a tool for general use and a research instrument; not the original
  three-tier idea. Every example is checked against what runs before the storyboard.
- **On the page:** both run muted while in view with sound on a click, as the MasterForge and Luviamo
  plates. The plate's text is read against its video in the same build round, so both tell the same
  story. The wording of each plate is decided in its own text and build rounds.
- **Made in the lab:** the videos are made where the kit, the pipeline and their rules live, and the
  finished cut is copied to this site's `media/` under a new name.

The sub-pages `/atlas/` and `/somnus/` (K.3) are a later thread, with these videos as their lead media.
Until a video is built, its plate keeps the drawing.

## Consequences

The two plates stop being drawings of what the products might look like and become the products
explained in plain words, with their real records on screen. The site and sf3d.fi tell the same story
from the same source; the long version and the evidence stay on sf3d.fi.

The cost: the site depends on the lab's pipeline and on Petri's voice for each video, and a dated
count on screen ages. A cut is rendered again when its story changes, under a new file name, because
`/media/*` is cached as immutable (LESSONS 14.11.2026). A statement about the future (Somnus's second
machine) goes into a video only in a form the page's rules allow: no "coming soon", an idea shown as an
idea.
