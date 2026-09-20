# adr.sws.004: Every status on the page carries a date; no relative-time copy

| | |
|---|---|
| Status | proposed (Petri decides in the page-revision planning) |
| Date | 2026-09-17 |
| Proposed by | Claude Code, session 1, from Petri's instruction to bring the site to the present |
| Links | sws.site, sws.deployment |
| Amended by | adr.sws.015 (20.9.2026): a status carries a date, never a product version |

## Context

The page said "Launching within the month" about Luviamo from April to September 2026, gave
Quaesitor's version as 2.12.11 when production was 2.13.27, and priced MasterForge in tiers
that no longer existed. Copy that refers to "now" without a date is wrong the day after it
was true, and nothing on the page or in the repo made the staleness visible.

## Decision (proposed)

Every status on the page carries a version or a date, or both ("Live · v4.44 · September
2026"). The footer carries the revision date in a `data-revised` attribute, and CI fails when
it differs from `BUILD_INFO.updated`. The words "coming soon", "within the month" and
"recently" are forbidden strings in `scripts/check-site.mjs`.

## Consequences

Revising the page becomes a short routine (CLAUDE.md, session end) instead of a rewrite.
Staleness is visible on the page rather than hidden by phrasing. A dated fact that has aged is
still true; a relative one is a lie. Until the page revision lands, the check script is red on
V4.5 by design: the gate encodes the rule, the page does not yet meet it.
