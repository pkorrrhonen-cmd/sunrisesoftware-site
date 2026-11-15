# adr.sws.023: Cloudflare adds only the analytics beacon to the served page

| | |
|---|---|
| Status | accepted (Petri, 15.11.2026, session 12, Cloudflare side thread, decision box) |
| Date | 2026-11-15 |
| Decided by | Petri Korhonen |
| Links | sws.deployment; adr.sws.001 (static HTML, no build step) |

## Context

The site is served by Cloudflare Pages on the zone `sunrisesoftware.app`. Two zone features change
what a visitor gets compared with what the repository holds and what a `*.pages.dev` preview shows.

**Email Address Obfuscation** was on for the zone (Cloudflare turns it on at sign-up). On the live
domain it rewrote both `mailto:` links of the front page to `/cdn-cgi/l/email-protection#...`,
replaced the address in §06 with `[email protected]` and added a decode script
(`/cdn-cgi/scripts/.../email-decode.min.js`, 1.2 kB). Measured on 15.11.2026:

- The address stayed readable in plain text in two places the feature does not touch: the
  structured data's `"email"` (inside `<script>`) and the hero's meta row, where `<wbr>` splits the
  address. A harvester reading the HTML found it anyway.
- Without JavaScript the hero's link led to Cloudflare's "Email Protection" page (status 404,
  "unable to access this email address"), and §06 showed `[email protected]`. Reader views and
  link previews saw the same.
- Previews did not have it, so a page checked on its preview was not the page served live.

**Web Analytics** had been planned since the concept (`docs/archive/concept-v3.html`) and was
listed in `BUILD_INFO.next`, but was never turned on. The pages are edited only together with
Petri, so the beacon may not be added to the HTML by a session.

## Decision

1. Email Address Obfuscation is **off for the whole zone** (Security > Settings > Email Address
   Obfuscation). The live page serves the same contact markup as the repository and the previews.
2. Web Analytics is turned on **through the Pages project** (Workers & Pages >
   `sunrisesoftware-site` > Metrics > Web Analytics), not through the zone's automatic setup and
   not by editing `index.html`. Cloudflare injects the beacon on each deployment.

## Consequences

- The only thing Cloudflare adds to the served HTML is the Web Analytics beacon: a `defer` script
  from `https://static.cloudflareinsights.com/beacon.min.js` that reports to
  `https://cloudflareinsights.com/cdn-cgi/rum` (measured in a browser on 15.11.2026, answer 204). A
  future Content-Security-Policy needs `script-src https://static.cloudflareinsights.com` and
  `connect-src https://cloudflareinsights.com` for it; today the site sends no CSP.
- The Pages project injects the beacon into every deployment, the `*.pages.dev` previews
  included, with the same token. Preview visits are counted too, under their own hostnames; the
  Web Analytics view is read filtered to `sunrisesoftware.app`.
- The address is as public as the page makes it. Hiding it from harvesters would be a page change
  (the structured data and the hero's meta row), taken together with Petri if ever wanted.
- The feature is off for every hostname under the zone, not only for the site.
