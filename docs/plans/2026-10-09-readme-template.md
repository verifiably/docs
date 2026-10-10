# verifiably README template Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** This repository declares the verifiably family and its README template, and
each of atoms, nodes, beliefs, science and autonomy adopts it in one commit that also
fixes its README's known defects.

**Architecture:** The home (this repository) commits `family.toml`, the README template
and a pre-push `family check`. Each member's rollout runs in that member's own task
worktree: it vendors `tools/ops-docs`, copies the home's committed family file byte for
byte, writes `identity.toml`, lays the template over its README, renders both guide
regions with its own `ops-docs write --init`, moves bookkeeping into `docs/` indexes,
and lands as one commit. The home's pre-push `family check` passes once the five
merges are on each member's `main`.

**Tech Stack:** `ops-docs` version 3 (Python 3 standard library, vendored), `just`,
the tasks CLI, this repository's `tools/check_links.py`.

**Spec:** `docs/specs/2026-10-09-readme-template-design.md` (accepted 2026-10-09, review
round 2). Its mechanism is ops `docs/specs/2026-10-09-family-guide-templates-design.md`.

## Global Constraints

- Family file limits, checked by `ops-docs` wherever the file is read: `summary` at most
  300 characters and two sentences; each `label` a single line of at most 60 characters
  with no `"`; each `url` `https://`; `name` and `prefix` unique across members.
- Identity limits: `purpose` at most 80 characters, one line; `abstract` at most 400
  characters and three sentences; every `authority` path exists and is tracked.
- `AGENTS.md` within the default 120-line budget; sections `Setup`, `Gates`, `Layout`,
  `Rules`, in that order, any omitted.
- README sections, in order, any omitted: `Install`, `Usage`, `Layout`,
  `Documentation`, `License`. No status region. The family region directly follows the
  identity region.
- Prose rules (spec §4): the stack is "verifiably", never "Science" (rule identities
  such as `science.identity.v1` keep their names); no machine-local paths (`~/d/...`);
  no `../<repo>` links; cross-repository links are
  `https://github.com/verifiably/<repo>/blob/main/<path>`.
- Every rollout happens in that member's own task worktree, never in its main checkout;
  `family publish` is not used during the rollout (spec §9).
- Commits use conventional commit messages, no attribution trailers.
- Plan clarifications of the spec (bounded choices, stated so a reviewer can check
  them): the home's link checker skips `templates/`, because a template's relative links
  resolve in the member that copies it, not here; autonomy's justfile sets every test
  command to `true` until something is built, so its hooks run `ops-docs check` today;
  nodes' and beliefs' `docs_paths` allowlists keep README.md out, as their guides
  already require, so a README commit runs the full check there.

## Review Focus

1. A member whose `identity.toml` name differs from its `family.toml` member name
   (`science` vs `sci`): `ops-docs check` must report the copy as not listing the
   repository, and the nav must not bold the wrong entry. Pinned in Rollout 2, step 7.
2. The home's `family check` before any member has committed its copy: five `missing`
   lines and exit 1, never a pass. Pinned in Task 3, step 4.
3. A README section out of contract order (`License` before `Documentation`):
   `ops-docs check` exit 1 naming the section. Pinned in Task 2, step 4.
4. atoms' roadmap index disagreeing with `FIRST_UNIMPLEMENTED` after the move: the
   status test must still fail on a stale claim in the index. Pinned in Rollout 4,
   step 5.
5. The template's relative licence link, read by this repository's link checker:
   it must be skipped here and verified in a member. Pinned in Task 2, steps 2 and 3,
   and the link check in every rollout's common step 8.

## Conventions

No machine-specific path appears below. Every command that reaches another checkout
resolves it through the tasks registry first; run this once per shell:

```bash
root() { tasks resolve --json "$1" | python3 -c 'import sys, json; print(json.load(sys.stdin)["results"][0]["root"])'; }
OPS=$(root ops); DOCS=$(root vdocs)
```

`$OPS` is the ops checkout (the source of `bin/ops-docs` and `templates/`), `$DOCS`
this repository's main checkout (the home). A member's own root is `$(root <prefix>)`
with the prefixes `atoms`, `nodes`, `beliefs`, `sci`, `autonomy`.

---

## File structure

Home (this repository, on branch `design/readme-template` in
`.worktrees/readme-template`):

- Create `family.toml` — the family declaration (spec §3).
- Create `templates/README.md` — the README skeleton a member copies (spec §4).
- Modify `tools/check_links.py` — skip `templates/`.
- Modify `justfile` — `hook-pre-push` also runs `family check`.
- Modify `README.md`, `AGENTS.md` — layout lines for the two new files; the label rule.

Each member (its own worktree): `tools/ops-docs`, `tools/family.toml`, `identity.toml`,
`README.md`, `AGENTS.md`, `justfile`; plus per member the files its rollout names.

---

### Task 1: The family file

**Files:**
- Create: `family.toml`

**Interfaces:**
- Produces: `family.toml` at the home root, read by `tools/ops-docs check` here and
  copied byte for byte into each member as `tools/family.toml` (Rollouts 1–5).

- [ ] **Step 1: Write the file with one deliberate constraint breach**

Write `family.toml` exactly as spec §3 gives it, except make beliefs' label too long,
so the first check proves the gate reads the file:

```toml
label = "The epistemic kernel: claims, runs, verification, belief, and the world index"
```

- [ ] **Step 2: Run the check and see it refuse**

Run: `python3 tools/ops-docs check; echo exit=$?`
Expected: a line containing `label must be a single line of at most 60 characters`, `exit=1`.

- [ ] **Step 3: Restore the spec's label**

```toml
label = "The epistemic kernel: claims, runs, verification, belief"
```

The whole file, for comparison, is spec §3 verbatim: `name`, `summary`, `overview`,
five `[[members]]` tables in the order atoms, nodes, beliefs, science, autonomy, and
`[readme]` with `lead = ["purpose", "abstract"]` and
`sections = ["Install", "Usage", "Layout", "Documentation", "License"]`. No
`status_before`, no `[agents]`.

- [ ] **Step 4: Run the check and the render probe**

Run: `python3 tools/ops-docs check; echo exit=$?`
Expected: no output, `exit=0`.

Run the render probe from the scratchpad (it loads the vendored script as a module):

```bash
( S=$(mktemp -d) && cp tools/ops-docs family.toml "$S/" && cd "$S" && python3 - <<'EOF'
import pathlib
ns = {}
src = pathlib.Path("ops-docs").read_text().replace('if __name__ == "__main__":', 'if False:')
exec(compile(src, "ops-docs", "exec"), ns)
fam = ns["load_family"](pathlib.Path("family.toml"))
assert ns["family_problems"](fam) == []
assert [m["name"] for m in fam["members"]] == ["atoms", "nodes", "beliefs", "science", "autonomy"]
assert ns["contract_of"](fam)["readme"]["sections"] == ["Install", "Usage", "Layout", "Documentation", "License"]
print(ns["render_family"](fam, {"name": "science"}, "readme", "tools/family.toml"))
EOF
)
```

The subshell leaves the working directory where it was.

Expected: the region prints with `**science**` bold and the other four as links whose
titles are their labels.

- [ ] **Step 5: Commit**

```bash
tasks done vdocs-d68fd2 "family.toml declared and validated by ops-docs check"
git add family.toml tasks/
git commit -m "feat: declare the verifiably family and its README contract"
```

---

### Task 2: The README template

**Files:**
- Create: `templates/README.md`
- Modify: `tools/check_links.py` (the `SKIP_DIRS` line)

**Interfaces:**
- Produces: `templates/README.md`, copied over a member's README head in every rollout.

- [ ] **Step 1: Write the template**

