# adr.sws.005: Atlas is selected work, and its cover is a drawn schematic

| | |
|---|---|
| Status | proposed (showing Atlas is Petri's instruction, 17.9.2026; the placement and the cover are the proposal) |
| Date | 2026-09-17 |
| Instruction by | Petri Korhonen |
| Links | sws.site |

## Context

Atlas grew from a mapping tool (SEED v0.1, 6.7.2026) into the control plane and knowledge graph
of the whole family: the model as the single source of truth, the proposals and artifact
channels, Atlas Teamwork (a partner's own Claude scoped to their projects) and Atlas Connect
(the installable phone app for partners and the owner, in use since 7.9.2026). For a technical
reader it is the most distinctive thing in the portfolio, and it explains how one person keeps
nineteen systems honest. Petri named it on 17.9.2026 as the collaboration tool to show, now
that the workspace and Connect have matured. The viewer and Connect are access-protected, so no
screenshot is cleared for public use.

## Decision (proposed)

Atlas is §02.4 of Selected work. Its cover is an inline SVG schematic in the page's own
palette: the model in the middle, the three doors (Claude chat, Claude Code, Atlas Connect)
around it, the gates named, and the model's figures with their date (19 systems, 208 modules,
175 connections, 116 ADRs on 7.9.2026). A cleared screenshot (viewer or Connect) may replace
the schematic; until then the schematic is a catalogue plate, not a placeholder. Atlas Connect
is described, not linked: its address is a sign-in page for partners.

## Consequences

The SVG lives in `index.html` and is maintained there. The figures are refreshed from
`pnpm validate:models` in the Atlas repo whenever the page is revised, and their date moves
with them.
