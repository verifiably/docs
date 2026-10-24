---
id: vdocs-aabed7
title: "overview.md layer-state column: autonomy row says 'Designed, not started' but autonomy reports built parts"
status: done
priority: 2
size: xs
complexity: low
process: direct
owner: docs/vdocs-aabed7-layer-states
created: 2026-10-23T18:52:18Z
updated: 2026-10-24T15:19:29Z
started: 2026-10-24T15:13:50Z
completed: 2026-10-24T15:19:06Z
closed: 2026-10-24T15:19:06Z
depends: []
tags: [docs]
agent: claude-code/claude-opus-5-5
---

Found 2026-10-14 and rechecked 2026-10-23 during the guided-tour pilot (vdocs-9ca77b). overview.md's layer-state table (snapshot dated 2026-09-26) says autonomy is 'Designed, not started'. autonomy's README now says: 'Built: tiers, the closing check, the sandbox, and autonomy run's launch side.' Do: re-read each layer's own state authority (README / adoption ledger) and update the column and its date in one pass, per this repository's rule that the column is a dated snapshot. Check every row, not only autonomy.

## Notes

- 2026-10-24T15:13:50Z (main): started
  provenance: {"harness_session":"codex:01a16e79-06c8-76b0-9c72-6a9214c2650a","harness_session_source":"CODEX_THREAD_ID"}
- 2026-10-24T15:13:57Z (docs/vdocs-aabed7-layer-states): resumed
  provenance: {"harness_session":"codex:01a16e79-06c8-76b0-9c72-6a9214c2650a","harness_session_source":"CODEX_THREAD_ID"}
- 2026-10-24T15:15:51Z (docs/vdocs-aabed7-layer-states): Scope: overview.md layer-state table and its authority paragraph only. Checked atoms README/Plan A roadmap, nodes README and both Corpus implementations, beliefs current-state ledger (cut 46), science README/coordination closeout/commons 1a completion and handlers, and autonomy README/envelope status and modules. No implementation changes or new design documents needed. Baseline: just setup completed; default just test exited 0 but skipped all five siblings, so it was not accepted as the baseline. Repeated the full-suite just test recipe with test_cmd invoking the same checker and SIBLINGS set to the actual sibling checkout directory: 57 link targets checked, no skips or errors. The checker exposes links rather than unit-test counts.
- 2026-10-24T15:16:06Z (docs/vdocs-aabed7-layer-states): Correction to preceding baseline note: the observed count was 35 link targets checked, not 57. The full-suite recipe exited 0 with no sibling skips or errors.
- 2026-10-24T15:18:32Z (docs/vdocs-aabed7-layer-states): review: impl round 1 — verdict: accept; findings: none; reviewer: codex/gpt-6.1-sol
- 2026-10-24T15:18:35Z (docs/vdocs-aabed7-layer-states): attached: layer-states-review-report.md (2439 bytes): Full read-only review of c292131 by codex/gpt-6.1-sol; accepted with no findings
- 2026-10-24T15:19:03Z (docs/vdocs-aabed7-layer-states): Ruling: Accept the reviewer’s scope exclusion of runtime correctness, crash recertification and complete cross-installation execution for revision c292131. Why: this task refreshes a dated ecosystem snapshot against named layer-owned authorities and changes no implementation. Cost: underlying runtime defects are not ruled out by this documentation review. Live GitHub deployment was also not checked; all linked files and anchors were checked locally. Final verification: just test with the actual sibling directory checked 38 link targets without errors/skips; just check, tasks check and git diff --check passed. Full reviewer report attached; its ignored temporary copy matched the attachment and was removed.
- 2026-10-24T15:19:04Z (docs/vdocs-aabed7-layer-states): retained: {"host":"titan","kind":"worktree","path":".worktrees/vdocs-aabed7","state":"kept","verification":"verified","purpose":"Immediate local integration and checked removal of the reviewed documentation branch; no separate scratch or off-tree evidence remains","next_owner":"session:codex:01a16e79-06c8-76b0-9c72-6a9214c2650a","cleanup_trigger":"After local merge and passing merged-tree checks, inspect ignored files and host pointers, harvest timings, then remove the worktree"}
- 2026-10-24T15:19:06Z (docs/vdocs-aabed7-layer-states): done
  provenance: {"harness_session":"codex:01a16e79-06c8-76b0-9c72-6a9214c2650a","harness_session_source":"CODEX_THREAD_ID"}
- 2026-10-24T15:19:06Z (docs/vdocs-aabed7-layer-states): Refreshed all five layer states and snapshot date to 2026-10-24 with named authorities; independent review accepted with no findings; 38 link targets and repository checks passed.
  provenance: {"harness_session":"codex:01a16e79-06c8-76b0-9c72-6a9214c2650a","harness_session_source":"CODEX_THREAD_ID"}
- 2026-10-24T15:19:29Z (main): retained: {"host":"titan","kind":"worktree","path":".worktrees/vdocs-aabed7","state":"released","verification":"verified","purpose":"Reviewed branch fast-forward merged locally into main at 1a6ed5d; merged just test and just check passed; no ignored or uncommitted files, no submodules or host pointers remained; tt-report ran; worktree and merged task branch removed; full review is preserved in the task attachment","next_owner":"none","cleanup_trigger":"none"}
