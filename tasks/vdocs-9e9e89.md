---
id: vdocs-9e9e89
title: "overview.md: reword the PHF19 example question and qualify the claim that ontology identifiers are not subjective"
status: todo
priority: 2
size: s
complexity: low
process: direct
created: 2026-10-02T19:25:51Z
updated: 2026-10-14T15:24:10Z
depends: []
tags: [quick-add]
source: "mindful:thought:57edd707394a7744bf8fa876f929dfb7"
agent: claude-code/claude-opus-5-5
---

Why: two passages in overview.md read wrongly to the owner (source thought 57edd707).

(1) The worked example (overview.md, "One building block", step 1): "Does disease stage raise PHF19 expression in multiple myeloma?" — "disease stage raise" is unusual wording. Owner's candidates: "Does disease stage progression increase PHF19 gene expression levels?", or "Is disease stage progression associated with higher PHF19 gene expression in patients, on average?" (a third, "Does patient PHF19 gene expression levels over the course of disease progress?", was left unfinished in the thought).

(2) "Subjective categories and labels" (overview.md, "What is kept out"): gene, disease and cell line names, ontology ones included, are names people or algorithms chose. Keep ontologies as trusted identifiers but state their limits rather than calling them "not by names someone chose".

Established (scope 2026-10-14, against overview.md at 0a9571b and beliefs docs/designs/2026-09-05-mm30-reproduction.md §2):
- Both passages are unchanged since the thought (overview.md lines 67-68 and 88).
- The recorded proposition is `concept:disease-stage affects protein:PHF19`, `claim_layer: causal_effect`, `polarity: positive`; the comparison is PHF19 in progressive disease (PD) against newly diagnosed (NDMM). Step 1 goes on to say the claim is cause-and-effect "rather than, say, a mere association", so the question must stay causal: the "associated with" candidate would contradict the next sentence. Use the "progression increases" form (e.g. "Does progression of multiple myeloma increase PHF19 gene expression?"), and keep step 1's *raises*/*lowers* polarity gloss consistent with the new verb.
- Ecosystem level only (AGENTS.md): qualify the ontology claim in a sentence or two; do not restate the beliefs vocabulary or resolution mechanics.

Done: both passages reworded in overview.md as above; `just check` passes.
Where: overview.md "What is kept out" and "One building block, start to finish" step 1; the mm30 record linked from that section.

## Notes

- 2026-10-14T15:24:09Z (main): scope: rescoped; premises checked against overview.md at 0a9571b and beliefs mm30 record §2 (proposition causal_effect, positive); body now records that the reworded question must stay causal, so the 'associated with' candidate is ruled out; process direct, size s, complexity low
