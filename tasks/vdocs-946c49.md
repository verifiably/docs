---
id: vdocs-946c49
title: "Declare python/ and ts/ subsystems in nodes, atoms and beliefs"
status: todo
priority: 2
size: m
complexity: mid
process: direct
created: 2026-10-10T11:26:12Z
updated: 2026-10-23T20:16:42Z
depends: []
tags: [docs, cross-project]
agent: claude-code/claude-fable-5-1
---

Why: nodes, atoms and beliefs have package READMEs under python/ (all three) and ts/ (nodes and beliefs; atoms has no ts/), but none is declared as a subsystem. A declared subsystem has its own identity.toml (purpose and abstract), so the parent README lists it and the nested AGENTS.md/CLAUDE.md give agents working there their own guide. Both designs call for it: ops docs/specs/2026-09-22-project-guides-design.md §3 and §9 step 3 ("Subsystems are declared where a boundary already has its own README"), and this repository's docs/specs/2026-10-09-readme-template-design.md §12 (deferred "once the root guides have settled"). They have: every rollout under vdocs-0f0163 merged by 2026-10-10.

Established (2026-10-14): ops-docs (vendored as tools/ops-docs in each member) already validates and renders subsystems: a nested identity.toml with no `subsystems` key of its own, README.md and AGENTS.md at the subsystem root, no family region and no status region in subsystem guides, and the parent's identity region lists each child's purpose and path. No project in the tree declares a subsystem yet, so this is the check's first real use. Every root identity.toml currently has `subsystems = []`.

Done: in each of nodes (python, ts), atoms (python) and beliefs (python, ts), each subsystem directory holds identity.toml (name, purpose ≤80, abstract ≤3 sentences, authority where one exists), AGENTS.md, and CLAUDE.md as a one-line `@AGENTS.md` include (design §4); the root identity.toml lists them; `tools/ops-docs write` re-renders the regions; `just check` passes in each repository; one commit per repository. Back in this repository, `tools/ops-docs family check` (pre-push) still passes.

Where to look: ops-docs `check` and `write` (the `subsystem=True` paths in marker_problems/shape_problems/rendered); ops templates/AGENTS.md and templates/README.md for the section order; the existing python/README.md and ts/README.md files for each abstract. Before rewriting a subsystem README, grep that repository's tests for reads of README.md or AGENTS.md (atoms' test_fs_architecture.py asserted AGENTS.md sentences during the rollout; vdocs-0f0163 note). If a check finding shows the subsystem contract does not fit, report it to ops rather than bending it locally. The work happens in the member repositories; file one task in each when starting, or do it directly, and close this task once all three have landed.

## Notes

- 2026-10-14T15:10:46Z (main): scope: scoped; rollouts it waited on landed (vdocs-0f0163 done 2026-10-10); ops-docs subsystem support confirmed in the vendored tools; premise corrected: atoms has python/ only, no ts/; set todo, m/mid/direct
- 2026-10-23T18:01:39Z (main): 2026-10-23: drift confirmed in beliefs' undeclared subsystem READMEs (python/README.md headed 'science — Python' with one module of about 60 listed; ts/README.md 'Python-primary'); content correction filed as beliefs-e3ca2a, to be done in this task's rewrite pass if it starts first. Declaring subsystems widens mechanical coverage only; prose review is ops-b7e4a2.
- 2026-10-23T20:16:42Z (main): 2026-10-23: ops-2c5fbc reconciled the project-guides rollout and keeps this task as the owner of the verifiably members' remaining wave-3 work (subsystem declarations); root adoption of atoms, nodes, beliefs, sci and autonomy landed under ops-a0318e on 2026-10-10.
