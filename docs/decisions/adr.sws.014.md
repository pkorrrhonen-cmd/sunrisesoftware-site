# adr.sws.014: one source for the facts the page shares with the profile README

| | |
|---|---|
| Status | accepted (Petri, 15.11.2026, session 12 side thread: "kyllä, tee tämä", and the shape in decision boxes GH.1 to GH.3 and GH.21, all as recommended; `docs/design/profile-readme.md`) |
| Date | 2026-09-19 (proposed), 2026-11-15 (accepted) |
| Decided by | Petri Korhonen |
| Links | sws.site; github-profile repo (`pkorrrhonen-cmd/pkorrrhonen-cmd`) |
| Builds on | adr.sws.004 as amended by adr.sws.015 (every status carries a date); adr.sws.006 (the employer's applications) |

## Context

The page and the GitHub profile README (`github.com/pkorrrhonen-cmd`) are both public and the
page links to the profile four times. Within a day of the V5 launch the two surfaces disagreed
on five facts: ReviewGlass's licence (the page said "once the name is cleared", the README said
Apache-2.0 with a link), SF3D's years (2006 versus 2008), SpectralForge's state (production
versus beta), MasterForge's first paying year (2023 versus the company's 2024) and Quaesitor's
presence. The feedback (`SW-SIVUSTO-MSG-PALAUTE-V5`) named the class: content truth kept by hand
between two public surfaces. Each item was a one-line fix; the class is what recurs.

It recurred. On 15.11.2026 the README, unchanged since 24.9.2026, still named the employer's
applications, said ReviewGlass would get "later a live diff" when it had one, gave MasterForge four
tiers when it has three, called SpectralForge a beta when its gate says closed beta, and lacked
HomeTeam, which the page had carried for two days. Reading both surfaces against each other also
found the page wrong: Petri set every product's year to 2026, the year of its commercial use or
release, where the page says 2024 for MasterForge and TilastoSilta and 2025 for SpectralForge.

## Decision

The facts both surfaces carry come from one file in this repository, and neither surface types
them by hand:

- **The source is `docs/facts.json`**, JSON so that `check-site` stays dependency-free (GH.1). Per
  product: name, state, detail, the year (`since`), the address (`where`), the licence where there is
  one, the sub-page where there is one, the README's description, and what was checked and when. The
  groups and their order are the page's. The repository is public, so the employer's applications
  never appear in it.
- **`scripts/readme-facts.mjs` writes the README's whole product table** between the markers
  `<!-- facts:start` and `<!-- facts:end -->`: one table per group, `Product · What it is · State ·
  Where`, the state in the page's words (`Live · paying customers · 2026 →`). The rest of the README
  is hand-written in its own repository (GH.2, GH.16).
- **`scripts/check-site.mjs` checks the page against the facts in CI** (GH.3): every product's status
  on the front page (its group, state words, year, address and licence) and on its sub-page, the
  products in the facts' order, and no product on the page without a fact. The facts' own words obey
  the page's rules (forbidden strings, no version numbers, no em dashes). The check lives in
  `scripts/facts.mjs` with its self-test, which `check-site` runs first on every run.
- **The README is checked in the session routine**, not in CI, as it lives in another repository:
  `node scripts/check-site.mjs --readme <profile checkout>/README.md` fails when the table differs
  from what the generator would write or when the README carries a forbidden string.
- **A decided fact the page does not carry yet is a pending record** (GH.21): the product's `pending`
  names the page's old value and the decision the fix waits for. The check accepts that one old
  value and no other, prints it on every run, and fails once the page is fixed and the record stays.

## The proposal of 19.9.2026, and what changed

The proposal took the Atlas model's BUILD facts per system as the source. Accepted instead: a file in
this repository, because Atlas is the mirror and the repository the truth (CLAUDE.md), because the
site's CI runs without a network, and because the model holds the employer's systems. The family
map the README carried from Atlas (`pnpm portfolio`) left the README the same day (GH.4): the
generator names every system it leaves out, by design, so it cannot withhold the employer's systems
without naming them. The map comes back when Atlas can count a withheld system without naming it.

## Consequences

One place to edit when a product changes state, year or address; CI fails when the page drifts
from it; the README's table is generated rather than typed. The session routine changes: a product's
state is checked from its repository into `docs/facts.json`, then `check-site` tells which surface
disagrees. The descriptions are not facts the check can read: a product whose use changes (Somnus,
GH.19) still needs a reading of its repository. The three pending years wait for a page session with
Petri (`BUILD_INFO.next`).
