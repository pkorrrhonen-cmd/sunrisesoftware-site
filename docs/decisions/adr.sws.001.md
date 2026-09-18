# adr.sws.001: Static HTML with no build step

| | |
|---|---|
| Status | accepted |
| Date | 2026-04 (recorded in Atlas; brought into the repo 2026-09-17) |
| Decided by | Petri Korhonen |
| Links | sws.site, sws.deployment |

## Context

The site's purpose is portfolio and business card. Content and design are stable, and the
complexity of build tooling is not justified for single-page static content.

## Decision

The deliverable is a single `index.html` with inline CSS and about fifty lines of vanilla JS.
No build, no framework, no dependency beyond Google Fonts. Served by Cloudflare Pages with an
empty build command.

## Consequences

Simplicity and instant deploy. Full-page inline CSS and JS is harder to maintain at scale. A
framework migration is considered only if complexity warrants it (see adr.sws.008 for the
September 2026 reading of that clause).