```markdown
# <name>

<!-- ops:identity start — generated by ops-docs; edit identity.toml -->
<!-- ops:identity end -->

<!-- ops:family start — generated by ops-docs; edit family.toml in the family home -->
<!-- ops:family end -->

<!-- verifiably README template (verifiably/docs templates/README.md). The lines above the
H1 are the header slot for the family illustration; leave them empty until it exists.
The H1 is the identity.toml name. The two regions are rendered by `tools/ops-docs write`
(purpose in italics, abstract, authority; then the family summary and nav); edit
identity.toml and the family file in verifiably/docs, never the regions. Sections below
are optional but keep this order; Documentation and License are always present. Say
"verifiably" for the stack, never "Science". No machine-local paths, no ../<repo>
links: link across repositories with https://github.com/verifiably/<repo>/blob/main/<path>.
Delete this comment in the copy. -->

## Install

<The install command per language, with the registry page linked in text; or how to run
from a checkout when nothing is published. Omit when there is nothing to install.>

## Usage

<One real example per entry point, taken from the code or its tests: a command with what
it prints, or a call with what it returns. Omit when nothing runs.>

## Layout

<One line per top-level directory a reader needs. Omit when the layout is only docs/.>

## Documentation

<The reading entry points in reading order, each with what it answers: a guide, a
standard, a designs or plans index, a glossary. Relative links within the repository.>

## License

MIT, see [LICENSE](LICENSE).
```

- [ ] **Step 2: Run the link checker and see it refuse the template**

Run: `python3 tools/check_links.py; echo exit=$?`
Expected: `templates/README.md: missing target: LICENSE`, `exit=1`.

- [ ] **Step 3: Skip `templates/` in the link checker**

In `tools/check_links.py`, change the skip set:

```python
SKIP_DIRS = {".git", "tasks", ".worktrees", ".tt", "templates"}
```

and add after the module docstring's last sentence:

```
Files under `templates/` are skipped: a template's relative links resolve in the
repository that copies it, not here.
```

Run: `python3 tools/check_links.py; echo exit=$?`
Expected: only `skipped:` lines (none from the main checkout, five from a worktree),
`exit=0`.

- [ ] **Step 4: Prove the template passes the contract in a member-shaped repository**

Build a scratch member from the template, ops's `AGENTS.md` template and this family
file, and run its check; then break the order and see it refuse:

```bash
( H=$PWD && S=$(mktemp -d) && cd "$S" && git init -q . && mkdir tools \
 && cp "$H/tools/ops-docs" tools/ && cp "$H/family.toml" tools/family.toml \
 && cp "$H/templates/README.md" README.md \
 && cp "$OPS/templates/AGENTS.md" AGENTS.md \
 && printf 'name = "science"\naliases = []\npurpose = "Probe"\nabstract = "A probe."\nauthority = []\nsubsystems = []\n' > identity.toml \
 && sed -i 's/^# <name>$/# science/; s/^# <name> — agent guide$/# science — agent guide/' README.md AGENTS.md \
 && sed -i '/^<!-- verifiably README template/,/^Delete this comment in the copy. -->$/d' README.md \
 && python3 tools/ops-docs write --init && git add -A && git commit -qm probe \
 && python3 tools/ops-docs check; echo exit=$? \
 && grep -n -E '^\*Probe\*$|^\*\*science\*\*|^## ' README.md \
 && python3 - <<'EOF'
import pathlib
p = pathlib.Path("README.md"); t = p.read_text()
head, doc = t.split("## Documentation\n", 1)
doc, lic = doc.split("## License\n", 1)
p.write_text(head + "## License\n" + lic + "## Documentation\n" + doc)
EOF
python3 tools/ops-docs check; echo swapped exit=$? )
```

One subshell, so the scratch directory and the working directory both survive the
sequence. Expected: `exit=0`, then the grep shows `*Probe*`, `**science**` in the nav
and the five `## ` headings in contract order, then a finding naming the section order
and `swapped exit=1`. The scratch directory is under `mktemp` and is left alone.

- [ ] **Step 5: Commit**

```bash
tasks done vdocs-3432ce "templates/README.md; link checker skips templates/; contract probe passed"
git add templates/README.md tools/check_links.py tasks/
git commit -m "feat: README template for family members; link checker skips templates/"
```

---

### Task 3: The home's gate and guides

**Files:**
- Modify: `justfile` (the `hook-pre-push` recipe)
- Modify: `README.md` (the `## Layout` list, the `## Repositories` paragraph)
- Modify: `AGENTS.md` (the `## Layout` list, one rule)

**Interfaces:**
- Produces: a pre-push that refuses while any member's committed `tools/family.toml`
  differs from `family.toml` here.

- [ ] **Step 1: Add `family check` to the pre-push recipe**

Replace the recipe:

```just
# What the pre-push hook runs: the same commands as `gate`, under one hook target. This
# repository is the verifiably family home, so the push also judges every member's
# committed tools/family.toml against family.toml (ops family guide templates design §6).
hook-pre-push:
    {{tt}} hook-pre-push -- sh -c '{{check_cmd}} && {{test_cmd}} && python3 tools/ops-docs family check'
```

- [ ] **Step 2: Name the two files in both guides**

In `README.md`, `## Layout` becomes:

```markdown
- `overview.md` — the ecosystem overview.
- `family.toml` — the verifiably family: its summary, members and README contract,
  rendered into every member's guides by ops-docs.
- `templates/README.md` — the README a member starts from.
- `tools/` — the link checker, and tooling vendored from ops.
- `tasks/` — task records, managed with the `tasks` CLI.
```

and the `## Repositories` table gains, after it, the sentence:

```markdown
The layer column is each member's label in `family.toml`; change the two together.
```

In `AGENTS.md`, `## Layout` gains two lines after `overview.md`:

```markdown
- `family.toml` — the family declaration; `tools/ops-docs family check` at pre-push
  judges every member's committed copy against it.
- `templates/README.md` — the member README template; `tools/check_links.py` skips
  `templates/`.
```

and `## Rules` gains:

```markdown
- A member's label in `family.toml` is the layer column of the README table; a change
  to one is a change to both, and nothing checks it.
```

- [ ] **Step 3: Render and check**

Run: `python3 tools/ops-docs write && just check; echo exit=$?`
Expected: `exit=0` (the identity region is unchanged; `write` is a no-op).

- [ ] **Step 4: Prove the pre-push wiring, and that it refuses today**

Run: `python3 tools/ops-docs family check; echo exit=$?`
Expected, before any rollout: five lines, one per member, each `missing`, `exit=1`.
This is the state until Rollouts 1–5 land; the home is not pushed before then.

- [ ] **Step 5: Commit**

```bash
tasks done vdocs-47d656 "family check at pre-push; guides name family.toml and the template"
git add justfile README.md AGENTS.md tasks/
git commit -m "feat: family check at pre-push; guides name family.toml and the template"
```

---

### Task 4: File the member rollout tasks and close the design task

**Files:**
- Create: one task record in each of autonomy, science, nodes, atoms, beliefs (their
  registered checkouts, via `tasks add --project`)
- Modify: `tasks/vdocs-fff787.md`, `tasks/vdocs-3474e8.md`, `tasks/vdocs-0f0163.md`,
  `tasks/vdocs-910898.md` (through the CLI). `done` refuses a task with an open child, so
  the Task 4 child and the idea close before the design task, and the goal closes last.

**Interfaces:**
- Consumes: the merged home branch (Tasks 1–3 on `main`), so that each rollout's
  `git -C <home> show HEAD:family.toml` reads the committed family file.
- Produces: five task ids, each named in this plan's rollout section by its own note.

- [ ] **Step 1: Merge the home branch**

From the main checkout:

```bash
git merge --ff-only design/readme-template && just check; echo exit=$?
```

Expected: `exit=0` with no `skipped:` lines (the siblings are beside the main checkout,
so every cross-repository link is verified).

- [ ] **Step 2: File one rollout task per member**

First `tasks start vdocs-fff787` in the main checkout, so the claim moves here from the
worktree before any record is written here.

