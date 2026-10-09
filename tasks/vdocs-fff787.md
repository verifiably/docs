---
id: vdocs-fff787
title: Design the verifiably README template from the brief
status: doing
priority: 2
size: m
complexity: high
process: planned
owner: design/readme-template
created: 2026-10-09T18:36:19Z
updated: 2026-10-09T22:30:39Z
started: 2026-10-09T21:48:52Z
depends: [ops-a0318e]
parent: vdocs-0f0163
tags: [docs]
agent: claude-code/claude-opus-5-5
spec: docs/specs/2026-10-09-readme-template-design.md
plan: docs/plans/2026-10-09-readme-template.md
---

Design the verifiably README template, kept in verifiably/docs, for atoms, nodes, beliefs, science and autonomy, starting from docs/notes/2026-10-09-readme-template-brief.md (audit in §2). Settled by the user 2026-10-09: verifiably gets its own family template rather than the ops default contract, rendered and checked by the generalized per-family ops-docs (ops-a0318e, which this waits on); licence is MIT everywhere (beliefs-c92ca9, sci-a2c91b, autonomy-b12f43 add the files); header art is a separate design built on the stack infographic (ops-adcd29), so the template reserves a header slot. The spec settles: the sections and their order; the verifiably block (ecosystem summary, overview link, nav with the current repository unlinked) and how it is rendered from the family's member list; package links; where each repository's bookkeeping moves (atoms status, beliefs' design table). Done when the spec and plan are reviewed by the user and the plan names one rollout task per repository that also fixes the §2 defects (machine-local and khughitt links, relative ../ links, 'Science' as the stack name, stale status claims), absorbing autonomy-6e0015 and sci-edc546. On completion, note the outcome on vdocs-910898.

## Notes

- 2026-10-09T21:48:52Z (main): started
  provenance: {"harness_session":"claude-code:cb0d9bf1-6fbf-40dd-a649-5096038c67d2","harness_session_source":"CLAUDE_CODE_SESSION_ID"}
- 2026-10-09T21:50:47Z (design/readme-template): resumed
  provenance: {"harness_session":"claude-code:cb0d9bf1-6fbf-40dd-a649-5096038c67d2","harness_session_source":"CLAUDE_CODE_SESSION_ID"}
- 2026-10-09T21:56:23Z (design/readme-template): Design choices in the draft spec: home not a member; lead purpose+abstract; sections Install, Usage, Layout, Documentation, License; no status region; default AGENTS contract; atoms roadmap to docs/plans/README.md (status test follows), beliefs design table to docs/designs/README.md, status prose deleted; rollout home first then autonomy, science, nodes, atoms, beliefs, one task per member project
- 2026-10-09T21:56:39Z (design/readme-template): parked (waiting on user, review): User reviews docs/specs/2026-10-09-readme-template-design.md in .worktrees/readme-template; on approval, write the implementation plan there with writing-plans (home steps here, one rollout task per member project)
  provenance: {"harness_session":"claude-code:cb0d9bf1-6fbf-40dd-a649-5096038c67d2","harness_session_source":"CLAUDE_CODE_SESSION_ID"}
- 2026-10-09T22:10:52Z (design/readme-template): review: spec round 1 — verdict: revise; findings: P1 2, P2 1; reviewer: codex
- 2026-10-09T22:10:52Z (design/readme-template): Spec review findings: §9 family publish resolves registered main checkouts rather than rollout worktrees; §9 member adoption edits README before publication, which refuses dirty guides (and the initial family copy is itself uncommitted); §8 atoms abstract omits the existing explicit qualification that direct nodes adoption is deferred. Recommend publishing once to clean registered checkouts, transferring the committed-home family bytes into each isolated rollout worktree, rendering locally with ops-docs write --init, and locally integrating before the home family check; qualify the atoms/nodes relationship.
- 2026-10-09T22:11:00Z (design/readme-template): Clarification to the review recommendation: skip the initial broadcast into main checkouts for adoption. Copy the home HEAD:family.toml bytes directly into each isolated member worktree, render there with ops-docs write --init, then commit and integrate locally before family check. Reserve family publish for subsequent updates to clean adopted checkouts under an explicitly authorized workspace policy.
- 2026-10-09T22:14:18Z (design/readme-template): resumed
  provenance: {"harness_session":"claude-code:cb0d9bf1-6fbf-40dd-a649-5096038c67d2","harness_session_source":"CLAUDE_CODE_SESSION_ID"}
- 2026-10-09T22:14:25Z (design/readme-template): Spec revised for round 1: rollout drops family publish (it targets registered main checkouts and refuses dirty guides); each member worktree copies the home's HEAD:family.toml and renders with its own ops-docs write --init, one adoption commit, home family check after the merges; publish reserved for later family.toml edits. Atoms abstract keeps the deferred direct-nodes-adoption qualification.
- 2026-10-09T22:14:25Z (design/readme-template): parked (waiting on user, review): Re-review docs/specs/2026-10-09-readme-template-design.md (round 2) in .worktrees/readme-template; on approval, write the implementation plan there with writing-plans
  provenance: {"harness_session":"claude-code:cb0d9bf1-6fbf-40dd-a649-5096038c67d2","harness_session_source":"CLAUDE_CODE_SESSION_ID"}
- 2026-10-09T22:22:06Z (design/readme-template): review: spec round 2 — verdict: accept; findings: none; reviewer: codex
- 2026-10-09T22:22:54Z (design/readme-template): resumed
  provenance: {"harness_session":"claude-code:cb0d9bf1-6fbf-40dd-a649-5096038c67d2","harness_session_source":"CLAUDE_CODE_SESSION_ID"}
- 2026-10-09T22:30:38Z (design/readme-template): Plan drafted: four home tasks here (family.toml, template plus link-checker skip, pre-push family check and guides, file the five rollout tasks and close) and five member rollout recipes; plan review next
- 2026-10-09T22:30:38Z (design/readme-template): parked (waiting on user, review): User reviews docs/plans/2026-10-09-readme-template.md in .worktrees/readme-template and picks an execution method (recommended: native, executing-plans); then execute Tasks 1-4 there
  provenance: {"harness_session":"claude-code:cb0d9bf1-6fbf-40dd-a649-5096038c67d2","harness_session_source":"CLAUDE_CODE_SESSION_ID"}
