# adr.sws.019: the structured data names the products

| | |
|---|---|
| Status | accepted (Petri, 11.11.2026, round 1 of the status review) |
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
  the Person. Decided on 11.11.2026, these are the six: MasterForge, Luviamo, Virustutka,
  Ultra Gravel, TilastoSilta and SF3D AI Lab. An entity promises an application the reader can
  use, and that promise does not hold for SpectralForge (closed beta), ReviewGlass (a repository
  rather than a service), Somnus, Atlas, Salpa Defence or HomeTeam, so none of them gets one

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
