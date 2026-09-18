# adr.sws.007: The public GitHub profile is linked from the page

| | |
|---|---|
| Status | accepted (the link is Petri's decision, 17.9.2026; the profile address and the placements are confirmed in the page-revision planning) |
| Date | 2026-09-17 |
| Decided by | Petri Korhonen |
| Links | sws.site |

## Context

V4.5 left GitHub out because there were no public repositories. The public profile is being
completed in September 2026 as part of the same revision package as this page; ReviewGlass is
planned as the first open-source release (Apache-2.0) once its name is cleared. A hackathon or
hiring reader expects the link in the nav and reads its absence as a gap. On 17.9.2026 the
account `pkorrrhonen-cmd` (the owner of this repository) has no public repositories, name or
bio yet, and the organisation `Sunrisesoftware-app` holds fifteen private repositories.

## Decision

The page links the public profile (assumed `https://github.com/pkorrrhonen-cmd`; Petri
confirms) from the nav as the primary link, from the opening meta row, from the correspondence
section, and in the Person structured data (`sameAs`). The organisation is not linked while
every repository in it is private.

## Consequences

The link goes live in the same package that fills the profile. If the address changes, the
occurrences in `index.html` change together; the check script counts them so one cannot be
missed.
