# adr.sws.014: one source for the facts the page shares with the profile README

| | |
|---|---|
| Status | proposed (session 3, 19.9.2026; Petri chose "ADR proposed + a next row" in the decision box, the design is not yet accepted) |
| Date | 2026-09-19 |
| Decided by | Petri Korhonen (pending) |
| Links | sws.site; github-profile repo |
| Builds on | adr.sws.004 (every status carries a version or a date) |

## Context

The page and the GitHub profile README (`github.com/pkorrrhonen-cmd`) are both public and the
page links to the profile four times. Within a day of the V5 launch the two surfaces disagreed
on five facts: ReviewGlass's licence (the page said "once the name is cleared", the README said
Apache-2.0 with a link), SF3D's years (2006 versus 2008), SpectralForge's state (production
versus beta), MasterForge's first paying year (2023 versus the company's 2024) and Quaesitor's
presence. The feedback (`SW-SIVUSTO-MSG-PALAUTE-V5`) named the class: content truth kept by hand
between two public surfaces. Each item was a one-line fix; the class is what recurs.

## Decision (proposed)

The facts both surfaces carry (state, version, first year, licence, URL per product) come from
one source, and neither surface types them by hand:

- The source is the Atlas model's BUILD facts per system (`<system>.BUILD`: version, updated,
  url), which the family already keeps and which the profile README's family table is already
  generated from (`pnpm portfolio`).
- The page keeps its hand-written copy, but `scripts/check-site.mjs` gains a check that reads a
  small facts file (`docs/facts.json`: product, state, version, since, licence, url) and fails
  when a status line on the page disagrees with it. The same file is what the README generator
  reads for its product table.
- The facts file is refreshed from the product repos in the session routine, as the facts are
  checked today; the difference is that the check is mechanical and covers both surfaces.

## Consequences

One place to edit when a product changes state; CI catches a page that drifts from it; the
README's product table is generated rather than typed. Not built in session 3: the shape of the
facts file and the generator's home (site repo or profile repo) are Petri's call. Until then the
session routine checks the README against the page by hand (LESSONS 19.9.2026).
