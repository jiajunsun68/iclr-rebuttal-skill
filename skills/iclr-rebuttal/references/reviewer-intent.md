# Inferring reviewer concerns and choosing an evidence obligation

[English](reviewer-intent.md) · [简体中文完整规则](reviewer-intent.zh-CN.md)

This is a reproducible analysis framework, **not mind reading**. Infer an academic decision criterion from the review text and manuscript, never presumed reviewer identity, national origin, seniority, motives, emotion, or lab affiliation. A good rebuttal makes a claim more checkable, not simply more agreeable. Evidence and first-person score attribution remain separate.

## 1. Four layers of interpretation

1. **Source observation:** exact reviewer sentence and note/section; distinguish quotation from paraphrase.
2. **Explicit question:** comparison, definition, proof correction, limitation, missing baseline, etc.
3. **Hypothesized scientific blocker:** which alternative explanation would make the paper's conclusion unreliable? Record a different plausible interpretation if it changes the next action.
4. **Response:** what evidence or correction *would suffice* to answer the concern, and which actions are appropriate under actual resource constraints?

Record **two independent confidence levels**:

| Level | Interpretation of question | Importance to recommendation |
|---|---|---|
| High | Reviewer names specific confound, missing experiment, theorem or false assertion | Says it is a major issue / an explicit decision condition / latest remaining blocker |
| Medium | Review context points to a specific concern but has credible alternatives | Repeated or tied to a negative soundness/contribution assessment without a stated threshold |
| Low | Only “limited,” “weak,” “unclear,” or “not convincing” is given | No evidence that addressing this alone changes recommendation |

Never use fabricated probabilities like “87% likely.” Ask at most one targeted question if ambiguity affects experimental design. Phrase hypotheses to the author, **not** as if reviewer motives were known.

A useful question:

> We interpret the central concern as whether [testable issue], rather than only [alternative reading]. Is this the issue most relevant to your assessment?

Do not invent the alternative merely because it is easy to refute. First answer whichever portion is unambiguous.

## 2. Action rules

**Add data, measurements, or proof** when the criticism identifies a causal confound, an unverified theorem–implementation bridge, questionable evaluation validity, missing mechanism isolation, or unjustified scope. Prioritize a small discriminative test with matched control variables over a generic pile of datasets. Do not claim the proposed result before it exists.

**Rebut** when a reviewer's premise is concretely false under the paper's actual configuration, definition, or mathematics. Quote the exact evidence and correct only the false proposition, without attacking competence. Even a false premise may signal poor presentation; revise exposition if warranted.

**Concede, apologize where material, and correct** upon verifying missing related work, numerical mistakes, incorrect experimental setup, test leakage, invalid proof, or overclaiming. State which conclusions change. An omission is not fixed by a graceful apology without an actual citation or manuscript revision. Do not apologize for legitimate disagreement.

**Narrow the scope** if the original statement covers populations, assumptions, hardware, distributions or settings not justified by results. Clearly name the new scope and why the contribution remains relevant.

**Explain why a demand is out of scope** only after verifying what the *paper itself* promises. A new environment may be irrelevant to a limited theorem, but a broad claim of universality makes a cross-domain request relevant.

**Mark unresolved** when data or compute cannot be obtained. Distinguish a scientific obligation from a currently feasible experimental commitment.

## 3. Seventeen recurring reviewer-comment types

For each type, the suggested wording is **new teaching language**, not quoted from ICLR authors; examples must be populated using the submitter's verified facts.

### 01. Missing a genuinely competitive baseline

**Possible blocker:** improvements only hold versus a weak comparator. **Sufficient evidence:** reproduce the strongest relevant method on a matched dataset/protocol/budget; document differences in objective, compute and implementation. **Action:** run a matched baseline or narrow the head-to-head claim. **Example:** “We reran [baseline] with the same [verified conditions]. Under this comparison, [actual result].”

**Relevant cases:** PF-LRM (C64), Explainable Unlearning (C09), Conductor (C17).

