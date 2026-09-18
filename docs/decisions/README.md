# Decisions

One file per architecture decision, in the record shape Atlas uses for every system
(`id`, `title`, `context`, `decision`, `consequences`, `status`, `links`). The ids continue
the numbering Atlas already holds for this site (`adr.sws.001` and `002` were first recorded in
`model/systems/sw-sivusto.model.json`); this folder is the source and Atlas is the mirror.

A decision is `accepted`, `proposed` (waiting for Petri) or `superseded` (by a named later
decision). A decision is never deleted: a wrong one is superseded and the file says by what.

| Id | Title | Status |
|---|---|---|
| [adr.sws.001](adr.sws.001.md) | Static HTML with no build step | accepted |
| [adr.sws.002](adr.sws.002.md) | Editorial numbered-section architecture over the SaaS landing pattern | accepted |
| [adr.sws.003](adr.sws.003.md) | The SF3D history is a footnote, and the heritage lives at sf3d.fi | accepted |
| [adr.sws.004](adr.sws.004.md) | Every status on the page carries a date; no relative-time copy | accepted |
| [adr.sws.005](adr.sws.005.md) | Atlas is selected work, and its cover is a drawn schematic | accepted |
| [adr.sws.006](adr.sws.006.md) | The employer's applications are withheld until permission | accepted |
| [adr.sws.007](adr.sws.007.md) | The public GitHub profile is linked from the page | accepted |
| [adr.sws.008](adr.sws.008.md) | The React migration leaves the roadmap | proposed |
| [adr.sws.009](adr.sws.009.md) | Documentation follows the family standard | accepted |
| [adr.sws.010](adr.sws.010.md) | The look is the sunrise over the sea, palette A shifted a little toward C | accepted |
| [adr.sws.011](adr.sws.011.md) | Flow 1 is the direction of the page | accepted |
| [adr.sws.012](adr.sws.012.md) | The typefaces are Familjen Grotesk and Public Sans | accepted |
| [adr.sws.013](adr.sws.013.md) | Flow 4 is the page; SEED v3.0.0 records it | accepted |
