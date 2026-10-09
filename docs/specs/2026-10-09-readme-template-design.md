# verifiably README template — design

**Status:** draft 2026-10-09, for user review. Task: vdocs-fff787, under the goal
vdocs-0f0163. Source: the brief `docs/notes/2026-10-09-readme-template-brief.md` and the
user's answers of 2026-10-09 recorded there (§5). Builds on ops's family guide templates
design (ops `docs/specs/2026-10-09-family-guide-templates-design.md`, implemented in
`ops-docs` version 3), which supplies the mechanism; this document supplies the
verifiably family's declaration, its README contract, the template, and the rollout.

## 1. Problem

A reader landing on atoms, nodes, beliefs, science or autonomy should learn in one
screen what the project is, where it sits in verifiably, how to install and use it, and
where the detail lives. Today the five READMEs share no structure (19 to 255 lines),
none introduces the ecosystem the same way, and several carry bookkeeping (atoms' Plan A
roadmap, beliefs' 85-row design table and status prose), machine-local or wrong links,
relative links that break on GitHub, "Science" as the stack's name, and stale claims.

`ops-docs` version 3 lets a family declare its own README contract and renders one
family region, the same in every member, from one file in the family's home. What
remains is to decide what verifiably's declaration says, what the README looks like
around the rendered regions, where each repository's bookkeeping goes, and how the five
repositories adopt it.

## 2. Decisions

- **One family, home here.** `family.toml` at this repository's root declares the
  `verifiably` family: its summary, the overview link, the five members in stack order,
  and the README contract. This repository is the home and is not a member: its own
  README is the map of the family and stays under the default contract.
- **The README is the sketch, in the contract's terms.** Name, slogan (the purpose, in
  italics), the ecosystem block, then `Install`, `Usage`, `Layout`, `Documentation`,
  `License`. The abstract is the overview; there is no Overview section and no status
  region. Every section is optional to the tool, as the contract makes them; the family's
  rule, enforced by review, is that every member carries `Documentation` and `License`,
  and `Install` and `Usage` wherever there is something to install or run.
- **The family region is rendered, never written.** The ecosystem summary, the overview
  link and the nav row come from `family.toml` through `ops-docs`; a member edits
  nothing there. Labels are the layer column of this repository's README table.
- **`AGENTS.md` keeps the default contract.** `family.toml` declares no `[agents]`
  table: `Setup`, `Gates`, `Layout`, `Rules` under the default budget serve the five as
  they serve every other project, and the family line that `ops-docs` renders there is
  what lore-6815ec needs.
- **Bookkeeping leaves the README for a file beside what it tracks.** Status prose and
  roadmap lists move into `docs/` indexes that the repository's own tests or guides
  already own (§7). A README names the authority for a state claim; it does not restate
  the state.
- **The header slot is the lines above the H1.** `ops-docs` does not check them. The
  template leaves them empty; the family illustration (ops-adcd29) fills them later in
  every member at once, without a contract change.
- **Package links are text, not badges.** `Install` opens with the install command and
  links the registry page. A badge is an image that says less than the line beside it.
