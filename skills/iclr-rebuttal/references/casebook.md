# ICLR rebuttal: 70 annotated cases (English)

[English (default)](casebook.md) · [简体中文完整案例详录](casebook.zh-CN.md)

**Evidence summary, not reproduced review text.** 70 unique OpenReview paper forums: ICLR 2026 (49), 2025 (12), 2024 (9). 22 core positive examples, 16 extended positives, 19 qualified positives, 6 outcome counterexamples, 2 numerical evidence exclusions and 5 context-only records. Read the [selection methodology](case-selection.md) before treating any score trajectory as evidence of reversal.

**ICLR 2026 warning:** Following the security incident, review scores/text were rolled back. The current displayed rating cannot establish post-rebuttal score. Numeric changes in source notes are historical reviewer statements, intentions, author or AC records, or predictions, as separately labeled in [cases.json](cases.json). Acceptance is a different outcome and does not demonstrate a causal effect of any single reply.

## Quick index

| ID | ICLR | Paper | Role | Outcome |
|---|---:|---|---|---|
| [C01](#c01) | 2026 | BiasFreeBench | `qualified_positive` | Accept (Poster) |
| [C02](#c02) | 2026 | FASA | `core_positive` | Accept (Poster) |
| [C03](#c03) | 2026 | Evaluating Memory in LLM Agents via Incremental Multi-Turn Interactions | `context_only` | Accept (Poster) |
| [C04](#c04) | 2026 | Token-Efficient Item Representation via Images for LLM Recommender Systems | `qualified_positive` | Accept (Poster) |
| [C05](#c05) | 2026 | How to train data-efficient LLMs | `context_only` | Accept (Poster) |
| [C06](#c06) | 2026 | Steering Autoregressive Music Generation with Recursive Feature Machines | `qualified_positive` | Accept (Poster) |
| [C07](#c07) | 2026 | Importance Sampling for Multi-Negative Multimodal Direct Preference Optimization | `context_only` | Accept (Poster) |
| [C08](#c08) | 2026 | Extending the Context of Pretrained LLMs by Dropping Their Positional Embedding | `extended_positive` | Accept (Poster) |
| [C09](#c09) | 2026 | Explainable LLM Unlearning through Reasoning | `core_positive` | Accept (Poster) |
| [C10](#c10) | 2026 | Mitigating the Safety Alignment Tax with Null-Space Constrained Policy Optimization | `core_positive` | Accept (Poster) |
| [C11](#c11) | 2026 | Keep the Best, Forget the Rest | `core_positive` | Accept (Poster) |
| [C12](#c12) | 2026 | Best-of-N through the Smoothing Lens | `core_positive` | Accept (Poster) |
| [C13](#c13) | 2026 | GPG | `core_positive` | Accept (Poster) |
| [C14](#c14) | 2026 | MCP-SafetyBench | `extended_positive` | Accept (Poster) |
| [C15](#c15) | 2026 | SCUBA | `core_positive` | Accept (Poster) |
| [C16](#c16) | 2026 | Towards Safe Reasoning in Large Reasoning Models via Corrective Intervention | `qualified_positive` | Accept (Poster) |
| [C17](#c17) | 2026 | Learning to Orchestrate Agents in Natural Language with the Conductor | `core_positive` | Accept (Poster) |
| [C18](#c18) | 2026 | Softmax Transformers are Turing-Complete | `core_positive` | Accept (Oral) |
| [C19](#c19) | 2026 | InnovatorBench | `core_positive` | Accept (Poster) |
| [C20](#c20) | 2026 | Semantic Voting | `extended_positive` | Accept (Poster) |
| [C21](#c21) | 2026 | PEERING INTO THE UNKNOWN | `extended_positive` | Accept (Poster) |
| [C22](#c22) | 2026 | Triangle Multiplication | `extended_positive` | Accept (Poster) |
| [C23](#c23) | 2026 | Taming Score-Based Denoisers | `core_positive` | Accept (Poster) |
| [C24](#c24) | 2026 | MOSAIC | `extended_positive` | Accept (Poster) |
| [C25](#c25) | 2026 | FACT | `core_positive` | Accept (Poster) |
| [C26](#c26) | 2026 | Atomic HINs | `core_positive` | Accept (Poster) |
| [C27](#c27) | 2026 | Quantum Attention Approximation | `qualified_positive` | Accept (Poster) |
| [C28](#c28) | 2026 | LCA | `core_positive` | Accept (Poster) |
| [C29](#c29) | 2026 | Learning to Segment for VRP | `extended_positive` | Accept (Oral) |
| [C30](#c30) | 2026 | LoRA meets Riemannion | `extended_positive` | Accept (Poster) |
| [C31](#c31) | 2026 | Decoupling Dynamical Richness | `qualified_positive` | Accept (Poster) |
| [C32](#c32) | 2026 | Procedural Mistake Detection | `core_positive` | Accept (Poster) |
| [C33](#c33) | 2026 | Metric Tensors on Neuromanifolds | `core_positive` | Accept (Poster) |
| [C34](#c34) | 2026 | Guarantees for Dataset Distillation | `qualified_positive` | Accept (Poster) |
| [C35](#c35) | 2026 | Dense Associative Memory Dynamics | `qualified_positive` | Accept (Poster) |
| [C36](#c36) | 2026 | WILD-Diffusion | `extended_positive` | Accept (Poster) |
| [C37](#c37) | 2026 | DeMo | `qualified_positive` | Accept (Poster) |
| [C38](#c38) | 2026 | Accelerated Parallel Tempering | `qualified_positive` | Accept (Poster) |
| [C39](#c39) | 2026 | Bilevel Uniform Convexity | `extended_positive` | Accept (Poster) |
| [C40](#c40) | 2026 | Self-Representation Alignment | `extended_positive` | Accept (Poster) |
| [C41](#c41) | 2026 | Reassessing Layer Pruning | `qualified_positive` | Accept (Poster) |
| [C42](#c42) | 2026 | SuperMAN / GMAN | `qualified_positive` | Accept (Poster) |
| [C43](#c43) | 2026 | MonoSoup | `outcome_counterexample` | Reject |
| [C44](#c44) | 2026 | FuseGPT | `outcome_counterexample` | Reject |
| [C45](#c45) | 2026 | Censoring with Plausible Deniability | `outcome_counterexample` | Reject |
| [C46](#c46) | 2026 | ASMG | `outcome_counterexample` | Reject |
| [C47](#c47) | 2026 | InfoNCE Induces Gaussian Distribution | `context_only` | Accept (Oral) |
| [C48](#c48) | 2026 | GAGA | `qualified_positive` | Accept (Poster) |
| [C49](#c49) | 2026 | PLAGUE | `context_only` | Accept (Poster) |
| [C50](#c50) | 2025 | Dynamic Neural Fortresses | `evidence_exclusion` | Accept (Poster) |
| [C51](#c51) | 2025 | BiGR | `extended_positive` | Accept (Poster) |
| [C52](#c52) | 2025 | GenSE | `core_positive` | Accept (Poster) |
| [C53](#c53) | 2025 | CO-MOT | `core_positive` | Accept (Poster) |
| [C54](#c54) | 2025 | Variational Bayesian Pseudo-Coreset | `qualified_positive` | Accept (Poster) |
| [C55](#c55) | 2025 | Generation and Comprehension Hand-in-Hand | `extended_positive` | Accept (Poster) |
| [C56](#c56) | 2025 | Shallow Diffuse | `outcome_counterexample` | Reject |
| [C57](#c57) | 2025 | GRIC | `outcome_counterexample` | Reject |
| [C58](#c58) | 2025 | Multi-modal Agent Tuning | `qualified_positive` | Accept (Spotlight) |
| [C59](#c59) | 2025 | NetMoE | `evidence_exclusion` | Accept (Spotlight) |
| [C60](#c60) | 2025 | ThunderKittens | `qualified_positive` | Accept (Spotlight) |
| [C61](#c61) | 2025 | Bayesian Optimization via Continual Variational Last Layer Training | `qualified_positive` | Accept (Spotlight) |
| [C62](#c62) | 2024 | Large Language Models Cannot Self-Correct Reasoning Yet | `qualified_positive` | Accept (Poster) |
| [C63](#c63) | 2024 | Adaptive Rational Activations to Boost Deep Reinforcement Learning | `extended_positive` | Accept (Spotlight) |
| [C64](#c64) | 2024 | PF-LRM | `core_positive` | Accept (Spotlight) |
| [C65](#c65) | 2024 | Learning Delays in Spiking Neural Networks using Dilated Convolutions with Learnable Spacings | `qualified_positive` | Accept (Poster) |
| [C66](#c66) | 2024 | Open the Black Box | `extended_positive` | Accept (Poster) |
| [C67](#c67) | 2024 | Teaching Large Language Models to Self-Debug | `core_positive` | Accept (Poster) |
| [C68](#c68) | 2024 | In-Context Learning Dynamics with Random Binary Sequences | `core_positive` | Accept (Poster) |
| [C69](#c69) | 2024 | Role of Locality and Weight Sharing in Image-Based Tasks | `core_positive` | Accept (Spotlight) |
| [C70](#c70) | 2024 | MovingParts | `extended_positive` | Accept (Spotlight) |

## Annotated discussions

### C01 — BiasFreeBench (2026)

**Selection:** `qualified_positive`. **Outcome:** Accept (Poster). **Mechanisms:** `novelty`, `evaluation`, `claim_scope`, `ac_summary`.

**Concern:** Novelty and judge dependence in a fairness benchmark

**Author action and observed response:** Authors clarified contribution and evaluated a different judge; a reviewer acknowledged an increase

**Why teach / qualify this case:** Positive or improved outcome requiring attribution, condition, timing, rhetoric, or reviewer-stance qualifications. Authors clarified contribution and evaluated a different judge; a reviewer acknowledged an increase

**Do not overgeneralize:** Reviewer did not personally state the numeric target 6; that target comes from the authors' summary The ICLR 2026 rating rollback also applies.

**Sources:** [OpenReview discussion](https://openreview.net/forum?id=Ncf2LFDT4e) · [Key evidence note](https://openreview.net/forum?id=Ncf2LFDT4e&noteId=nshgScU10i) · [AC](https://openreview.net/forum?id=Ncf2LFDT4e&noteId=HbFJkG8TZA) · [Full original Chinese analysis](casebook.zh-CN.md#c01). Detailed source IDs, conditions, archive and historic rating statements are in [cases.json](cases.json).

---

### C02 — FASA (2026)

**Selection:** `core_positive`. **Outcome:** Accept (Poster). **Mechanisms:** `evaluation`, `multi_round`, `claim_scope`, `ac_summary`.

**Concern:** Calibration, sparsity evidence, and theoretical basis

**Author action and observed response:** Clarified task-independent calibration and added evidence; reviewer explicitly moved 4→6

**Why teach / qualify this case:** Primary accepted example with a reviewer’s first-person numeric raise or unconditional numeric intention and a traceable action–feedback chain. Clarified task-independent calibration and added evidence; reviewer explicitly moved 4→6

**Do not overgeneralize:** Theory and some sparsity concerns survived; raised score does not mean full resolution The ICLR 2026 rating rollback also applies.

**Sources:** [OpenReview discussion](https://openreview.net/forum?id=FnSgecCEwg) · [Key evidence note](https://openreview.net/forum?id=FnSgecCEwg&noteId=un60K64zf2) · [AC](https://openreview.net/forum?id=FnSgecCEwg&noteId=Tg1YSs21TV) · [Full original Chinese analysis](casebook.zh-CN.md#c02). Detailed source IDs, conditions, archive and historic rating statements are in [cases.json](cases.json).

---

### C03 — Evaluating Memory in LLM Agents via Incremental Multi-Turn Interactions (2026)

**Selection:** `context_only`. **Outcome:** Accept (Poster). **Mechanisms:** `baseline_fairness`, `benchmark_value`, `evaluation`.

**Concern:** Memory benchmark validity and matched model comparisons

**Author action and observed response:** Compute-matched controls and negative checks were examined in the AC's assessment

**Why teach / qualify this case:** Decision or discussion context with no confirmed negative-to-positive numeric reviewer path. Compute-matched controls and negative checks were examined in the AC's assessment

**Do not overgeneralize:** No first-person numeric raise is established; use for decision context only The ICLR 2026 rating rollback also applies.

**Sources:** [OpenReview discussion](https://openreview.net/forum?id=DT7JyQC3MR) · [Key evidence note](https://openreview.net/forum?id=DT7JyQC3MR&noteId=RwE8eXFlXJ) · [AC](https://openreview.net/forum?id=DT7JyQC3MR&noteId=RwE8eXFlXJ) · [Full original Chinese analysis](casebook.zh-CN.md#c03). Detailed source IDs, conditions, archive and historic rating statements are in [cases.json](cases.json).

---

### C04 — Token-Efficient Item Representation via Images for LLM Recommender Systems (2026)

**Selection:** `qualified_positive`. **Outcome:** Accept (Poster). **Mechanisms:** `claim_scope`, `baseline_fairness`, `efficiency`.

**Concern:** Image-token representation efficiency and claim boundaries

**Author action and observed response:** Authors narrowed the title and answered efficiency and fairness questions; supportive reviewers increased support

**Why teach / qualify this case:** Positive or improved outcome requiring attribution, condition, timing, rhetoric, or reviewer-stance qualifications. Authors narrowed the title and answered efficiency and fairness questions; supportive reviewers increased support

**Do not overgeneralize:** Both target score numbers are from author summary and initial reviewers were already supportive The ICLR 2026 rating rollback also applies.

**Sources:** [OpenReview discussion](https://openreview.net/forum?id=vizM7B7vuW) · [Key evidence note](https://openreview.net/forum?id=vizM7B7vuW&noteId=tr1dPtDDM5) · [AC](https://openreview.net/forum?id=vizM7B7vuW&noteId=JRzaD8lqoH) · [Full original Chinese analysis](casebook.zh-CN.md#c04). Detailed source IDs, conditions, archive and historic rating statements are in [cases.json](cases.json).

---

### C05 — How to train data-efficient LLMs (2026)

**Selection:** `context_only`. **Outcome:** Accept (Poster). **Mechanisms:** `efficiency`, `evaluation`, `ac_summary`.

**Concern:** Efficiency and qualitative evidence for data-efficient LLM training

**Author action and observed response:** Authors clarified cost and supporting observations for an already positively reviewed paper

**Why teach / qualify this case:** Decision or discussion context with no confirmed negative-to-positive numeric reviewer path. Authors clarified cost and supporting observations for an already positively reviewed paper

**Do not overgeneralize:** Only an AC expectation of improvement is available, not reviewer numeric changes The ICLR 2026 rating rollback also applies.

**Sources:** [OpenReview discussion](https://openreview.net/forum?id=yKUbw7q1IA) · [Key evidence note](https://openreview.net/forum?id=yKUbw7q1IA&noteId=CaiBtzcKaD) · [AC](https://openreview.net/forum?id=yKUbw7q1IA&noteId=CaiBtzcKaD) · [Full original Chinese analysis](casebook.zh-CN.md#c05). Detailed source IDs, conditions, archive and historic rating statements are in [cases.json](cases.json).

---

### C06 — Steering Autoregressive Music Generation with Recursive Feature Machines (2026)

**Selection:** `qualified_positive`. **Outcome:** Accept (Poster). **Mechanisms:** `baseline_fairness`, `evaluation`, `ac_summary`.

**Concern:** Music-generation steering evaluation and independent baselines

**Author action and observed response:** Added independent audio metrics and a prompt-only baseline to probe steering effects

**Why teach / qualify this case:** Positive or improved outcome requiring attribution, condition, timing, rhetoric, or reviewer-stance qualifications. Added independent audio metrics and a prompt-only baseline to probe steering effects

**Do not overgeneralize:** The 8→10 increase was a supporter's intention, not a negative-to-positive reversal The ICLR 2026 rating rollback also applies.

**Sources:** [OpenReview discussion](https://openreview.net/forum?id=NaHzPMaCY9) · [Key evidence note](https://openreview.net/forum?id=NaHzPMaCY9&noteId=MMa8uE4NYd) · [AC](https://openreview.net/forum?id=NaHzPMaCY9&noteId=XeXbkPqOSi) · [Full original Chinese analysis](casebook.zh-CN.md#c06). Detailed source IDs, conditions, archive and historic rating statements are in [cases.json](cases.json).

---

### C07 — Importance Sampling for Multi-Negative Multimodal Direct Preference Optimization (2026)

**Selection:** `context_only`. **Outcome:** Accept (Poster). **Mechanisms:** `related_work`, `theory_repair`, `evaluation`, `ac_summary`.

**Concern:** Theory and evaluation of importance-sampled multimodal preference optimization

**Author action and observed response:** Author answers addressed a critical reviewer's stated concern and clarified related work

**Why teach / qualify this case:** Decision or discussion context with no confirmed negative-to-positive numeric reviewer path. Author answers addressed a critical reviewer's stated concern and clarified related work

**Do not overgeneralize:** Reviewer acknowledgment did not produce a confirmed score raise; another remained at 6 The ICLR 2026 rating rollback also applies.

**Sources:** [OpenReview discussion](https://openreview.net/forum?id=HEFPwoGtTj) · [Key evidence note](https://openreview.net/forum?id=HEFPwoGtTj&noteId=FBjEoeEWB3) · [AC](https://openreview.net/forum?id=HEFPwoGtTj&noteId=7NQxOXTRhj) · [Full original Chinese analysis](casebook.zh-CN.md#c07). Detailed source IDs, conditions, archive and historic rating statements are in [cases.json](cases.json).

---

### C08 — Extending the Context of Pretrained LLMs by Dropping Their Positional Embedding (2026)

**Selection:** `extended_positive`. **Outcome:** Accept (Poster). **Mechanisms:** `evaluation`, `baseline_fairness`, `efficiency`, `claim_scope`.

**Concern:** Scale, context-length coverage and evaluation scope

**Author action and observed response:** Authors expanded tasks and sizes to address initially negative reviewers

**Why teach / qualify this case:** Supplementary accepted example, specialized or overlapping with a core teaching mechanism. Authors expanded tasks and sizes to address initially negative reviewers

**Do not overgeneralize:** Explicit 2→6 and 4→6 statements exist; mechanism overlaps with other core fairness cases The ICLR 2026 rating rollback also applies.

**Sources:** [OpenReview discussion](https://openreview.net/forum?id=RlPVSeKjoc) · [Key evidence note](https://openreview.net/forum?id=RlPVSeKjoc&noteId=NZTVcCaQeq) · [AC](https://openreview.net/forum?id=RlPVSeKjoc&noteId=5nSLvw6Y3l) · [Full original Chinese analysis](casebook.zh-CN.md#c08). Detailed source IDs, conditions, archive and historic rating statements are in [cases.json](cases.json).

---

### C09 — Explainable LLM Unlearning through Reasoning (2026)

**Selection:** `core_positive`. **Outcome:** Accept (Poster). **Mechanisms:** `baseline_fairness`, `evaluation`, `negative_results`, `paper_revision`, `multi_round`.

**Concern:** Weak unlearning baselines, reproduction, and metric validity

**Author action and observed response:** Audited and reran baselines, corrected comparisons and acknowledged competitor advantages; 2→6

**Why teach / qualify this case:** Primary accepted example with a reviewer’s first-person numeric raise or unconditional numeric intention and a traceable action–feedback chain. Audited and reran baselines, corrected comparisons and acknowledged competitor advantages; 2→6

**Do not overgeneralize:** Reviewer still withheld stronger endorsement because some optimality and metric issues remained The ICLR 2026 rating rollback also applies.

**Sources:** [OpenReview discussion](https://openreview.net/forum?id=wec4qy2XIF) · [Key evidence note](https://openreview.net/forum?id=wec4qy2XIF&noteId=yrS6CQAobd) · [AC](https://openreview.net/forum?id=wec4qy2XIF&noteId=FsLiSfcQ0F) · [Full original Chinese analysis](casebook.zh-CN.md#c09). Detailed source IDs, conditions, archive and historic rating statements are in [cases.json](cases.json).

---

### C10 — Mitigating the Safety Alignment Tax with Null-Space Constrained Policy Optimization (2026)

**Selection:** `core_positive`. **Outcome:** Accept (Poster). **Mechanisms:** `baseline_fairness`, `theory_repair`, `multi_round`, `negative_results`, `claim_scope`.

**Concern:** Fair safety–utility comparison and practical null-space assumptions

**Author action and observed response:** Matched reward model, used a distinct evaluator and explained approximation/distribution error; 2→4→6

**Why teach / qualify this case:** Primary accepted example with a reviewer’s first-person numeric raise or unconditional numeric intention and a traceable action–feedback chain. Matched reward model, used a distinct evaluator and explained approximation/distribution error; 2→4→6

**Do not overgeneralize:** Approximate projection does not imply zero safety–utility tax in realistic use The ICLR 2026 rating rollback also applies.

**Sources:** [OpenReview discussion](https://openreview.net/forum?id=GFyVxtyMvq) · [Key evidence note](https://openreview.net/forum?id=GFyVxtyMvq&noteId=XGLoZWrYhN) · [AC](https://openreview.net/forum?id=GFyVxtyMvq&noteId=8OagbtCjnd) · [Full original Chinese analysis](casebook.zh-CN.md#c10). Detailed source IDs, conditions, archive and historic rating statements are in [cases.json](cases.json).

---

### C11 — Keep the Best, Forget the Rest (2026)

**Selection:** `core_positive`. **Outcome:** Accept (Poster). **Mechanisms:** `evaluation`, `baseline_fairness`, `efficiency`, `paper_revision`.

**Concern:** Strong unlearning baseline and robustness of evaluation

**Author action and observed response:** Converted promised baseline, multi-judge and sensitivity tests into checked results and manuscript changes; 2→6

**Why teach / qualify this case:** Primary accepted example with a reviewer’s first-person numeric raise or unconditional numeric intention and a traceable action–feedback chain. Converted promised baseline, multi-judge and sensitivity tests into checked results and manuscript changes; 2→6

**Do not overgeneralize:** Pending experiments cannot be reported before they actually finish The ICLR 2026 rating rollback also applies.

**Sources:** [OpenReview discussion](https://openreview.net/forum?id=LrHfYPFTtg) · [Key evidence note](https://openreview.net/forum?id=LrHfYPFTtg&noteId=1nAh6t0eMT) · [AC](https://openreview.net/forum?id=LrHfYPFTtg&noteId=XZTFcu5TFW) · [Full original Chinese analysis](casebook.zh-CN.md#c11). Detailed source IDs, conditions, archive and historic rating statements are in [cases.json](cases.json).

---

### C12 — Best-of-N through the Smoothing Lens (2026)

**Selection:** `core_positive`. **Outcome:** Accept (Poster). **Mechanisms:** `theory_repair`, `claim_scope`, `multi_round`, `paper_revision`.

**Concern:** A theoretical upper bound insufficient to justify a performance explanation

**Author action and observed response:** Removed an overinterpreted theorem and rebuilt the argument through a more appropriate analysis; 2→6

**Why teach / qualify this case:** Primary accepted example with a reviewer’s first-person numeric raise or unconditional numeric intention and a traceable action–feedback chain. Removed an overinterpreted theorem and rebuilt the argument through a more appropriate analysis; 2→6

**Do not overgeneralize:** Do not claim the original inequality itself was false without separate proof The ICLR 2026 rating rollback also applies.

**Sources:** [OpenReview discussion](https://openreview.net/forum?id=tCv1D3M7Lb) · [Key evidence note](https://openreview.net/forum?id=tCv1D3M7Lb&noteId=VRswyacvFu) · [AC](https://openreview.net/forum?id=tCv1D3M7Lb&noteId=64HvM045i8) · [Full original Chinese analysis](casebook.zh-CN.md#c12). Detailed source IDs, conditions, archive and historic rating statements are in [cases.json](cases.json).

---

### C13 — GPG (2026)

**Selection:** `core_positive`. **Outcome:** Accept (Poster). **Mechanisms:** `claim_scope`, `evaluation`, `paper_revision`, `multi_round`.

**Concern:** Scope of the claimed guidance mechanism

**Author action and observed response:** Narrowed the applicable claim in the revised manuscript; reviewer then confirmed a move to 6

**Why teach / qualify this case:** Primary accepted example with a reviewer’s first-person numeric raise or unconditional numeric intention and a traceable action–feedback chain. Narrowed the applicable claim in the revised manuscript; reviewer then confirmed a move to 6

**Do not overgeneralize:** A promised scope revision must be incorporated before confirmation is claimed The ICLR 2026 rating rollback also applies.

**Sources:** [OpenReview discussion](https://openreview.net/forum?id=inccdtfx8x) · [Key evidence note](https://openreview.net/forum?id=inccdtfx8x&noteId=wHZtFOpZwy) · [AC](https://openreview.net/forum?id=inccdtfx8x&noteId=E4KfbiBnvw) · [Full original Chinese analysis](casebook.zh-CN.md#c13). Detailed source IDs, conditions, archive and historic rating statements are in [cases.json](cases.json).

---

### C14 — MCP-SafetyBench (2026)

**Selection:** `extended_positive`. **Outcome:** Accept (Poster). **Mechanisms:** `benchmark_value`, `evaluation`, `claim_scope`.

**Concern:** Safety benchmark threat model, orthogonal tests, and evaluator validity

**Author action and observed response:** Clarified threat assumptions and ran relevant ablations; one reviewer moved 4→6

**Why teach / qualify this case:** Supplementary accepted example, specialized or overlapping with a core teaching mechanism. Clarified threat assumptions and ran relevant ablations; one reviewer moved 4→6

**Do not overgeneralize:** This specialized benchmark complements rather than replaces the core benchmark examples The ICLR 2026 rating rollback also applies.

**Sources:** [OpenReview discussion](https://openreview.net/forum?id=7XYjeL46co) · [Key evidence note](https://openreview.net/forum?id=7XYjeL46co&noteId=yYqoQEPSGs) · [AC](https://openreview.net/forum?id=7XYjeL46co&noteId=987VZL48ZY) · [Full original Chinese analysis](casebook.zh-CN.md#c14). Detailed source IDs, conditions, archive and historic rating statements are in [cases.json](cases.json).

---

### C15 — SCUBA (2026)

**Selection:** `core_positive`. **Outcome:** Accept (Poster). **Mechanisms:** `benchmark_value`, `multi_round`, `evaluation`, `claim_scope`.

**Concern:** Whether a sandbox benchmark supports useful research beyond a leaderboard

**Author action and observed response:** Described trajectory collection, task synthesis and evaluation code; reviewer moved 2→4→6

**Why teach / qualify this case:** Primary accepted example with a reviewer’s first-person numeric raise or unconditional numeric intention and a traceable action–feedback chain. Described trajectory collection, task synthesis and evaluation code; reviewer moved 2→4→6

**Do not overgeneralize:** Do not promise unsupported task diversity, long-term maintenance or evaluation reliability The ICLR 2026 rating rollback also applies.

**Sources:** [OpenReview discussion](https://openreview.net/forum?id=bkjKnO9s7T) · [Key evidence note](https://openreview.net/forum?id=bkjKnO9s7T&noteId=xgQxWovHPV) · [AC](https://openreview.net/forum?id=bkjKnO9s7T&noteId=iUnVQlwyWn) · [Full original Chinese analysis](casebook.zh-CN.md#c15). Detailed source IDs, conditions, archive and historic rating statements are in [cases.json](cases.json).

---

### C16 — Towards Safe Reasoning in Large Reasoning Models via Corrective Intervention (2026)

**Selection:** `qualified_positive`. **Outcome:** Accept (Poster). **Mechanisms:** `evaluation`, `multi_round`, `claim_scope`, `negative_results`.

**Concern:** Safety evaluation breadth for reasoning agents

**Author action and observed response:** Added a language-only proxy and staged technical clarifications; reviewer expressed 2→4→6

**Why teach / qualify this case:** Positive or improved outcome requiring attribution, condition, timing, rhetoric, or reviewer-stance qualifications. Added a language-only proxy and staged technical clarifications; reviewer expressed 2→4→6

**Do not overgeneralize:** The proxy did not fully answer the request for agentic evaluation The ICLR 2026 rating rollback also applies.

**Sources:** [OpenReview discussion](https://openreview.net/forum?id=2uTxLC4LmC) · [Key evidence note](https://openreview.net/forum?id=2uTxLC4LmC&noteId=463GLSs3te) · [AC](https://openreview.net/forum?id=2uTxLC4LmC&noteId=IkgkFklkXB) · [Full original Chinese analysis](casebook.zh-CN.md#c16). Detailed source IDs, conditions, archive and historic rating statements are in [cases.json](cases.json).

---

### C17 — Learning to Orchestrate Agents in Natural Language with the Conductor (2026)

**Selection:** `core_positive`. **Outcome:** Accept (Poster). **Mechanisms:** `baseline_fairness`, `evaluation`, `efficiency`, `novelty`.

**Concern:** Whether a learned agent orchestration component is necessary

**Author action and observed response:** Replaced the module with a strong direct-model alternative and compared costs; reviewer moved 2→6

**Why teach / qualify this case:** Primary accepted example with a reviewer’s first-person numeric raise or unconditional numeric intention and a traceable action–feedback chain. Replaced the module with a strong direct-model alternative and compared costs; reviewer moved 2→6

**Do not overgeneralize:** A stronger baseline can weaken the original contribution; report the actual trade-off The ICLR 2026 rating rollback also applies.

**Sources:** [OpenReview discussion](https://openreview.net/forum?id=U23A2BUKYt) · [Key evidence note](https://openreview.net/forum?id=U23A2BUKYt&noteId=R0u45YQc2S) · [AC](https://openreview.net/forum?id=U23A2BUKYt&noteId=DouxKBeSOa) · [Full original Chinese analysis](casebook.zh-CN.md#c17). Detailed source IDs, conditions, archive and historic rating statements are in [cases.json](cases.json).

---

### C18 — Softmax Transformers are Turing-Complete (2026)

**Selection:** `core_positive`. **Outcome:** Accept (Oral). **Mechanisms:** `theory_repair`, `novelty`, `related_work`, `paper_revision`.

**Concern:** Turing completeness theorem assumptions, previous work and trainability

**Author action and observed response:** Clarified the formal theorem and its interpretation; reviewers reported 2→6 and 4→6

**Why teach / qualify this case:** Primary accepted example with a reviewer’s first-person numeric raise or unconditional numeric intention and a traceable action–feedback chain. Clarified the formal theorem and its interpretation; reviewers reported 2→6 and 4→6

**Do not overgeneralize:** Expressive power is not an empirical training or practical deployment guarantee The ICLR 2026 rating rollback also applies.

**Sources:** [OpenReview discussion](https://openreview.net/forum?id=FdkPOHlChS) · [Key evidence note](https://openreview.net/forum?id=FdkPOHlChS&noteId=l4fwsSOLl8) · [AC](https://openreview.net/forum?id=FdkPOHlChS&noteId=fnV5UVObiS) · [Full original Chinese analysis](casebook.zh-CN.md#c18). Detailed source IDs, conditions, archive and historic rating statements are in [cases.json](cases.json).

---

### C19 — InnovatorBench (2026)

**Selection:** `core_positive`. **Outcome:** Accept (Poster). **Mechanisms:** `benchmark_value`, `claim_scope`, `negative_results`, `multi_round`.

**Concern:** Overbroad AI-research benchmark scope and scarce negative outcomes

**Author action and observed response:** Narrowed to LLM research and reported zero-score failures; reviewer moved 2→6

**Why teach / qualify this case:** Primary accepted example with a reviewer’s first-person numeric raise or unconditional numeric intention and a traceable action–feedback chain. Narrowed to LLM research and reported zero-score failures; reviewer moved 2→6

**Do not overgeneralize:** Small task count and resource dependence still limit generalization The ICLR 2026 rating rollback also applies.

**Sources:** [OpenReview discussion](https://openreview.net/forum?id=w8rZ2Jd6Jo) · [Key evidence note](https://openreview.net/forum?id=w8rZ2Jd6Jo&noteId=MlSsFU2LBn) · [AC](https://openreview.net/forum?id=w8rZ2Jd6Jo&noteId=QYCtLP30Ih) · [Full original Chinese analysis](casebook.zh-CN.md#c19). Detailed source IDs, conditions, archive and historic rating statements are in [cases.json](cases.json).

---

### C20 — Semantic Voting (2026)

**Selection:** `extended_positive`. **Outcome:** Accept (Poster). **Mechanisms:** `evaluation`, `claim_scope`, `negative_results`.

**Concern:** Applicability of semantic voting and reward variability

**Author action and observed response:** Measured voting behavior and reward variance, with a first-person 2→6 statement

**Why teach / qualify this case:** Supplementary accepted example, specialized or overlapping with a core teaching mechanism. Measured voting behavior and reward variance, with a first-person 2→6 statement

**Do not overgeneralize:** Coverage largely duplicates scope and evaluation cases in the core set The ICLR 2026 rating rollback also applies.

**Sources:** [OpenReview discussion](https://openreview.net/forum?id=7AlPbFkcs3) · [Key evidence note](https://openreview.net/forum?id=7AlPbFkcs3&noteId=hFwrhPH9Ks) · [AC](https://openreview.net/forum?id=7AlPbFkcs3&noteId=Nw43dPS1GF) · [Full original Chinese analysis](casebook.zh-CN.md#c20). Detailed source IDs, conditions, archive and historic rating statements are in [cases.json](cases.json).

---

### C21 — PEERING INTO THE UNKNOWN (2026)

**Selection:** `extended_positive`. **Outcome:** Accept (Poster). **Mechanisms:** `baseline_fairness`, `efficiency`, `evaluation`, `claim_scope`.

**Concern:** Visual-system baseline strength and backend substitution

**Author action and observed response:** Tested strong replacement backends and cost, with an expressed 4→8 willingness

**Why teach / qualify this case:** Supplementary accepted example, specialized or overlapping with a core teaching mechanism. Tested strong replacement backends and cost, with an expressed 4→8 willingness

**Do not overgeneralize:** Some later scores were conveyed by the AC; avoid collapsing separate source types The ICLR 2026 rating rollback also applies.

**Sources:** [OpenReview discussion](https://openreview.net/forum?id=e7gbgdw05A) · [Key evidence note](https://openreview.net/forum?id=e7gbgdw05A&noteId=7xyZuVNFUM) · [AC](https://openreview.net/forum?id=e7gbgdw05A&noteId=PzfV8PkQLb) · [Full original Chinese analysis](casebook.zh-CN.md#c21). Detailed source IDs, conditions, archive and historic rating statements are in [cases.json](cases.json).

---

### C22 — Triangle Multiplication (2026)

**Selection:** `extended_positive`. **Outcome:** Accept (Poster). **Mechanisms:** `novelty`, `evaluation`, `claim_scope`.

**Concern:** Triangle multiplication's value beyond simplified engineering

**Author action and observed response:** Clarified structural mechanism and comparison; reviewers promised or reported 4→6

**Why teach / qualify this case:** Supplementary accepted example, specialized or overlapping with a core teaching mechanism. Clarified structural mechanism and comparison; reviewers promised or reported 4→6

**Do not overgeneralize:** One low reviewer stayed on the reject side; one score commitment could not be saved The ICLR 2026 rating rollback also applies.

**Sources:** [OpenReview discussion](https://openreview.net/forum?id=CrXcfMLR9q) · [Key evidence note](https://openreview.net/forum?id=CrXcfMLR9q&noteId=Kq0Zg9XRM1) · [AC](https://openreview.net/forum?id=CrXcfMLR9q&noteId=Vtu5YntMdN) · [Full original Chinese analysis](casebook.zh-CN.md#c22). Detailed source IDs, conditions, archive and historic rating statements are in [cases.json](cases.json).

---

### C23 — Taming Score-Based Denoisers (2026)

**Selection:** `core_positive`. **Outcome:** Accept (Poster). **Mechanisms:** `theory_repair`, `claim_scope`, `related_work`, `paper_revision`.

**Concern:** Guarantees under unrealistic stationarity assumptions

**Author action and observed response:** Reworked the analysis toward a finite-step implementable denoiser; two reviewers moved 4→6

**Why teach / qualify this case:** Primary accepted example with a reviewer’s first-person numeric raise or unconditional numeric intention and a traceable action–feedback chain. Reworked the analysis toward a finite-step implementable denoiser; two reviewers moved 4→6

**Do not overgeneralize:** Claim only the finite-step guarantees actually proven The ICLR 2026 rating rollback also applies.

**Sources:** [OpenReview discussion](https://openreview.net/forum?id=BiXwSIIMIq) · [Key evidence note](https://openreview.net/forum?id=BiXwSIIMIq&noteId=ajh21lnVqs) · [AC](https://openreview.net/forum?id=BiXwSIIMIq&noteId=xC9JQrcLQs) · [Full original Chinese analysis](casebook.zh-CN.md#c23). Detailed source IDs, conditions, archive and historic rating statements are in [cases.json](cases.json).

---

### C24 — MOSAIC (2026)

**Selection:** `extended_positive`. **Outcome:** Accept (Poster). **Mechanisms:** `evaluation`, `benchmark_value`, `paper_revision`.

**Concern:** A visual-generation method's components and distribution shifts

**Author action and observed response:** Added 2×2 ablations, external-distribution and diversity checks; reviewer promised 4→6

**Why teach / qualify this case:** Supplementary accepted example, specialized or overlapping with a core teaching mechanism. Added 2×2 ablations, external-distribution and diversity checks; reviewer promised 4→6

**Do not overgeneralize:** Score entry was unavailable and an additional change came from AC recollection The ICLR 2026 rating rollback also applies.

**Sources:** [OpenReview discussion](https://openreview.net/forum?id=7AH0y1OtnC) · [Key evidence note](https://openreview.net/forum?id=7AH0y1OtnC&noteId=DQlg1bQkHU) · [AC](https://openreview.net/forum?id=7AH0y1OtnC&noteId=V7Za3FCgfG) · [Full original Chinese analysis](casebook.zh-CN.md#c24). Detailed source IDs, conditions, archive and historic rating statements are in [cases.json](cases.json).

---

### C25 — FACT (2026)

**Selection:** `core_positive`. **Outcome:** Accept (Poster). **Mechanisms:** `evaluation`, `claim_scope`, `baseline_fairness`.

**Concern:** Averages, arbitrary variable order and hyperparameter robustness

**Author action and observed response:** Tested the specific alternative explanations; reviewer explicitly moved 4→6

**Why teach / qualify this case:** Primary accepted example with a reviewer’s first-person numeric raise or unconditional numeric intention and a traceable action–feedback chain. Tested the specific alternative explanations; reviewer explicitly moved 4→6

**Do not overgeneralize:** Only state robustness for tested orders and settings The ICLR 2026 rating rollback also applies.

**Sources:** [OpenReview discussion](https://openreview.net/forum?id=j3gNYqrHtl) · [Key evidence note](https://openreview.net/forum?id=j3gNYqrHtl&noteId=5wbsraNdEs) · [AC](https://openreview.net/forum?id=j3gNYqrHtl&noteId=lpaA7XFMKH) · [Full original Chinese analysis](casebook.zh-CN.md#c25). Detailed source IDs, conditions, archive and historic rating statements are in [cases.json](cases.json).

---

### C26 — Atomic HINs (2026)

**Selection:** `core_positive`. **Outcome:** Accept (Poster). **Mechanisms:** `efficiency`, `evaluation`, `paper_revision`.

**Concern:** Actual implementation costs and backend portability

**Author action and observed response:** Reported seconds, amortization and cross-backend tests; reviewer explicitly moved 4→6

**Why teach / qualify this case:** Primary accepted example with a reviewer’s first-person numeric raise or unconditional numeric intention and a traceable action–feedback chain. Reported seconds, amortization and cross-backend tests; reviewer explicitly moved 4→6

**Do not overgeneralize:** Do not extend measured hardware performance to untested backends The ICLR 2026 rating rollback also applies.

**Sources:** [OpenReview discussion](https://openreview.net/forum?id=AG7fjg5azU) · [Key evidence note](https://openreview.net/forum?id=AG7fjg5azU&noteId=BDmE1pBu9v) · [AC](https://openreview.net/forum?id=AG7fjg5azU&noteId=Hd6T0WBXHk) · [Full original Chinese analysis](casebook.zh-CN.md#c26). Detailed source IDs, conditions, archive and historic rating statements are in [cases.json](cases.json).

---

### C27 — Quantum Attention Approximation (2026)

**Selection:** `qualified_positive`. **Outcome:** Accept (Poster). **Mechanisms:** `theory_repair`, `multi_round`, `paper_revision`.

**Concern:** Finite-precision quantum attention analysis and proof correctness

**Author action and observed response:** Multiple rounds repaired precision, complexity and classical subroutine assumptions; reviewer moved 4→8

**Why teach / qualify this case:** Positive or improved outcome requiring attribution, condition, timing, rhetoric, or reviewer-stance qualifications. Multiple rounds repaired precision, complexity and classical subroutine assumptions; reviewer moved 4→8

**Do not overgeneralize:** Reviewer criticized maturity of the original submission and the revision scale; learn proof repair, not deferral The ICLR 2026 rating rollback also applies.

**Sources:** [OpenReview discussion](https://openreview.net/forum?id=0zIcPe4CtY) · [Key evidence note](https://openreview.net/forum?id=0zIcPe4CtY&noteId=RhSckfziEE) · [AC](https://openreview.net/forum?id=0zIcPe4CtY&noteId=RliDJMYTCl) · [Full original Chinese analysis](casebook.zh-CN.md#c27). Detailed source IDs, conditions, archive and historic rating statements are in [cases.json](cases.json).

---

### C28 — LCA (2026)

**Selection:** `core_positive`. **Outcome:** Accept (Poster). **Mechanisms:** `novelty`, `related_work`, `multi_round`, `claim_scope`.

**Concern:** Novelty of a merged auxiliary component

**Author action and observed response:** Authors acknowledged the inherited component and recentered the contribution; reviewer moved 4→6

**Why teach / qualify this case:** Primary accepted example with a reviewer’s first-person numeric raise or unconditional numeric intention and a traceable action–feedback chain. Authors acknowledged the inherited component and recentered the contribution; reviewer moved 4→6

**Do not overgeneralize:** Do not portray prior work adaptations as newly invented primitives The ICLR 2026 rating rollback also applies.

**Sources:** [OpenReview discussion](https://openreview.net/forum?id=3uINmRldVW) · [Key evidence note](https://openreview.net/forum?id=3uINmRldVW&noteId=yxNHvwiq0P) · [AC](https://openreview.net/forum?id=3uINmRldVW&noteId=Wx2XB6mda3) · [Full original Chinese analysis](casebook.zh-CN.md#c28). Detailed source IDs, conditions, archive and historic rating statements are in [cases.json](cases.json).

---

### C29 — Learning to Segment for VRP (2026)

**Selection:** `extended_positive`. **Outcome:** Accept (Oral). **Mechanisms:** `novelty`, `baseline_fairness`, `evaluation`, `claim_scope`.

**Concern:** Novelty and validation of segmentation for routing

**Author action and observed response:** Tested addition to near-neighbor methods and examined label reliability; reviewer expressed 4→6

**Why teach / qualify this case:** Supplementary accepted example, specialized or overlapping with a core teaching mechanism. Tested addition to near-neighbor methods and examined label reliability; reviewer expressed 4→6

**Do not overgeneralize:** Some numbers are AC-reported; keep each path's attribution distinct The ICLR 2026 rating rollback also applies.

**Sources:** [OpenReview discussion](https://openreview.net/forum?id=pN261iTKvr) · [Key evidence note](https://openreview.net/forum?id=pN261iTKvr&noteId=g7ihOdcQhb) · [AC](https://openreview.net/forum?id=pN261iTKvr&noteId=We9Xo1pOmG) · [Full original Chinese analysis](casebook.zh-CN.md#c29). Detailed source IDs, conditions, archive and historic rating statements are in [cases.json](cases.json).

---

### C30 — LoRA meets Riemannion (2026)

**Selection:** `extended_positive`. **Outcome:** Accept (Poster). **Mechanisms:** `theory_repair`, `evaluation`, `claim_scope`.

**Concern:** Invariants and minimal tests for a Riemannian low-rank approach

**Author action and observed response:** Provided a short invariant argument and classical diagnostic; reviewer moved 4→6

**Why teach / qualify this case:** Supplementary accepted example, specialized or overlapping with a core teaching mechanism. Provided a short invariant argument and classical diagnostic; reviewer moved 4→6

**Do not overgeneralize:** Another reviewer remained at 2; do not infer consensus The ICLR 2026 rating rollback also applies.

**Sources:** [OpenReview discussion](https://openreview.net/forum?id=WtbXgc9GVA) · [Key evidence note](https://openreview.net/forum?id=WtbXgc9GVA&noteId=38JqV9KeMs) · [AC](https://openreview.net/forum?id=WtbXgc9GVA&noteId=MYwtGXXWTV) · [Full original Chinese analysis](casebook.zh-CN.md#c30). Detailed source IDs, conditions, archive and historic rating statements are in [cases.json](cases.json).

---

### C31 — Decoupling Dynamical Richness (2026)

**Selection:** `qualified_positive`. **Outcome:** Accept (Poster). **Mechanisms:** `claim_scope`, `theory_repair`, `evaluation`, `ac_summary`.

**Concern:** Scope and interpretation of dynamical richness theory

**Author action and observed response:** Clarified limited theoretical scope and evaluation; reviewer planned 4→6

**Why teach / qualify this case:** Positive or improved outcome requiring attribution, condition, timing, rhetoric, or reviewer-stance qualifications. Clarified limited theoretical scope and evaluation; reviewer planned 4→6

**Do not overgeneralize:** Planned increase is not a saved rating and remaining doubts persisted The ICLR 2026 rating rollback also applies.

**Sources:** [OpenReview discussion](https://openreview.net/forum?id=7Mbz5uSf2J) · [Key evidence note](https://openreview.net/forum?id=7Mbz5uSf2J&noteId=K8v4Gl0HSE) · [AC](https://openreview.net/forum?id=7Mbz5uSf2J&noteId=vFWD2lzWiZ) · [Full original Chinese analysis](casebook.zh-CN.md#c31). Detailed source IDs, conditions, archive and historic rating statements are in [cases.json](cases.json).

---

### C32 — Procedural Mistake Detection (2026)

**Selection:** `core_positive`. **Outcome:** Accept (Poster). **Mechanisms:** `evaluation`, `baseline_fairness`, `efficiency`.

**Concern:** Test threshold selection and stronger substitute methods

**Author action and observed response:** Clarified selection protocol and ran stronger comparisons; lowest reviewer moved 2→6

**Why teach / qualify this case:** Primary accepted example with a reviewer’s first-person numeric raise or unconditional numeric intention and a traceable action–feedback chain. Clarified selection protocol and ran stronger comparisons; lowest reviewer moved 2→6

**Do not overgeneralize:** Never gloss over test-set leakage if the actual protocol is invalid The ICLR 2026 rating rollback also applies.

**Sources:** [OpenReview discussion](https://openreview.net/forum?id=HsB5EuQOoS) · [Key evidence note](https://openreview.net/forum?id=HsB5EuQOoS&noteId=cWsuDKSibZ) · [AC](https://openreview.net/forum?id=HsB5EuQOoS&noteId=e84MJbo1sO) · [Full original Chinese analysis](casebook.zh-CN.md#c32). Detailed source IDs, conditions, archive and historic rating statements are in [cases.json](cases.json).

---

### C33 — Metric Tensors on Neuromanifolds (2026)

**Selection:** `core_positive`. **Outcome:** Accept (Poster). **Mechanisms:** `evaluation`, `theory_repair`, `efficiency`, `ac_summary`.

**Concern:** Calibration of a geometric metric estimator

**Author action and observed response:** Compared estimates against computable reference truth; reviewer explicitly moved 4→6

**Why teach / qualify this case:** Primary accepted example with a reviewer’s first-person numeric raise or unconditional numeric intention and a traceable action–feedback chain. Compared estimates against computable reference truth; reviewer explicitly moved 4→6

**Do not overgeneralize:** AC static list disagreed with a later first-person statement; retain provenance The ICLR 2026 rating rollback also applies.

**Sources:** [OpenReview discussion](https://openreview.net/forum?id=Ssevs8KCsU) · [Key evidence note](https://openreview.net/forum?id=Ssevs8KCsU&noteId=6u69DwVi5N) · [AC](https://openreview.net/forum?id=Ssevs8KCsU&noteId=spZIwf40xJ) · [Full original Chinese analysis](casebook.zh-CN.md#c33). Detailed source IDs, conditions, archive and historic rating statements are in [cases.json](cases.json).

---

### C34 — Guarantees for Dataset Distillation (2026)

**Selection:** `qualified_positive`. **Outcome:** Accept (Poster). **Mechanisms:** `theory_repair`, `claim_scope`, `multi_round`, `paper_revision`.

**Concern:** Quantifiers and scope of a dataset-distillation guarantee

**Author action and observed response:** Clarified conditional existence and promised stronger scope discussion

**Why teach / qualify this case:** Positive or improved outcome requiring attribution, condition, timing, rhetoric, or reviewer-stance qualifications. Clarified conditional existence and promised stronger scope discussion

**Do not overgeneralize:** A 4→6 raise was conditional on manuscript changes The ICLR 2026 rating rollback also applies.

**Sources:** [OpenReview discussion](https://openreview.net/forum?id=zueIXg5FP5) · [Key evidence note](https://openreview.net/forum?id=zueIXg5FP5&noteId=63ukDRmpgI) · [AC](https://openreview.net/forum?id=zueIXg5FP5&noteId=uaxDBUMbDj) · [Full original Chinese analysis](casebook.zh-CN.md#c34). Detailed source IDs, conditions, archive and historic rating statements are in [cases.json](cases.json).

---

### C35 — Dense Associative Memory Dynamics (2026)

**Selection:** `qualified_positive`. **Outcome:** Accept (Poster). **Mechanisms:** `claim_scope`, `theory_repair`, `evaluation`.

**Concern:** The interpretation and practicality of associative-memory dynamics

**Author action and observed response:** Clarified theoretical object and provided additional diagnostics; reviewer was happy to move 2→6

**Why teach / qualify this case:** Positive or improved outcome requiring attribution, condition, timing, rhetoric, or reviewer-stance qualifications. Clarified theoretical object and provided additional diagnostics; reviewer was happy to move 2→6

**Do not overgeneralize:** Keep the reviewer’s intention separate from an updated interface and pending experiments The ICLR 2026 rating rollback also applies.

**Sources:** [OpenReview discussion](https://openreview.net/forum?id=TeDkzf34hs) · [Key evidence note](https://openreview.net/forum?id=TeDkzf34hs&noteId=TfiPxMzAaS) · [AC](https://openreview.net/forum?id=TeDkzf34hs&noteId=LmhaGMY2Br) · [Full original Chinese analysis](casebook.zh-CN.md#c35). Detailed source IDs, conditions, archive and historic rating statements are in [cases.json](cases.json).

---

### C36 — WILD-Diffusion (2026)

**Selection:** `extended_positive`. **Outcome:** Accept (Poster). **Mechanisms:** `efficiency`, `baseline_fairness`, `evaluation`, `related_work`.

**Concern:** Diffusion efficiency and competitive versus complementary baselines

**Author action and observed response:** Reported absolute resource costs and clarified which systems should be compared; 4→6

**Why teach / qualify this case:** Supplementary accepted example, specialized or overlapping with a core teaching mechanism. Reported absolute resource costs and clarified which systems should be compared; 4→6

**Do not overgeneralize:** Specialized diffusion example supplements, not supersedes, general fairness cases The ICLR 2026 rating rollback also applies.

**Sources:** [OpenReview discussion](https://openreview.net/forum?id=OrCVuQAYzF) · [Key evidence note](https://openreview.net/forum?id=OrCVuQAYzF&noteId=VkNBEwFWsD) · [AC](https://openreview.net/forum?id=OrCVuQAYzF&noteId=DHEM73J2sX) · [Full original Chinese analysis](casebook.zh-CN.md#c36). Detailed source IDs, conditions, archive and historic rating statements are in [cases.json](cases.json).

---

### C37 — DeMo (2026)

**Selection:** `qualified_positive`. **Outcome:** Accept (Poster). **Mechanisms:** `baseline_fairness`, `efficiency`, `negative_results`, `claim_scope`, `ac_summary`.

**Concern:** Hyperparameter parity and communication–performance trade-off

**Author action and observed response:** Disclosed undertuning and ran a fully tuned comparison; AC assessed the evidence positively

**Why teach / qualify this case:** Positive or improved outcome requiring attribution, condition, timing, rhetoric, or reviewer-stance qualifications. Disclosed undertuning and ran a fully tuned comparison; AC assessed the evidence positively

**Do not overgeneralize:** A 4→6 was conditional; AC prediction of four 6s is not four saved raises The ICLR 2026 rating rollback also applies.

**Sources:** [OpenReview discussion](https://openreview.net/forum?id=U9oewpa7cn) · [Key evidence note](https://openreview.net/forum?id=U9oewpa7cn&noteId=MbpXnuAD0V) · [AC](https://openreview.net/forum?id=U9oewpa7cn&noteId=FbtyEw7X0b) · [Full original Chinese analysis](casebook.zh-CN.md#c37). Detailed source IDs, conditions, archive and historic rating statements are in [cases.json](cases.json).

---

### C38 — Accelerated Parallel Tempering (2026)

**Selection:** `qualified_positive`. **Outcome:** Accept (Poster). **Mechanisms:** `efficiency`, `baseline_fairness`, `multi_round`, `ac_summary`.

**Concern:** Parallel tempering cost and fair competing implementations

**Author action and observed response:** Improved experimental cost evidence and reasoning in several rounds; reviewer moved 2→4→6

**Why teach / qualify this case:** Positive or improved outcome requiring attribution, condition, timing, rhetoric, or reviewer-stance qualifications. Improved experimental cost evidence and reasoning in several rounds; reviewer moved 2→4→6

**Do not overgeneralize:** Reviewer-to-reviewer exchange also influenced the assessment; rebuttal alone cannot be credited The ICLR 2026 rating rollback also applies.

**Sources:** [OpenReview discussion](https://openreview.net/forum?id=CODnlyYUli) · [Key evidence note](https://openreview.net/forum?id=CODnlyYUli&noteId=vKLQpAKi1u) · [AC](https://openreview.net/forum?id=CODnlyYUli&noteId=8RxW2Gc3qv) · [Full original Chinese analysis](casebook.zh-CN.md#c38). Detailed source IDs, conditions, archive and historic rating statements are in [cases.json](cases.json).

---

### C39 — Bilevel Uniform Convexity (2026)

**Selection:** `extended_positive`. **Outcome:** Accept (Poster). **Mechanisms:** `theory_repair`, `paper_revision`, `claim_scope`.

**Concern:** Formal definitions, random sources and dependency structure

**Author action and observed response:** Repaired definitions and algorithmic explanation; reviewer stated intention to move 4→6

**Why teach / qualify this case:** Supplementary accepted example, specialized or overlapping with a core teaching mechanism. Repaired definitions and algorithmic explanation; reviewer stated intention to move 4→6

**Do not overgeneralize:** Future-tense score is not verified saved state; another reviewer might remain unchanged The ICLR 2026 rating rollback also applies.

**Sources:** [OpenReview discussion](https://openreview.net/forum?id=dJgb3ngAvT) · [Key evidence note](https://openreview.net/forum?id=dJgb3ngAvT&noteId=eBlwdlPOIM) · [AC](https://openreview.net/forum?id=dJgb3ngAvT&noteId=zJqqhMuGOM) · [Full original Chinese analysis](casebook.zh-CN.md#c39). Detailed source IDs, conditions, archive and historic rating statements are in [cases.json](cases.json).

---

### C40 — Self-Representation Alignment (2026)

**Selection:** `extended_positive`. **Outcome:** Accept (Poster). **Mechanisms:** `evaluation`, `claim_scope`, `negative_results`.

**Concern:** Whether representation changes follow the proposed mechanism

**Author action and observed response:** Added longitudinal probes and hyperparameter transfer checks; reviewer moved 4→6

**Why teach / qualify this case:** Supplementary accepted example, specialized or overlapping with a core teaching mechanism. Added longitudinal probes and hyperparameter transfer checks; reviewer moved 4→6

**Do not overgeneralize:** The evidence supports tested representation probes, not every causal account The ICLR 2026 rating rollback also applies.

**Sources:** [OpenReview discussion](https://openreview.net/forum?id=ds5w2xth93) · [Key evidence note](https://openreview.net/forum?id=ds5w2xth93&noteId=uKHH48tjer) · [AC](https://openreview.net/forum?id=ds5w2xth93&noteId=K423bvgybp) · [Full original Chinese analysis](casebook.zh-CN.md#c40). Detailed source IDs, conditions, archive and historic rating statements are in [cases.json](cases.json).

---

### C41 — Reassessing Layer Pruning (2026)

**Selection:** `qualified_positive`. **Outcome:** Accept (Poster). **Mechanisms:** `evaluation`, `baseline_fairness`, `paper_revision`, `ac_summary`.

**Concern:** Fair model-pruning evaluation and exact rating provenance

**Author action and observed response:** Aligned experimental conditions and reported reviewer responses

**Why teach / qualify this case:** Positive or improved outcome requiring attribution, condition, timing, rhetoric, or reviewer-stance qualifications. Aligned experimental conditions and reported reviewer responses

**Do not overgeneralize:** One 4→6 target was AC-sourced, a 2→4 path stayed negative; do not misattribute The ICLR 2026 rating rollback also applies.

**Sources:** [OpenReview discussion](https://openreview.net/forum?id=04Tfwy3LLC) · [Key evidence note](https://openreview.net/forum?id=04Tfwy3LLC&noteId=zjicUikvES) · [AC](https://openreview.net/forum?id=04Tfwy3LLC&noteId=icHquSOLSK) · [Full original Chinese analysis](casebook.zh-CN.md#c41). Detailed source IDs, conditions, archive and historic rating statements are in [cases.json](cases.json).

---

### C42 — SuperMAN / GMAN (2026)

**Selection:** `qualified_positive`. **Outcome:** Accept (Poster). **Mechanisms:** `evaluation`, `efficiency`, `paper_revision`, `ac_summary`.

**Concern:** Reliability, calibration and runtime of a generalized model

**Author action and observed response:** Added evidence and elicited a supportive reviewer’s increased assessment

**Why teach / qualify this case:** Positive or improved outcome requiring attribution, condition, timing, rhetoric, or reviewer-stance qualifications. Added evidence and elicited a supportive reviewer’s increased assessment

**Do not overgeneralize:** No exact total new numeric score and the sole initially negative reviewer did not follow up The ICLR 2026 rating rollback also applies.

**Sources:** [OpenReview discussion](https://openreview.net/forum?id=1MVeSLvfxU) · [Key evidence note](https://openreview.net/forum?id=1MVeSLvfxU&noteId=nbE4MoSOmL) · [AC](https://openreview.net/forum?id=1MVeSLvfxU&noteId=TtRRHoCMtX) · [Full original Chinese analysis](casebook.zh-CN.md#c42). Detailed source IDs, conditions, archive and historic rating statements are in [cases.json](cases.json).

---

### C43 — MonoSoup (2026)

**Selection:** `outcome_counterexample`. **Outcome:** Reject. **Mechanisms:** `theory_repair`, `evaluation`, `ac_summary`.

**Concern:** Theory supporting model-soup weights and size of benefit

**Author action and observed response:** Authors provided responses and several score increases were recorded by AC

**Why teach / qualify this case:** Score movement or partial resolution that did not yield acceptance or close the critical condition. Authors provided responses and several score increases were recorded by AC

**Do not overgeneralize:** Ultimately rejected; unresolved theoretical support and small benefit remained decisive The ICLR 2026 rating rollback also applies.

**Sources:** [OpenReview discussion](https://openreview.net/forum?id=ICANwnoGgN) · [Key evidence note](https://openreview.net/forum?id=ICANwnoGgN&noteId=Ax5fH58HGb) · [Full original Chinese analysis](casebook.zh-CN.md#c43). Detailed source IDs, conditions, archive and historic rating statements are in [cases.json](cases.json).

---

### C44 — FuseGPT (2026)

**Selection:** `outcome_counterexample`. **Outcome:** Reject. **Mechanisms:** `baseline_fairness`, `evaluation`, `ac_summary`.

**Concern:** Fusion baseline and reported improvement strength

**Author action and observed response:** Responses led to reported 2→4 movement

**Why teach / qualify this case:** Score movement or partial resolution that did not yield acceptance or close the critical condition. Responses led to reported 2→4 movement

**Do not overgeneralize:** Still on the reject side and ultimately rejected; movement is not reversal The ICLR 2026 rating rollback also applies.

**Sources:** [OpenReview discussion](https://openreview.net/forum?id=tNnXu5bKoo) · [Key evidence note](https://openreview.net/forum?id=tNnXu5bKoo&noteId=UtzoOFDGyl) · [Full original Chinese analysis](casebook.zh-CN.md#c44). Detailed source IDs, conditions, archive and historic rating statements are in [cases.json](cases.json).

---

### C45 — Censoring with Plausible Deniability (2026)

**Selection:** `outcome_counterexample`. **Outcome:** Reject. **Mechanisms:** `theory_repair`, `claim_scope`, `paper_revision`, `ac_summary`.

**Concern:** Privacy guarantee and plausible deniability scope

**Author action and observed response:** Authors addressed some concerns and reviewer moved 2→4

**Why teach / qualify this case:** Score movement or partial resolution that did not yield acceptance or close the critical condition. Authors addressed some concerns and reviewer moved 2→4

**Do not overgeneralize:** Further 4→6 willingness depended on unclosed manuscript clarification; rejected The ICLR 2026 rating rollback also applies.

**Sources:** [OpenReview discussion](https://openreview.net/forum?id=vSXIEbTVhE) · [Key evidence note](https://openreview.net/forum?id=vSXIEbTVhE&noteId=pyIl197Hos) · [Full original Chinese analysis](casebook.zh-CN.md#c45). Detailed source IDs, conditions, archive and historic rating statements are in [cases.json](cases.json).

---

### C46 — ASMG (2026)

**Selection:** `outcome_counterexample`. **Outcome:** Reject. **Mechanisms:** `efficiency`, `evaluation`, `ac_summary`.

**Concern:** Engineering complexity versus achieved gains

**Author action and observed response:** Authors answered cost and experiment questions; two reviewers moved 4→6

**Why teach / qualify this case:** Score movement or partial resolution that did not yield acceptance or close the critical condition. Authors answered cost and experiment questions; two reviewers moved 4→6

**Do not overgeneralize:** Ultimately rejected: AC found complexity, effect and coverage insufficient The ICLR 2026 rating rollback also applies.

**Sources:** [OpenReview discussion](https://openreview.net/forum?id=xsqiDQjSvV) · [Key evidence note](https://openreview.net/forum?id=xsqiDQjSvV&noteId=dPi75ZnQsI) · [Full original Chinese analysis](casebook.zh-CN.md#c46). Detailed source IDs, conditions, archive and historic rating statements are in [cases.json](cases.json).

---

### C47 — InfoNCE Induces Gaussian Distribution (2026)

**Selection:** `context_only`. **Outcome:** Accept (Oral). **Mechanisms:** `novelty`, `theory_repair`, `evaluation`, `ac_summary`.

**Concern:** Contrastive objective and Gaussian-distribution claims

**Author action and observed response:** Authors revised theory positioning and added controlled SimCLR experiments; AC supported the paper

**Why teach / qualify this case:** Decision or discussion context with no confirmed negative-to-positive numeric reviewer path. Authors revised theory positioning and added controlled SimCLR experiments; AC supported the paper

**Do not overgeneralize:** Initial 8/4/2/2 and final Oral are not a verified per-reviewer score reversal vector The ICLR 2026 rating rollback also applies.

**Sources:** [OpenReview discussion](https://openreview.net/forum?id=BlSH7gNQSq) · [Key evidence note](https://openreview.net/forum?id=BlSH7gNQSq&noteId=Bzx9XPwY2V) · [Full original Chinese analysis](casebook.zh-CN.md#c47). Detailed source IDs, conditions, archive and historic rating statements are in [cases.json](cases.json).

---

### C48 — GAGA (2026)

**Selection:** `qualified_positive`. **Outcome:** Accept (Poster). **Mechanisms:** `evaluation`, `theory_repair`, `ac_summary`.

**Concern:** Evidence for the GAGA formulation and theoretical framing

**Author action and observed response:** One reviewer expressed a 2→6 intention after revisions

**Why teach / qualify this case:** Positive or improved outcome requiring attribution, condition, timing, rhetoric, or reviewer-stance qualifications. One reviewer expressed a 2→6 intention after revisions

**Do not overgeneralize:** Another reviewer disputed the AC's expectation of broader agreement The ICLR 2026 rating rollback also applies.

**Sources:** [OpenReview discussion](https://openreview.net/forum?id=Q9gz8lVyAi) · [Key evidence note](https://openreview.net/forum?id=Q9gz8lVyAi&noteId=NN9VIC3nKz) · [Full original Chinese analysis](casebook.zh-CN.md#c48). Detailed source IDs, conditions, archive and historic rating statements are in [cases.json](cases.json).

---

### C49 — PLAGUE (2026)

**Selection:** `context_only`. **Outcome:** Accept (Poster). **Mechanisms:** `baseline_fairness`, `novelty`, `evaluation`, `ac_summary`.

**Concern:** Engineering contribution despite multiple low initial scores

**Author action and observed response:** AC independently evaluated manuscript and author explanations; final Poster

**Why teach / qualify this case:** Decision or discussion context with no confirmed negative-to-positive numeric reviewer path. AC independently evaluated manuscript and author explanations; final Poster

**Do not overgeneralize:** No first-person numeric reversals for those initial negatives were established The ICLR 2026 rating rollback also applies.

**Sources:** [OpenReview discussion](https://openreview.net/forum?id=05hNleYOcG) · [Key evidence note](https://openreview.net/forum?id=05hNleYOcG&noteId=KuzTZta1WZ) · [Full original Chinese analysis](casebook.zh-CN.md#c49). Detailed source IDs, conditions, archive and historic rating statements are in [cases.json](cases.json).

---

### C50 — Dynamic Neural Fortresses (2025)

**Selection:** `evidence_exclusion`. **Outcome:** Accept (Poster). **Mechanisms:** `ac_summary`, `evaluation`.

**Concern:** Abrupt anomalous score change in a model-extraction defense

**Author action and observed response:** Other reviews and rebuttal supported acceptance, but a 1→8 jump lacked explanatory dialogue

**Why teach / qualify this case:** Anomalous or conflicting numeric evidence excluded as clean reversal proof while preserved for audit. Other reviews and rebuttal supported acceptance, but a 1→8 jump lacked explanatory dialogue

**Do not overgeneralize:** AC explicitly excluded that review as an outlier; never use it as successful-rebuttal proof 

**Sources:** [OpenReview discussion](https://openreview.net/forum?id=029hDSVoXK) · [Key evidence note](https://openreview.net/forum?id=029hDSVoXK&noteId=dHvqGcF4MN) · [Full original Chinese analysis](casebook.zh-CN.md#c50). Detailed source IDs, conditions, archive and historic rating statements are in [cases.json](cases.json).

---

### C51 — BiGR (2025)

**Selection:** `extended_positive`. **Outcome:** Accept (Poster). **Mechanisms:** `claim_scope`, `evaluation`, `baseline_fairness`, `efficiency`.

**Concern:** Generalization of bidirectional generative representation claims

**Author action and observed response:** Expanded text-to-image evidence and corrected interpretive ambiguity; reviewer moved 3→6

**Why teach / qualify this case:** Supplementary accepted example, specialized or overlapping with a core teaching mechanism. Expanded text-to-image evidence and corrected interpretive ambiguity; reviewer moved 3→6

**Do not overgeneralize:** Additional application-specific scope example, not a unique default mechanism 

**Sources:** [OpenReview discussion](https://openreview.net/forum?id=1Z6PSw7OL8) · [Key evidence note](https://openreview.net/forum?id=1Z6PSw7OL8&noteId=QuDXHs2Qhy) · [Full original Chinese analysis](casebook.zh-CN.md#c51). Detailed source IDs, conditions, archive and historic rating statements are in [cases.json](cases.json).

---

### C52 — GenSE (2025)

**Selection:** `core_positive`. **Outcome:** Accept (Poster). **Mechanisms:** `related_work`, `novelty`, `paper_revision`, `multi_round`.

**Concern:** Uncited related work and novelty of generative speech enhancement

**Author action and observed response:** Acknowledged missing citation and compared mechanisms and tasks; reviewer moved 3→6

**Why teach / qualify this case:** Primary accepted example with a reviewer’s first-person numeric raise or unconditional numeric intention and a traceable action–feedback chain. Acknowledged missing citation and compared mechanisms and tasks; reviewer moved 3→6

**Do not overgeneralize:** Adding a citation alone does not resolve a novelty critique 

**Sources:** [OpenReview discussion](https://openreview.net/forum?id=1p6xFLBU4J) · [Key evidence note](https://openreview.net/forum?id=1p6xFLBU4J&noteId=PdY7uWdRdJ) · [Full original Chinese analysis](casebook.zh-CN.md#c52). Detailed source IDs, conditions, archive and historic rating statements are in [cases.json](cases.json).

---

### C53 — CO-MOT (2025)

**Selection:** `core_positive`. **Outcome:** Accept (Poster). **Mechanisms:** `paper_revision`, `evaluation`, `related_work`, `negative_results`.

**Concern:** Whether a resubmission had materially improved

**Author action and observed response:** Listed exact manuscript changes and new evidence; reviewer explicitly moved 3→6

**Why teach / qualify this case:** Primary accepted example with a reviewer’s first-person numeric raise or unconditional numeric intention and a traceable action–feedback chain. Listed exact manuscript changes and new evidence; reviewer explicitly moved 3→6

**Do not overgeneralize:** Verify that every claimed revision exists in the submitted version 

**Sources:** [OpenReview discussion](https://openreview.net/forum?id=0ov0dMQ3mN) · [Key evidence note](https://openreview.net/forum?id=0ov0dMQ3mN&noteId=WxhCpMIhZG) · [Full original Chinese analysis](casebook.zh-CN.md#c53). Detailed source IDs, conditions, archive and historic rating statements are in [cases.json](cases.json).

---

### C54 — Variational Bayesian Pseudo-Coreset (2025)

**Selection:** `qualified_positive`. **Outcome:** Accept (Poster). **Mechanisms:** `evaluation`, `efficiency`, `claim_scope`, `ac_summary`.

**Concern:** Scale limits and out-of-memory behavior of a variational method

**Author action and observed response:** Reported scaling and OOM results, with archived score improvements

**Why teach / qualify this case:** Positive or improved outcome requiring attribution, condition, timing, rhetoric, or reviewer-stance qualifications. Reported scaling and OOM results, with archived score improvements

**Do not overgeneralize:** AC discounted highly similar reviews; some number paths rely on snapshot pairing 

**Sources:** [OpenReview discussion](https://openreview.net/forum?id=0NAVeUm7sk) · [Key evidence note](https://openreview.net/forum?id=0NAVeUm7sk&noteId=L8nLEBXLLf) · [Full original Chinese analysis](casebook.zh-CN.md#c54). Detailed source IDs, conditions, archive and historic rating statements are in [cases.json](cases.json).

---

### C55 — Generation and Comprehension Hand-in-Hand (2025)

**Selection:** `extended_positive`. **Outcome:** Accept (Poster). **Mechanisms:** `related_work`, `evaluation`, `efficiency`, `ac_summary`.

**Concern:** Related-work placement, sample budget and compute

**Author action and observed response:** Explained sampling and cost accounting; one reviewer explicitly moved 5→6

**Why teach / qualify this case:** Supplementary accepted example, specialized or overlapping with a core teaching mechanism. Explained sampling and cost accounting; one reviewer explicitly moved 5→6

**Do not overgeneralize:** The larger 3→6 history is AC-confirmed without a corresponding reviewer textual statement 

**Sources:** [OpenReview discussion](https://openreview.net/forum?id=1qbZekXGrp) · [Key evidence note](https://openreview.net/forum?id=1qbZekXGrp&noteId=IUT5MHiWcE) · [Full original Chinese analysis](casebook.zh-CN.md#c55). Detailed source IDs, conditions, archive and historic rating statements are in [cases.json](cases.json).

---

### C56 — Shallow Diffuse (2025)

**Selection:** `outcome_counterexample`. **Outcome:** Reject. **Mechanisms:** `evaluation`, `negative_results`, `claim_scope`, `ac_summary`.

**Concern:** Robustness and multi-key performance of a diffusion method

**Author action and observed response:** Paired snapshot showed four reviews shifting 5→6

**Why teach / qualify this case:** Score movement or partial resolution that did not yield acceptance or close the critical condition. Paired snapshot showed four reviews shifting 5→6

**Do not overgeneralize:** Ultimately rejected; broad superiority claims were inconsistent with negative results 

**Sources:** [OpenReview discussion](https://openreview.net/forum?id=1IwoEFyErz) · [Key evidence note](https://openreview.net/forum?id=1IwoEFyErz&noteId=E7x0QUpuNC) · [Full original Chinese analysis](casebook.zh-CN.md#c56). Detailed source IDs, conditions, archive and historic rating statements are in [cases.json](cases.json).

---

### C57 — GRIC (2025)

**Selection:** `outcome_counterexample`. **Outcome:** Reject. **Mechanisms:** `claim_scope`, `baseline_fairness`, `paper_revision`, `ac_summary`.

**Concern:** Whether a representation method actually qualifies as zero-shot

**Author action and observed response:** Some reviewers increased scores following discussion

**Why teach / qualify this case:** Score movement or partial resolution that did not yield acceptance or close the critical condition. Some reviewers increased scores following discussion

**Do not overgeneralize:** Ultimately rejected; ID-data PCA made the zero-shot framing and comparison fundamentally problematic 

**Sources:** [OpenReview discussion](https://openreview.net/forum?id=0owAtTCOlU) · [Key evidence note](https://openreview.net/forum?id=0owAtTCOlU&noteId=ykOuNZJSUs) · [Full original Chinese analysis](casebook.zh-CN.md#c57). Detailed source IDs, conditions, archive and historic rating statements are in [cases.json](cases.json).

---

### C58 — Multi-modal Agent Tuning (2025)

**Selection:** `qualified_positive`. **Outcome:** Accept (Spotlight). **Mechanisms:** `evaluation`, `benchmark_value`, `baseline_fairness`, `paper_revision`.

**Concern:** Annotation reliability and matched model comparisons in multi-modal tuning

**Author action and observed response:** Expanded blind human evaluation and corrected dataset statistics

**Why teach / qualify this case:** Positive or improved outcome requiring attribution, condition, timing, rhetoric, or reviewer-stance qualifications. Expanded blind human evaluation and corrected dataset statistics

**Do not overgeneralize:** Large raises rely partly on paired score archive; numeric targets not all stated directly 

**Sources:** [OpenReview discussion](https://openreview.net/forum?id=0bmGL4q7vJ) · [Key evidence note](https://openreview.net/forum?id=0bmGL4q7vJ&noteId=lKbzXFBqf9) · [Full original Chinese analysis](casebook.zh-CN.md#c58). Detailed source IDs, conditions, archive and historic rating statements are in [cases.json](cases.json).

---

### C59 — NetMoE (2025)

**Selection:** `evidence_exclusion`. **Outcome:** Accept (Spotlight). **Mechanisms:** `efficiency`, `claim_scope`, `negative_results`, `ac_summary`.

**Concern:** Reported score trajectory for network mixture of experts

**Author action and observed response:** Hardware-cost boundary and real measurements are useful

**Why teach / qualify this case:** Anomalous or conflicting numeric evidence excluded as clean reversal proof while preserved for audit. Hardware-cost boundary and real measurements are useful

**Do not overgeneralize:** Score archive conflicts with AC's description of initial scores; do not call it a clean numerical reversal 

**Sources:** [OpenReview discussion](https://openreview.net/forum?id=1qP3lsatCR) · [Key evidence note](https://openreview.net/forum?id=1qP3lsatCR&noteId=m4l4gosFxJ) · [Full original Chinese analysis](casebook.zh-CN.md#c59). Detailed source IDs, conditions, archive and historic rating statements are in [cases.json](cases.json).

---

### C60 — ThunderKittens (2025)

**Selection:** `qualified_positive`. **Outcome:** Accept (Spotlight). **Mechanisms:** `efficiency`, `evaluation`, `related_work`, `claim_scope`.

**Concern:** GPU kernel speed and controlled benchmark methodology

**Author action and observed response:** Measured precision, kernel configuration and shape variation; reviewer sentiment improved

**Why teach / qualify this case:** Positive or improved outcome requiring attribution, condition, timing, rhetoric, or reviewer-stance qualifications. Measured precision, kernel configuration and shape variation; reviewer sentiment improved

**Do not overgeneralize:** 5→8 targets depend on paired scores rather than direct first-person target statements 

**Sources:** [OpenReview discussion](https://openreview.net/forum?id=0fJfVOSUra) · [Key evidence note](https://openreview.net/forum?id=0fJfVOSUra&noteId=rx8VtsHol3) · [Full original Chinese analysis](casebook.zh-CN.md#c60). Detailed source IDs, conditions, archive and historic rating statements are in [cases.json](cases.json).

---

### C61 — Bayesian Optimization via Continual Variational Last Layer Training (2025)

**Selection:** `qualified_positive`. **Outcome:** Accept (Spotlight). **Mechanisms:** `efficiency`, `baseline_fairness`, `negative_results`, `claim_scope`, `ac_summary`.

**Concern:** Time-versus-quality trade-offs in Bayesian optimization

**Author action and observed response:** Added timing curves and stronger GP comparisons; acknowledged possible overclaim

**Why teach / qualify this case:** Positive or improved outcome requiring attribution, condition, timing, rhetoric, or reviewer-stance qualifications. Added timing curves and stronger GP comparisons; acknowledged possible overclaim

**Do not overgeneralize:** Score path comes from archived pairing; Spotlight decision still had a 5-score review 

**Sources:** [OpenReview discussion](https://openreview.net/forum?id=1jcnvghayD) · [Key evidence note](https://openreview.net/forum?id=1jcnvghayD&noteId=lGopSQgMyt) · [Full original Chinese analysis](casebook.zh-CN.md#c61). Detailed source IDs, conditions, archive and historic rating statements are in [cases.json](cases.json).

---

### C62 — Large Language Models Cannot Self-Correct Reasoning Yet (2024)

**Selection:** `qualified_positive`. **Outcome:** Accept (Poster). **Mechanisms:** `claim_scope`, `evaluation`, `paper_revision`, `ac_summary`.

**Concern:** Self-correction claims under different prompting and titles

**Author action and observed response:** Narrowed the title and added evaluations, including a supportive 6→8 path

**Why teach / qualify this case:** Positive or improved outcome requiring attribution, condition, timing, rhetoric, or reviewer-stance qualifications. Narrowed the title and added evaluations, including a supportive 6→8 path

**Do not overgeneralize:** Negative 3→6 path was conditional; archives and reviewer initial self-report conflict 

**Sources:** [OpenReview discussion](https://openreview.net/forum?id=IkmD3fKBPQ) · [Key evidence note](https://openreview.net/forum?id=IkmD3fKBPQ&noteId=b2CsLfx0dr) · [Full original Chinese analysis](casebook.zh-CN.md#c62). Detailed source IDs, conditions, archive and historic rating statements are in [cases.json](cases.json).

---

### C63 — Adaptive Rational Activations to Boost Deep Reinforcement Learning (2024)

**Selection:** `extended_positive`. **Outcome:** Accept (Spotlight). **Mechanisms:** `evaluation`, `baseline_fairness`, `theory_repair`, `paper_revision`.

**Concern:** Activation-capacity confounds and reinforcement-learning evaluation

**Author action and observed response:** Performed capacity-controlled ablations and explained mechanism

**Why teach / qualify this case:** Supplementary accepted example, specialized or overlapping with a core teaching mechanism. Performed capacity-controlled ablations and explained mechanism

**Do not overgeneralize:** Useful RL-specific complement to the more generally applicable core examples 

**Sources:** [OpenReview discussion](https://openreview.net/forum?id=g90ysX1sVs) · [Key evidence note](https://openreview.net/forum?id=g90ysX1sVs&noteId=lJPa2kx2YJ) · [Full original Chinese analysis](casebook.zh-CN.md#c63). Detailed source IDs, conditions, archive and historic rating statements are in [cases.json](cases.json).

---

### C64 — PF-LRM (2024)

**Selection:** `core_positive`. **Outcome:** Accept (Spotlight). **Mechanisms:** `baseline_fairness`, `multi_round`, `claim_scope`, `evaluation`.

**Concern:** Pose-free reconstruction baseline unfairly trained on different data

**Author action and observed response:** After a weak first explanation, actually retrained the competitor on matched training data; reviewer 3→8

**Why teach / qualify this case:** Primary accepted example with a reviewer’s first-person numeric raise or unconditional numeric intention and a traceable action–feedback chain. After a weak first explanation, actually retrained the competitor on matched training data; reviewer 3→8

**Do not overgeneralize:** Do not assume a mismatch is harmless merely because another generalization metric is interesting 

**Sources:** [OpenReview discussion](https://openreview.net/forum?id=noe76eRcPC) · [Key evidence note](https://openreview.net/forum?id=noe76eRcPC&noteId=mhgl0z4oWL) · [Full original Chinese analysis](casebook.zh-CN.md#c64). Detailed source IDs, conditions, archive and historic rating statements are in [cases.json](cases.json).

---

### C65 — Learning Delays in Spiking Neural Networks using Dilated Convolutions with Learnable Spacings (2024)

**Selection:** `qualified_positive`. **Outcome:** Accept (Poster). **Mechanisms:** `baseline_fairness`, `evaluation`, `novelty`, `claim_scope`.

**Concern:** Convolution comparisons in learnable-spacings SNNs

**Author action and observed response:** Added a standard-convolution control; reviewer trajectory reached 3→8

**Why teach / qualify this case:** Positive or improved outcome requiring attribution, condition, timing, rhetoric, or reviewer-stance qualifications. Added a standard-convolution control; reviewer trajectory reached 3→8

**Do not overgeneralize:** Reviewer criticized the aggressive reply tone; never copy rhetoric as the lesson 

**Sources:** [OpenReview discussion](https://openreview.net/forum?id=4r2ybzJnmN) · [Key evidence note](https://openreview.net/forum?id=4r2ybzJnmN&noteId=YHNDSBss1E) · [Full original Chinese analysis](casebook.zh-CN.md#c65). Detailed source IDs, conditions, archive and historic rating statements are in [cases.json](cases.json).

---

### C66 — Open the Black Box (2024)

**Selection:** `extended_positive`. **Outcome:** Accept (Poster). **Mechanisms:** `evaluation`, `multi_round`, `efficiency`, `negative_results`, `ac_summary`.

**Concern:** Diagonal versus full covariance necessity and training cost

**Author action and observed response:** Ran directly matched covariance and compute ablations; multiple reviewers increased

**Why teach / qualify this case:** Supplementary accepted example, specialized or overlapping with a core teaching mechanism. Ran directly matched covariance and compute ablations; multiple reviewers increased

**Do not overgeneralize:** Useful robotics extension of minimal-discriminative-experiment principle 

**Sources:** [OpenReview discussion](https://openreview.net/forum?id=mnipav175N) · [Key evidence note](https://openreview.net/forum?id=mnipav175N&noteId=DFn01HHdOK) · [Full original Chinese analysis](casebook.zh-CN.md#c66). Detailed source IDs, conditions, archive and historic rating statements are in [cases.json](cases.json).

---

### C67 — Teaching Large Language Models to Self-Debug (2024)

**Selection:** `core_positive`. **Outcome:** Accept (Poster). **Mechanisms:** `baseline_fairness`, `multi_round`, `evaluation`, `paper_revision`.

**Concern:** Whether self-debug gain was really a prompt artifact

**Author action and observed response:** Identified the precise paired-prompt confound and ran matching controls; reviewer 3→5→6

**Why teach / qualify this case:** Primary accepted example with a reviewer’s first-person numeric raise or unconditional numeric intention and a traceable action–feedback chain. Identified the precise paired-prompt confound and ran matching controls; reviewer 3→5→6

**Do not overgeneralize:** Earlier generic reply was insufficient; respond to the new remaining concern 

**Sources:** [OpenReview discussion](https://openreview.net/forum?id=KuPixIqPiq) · [Key evidence note](https://openreview.net/forum?id=KuPixIqPiq&noteId=n3hMAyMgy3) · [Full original Chinese analysis](casebook.zh-CN.md#c67). Detailed source IDs, conditions, archive and historic rating statements are in [cases.json](cases.json).

---

### C68 — In-Context Learning Dynamics with Random Binary Sequences (2024)

**Selection:** `core_positive`. **Outcome:** Accept (Poster). **Mechanisms:** `claim_scope`, `theory_repair`, `evaluation`, `paper_revision`.

**Concern:** Toy binary-sequence assumptions, terminology and external relevance

**Author action and observed response:** Removed misleading terms, clarified guarantees and linked toy setup to real-world claims

**Why teach / qualify this case:** Primary accepted example with a reviewer’s first-person numeric raise or unconditional numeric intention and a traceable action–feedback chain. Removed misleading terms, clarified guarantees and linked toy setup to real-world claims

**Do not overgeneralize:** Avoid presenting toy formal results as unrestricted empirical generalization 

**Sources:** [OpenReview discussion](https://openreview.net/forum?id=62K7mALO2q) · [Key evidence note](https://openreview.net/forum?id=62K7mALO2q&noteId=MZJoxtJytr) · [Full original Chinese analysis](casebook.zh-CN.md#c68). Detailed source IDs, conditions, archive and historic rating statements are in [cases.json](cases.json).

---

### C69 — Role of Locality and Weight Sharing in Image-Based Tasks (2024)

**Selection:** `core_positive`. **Outcome:** Accept (Spotlight). **Mechanisms:** `novelty`, `theory_repair`, `related_work`, `claim_scope`.

**Concern:** Novelty of locality and weight-sharing proof tools

**Author action and observed response:** Explained precisely where the prior proof failed and how a new lemma repairs it; reviewer 3→8

**Why teach / qualify this case:** Primary accepted example with a reviewer’s first-person numeric raise or unconditional numeric intention and a traceable action–feedback chain. Explained precisely where the prior proof failed and how a new lemma repairs it; reviewer 3→8

**Do not overgeneralize:** Do not claim novelty until the exact added argument is differentiated 

**Sources:** [OpenReview discussion](https://openreview.net/forum?id=AfnsTnYphT) · [Key evidence note](https://openreview.net/forum?id=AfnsTnYphT&noteId=LU7mrnXNe7) · [Full original Chinese analysis](casebook.zh-CN.md#c69). Detailed source IDs, conditions, archive and historic rating statements are in [cases.json](cases.json).

---

### C70 — MovingParts (2024)

**Selection:** `extended_positive`. **Outcome:** Accept (Spotlight). **Mechanisms:** `evaluation`, `multi_round`, `negative_results`, `claim_scope`.

**Concern:** Video reconstruction evaluation breadth and cherry-pick risk

**Author action and observed response:** Reported full sequences, more scenes and ablations; two reviewers moved 3→8

**Why teach / qualify this case:** Supplementary accepted example, specialized or overlapping with a core teaching mechanism. Reported full sequences, more scenes and ablations; two reviewers moved 3→8

**Do not overgeneralize:** Useful visual-reconstruction complement; not a separate universal persuasion tactic 

**Sources:** [OpenReview discussion](https://openreview.net/forum?id=QQ6RgKYiQq) · [Key evidence note](https://openreview.net/forum?id=QQ6RgKYiQq&noteId=9TrLjlAb3E) · [Full original Chinese analysis](casebook.zh-CN.md#c70). Detailed source IDs, conditions, archive and historic rating statements are in [cases.json](cases.json).


**For verbatim quotations or claim verification, open the original OpenReview notes.** The English summaries do not replace the evidence provenance, conditions or full primary record. The case sample is purposive and must not be used to calculate rebuttal success rates.
