---
id: vdocs-e4318e
title: "Pilot a second guided tour on another repository, applying the first pilot's rules"
status: doing
priority: 2
size: s
complexity: mid
process: direct
owner: main
created: 2026-10-24T00:43:13Z
updated: 2026-10-24T19:03:20Z
started: 2026-10-24T16:09:04Z
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

## Notes

- 2026-10-24T16:09:04Z (main): started
  provenance: {"harness_session":"claude-code:1b29140b-c89c-4277-9bf0-a637ec403f80","harness_session_source":"CLAUDE_CODE_SESSION_ID"}
- 2026-10-24T16:14:05Z (main): repository chosen by the user: atoms (most distant domain from beliefs; tests portability of the §7 rules)
- 2026-10-24T16:15:07Z (main): tour of atoms: stop 1 (ecosystem placement) presented; check 1 is explain-it-back, grounded in family.toml, overview.md:219, atoms identity, authority design §1-§2
- 2026-10-24T16:15:08Z (main): parked (waiting on user): User answers check 1 (explain back atoms' problem and its classifiable-not-ACID contract); then the agent scores it against design §1-§2, records the rating, and presents stop 2 (layer ownership, shuffled choose-the-owner check)
  provenance: {"harness_session":"claude-code:1b29140b-c89c-4277-9bf0-a637ec403f80","harness_session_source":"CLAUDE_CODE_SESSION_ID"}
- 2026-10-24T17:09:29Z (main): resumed
  provenance: {"harness_session":"claude-code:1b29140b-c89c-4277-9bf0-a637ec403f80","harness_session_source":"CLAUDE_CODE_SESSION_ID"}
- 2026-10-24T17:10:05Z (main): check 1 (explain back): right on ACID contrast and end-state intent; wrong: Dropbox across hosts is a stated non-guarantee (§3.2); half: multiple agents (one-host cooperating lock only, §7.1); refinements: domain-neutral writes, third branch is halt. Side questions on consumer/ordering/ownership/split answered from superseded 2026-07-20 design §2
- 2026-10-24T17:10:28Z (main): parked (waiting on user): User rates check 1; then the agent records the rating and presents stop 2 (which layer owns a behaviour, shuffled items, placement questions only)
  provenance: {"harness_session":"claude-code:1b29140b-c89c-4277-9bf0-a637ec403f80","harness_session_source":"CLAUDE_CODE_SESSION_ID"}
- 2026-10-24T17:35:25Z (main): check 1 rated helpful. Learner's side note: guides (and the tour) explain atoms relative to proto-science's intermediate code state, not the status quo a newcomer knows; filed atoms-dd5a5e. Tour-method lesson: grounding in a quoted source must not mean quoting history-laden jargon untranslated; explain against what the learner knows
- 2026-10-24T17:35:57Z (main): parked (waiting on user): User replies (more side questions or go-ahead); then the agent presents stop 2: which layer owns a behaviour across atoms/nodes/beliefs, shuffled, placement questions only, explained against the status quo rather than project history
  provenance: {"harness_session":"claude-code:1b29140b-c89c-4277-9bf0-a637ec403f80","harness_session_source":"CLAUDE_CODE_SESSION_ID"}
- 2026-10-24T18:14:13Z (main): resumed
  provenance: {"harness_session":"claude-code:1b29140b-c89c-4277-9bf0-a637ec403f80","harness_session_source":"CLAUDE_CODE_SESSION_ID"}
- 2026-10-24T18:14:57Z (main): stop 2 presented: layer ownership, 7 shuffled items A-G over atoms/nodes/beliefs/science; key B,D atoms; C,G nodes; A,F beliefs; E science (sources: atoms README Install, design §1/§12.2; nodes STANDARD §8.2, §9.1; beliefs identity, family adapters §1; overview.md:222)
- 2026-10-24T18:14:58Z (main): parked (waiting on user): User answers check 2 (items A-G, which layer owns each); then the agent scores against the recorded key and sources, asks for a rating, and presents stop 3 (atoms repository: predict what happens)
  provenance: {"harness_session":"claude-code:1b29140b-c89c-4277-9bf0-a637ec403f80","harness_session_source":"CLAUDE_CODE_SESSION_ID"}
- 2026-10-24T18:59:53Z (main): resumed
  provenance: {"harness_session":"claude-code:1b29140b-c89c-4277-9bf0-a637ec403f80","harness_session_source":"CLAUDE_CODE_SESSION_ID"}
- 2026-10-24T19:01:59Z (main): check 2 (choose the layer): 7 of 7; rated useful. Side question on nodes adoption of atoms: no task tracked it; filed atoms-495445 (idea) and atoms-c0220c (§12.2 cites §15 for the seam, §15 lacks it). atoms-dd5a5e landed in another session during the tour (README abstract and design §2 rewritten)
- 2026-10-24T19:03:20Z (main): stop 3 presented: transaction life; check 3 predict P1-P5. Key: P1 halt, nothing touched, both entries kept, later commands return the same halt until operator acts (§8.4, §9.1, §12, A7 §9); P2 keep final state, re-prove surface, finish cleanup, never roll back (§8.1); P3 b.txt refused (EEXIST), own staging removed, index.md and a.txt restored first, PreconditionRefused, Dropbox file kept (§9.2, §11); P4 nothing to undo, recorded ROLLED_BACK, active cleared (§8.4 last para); P5 lease first rolls back b.txt (classified landed or not), then index.md, a.txt in reverse, ROLLED_BACK, then the new transaction runs (§7.1, §8.3, §8.4)
