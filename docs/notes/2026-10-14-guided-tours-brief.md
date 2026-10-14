# Guided tours of the ecosystem — brief

Scoping handoff for vdocs-c96d1b (source: mindful thought `f8b1c13f`). Written
2026-10-14.

## 1. Problem

The user wants to understand the verifiably codebases and systems well enough to steer
them, not only to read about them. The idea: an agent walks them through the
ecosystem at several scales (a guided, multiscale tour), pauses to check what has
been understood, and closes by distilling what was learned (self-assessment). Personal
learning comes first; polishing the result into this repository, or elsewhere, waits
until it has proved useful.

## 2. Current behaviour and evidence

- No tour exists. Nothing in this repository or its notes mentions one.
- The ecosystem already has a written ladder of scales, each with a named owner:
  1. **Ecosystem**: `overview.md` (266 lines), goal first, then the layers.
  2. **Layer**: the repository map in `README.md`, whose layer column is each member's
     label in `family.toml`.
  3. **Repository**: each member's `identity.toml` (an 80-character purpose, an
     abstract of at most three sentences, and `authority`, the design documents that
     decide what is built), rendered into its `README.md` and `AGENTS.md` by
     `ops-docs`.
  4. **Subsystem**: package READMEs under `python/` and `ts/` in nodes and beliefs,
     and `python/` in atoms. None is declared yet; vdocs-946c49 declares them, which
     gives each one its own purpose and abstract.
  5. **Design and code**: the `authority` documents, then the code they govern.
- `ops-projects` renders the cross-project block from the same identity files. The
  on-demand atlas planned in ops's project-guides design §9 (step 5) is not built:
  `ops-projects` has `render`, `pull`, `write`, `register`, `link` and `check`, and
  no `atlas`.
- The source thought also holds a separate idea: autonomy defaults tuned from real
  data, with the system pausing to check the user's understanding or their agreement
  with what they intended. This idea captured only the tour; the autonomy idea has no
  task here or in autonomy.

## 3. Constraints

- **Ecosystem level only** (this repository's `AGENTS.md`): a repository's own
  mechanics live in its own guide. Written tours here would restate kernel detail,
  which is how it drifts.
- **The goal comes first**: understanding the world from small, reproducible analyses.
  A tour that starts from the machinery breaks the overview's own rule.
- **Personal first** (the idea's body): work it in a worktree here, and commit nothing
  shared until it has proved useful.

## 4. Alternatives

- **A. A live tour, led by an agent (lean).** One session walks down the ladder in §2,
  reading the identity files and authority documents as it goes, and at each scale
  stops for a check: explain it back, predict what a command will do, or say which
  repository owns a behaviour. It ends with a short distillation. Nothing is written
  ahead of time, so nothing drifts. Whatever works can become a skill later.
- **B. Written tours in this repository** (`docs/tours/<scale>.md` with check
  questions). These are reusable by other people, but they restate what the members'
  guides own, against the ecosystem-level rule, and go stale with every design
  change.
- **C. Tours rendered from the identity tree**: the atlas plus generated questions.
  This stays current by construction, but it depends on the unbuilt atlas, and it is
  tooling before anyone knows what a good tour looks like.

## 5. Unanswered questions

- Which scales and which repositories come first, and whether "codebases and systems"
  reaches past verifiably into the shared tooling (ops, tasks, lore)? **The user.**
- What kind of check helps: quiz questions, explaining it back, predicting behaviour, or
  choosing between options? **The pilot** (vdocs-9ca77b).
- Where the distillation lands: a mindful thought, a note here, or a task? **The user,
  after the pilot.**
- Whether the tour's checks share a mechanism with autonomy's pausing to check
  understanding, from the same thought? **The user**; it would be filed in autonomy if
  it is pursued.

## 6. Proposed decomposition

- **vdocs-9ca77b** (under goal vdocs-d2d5ed): pilot one live tour (alternative A) over one repository and
  record what worked. vdocs-c96d1b waits on it.
- vdocs-946c49, already scoped, adds the subsystem scale. The pilot does not need it.
