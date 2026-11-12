# adr.sws.019: the structured data names the products

| | |
|---|---|
| Status | accepted (Petri, 11.11.2026, round 1 of the status review); amended 12.11.2026 (round H, a sub-page's own video) |
| Date | 2026-11-11 |
| Decided by | Petri Korhonen |
| Amends | the decision of 18.9.2026, "JSON-LD for Organization and Person only" (SEED v3.0.0 section 5.3) |
| Links | sws.site |

## Context

On 18.9.2026 Petri decided that the page's JSON-LD describes the company and the person and
nothing else, to keep the structured data honest and small. That held while the question was
what a search engine shows for the company's name.

The question has changed. A reader now often arrives through a machine that was asked what
Sunrise Software makes, and that machine finds the products only as prose and links. Nothing on
the page says in a machine-readable way that `masterforge.app`, `luviamo.app`,
`virustutka.app`, `ultragravel.app`, `tilastosilta.fi` and `sf3d.fi` belong to the same
company, which is also the fact a search engine uses to connect them.

## Decision

The front page's `@graph` gains, beside the Organization and the Person:

- a `WebSite` with `name`, `url` and `publisher` pointing at the Organization
- `sameAs` on the Organization naming the product domains and the GitHub profile
- one `SoftwareApplication` per product anyone can open, each with `name`, `url`,
  `applicationCategory`, `operatingSystem` where it means something, and `author` pointing at
  the Person and `publisher` pointing at the Organization. These are five: MasterForge,
  Luviamo, Virustutka, Ultra Gravel and TilastoSilta. An entity promises an application the
  reader can use, and that promise does not hold for SpectralForge (closed beta), ReviewGlass (a
  repository rather than a service), Somnus, Atlas, Salpa Defence or HomeTeam, so none of them
  gets one
- SF3D AI Lab as a `WebSite` with its own description and `author` pointing at the Person: it is
  a research lab site, as the page says, not an application. Round C on 11.11.2026 had it as the
  sixth application; corrected on 12.11.2026 before it shipped (copy-v4-pages.md D.1)
- `logo` on the Organization, pointing at `/icon-512.png` (adr.sws.017)

A sub-page carries only what it is about: a `WebPage` with `isPartOf` the WebSite, plus the one
`SoftwareApplication` or `CreativeWork` that page describes. No entity appears on a sub-page
that the front page does not also know.

No entity carries a version number, a price, a rating or a review count. Those age silently,
and a rating nobody gave would be a lie in a machine-readable field (adr.sws.015 is the same
rule in the same spirit).

## Consequences

An answer engine asked about the company finds a list of products with their addresses instead
of prose it has to parse. A search engine can connect the product domains to the company.

The structured data is now a place where a fact can go stale, so it joins the page in the
session routine: a product's row is checked from its repository or its live service in the same
session as any page change that touches it, and a product that stops being live loses its
entity in the same pull request as its status line changes.

The 18.9.2026 decision is not withdrawn in spirit: the structured data still describes only
what the page itself says, and it still carries no claim the page does not make.

## Amendment, 12.11.2026: a sub-page's own video

Decided by Petri in round H of `docs/design/copy-v4-pages.md`, while the copy of `/silent-context/`
was decided.

A sub-page whose lead medium is a video of its own describes that video as a `VideoObject`
(`name`, `description`, `thumbnailUrl` the poster, `contentUrl` the site's own file, `uploadDate`,
`duration`), so that a search engine can show the video for the page. This is the one entity a
sub-page may carry that the front page does not, because the video plays only on its page (SEED
v4.0.0 section 3.6). It carries no view count, no rating and no interaction statistics, for the
same reason as the rest of this decision.

A sub-page about something that is code rather than a service describes it as a
`SoftwareSourceCode` (`codeRepository`, `license`, `programmingLanguage`, `author` the Person). The
front page's graph gains the same entity in the same pull request, so the rule that a sub-page names
nothing the front page does not know still holds for everything but the video. The first is Silent
context: `/silent-context/` carries `WebPage`, `SoftwareSourceCode` and `VideoObject`.
