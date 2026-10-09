---
id: vdocs-f1291d
title: Commit the published tools/tt (tt version 3) once the pre-commit gate passes
status: todo
priority: 2
size: xs
complexity: low
process: direct
created: 2026-10-01T11:51:24Z
updated: 2026-10-01T11:51:30Z
depends: []
tags: []
source: ops-8fe6c9
agent: claude-code/claude-opus-5-5
---

ops published tt version 3 (ops 910d8ea: an interrupted command finishes its own cleanup and the run is recorded) into this checkout's tools/tt with `just vendor-publish tt`. The rollout rule is to commit tools/tt alone: `git commit -m 'chore(tools): tt version 3 from ops' -- tools/tt`. The publishing session's commit was refused by this project's own pre-commit gate, for a reason unrelated to tt (see the first note), so the file is left modified in the working tree. ops's check passes meanwhile, because it reads the working copy.

## Notes

- 2026-10-01T11:51:30Z (main): refused 2026-10-01 by hook-pre-commit: overview.md link to beliefs docs/designs/2026-08-03-redesign-adoption-ledger.md#current-state-2026-09-16: target resolves but its anchor does not