```bash
tasks add "Adopt the verifiably README template (rollout 1)" --project autonomy -p 2 --size s --complexity low --process direct --tag docs \
  -b "Adopt the verifiably family README template as verifiably/docs docs/plans/2026-10-09-readme-template.md, section 'Rollout 1: autonomy', specifies: tools, identity.toml, both guides, the family copy, the defect fixes. Absorbs autonomy-6e0015. Spec: verifiably/docs docs/specs/2026-10-09-readme-template-design.md."
tasks add "Adopt the verifiably README template (rollout 2)" --project sci -p 2 --size m --complexity low --process direct --tag docs \
  -b "Adopt the verifiably family README template as verifiably/docs docs/plans/2026-10-09-readme-template.md, section 'Rollout 2: science', specifies: tools, identity.toml, both guides, the family copy, Usage from tools/cli.toml, the defect fixes. Absorbs sci-edc546. Spec: verifiably/docs docs/specs/2026-10-09-readme-template-design.md."
tasks add "Adopt the verifiably README template (rollout 3)" --project nodes -p 2 --size m --complexity low --process direct --tag docs \
  -b "Adopt the verifiably family README template as verifiably/docs docs/plans/2026-10-09-readme-template.md, section 'Rollout 3: nodes', specifies: tools, identity.toml, both guides, the family copy, the moves and the machine-local link fixes. Spec: verifiably/docs docs/specs/2026-10-09-readme-template-design.md."
tasks add "Adopt the verifiably README template (rollout 4)" --project atoms -p 2 --size m --complexity mid --process direct --tag docs \
  -b "Adopt the verifiably family README template as verifiably/docs docs/plans/2026-10-09-readme-template.md, section 'Rollout 4: atoms', specifies: tools, identity.toml, both guides, the family copy, the Plan A roadmap index at docs/plans/README.md with test_docs_status.py following it. Spec: verifiably/docs docs/specs/2026-10-09-readme-template-design.md."
tasks add "Adopt the verifiably README template (rollout 5)" --project beliefs -p 2 --size m --complexity mid --process direct --tag docs \
  -b "Adopt the verifiably family README template as verifiably/docs docs/plans/2026-10-09-readme-template.md, section 'Rollout 5: beliefs', specifies: tools, identity.toml, both guides, the family copy, the designs index at docs/designs/README.md, the khughitt link fixes, the guide pointer. Spec: verifiably/docs docs/specs/2026-10-09-readme-template-design.md."
```

Each prints its id. Record them:

```bash
tasks note vdocs-fff787 "Rollout tasks filed: autonomy <id1>, science <id2>, nodes <id3>, atoms <id4>, beliefs <id5>"
```

- [ ] **Step 3: Wire the dependencies**

```bash
tasks dep <id1> --on autonomy-b12f43
tasks dep <id2> --on sci-a2c91b
tasks dep <id5> --on beliefs-c92ca9
tasks dep vdocs-0f0163 --on <id1>
tasks dep vdocs-0f0163 --on <id2>
tasks dep vdocs-0f0163 --on <id3>
tasks dep vdocs-0f0163 --on <id4>
tasks dep vdocs-0f0163 --on <id5>
tasks check; echo exit=$?
```

Expected: `exit=0`. A `unreachable_dep` warning here means a member is not registered on
this host; every member resolved on 2026-10-09 (`tasks resolve --json atoms nodes beliefs sci autonomy`).

- [ ] **Step 4: Commit each record in its project**

In each member's main checkout:

```bash
git -C "$(root <prefix>)" add tasks/<id>.md
git -C "$(root <prefix>)" commit -m "chore(tasks): file the README template rollout" -- tasks/<id>.md
```

Their pre-commit hooks run their
own checks; a hook that refuses is reported, not bypassed.

- [ ] **Step 5: Close the design task**

```bash
tasks note vdocs-910898 "Design done: spec docs/specs/2026-10-09-readme-template-design.md, plan docs/plans/2026-10-09-readme-template.md; one rollout task per member filed, the goal vdocs-0f0163 depends on them"
tasks done vdocs-3474e8 "five rollout tasks filed and wired; records committed in their projects"
tasks done vdocs-910898 "Audited, designed and filed: spec and plan in vdocs-fff787, one rollout task per member"
tasks done vdocs-fff787 "Spec and plan reviewed; family.toml, template and pre-push family check on main; five rollout tasks filed"
git add tasks/
git commit -m "chore(tasks): close the README template design; goal depends on the five rollouts"
```

Then remove the worktree per the global rules (`tt-report`, the ignored-file check,
`git worktree unlock`, `git worktree remove`).

---

## Member rollouts

Each rollout is one task in the member's project (Task 4), executed in that member's
own task worktree under its `.worktrees/`, as one commit. The steps below are the
recipe each task follows; they are written for an executor who has never seen the
repository. The README listings show their code blocks indented, because this plan is
itself link-checked and nested fences defeat the checker; in the member's README each is
a fenced `sh` block (the beliefs layout block is a plain fence). Common to all five, in
this order:

1. `tasks start <id>` in the member's main checkout, commit the record, `git worktree
   add .worktrees/readme-template -b docs/readme-template`, `just setup` where the
   justfile defines it, `tasks start <id>` again in the worktree.
2. Vendor the tool: `cp $OPS/bin/ops-docs tools/ops-docs` (ops must be
   on `main` and clean: `git -C $OPS status --short` prints nothing for
   `bin/ops-docs`; the second line of the copy reads `# ops-docs version 3`).
3. Copy the family file: `git -C $DOCS show HEAD:family.toml > tools/family.toml`
   and confirm `cmp tools/family.toml $DOCS/family.toml`.
4. Write `identity.toml` (given per rollout).
5. Lay the template over the README: keep the existing file for its content, but its
   head becomes the template's head. Concretely, write the new README from the
   template, delete the guidance comment with the blank line after it, and fill the
   sections from the old README as each rollout says.
6. Write `AGENTS.md` as each rollout says.
7. Render: `python3 tools/ops-docs write --init` (both regions in both files), then
   `python3 tools/ops-docs check; echo exit=$?` expecting `exit=0`.
8. Grep the guards:
   `grep -n -E 'Science|~/d/|\]\(\.\./' README.md AGENTS.md` expecting no output, except
   for rule identities such as `science.identity.v1` where a rollout names them. Then
   verify every relative Markdown link in both guides, which neither the member's gate
   nor ops-check does (ops-check reads backticked paths, not links):

   ```bash
   python3 - <<'EOF'
   import re, pathlib, sys
   bad = [(f, m.group(1)) for f in ("README.md", "AGENTS.md")
          for m in re.finditer(r"(?<!!)\[[^]]*]\(([^)\s#]+)", pathlib.Path(f).read_text())
          if not m.group(1).startswith("https://") and not pathlib.Path(m.group(1)).exists()]
   print(bad or "links ok"); sys.exit(1 if bad else 0)
   EOF
   ```

   expecting `links ok`. The `https://github.com/verifiably/...` links are verified by
   the home's `just check` after the merge (step 10), which reads the siblings.
9. The member's own gate: `just check; echo exit=$?` expecting `exit=0` (it now runs
   `ops-docs check`), and the tests each rollout names.
10. One commit, with the absorbed task closed in it where a rollout says so; merge to
    the member's `main` (fast-forward); from the home's main checkout
    `python3 tools/ops-docs family check` now lists this member no longer as `missing`.

### Rollout 1: autonomy

**Files:**
- Create: `tools/tt`, `tools/ops-check`, `tools/ops-docs` (copied from ops `bin/`),
  `tools/family.toml`, `identity.toml`, `AGENTS.md`, `justfile`, `.githooks/pre-commit`,
  `.githooks/pre-push`, `.gitignore`
- Modify: `README.md`

- [ ] **Step 1: The front door**

```bash
mkdir -p tools && cp $OPS/bin/tt $OPS/bin/ops-check $OPS/bin/ops-docs tools/
cp -r $OPS/templates/githooks .githooks
cp $OPS/templates/gitignore .gitignore
cp $OPS/templates/justfile justfile
git config core.hooksPath .githooks
```

