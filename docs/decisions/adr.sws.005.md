# adr.sws.005: Atlas is on the page as an instrument, and its plate is drawn

| | |
|---|---|
| Status | accepted (Petri, 18.9.2026, through adr.sws.013, in the shape Flow 4 gave it) |
| Date | 2026-09-17 (proposed), 2026-09-18 (decided) |
| Instruction by | Petri Korhonen |
| Links | sws.site |
| Settled by | adr.sws.013 (Flow 4), SEED v3.0.0, `docs/design/apps-v3.md` A.6 |

## Context

Atlas grew from a mapping tool (SEED v0.1, 6.7.2026) into the control plane and knowledge graph
of the whole family: the model as the single source of truth, the proposals and artifact
channels, Atlas Teamwork (a partner's own Claude scoped to their projects) and Atlas Connect
(the installable phone app for partners and the owner, in use since 7.9.2026). For a technical
reader it is the most distinctive thing in the portfolio, and it explains how one person keeps
nineteen systems honest. Petri named it on 17.9.2026 as the collaboration tool to show, now
that the workspace and Connect have matured. The viewer and Connect are access-protected, so no
screenshot is cleared for public use.

## Decision

Atlas is one of the section 02 products, in the group "Tools and research instruments" with
Somnus. Its plate is a drawn instrument in the page's palette (the workspace board, apps-v3
A.6), because the viewer and Connect are access-protected, and it carries the quiet
Access-protected pill. The 17.9.2026 proposal (section 02.4 of Selected work, a schematic with
the model's figures) was not built; no figures are shown.

## Consequences

The drawing lives in `index.html` (`sketches.atlas`) and is maintained there. A real mockup
may replace it, with a decision of its own (Petri, 13.11.2026). The file was completed on
15.11.2026 from SEED v3.0.0 and adr.sws.013; the proposal of 17.9.2026 is in the git history.
