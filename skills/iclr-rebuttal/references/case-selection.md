# Case selection, provenance and responsible score reading

[English](case-selection.md) · [简体中文](case-selection.zh-CN.md)

## Scope and sampling limits

As of **2026-11-09**, the catalogue contains **70 unique OpenReview paper forums**: ICLR 2026 (49), ICLR 2025 (12), and ICLR 2024 (9); 64 accepted and 6 rejected. A forum counts once even if it contains many reviewer notes. The sample was **purposively selected to teach rebuttal mechanisms and evidence limits**. It cannot estimate the general rebuttal success probability or identify causal wording effects.

Coverage focuses on the relevant complete reviewer–author exchange, associated notes, AC feedback and the final decision—not every unrelated side-thread. Evidence sources include public OpenReview records, author-maintained PDFs and publicly indexed raw discussion datasets. Some live pages require verification. Each [structured record](cases.json) preserves provenance, scope, note links and score qualifications.

For ICLR 2026, publicly displayed scores/reviews were rolled back; do not confuse a historical reviewer statement, unconditional intention, conditional promise, author report, AC historical recollection, or AC prediction. See [evidence/follow-up rules](evidence-and-followup.md).

## Six teaching roles

| Role | Count | How to use it |
|---|---:|---|
| \`core_positive\` | 22 | Accepted, reviewer first-person numeric raise or unconditional numeric intention, traceable issue/action/feedback, a distinct and teachable mechanism |
| \`extended_positive\` | 16 | Useful additional mechanism, narrower field or overlap with core; keep score attribution limits |
| \`qualified_positive\` | 19 | Qualified positive example: conditions, intentions, initial positive reviewers, snapshot dependence, attribution mixtures or problematic rhetoric |
| \`outcome_counterexample\` | 6 | Improved reviews with rejection, or an unclosed condition; prevents equating score movement and acceptance |
| \`evidence_exclusion\` | 2 | Anomalous jump excluded by an AC or unresolved conflicts in score provenance; retain for auditing, not clean reversal proof |
| \`context_only\` | 5 | AC independent decision-making, reviewer acknowledgment without raise, or already-positive initial assessment |

## Core-positive admission test

1. At least one reviewer’s **first-person explicit numeric score statement** or **unconditional numeric intention**; no reliance solely on an author summary, AC prediction, or an unfulfilled condition.
2. Final paper decision: accepted. This does not demonstrate that the intervention caused acceptance.
3. The original concern, author action, reviewer reaction and remaining scope can be traced.
4. Prefer complementary, generalizable mechanisms over maximum point jump, Oral status, or impressive-sounding rhetoric.
5. For a paper with mixed evidence, label and reuse **only the qualifying reviewer path** as the core exemplar.

Core by year: 16 (2026), 2 (2025), 4 (2024). The record's \`selection.core_numeric_anchor\` holds the relevant source and wording attribution. It **does not** convert an intention into a saved score. Core membership **does not** imply unanimous support or resolution of every limitation.

## Mechanisms covered

| Mechanism tag | Practical question | Examples |
|---|---|---|
| \`baseline_fairness\` | Are datasets, tuning and inference conditions matched? | PF-LRM, NSPO, Explainable Unlearning |
| \`theory_repair\` | Is the theorem true, and does it actually justify this claim? | Best-of-N, Taming Denoisers |
| \`novelty\` / \`related_work\` | Which component is genuinely new? | LCA, GenSE |
| \`claim_scope\` | Where does the evidence stop? | InnovatorBench, GPG |
| \`multi_round\` | Which concern remains after the first response? | NSPO, SCUBA, Self-Debug |
| \`benchmark_value\` | Does the benchmark support meaningful scientific use? | SCUBA, InnovatorBench |
| \`evaluation\` | Do the judge and metrics measure the intended construct? | FASA, Procedural Mistake Detection |
| \`efficiency\` | Are actual runtime, hardware and costs documented? | Atomic HINs, Conductor |
| \`paper_revision\` | Were claimed fixes incorporated in the manuscript? | GPG, CO-MOT |
| \`negative_results\` | Are inconvenient outcomes handled honestly? | InnovatorBench |
| \`ac_summary\` | Does the summary attribute reviewer positions correctly? | FASA, DeMo (qualified) |

## Why spectacular cases may be excluded or qualified

Exclusion is **use-specific**, not a judgment of paper quality. The complete table of 19 notable cases, with links and reasons, appears in the [English README](../../../README.md#why-some-spectacular-jumps-are-not-core-templates). Key rules:

- **Anomalous score:** Dynamic Neural Fortresses' apparent 1→8 was explicitly discarded as an outlier by the AC; not reliable evidence that the author’s text caused a reversal.
- **Conflicting sources:** NetMoE’s paired score snapshot and AC description of initial scores disagree; retain the conflict rather than cherry-picking the larger change.
- **Score increases but rejected:** MonoSoup, Shallow Diffuse, GRIC and ASMG demonstrate that additional scores or apparent consensus are not a sufficient decision criterion.
- **Unfulfilled conditions / predictions:** Censoring, DeMo, InfoNCE, PLAGUE and GAGA require exact attribution of reviewer promises and AC inferences.
- **Good numbers, bad transferable strategy:** Quantum Attention's 4→8 illustrates proof repair but a reviewer complained about original manuscript maturity. Learning Delays in SNNs received aggressive-tone criticism; do not imitate the rhetoric.
- **Confounded attribution:** Accelerated Parallel Tempering involved reviewer-to-reviewer discussion, not only author reply.
- **Supporter boosts vs negative-to-positive:** BiasFreeBench, Token-Efficient Items, Steering Music Generation and Self-Correction have score-source/initial-score/conditional distinctions.

## When using or updating a case

Retrieve the original review and relevant author/reviewer notes. Record exact score wording and whether it's an actual reported change, stated goal, conditional promise, AC recollection or prediction. Keep the objection, intervention, feedback and limitation together. Do not quote more from a single third-party copyrighted source than permitted. Prefer concise paraphrases and direct OpenReview links. For complete 70-paper navigation, see [English casebook](casebook.md) or [detailed Chinese casebook](casebook.zh-CN.md).