In `justfile`, set the commands (nothing is built, so every test command is `true` and
says so):

```just
# Nothing is built yet: every test command is `true` until the envelope lands, so the
# hooks run the docs checks today and the report shows the gap as equal durations.
fast_cmd := "true"
test_cmd := "true"
check_cmd := "python3 tools/ops-check && python3 tools/ops-docs check && tasks check"
docs_paths := "*.md docs/* tasks/*"
docs_check_cmd := check_cmd
ci_suite_refs := ""
ci_remote := "origin"
push_fast_cmd := "true"
one_cmd := "true"
setup_cmd := "true"
```

- [ ] **Step 2: Family copy and identity**

```bash
git -C $DOCS show HEAD:family.toml > tools/family.toml
```

`identity.toml`:

```toml
# What this project is. `tools/ops-docs write` renders it into the identity region of
# README.md and AGENTS.md; `tools/ops-docs check` refuses a commit while they differ.
# Design: ops docs/specs/2026-09-22-project-guides-design.md §3.
name = "autonomy"
aliases = []
purpose = "The envelope and orchestrator of verifiably: what may run unattended"
abstract = """
What may run unattended, under what tier, and how the next research action is chosen: the run baseline and dispositions, tiers as write-class permits, the actor sandbox and session ledger, behavioural profiles and the versioned priority function. It drives science's commands as tools and holds no private kernel access. Designed, not started.
"""
authority = []
subsystems = []
```

- [ ] **Step 3: The README**

```markdown
# autonomy

<!-- ops:identity start — generated by ops-docs; edit identity.toml -->
<!-- ops:identity end -->

<!-- ops:family start — generated by ops-docs; edit family.toml in the family home -->
<!-- ops:family end -->

## Documentation

- [User and autonomy layer design](https://github.com/verifiably/beliefs/blob/main/docs/superpowers/specs/2026-08-29-user-and-autonomy-layer-design.md)
  — the governing design, in the kernel repository: §7 is this layer, §8 orders the
  sub-projects. Work here starts at sub-project #6, the envelope, after the command
  framework, and ends with #7, the loop and the priority function (`science.priority.v1`).
- This repository's own designs and plans will live under docs/ (specs and plans) once
  written; nothing is there today.
- This layer is split from `science` on code-lineage independence: the envelope must
  not share a package with the surface it constrains, so its only seam is `science`'s
  commands as tools.

## License

MIT, see [LICENSE](LICENSE).
```

- [ ] **Step 4: `AGENTS.md`**

```markdown
# autonomy — agent guide

<!-- ops:identity start — generated by ops-docs; edit identity.toml -->
<!-- ops:identity end -->

## Gates

`just check` runs ops-check, `ops-docs check` and `tasks check`; the pre-commit hook
runs it. Every test recipe is `true` until the envelope is built; replace them in
`justfile` with the first suite. On a fresh clone, `git config core.hooksPath .githooks`.

## Layout

- docs/ — designs (specs) and plans for this layer, once written; empty today.
- `tools/` — `tt`, `ops-check`, `ops-docs` vendored from ops; `family.toml` published
  from verifiably/docs.

## Rules

- No kernel import. This layer reaches `beliefs` only through `science`'s commands as
  tools; a private kernel path would let the envelope bypass the surface it constrains.
- The governing design is in the kernel repository (README, Documentation); a design
  written here cites it by its GitHub URL, never by a relative path into the sibling
  checkout, which breaks on GitHub.
```

- [ ] **Step 5: Render, check, close the absorbed task, commit**

```bash
python3 tools/ops-docs write --init && python3 tools/ops-docs check; echo exit=$?
grep -n -E 'Science|~/d/|\]\(\.\./' README.md AGENTS.md; echo grep=$?
just check; echo exit=$?
```

Expected: `exit=0`, `grep=1` (no matches), `exit=0`. `just check` includes ops-check,
whose backtick rule treats every backticked path in the guides as a claim that it is
tracked: the two guides above backtick none that is not. The README's family region
shows `**autonomy**` bold.

```bash
tasks done autonomy-6e0015 "Absorbed by the README template rollout: the family region links the overview and the stack is called verifiably"
git add -A
git commit -m "docs: adopt the verifiably README template and the project guides contract"
```

### Rollout 2: science

**Files:**
- Create: `tools/ops-docs`, `tools/family.toml`, `identity.toml`
- Modify: `README.md`, `AGENTS.md`, `justfile` (`check_cmd`)

- [ ] **Step 1: Tool, family copy, gate**

```bash
cp $OPS/bin/ops-docs tools/ops-docs
git -C $DOCS show HEAD:family.toml > tools/family.toml
```

In `justfile`: `check_cmd := "python3 tools/ops-check && python3 tools/ops-docs check && tasks check"`
(`docs_check_cmd := check_cmd` already follows it).

- [ ] **Step 2: Identity**

```toml
# What this project is. `tools/ops-docs write` renders it into the identity region of
# README.md and AGENTS.md; `tools/ops-docs check` refuses a commit while they differ.
# Design: ops docs/specs/2026-09-22-project-guides-design.md §3.
name = "science"
aliases = []
purpose = "The daily surface of verifiably: the layer people and agents use"
abstract = """
Harness-neutral commands and skills over the beliefs kernel, served as a CLI and over MCP, with generated harness adapters (Claude Code first), the derived work queue and publish. It owns no kinds and no storage: every durable thing is a governed record in a beliefs corpus, and every write is a kernel act.
"""
authority = ["docs/specs/2026-08-31-command-framework-design.md"]
subsystems = []
```

- [ ] **Step 3: The README**

The command list below is `tools/cli.toml`'s `[[cli.science.commands]]` rows on
2026-10-09; re-read the file and list what it holds at rollout time.

```markdown
# science

<!-- ops:identity start — generated by ops-docs; edit identity.toml -->
<!-- ops:identity end -->

<!-- ops:family start — generated by ops-docs; edit family.toml in the family home -->
<!-- ops:family end -->

## Install

`verifiably-science` is not yet published. From a checkout, with `beliefs` checked out
beside it as an editable path dependency:

    cd python && uv sync

## Usage

`science` is the CLI (`uv run science <command>` under `python/`); `science mcp serve`
serves the same commands over MCP on stdio. The command surface, from `tools/cli.toml`:

- The belief path: `dataset`, `claim`, `spec`, `run`, `assess`, `verify`, `belief`,
  `next`.
- Coordination: `project`, `question`, `hypothesis`, `task`, `decide`, `revise`,
  `reuse`, `project-select`, `projects`, `project-show`.
- The world: `status`, `build`, `epoch`, `serve`, `mcp`, `adapters`.

    uv run science status

prints the world: corpora and their lifecycle status, the current epoch, and record
counts by kind. Writes run as kernel acts through an attended `beliefs` session,
permit-checked per act and deduplicated through its ledger.

## Layout

- `commands/` — one directory per command: its declaration and prompt.
- `skills/`, `adapters/` — harness-neutral skills and the generated harness adapters.
- `python/` — the package: the dispatcher, the CLI and MCP surfaces, the writer service.
- `docs/specs/`, `docs/plans/`, `docs/records/` — designs, plans and records.

## Documentation

- [Command framework design](docs/specs/2026-08-31-command-framework-design.md) — the
  declaration schema and write classes, the renderer, the dispatcher, the surfaces.
- [User and autonomy layer design](https://github.com/verifiably/beliefs/blob/main/docs/superpowers/specs/2026-08-29-user-and-autonomy-layer-design.md)
  — the governing design in the kernel repository: §5 is this layer, §8 orders the
  sub-projects.

## License

MIT, see [LICENSE](LICENSE).
```

- [ ] **Step 4: `AGENTS.md`**

