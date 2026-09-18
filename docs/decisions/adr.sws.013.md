# adr.sws.013: Flow 4 is the page; SEED v3.0.0 records it

| | |
|---|---|
| Status | accepted (Petri, 18.9.2026: "a huge improvement on the previous version; we are ready") |
| Date | 2026-09-18 |
| Decided by | Petri Korhonen |
| Links | sws.site |
| Builds on | adr.sws.010 (look), 011 (Flow 1 direction), 012 (type); copy in `docs/design/copy-v3.md`, app views in `docs/design/apps-v3.md` |
| Supersedes | SEED v2.0.0 (the cabinet-dark page) and the v2.1.0 content draft |

## Context

Four mockup rounds on 17.9. and 18.9.2026: the look (three palettes), Flow 1 (motion and flow),
Flow 2 (the answers applied, reviewed and fixed), the type round, Flow 3 (the decided copy) and
Flow 4 (the decided app views: a real EQ capture for MasterForge, Luviamo's video, the Somnus
rack panel, the Atlas workspace board, real captures in the drawers, Salpa's brand mark, a
ReviewGlass interface mockup). Every text and every image was decided item by item.

## Decision

`docs/mockups/flow-4.html` is the page. SEED v3.0.0 records its design system, its copy and its
app views as the spec; `index.html` is rewritten to it together with Petri, and the page assets
(portrait cutout, EQ clip, captures, Salpa logo, OG image, favicon, robots, sitemap, headers)
ship with it. One noted limit: the EQ capture shows the EQ control's narrow band; acceptable
now, a wider capture can replace it later without a design change.

## Consequences

SEED v2.0.0 and the v2.1.0 draft move to `docs/archive/`. `BUILD_INFO.version` becomes 5.0.0
on publish (a new design generation). The check script's rules (dated statuses, forbidden
strings, footer date) apply to the new page from the first commit.
