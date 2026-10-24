---
id: vdocs-f6fd54
title: Resolve existing tilde-layout findings before checker rollout
status: doing
priority: 2
size: s
complexity: mid
process: direct
owner: fix/vdocs-f6fd54
created: 2026-10-22T19:08:12Z
updated: 2026-10-24T15:54:51Z
started: 2026-10-24T15:48:20Z
depends: []
tags: []
source: ops-295f8d
agent: codex
---

Why: the final candidate from ops-295f8d reports existing home-relative machine-layout paths that the current checker misses. Resolve these before the stricter vendored copy arrives, so unrelated commits are not blocked. These are scanner findings to classify, not an instruction to discard historical documents.

Done: inspect each listed file in context. Replace accidental checkout/storage paths in shared docs, examples or fixtures with repository-relative paths, project-role references or portable URLs as appropriate. For intentional host configuration, use only the narrow existing layout_allowed mechanism where this repository is host configuration by design; do not exempt ordinary docs wholesale. Preserve historical evidence, attachments and every spec/plan review ledger; follow the task attachment CLI and retention rules instead of editing attached artifacts by hand. If a runtime-path correction needs an unsettled public contract, change that piece to planned before implementation. Run the project-declared checks and the reviewed candidate checker by explicit path, then record every listed file disposition and the clean verdict on this task. Do not repoint shared launchers, vendor the checker, publish, push or activate global guidance in this task.

Where: the current project guide/profile, listed tracked files, existing layout_allowed, and ops-295f8d for candidate branch/path and canonical report. The full sweep reached 36 registered repositories with no unavailable roots; counts here are capped scanner records, not an estimate of all occurrences. No source snippets are copied.

Reported files:
- docs/notes/2026-10-09-readme-template-brief.md: first reported line 22; 2 reported finding(s)
- docs/plans/2026-10-09-readme-template.md: first reported line 36; 9 reported finding(s)
- docs/specs/2026-10-09-readme-template-design.md: first reported line 238; 1 reported finding(s)

## Notes

- 2026-10-24T15:48:20Z (main): started
  provenance: {"harness_session":"codex:01a16e98-902b-7952-bfd9-3c4944ca26d7","harness_session_source":"CODEX_THREAD_ID"}
- 2026-10-24T15:48:30Z (fix/vdocs-f6fd54): resumed
  provenance: {"harness_session":"codex:01a16e98-902b-7952-bfd9-3c4944ca26d7","harness_session_source":"CODEX_THREAD_ID"}
- 2026-10-24T15:49:41Z (fix/vdocs-f6fd54): Scope confirmed: direct documentation-only cleanup of the three reported historical documents; no runtime contract, attachments, review ledgers, vendored tools or exemptions change. Candidate ops/.worktrees/ops-295f8d/bin/ops-check reproduces 12 findings (brief 2, plan 9, spec 1), exit 1; source evidence manifest verified as 95e95ef6b93f94927641b71d48af6df65d0239e085ae3f59ecc24ba44b72b2f3 and every listed hash matches. Baseline just test exits 0 but skips five absent sibling checkouts and reports no test count; this is incomplete cross-repository verification, to be supplemented against the main checkout siblings. just setup is the declared no-op and completed.
- 2026-10-24T15:50:58Z (fix/vdocs-f6fd54): Disposition docs/notes/2026-10-09-readme-template-brief.md: replaced the two literal historical home-relative checkout links with the named consumers mindful v6 and beliefs; preserved the dated audit and its defect classification. Exact original text remains in pre-change Git history at 2d275db.
- 2026-10-24T15:50:59Z (fix/vdocs-f6fd54): Disposition docs/plans/2026-10-09-readme-template.md: replaced three literal checkout-path descriptions (constraint, nodes rule, atoms rule) with portable role descriptions; replaced six hardcoded checkout-path grep arms with the existing ops-check machine-layout guard and retained the other grep checks, updating the explicit expected output. No plan headings, rollout decisions, task associations or review records removed.
- 2026-10-24T15:50:59Z (fix/vdocs-f6fd54): Disposition docs/specs/2026-10-09-readme-template-design.md: replaced the literal checkout-path example in the nodes Consumers migration row with home-relative checkout paths; preserved the decision and destination. No host-configuration exemption applies; no layout_allowed file added. No attachments or review ledgers changed.
- 2026-10-24T15:51:00Z (fix/vdocs-f6fd54): Verification at cd8657e: reviewed candidate ops/.worktrees/ops-295f8d/bin/ops-check exits 0 with zero findings; its SHA-256 ca6fd1b272a5f25f5f001ef1fde215e1e6a3aef847df063a0d58e3bdf3a96e25 matches ops implementation 79f1235 exactly. just test-fast, just check, tasks check and git diff --check pass. Project recipes report no test count and skip five siblings from a worktree. Supplemental through just --set test_cmd "python3 -" test checks the same worktree link checker against the main checkout sibling directory: 8 Markdown files, all 5 sibling repositories present, zero errors and no skips. No runner or shared pointer modified.
- 2026-10-24T15:53:09Z (fix/vdocs-f6fd54): review: impl round 1 — verdict: revise; findings: Critical 0, Important 0, Minor 1; reviewer: codex/gpt-6.1-sol
- 2026-10-24T15:53:10Z (fix/vdocs-f6fd54): Ruling: regrade the guard-prerequisite finding from Minor to Important and fix before merge (reviewed revision cd8657e, plan line 487 and five rollout blocks). Why: following the edited commands with the existing vendored checker loses the old grep coverage; the cleanup must preserve that coverage explicitly even in historical instructions. Cost: without the correction, a reader could receive a clean verdict for a protected home-relative checkout path. The reviewer treats it as Minor because historical rollouts are not being executed; the controller requires the dependency clarification as part of preserving meaning.
- 2026-10-24T15:53:36Z (fix/vdocs-f6fd54): attached: impl-round-1-report.md (2726 bytes): Full frozen-revision review by codex/gpt-6.1-sol of cd8657e; guard dependency finding and controller regrade recorded on task
- 2026-10-24T15:54:51Z (fix/vdocs-f6fd54): review: impl round 2 — verdict: accept; findings: Critical 0, Important 0, Minor 0; reviewer: codex/gpt-6.1-sol