Keep the current `## Setup` body. `## Session protocol` becomes `## Gates` holding the
test bullet, the pre-commit classification bullet, the CI bullet and the `tt-report`
bullet verbatim; its first bullet (tasks prime, start, done, check) is deleted as a
restatement of the global layer. Add:

```markdown
## Layout

- `commands/<name>/` — `command.toml` and `prompt.md` per command; `tools/cli.toml` is
  the authority for the surface.
- `python/` — the package; tests under `python/tests/`.

## Rules

- Every durable thing is a governed record in a `beliefs` corpus, and every write is a
  kernel act through the permit-bound writer endpoint: no storage of its own here.
- A new command is a row in `tools/cli.toml` first; the conformance test asserts the
  live parser surface equals it.
```

The first paragraph under the H1 (the "Science" summary and the governing design) is
deleted: the identity region replaces it.

- [ ] **Step 5: Render, check, close the absorbed task, commit**

```bash
python3 tools/ops-docs write --init && python3 tools/ops-docs check; echo exit=$?
grep -n -E 'Science|~/d/|\]\(\.\./' README.md AGENTS.md; echo grep=$?
just check; echo exit=$?
just test-fast; echo exit=$?
```

Expected: all `exit=0`, `grep=1`. Confirm `wc -l AGENTS.md` is at most 120.

- [ ] **Step 6: Commit**

```bash
tasks done sci-edc546 "Absorbed by the README template rollout: the family region links the overview and the stack is called verifiably"
git add -A
git commit -m "docs: adopt the verifiably README template and the project guides contract"
```

- [ ] **Step 7: Pin review focus 1 (name versus prefix)**

In the worktree, temporarily set `name = "sci"` in `identity.toml`, run
`python3 tools/ops-docs check; echo exit=$?`, expect a finding that the family copy does
not list this repository and `exit=1`; restore `name = "science"` and confirm `exit=0`.
No commit.

### Rollout 3: nodes

**Files:**
- Create: `tools/ops-docs`, `tools/family.toml`, `identity.toml`
- Modify: `README.md`, `AGENTS.md`, `justfile` (`check_cmd`)

- [ ] **Step 1: Tool, family copy, gate**

```bash
cp $OPS/bin/ops-docs tools/ops-docs
git -C $DOCS show HEAD:family.toml > tools/family.toml
cmp tools/family.toml $DOCS/family.toml && echo same
```

In `justfile`:
`check_cmd := "python3 tools/ops-check && python3 tools/ops-docs check && " + py_check_cmd + " && " + ts_check_cmd + " && tasks check"`.

- [ ] **Step 2: Identity**

```toml
# What this project is. `tools/ops-docs write` renders it into the identity region of
# README.md and AGENTS.md; `tools/ops-docs check` refuses a commit while they differ.
# Design: ops docs/specs/2026-09-22-project-guides-design.md §3.
name = "nodes"
aliases = []
purpose = "A problem-agnostic knowledge substrate: typed markdown nodes"
abstract = """
Entities as markdown files, typed relations, structural shapes and rebuildable derived indexes, implemented in Python and TypeScript over one shared on-disk format. The kernel is domain-free; domain profiles such as beliefs and mindful v6 register their own kinds on it.
"""
authority = ["docs/STANDARD.md"]
subsystems = []
```

- [ ] **Step 3: The README**

```markdown
# nodes

<!-- ops:identity start — generated by ops-docs; edit identity.toml -->
<!-- ops:identity end -->

<!-- ops:family start — generated by ops-docs; edit family.toml in the family home -->
<!-- ops:family end -->

## Install

Python ([`verifiably-nodes` on PyPI](https://pypi.org/project/verifiably-nodes/)) and
TypeScript ([`@verifiably/nodes` on npm](https://www.npmjs.com/package/@verifiably/nodes)):

    pip install verifiably-nodes
    npm install @verifiably/nodes

## Usage

A corpus is a directory; add a node, and a fresh `Corpus` over the same directory reads
it back from disk. Python:

    import tempfile
    from pathlib import Path
    from nodes.core.corpus import Corpus
    from nodes.core.node import Node

    root = Path(tempfile.mkdtemp())
    Corpus(root).add(Node(id="topic:a", kind="topic", title="A", body="hi"))
    print(Corpus(root).get("topic:a").title)  # A

TypeScript, the same corpus format with a camelCase API:

    import { mkdtempSync } from "node:fs";
    import { tmpdir } from "node:os";
    import { join } from "node:path";
    import { Corpus, makeNode } from "@verifiably/nodes";

    const root = mkdtempSync(join(tmpdir(), "nodes-"));
    new Corpus(root).add(makeNode({ id: "topic:a", kind: "topic", title: "A", body: "hi" }));
    console.log(new Corpus(root).get("topic:a").title); // A

`Corpus.read_and_check()` returns every node with the findings of a structural check;
inspect the findings before trusting the nodes.

## Layout

| Path | Contents |
|------|----------|
| `docs/STANDARD.md` | The versioned, normative portable contract. |
| `docs/designs/`, `docs/plans/` | Dated historical records (rationale, not authority). |
| `python/` | Python core distribution (`verifiably-nodes`); imports are `nodes.core`. |
| `ts/` | TypeScript core package (`@verifiably/nodes`), the domain-free kernel. |
| `fixtures/` | Shared cross-language conformance oracles. |

## Documentation

- [The standard](docs/STANDARD.md) — what both languages must agree on, in three
  tiers: the portable data contract, oracle-pinned behavior, and per-language surface.
  When any document here disagrees with it, the standard wins.
- [`python/README.md`](python/README.md), [`ts/README.md`](ts/README.md) — each
  package's own guide.

## License

MIT, see [LICENSE](LICENSE).
```

Before committing, run both examples. They are the round-trip tests
`python/tests/test_corpus.py` (`test_add_get_roundtrip`) and `ts/tests/corpus.test.ts`
("add then get round-trips") reduced to a script, so each must print `A`:

```bash
(cd python && uv run --frozen python - <<'EOF'
import tempfile
from pathlib import Path
from nodes.core.corpus import Corpus
from nodes.core.node import Node

root = Path(tempfile.mkdtemp())
Corpus(root).add(Node(id="topic:a", kind="topic", title="A", body="hi"))
print(Corpus(root).get("topic:a").title)
EOF
)
(cd ts && npm run build && sed 's#"@verifiably/nodes"#"./dist/index.js"#' > readme_example.mjs <<'EOF'
import { mkdtempSync } from "node:fs";
import { tmpdir } from "node:os";
import { join } from "node:path";
import { Corpus, makeNode } from "@verifiably/nodes";

const root = mkdtempSync(join(tmpdir(), "nodes-"));
new Corpus(root).add(makeNode({ id: "topic:a", kind: "topic", title: "A", body: "hi" }));
console.log(new Corpus(root).get("topic:a").title);
EOF
node readme_example.mjs; status=$?; rm readme_example.mjs; exit $status); echo ts exit=$?
```

The source tree imports its siblings as `.js`, which Node cannot resolve to `.ts`, so
the probe runs the package's own build (`tsc -p tsconfig.build.json`, into the
gitignored `dist/`) and imports the compiled entry point that the package's `exports`
name; the `sed` only redirects the package name there. The subshell exits with node's
status, so the cleanup cannot mask a failure. Both print `A`, and `ts exit=0`.

- [ ] **Step 4: `AGENTS.md`**

