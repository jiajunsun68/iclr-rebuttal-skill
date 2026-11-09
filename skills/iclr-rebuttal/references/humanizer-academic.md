# Academic Humanizer: make rebuttals readable without changing evidence

[English](humanizer-academic.md) · [简体中文完整指南与示例](humanizer-academic.zh-CN.md)

This module is an **academic adaptation** of selected principles from [blader/humanizer](https://github.com/blader/humanizer), pinned to [commit 0ef9fe5bc3572734fd3ae6c448fe00a30cd5dcf0](https://github.com/blader/humanizer/commit/0ef9fe5bc3572734fd3ae6c448fe00a30cd5dcf0) (upstream SKILL.md v3.1.0, 26 patterns). Upstream copyright **Copyright (c) 2025 Siqi Chen**, MIT license; see [unmodified MIT notice](humanizer-LICENSE.txt) and [third-party notices](../../../THIRD_PARTY_NOTICES.md). This adaptation is not endorsed by the original author.

**Goal:** reviewers should find the answer, evidence and revision quickly. This is *not* a detector-evasion tool. Do not change reporting/disclosure obligations or make up experiments, emotion, personal experience or citations to sound more human.

## 1. Non-negotiable order

1. Read the exact reviewer concern and draft alongside manuscript claims and verified results.
2. Lock numbers, units, signs, comparisons, statistical test and interpretation, formulas, hypotheses, scope, reviewer IDs, citation keys and real manuscript locations.
3. Lock completion (\`planned\`, \`running\`, \`verified\`, \`incorporated\`) and reviewer (\`conditional\`, \`confirmed\`, \`silent\`) states.
4. Improve **argument order** before rewriting sentences: answer first, then decisive evidence, actual revision, remaining boundary.
5. Remove decoration; preserve real contrasts, hedges and technical terms.
6. Compare edited text sentence-by-sentence against the fact ledger and report any substantial corrected claim.

## 2. Academic adaptation of the 26 upstream patterns

These are *application decisions*, not translations of upstream prose.

| # | Stylistic adjustment | What academic rebuttals must retain |
|---:|---|---|
| 1 | Trim generic “not just X but Y” constructions | Real competing hypotheses, reviewer objections and necessary experiment contrasts |
| 2 | Remove aphoristic closing fragments | A short conclusion that genuinely changes the decision-relevant interpretation |
| 3 | Replace “the essence/fundamental insight” without content | Formally named theorems and actual technical constructs |
| 4 | Avoid performance openings (“let us dive in”, “honestly?”) | A direct response to the question |
| 5 | Do not invent a straw-man objection | Actual reviewer criticisms and documented alternatives |
| 6 | Avoid arbitrary groups of three | Three real seeds, ablations or hypotheses where appropriate |
| 7 | Remove accidental repetitive sentence openings | Repeated “we ran / we added” when it accurately attributes distinct work |
| 8 | Use functional punctuation rather than decorative dashes | Minus signs, ranges, technical terms, specified typography |
| 9 | Eliminate redundant weak hedges | \`under\`, \`assuming\`, \`may\`, \`within\`, \`in expectation\`, probability qualifiers |
| 10 | Fix awkward adjective compounds | Standard domain spelling, model names, command syntax |
| 11 | Prefer identifiable subjects/actions | Legitimate technical passive constructions; accurate shared authorship |
| 12 | Reduce vague fashionable vocabulary | Precise terms even if they appear frequently |
| 13 | Delete unsubstantiated grandeur | Measured effects and clearly explained actual contribution |
| 14 | State association only where established | Correlation must not be converted to causality |
| 15 | Simplify ornamental “-ing” phrases | Genuine constraints, intermediate steps and causal mechanisms |
| 16 | Replace marketing copy with protocol and results | Precise SOTA, benchmark or efficiency claims only if supported |
| 17 | Attribute factual statements to real sources | Necessary references; mark uncertain citations for verification |
| 18 | Prefer plain verbs where semantically adequate | Distinctions among \`represents\`, \`approximates\`, \`estimates\` and \`is\` |
| 19 | Remove decorative bold emphasis | Question numbers, equations, reference anchors and helpful formatting |
| 20 | Make headings descriptive | Reviewer IDs, required response structure and mathematical arrows |
| 21 | Use venue-consistent quotation marks | Exact source quotes, Chinese punctuation and template conventions |
| 22 | Strip chat residue (“Hope this helps”) | A minimal genuine thank-you or relevant address |
| 23 | Remove irrelevant AI self-disclaimers | Genuine study dates, verification limits, pending experiments, disclosures |
| 24 | Avoid restating a title without information | Direct answer even if it naturally repeats the question |
| 25 | Cut commentary about document production | Actual changes to equations, sections, tables and appendices |
| 26 | Avoid repeating background before the answer | Enough math, assumptions and controls to let the reviewer verify the reasoning |

**Common hazards:** deleting a negative result (rule 13 or 16), removing \`may\` or \`assuming\` (rule 9), turning measured association into mechanism (rule 14), dropping actual revision locations (rule 25), and moving crucial evidence out of the reply (rule 26).

## 3. Practical edits

- Start with \`We retrained X using [matched data]\` instead of “We are grateful for this deeply insightful and important comment.”
- State disagreement precisely: “The budget is 10,000 optimization steps, not epochs. Our draft did not make the unit clear.”
- If an error is verified, acknowledge it plainly. “We omitted the relevant prior work and have added [citation] and [mechanism comparison].”
- State bounds directly: “The result holds for [assumptions] and does not imply [unsupported broader claim].”
- Preserve uncertainty: “We observed a 1.3-percentage-point difference over five seeds; we have not assessed statistical significance.”
- Do not turn \`we will evaluate\` into \`we evaluated\`, \`if the experiment completes\` into \`the result shows\`, or reviewer “would raise if X” into “raised.”

## 4. Twelve original before-and-after teaching examples

**Every number and setting below is hypothetical.** They illustrate editing behavior, not any of the 70 ICLR papers. Do not transplant them into a real rebuttal.

### Example 1 — baseline matching, no empty thanks

**Given:** baseline was retrained on the same split and Appendix B updated, no new metric supplied.

Before: “We sincerely thank the reviewer for this exceptionally insightful observation. We comprehensively retrained the baseline with the same training split and added details to Appendix B. We hope this fully resolves the concern.”

After: “We retrained the baseline using the same training split as our method. Appendix B now specifies the split for both models.”

### Example 2 — numerical effect without unsupported significance

**Given:** Test-D mean accuracy 81.2% ± 0.3% (ours), 79.9% ± 0.4% (baseline), five seeds, ± means across-seed SD; no significance test.

Before: “Our comprehensive evaluation demonstrates a significant gain of 1.3%.”

After: “Over five seeds on Test-D, accuracy was 81.2% ± 0.3% for our method and 79.9% ± 0.4% for the baseline, where ± denotes across-seed standard deviation. The difference is 1.3 percentage points; we have not tested statistical significance.”

### Example 3 — keep genuine training/inference contrast

**Given:** training uses ground-truth poses; inference takes RGB only; title has been narrowed.

Before: “This is not just about removing poses, but a revolutionary pose-free paradigm.”

After: “Training uses ground-truth camera poses, whereas inference takes only RGB images. The revised title limits the pose-free claim to inference.”

### Example 4 — novelty relative to a specific prior method

**Given:** \`\\cite{prior_A}\` freezes the encoder; ours updates encoder and head. Citation key here is illustrative.

Before: “Unlike all existing methods, we present an entirely groundbreaking framework.”

After: “The method in \`\\cite{prior_A}\` freezes the encoder. Our method jointly updates the encoder and prediction head.”

### Example 5 — keep necessary hedges

**Given:** two datasets measured; no cross-domain evaluation.

Before: “It could potentially possibly be argued that our results may suggest reduced overfitting.”

After: “The results suggest that the method may reduce overfitting in the two evaluated datasets. We have not evaluated cross-domain transfer.”

### Example 6 — keep a mathematically bounded guarantee

**Given:** \`f\` is \`L\`-smooth, \`x_{t+1}=x_t−η∇f(x_t)\`, and \`0<η<2/L\`.

Before: “Our fundamental result proves global convergence for arbitrary steps.”

After: “For an \`L\`-smooth \`f\` with \`x_{t+1}=x_t−η∇f(x_t)\` and \`0<η<2/L\`, the descent bound is \`f(x_{t+1})≤f(x_t)−η(1−Lη/2)‖∇f(x_t)‖²\`.” No assertion of global optimality follows from the given facts.

### Example 7 — completed versus running experiments

**Given:** ablation incorporated in Table 5; five-seed reruns still running, to be reported only if completed before deadline.

Before: “We have comprehensively established reproducibility with our additional experiments.”

After: “Table 5 now includes the completed ablation. The five-seed reruns are still running, so we cannot report their results yet. We will add them if they finish before the deadline.”

### Example 8 — do not delete a negative result

**Given:** accuracy changes A +1.2, B +0.4, C −0.3 percentage points.

Before: “Our approach improves performance consistently across all tasks.”

After: “Accuracy increases by 1.2 percentage points on A and 0.4 on B, and decreases by 0.3 on C.”

### Example 9 — retain the full latency measurement envelope

**Given:** A100 80 GB GPU, FP16, batch 1, 100 warm-up iterations, 1,000 timed runs, median inference latency 3.4 ms vs 5.2 ms; training unmeasured.

Before: “Our method offers exceptionally efficient and robust execution.”

After: “On one A100 80 GB GPU in FP16 at batch size 1, median per-sample inference latency is 3.4 ms versus 5.2 ms for the baseline over 1,000 timed runs after 100 warm-up runs. Training cost was not measured.”

### Example 10 — preserve useful reviewer references

**Given:** R2-W1 asked about loss terms; definition incorporated after Eq. (3), worked example in Appendix C.

Before: “**A Comprehensive And Transformative Clarification** — we have clarified the definition very clearly!”

After: “**R2-W1: Loss-term definition.** We now define the loss terms immediately after Eq. (3), with a worked example in Appendix C.”

### Example 11 — correct a misunderstanding without insulting the reviewer

**Given:** budget was 10,000 optimization steps, not epochs, and Section 4 was corrected.

Before: “The reviewer has clearly misunderstood something that should be obvious.”

After: “The budget is 10,000 optimization steps, not epochs. Our original wording did not make the unit clear; we have clarified it in Section 4.”

### Example 12 — preserve required disclosure

**Given:** a hypothetical venue requires this verified disclosure; this is **not** an assertion about ICLR policy.

Before: “Certainly! Here is our polished reply. We used an LLM for language editing and verified all technical claims. Hope this helps!”

After: “We used an LLM for language editing and verified all technical claims.”

## 5. Final semantic-diff checklist

Before approving any rewrite, compare each input fact with the output:

1. Numerical values, denominators, directions, units, standard deviations and intervals unchanged or correctly recomputed?
2. Baseline, model version, training/inference phase, budget, and data split accurate?
3. Correlation not promoted to causality; observations not turned into proofs or global laws?
4. Mathematical symbols, conditions, quantifiers and inequalities unchanged?
5. Planned/running/verified/incorporated states retained?
6. Reviewer vs author vs AC statements correctly attributed, conditions still attached?
7. Citations, reviewer IDs and real section/table pointers preserved?
8. Negative results, exceptions and venue disclosures retained?
9. No invented author anecdotes, feelings, apologies or commitments?
10. Text actually answers the review instead of merely substituting “natural” synonyms?
11. Any substantive correction of an unsupported claim identified for author review?
12. Format, anonymization, external links and AI disclosure requirements checked against the current venue?

In practice, return the edited submission text, a brief explanation of *substantive* changes (e.g., removed “all datasets” because C regressed), and only necessary questions about unverified facts. Do not append an arbitrary “human-likeness score” or claim to bypass detectors.
