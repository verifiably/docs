# README template for the verifiably repositories — brief

Scoping handoff for vdocs-910898 (source: mindful thought `62b569ab`). Written
2026-10-09.

## 1. Problem

A reader landing on any of the five repositories (atoms, nodes, beliefs, science,
autonomy) should learn in one screen what the project is, how it fits into
verifiably, how to install and use it, and where the detail lives. Today the five
READMEs differ in structure and length (19 to 255 lines), none introduces the
ecosystem in the same way, and several carry stale or machine-local content. The
outcome wanted is a template, kept here in verifiably/docs, that all five follow.

## 2. Current behaviour and evidence

Audit of each `README.md` at its checkout's `main`, 2026-10-09:

| repo | lines | install / usage | ecosystem link | defects found |
|---|---|---|---|---|
| atoms | 140 | none | none | `## Status`, design decisions and future work are bookkeeping that belong in `docs/` |
| nodes | 54 | `## Development` (just recipes) | none | `## Consumers` links `~/d/mindful/v6/`, `~/d/beliefs/` |
| beliefs | 255 | none | yes, to the overview | 85-row design table and status prose; links `khughitt/nodes`, `khughitt/atoms`, `khughitt/proto-science` (org moved to `verifiably`); calls the stack "Science"; no LICENSE |
| science | 21 | none | none | relative `../beliefs/...` link (breaks on GitHub); "the one shipped command, `status`" while `commands/` holds 18 entries (likely stale); calls the stack "Science"; no LICENSE |
| autonomy | 19 | none (nothing built) | none | relative `../beliefs/...` link; calls the stack "Science"; no LICENSE |

Packages: `verifiably-atoms` 0.1.0 and `verifiably-nodes` 0.2.0 are on PyPI,
`@verifiably/nodes` 0.2.0 on npm; `verifiably-beliefs` and `verifiably-science` are
not published. All six GitHub repositories answer publicly.

None of the five has adopted ops's project-guides contract (ops
`docs/specs/2026-09-22-project-guides-design.md` §4, template ops
`templates/README.md`): no `identity.toml`, no `ops:identity` region. This repository
has adopted it. That design's wave 3 (adoption, including all five) has no open task
in ops.

## 3. Constraints

- **ops's README contract** fixes the order: `# <name>`, the rendered identity region
  (abstract, authority, subsystems), `## Setup`, `## Usage`, `## Layout`, an optional
  status region, `## Consumers`. It rejects an "Overview" or "Architecture" section
  (the abstract and the authority pointer are the overview) and any roadmap; extra
  sections go after the contracted ones. `identity.toml`'s `purpose` (≤ 80 chars) is
  already the sketch's slogan; its `abstract` (≤ 400 chars) is the overview.
- **This repository's rules**: ecosystem level only, so the template must not
  restate a repository's mechanics; cross-repository links use
  `https://github.com/verifiably/<repo>/blob/main/<path>`.
- **Open work touching the same files**: autonomy-6e0015 and sci-edc546 (point the
  README at the overview); ops-adcd29 (a layered stack infographic per README) and
  forge-524404 (per-repo character art) compete for the header slot; ops-81f03b (the
  cross-family goal) depends on this task; lore-6815ec (family conventions in agent
  context); ops-42d180 (docs/ layout); atoms-8be2dc (A9, the one remaining Plan A item
  atoms' status section tracks).

## 4. Alternatives

1. **Family layer on the ops contract** (lean). The template is ops's README plus a
   verifiably block right after the identity region: a two-line ecosystem summary,
   a link to the overview, and a nav row of the five repositories with the current
   one unlinked; a `## License` section after `## Consumers`; package badges or links
   in `## Setup`. Adopting the template *is* wave 3 for these five, so one commit per
   repository does both. The block could be rendered (an ops-docs region fed from a
   family list here) or a static snippet the link checker verifies.
2. **A standalone verifiably template** following the sketch (logo, slogan, block,
   overview, installation, usage, docs links, license). Closer to the sketch, but it
   conflicts with the ops contract's "no Overview" rule and its section order, so
   either ops-docs check fails on these repositories or they are exempted.
3. **Ecosystem pointer only**: do autonomy-6e0015 / sci-edc546 everywhere and move
   bookkeeping to `docs/`, no shared template. Cheapest, but leaves structure to drift.

## 5. Unanswered questions

Answered by the user 2026-10-09:

- **Template vs the ops contract**: neither alternative 1 nor 2 as written.
  READMEs should differ by project family, so the ops contract becomes one template
  among several: ops-docs is generalized to render and check a contract chosen by
  the project's family, the current one as the default (ops-a0318e; whether doc
  rendering moves to lore is open there). verifiably then adopts its own template,
  which may keep the sketch's shape.
- **The verifiably block** is rendered by that generalized tool from the family's
  declared member list (ops-a0318e).
- **Header art**: a custom verifiably family illustration close to the stack
  infographic (ops-adcd29), designed in its own session; the template reserves the
  slot.
- **Licence**: MIT everywhere, which atoms and nodes already ship and beliefs already
  declares in its package metadata (beliefs-c92ca9, sci-a2c91b, autonomy-b12f43). Side
  ideas: a licence preference new projects inherit (ops-4ff1a0), waiting on
  conventions for user preference config (ops-0e42cd).

Still open, for the design: where each repository's bookkeeping moves (atoms status
→ its plan or the tracker; beliefs' design table → `docs/designs/README.md` or the
contributor guide).

## 6. Proposed decomposition

- vdocs-910898 (this idea) stays an idea under the goal vdocs-0f0163, waiting on
  the design.
- ops-a0318e — per-family guide templates in ops-docs (planned).
- vdocs-fff787 — design the verifiably template from this brief (planned; spec
  reviewed by the user), after ops-a0318e. Its plan files one rollout task per
  repository, absorbing autonomy-6e0015 and sci-edc546 and correcting the defects in §2.
- beliefs-c92ca9, sci-a2c91b, autonomy-b12f43 — add the MIT LICENSE; independent of
  the template.