```markdown
# nodes — agent guide

<!-- ops:identity start — generated by ops-docs; edit identity.toml -->
<!-- ops:identity end -->

## Gates

- `just gate` — the whole thing: `just check` (ops-check, ops-docs check, ruff, pyright,
  biome, tsc, `tasks check`) then `just test` (pytest and vitest, both packages). Run it
  from anywhere in the tree.
- Every recipe records its run through `tools/tt`, the timing wrapper vendored from the
  ops repository, so do not call `pytest`, `npm test`, `ruff`, `pyright`, `tsc`, or
  `biome` directly.
- The git hooks in `.githooks/` run `just hook-pre-commit` (the `check` command) and
  `just hook-pre-push` (the whole gate). A fresh clone installs them with
  `git config core.hooksPath .githooks`.
- Before removing a worktree, run `tt-report` in the ops repository so this checkout's
  fallback test-timing log is harvested.

## Layout

- `python/`, `ts/` — the two packages; `fixtures/` — the shared conformance oracles.
- `docs/STANDARD.md` — the authority; `docs/designs/`, `docs/plans/` — dated records,
  rationale only.

## Rules

- Authority order: `docs/STANDARD.md`, then the code and its tests, then the dated
  records. When anything disagrees with the standard, it wins, or it has a bug: fix it
  in the same change. Do not execute old plans or treat their snippets as current.
- Layering is enforced: `nodes.core` imports nothing above it and names zero knowledge
  kinds; domain kinds live downstream, registered onto the kernel's `Registry`.
- Decide the parity tier before any feature (`docs/STANDARD.md` §1): tier 1 (format,
  identity, mutation semantics) and tier 2 (derived-index behavior, finding codes) land
  in both languages with the standard and the `fixtures/` oracles in the same change;
  tier 3 (per-language convenience) may be one language with no standard change.
- Wrap Pydantic/Zod errors into the kernel error hierarchy; they never escape public
  APIs. Kinds are name + facets + invariants, never subclasses.
```

The old `## Conventions` lines "Fail early", "Filepaths in docs use `~/d/nodes/...`",
"No AI-attribution trailers" and the whole `## Tasks workflow` are deleted: global
layer.

- [ ] **Step 5: Render, check, test, commit**

```bash
python3 tools/ops-docs write --init && python3 tools/ops-docs check; echo exit=$?
grep -n -E 'Science|~/d/|\]\(\.\./' README.md AGENTS.md; echo grep=$?
just check; echo exit=$?
just test-fast; echo exit=$?
git add -A
git commit -m "docs: adopt the verifiably README template and the project guides contract"
```

Expected: all `exit=0`, `grep=1`.

### Rollout 4: atoms

**Files:**
- Create: `tools/ops-docs`, `tools/family.toml`, `identity.toml`, `docs/plans/README.md`
- Modify: `README.md`, `AGENTS.md`, `justfile` (`check_cmd`, the `test-one` recipe),
  `python/tests/test_docs_status.py` (`status_regions`, the two entry-document tests)

- [ ] **Step 1: Tool, family copy, gate**

```bash
cp $OPS/bin/ops-docs tools/ops-docs
git -C $DOCS show HEAD:family.toml > tools/family.toml
cmp tools/family.toml $DOCS/family.toml && echo same
```

In `justfile`:
`check_cmd := "python3 tools/ops-check && python3 tools/ops-docs check && (cd python && uv run --frozen ruff check && uv run --frozen pyright) && tasks check"`.

The justfile has no `test-one` recipe, and the focused roadmap checks below need one
(testmon would skip a test whose only changed input is a Markdown file). Add, from
ops's `templates/justfile`: `set positional-arguments` on the line after `set quiet`;
after `test_cmd`, the runner `one_cmd := "cd python && uv run --frozen pytest"`; and
after the `test-fast` recipe:

```just
# One file, one test, or a filter, while working on it. Needs at least one argument;
# the whole suite is `test`. The sh -c string never holds the arguments, so quotes, $
# and globs in them reach the runner untouched.
test-one +args:
    {{tt}} test-one -- sh -c '{{one_cmd}} "$@" 2>&1' test-one "$@"
```

Run: `just test-one tests/test_docs_status.py; echo exit=$?` expecting `exit=0` before
any other change: the recipe works on the tree as it is.

- [ ] **Step 2: Identity**

```toml
# What this project is. `tools/ops-docs write` renders it into the identity region of
# README.md and AGENTS.md; `tools/ops-docs check` refuses a commit while they differ.
# Design: ops docs/specs/2026-09-22-project-guides-design.md §3.
name = "atoms"
aliases = []
purpose = "A recoverable filesystem effect engine: the crash-safe substrate"
abstract = """
Atomic multi-path filesystem mutation with write-ahead journaling, rollback and post-crash recovery, over an OS-neutral capability vocabulary: a write either lands completely or leaves a state that can be classified from durable evidence and safely completed, rolled back or halted. Conceptually the substrate below nodes, which does not yet adopt it directly; beliefs is its direct consumer.
"""
authority = ["docs/plans/2026-07-23-recoverable-fs-effect-engine-design.md"]
subsystems = []
```

- [ ] **Step 3: The roadmap index, and the test that guards it**

Write `docs/plans/README.md` from the README's `## Status` section and `AGENTS.md`'s
`## Status: Plan A in progress` section: the heading `# Plan A roadmap`, one paragraph
stating that the authority design's §14 decomposes Plan A into nine sub-plans and that
this file is the reader's map of what exists, then one `## Status` section holding, in
order, the sentence `Plan A is substantially implemented: A1–A8b are complete, and A9
— the macOS backend — remains.` and the README's bullet list verbatim (`**A1 — core
model (implemented):** …` through `**A8b — durability certification (implemented):**
…`, the `Historical (superseded)` bullet, with every link rewritten from
`docs/plans/<file>` to `<file>` since the index sits in that directory), then the
`AGENTS.md` paragraph on what writes where (the "A4a, A5a, and A6 write only to
engine-owned paths…" paragraph), and one closing sentence: `Beliefs' adoption of atoms
is governed by Beliefs' adoption ledger, not by this roadmap.`

Then in `python/tests/test_docs_status.py`:

```python
ROADMAP = PLANS / "README.md"


def status_regions() -> dict[str, str]:
    """Every live status claim in the repository, keyed by a readable source name."""
    regions = {"docs/plans/README.md": status_section(ROADMAP.read_text(encoding="utf-8"))}
    for path in live_plan_documents():
        field = status_field(path.read_text(encoding="utf-8"))
        if field is not None:
            regions[path.name] = field
    return regions
```

and in `live_plan_documents()` exclude the index, which carries no `**Status:**` field
and must not be asked for one:

```python
def live_plan_documents() -> list[Path]:
    return sorted(
        path for path in PLANS.glob("*.md") if SUPERSEDED not in path.name and path != ROADMAP
    )
```

`test_the_roadmap_boundary_is_stated_where_the_reader_looks_first` and
`test_the_entry_documents_list_every_implemented_sub_plan` iterate over
`("docs/plans/README.md",)` instead of `("AGENTS.md", "README.md")`; their docstrings
say the index is where the reader looks first. Both keep their assertions.

- [ ] **Step 4: Run the status test and see the index pass**

Run: `just test-one tests/test_docs_status.py; echo exit=$?`
Expected: every test passes, `exit=0`.

- [ ] **Step 5: Pin review focus 4 (a stale index still fails)**

Temporarily change the index's sentence to `A1–A7b are complete, and A8–A9 remain.`,
run `just test-one tests/test_docs_status.py`, expect
`test_no_live_document_calls_an_implemented_sub_plan_unimplemented` and
`test_the_roadmap_boundary_is_stated_where_the_reader_looks_first` to fail naming
`docs/plans/README.md`; restore the sentence and rerun to green.

- [ ] **Step 6: The README**

