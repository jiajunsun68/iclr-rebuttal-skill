# ICLR Rebuttal Skill

**English-first · Fully usable in English and 简体中文**

[English (default)](README.md) · [简体中文 / 中文完整说明](README.zh-CN.md) · [Skill instructions](skills/iclr-rebuttal/SKILL.md) · [中文技能说明](skills/iclr-rebuttal/SKILL.zh-CN.md)

An evidence-grounded agent skill for writing stronger ICLR and machine-learning **author rebuttals**. Instead of guessing a reviewer's personality or writing generic persuasion, it reconstructs the **scientific decision criterion** behind each criticism, decides what evidence would actually address it, and drafts a concise, source-honest response.

Its case catalogue covers **70 independent OpenReview paper discussions**: 49 from ICLR 2026, 12 from 2025 and 9 from 2024. It prioritizes **22 carefully chosen positive teaching cases**, retains failures and disputed score histories, and explains why spectacular-looking jumps are not always good models. Selection is purposive: these counts are **not** success-rate estimates.

## Install / 安装

Requires Node.js **22.20+** for the [Skills CLI](https://github.com/vercel-labs/skills). From the project where you want the skill:

~~~bash
# Codex
npx skills add jiajunsun68/iclr-rebuttal-skill --skill iclr-rebuttal -a codex

# Claude Code
npx skills add jiajunsun68/iclr-rebuttal-skill --skill iclr-rebuttal -a claude-code
~~~

Add \`-g\` for global installation, or use another agent supported by the CLI. The default \`SKILL.md\` is in English; a full Chinese version is available alongside it. **English is the default for diagnosis and submission-ready replies.** When you ask in Chinese, the agent may explain strategy in Chinese while drafting the actual English rebuttal, or produce Chinese on explicit request.

Example prompt:

~~~text
Use iclr-rebuttal for these reviewer comments and relevant manuscript excerpts.
Identify the reviewer's explicit request, plausible testable concern, confidence,
and the smallest sufficient evidence. Decide which points require new data or
proof, a factual rebuttal, concession/apology/correction, narrowed claims, or
clarification. Rank by importance to the recommendation. Use source-linked
cases, produce English point-by-point replies and a manuscript change checklist.
Do not invent experiment results or claim that a planned revision is completed.

[Paste the reviews, manuscript material, results, limits and conference rules.]
~~~

中文示例：

~~~text
请使用 iclr-rebuttal，分析审稿人表层问题和有证据支持的深层科学顾虑；
逐条判断需要补实验、据理反驳、承认道歉并修复、收窄主张还是澄清；
给出最小证据计划、相关 ICLR 真实案例、英文逐点回复和论文修改清单。
不可编造结果，不可把尚未完成的工作写成已完成。
~~~

## What the skill does

| Stage | Concrete behavior |
|---|---|
| **Infer the concern** | Separate verbatim reviewer request from a *hypothesis* about the confidence-blocking scientific issue; record alternative interpretations and confidence |
| **Choose the action** | Rebut a demonstrably wrong premise; add a controlled comparison or proof when needed; acknowledge a verified error and correct it; narrow an unsupported claim; request clarification when interpretations differ |
| **Design the evidence** | Specify the smallest test that discriminates between competing explanations; match baselines and budgets; report genuine uncertainty and negative results |
| **Draft the answer** | Use direct answer → evidence → actual manuscript change → remaining boundary, without empty flattery or invented results |
| **Handle follow-up** | Track whether the reviewer confirmed, partly agreed, gave a condition, did not reply, or remained opposed; respond to the latest blocker |
| **Prepare the AC summary** | Attribute historical scores correctly, preserve conditional commitments and remaining concerns; never manufacture consensus |
| **Humanize** | Tighten the prose using an academic adaptation of Humanizer, while protecting facts, equations, caveats, citations, and experiment status |

Read [the full decision guide](skills/iclr-rebuttal/references/reviewer-intent.md), [English response templates](skills/iclr-rebuttal/references/templates.md), and [evidence/follow-up rules](skills/iclr-rebuttal/references/evidence-and-followup.md).

### Five response choices

| Action | When it is justified | What must be provided |
|---|---|---|
| **Add experiments or proof** | A material empirical/theoretical claim lacks discriminative evidence | Controlled conditions, actual verified evidence, a bounded conclusion and unresolved gaps |
| **Rebut** | A checkable premise is factually or mathematically wrong, or the demand changes the stated question | A direct, specific correction with a traceable source or derivation |
| **Concede; apologize when appropriate** | Missing citation, incorrect table, implementation bug, unfair comparison or invalid proof is verified | Clear acknowledgement, effect on conclusions, concrete correction and manuscript location |
| **Narrow the claim** | A guarantee or empirical conclusion overreaches available evidence | Precise replacement claim and synchronized paper edits |
| **Clarify or ask a question** | Existing evidence is difficult to find, or the request is truly ambiguous | Direct explanation and location; one targeted question only when it changes the action |

A single comment can require both a factual rebuttal and a concession. For example, equal data volume does **not** prove equal hyperparameter search budgets.

## Why reviewer scores require careful attribution

**ICLR 2026 is exceptional:** after the November 2025 OpenReview security incident, review text and ratings were reset to the pre-discussion state. New ACs assessed available discussion history, author responses, and their independent judgment. Therefore current \`rating\` fields do **not** necessarily show the rebuttal-end score. Sources: [ICLR official response, December 3, 2025](https://blog.iclr.cc/2025/12/03/iclr-2026-response-to-security-incident/) and [retrospective, March 31, 2026](https://blog.iclr.cc/2026/03/31/a-retrospective-on-the-iclr-2026-review-process/).

| Evidence in a discussion | Supported interpretation | Unsupported leap |
|---|---|---|
| Reviewer explicitly reports raising a score | Historical first-person score statement | Today's rating still equals that number |
| Reviewer says they *will* raise it | Unconditional stated intention | The interface was actually updated |
| Reviewer says *if X, then raise* | Conditional willingness, requiring follow-up | Authors completing X means reviewer confirmed |
| Author or AC gives historical score | Attributed report, subject to source conflict | The target was stated directly by the reviewer |
| AC *expects* a higher score | AC prediction/judgment | Every reviewer actually changed rating |
| Final Accept / Oral / Spotlight | Conference decision | All negative reviewers changed, or one reply caused acceptance |

Case-specific qualifications live in [the case selection guide](skills/iclr-rebuttal/references/case-selection.md), [the English 70-case overview](skills/iclr-rebuttal/references/casebook.md) and [the complete Chinese casebook](skills/iclr-rebuttal/references/casebook.zh-CN.md).

## Why these 22 core cases

Core entry requires: **(1)** first-person, explicit numeric raise or unconditional numeric intention, rather than only an author paraphrase, AC guess or unfulfilled condition; **(2)** final acceptance; **(3)** a traceable concern → author action → reviewer feedback chain; **(4)** a reusable, complementary teaching mechanism. A case with mixed evidence qualifies only on the specific reviewer path that passes the test. Inclusion never means all concerns were resolved, that a saved score is still visible, or that the reply caused acceptance.

| Case | Reusable lesson and reason for selection |
|---|---|
| [C64 PF-LRM](https://openreview.net/forum?id=noe76eRcPC) (2024) | Fairness: rerunning the disputed baseline on matched training data changed the reviewer's assessment; stronger than merely defending a mismatched comparison. |
| [C09 Explainable LLM Unlearning](https://openreview.net/forum?id=wec4qy2XIF) (2026) | Reproduce and audit a weak baseline; admit the competitor's advantages and residual metric limitations. |
| [C17 Conductor](https://openreview.net/forum?id=U23A2BUKYt) (2026) | Replace a proposed module with a strong alternative and compare cost to test necessity. |
| [C10 NSPO](https://openreview.net/forum?id=GFyVxtyMvq) (2026) | Distinct rounds: fairness controls first, approximation/distribution boundaries second; first-person 2→4→6 sequence. |
| [C12 Best-of-N](https://openreview.net/forum?id=tCv1D3M7Lb) (2026) | Withdraw an unsupported theoretical interpretation and rebuild the argument; don't confuse the inequality with the claim it fails to prove. |
| [C23 Taming Score-Based Denoisers](https://openreview.net/forum?id=BiXwSIIMIq) (2026) | Repair a theorem to cover the finite-step algorithm instead of an idealized stationary setting. |
| [C18 Softmax Transformers are Turing-Complete](https://openreview.net/forum?id=FdkPOHlChS) (2026) | Clarify theorem scope, assumptions, relation to prior work, and expressivity versus trainability; multiple first-person raises. |
| [C69 Role of Locality and Weight Sharing](https://openreview.net/forum?id=AfnsTnYphT) (2024) | Precisely identify where the previous proof fails and which new lemma supplies the missing result. |
| [C28 LCA](https://openreview.net/forum?id=3uINmRldVW) (2026) | Admit an adapted existing component and redefine the actual novel contribution; reviewer explicitly moved 4→6. |
| [C52 GenSE](https://openreview.net/forum?id=1p6xFLBU4J) (2025) | Correct a missed citation and substantively compare mechanism and task, not just add a bibliography entry. |
| [C13 GPG](https://openreview.net/forum?id=inccdtfx8x) (2026) | Narrow scope in the manuscript itself, then get explicit confirmation rather than claiming a promised change is complete. |
| [C68 In-Context Learning Dynamics](https://openreview.net/forum?id=62K7mALO2q) (2024) | Remove misleading terminology and link an idealized toy setting to claims about real tasks. |
| [C25 FACT](https://openreview.net/forum?id=j3gNYqrHtl) (2026) | Directly test aggregation, variable order and hyperparameter sensitivity instead of adding unrelated experiments. |
| [C02 FASA](https://openreview.net/forum?id=FnSgecCEwg) (2026) | Distinguish resolved decision-critical calibration concerns from surviving theory/sparsity questions. |
| [C67 Teaching LLMs to Self-Debug](https://openreview.net/forum?id=KuPixIqPiq) (2024) | Reinterpret the real prompt confound after follow-up, then run a paired control; 3→5→6. |
| [C15 SCUBA](https://openreview.net/forum?id=bkjKnO9s7T) (2026) | Show benchmark utility via implementable trajectories, task templates and evaluator code; staged response. |
| [C19 InnovatorBench](https://openreview.net/forum?id=w8rZ2Jd6Jo) (2026) | Narrow a broad benchmark claim and report genuine zero-score failures without hiding them. |
| [C11 Keep the Best, Forget the Rest](https://openreview.net/forum?id=LrHfYPFTtg) (2026) | Turn promised strong-baseline/multi-judge/sensitivity experiments into verifiable, included results. |
| [C32 Procedural Mistake Detection](https://openreview.net/forum?id=HsB5EuQOoS) (2026) | Check test-threshold choice and stronger substitute models to restore evaluation credibility. |
| [C33 Metric Tensors on Neuromanifolds](https://openreview.net/forum?id=Ssevs8KCsU) (2026) | Calibrate a theoretical estimator against computable ground truth; keep the score-source conflict explicit. |
| [C26 Atomic HINs](https://openreview.net/forum?id=AG7fjg5azU) (2026) | Answer engineering feasibility with actual runtime, amortization and backend portability. |
| [C53 CO-MOT](https://openreview.net/forum?id=0ov0dMQ3mN) (2025) | For a resubmission, provide a traceable change log and correct an inaccurate “no progress” perception. |

[Evidence policy and selection criteria](skills/iclr-rebuttal/references/case-selection.md) · [All 70 cases](skills/iclr-rebuttal/references/casebook.md)

## Why some spectacular jumps are **not** core templates

“Excluded from core” means **not suitable as clean evidence of a reproducible positive reversal**—not that the paper, reviewer, or entire conversation is uninformative. Most remain valuable qualified examples. The README names the exact attribution issue rather than sorting papers by score increase.

| Case | Why it is not presented as a clean, recommended reversal |
|---|---|
| [C50 Dynamic Neural Fortresses — apparent 1→8](https://openreview.net/forum?id=029hDSVoXK) | AC explicitly discarded the anomalous jump as an outlier, with no corresponding explanatory dialogue. |
| [C59 NetMoE](https://openreview.net/forum?id=1qP3lsatCR) | Paired score archive conflicts with the AC's description of the initial scores. |
| [C43 MonoSoup](https://openreview.net/forum?id=ICANwnoGgN) | AC recorded several raises, but the paper was rejected amid remaining theoretical/benefit concerns. |
| [C56 Shallow Diffuse](https://openreview.net/forum?id=1IwoEFyErz) | Archived four 5→6 changes did not prevent rejection; robustness and broad superiority claims remained problematic. |
| [C57 GRIC](https://openreview.net/forum?id=0owAtTCOlU) | Multiple raises did not repair the zero-shot definition and experimental framework; rejected. |
| [C46 ASMG](https://openreview.net/forum?id=xsqiDQjSvV) | Multiple 4→6 statements, yet AC judged complexity/benefit/coverage inadequate; rejected. |
| [C44 FuseGPT](https://openreview.net/forum?id=tNnXu5bKoo) | 2→4 is still on the reject side and the paper was rejected. |
| [C45 Censoring with Plausible Deniability](https://openreview.net/forum?id=vSXIEbTVhE) | 2→4 confirmed; further 4→6 was conditional and not closed; rejected. |
| [C37 DeMo](https://openreview.net/forum?id=U9oewpa7cn) | One reviewer's 4→6 was conditional; an AC prediction of four 6s is not four actual changes. |
| [C47 InfoNCE Induces Gaussian Distribution](https://openreview.net/forum?id=BlSH7gNQSq) | Final Oral despite initial 8/4/2/2; AC predicted improvement but no verified per-reviewer final vector. |
| [C48 GAGA](https://openreview.net/forum?id=Q9gz8lVyAi) | A 2→6 intention is reviewer-specific; another reviewer disputed the AC's projection of broader agreement. |
| [C49 PLAGUE](https://openreview.net/forum?id=05hNleYOcG) | Low initial scores and final Poster show independent AC judgment, not documented numeric reversals. |
| [C27 Quantum Attention Approximation — 4→8](https://openreview.net/forum?id=0zIcPe4CtY) | The numeric movement is credible, but a reviewer criticized the original draft's maturity and excessive revision scale. Learn proof repair, not “submit unfinished proof.” |
| [C65 Learning Delays in SNNs — 3→8](https://openreview.net/forum?id=4r2ybzJnmN) | Reviewer explicitly criticized aggressive tone; copy the controlled comparison, not the rhetoric. |
| [C38 Accelerated Parallel Tempering](https://openreview.net/forum?id=CODnlyYUli) | Reviewer explicitly credited discussion with other reviewers too, so changes cannot all be attributed to the rebuttal. |
| [C01 BiasFreeBench](https://openreview.net/forum?id=Ncf2LFDT4e) | Reviewer said score increased, but target 6 was supplied by the authors rather than a first-person numeric statement. |
| [C04 Token-Efficient Item Representation via Images](https://openreview.net/forum?id=vizM7B7vuW) | Improvements were by already supportive reviewers; target numbers were author-reported. |
| [C06 Steering Autoregressive Music Generation](https://openreview.net/forum?id=NaHzPMaCY9) | 8→10 was a supporter's intention, not reversal of the initial negative review. |
| [C62 LLMs Cannot Self-Correct Reasoning Yet](https://openreview.net/forum?id=IkmD3fKBPQ) | A 3→6 statement had a title condition; another 6→8 is a different review; initial snapshots also differ. |

All 19 are retained, with caveats, in the [case selection guide](skills/iclr-rebuttal/references/case-selection.md) and original-linked records.

## Search all 70 cases, in either language

The [Python search utility](skills/iclr-rebuttal/scripts/search_cases.py) uses only the standard library. **English is the default;** request Chinese with \`--lang zh-CN\`. It can filter by year, selection role, mechanism and keyword. IDs, forum URLs and numeric evidence retain their original identifiers.

~~~bash
python3 skills/iclr-rebuttal/scripts/search_cases.py --year 2026 --role core_positive --mechanism baseline_fairness --limit 4
python3 skills/iclr-rebuttal/scripts/search_cases.py --query bkjKnO9s7T --format json --lang en
python3 skills/iclr-rebuttal/scripts/search_cases.py --role outcome_counterexample --lang zh-CN --limit 6
~~~

English catalogue: [casebook.md](skills/iclr-rebuttal/references/casebook.md). Detailed Chinese catalogue: [casebook.zh-CN.md](skills/iclr-rebuttal/references/casebook.zh-CN.md). The [JSON source](skills/iclr-rebuttal/references/cases.json) retains the original Chinese analyses, adds aligned English summaries, and preserves all source note IDs and caveats.

## Academic Humanizer adaptation

Partly adapted from [blader/humanizer](https://github.com/blader/humanizer), pinned to [commit \`0ef9fe5bc3572734fd3ae6c448fe00a30cd5dcf0\`](https://github.com/blader/humanizer/commit/0ef9fe5bc3572734fd3ae6c448fe00a30cd5dcf0) (upstream SKILL.md v3.1.0, 26 patterns). The skill integrates the patterns **only after scientific verification**: remove generic “groundbreaking” claims, unnecessary praise and mechanical rhetoric, while preserving math, numbers, uncertainty, negative results, exact references, and planned-vs-completed status.

The academic module contains **12 original before/after examples**, not real ICLR experimental results. No claim is made that it defeats AI detectors or improves acceptance rates. Upstream copyright **Copyright (c) 2025 Siqi Chen**, MIT license, and pinned version are preserved in [THIRD_PARTY_NOTICES.md](THIRD_PARTY_NOTICES.md) and [the upstream license](skills/iclr-rebuttal/references/humanizer-LICENSE.txt). This adaptation is not endorsed by the upstream author.

## Documentation / 文档

| English (default) | 简体中文 | Scope |
|---|---|---|
| [SKILL.md](skills/iclr-rebuttal/SKILL.md) | [SKILL.zh-CN.md](skills/iclr-rebuttal/SKILL.zh-CN.md) | Main agent workflow |
| [Reviewer intent](skills/iclr-rebuttal/references/reviewer-intent.md) | [审稿意图](skills/iclr-rebuttal/references/reviewer-intent.zh-CN.md) | Concern inference and 17 issue types |
| [Evidence and follow-up](skills/iclr-rebuttal/references/evidence-and-followup.md) | [证据与跟进](skills/iclr-rebuttal/references/evidence-and-followup.zh-CN.md) | Facts, score attribution, AC |
| [Templates](skills/iclr-rebuttal/references/templates.md) | [回复模板](skills/iclr-rebuttal/references/templates.zh-CN.md) | Evidence-aware English replies |
| [Humanizer academic](skills/iclr-rebuttal/references/humanizer-academic.md) | [学术去 AI 味](skills/iclr-rebuttal/references/humanizer-academic.zh-CN.md) | Editing safeguards and examples |
| [Case selection](skills/iclr-rebuttal/references/case-selection.md) | [选例说明](skills/iclr-rebuttal/references/case-selection.zh-CN.md) | Core, excluded, qualified |
| [70-case overview](skills/iclr-rebuttal/references/casebook.md) | [70 篇案例详录](skills/iclr-rebuttal/references/casebook.zh-CN.md) | Linked discussions and transferable insights |
| [Validation](evals/RESULTS.md) | [验证记录](evals/RESULTS.zh-CN.md) | Test scope and limitations |

## Checks and limitations

~~~bash
python3 scripts/validate_repository.py
python3 -m unittest discover -s tests -v
~~~

These checks validate structure, links, translated case metadata, role classifications and CLI behavior; they cannot verify paper results, prove rebuttal causality or predict acceptance. ICLR 2026's rollback and year-to-year rating differences preclude naive comparisons. All decisions must remain grounded in the author's actual paper and the conference's current rules.

Licensed under [MIT](LICENSE). See [third-party attribution](THIRD_PARTY_NOTICES.md).