### 02. Baseline may be undertuned or unfairly tuned

**Blocker:** apparent gains come from search-budget asymmetry. **Evidence:** match hyperparameter trials/compute or provide a transparent budget sensitivity curve. Equal sample count does not imply equal tuning effort. **Action:** concede any verified mismatch, run fair controls if feasible, and disclose limitations. **Cases:** DeMo (C37), NSPO (C10).

### 03. A component’s contribution is not isolated

**Blocker:** the full system works but the advertised mechanism may be unnecessary. **Evidence:** targeted remove/replace/hold-fixed ablations, not unrelated new datasets. **Action:** matched ablation or narrower explanation. **Cases:** Self-Debug (C67), Open the Black Box (C66), Conductor (C17).

### 04. Means conceal failures or trade-offs

**Blocker:** average accuracy obscures severe cases, subgroup regressions, safety–utility costs or calibration failures. **Evidence:** distribution, subgroup, full matrix and negative cases with sample counts. **Action:** report actual breakdown and narrow “consistently improves.” **Cases:** FASA (C02), InnovatorBench (C19).

### 05. The theorem does not cover the implemented algorithm

**Blocker:** stationary/perfect/idealized condition does not apply to finite-step approximation. **Evidence:** prove the actual variant or explicitly state approximation residuals, assumptions and failure conditions. **Action:** repair theorem/proof; do not substitute another benchmark for a missing logical implication. **Cases:** NSPO (C10), Taming Score-Based Denoisers (C23).

### 06. Definitions, notation, or probability model are unclear

**Blocker:** a mathematical assertion cannot be reproduced because random sources, conditioning, quantifiers, variables or update rules are ambiguous. **Evidence:** explicit formal definition, worked example and corrected statement. **Action:** clarify or concede actual inconsistency. **Cases:** Softmax Transformers (C18), Bilevel Uniform Convexity (C39).

### 07. The method appears to be a combination or simplification of known components

**Blocker:** the claimed novelty already exists, or the additional knowledge is unspecified. **Evidence:** comparison to nearest prior work and isolated novelty (new result, problem, property, mechanism or capability). **Action:** acknowledge inherited components and amend contribution statements. **Cases:** LCA (C28), GenSE (C52).

### 08. Results are tested only on narrow datasets or model families

**Blocker:** conclusions overgeneralize. **Evidence:** diagnostic transfer test when feasible, or precise task/model/distribution bounds; failures are informative. **Action:** experiment or narrow scope. **Cases:** InnovatorBench (C19), GPG (C13), In-Context Dynamics (C68).

### 09. Search, preprocessing, or deployment cost is hidden

**Blocker:** savings omit expensive operations or use incomparable hardware. **Evidence:** timing setup, GPU, batch size, precision, warm-up, search trials, preprocessing, memory, network traffic and amortization. **Action:** measure or remove unsupported “efficient” claims. **Cases:** Atomic HINs (C26), ThunderKittens (C60).

### 10. Model/threshold selection may leak test information

**Blocker:** results reflect choices made on the test set. **Evidence:** selection rules, validation holdout, locked thresholds and separation of training/validation/test. **Action:** correct leaked protocols; rerun if necessary. **Cases:** Procedural Mistake Detection (C32).

### 11. A conditional guarantee is being misread as existence or attainability

**Blocker:** a bound conditioned on a good initial state is presented as an algorithm that achieves it. **Evidence:** explicit antecedents, constructive conditions where actually proven, statement of what is not guaranteed. **Action:** repair derivation/claim scope. **Cases:** Guarantees for Dataset Distillation (C34), Best-of-N (C12).

### 12. An estimator lacks calibration or practical utility

**Blocker:** theoretical quantity is uninterpretable or biased in realistic settings. **Evidence:** compare estimates with computable ground truth, quantify error and give a valid use case. **Action:** calibrate or limit applications. **Cases:** Metric Tensors on Neuromanifolds (C33).