```markdown
# atoms

<!-- ops:identity start — generated by ops-docs; edit identity.toml -->
<!-- ops:identity end -->

<!-- ops:family start — generated by ops-docs; edit family.toml in the family home -->
<!-- ops:family end -->

## Install

[`verifiably-atoms` on PyPI](https://pypi.org/project/verifiably-atoms/):

    pip install verifiably-atoms

Linux is complete; macOS fills in capability by capability (A9, not yet built). Every
mount is probed for the capabilities it supports (`atomic_exchange`,
`noclobber_transfer`, `durable_publish`, …) and only the effects it cannot satisfy are
refused; the crash-certified configurations are the `CERTIFIED_ALLOWLIST`, and every
other tuple fails closed.

## Usage

`atoms.coordinator.commands` is the public surface. A project root is registered once;
`run_transaction` then executes a compiled spec against it and converges after a crash
in a fresh process. Run this from a directory on a certified ext4 volume (any other
configuration fails closed with `CapabilityUnavailable`, by design):

    import hashlib, io, tempfile
    from pathlib import Path
    from atoms.coordinator.commands import register_root, run_transaction
    from atoms.core.effects import CreateFileNoClobber
    from atoms.core.fingerprint import ABSENT, FileState
    from atoms.core.spec import build_spec
    from atoms.fs.platform import select_backend
    from atoms.fs.volume import StorageProfile

    def sha(b): return "sha256:" + hashlib.sha256(b).hexdigest()
    class Payloads:  # a PayloadSource: a fresh stream per call, KeyError when unknown
        def __init__(self, m): self.m = m
        def open(self, digest): return io.BytesIO(self.m[digest])

    work = Path(tempfile.mkdtemp(dir=Path.cwd())).resolve()
    project, metadata = work / "project", str(work / "project.metadata")
    (project / "d").mkdir(parents=True)
    backend, storage = select_backend(), StorageProfile(profile_id="flush-honoring-disk.v1")
    register_root(backend, str(project), metadata, storage, b"root", ())
    body = b"after"; post = FileState(content_hash=sha(body), mode=0o644, byte_len=len(body))
    spec = build_spec(consumer_tag="example", intent_digest=sha(b"example intent"),
        initial_surface={"d/f.txt": ABSENT}, final_surface={"d/f.txt": post},
        effects=[CreateFileNoClobber(effect_id="e1", path="d/f.txt", post=post)])
    out = run_transaction(backend, str(project), metadata, storage, spec, Payloads({sha(body): body}))
    print(out.outcome, (project / "d/f.txt").read_bytes())  # ChainOutcome.COMMITTED b'after'

`read_preimage(backend, project, metadata, storage, txid, path, max_bytes=...)` then
returns the bytes a registered path held before a settled transaction.

## Layout

- `python/` — the package: `atoms.core` (the pure model), `atoms.fs` (capability
  backend, volume binding, project approval), `atoms.store` (the SQLite-in-WAL
  metadata store), `atoms.coordinator` (lease, admission, preparation, executors).
- `docs/plans/` — the authority design and the Plan A sub-plans, with their roadmap
  index; `docs/certification/` — the crash-certification records;
  `docs/deferred-obligation-ledger.md` — what a trust boundary admits but does not yet
  execute.

## Documentation

- [Plan A roadmap](docs/plans/README.md) — what is built and what remains, with each
  sub-plan's design and plan.
- [Authority design](docs/plans/2026-07-23-recoverable-fs-effect-engine-design.md) —
  the standalone engine and its metadata store; its §14 is the delivery roadmap.
- [Public preimage contract](docs/plans/2026-09-11-public-preimage-read-design.md) —
  the one history read the engine exposes.

## License

MIT, see [LICENSE](LICENSE).
```

Before committing, run the example. It is `test_run_transaction_commits_the_world_chain_and_public_outcome`
(`python/tests/test_coordinator_run.py`) reduced to a script with the production storage
profile, which `beliefs` uses unpatched, so it needs no allowlist patch. Write the block
above, unindented, to `readme_example.py` at the worktree root, then run it with the
worktree's Python project named by absolute path while the working directory is on the
ext4 test volume (`ATOMS_TEST_VOLUME`, else `.atoms-test-volume` under the main
checkout, as `python/tests/fs_support.py` resolves it; `uv --project` is relative to the
working directory, so a bare `python` would not resolve from there):

```bash
W=$PWD && V=${ATOMS_TEST_VOLUME:-$(root atoms)/.atoms-test-volume} && mkdir -p "$V" \
 && (cd "$V" && uv run --frozen --project "$W/python" python "$W/readme_example.py"); echo exit=$?
rm readme_example.py
```

Expected output: `ChainOutcome.COMMITTED b'after'`, `exit=0`. A `CapabilityUnavailable`
refusal names the volume's mismatch and means `$V` is not on the certified
configuration, not that the example is wrong; set `ATOMS_TEST_VOLUME` to a directory
that is and rerun. The temporary project the example creates stays under `$V`; the
suite's own runs leave the same kind of directory there.

- [ ] **Step 7: `AGENTS.md`**

```markdown
# atoms — agent guide

<!-- ops:identity start — generated by ops-docs; edit identity.toml -->
<!-- ops:identity end -->

## Gates

`just check` runs ops-check, ops-docs check, ruff, pyright and `tasks check`;
`just test-one <pytest args>` runs one test (paths relative to `python/`);
`just test-fast` is the inner loop (testmon, excluding the kill-matrix,
persistence-cut and exerciser suites); `just test` is the full suite, which the
pre-push hook runs, including the suites the fast loop excludes. Capability-dependent
tests are proven only on the certified ext4 tuple, which the pre-push gate uses and
`docs/certification/` records. On a fresh clone, `git config core.hooksPath .githooks`.

## Layout

- `python/src/atoms/` — `core`, `fs`, `store`, `coordinator`; `python/tests/` — the
  suites, including the status guard `test_docs_status.py`.
- `docs/plans/` — the authority design, the sub-plans, and `README.md`, the roadmap
  index; `docs/deferred-obligation-ledger.md`; `docs/certification/`.

## Rules

- Authority order: the authority design, then the sub-plans under `docs/plans/` that
  refine it (where they disagree, the design wins). The 2026-07-20 design and roadmap
  are superseded, kept only as the record of the review that hardened the contracts;
  their `Package: science` framing is pre-extraction rationale.
- The roadmap is one fact, `FIRST_UNIMPLEMENTED` in `python/tests/test_docs_status.py`,
  and `docs/plans/README.md` is the reader's copy of it. Landing a sub-plan moves the
  boundary there; the guard then names every document that still disagrees. Never add
  a per-sub-plan status test: four existed, and two pinned claims the next sub-plan
  falsified.
- `docs/deferred-obligation-ledger.md` tracks every shape a trust boundary admits but
  does not execute, with the sub-plan that owes it. Add an entry in the commit that
  creates the admission; remove one only when its owner lands and its suite covers it.
  Every sub-plan from A3 on gets a seam review against the ledger before its plan is
  written (§3 of each design).
```

The `## What this is`, `## Status`, `## Conventions` (global restatements and the
`~/d/atoms/...` path rule) and `## Tasks workflow` sections are gone.

- [ ] **Step 8: Render, check, test, commit**

```bash
python3 tools/ops-docs write --init && python3 tools/ops-docs check; echo exit=$?
grep -n -E 'Science|~/d/|\]\(\.\./' README.md AGENTS.md docs/plans/README.md; echo grep=$?
just check; echo exit=$?
just test-one tests/test_docs_status.py; echo exit=$?
just test-fast; echo exit=$?
git add -A
git commit -m "docs: adopt the verifiably README template; the Plan A roadmap moves to docs/plans/README.md"
```

Expected: all `exit=0`; `grep` may match `Package: science` in `AGENTS.md`, which is a
quoted historical label, and nothing else. `wc -l AGENTS.md` at most 120.

### Rollout 5: beliefs

**Files:**
- Create: `tools/ops-docs`, `tools/family.toml`, `identity.toml`, `docs/designs/README.md`
- Modify: `README.md`, `AGENTS.md`, `justfile` (`hygiene_cmd`), `docs/guide/README.md`
  (the "Read in this order" section)

- [ ] **Step 1: Tool, family copy, gate**

```bash
cp $OPS/bin/ops-docs tools/ops-docs
git -C $DOCS show HEAD:family.toml > tools/family.toml
cmp tools/family.toml $DOCS/family.toml && echo same
```

In `justfile`:
`hygiene_cmd := "python3 tools/ops-check && python3 tools/ops-docs check"`, so both
`check_cmd` and `docs_check_cmd` run it.

