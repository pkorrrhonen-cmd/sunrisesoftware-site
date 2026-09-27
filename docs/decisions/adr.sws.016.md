# adr.sws.016: the site serves the SCC2 app icons under /scc/

| | |
|---|---|
| Status | accepted (Petri, 27.9.2026: "kuvan tarjoilu 1 vaihtoehto", icons from the public site) |
| Date | 2026-09-27 |
| Decided by | Petri Korhonen |
| Links | sws.site, scc2 |

## Context

Sunrise Command Center v2 (scc.sunrisesoftware.app) sits entirely behind Cloudflare Access.
When the app is installed on an Android phone, Chrome downloads the manifest icons again
without cookies to build the WebAPK, and behind Access that request ends at the login page, so
the install falls back to a generic icon (the phone showed Google's "G"). Measured 27.9.2026:
`/manifest.webmanifest` on the app host answers 302 to the Access login. The alternatives were
an Access bypass policy for the icon paths (a security setting Petri would change by hand) or a
public host that already exists.

## Decision

The four install icons live in this repo under `/scc/` (192, 512, maskable 512 and the
180 px apple-touch-icon) and are served publicly with a one-day cache and
`Access-Control-Allow-Origin: *`. They are generated in the scc2 repo
(`scripts/kuvakkeet.mjs`) and copied here unchanged; they are not referenced from
`index.html` and are not part of the page.

## Consequences

The app installs with its own icon without any change to Access. An icon change needs a PR
here as well as in scc2. Nothing on the page changes, so the footer date and
`BUILD_INFO.updated` stay.