- **Adoption is the rollout.** Each member's rollout commit is that member's adoption of
  the project guides contract (ops's wave 3 for these five): `identity.toml`, the
  vendored `tools/ops-docs`, the rendered regions, the contracted sections, the
  `AGENTS.md` reshape, the bookkeeping moves, and the brief's §2 defect fixes.

## 3. The family file

`family.toml` at this repository's root:

```toml
name = "verifiably"
summary = """
verifiably builds understanding of the world from small, reproducible data analyses:
each one a precise question asked of real data, recorded so anyone can run it again,
with the data leading and unverified claims kept out.
"""
overview = "https://github.com/verifiably/docs/blob/main/overview.md"

[[members]]
name = "atoms"
prefix = "atoms"
url = "https://github.com/verifiably/atoms"
label = "Crash-safe filesystem effects"

[[members]]
name = "nodes"
prefix = "nodes"
url = "https://github.com/verifiably/nodes"
label = "Generic record and relation storage"

[[members]]
name = "beliefs"
prefix = "beliefs"
url = "https://github.com/verifiably/beliefs"
label = "The epistemic kernel: claims, runs, verification, belief"

[[members]]
name = "science"
prefix = "sci"
url = "https://github.com/verifiably/science"
label = "The daily surface: commands for people and agents"

[[members]]
name = "autonomy"
prefix = "autonomy"
url = "https://github.com/verifiably/autonomy"
label = "Running the daily surface unattended"

[readme]
lead = ["purpose", "abstract"]
sections = ["Install", "Usage", "Layout", "Documentation", "License"]
```

- The summary is one sentence of 223 characters, inside the 300-character, two-sentence
  bound, and is the overview's first paragraph condensed. It is rendered into every
  member, so it changes only with the overview's own framing.
- Members are in stack order, bottom up, as the overview's layer table and this
  repository's README list them. `name` is each member's `identity.toml` name; `prefix`
  is its tasks prefix, which `family publish` and `family check` resolve through the
  registry (science's is `sci`).
- Labels are the README table's layer column, within 60 characters and without double
  quotes (they become link titles). When the overview's layer table changes a layer's
  description, the label and the table change together; the link checker does not tie
  them, so the README's rules say so.
- `status_before` is omitted: a status region is a finding in a verifiably README (§4).
- No `[agents]` table: the default `AGENTS.md` contract applies (§5).

`ops-docs check` in this repository (its pre-commit) validates the file; `ops-docs
family check` (added to its pre-push) judges every member's committed copy against it.

## 4. The README

What `ops-docs` renders and checks, and what the template puts around it. The
template is committed as `templates/README.md` here; a member copies it at adoption.

```
<header slot: empty lines above the H1, reserved for the family illustration>
# <name>

<!-- ops:identity start — generated by ops-docs; edit identity.toml -->
*<purpose>*

<abstract>

Authority: `<path>`
<!-- ops:identity end -->

<!-- ops:family start — generated by ops-docs; edit family.toml in the family home -->
Part of **verifiably**: <summary> [Overview](<overview>)

[atoms](… "Crash-safe filesystem effects") · [nodes](…) · **beliefs** · [science](…) · [autonomy](…)
<!-- ops:family end -->

## Install

## Usage

## Layout

## Documentation

## License
```

- **Name and slogan.** The H1 is the `identity.toml` name. The purpose line, rendered in
  italics as the lead's first part, is the sketch's slogan: at most 80 characters, what
  the thing is. The abstract follows: one to three sentences, at most 400 characters,
  what it does and for whom. Together they are the overview the sketch asked for, so
  there is no Overview section: the contract forbids one, and the two lead parts say it
  in fewer lines. The `Authority:` line names the document that is the authority for
  what is built; it is where the state of the work is read, which is why no status
  claim appears in the README.
- **The family region** directly follows the identity region, as the tool requires. The
  current member is bold and unlinked; every other member links to its repository with
  its label as the hover title. Nothing in it is edited by hand.
- **`Install`.** The install command per language, with the package's registry page
  linked in text: `pip install verifiably-atoms` with the PyPI page; `pip install
  verifiably-nodes` and `npm install @verifiably/nodes` with PyPI and npm. A member whose
  package is not published (beliefs, science) says how to run it from a checkout in one
  or two lines (`uv run` under `python/`); a member with nothing to install (autonomy
  today) omits the section.
- **`Usage`.** One real example per entry point, taken from the code or its tests, never
  invented: a CLI command with what it prints, or a library call with what it returns.
  science's lists its command surface from the authority (`tools/cli.toml`) rather than
  naming "the one shipped command". A member with nothing runnable omits the section.
- **`Layout`.** One line per top-level directory a reader needs: nodes' repo-layout
  table and beliefs' layout block already have this shape. Optional for a repository
  whose layout is only `docs/`.
- **`Documentation`.** The reading entry points, each with what it answers, in reading
  order: a contributor guide, a standard, a designs or plans index, a glossary. It links
  within the repository by relative path and across repositories by
  `https://github.com/verifiably/<repo>/blob/main/<path>`, never `../<repo>`. It does not
  repeat the `Authority:` line's document except to say where to start reading.
- **`License`.** One line naming MIT and linking the `LICENSE` file at the root. Every member ships the MIT text
  at its root (beliefs-c92ca9, sci-a2c91b, autonomy-b12f43 add the missing three; the
  rollout tasks depend on them).
- **After the contract.** A section the contract does not name goes after `License`.
  None of the five needs one in this rollout; a later one is asked, as the ops design
  asks, whether it earns its lines.
- **No status region.** The README is for a reader who wants to use the project, and
  the tracker's open goals are not that reader's question. A state claim names its
  authority, which is this repository's rule: the overview's layer table is the dated
  ecosystem snapshot, and each member's `Documentation` section points at the document
  that holds its own state (§7).

Prose rules, in the template's comments and checked by review: refer to the stack as
verifiably, never "Science" (the predecessor's name; `science` is the daily-surface
layer, and rule identities such as `science.identity.v1` keep their names); no
machine-local paths; no relative links into a sibling repository.

## 5. `AGENTS.md`

The default contract, unchanged: H1 `<name> — agent guide`, the identity region
(purpose only), the family line region directly after it, then `Setup`, `Gates`,
`Layout`, `Rules`, within the 120-line budget. `ops-docs write --init` inserts both
regions; the family line reads
`Member of the verifiably family (<overview>); this repository's guides follow its contract in tools/family.toml.`

The reshape each rollout makes: an authority-order or conventions section becomes
`Rules` (what is true here and stated nowhere in the global layer, each rule naming the
failure it prevents); a gates or session-protocol section becomes `Gates`; a status or
roadmap section leaves the file (§7); a restatement of the tasks skill or the core rules
is deleted. A member that cannot fit the budget declares a raise in `identity.toml`; none
of the five is expected to need one once status prose is gone.

## 6. The header slot

The lines above the H1. `ops-docs` checks nothing there, so the illustration lands
without a contract change. The template keeps the slot empty rather than holding a
placeholder comment: five READMEs carrying an HTML comment for a picture that does not
yet exist is noise for every reader until then. ops-adcd29 designs the illustration
(one image, five variants with the member's layer highlighted) and adds it to each
member in its own rollout; the template's comments name the slot so that work knows
where it goes.

## 7. Where each repository's bookkeeping moves

| Repository | Leaves the README (and `AGENTS.md`) | Goes to |
|---|---|---|
| atoms | `## Status` (the Plan A roadmap, A1–A9, with per-plan links) and `AGENTS.md`'s `## Status: Plan A in progress` | `docs/plans/README.md`, a Plan A roadmap index: the authority, each sub-plan with its design and plan links and its implemented or remaining state. `python/tests/test_docs_status.py` reads it in place of the two guides, so the one-roadmap-fact guard keeps working; the test's "entry documents" become the index. |
| atoms | `## Scope`, `## Design decisions`, `## Future hardening and extensions` | Dropped: the authority design holds them (the README says so itself). The public preimage contract and the capability model get their lines in `Documentation`. |
| atoms | `## Relationship to Beliefs` | Dropped; one sentence in the plans index says Beliefs' adoption is governed by Beliefs' adoption ledger. |
| atoms | `AGENTS.md` `## Deferred obligations`, `## Authority order`, `## Conventions` | `Rules` names the deferred-obligation ledger and the authority order; conventions that restate the global layer are deleted. |
| nodes | `## Architecture` (the two-layer diagram) | Dropped; the abstract states the layering in words and `docs/STANDARD.md` is the authority. |
| nodes | `## Development` (just recipes) | `AGENTS.md` `Gates`. |
| nodes | `## Consumers` with `~/d/...` paths | The abstract names beliefs and mindful v6 as the profiles built on it; the machine-local paths go. |
| beliefs | `## The designs` (the 85-row table and its read-order guidance) and the clean-start paragraph naming `proto-science` | `docs/designs/README.md`, a designs index: the same table, the reading order, and the predecessor paragraph (the `proto-science` link stays under `khughitt`, where that repository is). The contributor guide's "Read in this order" links the index. |
| beliefs | `## Status` (the implementation tally) | Deleted. The adoption ledger's current-state summary is the sole authority for what is built, as the contributor guide already states; `Documentation` links it. |
| beliefs | The layout code block | `## Layout`. |
| beliefs | `AGENTS.md` `## Authority`, `## Repository gates`, `## Tasks workflow`, `## Design documents`, `## Cut plans` | `Rules`, `Gates`, deleted, `Layout` and `Rules` respectively. |
| science | "the one shipped command, `status`" | `Usage` lists the command surface from `tools/cli.toml`; the sub-project list stays in the command-framework design, which `Documentation` names. |
| science | `AGENTS.md` `## Session protocol` | `Gates` (the test recipes, hooks and their classification) and `Rules` (what is true only here); the tasks restatements are deleted. |
| autonomy | Nothing to move: 19 lines | A new `identity.toml` and `AGENTS.md`; the README is lead, family region, `Documentation` and `License`. |

The destinations are the ones the brief left open: atoms' roadmap goes beside its plans
rather than into the tracker, because its test guards the roadmap as a document and
a tracker goal cannot carry per-plan links; beliefs' table goes to a designs index
rather than into the contributor guide, because the guide is curated prose under its own
freshness rules and the table is a catalogue.

## 8. Identity values, drafted

Each rollout confirms these against the code before committing them. Purposes are
within 80 characters; abstracts within 400 and three sentences.

| Member | purpose | abstract | authority |
|---|---|---|---|
| atoms | A recoverable filesystem effect engine: the crash-safe substrate | Atomic multi-path filesystem mutation with write-ahead journaling, rollback and post-crash recovery, over an OS-neutral capability vocabulary: a write either lands completely or leaves a state that can be classified from durable evidence and safely completed, rolled back or halted. The physical substrate under nodes; beliefs is its direct consumer. | `docs/plans/2026-07-23-recoverable-fs-effect-engine-design.md` |
| nodes | A problem-agnostic knowledge substrate: typed markdown nodes | Entities as markdown files, typed relations, structural shapes and rebuildable derived indexes, implemented in Python and TypeScript over one shared on-disk format. The kernel is domain-free; domain profiles such as beliefs and mindful v6 register their own kinds on it. | `docs/STANDARD.md` |
| beliefs | The epistemic kernel of verifiably: recording scientific belief | Records scientific belief and the evidence it rests on: typed claims, datasets and holdings, analysis runs and their verification, belief computed on request under a named policy, the world index, additive correction and the mutation log, each guaranteed by a frozen conformance cut. Built on nodes and atoms; consumed by science and autonomy. | `docs/designs/2026-08-02-epistemic-kernel-design.md`, `docs/designs/2026-08-03-redesign-adoption-ledger.md` |
| science | The daily surface of verifiably: the layer people and agents use | Harness-neutral commands and skills over the beliefs kernel, served as a CLI and over MCP, with generated harness adapters (Claude Code first), the derived work queue and publish. It owns no kinds and no storage: every durable thing is a governed record in a beliefs corpus, and every write is a kernel act. | `docs/specs/2026-08-31-command-framework-design.md` |
| autonomy | The envelope and orchestrator of verifiably: what may run unattended | What may run unattended, under what tier, and how the next research action is chosen: the run baseline and dispositions, tiers as write-class permits, the actor sandbox and session ledger, behavioural profiles and the versioned priority function. It drives science's commands as tools and holds no private kernel access. Designed, not started. | none tracked here; `Documentation` links the governing design in beliefs by URL |

`subsystems` is empty in every member for this rollout (§12).

## 9. Rollout

Six commits in six repositories, the home first and then the members smallest first,
as ops's wave rule has it, so the template is corrected on the small files before the
large ones. The plan files the home's work as its own steps here and one rollout task in
each member project; the goal vdocs-0f0163 depends on the five.

1. **Home (this repository).** `family.toml` (§3); `templates/README.md` (§4), with
   its guidance as HTML comments; `family check` added to the pre-push recipe; this
   README's and `AGENTS.md`'s layout lines name the two files; the README's rules note
   that a layer description changes in the table and the label together. Then
   `tools/ops-docs family publish`, which writes `tools/family.toml` into every reachable
   member (a copy only, until the member adopts). The home's push waits for step 6: its
   pre-push `family check` reports `missing` until every member has committed its copy.
2. **autonomy** (19 lines, nothing built): vendors `tools/tt`, `tools/ops-check` and
   `tools/ops-docs` from ops main, takes ops's template `justfile` and `.githooks` with
   no-op test commands so its pre-commit runs `ops-docs check`; `identity.toml`;
   `AGENTS.md` from the template; the README to §4; the relative `../beliefs/` link
   becomes a GitHub URL; "Science" becomes verifiably. Closes autonomy-6e0015. Depends on
   autonomy-b12f43.
3. **science** (21 lines): vendors `tools/ops-docs`; adds `ops-docs check` to its check
   commands; `identity.toml`; the README to §4 with `Usage` from `tools/cli.toml`; the
   `AGENTS.md` reshape (§7); the relative link and "Science" fixed. Closes sci-edc546.
   Depends on sci-a2c91b.
4. **nodes** (54 lines): as science, plus the moves in §7; `Install` and `Usage` for
   both packages, the usage examples from `python/README.md` and `ts/README.md`.
5. **atoms** (140 lines): as nodes, plus `docs/plans/README.md` and the
   `test_docs_status.py` change, proven by the suite before and after the move.
6. **beliefs** (255 lines): as nodes, plus `docs/designs/README.md`, the `khughitt`
   links corrected to `verifiably`, and the contributor guide's pointer to the index.
   Depends on beliefs-c92ca9. Then the home runs `family check`, pushes, and the
   outcome is noted on vdocs-910898 and on ops's project guides design task record.

Within a member, the order is: vendor `tools/ops-docs`, write `identity.toml`, copy the
template over the README's head; from the home, `family publish` (which now finds the
member adopted and runs its `ops-docs write --init`, inserting both regions); then the
prose and moves; then `just check` in the member and one commit, with the member's
status-guard or link tests green. The home's `family publish` never commits; the
member's commit carries `tools/family.toml` with the rest.

## 10. Checks

| Where | Check | Reads |
|---|---|---|
| member pre-commit (`ops-docs check`) | `tools/family.toml` valid and listing the member; identity and family regions current; sections in contract order; no status region; `AGENTS.md` within budget | the member's tree |
| member tests | atoms: the roadmap index agrees with the implemented boundary; nodes, beliefs: unchanged | the member's tree |
| home pre-commit (`ops-docs check`, `check_links.py`) | `family.toml` valid; every `https://github.com/verifiably/<repo>/blob/main/<path>` link resolves in the sibling checkout | the home's tree and siblings |
| home pre-push (`ops-docs family check`) | every member's committed copy equals the home's | registered member checkouts |
| ops pre-push (`vendored check`) | `tools/ops-docs` current in the five | as today |
| review | the family's prose rules (§4): verifiably not "Science", no machine-local paths, no `../<repo>` links, `Documentation` and `License` present | the rollout commit |

## 11. Alternatives rejected

- **An Overview section.** The sketch's overview is the purpose line and the abstract,
  which the lead renders; a third telling of what the project is would be the drift the
  identity file exists to prevent.
- **A status region before `License`.** The tracker's goal counts answer a maintainer's
  question, not a reader's, and would make every goal change a README commit in five
  repositories.
- **A `Consumers` section.** Within the family, the nav row shows the neighbours;
  outside it, one consumer (mindful v6 of nodes) fits in the abstract's "for whom".
- **Badges.** An image per package that says less than the install line beside it, and
  one more external fetch per README render.
- **A placeholder comment in the header slot.** Noise in five files until the
  illustration exists; the template's comments carry the pointer instead.
- **Listing the home as a member.** This README is the family's map, with the table
  and the overview; rendering the nav into it would link every member from a page that
  already does, and put the home under a contract written for packages.
- **Moving beliefs' design table into the contributor guide.** The guide is curated
  prose with its own freshness rules; an 85-row catalogue belongs in an index beside the
  designs it lists.
- **Moving atoms' roadmap into the tracker.** Its status test guards a document with
  per-plan links; a tracker goal carries neither.

## 12. Deferred

- **Subsystems.** nodes, atoms and beliefs have package READMEs under `python/` and
  `ts/`; declaring them means an `identity.toml` and `AGENTS.md` in each. A later task
  per repository, once the root guides have settled.
- **The header illustration**: ops-adcd29, its own design.
- **`AGENTS.md` family conventions in agent context**: lore-6815ec, from the rendered
  family line.
- **A family for the agent tooling** and the atlas's family grouping: the ops design's
  §10.
