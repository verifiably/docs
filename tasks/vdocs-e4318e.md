---
id: vdocs-e4318e
title: "Pilot a second guided tour on another repository, applying the first pilot's rules"
status: todo
priority: 2
size: s
complexity: mid
process: direct
created: 2026-10-24T00:43:13Z
updated: 2026-10-24T15:41:30Z
depends: []
parent: vdocs-d2d5ed
tags: [docs]
agent: claude-code/claude-opus-5-5
---

Question: Do the rules in [ref:brief] §7 (shuffled items, one kind of question per check, answers grounded in quoted sources, examples checked against the domain, a closing mixed check) carry beyond beliefs, before the method is written up as a skill?
Where to start: Read [ref:brief] §2 for the ladder and §7 for the first pilot's results and rules; then read the chosen repository's identity.toml, README.md and authority documents. Ask the user which repository other than beliefs to tour; science or atoms would test portability.
Bound: One live session with the user over one repository other than beliefs; nothing committed except the result appended to the brief. No skill or written tours. File each drift finding in the project that owns it.
Expected result: Record per-check ratings and scores on this task and in the brief, which rules held, which changed, and a go/no-go for the skill that vdocs-c96d1b would scope.
Ideas it wakes: On completion, run `tasks -C <root> note vdocs-c96d1b --no-reviewed "<finding>"` in this project's checkout before this result's branch merges.

## References

- brief (input, required, kind=brief): docs/notes/2026-10-14-guided-tours-brief.md — the ladder (§2) and the first pilot result and rules (§7)
