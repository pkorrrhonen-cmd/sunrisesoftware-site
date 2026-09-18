# adr.sws.006: Premius applications are withheld until permission

| | |
|---|---|
| Status | accepted |
| Date | 2026-09-17 |
| Decided by | Petri Korhonen |
| Links | sws.site |

## Context

Premius Arki, the Premius strategy workspace, Premius Plus and Premius Planner belong to the
sphere of Premius Kuntoutus Oy, where Petri is development manager. Showing them on a Sunrise
Software page needs that company's agreement, which has not been asked. V4.5 lists "Premius
Plus" as an archive row and "Premius Planner" among the internal tools.

## Decision

No Premius application, workspace or name appears on the page until Petri has agreed it with
Premius. In the page revision the archive row and the internal-tools mention are removed. The
check script carries "Premius" as a forbidden string in `index.html`, so it cannot return by
accident.

## Consequences

The clinical discipline in §01 stays: it is Petri's, not Premius's. When permission arrives,
the forbidden string is removed, the rows return, and this decision is superseded by the one
that records the permission and its scope.