- [ ] **Step 2: Identity**

```toml
# What this project is. `tools/ops-docs write` renders it into the identity region of
# README.md and AGENTS.md; `tools/ops-docs check` refuses a commit while they differ.
# Design: ops docs/specs/2026-09-22-project-guides-design.md §3.
name = "beliefs"
aliases = []
purpose = "The epistemic kernel of verifiably: recording scientific belief"
abstract = """
Records scientific belief and the evidence it rests on: typed claims, datasets and holdings, analysis runs and their verification, belief computed on request under a named policy, the world index, additive correction and the mutation log, each guaranteed by a frozen conformance cut. Built on nodes and atoms; consumed by science and autonomy.
"""
authority = ["docs/designs/2026-08-02-epistemic-kernel-design.md", "docs/designs/2026-08-03-redesign-adoption-ledger.md"]
subsystems = []
```

- [ ] **Step 3: The designs index**

Write `docs/designs/README.md`: the heading `# The designs`, then the README's
paragraph "This repository is a clean start. Its predecessor is preserved, public and
unchanged, as `proto-science` …" verbatim (its link stays
`https://github.com/khughitt/proto-science`, where that repository is), then the
README's `## The designs` body verbatim: the count sentence, the 85-row table with its
"Read them in this order" lead, and the closing paragraph on the ledger as the entry
point and frozen identifiers. The table's bare file names are already relative to this
directory, so they need no rewriting.

In `docs/guide/README.md`, under `## Read in this order`, add after the numbered list:

```markdown
The [designs index](../designs/README.md) lists every banked design, cut and ruling in
reading order.
```

- [ ] **Step 4: The README**

```markdown
# beliefs

<!-- ops:identity start — generated by ops-docs; edit identity.toml -->
<!-- ops:identity end -->

<!-- ops:family start — generated by ops-docs; edit family.toml in the family home -->
<!-- ops:family end -->

## Install

`verifiably-beliefs` is not yet published. From a checkout:

    cd python && uv sync --frozen
    cd ../ts && npm ci

## Usage

The kernel is a library; the `science` CLI is its daily surface. Directly: register a
corpus root under an authority, open it under the shipped base profile, and add one
proposition. The root must sit on a certified ext4 volume, as `atoms` requires:

    import tempfile
    from pathlib import Path
    from beliefs import stored
    from beliefs.permit import Authority, WritePermit
    from beliefs.profile import shipped_base
    from beliefs.root import init_corpus_root, open_corpus

    authority = Authority(WritePermit.full(), "readme-example")
    root = Path(tempfile.mkdtemp(dir=Path.cwd())) / "corpus"
    init_corpus_root(root, authority=authority)
    writer = open_corpus(root, authority=authority, profile=shipped_base())
    node = writer.add(stored.proposition_node("p", title="p", claim={"operator": "affects"}))
    print(writer.read_view.get(node.id).id)  # proposition:p

For a whole walk from held data to a belief, the
[mm30 reproduction](docs/designs/2026-09-05-mm30-reproduction.md) drives the kernel
the same way.

## Layout

```
python/     the implementation, package `beliefs` (substrate §11 puts the composition root here)
ts/         the one shared encoding, and nothing else (formal model lim. 9)
fixtures/   the cross-language parity corpus, owned by neither
contracts/  the science base contract
domains/    the packaged domain contracts (biology)
docs/       guide/, designs/, plans/, notes/, specs/ (see Documentation)
```

## Documentation

- [Contributor guide](docs/guide/README.md) — the key ideas, reading paths, glossary
  and open questions; start here.
- [Designs index](docs/designs/README.md) — the banked designs, conformance cuts and
  rulings, in reading order; every guarantee table is frozen under its identifiers.
- [Adoption ledger, current state](docs/designs/2026-08-03-redesign-adoption-ledger.md#current-state-2026-10-02)
  — the sole authority for what is built and what remains, each remainder with its
  owner. The per-cut results records under [`docs/plans/`](docs/plans/) are the
  evidence trail.
- [User and autonomy layer design](docs/superpowers/specs/2026-08-29-user-and-autonomy-layer-design.md)
  — the layers above the kernel, `science` and `autonomy`.

## License

MIT, see [LICENSE](LICENSE).
```

The old head paragraphs (the "Science" framing, the rename note, the clean-start
paragraph, the overview pointer), `## The designs` and the whole `## Status` tally are
gone: the identity and family regions, the designs index and the ledger link replace
them. The `khughitt/nodes` and `khughitt/atoms` links disappear with the head; the nav
row links the two repositories under `verifiably`.

Before committing, run the example. It is the write in
`python/tests/test_operation_port.py` (the `init_corpus_root`, `open_corpus`,
`writer.add` sequence around line 253) reduced to a script. Write the block above,
unindented, to `readme_example.py` at the worktree root, then run it with the
worktree's Python project named by absolute path while the working directory is on the
certified test volume the suite uses (`python/tests/conftest.py`, the `certified_work`
fixture: `.lifecycle-wrappers-test` under the main checkout unless a `SCIENCE_CUT*_ROOT`
variable names another; `uv --project` is relative to the working directory):

```bash
W=$PWD && V=$(root beliefs)/.lifecycle-wrappers-test && mkdir -p "$V" \
 && (cd "$V" && uv run --frozen --project "$W/python" python "$W/readme_example.py"); echo exit=$?
rm readme_example.py
```

Expected output: `proposition:p`, `exit=0`. A `CapabilityUnavailable` refusal means
`$V` is not on the certified configuration; point it at a directory that is and rerun.

- [ ] **Step 5: `AGENTS.md`**

```markdown
# beliefs — agent guide

<!-- ops:identity start — generated by ops-docs; edit identity.toml -->
<!-- ops:identity end -->

## Gates
```

followed by the current `## Repository gates` bullets verbatim, with "ruff check,
ruff format --check, pyright, biome, tsc, `tasks check`" in the first bullet extended
to open with "ops-check, ops-docs check,"; then:

```markdown
## Layout

- `python/`, `ts/`, `fixtures/`, `contracts/`, `domains/` — as the README's Layout.
- `docs/designs/` — banked designs, cuts and rulings (index: `README.md` there);
  `docs/superpowers/specs/` and `docs/superpowers/plans/` — each slice's committed spec
  and plan; `docs/plans/` — per-cut results records.

## Rules
```

followed by the current `## Authority` bullets, the `## Design documents` bullet, and
the `## Cut plans` paragraph and its two bullets, all verbatim. `## Tasks workflow` is
deleted. The H1 changes from `# Repository guidance` to `# beliefs — agent guide`.

- [ ] **Step 6: Render, check, test, commit**

```bash
python3 tools/ops-docs write --init && python3 tools/ops-docs check; echo exit=$?
grep -n -E 'Science|~/d/|\]\(\.\./|khughitt' README.md AGENTS.md docs/designs/README.md; echo grep=$?
just check; echo exit=$?
just test-fast; echo exit=$?
```

Expected: `exit=0` throughout; `grep` matches only `proto-science` under `khughitt` in
the designs index and the `science base contract` layout line, nothing else.
`wc -l AGENTS.md` at most 120: the gates bullets are long lines, and if the file
exceeds the budget, declare `[agents] budget = 140` in `identity.toml` with the
over-budget bullet named in the commit message, rather than cutting a gate rule.

```bash
git add -A
git commit -m "docs: adopt the verifiably README template; the designs table moves to docs/designs/README.md"
```

### After the five

From the home's main checkout:

```bash
python3 tools/ops-docs family check; echo exit=$?
just check; echo exit=$?
git push
```

Expected: `exit=0` for both (five members, none `missing` or `stale`; every sibling
link verified), and the push's pre-push passes. Then note the outcome on vdocs-910898
and on ops-a0318e (the five members adopted under the verifiably contract: the project
guides design's wave 3 for them), and `tasks done vdocs-0f0163` once all five rollout
tasks are closed and `prime` offers it in closeout.