### 13. Reviewer asks for real-world data or a different algorithm outside the stated theorem

**Blocker:** unclear how the toy theorem relates to external practice. **Evidence:** explicitly distinguish the mathematical object from untested settings; add bridge tests only if claims require them. **Action:** explain or narrow scope, not automatic acceptance/refusal of all expansion requests. **Cases:** In-Context Dynamics (C68), Role of Locality (C69).

### 14. A verifiable premise such as “there is no code” or “no ablation” is incorrect

**Blocker:** reviewer may have missed a submitted artifact, or the artifact was not discoverable. **Evidence:** exact version, link/section/commit within conference rules and what it contains. **Action:** factual rebuttal plus clearer manuscript reference if warranted. Never allege incompetence.

### 15. Mechanism is only a narrative without measurement

**Blocker:** post hoc explanation may fit any outcome. **Evidence:** intervention, probing or prediction that distinguishes mechanism hypotheses, including failure cases. **Action:** targeted measurement or change causal language into a hypothesis. **Cases:** FACT (C25), Self-Representation Alignment (C40).

### 16. Reviewer and author disagree on benchmark value or cost objective

**Blocker:** task utility and intended use are not convincing. **Evidence:** concrete downstream use, training/data collection procedure, task generator, reproducible evaluator and operational cost. **Action:** demonstrate usability, not just aggregate leaderboard scores. **Cases:** SCUBA (C15), InnovatorBench (C19).

### 17. Complexity model, numerical precision or hidden terms differ

**Blocker:** speedup/proof depends on inaccessible precision, classical routines, hidden exponential factors or mismatched hardware. **Evidence:** explicit asymptotics and finite-instance costs, numerical error, subroutine assumptions and real runtime when relevant. **Action:** theoretical repair and/or practical benchmarking. **Cases:** Quantum Attention (C27), Atomic HINs (C26).

## 4. Iterative rebuttal: focus on the latest objection

After each reviewer follow-up:

- Determine what was **actually accepted** and what remained; do not repeat previous paragraphs.
- Check new concern against the fact ledger; change experiment only if a new confound is identified.
- Record the reviewer's exact statement about scores and whether it is unconditional or conditional.
- Respond promptly but within the venue's rules. Ask one precise question only where useful; do not nag about ratings.

Use NSPO C10 (2→4→6), SCUBA C15 (2→4→6), Self-Debug C67 (3→5→6) as contrasting staged discussions. Do not infer a generic “second message guarantees acceptance.”

## 5. AC summary and provenance

The AC must be able to independently verify major updates:

1. Initial rejection basis, not a rewritten caricature.
2. Completed evidence and its controls, including negative findings.
3. Real revision locations and dates/versions.
4. Reviewer-specific reactions, verbatim meaning and note IDs, not the author's summary of unanimity.
5. Conditions, unresolved limitations and silent reviewers.

**ICLR 2026:** original displayed scores were rolled back. The AC can reach an independent acceptance decision. Distinguish reviewer numeric self-report, intention, AC recollection and AC expectation.

## 6. Analyst worksheet

| Reviewer / anchor | Explicit request | Falsifiable concern | Interpretation confidence | Decision-impact confidence | Alternative reading | Discriminative evidence | Required action | Actual work state | Reviewer stance | Manuscript location |
|---|---|---|---|---|---|---|---|---|---|---|
| R? / note? | [verbatim] | [hypothesis] | high / medium / low + reason | high / medium / low + reason | [one if relevant] | [control / proof] | evidence / rebut / concede / narrow / clarify | planned / running / verified / incorporated | unresolved / conditional / explicit / confirmed | section / table / pending |

## 7. Last checks

Does the reply address the actual alternative explanation? Is the claim justified under matched conditions? Are uncompleted experiments described in future tense? Are author/AC predictions kept distinct from reviewer's own statements? Was any supported mathematical condition or negative result removed in “humanization”? Is the proposed work achievable and within the declared research question? If not, correct or flag before release.
