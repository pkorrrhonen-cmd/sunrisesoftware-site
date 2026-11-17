# adr.sws.025: The typefaces are served from the site itself

| | |
|---|---|
| Status | accepted (Petri, 17.11.2026, session 13, round AU.4, decision box) |
| Date | 2026-11-17 |
| Decided by | Petri Korhonen |
| Links | sws.site; adr.sws.012 (the typefaces); adr.sws.001 (static HTML, no build step) |

## Context

The pages loaded Familjen Grotesk, Public Sans and JetBrains Mono through the Google Fonts stylesheet. On a
phone that stylesheet blocked rendering for about 770 ms (Lighthouse 13.6.0, 15.11 and again 17.11.2026), and it
was the site's only external dependency besides Cloudflare's own beacon. adr.sws.012 chose the typefaces; it
did not decide where they are served from.

## Decision

The three families are served from `fonts/`:

- The variable woff2 files Google Fonts serves (Familjen Grotesk v11, weights 400 to 600; Public Sans v21,
  300 to 600; JetBrains Mono v24, 400 to 500), the latin and latin-ext subsets with Google's unicode ranges:
  six files, 122 kB in all. Petri gave the download in his answer to AU.4.
- Each family's SIL Open Font License beside them (`fonts/OFL-*.txt`, from github.com/google/fonts), as the
  licence requires when the fonts are redistributed.
- `@font-face` inline at the top of each page's `<style>`, `font-display: swap`, and the three latin files
  preloaded. No request leaves the site for a typeface.
- `_headers` caches `/fonts/*` for a year, immutable; each name carries Google's version, so a changed font
  gets a new name.

## Consequences

- Render-blocking requests on the five pages: none (locally measured 17.11.2026; FCP on a simulated phone
  1.7 s before, 1.2 s after).
- `check-site` now follows `fonts/` references, srcset entries and CSS `url()` (with a self-test), so a
  missing font or variant fails CI.
- Updating a typeface means fetching the new version's files from Google Fonts under new names and changing
  the six `@font-face` lines and three preloads in every page.
