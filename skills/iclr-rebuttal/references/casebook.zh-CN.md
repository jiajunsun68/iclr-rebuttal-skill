# 70 篇 ICLR rebuttal 案例手册

这是源链接与独立分析的阅读索引，不是原始评审全文转载。每一例对应一个独立 OpenReview forum；查阅原话时打开具体 note。原站临时不可访问时，可参考记录的作者存档或公开数据快照。

**先读限制：** 2026 年评分已回滚；轨迹保留历史发言与证据类别，不代表当前 rating 或全部评审终分。角色不是论文质量分级；提分与接收不同，目的性样本不支持成功率或话术因果。选择规则见 [case-selection.md](case-selection.zh-CN.md)，结构化完整来源与状态见 [cases.json](cases.json)。

## 目录与快速索引

| ID | 年份 | 论文简称 | 教学角色 | 最终决定 |
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

## C01

### [BiasFreeBench: a Benchmark for Mitigating Bias in Large Language Model Responses](https://openreview.net/forum?id=Ncf2LFDT4e)

**ICLR 2026 · Accept (Poster) · `qualified_positive`**

**记录到的变化：** 156a 4→6（目标数字由作者总结给出）；zx3y 维持6

**证据身份：** 本人表态；数字由作者补充；2026评分栏已回滚；数值变化仅按本人讨论表态、明确标注的作者/AC历史转述记录。

**原始阻碍：** QA式评价不新颖；benchmark与去偏方法贡献混杂；单一分数能否覆盖多种偏差；LLM judge偏差/拒答混淆。

**作者动作：** 用贡献与前作对照表区分闭式QA和开放式完整回答评估；把4类prompting与4类training方法置于统一response-level协议。 明确指标针对fair/safe/benign responses，不宣称一个分数刻画所有公平性。 补GPT-5-mini judge并重新跑主要表，回应评估器偏差。

**评审反馈：** 156a明确说贡献和新颖性疑虑得到澄清并愿意提分；zx3y维持6；AC认为3/4评审总体正面，最终Poster。

**选例理由：** 贡献定位与更换judge的回应可学习；本人确认提高，但4→6的目标值仅由作者总结给出，因此不作为本人数字逆转确证。

**可迁移机制：** 把新问题、已有组件与统一评价协议逐项对照；对judge偏差用另一评估器复核。

**必须保留的限制：** 156a没有亲口给6；zx3y明确维持6。不能把认可解释成全员加分或把作者总结升级为本人记录。 不能把4→6写为评审亲口精确数值；hVui初始2未被证明转正。

**阅读范围与访问来源：** 作者网页存档17页中读取初评、156a回应及跟进、zx3y补judge讨论、AC和decision；raw交叉核对。；作者主页保存的原始OpenReview网页PDF全文 + 原始notes数据快照交叉核对

**机制标签：** `novelty`、`evaluation`、`claim_scope`、`ac_summary`

**复核链接：** [重点评审 note](https://openreview.net/forum?id=Ncf2LFDT4e&noteId=nshgScU10i) · [其他关键 note 2](https://openreview.net/forum?id=Ncf2LFDT4e&noteId=PRln4eZoZM) · [其他关键 note 3](https://openreview.net/forum?id=Ncf2LFDT4e&noteId=MHnNCUXVfz) · [作者回复 1](https://openreview.net/forum?id=Ncf2LFDT4e&noteId=Vcyu8Fjkqi) · [AC](https://openreview.net/forum?id=Ncf2LFDT4e&noteId=HbFJkG8TZA) · [决定](https://openreview.net/forum?id=Ncf2LFDT4e&noteId=9RJubtcu7M) · [作者存档](https://cseweb.ucsd.edu/~jmcauley/reviews/iclr26a.pdf) · [公开档案](https://huggingface.co/datasets/McGill-NLP/AI-For-Science-Retreat-Data/blob/main/iclr-dataset/iclr_2026_raw.parquet)

## C02

### [FASA: FREQUENCY-AWARE SPARSE ATTENTION](https://openreview.net/forum?id=FnSgecCEwg)

**ICLR 2026 · Accept (Poster) · `core_positive`**

**记录到的变化：** VxaW 4→6

**证据身份：** 本人明确数值表态；2026评分栏已回滚；数值变化仅按本人讨论表态、明确标注的作者/AC历史转述记录。

**原始阻碍：** 功能性频率稀疏缺理论；热图可能挑选；跨任务与校准独立性不足；长上下文与CoT用不同校准；设置和图不清楚。

**作者动作：** 量化10模型dominant frequency chunks占比，并分析主/非主FC预测贡献。 补4模型跨任务FC overlap与跨校准实验；解释模型中心校准而非对每个任务调参。 调整正文设置与图像；后续补CDF，承认完整理论仍开放。

**评审反馈：** VxaW保留W1理论疑虑，W2仅部分缓解，但W3/W4完全解决，明确4→6；说额外W2解释对最终评级影响不大。AC保守写likely+2，最终Poster。

**选例理由：** 本人明确4→6；清楚显示核心疑虑解决即可提高支持度，同时保留部分理论与稀疏性疑问，适合教问题优先级。

**可迁移机制：** 把校准依赖等决定性疑虑转为跨任务、跨校准试验；用分布量化补热图，并准确列出残余意见。

**必须保留的限制：** 只模仿针对性证据与诚实总结；评审W1仍保留、W2部分解决，不能套用作者“全部解决”的自述。 作者summary“all concerns addressed”比评审原文更强；本记录以评审原话为准。

**阅读范围与访问来源：** 作者网页存档25页，重点阅读VxaW初评、三段回应、明确提分与保留意见及AC；raw核对note。；作者主页保存的原始OpenReview网页PDF全文 + 原始notes数据快照交叉核对

**机制标签：** `evaluation`、`multi_round`、`claim_scope`、`ac_summary`

**复核链接：** [核心数值表态](https://openreview.net/forum?id=FnSgecCEwg&noteId=un60K64zf2) · [作者回复 1](https://openreview.net/forum?id=FnSgecCEwg&noteId=H5n9JZfKdF) · [作者回复 2](https://openreview.net/forum?id=FnSgecCEwg&noteId=oAu1bXHsRA) · [作者回复 3](https://openreview.net/forum?id=FnSgecCEwg&noteId=41abXNRLMY) · [AC](https://openreview.net/forum?id=FnSgecCEwg&noteId=Tg1YSs21TV) · [决定](https://openreview.net/forum?id=FnSgecCEwg&noteId=afZqSdCTZh) · [作者存档](https://cseweb.ucsd.edu/~jmcauley/reviews/iclr26b.pdf) · [公开档案](https://huggingface.co/datasets/McGill-NLP/AI-For-Science-Retreat-Data/blob/main/iclr-dataset/iclr_2026_raw.parquet)

## C03

### [Evaluating Memory in LLM Agents via Incremental Multi-Turn Interactions](https://openreview.net/forum?id=DT7JyQC3MR)

**ICLR 2026 · Accept (Poster) · `context_only`**

**记录到的变化：** 仅有AC提分预期，未证实逐评审数字变化

**证据身份：** AC预期，非真实终评分；2026评分栏已回滚；数值变化仅按本人讨论表态、明确标注的作者/AC历史转述记录。

**原始阻碍：** 选择性遗忘任务被认为人造；test-time learning可能只是长上下文检索；RAG与长上下文比较预算不公；仅语言任务；提示是否能绕过。

**作者动作：** 补相关工作、short-context可解性、zero-shot对照来区分记忆与推理。 加成本分析和compute-matched RAG/long-context比较，分别说明低/高预算区间。 补显式覆盖提示的policy grid，检验任务是否被简单prompt解决。

**评审反馈：** AC预计nPYL仍4、zBBu强6、Mcjo8、RnwS可能6→8；这些都是AC反事实判断，没有本人实际提分证据。最终Poster。

**选例理由：** compute-matched比较和记忆能力负控有研究价值，但没有评审本人数字提分，适合作为方法背景和AC判断对照。

**可迁移机制：** 用预算配平、zero-shot、提示网格区分记忆能力与其他解释。

**必须保留的限制：** RnwS可能6→8等均为AC预期；nPYL的选择性遗忘概念异议可能仍在，不能称实际翻盘。 不能把RnwS可能6→8计为真实改分；选择性遗忘的哲学性保留仍在。

**阅读范围与访问来源：** 作者网页存档18页读取所有初评、主要fairness/validity回应、AC和decision。；作者主页保存的原始OpenReview网页PDF全文 + 原始notes数据快照交叉核对

**机制标签：** `baseline_fairness`、`benchmark_value`、`evaluation`

**复核链接：** [重点评审 note](https://openreview.net/forum?id=DT7JyQC3MR&noteId=RwE8eXFlXJ) · [决定](https://openreview.net/forum?id=DT7JyQC3MR&noteId=o1D3SWn2Vl) · [作者存档](https://cseweb.ucsd.edu/~jmcauley/reviews/iclr26c.pdf) · [公开档案](https://huggingface.co/datasets/McGill-NLP/AI-For-Science-Retreat-Data/blob/main/iclr-dataset/iclr_2026_raw.parquet)

## C04

### [Token-Efficient Item Representation via Images for LLM Recommender Systems](https://openreview.net/forum?id=vizM7B7vuW)

**ICLR 2026 · Accept (Poster) · `qualified_positive`**

**记录到的变化：** 1MNz 6→8（目标数字由作者总结给出）；11jm 8→10（目标数字由作者总结给出）

**证据身份：** 本人表态；数字由作者补充；2026评分栏已回滚；数值变化仅按本人讨论表态、明确标注的作者/AC历史转述记录。

**原始阻碍：** images-only宣传过强；与LC-Rec语义ID差异不清；图像编码开销；弱视觉域如书籍；参数预算公平性和新商品扩展。

**作者动作：** 缩窄为图片是节约token的商品表示，并非无文本即可万能；说明缺图/低质图fallback。 增加Goodbooks、MicroLens以及图像增强TALLRec/LCRec。 LoRA参数预算配平，catalog由5K扩到20K并报告训练/推理/显存成本。

**评审反馈：** 两位原本正面评审确认提高；AC预测3dZW可能4→6但没有本人数字确认；xUwd2仍可能维持。最终Poster。

**选例理由：** 有两位支持者确认加分，但6→8和8→10均由作者总结补充；适合说明巩固支持者和收窄标题，不作负评亲口转正模板。

**可迁移机制：** 缩窄images-only宣传，匹配可训练参数并报告catalog扩展与真实开销。

**必须保留的限制：** 负面评审是否转正没有本人证据；不要把正面支持增强写成2→10或全员转正。 并非已验证负评者转正；当前metadata标题已是Token-Efficient Item Representation via Images。

**阅读范围与访问来源：** 原始网页PDF18页读取四初评、主要回应、两条提分、author summary和AC；raw核对。；作者主页保存的原始OpenReview网页PDF全文 + 原始notes数据快照交叉核对

**机制标签：** `claim_scope`、`baseline_fairness`、`efficiency`

**复核链接：** [重点评审 note](https://openreview.net/forum?id=vizM7B7vuW&noteId=tr1dPtDDM5) · [其他关键 note 2](https://openreview.net/forum?id=vizM7B7vuW&noteId=0ul1MhpP5m) · [其他关键 note 3](https://openreview.net/forum?id=vizM7B7vuW&noteId=MWE4uOHcGZ) · [作者回复 2](https://openreview.net/forum?id=vizM7B7vuW&noteId=9U5Cqd1MTc) · [作者回复 3](https://openreview.net/forum?id=vizM7B7vuW&noteId=AvsFeo4CB8) · [作者回复 4](https://openreview.net/forum?id=vizM7B7vuW&noteId=9jo4kHJPAU) · [作者回复 5](https://openreview.net/forum?id=vizM7B7vuW&noteId=HXvc4HWBMe) · [AC](https://openreview.net/forum?id=vizM7B7vuW&noteId=JRzaD8lqoH) · [决定](https://openreview.net/forum?id=vizM7B7vuW&noteId=ebfjMncXtQ) · [作者存档](https://cseweb.ucsd.edu/~jmcauley/reviews/iclr26d.pdf) · [公开档案](https://huggingface.co/datasets/McGill-NLP/AI-For-Science-Retreat-Data/blob/main/iclr-dataset/iclr_2026_raw.parquet)

## C05

### [How to train data-efficient LLMs](https://openreview.net/forum?id=yKUbw7q1IA)

**ICLR 2026 · Accept (Poster) · `context_only`**

**记录到的变化：** 仅有AC提分预期，未证实逐评审数字变化

**证据身份：** AC预期，非真实终评分；2026评分栏已回滚；数值变化仅按本人讨论表态、明确标注的作者/AC历史转述记录。

**原始阻碍：** 计算成本未完整；现代/大模型覆盖不足；prompt/judge敏感性；数据选择机制与自强化信息茧房风险。

**作者动作：** 解释AskLLM式选择的计算开销、prompt和judge；提供变体与机制讨论。 对模型多样性和信息茧房给定性分析，但没有完整现代模型补充或实证消除风险。

**评审反馈：** 五位初评均6/8。AC预计WkEw可能提高，其他维持或略升，明确指出若干只定性回答仍不足；最终Poster。

**选例理由：** 初始全为6/8，提分仅有AC推测；保留为成本回应与定性解释不足的对照。

**可迁移机制：** 对数据效率给全流程计算账单，并将机制推测与实际验证分开。

**必须保留的限制：** 不是拒转收，不能以最终接收推断作者回应使每位评审提高。 没有实际数字提分证据，不能称拒转收；初始已全正面。

**阅读范围与访问来源：** 原始网页PDF16页读取初评、成本/机制回应、AC和decision。；作者主页保存的原始OpenReview网页PDF全文 + 原始notes数据快照交叉核对

**机制标签：** `efficiency`、`evaluation`、`ac_summary`

**复核链接：** [重点评审 note](https://openreview.net/forum?id=yKUbw7q1IA&noteId=CaiBtzcKaD) · [决定](https://openreview.net/forum?id=yKUbw7q1IA&noteId=OKDDV6Vmc8) · [作者存档](https://cseweb.ucsd.edu/~jmcauley/reviews/iclr26e.pdf) · [公开档案](https://huggingface.co/datasets/McGill-NLP/AI-For-Science-Retreat-Data/blob/main/iclr-dataset/iclr_2026_raw.parquet)

## C06

### [Steering Autoregressive Music Generation with Recursive Feature Machines](https://openreview.net/forum?id=NaHzPMaCY9)

**ICLR 2026 · Accept (Poster) · `qualified_positive`**

**记录到的变化：** h1Zj 8→10（意愿，非评分栏核验）

**证据身份：** 本人明确提分意愿；2026评分栏已回滚；数值变化仅按本人讨论表态、明确标注的作者/AC历史转述记录。

**原始阻碍：** 创新性与现有PEFT差异；缺简单prompt baseline；用自身probe评价有循环；主观听测与伦理流程不够明确。

**作者动作：** 增加prompt-only和prompt+RFM基线。 使用独立波形指标（chromagram/Essentia/onset density），附伪代码、音频与时变控制demo。 补听测人口构成/协议；面对AC明确追问确认遵守机构伦理程序。

**评审反馈：** h1Zj原8表示愿意升10并为接收辩护；UgTQ原2未更新。AC记录支持增强，最终Poster。

**选例理由：** 独立音频指标和prompt-only基线值得借鉴；8→10只是已有支持者的明确意愿，不能当负面逆转。

**可迁移机制：** 避免训练probe兼任唯一评测器；加入朴素强基线与独立信号验证。

**必须保留的限制：** h1Zj原8，UgTQ原2未转正；愿升10不等于评分栏保存10，伦理流程回应也须按具体要求回答。 不是2→10；负面评审没有亲自转正；意愿不是最终数值记录。

**阅读范围与访问来源：** 原始网页PDF14页读取UgTQ质疑、补实验、h1Zj支持与伦理AC往返、decision。；作者主页保存的原始OpenReview网页PDF全文 + 原始notes数据快照交叉核对

**机制标签：** `baseline_fairness`、`evaluation`、`ac_summary`

**复核链接：** [重点评审 note](https://openreview.net/forum?id=NaHzPMaCY9&noteId=MMa8uE4NYd) · [AC](https://openreview.net/forum?id=NaHzPMaCY9&noteId=XeXbkPqOSi) · [决定](https://openreview.net/forum?id=NaHzPMaCY9&noteId=tUfyo8mjjU) · [作者存档](https://cseweb.ucsd.edu/~jmcauley/reviews/iclr26f.pdf) · [公开档案](https://huggingface.co/datasets/McGill-NLP/AI-For-Science-Retreat-Data/blob/main/iclr-dataset/iclr_2026_raw.parquet)

## C07

### [Importance Sampling for Multi-Negative Multimodal Direct Preference Optimization](https://openreview.net/forum?id=HEFPwoGtTj)

**ICLR 2026 · Accept (Poster) · `context_only`**

**记录到的变化：** HwrY 初始4；认可回应，未证实提分；h9st 维持6

**证据身份：** 认可回应但未证实数值提分；2026评分栏已回滚；数值变化仅按本人讨论表态、明确标注的作者/AC历史转述记录。

**原始阻碍：** first listwise等新颖性定位过强；缺OPA-DPO/SymMPO等强比较；重要性采样无偏性/方差论证；组件与成本不清；幻觉外能力不足。

**作者动作：** 对照LPOI/PLPO调整first claim并承认前作；加OPA-DPO/SymMPO。 补无偏性与方差推导、各组件消融、计算成本和SEEDBench。

**评审反馈：** HwrY本人说主要疑虑解决；AC明确其未加分，认为回应有实质帮助；其余正面评审支持，最终Poster。

**选例理由：** 负面评审说主要顾虑解决，但AC明确其未加分；用于教授回应认可、数字变化和接收三者不同。

**可迁移机制：** 补近邻工作、理论与成本证据后，为AC准确整理已解决事项。

**必须保留的限制：** HwrY没有数值上涨；h9st明确维持6，不能将两条都计为加分。 MME/MMMU等广泛通用能力覆盖仍不足。

**阅读范围与访问来源：** 原始网页PDF18页读三初评、相关工作/理论/实验回应、HwrY acknowledgment、AC和decision。；作者主页保存的原始OpenReview网页PDF全文 + 原始notes数据快照交叉核对

**机制标签：** `related_work`、`theory_repair`、`evaluation`、`ac_summary`

**复核链接：** [重点评审 note](https://openreview.net/forum?id=HEFPwoGtTj&noteId=FBjEoeEWB3) · [其他关键 note 2](https://openreview.net/forum?id=HEFPwoGtTj&noteId=4YK8CEYJ1J) · [AC](https://openreview.net/forum?id=HEFPwoGtTj&noteId=7NQxOXTRhj) · [决定](https://openreview.net/forum?id=HEFPwoGtTj&noteId=WEEeGpUUHc) · [作者存档](https://cseweb.ucsd.edu/~jmcauley/reviews/iclr26g.pdf) · [公开档案](https://huggingface.co/datasets/McGill-NLP/AI-For-Science-Retreat-Data/blob/main/iclr-dataset/iclr_2026_raw.parquet)

## C08

### [Extending the Context of Pretrained LLMs by Dropping Their Positional Embedding](https://openreview.net/forum?id=RlPVSeKjoc)

**ICLR 2026 · Accept (Poster) · `extended_positive`**

**记录到的变化：** Zi8P 2→6；iW8i 4→6；fTZx 6→7（意愿，非评分栏核验）

**证据身份：** 本人明确数值表态；2026评分栏已回滚；数值变化仅按本人讨论表态、明确标注的作者/AC历史转述记录。

**原始阻碍：** 初稿模型<0.5B、评估/基线不足、是否仅2倍外推；NoPE恢复已有前作；“free”与YaRN公平性。

**作者动作：** 新增SmolLM1.7B与Llama2-7B，明确20B tokens再训练预算及预训练数据不可得的限制。 说明原LongBench含16x并补26任务完整结果、NIAH4K/8K/16K、NarrativeQA和长度分层。 增加LongRoPE2/ALiBi、校准预算/时机消融，澄清新贡献是获得有效NoPE骨干而非首次提出无位置编码。

**评审反馈：** Zi8P认为核心贡献得到扩展实验支撑，2→6；iW8i4→6但仍要求YaRN大scale同训练配方才可进一步加分；AC确认这些历史变化，Poster。

**选例理由：** 两位负面评审有明确2→6和4→6，可作规模与任务覆盖的扩展范例；默认核心已由更集中、较易复用的公平对照案例覆盖。

**可迁移机制：** 将模型规模、上下文长度、基线和训练预算逐一配到主张，区分已有证据与新补结果。

**必须保留的限制：** 新增7B训练代价很高，不建议机械复制；YaRN同预算公平性仍有保留，6→7只是另一评审的口头意愿。 iW8i核心公平比较仍未完全解决，不能说全员无保留；PvVC是否提分只见AC推断。

**阅读范围与访问来源：** 完整Zi8P多段回应与跟进、其他提分评论、AC和decision；初始2/4/2/6。；原始OpenReview notes数据快照（有id/replyto/signatures/rating），live页面访问受验证码限制；非摘要转述

**机制标签：** `evaluation`、`baseline_fairness`、`efficiency`、`claim_scope`

**复核链接：** [重点评审 note](https://openreview.net/forum?id=RlPVSeKjoc&noteId=NZTVcCaQeq) · [其他关键 note 2](https://openreview.net/forum?id=RlPVSeKjoc&noteId=0pfrdz3oGB) · [其他关键 note 3](https://openreview.net/forum?id=RlPVSeKjoc&noteId=9eV18BoiL6) · [作者回复 1](https://openreview.net/forum?id=RlPVSeKjoc&noteId=m2jiILIXKK) · [作者回复 2](https://openreview.net/forum?id=RlPVSeKjoc&noteId=0C7uhGhemt) · [作者回复 3](https://openreview.net/forum?id=RlPVSeKjoc&noteId=5WTcCUXOnq) · [AC](https://openreview.net/forum?id=RlPVSeKjoc&noteId=5nSLvw6Y3l) · [决定](https://openreview.net/forum?id=RlPVSeKjoc&noteId=SKmMsqvKvy) · [公开档案](https://huggingface.co/datasets/McGill-NLP/AI-For-Science-Retreat-Data/blob/main/iclr-dataset/iclr_2026_raw.parquet)

## C09

### [Explainable LLM Unlearning through Reasoning](https://openreview.net/forum?id=wec4qy2XIF)

**ICLR 2026 · Accept (Poster) · `core_positive`**

**记录到的变化：** NNq9 2→6

**证据身份：** 本人明确数值表态；2026评分栏已回滚；数值变化仅按本人讨论表态、明确标注的作者/AC历史转述记录。

**原始阻碍：** reasoning tags怎样加到非推理模型；是否只改变遗忘/效用权衡；RMU UQ接近0可能复现错；新LLM指标可靠性；鲁棒性比较不足。

**作者动作：** 交代tokenizer、think/answer监督和固定数据/权重的推理消融。 审计RMU，发现OpenUnlearning与原实现训练模块不同；改跑原实现并更新标准和新指标。 补MCQ/标准WMDP/ES指标及跨语言攻击对照；承认RMU在某些utility指标更好。

**评审反馈：** NNq9认为scope和跨语言鲁棒性有价值，2→6；明确不愿给8，因为新指标不足支撑最佳遗忘-保留权衡。作者随后修正全表而非只改局部。AC保留LLM judge和scope限制，Poster。

**选例理由：** 本人明确2→6，并清楚说明为何不给8；baseline复现审计、承认对方优势及全表修正是高价值纠错范例。

**可迁移机制：** 检查异常弱baseline的实现模块与配置；重跑原实现，并同时给公认指标、新指标及鲁棒性。

**必须保留的限制：** 提分不证明“最佳遗忘—效用权衡”；LLM指标可靠性仍受质疑，后续改表不能倒写成提分前已经完成。 提分时仍有Q3/Q4争议；不能宣称所有评审认可最佳tradeoff。

**阅读范围与访问来源：** 完整NNq9初评、5项回复、长追问与两条修正跟进、AC和decision。；原始OpenReview notes数据快照（有id/replyto/signatures/rating），live页面访问受验证码限制；非摘要转述

**机制标签：** `baseline_fairness`、`evaluation`、`negative_results`、`paper_revision`、`multi_round`

**复核链接：** [核心数值表态](https://openreview.net/forum?id=wec4qy2XIF&noteId=yrS6CQAobd) · [作者回复 1](https://openreview.net/forum?id=wec4qy2XIF&noteId=MstbhgkAf0) · [作者回复 2](https://openreview.net/forum?id=wec4qy2XIF&noteId=6CqNFZlyO2) · [作者回复 3](https://openreview.net/forum?id=wec4qy2XIF&noteId=3Uapnixqzm) · [作者回复 4](https://openreview.net/forum?id=wec4qy2XIF&noteId=PWp5RayyjT) · [作者回复 5](https://openreview.net/forum?id=wec4qy2XIF&noteId=9ahYbDUMb2) · [作者回复 6](https://openreview.net/forum?id=wec4qy2XIF&noteId=ZsCaNEDZMm) · [作者回复 7](https://openreview.net/forum?id=wec4qy2XIF&noteId=lIy7wx6iW0) · [AC](https://openreview.net/forum?id=wec4qy2XIF&noteId=FsLiSfcQ0F) · [决定](https://openreview.net/forum?id=wec4qy2XIF&noteId=YWlT6Eh5Rc) · [公开档案](https://huggingface.co/datasets/McGill-NLP/AI-For-Science-Retreat-Data/blob/main/iclr-dataset/iclr_2026_raw.parquet)

## C10

### [Mitigating the Safety Alignment Tax with Null-Space Constrained Policy Optimization](https://openreview.net/forum?id=GFyVxtyMvq)

**ICLR 2026 · Accept (Poster) · `core_positive`**

**记录到的变化：** M1U2 2→4→6；qyGg 4→6；w5Ps 4→6

**证据身份：** 本人明确数值表态；2026评分栏已回滚；数值变化仅按本人讨论表态、明确标注的作者/AC历史转述记录。

**原始阻碍：** 安全与效用能否真正解耦；梯度投影公式与d含义不清；baseline reward model不一致；训练和评估judge同族；超参表错；安全训练与utility测试域不重叠。

**作者动作：** 解释梯度投影与K的安全数据含义、d由架构决定；修正DPO beta/epochs表并提供配置。 用同LlamaGuard4奖励重跑SafeRLHF、换GPT4评估；补I-PhysicalSafety的safe/unsafe同域对照。 当新实验出现轻微utility跌落，承认approximate nullspace残差和reference/test分布差；解释特征值阈值与多样化K的实际tradeoff。

**评审反馈：** 第一轮未打消顾虑；公平重跑后M1U2升4，最后边界与机制分析后升6。qyGg/w5Ps各4→6；AC明确记录6/6/6/6，Poster。

**选例理由：** 本人完整2→4→6及另两位4→6；将公平性、近似误差和追问闭环串成可审计的多轮范例。

**可迁移机制：** 先配平奖励模型与评价条件，再用同域任务检验安全—效用权衡；面对小幅负结果解释近似与分布边界。

**必须保留的限制：** 异源judge不等于统计独立；近似投影不保证现实零安全税，不能把三轮同时发生的改动归功于一句话。 不可将nullspace方法解释为现实零安全税保证；讨论承认近似与分布差距。

**阅读范围与访问来源：** 完整M1U2初评和三轮作者/评审往返；另核对qyGg/w5Ps本人明确提分及AC。；原始OpenReview notes数据快照（有id/replyto/signatures/rating），live页面访问受验证码限制；非摘要转述

**机制标签：** `baseline_fairness`、`theory_repair`、`multi_round`、`negative_results`、`claim_scope`

**复核链接：** [核心数值表态](https://openreview.net/forum?id=GFyVxtyMvq&noteId=6jKiyVjkYR) · [重点评审 note](https://openreview.net/forum?id=GFyVxtyMvq&noteId=XGLoZWrYhN) · [其他关键 note 3](https://openreview.net/forum?id=GFyVxtyMvq&noteId=1hDRe2NBs2) · [其他关键 note 4](https://openreview.net/forum?id=GFyVxtyMvq&noteId=8m2PzeyGMt) · [作者回复 1](https://openreview.net/forum?id=GFyVxtyMvq&noteId=8bXoUVFB5u) · [作者回复 2](https://openreview.net/forum?id=GFyVxtyMvq&noteId=ucdgBrgT5J) · [作者回复 3](https://openreview.net/forum?id=GFyVxtyMvq&noteId=jNkZfNYNLV) · [作者回复 4](https://openreview.net/forum?id=GFyVxtyMvq&noteId=Lly32fvL7y) · [作者回复 5](https://openreview.net/forum?id=GFyVxtyMvq&noteId=5n6lx7jhDm) · [AC](https://openreview.net/forum?id=GFyVxtyMvq&noteId=8OagbtCjnd) · [决定](https://openreview.net/forum?id=GFyVxtyMvq&noteId=9bAPmAlcqi) · [公开档案](https://huggingface.co/datasets/McGill-NLP/AI-For-Science-Retreat-Data/blob/main/iclr-dataset/iclr_2026_raw.parquet)

## C11

### [Keep the Best, Forget the Rest: Reliable Alignment with Order-Aware Preference Optimization](https://openreview.net/forum?id=LrHfYPFTtg)

**ICLR 2026 · Accept (Poster) · `core_positive`**

**记录到的变化：** QGJd 2→6

**证据身份：** 本人明确数值表态；2026评分栏已回滚；数值变化仅按本人讨论表态、明确标注的作者/AC历史转述记录。

**原始阻碍：** reference model误校准会删有效样本；代码复现；单GPT judge偏差；少IPO/ORPO/R-DPO；q/tau敏感性。

**作者动作：** 解释gate与order-SGD风险下降/方差保证条件，弱中强reference模型对照。 四个LLM judge对同一匿名随机顺序输出对打分，提供胜率与Kendall tau。 先告知强baseline计算中，随后贴IPO/ORPO/R-DPO完整结果；补q×batch和tau sweep并给默认值建议。 上传红色标改稿并指出补充代码位置。

**评审反馈：** 新增强baseline结果发布后QGJd明确2→6；AC预测iNHd4也可能转正，但未见本人确认，Poster。

**选例理由：** 本人明确2→6；从“实验在跑”到实际发布强baseline、多judge与敏感性表，适合教授承诺兑现。

**可迁移机制：** 对同一批匿名随机顺序输出做多judge复核，补近邻强基线与参数网格，并给默认设置和修订位置。

**必须保留的限制：** 多judge一致不是人工真值；iNHd是否4→正面仅AC预期，不要扩写为全部评审同意。 judge一致不等于人工真值验证；iNHd4→正面仅AC反事实。

**阅读范围与访问来源：** 完整QGJd初评、6段回应与后续baseline表、明确改分、AC和decision。；原始OpenReview notes数据快照（有id/replyto/signatures/rating），live页面访问受验证码限制；非摘要转述

**机制标签：** `evaluation`、`baseline_fairness`、`efficiency`、`paper_revision`

**复核链接：** [核心数值表态](https://openreview.net/forum?id=LrHfYPFTtg&noteId=1nAh6t0eMT) · [作者回复 1](https://openreview.net/forum?id=LrHfYPFTtg&noteId=jwSDy38zpy) · [作者回复 2](https://openreview.net/forum?id=LrHfYPFTtg&noteId=F1bEJDbYDk) · [作者回复 3](https://openreview.net/forum?id=LrHfYPFTtg&noteId=fSJYUYu0S6) · [作者回复 4](https://openreview.net/forum?id=LrHfYPFTtg&noteId=jjJeWsurRO) · [作者回复 5](https://openreview.net/forum?id=LrHfYPFTtg&noteId=GtM8GKyLVV) · [作者回复 6](https://openreview.net/forum?id=LrHfYPFTtg&noteId=Axmf5zZN0c) · [作者回复 7](https://openreview.net/forum?id=LrHfYPFTtg&noteId=9hDS0PjDkw) · [AC](https://openreview.net/forum?id=LrHfYPFTtg&noteId=XZTFcu5TFW) · [决定](https://openreview.net/forum?id=LrHfYPFTtg&noteId=CxAxy2h0ii) · [公开档案](https://huggingface.co/datasets/McGill-NLP/AI-For-Science-Retreat-Data/blob/main/iclr-dataset/iclr_2026_raw.parquet)

## C12

### [Best-of-N through the Smoothing Lens: KL Divergence and Regret Analysis](https://openreview.net/forum?id=tCv1D3M7Lb)

**ICLR 2026 · Accept (Poster) · `core_positive`**

**记录到的变化：** rpmQ 2→6；vx3U 初始4；表态提高/支持，目标数字未知

**证据身份：** 本人明确数值表态；2026评分栏已回滚；数值变化仅按本人讨论表态、明确标注的作者/AC历史转述记录。

**原始阻碍：** 符号复杂；beta多个角色；reward upper bound不能推出性能改善/非单调tradeoff；finite-N regret下界缺；证明步骤与离散假设不清。

**作者动作：** 补符号表、假设与证明中间步骤、指标方向；导出finite N/fixed beta下界。 首轮仍试图用Theorem4.3上界解释过优化，评审指出逻辑问题后承认并删除整个定理。 用KL分解和Appendix K信息投影重构可支持的结论，解释proxy error消耗divergence预算。

**评审反馈：** rpmQ认为主线与贡献终于清楚，2→6；不给8原因是自认领域熟悉度有限。vx3U原4明确推荐accept但未写目标；AC认可两负面转正，Poster。

**选例理由：** 本人明确2→6；作者撤去不能支持性能解释的定理并重建论据，展示如何处理实质理论反驳。

**可迁移机制：** 检验定理是否真的推出主张；若解释不成立，删除或收窄，并以新的分解、界限或证明替代。

**必须保留的限制：** 不能断言原不等式数学上已被证明为假；该例支持修复论据，不支持先提交不完整理论再等rebuttal重写。 该案例支持“删掉误导性理论解释可接受”，不表示rebuttal可以无界替换主工作。

**阅读范围与访问来源：** 完整rpmQ初评、作者首轮三段、reviewer二次技术反驳、删除定理回应、最终明确改分及AC。；原始OpenReview notes数据快照（有id/replyto/signatures/rating），live页面访问受验证码限制；非摘要转述

**机制标签：** `theory_repair`、`claim_scope`、`multi_round`、`paper_revision`

**复核链接：** [核心数值表态](https://openreview.net/forum?id=tCv1D3M7Lb&noteId=VRswyacvFu) · [其他关键 note 2](https://openreview.net/forum?id=tCv1D3M7Lb&noteId=s0pmQuhXsX) · [作者回复 1](https://openreview.net/forum?id=tCv1D3M7Lb&noteId=pYEvUv71eP) · [作者回复 2](https://openreview.net/forum?id=tCv1D3M7Lb&noteId=jM9zQFSzBp) · [作者回复 3](https://openreview.net/forum?id=tCv1D3M7Lb&noteId=pgzz39gS6q) · [作者回复 4](https://openreview.net/forum?id=tCv1D3M7Lb&noteId=ov127u4oEw) · [AC](https://openreview.net/forum?id=tCv1D3M7Lb&noteId=64HvM045i8) · [决定](https://openreview.net/forum?id=tCv1D3M7Lb&noteId=sGfnjVP13v) · [公开档案](https://huggingface.co/datasets/McGill-NLP/AI-For-Science-Retreat-Data/blob/main/iclr-dataset/iclr_2026_raw.parquet)

## C13

### [GPG: A Simple and Strong Reinforcement Learning Baseline for Model Reasoning](https://openreview.net/forum?id=inccdtfx8x)

**ICLR 2026 · Accept (Poster) · `core_positive`**

**记录到的变化：** gf7C 2→6；u5um 初始4；本人确认提高但未给目标（AC记为6）

**证据身份：** 本人明确数值表态；2026评分栏已回滚；数值变化仅按本人讨论表态、明确标注的作者/AC历史转述记录。

**原始阻碍：** 去critic/KL/surrogate为何稳定；是否声称通用RL；PPO→GRPO→GPG各组件作用；pass@k；DAPO先有类似sampling。

**作者动作：** 限定研究为预训练LLM的reasoning post-training，解释为何与从零学视觉控制不同。 逐组件说明normalization、debiased gradient、variance reduction及已有消融对应；补pass@3/5。 澄清与并行DAPO的关系和采样特例；根据追问把scope明确写到正文83–91行。

**评审反馈：** gf7C先认可但要求改稿才加分，作者上传明确scope后本人确认2→6；AC认可，Poster。

**选例理由：** 本人先提出改稿条件，作者写回scope后再明确确认已升6；适合教完成修订与获得确认的区别。

**可迁移机制：** 解释简单RL组件为何适用于LLM reasoning post-training，逐组件对应消融，并把范围写回指定正文位置。

**必须保留的限制：** 核心资格来自gf7C后续明确确认，不能停在此前条件句；u5um的目标6由AC补充。 大于7B未验证、严格收敛/稳定理论仍有限；u5um目标6由AC给出。

**阅读范围与访问来源：** 完整gf7C2分初评、解释、条件式提分、作者改稿、确认6、AC和decision。；原始OpenReview notes数据快照（有id/replyto/signatures/rating），live页面访问受验证码限制；非摘要转述

**机制标签：** `claim_scope`、`evaluation`、`paper_revision`、`multi_round`

**复核链接：** [核心数值表态](https://openreview.net/forum?id=inccdtfx8x&noteId=wHZtFOpZwy) · [其他关键 note 2](https://openreview.net/forum?id=inccdtfx8x&noteId=DVRANX5OXP) · [作者回复 1](https://openreview.net/forum?id=inccdtfx8x&noteId=S0VWTeI4nt) · [作者回复 2](https://openreview.net/forum?id=inccdtfx8x&noteId=kVvAMSjbSi) · [AC](https://openreview.net/forum?id=inccdtfx8x&noteId=E4KfbiBnvw) · [决定](https://openreview.net/forum?id=inccdtfx8x&noteId=i1KmAtJltl) · [公开档案](https://huggingface.co/datasets/McGill-NLP/AI-For-Science-Retreat-Data/blob/main/iclr-dataset/iclr_2026_raw.parquet)

## C14

### [MCP-SafetyBench: A Benchmark for Safety Evaluation of Large Language Models with Real-World MCP Servers](https://openreview.net/forum?id=7XYjeL46co)

**ICLR 2026 · Accept (Poster) · `extended_positive`**

**记录到的变化：** aJQS 4→6；TNH4 初始2；表态提高/支持，目标数字未知

**证据身份：** 本人明确数值表态；2026评分栏已回滚；数值变化仅按本人讨论表态、明确标注的作者/AC历史转述记录。

**原始阻碍：** MCP threat model缺现有安全框架定位；只用ReAct；未讨论防御；服务器数量、decoy、攻击budget消融欠缺。

**作者动作：** 映射CIAP目标与攻击层；明确contextual least privilege的安全定义。 补Safety Prompt、Plan-and-Execute vs ReAct、2/3/4服务器、decoy和字符/迭代budget实验及统计。

**评审反馈：** aJQS认可定位和新消融，明确4→6，仍觉得decoy零falsepositive过于简单；TNH4认可统计分析愿提分未报目标，Poster。

**选例理由：** aJQS明确4→6，威胁模型与正交消融有价值；作为benchmark安全方向扩展，与核心SCUBA和InnovatorBench互补。

**可迁移机制：** 明确攻击能力、目标与成功条件，分别检验agent策略、服务器数和攻击预算。

**必须保留的限制：** p>0.05不证明两种架构等价；decoy设置仍被认为简单；TNH4只愿提高而未给目标数字。 作者把p>0.05解读为架构不是显著因素，仅能说本实验未检测到差异。TNH4不推断2→6。

**阅读范围与访问来源：** 完整aJQS初评、三段回应、明确改分与保留意见；核对TNH4本人评论、AC和decision。；原始OpenReview notes数据快照（有id/replyto/signatures/rating），live页面访问受验证码限制；非摘要转述

**机制标签：** `benchmark_value`、`evaluation`、`claim_scope`

**复核链接：** [重点评审 note](https://openreview.net/forum?id=7XYjeL46co&noteId=yYqoQEPSGs) · [其他关键 note 2](https://openreview.net/forum?id=7XYjeL46co&noteId=U8pDb9Oy09) · [作者回复 1](https://openreview.net/forum?id=7XYjeL46co&noteId=JKWPo5OiX4) · [作者回复 2](https://openreview.net/forum?id=7XYjeL46co&noteId=FSAFEhe2cl) · [作者回复 3](https://openreview.net/forum?id=7XYjeL46co&noteId=mslZ74zROg) · [AC](https://openreview.net/forum?id=7XYjeL46co&noteId=987VZL48ZY) · [决定](https://openreview.net/forum?id=7XYjeL46co&noteId=n54l9btE9k) · [公开档案](https://huggingface.co/datasets/McGill-NLP/AI-For-Science-Retreat-Data/blob/main/iclr-dataset/iclr_2026_raw.parquet)

## C15

### [SCUBA: Salesforce Computer Use Benchmark](https://openreview.net/forum?id=bkjKnO9s7T)

**ICLR 2026 · Accept (Poster) · `core_positive`**

**记录到的变化：** YpFg 2→4→6

**证据身份：** 本人明确数值表态；2026评分栏已回滚；数值变化仅按本人讨论表态、明确标注的作者/AC历史转述记录。

**原始阻碍：** 依赖Salesforce live sandbox维护；300任务规模和admin偏斜；browser vs computer agent不公平；跨平台泛化；能否生成训练轨迹。

**作者动作：** 说明真实工作流访谈与角色工具生态、免费sandbox/付费功能的可访问性限制。 承认observation/action space不同，避免把结果当控制比较或泛化到全部平台。 第二轮给动态环境采轨迹三条路径、参数化任务模板与真实SOQL evaluator代码，解释扩容与验证难点。

**评审反馈：** 第一轮后YpFg2→4并问轨迹采集；具体模板与可实现路径后4→6，认为环境训练用途提高价值。AC保留评估side effects局限，Poster。

**选例理由：** 本人明确2→4→6；用可实现的轨迹采集与任务合成路径解释benchmark价值，适合抽象规模争议的处理。

**可迁移机制：** 说明现实性与免费可访问性的取舍，再给任务模板、扩展接口和evaluator代码片段。

**必须保留的限制：** 维护成本和对副作用的评估仍有限；第二轮被认可的是动态环境的训练/采数用途，不只是代码更多。 live benchmark维护与跨平台覆盖仍是真限制，作者没有靠rebuttal消除。

**阅读范围与访问来源：** 完整YpFg初评、三段首轮、2→4追问、两段模板/evaluator回应、4→6、AC与decision。；原始OpenReview notes数据快照（有id/replyto/signatures/rating），live页面访问受验证码限制；非摘要转述

**机制标签：** `benchmark_value`、`multi_round`、`evaluation`、`claim_scope`

**复核链接：** [核心数值表态](https://openreview.net/forum?id=bkjKnO9s7T&noteId=PPgb7XQe7O) · [重点评审 note](https://openreview.net/forum?id=bkjKnO9s7T&noteId=xgQxWovHPV) · [作者回复 1](https://openreview.net/forum?id=bkjKnO9s7T&noteId=1ICRihBcaZ) · [作者回复 2](https://openreview.net/forum?id=bkjKnO9s7T&noteId=wqhCQo0SoC) · [作者回复 3](https://openreview.net/forum?id=bkjKnO9s7T&noteId=UzLt6MAWNz) · [作者回复 4](https://openreview.net/forum?id=bkjKnO9s7T&noteId=XA1ogoGa6a) · [作者回复 5](https://openreview.net/forum?id=bkjKnO9s7T&noteId=mogTgr229R) · [AC](https://openreview.net/forum?id=bkjKnO9s7T&noteId=iUnVQlwyWn) · [决定](https://openreview.net/forum?id=bkjKnO9s7T&noteId=TbqvhUxLQa) · [公开档案](https://huggingface.co/datasets/McGill-NLP/AI-For-Science-Retreat-Data/blob/main/iclr-dataset/iclr_2026_raw.parquet)

## C16

### [Towards Safe Reasoning in Large Reasoning Models via Corrective Intervention](https://openreview.net/forum?id=2uTxLC4LmC)

**ICLR 2026 · Accept (Poster) · `qualified_positive`**

**记录到的变化：** 1hr8 2→4→6；ooTQ 4→6

**证据身份：** 本人明确数值表态；2026评分栏已回滚；数值变化仅按本人讨论表态、明确标注的作者/AC历史转述记录。

**原始阻碍：** CoT变安全会不会只是obfuscation破坏monitorability；缺Backtrack/TARS；DPO likelihood displacement；overrefusal；安全judge定义。

**作者动作：** 限定open-weight可见CoT问题；局部干预、共同prefix的偏好训练不同于全程奖励压制，承认monitorability风险开放。 补Backtrack/TARS、明确实际DPO+SFT objective、XsTest benign，区分process/response安全。 二轮在语言代理设置延长GRPO训练观察安全CoT/有害answer错配，解释主实验短预算与offline IPO的差异。

**评审反馈：** 机制说明后1hr8升4，要求更直接实验；作者补500step语言代理实验后评审升6；AC仍指出frontier-scale monitorability tradeoff未解决，Poster。

**选例理由：** 有本人2→4→6，但新增证据只是language-only proxy，与评审最初要求的agentic验证有距离；用于带边界的安全机制讨论。

**可迁移机制：** 先澄清部署场景，再将根本风险转成可做的诊断实验，并解释实验与真实场景的距离。

**必须保留的限制：** 不能把有限离线训练中未观察到obfuscation说成普遍安全保证，也不能将代理实验称为frontier长程agent实测。 新增是language-only proxy，不是真正长程工具agent或frontier实验；不能说证明永不obfuscate。

**阅读范围与访问来源：** 完整1hr8最强负评、五段首轮、2→4、机制追问、实验追问和补实验、2→6；另核对ooTQ4→6及AC。；原始OpenReview notes数据快照（有id/replyto/signatures/rating），live页面访问受验证码限制；非摘要转述

**机制标签：** `evaluation`、`multi_round`、`claim_scope`、`negative_results`

**复核链接：** [重点评审 note](https://openreview.net/forum?id=2uTxLC4LmC&noteId=463GLSs3te) · [其他关键 note 2](https://openreview.net/forum?id=2uTxLC4LmC&noteId=dmiecNWvs5) · [其他关键 note 3](https://openreview.net/forum?id=2uTxLC4LmC&noteId=SmjjnCyOqy) · [作者回复 1](https://openreview.net/forum?id=2uTxLC4LmC&noteId=4wo1CGRfNF) · [作者回复 2](https://openreview.net/forum?id=2uTxLC4LmC&noteId=XyOynsPbMl) · [作者回复 3](https://openreview.net/forum?id=2uTxLC4LmC&noteId=Tc83QF8iFw) · [作者回复 4](https://openreview.net/forum?id=2uTxLC4LmC&noteId=6WieSmbu3M) · [作者回复 5](https://openreview.net/forum?id=2uTxLC4LmC&noteId=GrwBvuxd3O) · [作者回复 6](https://openreview.net/forum?id=2uTxLC4LmC&noteId=RF1eTB3dqD) · [作者回复 7](https://openreview.net/forum?id=2uTxLC4LmC&noteId=As5HWHkj6Q) · [AC](https://openreview.net/forum?id=2uTxLC4LmC&noteId=IkgkFklkXB) · [决定](https://openreview.net/forum?id=2uTxLC4LmC&noteId=uf9sjgkIZy) · [公开档案](https://huggingface.co/datasets/McGill-NLP/AI-For-Science-Retreat-Data/blob/main/iclr-dataset/iclr_2026_raw.parquet)

## C17

### [Learning to Orchestrate Agents in Natural Language with the Conductor](https://openreview.net/forum?id=U23A2BUKYt)

**ICLR 2026 · Accept (Poster) · `core_positive`**

**记录到的变化：** TwCE 2→6

**证据身份：** 本人明确数值表态；2026评分栏已回滚；数值变化仅按本人讨论表态、明确标注的作者/AC历史转述记录。

**原始阻碍：** GRPO公式缺clip；agentic workflow定义含糊；收益可能全来自强worker；缺GPT5/Gemini直接planner；MoA配置/性能反常；成本与credit assignment不清。

**作者动作：** 写正式workflow定义、clip全式及一步优化解释；补reward如何作用完整token序列。 新加GPT5/Gemini planner共享worker池、放宽重试/token以保证baseline能力；给异质任务/子任务互补实例。 补5xconsensus/self-reflection成本控制，token/API费用与性能；说明各方法同worker pool。

**评审反馈：** TwCE认可强模型planner baseline显示训练Conductor有价值，成本问题充分回答，2→6；仍对latent capability术语与部分MoA解释保留。AC预测c7Bs4可能5/6非实际，Poster。

**选例理由：** 本人明确2→6；直接用强模型替换作者的新模块，并加入成本配平，是检验方法必要性的清晰范例。

**可迁移机制：** 让GPT-5/Gemini充当planner并共享worker；另用等轮数consensus/self-reflection对照报告token与费用。

**必须保留的限制：** 部分术语和MoA解释仍有保留；c7Bs可能转正只是AC判断，不能宣称全部竞争框架都已被彻底解释。 小AIME样本和术语仍有限；不能说所有baseline差异已完全解释。

**阅读范围与访问来源：** 完整TwCE初评、六段新增baseline/成本/定义回应、明确2→6、AC与decision。；原始OpenReview notes数据快照（有id/replyto/signatures/rating），live页面访问受验证码限制；非摘要转述

**机制标签：** `baseline_fairness`、`evaluation`、`efficiency`、`novelty`

**复核链接：** [核心数值表态](https://openreview.net/forum?id=U23A2BUKYt&noteId=R0u45YQc2S) · [作者回复 1](https://openreview.net/forum?id=U23A2BUKYt&noteId=K42vFlDHub) · [作者回复 2](https://openreview.net/forum?id=U23A2BUKYt&noteId=85kHWNcAju) · [作者回复 3](https://openreview.net/forum?id=U23A2BUKYt&noteId=GYXKvLLd2T) · [作者回复 4](https://openreview.net/forum?id=U23A2BUKYt&noteId=J6jTlHqwFA) · [作者回复 5](https://openreview.net/forum?id=U23A2BUKYt&noteId=8cjgnDr7xD) · [作者回复 6](https://openreview.net/forum?id=U23A2BUKYt&noteId=nZWC4HkpEM) · [AC](https://openreview.net/forum?id=U23A2BUKYt&noteId=DouxKBeSOa) · [决定](https://openreview.net/forum?id=U23A2BUKYt&noteId=yoqZZjPrmg) · [公开档案](https://huggingface.co/datasets/McGill-NLP/AI-For-Science-Retreat-Data/blob/main/iclr-dataset/iclr_2026_raw.parquet)

## C18

### [Softmax Transformers are Turing-Complete](https://openreview.net/forum?id=FdkPOHlChS)

**ICLR 2026 · Accept (Oral) · `core_positive`**

**记录到的变化：** b98p 2→6；rteb 4→6；DApH 6→8

**证据身份：** 本人明确数值表态；2026评分栏已回滚；数值变化仅按本人讨论表态、明确标注的作者/AC历史转述记录。

**原始阻碍：** 部分语言的Turing-completeness是否达主张；hardattention可逼近为何softmax非平凡；依赖前作过重；trainability含糊；实验细节欠缺。

**作者动作：** 指出主Theorem4.3覆盖recursively enumerable languages，中间命题只覆盖特定子类，重写定理表达。 区分表达性与learnability/length generalization；说明trainability指理想化训练算法的长度泛化。 补Huang框架primer、RPE背景、与前作技术差异、完整task/architecture/loss/dataset设置；后续把关联讨论写入Conclusion。

**评审反馈：** b98p2→6；rteb4→6但仍要求正文关联讨论，作者继续修改；DApH6→8；PWUm维持10。AC核实提分意向并提到score按钮问题，最终Oral。

**选例理由：** 本人2→6、4→6、6→8均可定位；把主定理、中间命题、理想化trainability与前作关系讲清楚，最终Oral。

**可迁移机制：** 明确每个命题的对象与假设，给前作背景和新技术对应表，补完整实验定义与设置。

**必须保留的限制：** trainability不等于普通SGD必然训练成功；Oral不是写作技巧的因果证明。 trainability不是常规SGD一定训练成功的普遍保证；只按论文/回应的理想化定义。

**阅读范围与访问来源：** 完整b98p和rteb初评/作者回应/后续改稿；核对DApH本人提分、AC和Oral决定。；原始OpenReview notes数据快照（有id/replyto/signatures/rating），live页面访问受验证码限制；非摘要转述

**机制标签：** `theory_repair`、`novelty`、`related_work`、`paper_revision`

**复核链接：** [核心数值表态](https://openreview.net/forum?id=FdkPOHlChS&noteId=l4fwsSOLl8) · [其他关键 note 2](https://openreview.net/forum?id=FdkPOHlChS&noteId=1ueD2YhH9n) · [其他关键 note 3](https://openreview.net/forum?id=FdkPOHlChS&noteId=FPPuCufS82) · [作者回复 1](https://openreview.net/forum?id=FdkPOHlChS&noteId=zd0mkK3cK8) · [作者回复 2](https://openreview.net/forum?id=FdkPOHlChS&noteId=wze1bppSrU) · [作者回复 3](https://openreview.net/forum?id=FdkPOHlChS&noteId=jt8dfnCpRF) · [AC](https://openreview.net/forum?id=FdkPOHlChS&noteId=fnV5UVObiS) · [决定](https://openreview.net/forum?id=FdkPOHlChS&noteId=HkKz1e63Xh) · [公开档案](https://huggingface.co/datasets/McGill-NLP/AI-For-Science-Retreat-Data/blob/main/iclr-dataset/iclr_2026_raw.parquet)

## C19

### [InnovatorBench: Evaluating Agents’ Ability to Conduct Innovative AI Research](https://openreview.net/forum?id=w8rZ2Jd6Jo)

**ICLR 2026 · Accept (Poster) · `core_positive`**

**记录到的变化：** kpnh 2→6

**证据身份：** 本人明确数值表态；2026评分栏已回滚；数值变化仅按本人讨论表态、明确标注的作者/AC历史转述记录。

**原始阻碍：** 20任务跨6类太少；8x80GB成本高；任务内容不透明；缺轻量open-source模型；标题AI Research泛化过强。

**作者动作：** 发布任务描述，解释ResearchGym多节点/异步/snapshot平台贡献。 首轮以工作量和前沿价值辩护仍未说服；第二轮把AI Research收窄为LLM Research。 按照要求精确补Qwen3-32B零分结果和配置/上下文总结失败解释，而非因零分省略。

**评审反馈：** kpnh初评称讨论期不会改，首轮仍拒；标题收窄后给有条件6，结果补齐后本人2→6。任务数疑虑明确仍保留；AC却概括all concerns addressed，记录以评审原文为准。Poster。

**选例理由：** 评审初称不会改分，最终明确2→6；标题收窄和如实报告零分结果是可迁移的benchmark诚信范例。

**可迁移机制：** 区分平台贡献与任务范围，按证据收窄标题，报告失败模型的精确配置和零结果。

**必须保留的限制：** 任务规模异议仍保留；不能把AC的all concerns addressed覆盖本人保留，也不建议复制早期关于资源的泛泛辩护。 没有补到20任务/类；小规模统计可靠性问题仍在；不建议模仿作者有关资源可得性的泛泛辩护。

**阅读范围与访问来源：** 完整kpnh初评、首轮作者双帖、保持拒绝追问、scope修正、条件式提分、零分结果、明确6及AC。；原始OpenReview notes数据快照（有id/replyto/signatures/rating），live页面访问受验证码限制；非摘要转述

**机制标签：** `benchmark_value`、`claim_scope`、`negative_results`、`multi_round`

**复核链接：** [核心数值表态](https://openreview.net/forum?id=w8rZ2Jd6Jo&noteId=MlSsFU2LBn) · [作者回复 1](https://openreview.net/forum?id=w8rZ2Jd6Jo&noteId=ZGddX6Wyc4) · [作者回复 2](https://openreview.net/forum?id=w8rZ2Jd6Jo&noteId=xfZxutqRBY) · [作者回复 3](https://openreview.net/forum?id=w8rZ2Jd6Jo&noteId=CjGGawf4w1) · [作者回复 4](https://openreview.net/forum?id=w8rZ2Jd6Jo&noteId=nfsgjprc79) · [AC](https://openreview.net/forum?id=w8rZ2Jd6Jo&noteId=QYCtLP30Ih) · [决定](https://openreview.net/forum?id=w8rZ2Jd6Jo&noteId=cc20XvnWhm) · [公开档案](https://huggingface.co/datasets/McGill-NLP/AI-For-Science-Retreat-Data/blob/main/iclr-dataset/iclr_2026_raw.parquet)

## C20

### [Semantic Voting: A Self-Evaluation-Free Approach for Efficient LLM Self-Improvement on Unverifiable Open-ended Tasks](https://openreview.net/forum?id=7AlPbFkcs3)

**ICLR 2026 · Accept (Poster) · `extended_positive`**

**记录到的变化：** ikCz 2→6；jSCx 4→6（目标数字由AC给出）

**证据身份：** 本人明确数值表态；2026评分栏已回滚；数值变化仅按本人讨论表态、明确标注的作者/AC历史转述记录。

**原始阻碍：** 技术简单/聚类无普适必要；相关工作、图标与loss呈现；HDBSCAN与参数；仅翻译摘要；GRPO波动；embedding依赖与conformity bias。

**作者动作：** 定位已存在的OPTICS/MeanShift消融和图例，解释数据流顺序与章节顺序不同、标准DPO式帮助可读性。 补CNN/DM参数网格和AlpacaEval开放任务；解释强模型可去聚类，聚类为弱模型稳定性而设。 将连续语义reward离散为1–5档，报告方差降低；承认一致性偏差和embedding依赖仍有限。

**评审反馈：** ikCz2→6；jSCx本人说提高但目标6来自AC；AC仍保留conformity bias、longform与主观任务、人评不足，Poster。

**选例理由：** 本人2→6可确认，模块适用性与降低reward方差的实验有补充价值；核心机制与scope/消融案例重复，作为扩展阅读。

**可迁移机制：** 定位原稿已存在的信息，对真实缺口补新任务、参数网格和连续/离散reward方差对照。

**必须保留的限制：** 回复有防御性措辞，不能因接收便模仿；jSCx目标6由AC给出；conformity bias未解决。 作者语气有防御性，不能据此推断强硬语气促进接收；无直接人类研究与偏差仍在。

**阅读范围与访问来源：** 完整ikCz长初评14问、三段作者回应、本人明确6；核对jSCx原话和AC。；原始OpenReview notes数据快照（有id/replyto/signatures/rating），live页面访问受验证码限制；非摘要转述

**机制标签：** `evaluation`、`claim_scope`、`negative_results`

**复核链接：** [重点评审 note](https://openreview.net/forum?id=7AlPbFkcs3&noteId=hFwrhPH9Ks) · [其他关键 note 2](https://openreview.net/forum?id=7AlPbFkcs3&noteId=qb3TMzA8MU) · [作者回复 1](https://openreview.net/forum?id=7AlPbFkcs3&noteId=1cBVHt4nT1) · [作者回复 2](https://openreview.net/forum?id=7AlPbFkcs3&noteId=r5jEyY42Zi) · [作者回复 3](https://openreview.net/forum?id=7AlPbFkcs3&noteId=dAYfwIZMDC) · [AC](https://openreview.net/forum?id=7AlPbFkcs3&noteId=Nw43dPS1GF) · [决定](https://openreview.net/forum?id=7AlPbFkcs3&noteId=ek3rWxPm9P) · [公开档案](https://huggingface.co/datasets/McGill-NLP/AI-For-Science-Retreat-Data/blob/main/iclr-dataset/iclr_2026_raw.parquet)

## C21

### [PEERING INTO THE UNKNOWN: ACTIVE VIEW SELECTION WITH NEURAL UNCERTAINTY MAPS FOR 3D RECONSTRUCTION](https://openreview.net/forum?id=e7gbgdw05A)

**ICLR 2026 · Accept (Poster) · `extended_positive`**

**记录到的变化：** Wvnw 4→8（本人 willing；AC 确认）；另 yuxC 4→6（AC 记录）

**证据身份：** 本人提分承诺；AC确认历史；2026官方回滚后的原review rating不是讨论后分数。这里before取原review字段，after仅取本人讨论承诺/已改分陈述或AC明确历史记录，绝不以AC预测代替实改。

**原始阻碍：** 主动选视角的实际价值不清：离线数据不缺视角；担心优点只来自弱重建后端；相机偏离物体中心及不可达视角未检验。

**作者动作：** 把实际预算明确为观测、运动和电池成本；保持重建后端与超参数一致；补全视角上界及更强 Binocular3DGS 后端比较；增加偏离中心的定量实验，并坦承大偏移限制。

**评审反馈：** 评审明确指出更强后端实验直接解决核心疑虑，偏心相机的限制分析有价值，承诺由4升8。AC 采纳该历史变化，但仍保留离线成本与自由空间泛化限制。

**选例理由：** 本人明确愿4→8、AC回顾支持，强后端替换很有判别力；与核心强baseline案例重复，保留为主动视觉扩展。

**可迁移机制：** 先定义观测/运动成本，再固定重建后端比较、换更强后端并测试偏心相机。

**必须保留的限制：** willing是公开意愿，不能称评分栏保存为8；大偏移与自由空间泛化限制保留。 2026官方回滚后的原review rating不是讨论后分数。这里before取原review字段，after仅取本人讨论承诺/已改分陈述或AC明确历史记录，绝不以AC预测代替实改。

**阅读范围与访问来源：** 逐条读完整关键评审主链及AC；未声称逐句精读其他无关支线。原网页受验证限制，以保留noteId/replyto/签名/时间的公开原始记录存档辅助读取。；公开 OpenReview 原始记录的匿名存档；非自动生成摘要

**机制标签：** `baseline_fairness`、`efficiency`、`evaluation`、`claim_scope`

**复核链接：** [重点评审 note](https://openreview.net/forum?id=e7gbgdw05A&noteId=7xyZuVNFUM) · [作者回复 1](https://openreview.net/forum?id=e7gbgdw05A&noteId=rx6BVJe4UA) · [作者回复 2](https://openreview.net/forum?id=e7gbgdw05A&noteId=D51NTXfVV4) · [AC](https://openreview.net/forum?id=e7gbgdw05A&noteId=PzfV8PkQLb) · [决定](https://openreview.net/forum?id=e7gbgdw05A&noteId=ozaGbN9TDt) · [公开档案](https://huggingface.co/datasets/McGill-NLP/AI-For-Science-Retreat-Data/blob/main/iclr-dataset/iclr_2026_raw.parquet)

## C22

### [Triangle Multiplication is All You Need for Biomolecular Structure Representations](https://openreview.net/forum?id=CrXcfMLR9q)

**ICLR 2026 · Accept (Poster) · `extended_positive`**

**记录到的变化：** J8sg 4→6（承诺，明确未能编辑）；qqDT 4→6；GgDp 2→4仍反对

**证据身份：** 本人提分承诺；AC确认历史；2026官方回滚后的原review rating不是讨论后分数。这里before取原review字段，after仅取本人讨论承诺/已改分陈述或AC明确历史记录，绝不以AC预测代替实改。

**原始阻碍：** 去掉 triangle attention 似乎只是工程简化，方法新颖性不足，是否值得机器学习会议发表。

**作者动作：** 精确区分先前模型与大规模 Pairformer 场景；增加 Section F 的稀疏长程几何交互机制分析、sequence track 消融，以及抗体、核酸等任务检验。

**评审反馈：** J8sg 点名机制分析让文章超越技术报告，愿4→6，但明确审稿编辑截止，留言供 AC 参考。AC 将有效意见综合为6/6/6/4，接受；最低分评审仍不认为技术贡献足够。

**选例理由：** 本人明确4→6承诺且解释编辑关闭；机制分析使工程简化的价值变清楚，可补充结构简化题材。

**可迁移机制：** 区分大规模使用场景，提供sequence track消融和几何机制分析，而非包装已有组件为新算子。

**必须保留的限制：** 评审明确未能编辑评分；另一个2分评审只到4且仍反对，不能称全员转正。 2026官方回滚后的原review rating不是讨论后分数。这里before取原review字段，after仅取本人讨论承诺/已改分陈述或AC明确历史记录，绝不以AC预测代替实改。

**阅读范围与访问来源：** 逐条读完整关键评审主链及AC；未声称逐句精读其他无关支线。原网页受验证限制，以保留noteId/replyto/签名/时间的公开原始记录存档辅助读取。；公开 OpenReview 原始记录的匿名存档；非自动生成摘要

**机制标签：** `novelty`、`evaluation`、`claim_scope`

**复核链接：** [重点评审 note](https://openreview.net/forum?id=CrXcfMLR9q&noteId=Kq0Zg9XRM1) · [作者回复 1](https://openreview.net/forum?id=CrXcfMLR9q&noteId=nSfaKKmqRt) · [AC](https://openreview.net/forum?id=CrXcfMLR9q&noteId=Vtu5YntMdN) · [决定](https://openreview.net/forum?id=CrXcfMLR9q&noteId=wh3tPmYv0x) · [公开档案](https://huggingface.co/datasets/McGill-NLP/AI-For-Science-Retreat-Data/blob/main/iclr-dataset/iclr_2026_raw.parquet)

## C23

### [Taming Score-Based Denoisers in ADMM: A Convergent Plug-and-Play Framework](https://openreview.net/forum?id=BiXwSIIMIq)

**ICLR 2026 · Accept (Poster) · `core_positive`**

**记录到的变化：** srVv 4→6（已改）；JtYg 4→6（已改）

**证据身份：** 本人明确数值表态；2026官方回滚后的原review rating不是讨论后分数。这里before取原review字段，after仅取本人讨论承诺/已改分陈述或AC明确历史记录，绝不以AC预测代替实改。

**原始阻碍：** 随机 denoiser 被当成确定性；Langevin 必须平稳分布的假设不现实；理论算法与有限步实现不一致，固定点与目标驻点概念混用。

**作者动作：** 用逐步高概率事件和 union bound 处理随机性；承认平稳假设过强，新增固定有限 J 步 Langevin 分析及误差项；分开强凸与非凸结论；后续纠正对既有 PnP 驻点工作的错误概括。

**评审反馈：** srVv 特别认可去掉不现实平稳性假设，并明确4→6；继续要求补全前人工作，作者随后接受并改稿。

**选例理由：** 本人明确已4→6；从不现实平稳假设修到有限步算法的保证，适合理论—实现一致性教学。

**可迁移机制：** 以实际运行的有限J步为分析对象，显式保留随机性和误差项，区分凸与非凸结论。

**必须保留的限制：** 提分后仍有相关工作纠错需求；高概率保证的事件和union bound条件不能省略。 2026官方回滚后的原review rating不是讨论后分数。这里before取原review字段，after仅取本人讨论承诺/已改分陈述或AC明确历史记录，绝不以AC预测代替实改。

**阅读范围与访问来源：** 逐条读完整关键评审主链及AC；未声称逐句精读其他无关支线。原网页受验证限制，以保留noteId/replyto/签名/时间的公开原始记录存档辅助读取。；公开 OpenReview 原始记录的匿名存档；非自动生成摘要

**机制标签：** `theory_repair`、`claim_scope`、`related_work`、`paper_revision`

**复核链接：** [核心数值表态](https://openreview.net/forum?id=BiXwSIIMIq&noteId=ajh21lnVqs) · [作者回复 1](https://openreview.net/forum?id=BiXwSIIMIq&noteId=rcP00y9UGz) · [作者回复 2](https://openreview.net/forum?id=BiXwSIIMIq&noteId=kSlcuzF8BP) · [AC](https://openreview.net/forum?id=BiXwSIIMIq&noteId=xC9JQrcLQs) · [决定](https://openreview.net/forum?id=BiXwSIIMIq&noteId=s3SgQ3mUBv) · [公开档案](https://huggingface.co/datasets/McGill-NLP/AI-For-Science-Retreat-Data/blob/main/iclr-dataset/iclr_2026_raw.parquet)

## C24

### [MOSAIC: Multi-Subject Personalized Generation via Correspondence-Aware Alignment and Disentanglement](https://openreview.net/forum?id=7AH0y1OtnC)

**ICLR 2026 · Accept (Poster) · `extended_positive`**

**记录到的变化：** cdZj 4→6（承诺，编辑关闭）；AC 记录另一个4转6

**证据身份：** 本人提分承诺；AC确认历史；2026官方回滚后的原review rating不是讨论后分数。这里before取原review字段，after仅取本人讨论承诺/已改分陈述或AC明确历史记录，绝不以AC预测代替实改。

**原始阻碍：** 数据集统计与外部泛化不清；两个损失缺独立消融；与 FastComposer、OrthogonalAdapt 的区别不清；忠实度是否以多样性为代价。

**作者动作：** 分 W1–W5 对应回答：补数据分布与标注流程；完整2×2损失消融；说明自动对应点和抽检；补外部数据集、10随机种子 LPIPS 多样性；将关键解释移入正文。

**评审反馈：** cdZj 承认此前漏看图注，新增细节解决了所有疑虑；先表态接受，再因编辑关闭留下明确4→6承诺。AC 综合为6/6/6/4并接受。

**选例理由：** 本人明确4→6承诺，2×2消融、外部分布与多样性证据完整；作为视觉生成数据/组件问题的扩展。

**可迁移机制：** 分别验证两个损失的独立和联合作用，披露标注流程，并用多种子评估忠实度—多样性。

**必须保留的限制：** 系统关闭未能编辑；指出漏看图注时同时改善展示，不可仅以“原文已有”结束回应。 2026官方回滚后的原review rating不是讨论后分数。这里before取原review字段，after仅取本人讨论承诺/已改分陈述或AC明确历史记录，绝不以AC预测代替实改。

**阅读范围与访问来源：** 逐条读完整关键评审主链及AC；未声称逐句精读其他无关支线。原网页受验证限制，以保留noteId/replyto/签名/时间的公开原始记录存档辅助读取。；公开 OpenReview 原始记录的匿名存档；非自动生成摘要

**机制标签：** `evaluation`、`benchmark_value`、`paper_revision`

**复核链接：** [重点评审 note](https://openreview.net/forum?id=7AH0y1OtnC&noteId=DQlg1bQkHU) · [作者回复 1](https://openreview.net/forum?id=7AH0y1OtnC&noteId=j85fHRs3vh) · [作者回复 2](https://openreview.net/forum?id=7AH0y1OtnC&noteId=aav8DCDIH5) · [作者回复 3](https://openreview.net/forum?id=7AH0y1OtnC&noteId=kf9570Bavb) · [作者回复 4](https://openreview.net/forum?id=7AH0y1OtnC&noteId=kqRvBsAWYO) · [作者回复 5](https://openreview.net/forum?id=7AH0y1OtnC&noteId=cy6HhW4Kku) · [作者回复 6](https://openreview.net/forum?id=7AH0y1OtnC&noteId=c5lOWzDxI7) · [AC](https://openreview.net/forum?id=7AH0y1OtnC&noteId=V7Za3FCgfG) · [决定](https://openreview.net/forum?id=7AH0y1OtnC&noteId=4VDqG7I77m) · [公开档案](https://huggingface.co/datasets/McGill-NLP/AI-For-Science-Retreat-Data/blob/main/iclr-dataset/iclr_2026_raw.parquet)

## C25

### [FACT: Fine-grained Across-variable Convolution for Multivariate Time Series Forecasting](https://openreview.net/forum?id=j3gNYqrHtl)

**ICLR 2026 · Accept (Poster) · `core_positive`**

**记录到的变化：** 5JYU 4→6（已改）；AC 记录4AVh 6→8

**证据身份：** 本人明确数值表态；2026官方回滚后的原review rating不是讨论后分数。这里before取原review字段，after仅取本人讨论承诺/已改分陈述或AC明确历史记录，绝不以AC预测代替实改。

**原始阻碍：** 平均预测窗口可能掩盖失败；任意变量重排成二维后的邻接关系可疑；“变量无固有顺序”及动态依赖主张过宽，超参数可能过拟合。

**作者动作：** 新增特定远期时间点而非仅均值的结果；测随机变量排列及多种二维布局；改成方法不要求先验顺序；补层数敏感性与默认值；精确比较 DeformTST 等近邻工作。

**评审反馈：** 目标评审对整轮修订明确4→6；AC 认为疑虑大部分解除，其他评审也有提分或意向。

**选例理由：** 本人明确已4→6；把平均指标、任意变量顺序与参数敏感性转成直接反驳实验，机制简明且跨领域可用。

**可迁移机制：** 报告具体预测时点，随机重排变量、改变布局，并给参数网格和默认值。

**必须保留的限制：** 证据只支持方法不要求先验顺序，不支持变量绝无真实结构；总体提分不能抹掉其他评审保留。 2026官方回滚后的原review rating不是讨论后分数。这里before取原review字段，after仅取本人讨论承诺/已改分陈述或AC明确历史记录，绝不以AC预测代替实改。

**阅读范围与访问来源：** 逐条读完整关键评审主链及AC；未声称逐句精读其他无关支线。原网页受验证限制，以保留noteId/replyto/签名/时间的公开原始记录存档辅助读取。；公开 OpenReview 原始记录的匿名存档；非自动生成摘要

**机制标签：** `evaluation`、`claim_scope`、`baseline_fairness`

**复核链接：** [核心数值表态](https://openreview.net/forum?id=j3gNYqrHtl&noteId=5wbsraNdEs) · [作者回复 1](https://openreview.net/forum?id=j3gNYqrHtl&noteId=B3jyOj0QRt) · [作者回复 2](https://openreview.net/forum?id=j3gNYqrHtl&noteId=OeHyhQEPIL) · [作者回复 3](https://openreview.net/forum?id=j3gNYqrHtl&noteId=yb5ntA65U0) · [作者回复 4](https://openreview.net/forum?id=j3gNYqrHtl&noteId=AkcaC8JSvK) · [AC](https://openreview.net/forum?id=j3gNYqrHtl&noteId=lpaA7XFMKH) · [决定](https://openreview.net/forum?id=j3gNYqrHtl&noteId=UWAyPEXaz4) · [公开档案](https://huggingface.co/datasets/McGill-NLP/AI-For-Science-Retreat-Data/blob/main/iclr-dataset/iclr_2026_raw.parquet)

## C26

### [Atomic HINs: Entity-Attribute Duality for Heterogeneous Graph Modeling](https://openreview.net/forum?id=AG7fjg5azU)

**ICLR 2026 · Accept (Poster) · `core_positive`**

**记录到的变化：** 8dUP 4→6（已改）；eaMx 6→8；另两位4→5仅AC推测

**证据身份：** 本人明确数值表态；2026官方回滚后的原review rating不是讨论后分数。这里before取原review字段，after仅取本人讨论承诺/已改分陈述或AC明确历史记录，绝不以AC预测代替实改。

**原始阻碍：** 遗传搜索代价可能很高；找出的图结构是否绑死特定后端；数值属性转节点是否造成全图稠密化。

**作者动作：** 报告每 trial 的真实秒数、总预算与一次离线搜索后可复用的成本；指出同一 schema 跨 sRGCN、SimpleHGN、PSHGCN 的结果；明确属性维度节点与加权边构造，仅局部星状连接。

**评审反馈：** 8dUP 在详细回复后明确4→6，并要求纳入正文。AC 接受，但另外两位可能升至5是推测，不能记作实改。

**选例理由：** 本人明确已4→6并要求纳入正文；真实秒数、摊销与跨后端复用能把工程可行性疑虑变为可检查账单。

**可迁移机制：** 报告每trial和总预算、一次搜索后的复用成本；用图构造和跨后端验证说明复杂度。

**必须保留的限制：** 另外两位4→5只是AC推测；离线摊销成立须说明部署复用次数和条件。 2026官方回滚后的原review rating不是讨论后分数。这里before取原review字段，after仅取本人讨论承诺/已改分陈述或AC明确历史记录，绝不以AC预测代替实改。

**阅读范围与访问来源：** 逐条读完整关键评审主链及AC；未声称逐句精读其他无关支线。原网页受验证限制，以保留noteId/replyto/签名/时间的公开原始记录存档辅助读取。；公开 OpenReview 原始记录的匿名存档；非自动生成摘要

**机制标签：** `efficiency`、`evaluation`、`paper_revision`

**复核链接：** [核心数值表态](https://openreview.net/forum?id=AG7fjg5azU&noteId=BDmE1pBu9v) · [作者回复 1](https://openreview.net/forum?id=AG7fjg5azU&noteId=3nu0AAQ7Q0) · [AC](https://openreview.net/forum?id=AG7fjg5azU&noteId=Hd6T0WBXHk) · [决定](https://openreview.net/forum?id=AG7fjg5azU&noteId=Xg03nz2YOl) · [公开档案](https://huggingface.co/datasets/McGill-NLP/AI-For-Science-Retreat-Data/blob/main/iclr-dataset/iclr_2026_raw.parquet)

## C27

### [Sublinear Time Quantum Algorithm for Attention Approximation](https://openreview.net/forum?id=0zIcPe4CtY)

**ICLR 2026 · Accept (Poster) · `qualified_positive`**

**记录到的变化：** zcdq 4→8（已改）

**证据身份：** 本人明确数值表态；2026官方回滚后的原review rating不是讨论后分数。这里before取原review字段，after仅取本人讨论承诺/已改分陈述或AC明确历史记录，绝不以AC预测代替实改。

**原始阻碍：** QRAM 有限精度输入与精确求逆分析不匹配；隐藏范数与条件数可能破坏次线性复杂度；如何次线性估计所需量不清。

**作者动作：** 多轮逐步修正：改误差保证及经典子程序代价，补有限精度 Appendix F；评审继续追问条件数获取后，作者给出子空间嵌入的小矩阵估计方案，补齐位复杂度。

**评审反馈：** 评审先认可经典子程序分析完整，再明确4→8并强烈支持接收；同时批评原稿不够成熟、rebuttal 改动过大，警告未来可能因此拒稿。

**选例理由：** 4→8是本人明确且可信的历史变化，但评审同时批评原稿不成熟、修订过大；保留为高级证明修复辅例，不作默认提交策略。

**可迁移机制：** 沿位复杂度、条件数估计和经典子程序代价逐环节修补，针对最新追问给实际可执行方案。

**必须保留的限制：** “猛提分”不能抵消原稿完成度警告；只借鉴修复过程，不模仿把重大理论缺口留到rebuttal。 2026官方回滚后的原review rating不是讨论后分数。这里before取原review字段，after仅取本人讨论承诺/已改分陈述或AC明确历史记录，绝不以AC预测代替实改。

**阅读范围与访问来源：** 逐条读完整关键评审主链及AC；未声称逐句精读其他无关支线。原网页受验证限制，以保留noteId/replyto/签名/时间的公开原始记录存档辅助读取。；公开 OpenReview 原始记录的匿名存档；非自动生成摘要

**机制标签：** `theory_repair`、`multi_round`、`paper_revision`

**复核链接：** [重点评审 note](https://openreview.net/forum?id=0zIcPe4CtY&noteId=RhSckfziEE) · [作者回复 1](https://openreview.net/forum?id=0zIcPe4CtY&noteId=R2JB0fqMAI) · [作者回复 2](https://openreview.net/forum?id=0zIcPe4CtY&noteId=JUemtg6TCZ) · [作者回复 3](https://openreview.net/forum?id=0zIcPe4CtY&noteId=tNfB3hoIy2) · [作者回复 4](https://openreview.net/forum?id=0zIcPe4CtY&noteId=kwnRwQZXxe) · [AC](https://openreview.net/forum?id=0zIcPe4CtY&noteId=RliDJMYTCl) · [决定](https://openreview.net/forum?id=0zIcPe4CtY&noteId=1aiCuJOBx6) · [公开档案](https://huggingface.co/datasets/McGill-NLP/AI-For-Science-Retreat-Data/blob/main/iclr-dataset/iclr_2026_raw.parquet)

## C28

### [LCA: Local Classifier Alignment for Continual Learning](https://openreview.net/forum?id=3uINmRldVW)

**ICLR 2026 · Accept (Poster) · `core_positive`**

**记录到的变化：** 7fmM 4→6（明确）；其他评审会提高仅AC推测

**证据身份：** 本人明确数值表态；2026官方回滚后的原review rating不是讨论后分数。这里before取原review字段，after仅取本人讨论承诺/已改分陈述或AC明确历史记录，绝不以AC预测代替实改。

**原始阻碍：** 最初是鲁棒损失消融和理论分布假设，随后聚焦 IM 组件只是 MagMAX 风格合并，整套方法可能仅是拼装。

**作者动作：** 补 λ=0 及将 LCA 加至已有框架的消融，补分布漂移理论；第二轮辩护仍未说服后，第三轮明确承认 IM 是已有方法的直接适配，不再主张其独立新颖性，重写贡献层次为 LCA 损失、理论和有效组合。

**评审反馈：** 评审先明确拒绝“应用到PEFT就是新颖性”的论点；作者收窄贡献后，评审认可新的贡献概括并由4升6。

**选例理由：** 本人明确4→6；作者第三轮承认辅助组件是既有方法适配后重写贡献，适合新颖性争议。

**可迁移机制：** 把独立新贡献、已有工具和有效组合分层列出，用loss消融和理论支撑主要贡献。

**必须保留的限制：** 不能把任何承认已有工作都解释为足以接收；本例仍有LCA损失、理论及组合证据。 2026官方回滚后的原review rating不是讨论后分数。这里before取原review字段，after仅取本人讨论承诺/已改分陈述或AC明确历史记录，绝不以AC预测代替实改。

**阅读范围与访问来源：** 逐条读完整关键评审主链及AC；未声称逐句精读其他无关支线。原网页受验证限制，以保留noteId/replyto/签名/时间的公开原始记录存档辅助读取。；公开 OpenReview 原始记录的匿名存档；非自动生成摘要

**机制标签：** `novelty`、`related_work`、`multi_round`、`claim_scope`

**复核链接：** [核心数值表态](https://openreview.net/forum?id=3uINmRldVW&noteId=yxNHvwiq0P) · [作者回复 1](https://openreview.net/forum?id=3uINmRldVW&noteId=d2PaJOV1RA) · [作者回复 2](https://openreview.net/forum?id=3uINmRldVW&noteId=MMG6zZs6DF) · [作者回复 3](https://openreview.net/forum?id=3uINmRldVW&noteId=yDlbZYGp2i) · [AC](https://openreview.net/forum?id=3uINmRldVW&noteId=Wx2XB6mda3) · [决定](https://openreview.net/forum?id=3uINmRldVW&noteId=ACn36ijC8A) · [公开档案](https://huggingface.co/datasets/McGill-NLP/AI-For-Science-Retreat-Data/blob/main/iclr-dataset/iclr_2026_raw.parquet)

## C29

### [Learning to Segment for Vehicle Routing Problems](https://openreview.net/forum?id=pN261iTKvr)

**ICLR 2026 · Accept (Oral) · `extended_positive`**

**记录到的变化：** Kw4B 4→6（承诺）；SSqq 6→8（AC 记录）；最终 Oral

**证据身份：** 本人提分承诺；AC确认历史；2026官方回滚后的原review rating不是讨论后分数。这里before取原review字段，after仅取本人讨论承诺/已改分陈述或AC明确历史记录，绝不以AC预测代替实改。

**原始阻碍：** 似乎是 ML-LNS 变体；定理只保证单调改进；启发式求解器产生的稳定性标签是否可信。

**作者动作：** 明确全局边稳定性和超节点压缩与局部 LNS 的差异及互补关系；在最接近基线之上加方法并做同预算比较；补标签随搜索预算、多随机种子的收敛与噪声 oracle 实验；解释 VRPTW 可行性证明的非平凡性。

**评审反馈：** Kw4B 承认误解了可行性与 ML-LNS 的关系，愿4→6；仍认为稳定性可学习的理论值得未来研究。AC 结合贡献、修订和各方支持推荐 Oral。

**选例理由：** 本人无条件宣布4→6且最终Oral；最近邻方法上的叠加实验和标签可靠性分析可作组合方法扩展。

**可迁移机制：** 将方法加入最接近baseline并配平预算，用多种子/搜索预算/噪声oracle检验标签稳定性。

**必须保留的限制：** 本人承诺不等于当前评分栏；标签稳定不等于稳定性可学习的理论已经证明。 2026官方回滚后的原review rating不是讨论后分数。这里before取原review字段，after仅取本人讨论承诺/已改分陈述或AC明确历史记录，绝不以AC预测代替实改。

**阅读范围与访问来源：** 逐条读完整关键评审主链及AC；未声称逐句精读其他无关支线。原网页受验证限制，以保留noteId/replyto/签名/时间的公开原始记录存档辅助读取。；公开 OpenReview 原始记录的匿名存档；非自动生成摘要

**机制标签：** `novelty`、`baseline_fairness`、`evaluation`、`claim_scope`

**复核链接：** [重点评审 note](https://openreview.net/forum?id=pN261iTKvr&noteId=g7ihOdcQhb) · [作者回复 1](https://openreview.net/forum?id=pN261iTKvr&noteId=ScLJNg9TT7) · [作者回复 2](https://openreview.net/forum?id=pN261iTKvr&noteId=g03Zyw6UuO) · [作者回复 3](https://openreview.net/forum?id=pN261iTKvr&noteId=4Tj4Kw33vc) · [作者回复 4](https://openreview.net/forum?id=pN261iTKvr&noteId=LZ11DtH7kj) · [AC](https://openreview.net/forum?id=pN261iTKvr&noteId=We9Xo1pOmG) · [决定](https://openreview.net/forum?id=pN261iTKvr&noteId=GQ6L1gF31V) · [公开档案](https://huggingface.co/datasets/McGill-NLP/AI-For-Science-Retreat-Data/blob/main/iclr-dataset/iclr_2026_raw.parquet)

## C30

### [LoRA meets Riemannion: Muon Optimizer for Parametrization-independent Low-Rank Adapters](https://openreview.net/forum?id=WtbXgc9GVA)

**ICLR 2026 · Accept (Poster) · `extended_positive`**

**记录到的变化：** h8Wt 4→6；另一位52qu仍2

**证据身份：** 本人明确数值表态；2026官方回滚后的原review rating不是讨论后分数。这里before取原review字段，after仅取本人讨论承诺/已改分陈述或AC明确历史记录，绝不以AC预测代替实改。

**原始阻碍：** 更新项任意缩放是否造成梯度爆炸；非零初始化是否破坏预训练权重；缺经典低秩问题验证。

**作者动作：** 展示 W−ΔW+ΔW 的 smart-zero 初始化保持有效参数不变；说明缩放不改变切空间与投影算子；重设基矩阵仍保持初始函数；补经典低秩近似实验。

**评审反馈：** h8Wt 认为数学疑虑解除，明确4→6，只剩记号小问题；AC 接受，尽管另一个强拒评审仍不支持。

**选例理由：** 本人明确4→6；短不变量等式与最小经典问题验证具有示范性，作为简洁数学澄清扩展。

**可迁移机制：** 展示smart-zero前后有效权重不变、缩放不改投影空间，并用低秩近似例子检验。

**必须保留的限制：** 另一位评审仍2；不要为使全员看似满意而隐去异议，也不能用初始化不变量替代所有收敛分析。 2026官方回滚后的原review rating不是讨论后分数。这里before取原review字段，after仅取本人讨论承诺/已改分陈述或AC明确历史记录，绝不以AC预测代替实改。

**阅读范围与访问来源：** 逐条读完整关键评审主链及AC；未声称逐句精读其他无关支线。原网页受验证限制，以保留noteId/replyto/签名/时间的公开原始记录存档辅助读取。；公开 OpenReview 原始记录的匿名存档；非自动生成摘要

**机制标签：** `theory_repair`、`evaluation`、`claim_scope`

**复核链接：** [重点评审 note](https://openreview.net/forum?id=WtbXgc9GVA&noteId=38JqV9KeMs) · [作者回复 1](https://openreview.net/forum?id=WtbXgc9GVA&noteId=t6fRRKhUJH) · [AC](https://openreview.net/forum?id=WtbXgc9GVA&noteId=MYwtGXXWTV) · [决定](https://openreview.net/forum?id=WtbXgc9GVA&noteId=fof9nf5AhO) · [公开档案](https://huggingface.co/datasets/McGill-NLP/AI-For-Science-Retreat-Data/blob/main/iclr-dataset/iclr_2026_raw.parquet)

## C31

### [Decoupling Dynamical Richness from Representation Learning: Towards Practical Measurement](https://openreview.net/forum?id=7Mbz5uSf2J)

**ICLR 2026 · Accept (Poster) · `qualified_positive`**

**记录到的变化：** Czxk 4→6（plan；仍有部分疑虑）

**证据身份：** 本人提分承诺；AC确认历史；2026官方回滚后的原review rating不是讨论后分数。这里before取原review字段，after仅取本人讨论承诺/已改分陈述或AC明确历史记录，绝不以AC预测代替实改。

**原始阻碍：** 只评估最后一层；平衡分类、正交和各向同性假设范围窄；理论与实践联系偏定性，符号密集。

**作者动作：** 补中间层分析 Appendix I；说明平衡分类为当前神经坍缩分析的适用范围；承认完整非线性理论未解决，解释 CKA 度量动机并改清记号。

**评审反馈：** 评审清楚说只部分解决，愿4→6，但不会给8，因为验证范围和理论联系仍有限。

**选例理由：** 本人计划4→6且明确不给8；适合展示部分解决后的支持增强，但不把计划写成已保存数字。

**可迁移机制：** 补中间层和度量依据，说明平衡分类、正交与各向同性分析的适用范围。

**必须保留的限制：** plan与实际数值更改不同；完整非线性理论和验证范围仍有限。 2026官方回滚后的原review rating不是讨论后分数。这里before取原review字段，after仅取本人讨论承诺/已改分陈述或AC明确历史记录，绝不以AC预测代替实改。

**阅读范围与访问来源：** 逐条读完整关键评审主链及AC；未声称逐句精读其他无关支线。原网页受验证限制，以保留noteId/replyto/签名/时间的公开原始记录存档辅助读取。；公开 OpenReview 原始记录的匿名存档；非自动生成摘要

**机制标签：** `claim_scope`、`theory_repair`、`evaluation`、`ac_summary`

**复核链接：** [重点评审 note](https://openreview.net/forum?id=7Mbz5uSf2J&noteId=K8v4Gl0HSE) · [作者回复 1](https://openreview.net/forum?id=7Mbz5uSf2J&noteId=qNvqGrGWrj) · [AC](https://openreview.net/forum?id=7Mbz5uSf2J&noteId=vFWD2lzWiZ) · [决定](https://openreview.net/forum?id=7Mbz5uSf2J&noteId=SulXEtrUyp) · [公开档案](https://huggingface.co/datasets/McGill-NLP/AI-For-Science-Retreat-Data/blob/main/iclr-dataset/iclr_2026_raw.parquet)

## C32

### [Procedural Mistake Detection via Action Effect Modeling](https://openreview.net/forum?id=HsB5EuQOoS)

**ICLR 2026 · Accept (Poster) · `core_positive`**

**记录到的变化：** JzSx 2→6（已改）

**证据身份：** 本人明确数值表态；2026官方回滚后的原review rating不是讨论后分数。这里before取原review字段，after仅取本人讨论承诺/已改分陈述或AC明确历史记录，绝不以AC预测代替实改。

**原始阻碍：** 怀疑在测试集挑最优阈值导致不公平；多模块延迟不清；缺 GPT-5/Gemini 强基线；action effect 新颖性不足。

**作者动作：** 澄清结果为固定阈值网格的聚合，并非按测试集挑最优阈值；增加训练与推理耗时、联合训练解释；补 GPT-5 和 Gemini 2.5 Pro 的直接比较；区分预测正常状态与检测异常结果。

**评审反馈：** 最负面的 JzSx 明确2→6；AC 认可，仍指出新颖性问题没有完全消失，其他优势足以接收。

**选例理由：** 最负面评审本人明确2→6；测试阈值选择和强替代模型的核验很适合教授评测公平性优先。

**可迁移机制：** 逐项说明阈值网格如何聚合，排除测试集挑最优的误解，补最强通用模型及真实耗时。

**必须保留的限制：** AC仍保留创新性疑虑；协议澄清应能复现，不能只笼统否认泄漏。 2026官方回滚后的原review rating不是讨论后分数。这里before取原review字段，after仅取本人讨论承诺/已改分陈述或AC明确历史记录，绝不以AC预测代替实改。

**阅读范围与访问来源：** 逐条读完整关键评审主链及AC；未声称逐句精读其他无关支线。原网页受验证限制，以保留noteId/replyto/签名/时间的公开原始记录存档辅助读取。；公开 OpenReview 原始记录的匿名存档；非自动生成摘要

**机制标签：** `evaluation`、`baseline_fairness`、`efficiency`

**复核链接：** [核心数值表态](https://openreview.net/forum?id=HsB5EuQOoS&noteId=cWsuDKSibZ) · [作者回复 1](https://openreview.net/forum?id=HsB5EuQOoS&noteId=gwewxbD6xU) · [AC](https://openreview.net/forum?id=HsB5EuQOoS&noteId=e84MJbo1sO) · [决定](https://openreview.net/forum?id=HsB5EuQOoS&noteId=aruXibj2aT) · [公开档案](https://huggingface.co/datasets/McGill-NLP/AI-For-Science-Retreat-Data/blob/main/iclr-dataset/iclr_2026_raw.parquet)

## C33

### [Deterministic Bounds and Random Estimates of Metric Tensors on Neuromanifolds](https://openreview.net/forum?id=Ssevs8KCsU)

**ICLR 2026 · Accept (Poster) · `core_positive`**

**记录到的变化：** rVQk 4→6（本人明确）；AC静态列表仍列4，不能覆盖本人陈述

**证据身份：** 本人明确数值表态；2026官方回滚后的原review rating不是讨论后分数。这里before取原review字段，after仅取本人讨论承诺/已改分陈述或AC明确历史记录，绝不以AC预测代替实改。

**原始阻碍：** 估计器精度没有真实值校验；理论工具对下游研究有何帮助不清。

**作者动作：** 跨 NLP、视觉、音频模型，用大量自动微分计算真 FIM 并测相对误差，比较无偏 Hutchinson 与有偏 empirical FIM；说明优化、剪枝和几何研究中精确度量的用途；按要求用颜色标出新增内容。

**评审反馈：** rVQk 明确4→6，认为新增证据说明工具价值；AC 支持新增准确性、耗时与架构覆盖，但其打分摘要仍有旧4分。

**选例理由：** 本人明确4→6；用可计算真值校准理论估计器是独特且可迁移的证据机制，来源冲突亦可明确消解。

**可迁移机制：** 计算真实FIM并给相对误差、不同估计器对照和跨模态结果，把工具精度与使用价值连接。

**必须保留的限制：** AC静态分数仍为旧4，不能覆盖署名评审的直接陈述；这一可定位回滚差异不同于NetMoE未解决的初分冲突。 2026官方回滚后的原review rating不是讨论后分数。这里before取原review字段，after仅取本人讨论承诺/已改分陈述或AC明确历史记录，绝不以AC预测代替实改。

**阅读范围与访问来源：** 逐条读完整关键评审主链及AC；未声称逐句精读其他无关支线。原网页受验证限制，以保留noteId/replyto/签名/时间的公开原始记录存档辅助读取。；公开 OpenReview 原始记录的匿名存档；非自动生成摘要

**机制标签：** `evaluation`、`theory_repair`、`efficiency`、`ac_summary`

**复核链接：** [核心数值表态](https://openreview.net/forum?id=Ssevs8KCsU&noteId=6u69DwVi5N) · [作者回复 1](https://openreview.net/forum?id=Ssevs8KCsU&noteId=lrdIzIbByp) · [作者回复 2](https://openreview.net/forum?id=Ssevs8KCsU&noteId=xlkp1DLaqe) · [AC](https://openreview.net/forum?id=Ssevs8KCsU&noteId=spZIwf40xJ) · [决定](https://openreview.net/forum?id=Ssevs8KCsU&noteId=wjq6wVxrqD) · [公开档案](https://huggingface.co/datasets/McGill-NLP/AI-For-Science-Retreat-Data/blob/main/iclr-dataset/iclr_2026_raw.parquet)

## C34

### [Algorithmic Guarantees for Distilling Supervised and Offline RL Datasets](https://openreview.net/forum?id=zueIXg5FP5)

**ICLR 2026 · Accept (Poster) · `qualified_positive`**

**记录到的变化：** 3Mno 4→6，条件为将范围讨论加入修订

**证据身份：** 本人条件性承诺；AC确认；2026官方回滚后的原review rating不是讨论后分数。这里before取原review字段，after仅取本人讨论承诺/已改分陈述或AC明确历史记录，绝不以AC预测代替实改。

**原始阻碍：** 定理似乎不能处理原数据 n 远大于合成数据 m；证明中 m、n、维度混淆；RL只有小型实验。

**作者动作：** 解释保证以存在 loss-matching 合成集为条件；用 q=d+1 网进行证明不等于约束原数据规模；二轮明确条件保证并不承诺任意小 m 都存在，补 Gram 谱下界与反例讨论；说明高级离线RL目标超出当前 Bellman matching 保证。

**评审反馈：** 第一轮澄清没有消除疑虑，评审继续追问最小 m；第二轮明确量词和存在性后，接受4→6，但要求写入正文。

**选例理由：** 理论量词与存在性澄清有价值，但4→6附写回范围讨论条件，不列为无条件已确认逆转。

**可迁移机制：** 分开保证的量词、存在性前提、最小合成集规模与算法可构造性，用反例界定条件。

**必须保留的限制：** 短引没有完整条件，使用时必须连同改稿要求；不能将条件保证说成任意小m均存在解。 2026官方回滚后的原review rating不是讨论后分数。这里before取原review字段，after仅取本人讨论承诺/已改分陈述或AC明确历史记录，绝不以AC预测代替实改。

**阅读范围与访问来源：** 逐条读完整关键评审主链及AC；未声称逐句精读其他无关支线。原网页受验证限制，以保留noteId/replyto/签名/时间的公开原始记录存档辅助读取。；公开 OpenReview 原始记录的匿名存档；非自动生成摘要

**机制标签：** `theory_repair`、`claim_scope`、`multi_round`、`paper_revision`

**复核链接：** [重点评审 note](https://openreview.net/forum?id=zueIXg5FP5&noteId=63ukDRmpgI) · [作者回复 1](https://openreview.net/forum?id=zueIXg5FP5&noteId=0eKLGuxvgD) · [作者回复 2](https://openreview.net/forum?id=zueIXg5FP5&noteId=ZJa4qlv8xJ) · [AC](https://openreview.net/forum?id=zueIXg5FP5&noteId=uaxDBUMbDj) · [决定](https://openreview.net/forum?id=zueIXg5FP5&noteId=0pzBzKcfW1) · [公开档案](https://huggingface.co/datasets/McGill-NLP/AI-For-Science-Retreat-Data/blob/main/iclr-dataset/iclr_2026_raw.parquet)

## C35

### [Dynamical properties of dense associative memory](https://openreview.net/forum?id=TeDkzf34hs)

**ICLR 2026 · Accept (Poster) · `qualified_positive`**

**记录到的变化：** cF5v 2→6（happy to increase）；AC说无法预测

**证据身份：** 本人明确提分意愿；2026官方回滚后的原review rating不是讨论后分数。这里before取原review字段，after仅取本人讨论承诺/已改分陈述或AC明确历史记录，绝不以AC预测代替实改。

**原始阻碍：** 实验仅 n=3，理论却覆盖更高阶；缺真实图像数据；为何只分析同步更新，异步更新更常见。

**作者动作：** 解释高阶存储容量导致计算成本；说明独立 Bernoulli 模式及同步更新是本文理论边界，真实相关模式和异步数值方法留待后续；后续补 T=50/100 吸引域实验，增大图中文字并解释有限尺寸效应。

**评审反馈：** 评审承认此前主要按实验评估，重新重视清晰的证明后愿2→6；真实图像、异步和高阶完整实验未全部补齐，后续仍提出改进。

**选例理由：** 本人愿2→6，但评价重心重新校准与完成扩展实验须分开；适合作为理论论文范围限定辅例。

**可迁移机制：** 说明随机模式、同步更新和高阶容量的研究对象，解释为何部分实验不是当前理论的直接验证。

**必须保留的限制：** happy to increase不等于已保存分数；真实图像、异步和高阶实验未全做，后续补图不得倒推为先前提分原因。 2026官方回滚后的原review rating不是讨论后分数。这里before取原review字段，after仅取本人讨论承诺/已改分陈述或AC明确历史记录，绝不以AC预测代替实改。

**阅读范围与访问来源：** 逐条读完整关键评审主链及AC；未声称逐句精读其他无关支线。原网页受验证限制，以保留noteId/replyto/签名/时间的公开原始记录存档辅助读取。；公开 OpenReview 原始记录的匿名存档；非自动生成摘要

**机制标签：** `claim_scope`、`theory_repair`、`evaluation`

**复核链接：** [重点评审 note](https://openreview.net/forum?id=TeDkzf34hs&noteId=TfiPxMzAaS) · [作者回复 1](https://openreview.net/forum?id=TeDkzf34hs&noteId=vS2CMprrEa) · [作者回复 2](https://openreview.net/forum?id=TeDkzf34hs&noteId=6dWifLn1dZ) · [AC](https://openreview.net/forum?id=TeDkzf34hs&noteId=LmhaGMY2Br) · [决定](https://openreview.net/forum?id=TeDkzf34hs&noteId=cLMsJso2DI) · [公开档案](https://huggingface.co/datasets/McGill-NLP/AI-For-Science-Retreat-Data/blob/main/iclr-dataset/iclr_2026_raw.parquet)

## C36

### [WILD-Diffusion: A WDRO Inspired Training Method for Diffusion Models under Limited Data](https://openreview.net/forum?id=OrCVuQAYzF)

**ICLR 2026 · Accept (Poster) · `extended_positive`**

**记录到的变化：** vXtY 4→6；rEDT 4→marginal accept（未给数字）

**证据身份：** 本人明确数值表态；2026官方回滚后的原review rating不是讨论后分数。这里before取原review字段，after仅取本人讨论承诺/已改分陈述或AC明确历史记录，绝不以AC预测代替实改。

**原始阻碍：** 训练开销只有比率；增强基线可能未调参；加速方法被误作同目标基线；复杂数据、条件生成与新颖性欠验证。

**作者动作：** 补绝对小时数、FLOPs、显存及 K/m 扩展曲线；调 Mixup/CutMix/Cutout；澄清 DeepCache 等是兼容性测试；补 ImageNet、条件生成、DreamBooth 与最近 DRO 论文直接对照。

**评审反馈：** vXtY 看完新增实验后明确4→6；rEDT 特别认可 ImageNet 和最近论文对照，改为边缘接受，但仍担心少数据应用场景有限。

**选例理由：** 本人明确4→6；绝对资源账单和区分竞争/兼容基线很实用，作为扩散效率方向补充。

**可迁移机制：** 补小时数、FLOPs、显存及规模曲线；分别设置竞争baseline与正交兼容性测试。

**必须保留的限制：** 另一评审只写marginal accept未给数字；少数据应用场景仍被质疑，不能泛化到所有生成任务。 2026官方回滚后的原review rating不是讨论后分数。这里before取原review字段，after仅取本人讨论承诺/已改分陈述或AC明确历史记录，绝不以AC预测代替实改。

**阅读范围与访问来源：** 逐条读完整关键评审主链及AC；未声称逐句精读其他无关支线。原网页受验证限制，以保留noteId/replyto/签名/时间的公开原始记录存档辅助读取。；公开 OpenReview 原始记录的匿名存档；非自动生成摘要

**机制标签：** `efficiency`、`baseline_fairness`、`evaluation`、`related_work`

**复核链接：** [重点评审 note](https://openreview.net/forum?id=OrCVuQAYzF&noteId=VkNBEwFWsD) · [作者回复 1](https://openreview.net/forum?id=OrCVuQAYzF&noteId=q2pRGj3B8Y) · [作者回复 2](https://openreview.net/forum?id=OrCVuQAYzF&noteId=sls1f8npue) · [作者回复 3](https://openreview.net/forum?id=OrCVuQAYzF&noteId=hLBAsMShZE) · [作者回复 4](https://openreview.net/forum?id=OrCVuQAYzF&noteId=IhDf97QEJ2) · [作者回复 5](https://openreview.net/forum?id=OrCVuQAYzF&noteId=scewqa3PzC) · [AC](https://openreview.net/forum?id=OrCVuQAYzF&noteId=DHEM73J2sX) · [决定](https://openreview.net/forum?id=OrCVuQAYzF&noteId=nWWQwteJ6i) · [公开档案](https://huggingface.co/datasets/McGill-NLP/AI-For-Science-Retreat-Data/blob/main/iclr-dataset/iclr_2026_raw.parquet)

## C37

### [DeMo: Decoupled Momentum Optimization](https://openreview.net/forum?id=U9oewpa7cn)

**ICLR 2026 · Accept (Poster) · `qualified_positive`**

**记录到的变化：** 原始4/4/4/4；NyAn承诺4→6，条件是图2/3加免责声明；AC推测全员会6

**证据身份：** 本人条件性提分承诺；2026官方回滚后的原review rating不是讨论后分数。这里before取原review字段，after仅取本人讨论承诺/已改分陈述或AC明确历史记录，绝不以AC预测代替实改。

**原始阻碍：** 缺通信优化强基线；AdamW可能未公平调参；压缩方法竟大幅优于非压缩基线，图2/3可信度受到质疑。

**作者动作：** 补 DiLoCo、Muon、PowerSGD，并在可承受规模广泛调学习率和动量；承认充分调参的 AdamW 略优于 DeMo；最终按评审要求在图2/3写清受限调参设置并指向公平比较图7。

**评审反馈：** 评审只认为核心疑虑部分解决，承诺加分以免责声明为条件，作者后续落实。AC 判断所有4都可能升6，但这不是四个评审实际改分。作者一度指责评审观点矛盾，未说服评审。

**选例理由：** DeMo很适合教披露调参限制和性能—通信取舍，但NyAn仅提出有条件4→6；AC预期四个6不能当四次实改。

**可迁移机制：** 公开充分调参后更强的AdamW，给预算与图注免责声明，并把可支持价值收窄到通信成本。

**必须保留的限制：** 作者落实条件不自动等于评审后续确认；不能用原4/4/4/4和最终Poster编造全员已转正。 2026官方回滚后的原review rating不是讨论后分数。这里before取原review字段，after仅取本人讨论承诺/已改分陈述或AC明确历史记录，绝不以AC预测代替实改。

**阅读范围与访问来源：** 逐条读完整关键评审主链及AC；未声称逐句精读其他无关支线。原网页受验证限制，以保留noteId/replyto/签名/时间的公开原始记录存档辅助读取。；公开 OpenReview 原始记录的匿名存档；非自动生成摘要

**机制标签：** `baseline_fairness`、`efficiency`、`negative_results`、`claim_scope`、`ac_summary`

**复核链接：** [重点评审 note](https://openreview.net/forum?id=U9oewpa7cn&noteId=MbpXnuAD0V) · [作者回复 1](https://openreview.net/forum?id=U9oewpa7cn&noteId=CV7JnVVWlT) · [作者回复 2](https://openreview.net/forum?id=U9oewpa7cn&noteId=0NBtdYLRIm) · [作者回复 3](https://openreview.net/forum?id=U9oewpa7cn&noteId=VaasJPKYXX) · [作者回复 4](https://openreview.net/forum?id=U9oewpa7cn&noteId=NvEbHm5jYY) · [AC](https://openreview.net/forum?id=U9oewpa7cn&noteId=FbtyEw7X0b) · [决定](https://openreview.net/forum?id=U9oewpa7cn&noteId=VyC0VfkDqE) · [公开档案](https://huggingface.co/datasets/McGill-NLP/AI-For-Science-Retreat-Data/blob/main/iclr-dataset/iclr_2026_raw.parquet)

## C38

### [Accelerated Parallel Tempering via Neural Transports](https://openreview.net/forum?id=CODnlyYUli)

**ICLR 2026 · Accept (Poster) · `qualified_positive`**

**记录到的变化：** xVCo 2→4→6；bR4T 4→6（本人承诺，AC给数字）；93BL仍2

**证据身份：** 本人明确数值表态；2026官方回滚后的原review rating不是讨论后分数。这里before取原review字段，after仅取本人讨论承诺/已改分陈述或AC明确历史记录，绝不以AC预测代替实改。

**原始阻碍：** 神经采样本身的合理性遭质疑；只看 round trips 不足以说明实际质量；神经基线的总计算量和训练设置不公平。

**作者动作：** 解释作为 PT 元算法的贡献与渐近保证；补固定 wall-clock 下 ESS/有效样本数；承认总 NFE 与并行时间是不同预算，改清 neural sampler 比较与 CMCD 命名；解释 global barrier 的实践作用和限制。

**评审反馈：** xVCo 先2→4，随后明确说与同领域同行讨论后认识到自身观点不完整，再升6并降低confidence；bR4T 因比较解释和全局barrier澄清愿转接收。93BL仍反对，AC独立接受。

**选例理由：** 本人2→4→6可信，但本人说与同行讨论改变理解，不能全部归因于作者rebuttal；保留为归因边界辅例。

**可迁移机制：** 按wall-clock报告ESS，分别披露总NFE与并行时间，澄清元算法与neural sampler比较。

**必须保留的限制：** 外部专家讨论、confidence下降和仍为2的评审必须保留；不能称作者某种措辞直接促成最后提分。 2026官方回滚后的原review rating不是讨论后分数。这里before取原review字段，after仅取本人讨论承诺/已改分陈述或AC明确历史记录，绝不以AC预测代替实改。

**阅读范围与访问来源：** 逐条读完整关键评审主链及AC；未声称逐句精读其他无关支线。原网页受验证限制，以保留noteId/replyto/签名/时间的公开原始记录存档辅助读取。；公开 OpenReview 原始记录的匿名存档；非自动生成摘要

**机制标签：** `efficiency`、`baseline_fairness`、`multi_round`、`ac_summary`

**复核链接：** [重点评审 note](https://openreview.net/forum?id=CODnlyYUli&noteId=vKLQpAKi1u) · [作者回复 1](https://openreview.net/forum?id=CODnlyYUli&noteId=LQe4wRAzvL) · [作者回复 2](https://openreview.net/forum?id=CODnlyYUli&noteId=ts19X9O95K) · [作者回复 3](https://openreview.net/forum?id=CODnlyYUli&noteId=FRZ1qeMQrS) · [作者回复 4](https://openreview.net/forum?id=CODnlyYUli&noteId=N4FpZnDNJF) · [作者回复 5](https://openreview.net/forum?id=CODnlyYUli&noteId=MbAwO3DQZt) · [作者回复 6](https://openreview.net/forum?id=CODnlyYUli&noteId=fEVxe4oRn6) · [AC](https://openreview.net/forum?id=CODnlyYUli&noteId=8RxW2Gc3qv) · [决定](https://openreview.net/forum?id=CODnlyYUli&noteId=6dT4Xsp3IS) · [公开档案](https://huggingface.co/datasets/McGill-NLP/AI-For-Science-Retreat-Data/blob/main/iclr-dataset/iclr_2026_raw.parquet)

## C39

### [Bilevel Optimization with Lower-Level Uniform Convexity: Theory and Algorithm](https://openreview.net/forum?id=dJgb3ngAvT)

**ICLR 2026 · Accept (Poster) · `extended_positive`**

**记录到的变化：** qtYP 4→6（will）；pm1j 6→8；s2ox4可能不变

**证据身份：** 本人提分承诺；AC确认历史；2026官方回滚后的原review rating不是讨论后分数。这里before取原review字段，after仅取本人讨论承诺/已改分陈述或AC明确历史记录，绝不以AC预测代替实改。

**原始阻碍：** 关键定义缺失、定理编号错、记号不统一；变换后的可逆性假设是否使理论退化为已知结果；同时用期望和高概率不清。

**作者动作：** 补定义并统一记号；把算法所用随机超梯度移入正文；解释新变量变换和 LLUC 难点；明确两个独立随机源分别取期望与高概率；给假设与结论的对应关系。

**评审反馈：** qtYP 认为大部分问题已解决、无继续提问，愿4→6，但要求进一步润色。AC仍保留实践动机偏理想化和部分假设可检验性的担忧。

**选例理由：** 本人无条件表示升6；定义、随机源和依赖关系的修复可作为理论呈现问题的扩展。

**可迁移机制：** 补定义与统一记号，分别解释独立随机源的期望/高概率保证，把算法所用量移入主文。

**必须保留的限制：** 仍有实际动机理想化和假设可检验性疑问；will表态不能冒充2026当前评分栏。 2026官方回滚后的原review rating不是讨论后分数。这里before取原review字段，after仅取本人讨论承诺/已改分陈述或AC明确历史记录，绝不以AC预测代替实改。

**阅读范围与访问来源：** 逐条读完整关键评审主链及AC；未声称逐句精读其他无关支线。原网页受验证限制，以保留noteId/replyto/签名/时间的公开原始记录存档辅助读取。；公开 OpenReview 原始记录的匿名存档；非自动生成摘要

**机制标签：** `theory_repair`、`paper_revision`、`claim_scope`

**复核链接：** [重点评审 note](https://openreview.net/forum?id=dJgb3ngAvT&noteId=eBlwdlPOIM) · [作者回复 1](https://openreview.net/forum?id=dJgb3ngAvT&noteId=dGq80DsO59) · [作者回复 2](https://openreview.net/forum?id=dJgb3ngAvT&noteId=1SXHdKN9Na) · [作者回复 3](https://openreview.net/forum?id=dJgb3ngAvT&noteId=ljScYiBwCD) · [AC](https://openreview.net/forum?id=dJgb3ngAvT&noteId=zJqqhMuGOM) · [决定](https://openreview.net/forum?id=dJgb3ngAvT&noteId=8k4FIjQvtH) · [公开档案](https://huggingface.co/datasets/McGill-NLP/AI-For-Science-Retreat-Data/blob/main/iclr-dataset/iclr_2026_raw.parquet)

## C40

### [Representation Alignment for Diffusion Transformers without External Components](https://openreview.net/forum?id=ds5w2xth93)

**ICLR 2026 · Accept (Poster) · `extended_positive`**

**记录到的变化：** NzJf 4→6；1H2k也4→6（本人及AC）

**证据身份：** 本人明确数值表态；2026官方回滚后的原review rating不是讨论后分数。这里before取原review字段，after仅取本人讨论承诺/已改分陈述或AC明确历史记录，绝不以AC预测代替实改。

**原始阻碍：** EMA设置敏感且解释薄弱；“教师持续改善”无证据；长期训练是否持续改进、能否文本到图像泛化不清；无强外部编码器场景没有实测。

**作者动作：** 解释高EMA系数稳定对齐与扩散目标的平衡；补200k/400k/800k线性探测；延长训练曲线；在MMDiT上复用超参数测试文本到图像；坦承资源不足未做大规模视频训练并加入限制。

**评审反馈：** NzJf 明确大部分疑虑解除并升至6；AC确认两个4转6，同时指出无强编码器动机及启发式设计仍未完全证实。

**选例理由：** 本人明确升6；纵向线性探测和冻结超参数迁移给机制叙述可测证据，作为扩展。

**可迁移机制：** 将教师变好的说法转成分阶段线性探测和长程曲线，再固定设置迁移到新任务。

**必须保留的限制：** 大规模视频未做、无强外部编码器动机未完全验证，不能把未做扩展写成已消除限制。 2026官方回滚后的原review rating不是讨论后分数。这里before取原review字段，after仅取本人讨论承诺/已改分陈述或AC明确历史记录，绝不以AC预测代替实改。

**阅读范围与访问来源：** 逐条读完整关键评审主链及AC；未声称逐句精读其他无关支线。原网页受验证限制，以保留noteId/replyto/签名/时间的公开原始记录存档辅助读取。；公开 OpenReview 原始记录的匿名存档；非自动生成摘要

**机制标签：** `evaluation`、`claim_scope`、`negative_results`

**复核链接：** [重点评审 note](https://openreview.net/forum?id=ds5w2xth93&noteId=uKHH48tjer) · [作者回复 1](https://openreview.net/forum?id=ds5w2xth93&noteId=F6wmJxEqdZ) · [作者回复 2](https://openreview.net/forum?id=ds5w2xth93&noteId=cI1MgaRY3m) · [AC](https://openreview.net/forum?id=ds5w2xth93&noteId=K423bvgybp) · [决定](https://openreview.net/forum?id=ds5w2xth93&noteId=Hvc3gQAg38) · [公开档案](https://huggingface.co/datasets/McGill-NLP/AI-For-Science-Retreat-Data/blob/main/iclr-dataset/iclr_2026_raw.parquet)

## C41

### [Reassessing Layer Pruning in LLMs: New Insights and Methods](https://openreview.net/forum?id=04Tfwy3LLC)

**ICLR 2026 · Accept (Poster) · `qualified_positive`**

**记录到的变化：** mE3b 4→6（AC数字）；Ncfm 6→8（本人）；PD7z 2→4仍负面

**证据身份：** 本人表态；数字由AC补充；2026官方回滚后的原review rating不是讨论后分数。这里before取原review字段，after仅取本人讨论承诺/已改分陈述或AC明确历史记录，绝不以AC预测代替实改。

**原始阻碍：** 主要用多项选择任务，不能推断数学、代码、生成任务的后层不重要；对MoE是否适用不清；其他评审质疑剪枝与微调公平性。

**作者动作：** 按目标评审预先明确的条件补 GSM8K、WikiText-2 困惑度、Mixtral 同剪枝率比较并改正文；其他线程补HumanEval、邻接层微调对照、宽度剪枝吞吐和更多微调层数。

**评审反馈：** mE3b 说问题已回答并已改分，AC明确为4→6；Ncfm明确6→8但提醒性能差距不大；最负面PD7z只2→4。

**选例理由：** mE3b确认已改但4→6数字来自AC；另有Ncfm6→8可用，适合实验条件对齐辅例，不作该负面路径的本人数字确证。

**可迁移机制：** 按评审提出的任务/架构条件补数学、生成与MoE，并报告同剪枝率和微调控制。

**必须保留的限制：** PD7z只2→4仍负面；Ncfm原本正面，不应移花接木证明最负面评审转正。 2026官方回滚后的原review rating不是讨论后分数。这里before取原review字段，after仅取本人讨论承诺/已改分陈述或AC明确历史记录，绝不以AC预测代替实改。

**阅读范围与访问来源：** 逐条读完整关键评审主链及AC；未声称逐句精读其他无关支线。原网页受验证限制，以保留noteId/replyto/签名/时间的公开原始记录存档辅助读取。；公开 OpenReview 原始记录的匿名存档；非自动生成摘要

**机制标签：** `evaluation`、`baseline_fairness`、`paper_revision`、`ac_summary`

**复核链接：** [重点评审 note](https://openreview.net/forum?id=04Tfwy3LLC&noteId=zjicUikvES) · [作者回复 1](https://openreview.net/forum?id=04Tfwy3LLC&noteId=GNfmVg8Bgn) · [AC](https://openreview.net/forum?id=04Tfwy3LLC&noteId=icHquSOLSK) · [决定](https://openreview.net/forum?id=04Tfwy3LLC&noteId=NJQs39JmYx) · [公开档案](https://huggingface.co/datasets/McGill-NLP/AI-For-Science-Retreat-Data/blob/main/iclr-dataset/iclr_2026_raw.parquet)

## C42

### [SuperMAN: Interpretable and Expressive Networks over Temporally Sparse Heterogeneous Data](https://openreview.net/forum?id=1MVeSLvfxU)

**ICLR 2026 · Accept (Poster) · `qualified_positive`**

**记录到的变化：** PX2M 6→更高/各项分数上调，具体总评分未知；唯一4分评审未追评

**证据身份：** 本人提分；目标数字未知；2026官方回滚后的原review rating不是讨论后分数。这里before取原review字段，after仅取本人讨论承诺/已改分陈述或AC明确历史记录，绝不以AC预测代替实改。

**原始阻碍：** 与 GNAN 相比新颖性需更明确；O(n²)长轨迹成本；临床应用缺校准、噪声与时间扰动稳健性；怀疑没提供代码。

**作者动作：** 澄清图内特征分组与跨图集合混合两层贡献；补长轨迹真实耗时、稀疏mask加速；补ECE和三类测试扰动曲线；指出补充zip已有代码与运行说明。

**评审反馈：** 初始6分的PX2M认为大量新增实验解决问题，明确说已提高分数，但未给数字；AC说唯一负面评审未继续回复，不能推断其转正。

**选例理由：** 本人明确提高但未报总分目标且初始已6；可以学习稳健性、校准和运行细节，不能作为负转正数字案例。

**可迁移机制：** 用ECE、噪声/时间扰动和长轨迹真实耗时补应用可用性，准确定位已提供的代码。

**必须保留的限制：** 唯一4分评审未再回复；沉默不是认可，不能补写其最终正面分数。 2026官方回滚后的原review rating不是讨论后分数。这里before取原review字段，after仅取本人讨论承诺/已改分陈述或AC明确历史记录，绝不以AC预测代替实改。

**阅读范围与访问来源：** 逐条读完整关键评审主链及AC；未声称逐句精读其他无关支线。原网页受验证限制，以保留noteId/replyto/签名/时间的公开原始记录存档辅助读取。；公开 OpenReview 原始记录的匿名存档；非自动生成摘要

**机制标签：** `evaluation`、`efficiency`、`paper_revision`、`ac_summary`

**复核链接：** [重点评审 note](https://openreview.net/forum?id=1MVeSLvfxU&noteId=nbE4MoSOmL) · [作者回复 1](https://openreview.net/forum?id=1MVeSLvfxU&noteId=G9CV6ZBWQT) · [作者回复 2](https://openreview.net/forum?id=1MVeSLvfxU&noteId=TpFJQEAngP) · [作者回复 3](https://openreview.net/forum?id=1MVeSLvfxU&noteId=LMsAPlcXZ7) · [AC](https://openreview.net/forum?id=1MVeSLvfxU&noteId=TtRRHoCMtX) · [决定](https://openreview.net/forum?id=1MVeSLvfxU&noteId=GFAyZqPIQb) · [公开档案](https://huggingface.co/datasets/McGill-NLP/AI-For-Science-Retreat-Data/blob/main/iclr-dataset/iclr_2026_raw.parquet)

## C43

### [Model soups need only one ingredient](https://openreview.net/forum?id=ICANwnoGgN)

**ICLR 2026 · Reject · `outcome_counterexample`**

**记录到的变化：** q1EA 4→6；gzvH 6→8；Yqvj 6→8（AC 记录）

**证据身份：** AC明确记录历史提分；按本人讨论或AC明确记录；AC条件预测不作实际改分。

**原始阻碍：** 谱权重的理论依据、单模型场景的新颖性、收益大小和适用规模。

**作者动作：** 增加有效秩选参、ConvNeXt 与 70 个检查点分析，补充表征对齐证据并修改正文。

**评审反馈：** 多位评审转正面，AC 也列出加分，但仍认为低能量权重缺乏充分理论依据、收益有限，最终拒稿。

**选例理由：** MonoSoup被保留为提分仍拒反例：AC明确列出历史加分，仍认定核心理论支撑和收益不足，不作接收逆转范本。

**可迁移机制：** 给AC按核心主张逐项对应新增证据与残余缺口，而非统计支持者人数。

**必须保留的限制：** 不代表论文低质量或回应毫无价值；只说明数字改善未解除该次决定中的关键拒稿依据。 按本人/AC原始措辞保留条件或推断；2026评分栏已回滚。

**阅读范围与访问来源：** 已读初评 作者回应 评审追评及 AC 原始记录；公开 OpenReview 原始记录存档

**机制标签：** `theory_repair`、`evaluation`、`ac_summary`

**复核链接：** [重点评审 note](https://openreview.net/forum?id=ICANwnoGgN&noteId=Ax5fH58HGb) · [作者回复 1](https://openreview.net/forum?id=ICANwnoGgN&noteId=dT64S3L0Jr) · [作者回复 2](https://openreview.net/forum?id=ICANwnoGgN&noteId=OpzUsoBSsr) · [作者回复 3](https://openreview.net/forum?id=ICANwnoGgN&noteId=sYehOtBG0B) · [作者回复 4](https://openreview.net/forum?id=ICANwnoGgN&noteId=G8d0mF50YD) · [作者回复 5](https://openreview.net/forum?id=ICANwnoGgN&noteId=a491n5Nd75) · [作者回复 6](https://openreview.net/forum?id=ICANwnoGgN&noteId=vQ70qzlIEk) · [作者回复 7](https://openreview.net/forum?id=ICANwnoGgN&noteId=neuwPICgjS) · [作者回复 8](https://openreview.net/forum?id=ICANwnoGgN&noteId=lSB4Ymr1IF) · [作者回复 9](https://openreview.net/forum?id=ICANwnoGgN&noteId=IeBe3NeLID) · [作者回复 10](https://openreview.net/forum?id=ICANwnoGgN&noteId=ecsnIie0F9) · [作者回复 11](https://openreview.net/forum?id=ICANwnoGgN&noteId=ndXTmKTFhC) · [作者回复 12](https://openreview.net/forum?id=ICANwnoGgN&noteId=0GS1ZGi1tj) · [作者回复 13](https://openreview.net/forum?id=ICANwnoGgN&noteId=hD3TveyxSL) · [决定](https://openreview.net/forum?id=ICANwnoGgN&noteId=p0VR9cKoYg) · [公开档案](https://huggingface.co/datasets/McGill-NLP/AI-For-Science-Retreat-Data/blob/main/iclr-dataset/iclr_2026_raw.parquet)

## C44

### [FuseGPT: Prune-and-Fuse Knowledge Redistribution for Efficient Transformers](https://openreview.net/forum?id=tNnXu5bKoo)

**ICLR 2026 · Reject · `outcome_counterexample`**

**记录到的变化：** Ycs9 2→4；AC 认为 t6pW 亦为 2→4

**证据身份：** 本人提分承诺；AC核对；按本人讨论或AC明确记录；AC条件预测不作实际改分。

**原始阻碍：** Macro Influence 与 fusion-aware 的联系、MKA 比较公平性、实验完成度。

**作者动作：** 补 MKA 和新模型比较、计时、域迁移说明。

**评审反馈：** Ycs9 明确愿升至 4；AC 认为方法机理、压缩率不一致和验证范围仍未解决，最终拒稿。

**选例理由：** FuseGPT的2→4仍在拒稿档，且最终Reject；不能因为上涨明显就列为负转正成功。

**可迁移机制：** 补实验前先确认机理、压缩率和比较协议一致，区分改善与跨过接受门槛。

**必须保留的限制：** 评分上涨未达到接收档；AC对另一评审的2→4是其回顾，不应伪装成两条本人确认。 按本人/AC原始措辞保留条件或推断；2026评分栏已回滚。

**阅读范围与访问来源：** 已读初评 作者回应 评审追评及 AC 原始记录；公开 OpenReview 原始记录存档

**机制标签：** `baseline_fairness`、`evaluation`、`ac_summary`

**复核链接：** [重点评审 note](https://openreview.net/forum?id=tNnXu5bKoo&noteId=UtzoOFDGyl) · [作者回复 1](https://openreview.net/forum?id=tNnXu5bKoo&noteId=MHtLfJRcu9) · [作者回复 2](https://openreview.net/forum?id=tNnXu5bKoo&noteId=WkAUkXpydx) · [作者回复 3](https://openreview.net/forum?id=tNnXu5bKoo&noteId=wIYjk5kV2P) · [作者回复 4](https://openreview.net/forum?id=tNnXu5bKoo&noteId=34C1spLa6f) · [作者回复 5](https://openreview.net/forum?id=tNnXu5bKoo&noteId=SmKIS8AIjg) · [作者回复 6](https://openreview.net/forum?id=tNnXu5bKoo&noteId=TU99Va8uCS) · [作者回复 7](https://openreview.net/forum?id=tNnXu5bKoo&noteId=00lhFtEXND) · [作者回复 8](https://openreview.net/forum?id=tNnXu5bKoo&noteId=G9xW1oCNml) · [作者回复 9](https://openreview.net/forum?id=tNnXu5bKoo&noteId=mPiWzVllvz) · [作者回复 10](https://openreview.net/forum?id=tNnXu5bKoo&noteId=ppLs1f395z) · [作者回复 11](https://openreview.net/forum?id=tNnXu5bKoo&noteId=1Cqen4Lxzd) · [作者回复 12](https://openreview.net/forum?id=tNnXu5bKoo&noteId=GrVYcHFltO) · [作者回复 13](https://openreview.net/forum?id=tNnXu5bKoo&noteId=WqL7ILP54a) · [决定](https://openreview.net/forum?id=tNnXu5bKoo&noteId=PW26mQgJ5i) · [公开档案](https://huggingface.co/datasets/McGill-NLP/AI-For-Science-Retreat-Data/blob/main/iclr-dataset/iclr_2026_raw.parquet)

## C45

### [Censoring with Plausible Deniability: Asymmetric Local Privacy for Multi-Category CDF Estimation](https://openreview.net/forum?id=vSXIEbTVhE)

**ICLR 2026 · Reject · `outcome_counterexample`**

**记录到的变化：** 4p71 2→4；只有满足正文澄清后的 4→6 条件意愿

**证据身份：** 条件性提分尚未闭环；按本人讨论或AC明确记录；AC条件预测不作实际改分。

**原始阻碍：** 隐私保证究竟针对原始连续特征，还是随机阈值形成的潜在敏感状态。

**作者动作：** 澄清保证作用于变换后的空间，补算法和真实数据说明；作者后来称已在 Remark 2 修改。

**评审反馈：** 评审认为第 2–15 点已解决，但核心第 1 点只部分解决；作者把条件性升分写成已同意。AC 最终仍判核心缺陷未解决。

**选例理由：** 隐私案例只确认2→4，4→6尚附条件且未闭环，作者自述过度概括；作为条件和确认混淆的反例。

**可迁移机制：** 精确定义隐私保证作用对象，修改后给位置并等待核验，逐条记录未解决核心问题。

**必须保留的限制：** 最终Reject不能简单归因语气；实质保证争议未解决。不能把作者称已修改写成评审已同意6。 按本人/AC原始措辞保留条件或推断；2026评分栏已回滚。

**阅读范围与访问来源：** 已读初评 作者回应 评审追评及 AC 原始记录；公开 OpenReview 原始记录存档

**机制标签：** `theory_repair`、`claim_scope`、`paper_revision`、`ac_summary`

**复核链接：** [重点评审 note](https://openreview.net/forum?id=vSXIEbTVhE&noteId=pyIl197Hos) · [作者回复 1](https://openreview.net/forum?id=vSXIEbTVhE&noteId=NfE7uAaQHe) · [作者回复 2](https://openreview.net/forum?id=vSXIEbTVhE&noteId=yNOoJ5q14I) · [作者回复 3](https://openreview.net/forum?id=vSXIEbTVhE&noteId=w01V6AmDMW) · [作者回复 4](https://openreview.net/forum?id=vSXIEbTVhE&noteId=7XcJ07Usnl) · [作者回复 5](https://openreview.net/forum?id=vSXIEbTVhE&noteId=HCtHsbrpxr) · [作者回复 6](https://openreview.net/forum?id=vSXIEbTVhE&noteId=MQshzc6eny) · [作者回复 7](https://openreview.net/forum?id=vSXIEbTVhE&noteId=vf2Ib1neJu) · [作者回复 8](https://openreview.net/forum?id=vSXIEbTVhE&noteId=LlpNL77hae) · [作者回复 9](https://openreview.net/forum?id=vSXIEbTVhE&noteId=qLx3t7lknh) · [作者回复 10](https://openreview.net/forum?id=vSXIEbTVhE&noteId=bD0UcHm0Px) · [决定](https://openreview.net/forum?id=vSXIEbTVhE&noteId=OrqyDcQzEj) · [公开档案](https://huggingface.co/datasets/McGill-NLP/AI-For-Science-Retreat-Data/blob/main/iclr-dataset/iclr_2026_raw.parquet)

## C46

### [ASMG: Data Structure-Aware Routing via Incremental Subspace Learning for MoE](https://openreview.net/forum?id=xsqiDQjSvV)

**ICLR 2026 · Reject · `outcome_counterexample`**

**记录到的变化：** 9td1 4→6、H4c4 4→6；ieFN 承诺 4→6

**证据身份：** 本人明确数值表态；按本人讨论或AC明确记录；AC条件预测不作实际改分。

**原始阻碍：** MoE 路由实验规模、额外复杂度与实际收益。

**作者动作：** 补 Qwen 与 Llama、路由消融、负载均衡和每步训练时间。

**评审反馈：** 两位评审明确已提分、一位承诺提分，但 AC 认为实验覆盖和实际收益仍不足，最终拒稿。

**选例理由：** ASMG有明确4→6但仍Reject；用于解释AC对额外复杂度、收益和覆盖范围的判断可不同于多数分数。

**可迁移机制：** 让规模实验、消融、时间账单回答实际价值问题，并明确哪些主张仍未支持。

**必须保留的限制：** 不将被拒等同论文整体低质量；反例只针对“多数加分便必接收”的错误推断。 按本人/AC原始措辞保留条件或推断；2026评分栏已回滚。

**阅读范围与访问来源：** 已读初评 作者回应 评审追评及 AC 原始记录；公开 OpenReview 原始记录存档

**机制标签：** `efficiency`、`evaluation`、`ac_summary`

**复核链接：** [重点评审 note](https://openreview.net/forum?id=xsqiDQjSvV&noteId=dPi75ZnQsI) · [作者回复 1](https://openreview.net/forum?id=xsqiDQjSvV&noteId=n6YvAzA5Wj) · [作者回复 2](https://openreview.net/forum?id=xsqiDQjSvV&noteId=lPAaI3ZT82) · [作者回复 3](https://openreview.net/forum?id=xsqiDQjSvV&noteId=yhAfmZFbtw) · [作者回复 4](https://openreview.net/forum?id=xsqiDQjSvV&noteId=yaIOZe0Yi2) · [作者回复 5](https://openreview.net/forum?id=xsqiDQjSvV&noteId=r3ls3zvSEw) · [作者回复 6](https://openreview.net/forum?id=xsqiDQjSvV&noteId=6kLshojSfJ) · [作者回复 7](https://openreview.net/forum?id=xsqiDQjSvV&noteId=LXxDE55k7u) · [作者回复 8](https://openreview.net/forum?id=xsqiDQjSvV&noteId=1zD7eHQt0h) · [作者回复 9](https://openreview.net/forum?id=xsqiDQjSvV&noteId=vBwFeMU5JQ) · [作者回复 10](https://openreview.net/forum?id=xsqiDQjSvV&noteId=auIEB28PoN) · [作者回复 11](https://openreview.net/forum?id=xsqiDQjSvV&noteId=SIdmzKuXL3) · [作者回复 12](https://openreview.net/forum?id=xsqiDQjSvV&noteId=Hi6AoMT4wo) · [作者回复 13](https://openreview.net/forum?id=xsqiDQjSvV&noteId=7nM0o67BGD) · [作者回复 14](https://openreview.net/forum?id=xsqiDQjSvV&noteId=3cmiRRzbCc) · [作者回复 15](https://openreview.net/forum?id=xsqiDQjSvV&noteId=Ylzl7ollJS) · [作者回复 16](https://openreview.net/forum?id=xsqiDQjSvV&noteId=DVhXRpJKFP) · [作者回复 17](https://openreview.net/forum?id=xsqiDQjSvV&noteId=z8n0Va1D4K) · [作者回复 18](https://openreview.net/forum?id=xsqiDQjSvV&noteId=xKA58woirp) · [作者回复 19](https://openreview.net/forum?id=xsqiDQjSvV&noteId=p9TPHkYxeS) · [作者回复 20](https://openreview.net/forum?id=xsqiDQjSvV&noteId=FETHGCFwVF) · [作者回复 21](https://openreview.net/forum?id=xsqiDQjSvV&noteId=hN9RjeaBtV) · [作者回复 22](https://openreview.net/forum?id=xsqiDQjSvV&noteId=phdeQPnLS9) · [作者回复 23](https://openreview.net/forum?id=xsqiDQjSvV&noteId=iBiaohLCvf) · [作者回复 24](https://openreview.net/forum?id=xsqiDQjSvV&noteId=Q9KqozQepa) · [作者回复 25](https://openreview.net/forum?id=xsqiDQjSvV&noteId=eQfHHQ4zhS) · [作者回复 26](https://openreview.net/forum?id=xsqiDQjSvV&noteId=Owh8Anl9up) · [作者回复 27](https://openreview.net/forum?id=xsqiDQjSvV&noteId=8zX7SzPhRP) · [作者回复 28](https://openreview.net/forum?id=xsqiDQjSvV&noteId=tlhoDFsinJ) · [作者回复 29](https://openreview.net/forum?id=xsqiDQjSvV&noteId=GMNdugD8Eh) · [决定](https://openreview.net/forum?id=xsqiDQjSvV&noteId=TW1ZPUkL6B) · [公开档案](https://huggingface.co/datasets/McGill-NLP/AI-For-Science-Retreat-Data/blob/main/iclr-dataset/iclr_2026_raw.parquet)

## C47

### [InfoNCE Induces Gaussian Distribution](https://openreview.net/forum?id=BlSH7gNQSq)

**ICLR 2026 · Accept (Oral) · `context_only`**

**记录到的变化：** 初始 8/4/2/2；AC 预计最终高于 6；Oral

**证据身份：** AC预期，非真实终评分；按本人讨论或AC明确记录；AC条件预测不作实际改分。

**原始阻碍：** 理论相对可辨识性文献的新颖性、假设合理性、高斯性检验与 SimCLR 验证。

**作者动作：** 澄清与 latent identifiability 的问题差异，加入二元与合成数据、SimCLR/监督对照，承认 DINO 超出理论并收窄措辞。

**评审反馈：** AC 认为主要问题得到回应，最终 Oral；没有足够依据写成每位评审真实加分。

**选例理由：** InfoNCE最终Oral值得保留为AC独立判断案例，但低初分加接收不构成逐评审改分证据。

**可迁移机制：** 澄清理论定位并用可控数据和直接对照支持边界，让AC可独立判断贡献。

**必须保留的限制：** 只有AC预计最终高于6，不能写成2→6或全体低分转正；Oral不填补缺失的评分证据。 按本人/AC原始措辞保留条件或推断；2026评分栏已回滚。

**阅读范围与访问来源：** 已读初评 作者回应 评审追评及 AC 原始记录；公开 OpenReview 原始记录存档

**机制标签：** `novelty`、`theory_repair`、`evaluation`、`ac_summary`

**复核链接：** [重点评审 note](https://openreview.net/forum?id=BlSH7gNQSq&noteId=Bzx9XPwY2V) · [作者回复 1](https://openreview.net/forum?id=BlSH7gNQSq&noteId=iUYUIKAyWn) · [作者回复 2](https://openreview.net/forum?id=BlSH7gNQSq&noteId=O89cxDSPGo) · [作者回复 3](https://openreview.net/forum?id=BlSH7gNQSq&noteId=4nJHQqx74c) · [作者回复 4](https://openreview.net/forum?id=BlSH7gNQSq&noteId=bV1GJ0IcoG) · [作者回复 5](https://openreview.net/forum?id=BlSH7gNQSq&noteId=JQN22dPUdG) · [作者回复 6](https://openreview.net/forum?id=BlSH7gNQSq&noteId=zB9oh3CoAg) · [作者回复 7](https://openreview.net/forum?id=BlSH7gNQSq&noteId=OHjd50lnbw) · [作者回复 8](https://openreview.net/forum?id=BlSH7gNQSq&noteId=dAMU7eWMcs) · [作者回复 9](https://openreview.net/forum?id=BlSH7gNQSq&noteId=DOVga3PAMZ) · [作者回复 10](https://openreview.net/forum?id=BlSH7gNQSq&noteId=jRlnsUQ07y) · [作者回复 11](https://openreview.net/forum?id=BlSH7gNQSq&noteId=0UmSTWm7kc) · [作者回复 12](https://openreview.net/forum?id=BlSH7gNQSq&noteId=jL01EIhjvn) · [作者回复 13](https://openreview.net/forum?id=BlSH7gNQSq&noteId=rHHpNXz4Rn) · [作者回复 14](https://openreview.net/forum?id=BlSH7gNQSq&noteId=SiAyqhzKWN) · [决定](https://openreview.net/forum?id=BlSH7gNQSq&noteId=7gfZmLbLoa) · [公开档案](https://huggingface.co/datasets/McGill-NLP/AI-For-Science-Retreat-Data/blob/main/iclr-dataset/iclr_2026_raw.parquet)

## C48

### [GAGA: Gaussianity-Aware Gaussian Approximation for Efficient 3D Molecular Generation](https://openreview.net/forum?id=Q9gz8lVyAi)

**ICLR 2026 · Accept (Poster) · `qualified_positive`**

**记录到的变化：** FhFk 2→6 承诺；其余 AC 预期升 6 不能作已证事实

**证据身份：** 本人承诺与AC推断有争议；按本人讨论或AC明确记录；AC条件预测不作实际改分。

**原始阻碍：** 高斯近似依据、截断训练采样、与既有工作的差别和复现性。

**作者动作：** 补定量高斯性比较、训练采样说明、标准差及匿名代码。

**评审反馈：** FhFk 表示满意并愿升 6，但因系统限制无法更新；另一评审后来公开反对 AC 对其态度变化的推断。最终 Poster。

**选例理由：** GAGA的一位评审有明确2→6意愿，可限于该个人记录借鉴；AC对其他人态度的推断被公开反对，不作全员逆转范例。

**可迁移机制：** 补高斯性定量检验、采样说明与复现代码，同时逐评审标记实际表态和争议。

**必须保留的限制：** 保留FhFk的个人承诺，不把其余AC预期合并成共识；争议不抹掉已存在的个人正面证据，也不评价论文质量。 按本人/AC原始措辞保留条件或推断；2026评分栏已回滚。

**阅读范围与访问来源：** 已读初评 作者回应 评审追评及 AC 原始记录；公开 OpenReview 原始记录存档

**机制标签：** `evaluation`、`theory_repair`、`ac_summary`

**复核链接：** [重点评审 note](https://openreview.net/forum?id=Q9gz8lVyAi&noteId=NN9VIC3nKz) · [作者回复 1](https://openreview.net/forum?id=Q9gz8lVyAi&noteId=WZvfLoc1zz) · [作者回复 2](https://openreview.net/forum?id=Q9gz8lVyAi&noteId=vS25Y1shdV) · [作者回复 3](https://openreview.net/forum?id=Q9gz8lVyAi&noteId=wmrWb0b0h7) · [作者回复 4](https://openreview.net/forum?id=Q9gz8lVyAi&noteId=BYADAn2IKz) · [作者回复 5](https://openreview.net/forum?id=Q9gz8lVyAi&noteId=xGuvSTxOcS) · [作者回复 6](https://openreview.net/forum?id=Q9gz8lVyAi&noteId=NRp0zxMBW3) · [作者回复 7](https://openreview.net/forum?id=Q9gz8lVyAi&noteId=hliOHpBVE9) · [作者回复 8](https://openreview.net/forum?id=Q9gz8lVyAi&noteId=EXZgww2b51) · [作者回复 9](https://openreview.net/forum?id=Q9gz8lVyAi&noteId=VYPbjkOTA9) · [作者回复 10](https://openreview.net/forum?id=Q9gz8lVyAi&noteId=yV12nP9N9X) · [作者回复 11](https://openreview.net/forum?id=Q9gz8lVyAi&noteId=NhdXcQhDyQ) · [决定](https://openreview.net/forum?id=Q9gz8lVyAi&noteId=d5Oo9Uuyfp) · [公开档案](https://huggingface.co/datasets/McGill-NLP/AI-For-Science-Retreat-Data/blob/main/iclr-dataset/iclr_2026_raw.parquet)

## C49

### [PLAGUE: Plug-and-play framework for Lifelong Adaptive Generation of mUlti-turn jailbrEaks](https://openreview.net/forum?id=05hNleYOcG)

**ICLR 2026 · Accept (Poster) · `context_only`**

**记录到的变化：** 初始 2/2/4/2；AC 预计部分 4→6；Poster

**证据身份：** AC预期，非真实终评分；按本人讨论或AC明确记录；AC条件预测不作实际改分。

**原始阻碍：** 工程组合新颖性、漏掉较强基线、比较预算和概念表述。

**作者动作：** 补匹配预算与轮数的基线实验、消融与评估说明，并修复版式问题。

**评审反馈：** AC 认可工程贡献并不同意部分评价标准；只有部分评分可能上升的判断，不能声称所有低分评审转正。

**选例理由：** PLAGUE低初分最终接收主要体现AC对工程贡献的独立评价，缺本人数字逆转，不入核心确证。

**可迁移机制：** 匹配攻击预算和轮数补强基线，以消融和评价协议说明组合系统的实质作用。

**必须保留的限制：** 初始多2分不能倒推全部变6；AC可能提高的判断仍是预测。 按本人/AC原始措辞保留条件或推断；2026评分栏已回滚。

**阅读范围与访问来源：** 已读初评 作者回应 评审追评及 AC 原始记录；公开 OpenReview 原始记录存档

**机制标签：** `baseline_fairness`、`novelty`、`evaluation`、`ac_summary`

**复核链接：** [重点评审 note](https://openreview.net/forum?id=05hNleYOcG&noteId=KuzTZta1WZ) · [作者回复 1](https://openreview.net/forum?id=05hNleYOcG&noteId=I700mkSVqd) · [作者回复 2](https://openreview.net/forum?id=05hNleYOcG&noteId=PUVaDbNR3R) · [作者回复 3](https://openreview.net/forum?id=05hNleYOcG&noteId=BMapmH5TQ8) · [作者回复 4](https://openreview.net/forum?id=05hNleYOcG&noteId=7uso70xsIZ) · [作者回复 5](https://openreview.net/forum?id=05hNleYOcG&noteId=8VB7vPq3eQ) · [作者回复 6](https://openreview.net/forum?id=05hNleYOcG&noteId=pSKDEAwzQR) · [作者回复 7](https://openreview.net/forum?id=05hNleYOcG&noteId=JZbdflwz6P) · [作者回复 8](https://openreview.net/forum?id=05hNleYOcG&noteId=9ND7NkNOsX) · [作者回复 9](https://openreview.net/forum?id=05hNleYOcG&noteId=7zAAjIW7oX) · [决定](https://openreview.net/forum?id=05hNleYOcG&noteId=Vmg9DHKxnh) · [公开档案](https://huggingface.co/datasets/McGill-NLP/AI-For-Science-Retreat-Data/blob/main/iclr-dataset/iclr_2026_raw.parquet)

## C50

### [Dynamic Neural Fortresses: An Adaptive Shield for Model Extraction Defense](https://openreview.net/forum?id=029hDSVoXK)

**ICLR 2025 · Accept (Poster) · `evidence_exclusion`**

**记录到的变化：** 1→8（AC明确剔除的异常）；其他两人5→6

**证据身份：** 异常或互相冲突的评分证据；PaperCopilot公开评分快照匹配档案，按reviewer局部ID配对；tracing_score=1。快照可能晚于部分更新，不等同于真实初评历史；正文中的明确改分数字以原始note为准。

**原始阻碍：** 设定、强攻击基线、架构保护证据及表述。

**作者动作：** AC总结作者回应解决其他评审的主要问题；本目标评审未公开继续讨论。不能把其巨大改分归于某一句或某个实验。

**评审反馈：** AC称初始1分评审直到催促后突然改为8且没有进一步问题，异常、作为outlier排除；其他review和rebuttal已足以接收。

**选例理由：** Dynamic Neural Fortresses的1→8虽醒目，但AC明确作为异常outlier剔除，且缺对应讨论链；排除为正面逆转确证。

**可迁移机制：** 选案例时先查AC是否采纳该数字、是否有作者动作与评审回应链，再看涨幅。

**必须保留的限制：** 保留异常与其他正常评审证据；论文接收有其他依据，不能据此认定论文低质量或把异常涨幅归功于某句rebuttal。 评分配对档案是采集时点快照，可能晚于部分更新；不作未经核实的真实初始评分向量。

**阅读范围与访问来源：** 关键目标评审的原评→作者逐点回应→追问/再回应完整主链，以及全页评审follow-up、AC meta-review和decision；未声称逐句精读每条无关评论。；公开原始OpenReview记录的McGill-NLP raw parquet（非缺嵌套回复的threads简化文件）

**机制标签：** `ac_summary`、`evaluation`

**复核链接：** [重点评审 note](https://openreview.net/forum?id=029hDSVoXK&noteId=dHvqGcF4MN) · [其他关键 note 2](https://openreview.net/forum?id=029hDSVoXK&noteId=Ef7KCRhqMy) · [其他关键 note 3](https://openreview.net/forum?id=029hDSVoXK&noteId=rvRdbzPCIy) · [公开档案](https://huggingface.co/datasets/McGill-NLP/AI-For-Science-Retreat-Data/blob/main/iclr-dataset/iclr_2025_raw.parquet)

## C51

### [BiGR: Harnessing Binary Latent Codes for Image Generation and Improved Visual Representation Capabilities](https://openreview.net/forum?id=1Z6PSw7OL8)

**ICLR 2025 · Accept (Poster) · `extended_positive`**

**记录到的变化：** 3→6；nzvc 5→6

**证据身份：** 原始讨论与评分快照交叉核对；PaperCopilot公开评分快照匹配档案，按reviewer局部ID配对；tracing_score=0。快照可能晚于部分更新，不等同于真实初评历史；正文中的明确改分数字以原始note为准。

**原始阻碍：** 只做类别条件生成，二进制latent可能仅在简单任务奏效；与LlamaGen对比不公平。

**作者动作：** 补JourneyDB上的text-to-image训练，给出32 A800、62小时、4M数据等限制；提供不同binary维度的reconstruction FID；逐条纠正LlamaGen只生成图像、不能靠prompt做判别的误解。

**评审反馈：** 认可基础研究定位、T2I结果及对LlamaGen的纠正，明确升至6。

**选例理由：** 本人明确升至6，扩展text-to-image检验简单任务局限有用；作为应用范围与误读纠正的扩展。

**可迁移机制：** 补一个能区分适用范围假说的更难任务，给训练资源，再以具体功能事实纠正baseline误读。

**必须保留的限制：** 精确初分来自配对档案时须保留采集时点限制；新增T2I不证明所有条件生成任务都适用。 评分配对档案是采集时点快照，可能晚于部分更新；不作未经核实的真实初始评分向量。

**阅读范围与访问来源：** 关键目标评审的原评→作者逐点回应→追问/再回应完整主链，以及全页评审follow-up、AC meta-review和decision；未声称逐句精读每条无关评论。；公开原始OpenReview记录的McGill-NLP raw parquet（非缺嵌套回复的threads简化文件）

**机制标签：** `claim_scope`、`evaluation`、`baseline_fairness`、`efficiency`

**复核链接：** [重点评审 note](https://openreview.net/forum?id=1Z6PSw7OL8&noteId=QuDXHs2Qhy) · [其他关键 note 2](https://openreview.net/forum?id=1Z6PSw7OL8&noteId=WY4kTOcYKF) · [其他关键 note 3](https://openreview.net/forum?id=1Z6PSw7OL8&noteId=AP7cFusnJW) · [其他关键 note 4](https://openreview.net/forum?id=1Z6PSw7OL8&noteId=aelD0eDtwL) · [公开档案](https://huggingface.co/datasets/McGill-NLP/AI-For-Science-Retreat-Data/blob/main/iclr-dataset/iclr_2025_raw.parquet)

## C52

### [GenSE: Generative Speech Enhancement via Language Models using Hierarchical Modeling](https://openreview.net/forum?id=1p6xFLBU4J)

**ICLR 2025 · Accept (Poster) · `core_positive`**

**记录到的变化：** 3→6；fv2J明确5→6

**证据身份：** 原始讨论与评分快照交叉核对；PaperCopilot公开评分快照匹配档案，按reviewer局部ID配对；tracing_score=1。快照可能晚于部分更新，不等同于真实初评历史；正文中的明确改分数字以原始note为准。

**原始阻碍：** 漏引SpeechX、UniAudio、SingleCodec，缺乏新颖性。

**作者动作：** 承认漏引并补引用；分辨去噪→语义→声学的分层建模与单一LM，波形codec与mel codec、额外reference encoder的差别；承诺把比较进入正文。

**评审反馈：** 批评漏引做法但认可详细比较，将分数调至6；另一评审因SimCodec结果5→6，随后仍追问UTMOS可比性，作者再补解释和实验。

**选例理由：** 本人明确已调到6；漏引并非只补引用，而是机制与任务逐项比较，适合相关工作和新颖性处理。

**可迁移机制：** 承认遗漏后比较建模阶段、token/codec和额外模块，把差异与实验结果写回正文。

**必须保留的限制：** 本人目标6明确；初分路径保留原档案口径。提分后UTMOS可比性追问仍需回答，不能认为已得分便停止修订。 评分配对档案是采集时点快照，可能晚于部分更新；不作未经核实的真实初始评分向量。

**阅读范围与访问来源：** 关键目标评审的原评→作者逐点回应→追问/再回应完整主链，以及全页评审follow-up、AC meta-review和decision；未声称逐句精读每条无关评论。；公开原始OpenReview记录的McGill-NLP raw parquet（非缺嵌套回复的threads简化文件）

**机制标签：** `related_work`、`novelty`、`paper_revision`、`multi_round`

**复核链接：** [核心数值表态](https://openreview.net/forum?id=1p6xFLBU4J&noteId=dNYe7G7eK5) · [重点评审 note](https://openreview.net/forum?id=1p6xFLBU4J&noteId=PdY7uWdRdJ) · [其他关键 note 2](https://openreview.net/forum?id=1p6xFLBU4J&noteId=nsJn0sChe8) · [其他关键 note 4](https://openreview.net/forum?id=1p6xFLBU4J&noteId=sVDlX0JCtO) · [其他关键 note 5](https://openreview.net/forum?id=1p6xFLBU4J&noteId=4PBb3EYELC) · [公开档案](https://huggingface.co/datasets/McGill-NLP/AI-For-Science-Retreat-Data/blob/main/iclr-dataset/iclr_2025_raw.parquet)

## C53

### [CO-MOT: Boosting End-to-end Transformer-based Multi-Object Tracking via Coopetition Label Assignment and Shadow Sets](https://openreview.net/forum?id=0ov0dMQ3mN)

**ICLR 2025 · Accept (Poster) · `core_positive`**

**记录到的变化：** 3→6；另两人5→6

**证据身份：** 原始讨论与评分快照交叉核对；PaperCopilot公开评分快照匹配档案，按reviewer局部ID配对；tracing_score=1。快照可能晚于部分更新，不等同于真实初评历史；正文中的明确改分数字以原始note为准。

**原始阻碍：** 评审认为与去年被拒版本几乎无改进；遗漏新tracker和多场景评价。

**作者动作：** 按去年每项批评列出当前改动及表/图定位：新增数据集、Trackformer与MeMOTR迁移、失败案例、MOT20、消融；补DiffMOT/MambaTrack/TrackSSM比较。

**评审反馈：** 评审重新对比去年版本后认可实验和写作大量改进，虽认为novelty增量但升6；AC记录最终全6。

**选例理由：** 本人明确决定提高到6；重投稿用逐项可定位差异清单改变“没有进步”的判断，补充其他核心例未覆盖的场景。

**可迁移机制：** 按上轮每项批评列当前改动、数据集、迁移与失败案例，标出既有内容和新补结果。

**必须保留的限制：** 不能假定新颖性异议全消失；评分档案只作路径核对，不能把采集快照泛称首次初评。 评分配对档案是采集时点快照，可能晚于部分更新；不作未经核实的真实初始评分向量。

**阅读范围与访问来源：** 关键目标评审的原评→作者逐点回应→追问/再回应完整主链，以及全页评审follow-up、AC meta-review和decision；未声称逐句精读每条无关评论。；公开原始OpenReview记录的McGill-NLP raw parquet（非缺嵌套回复的threads简化文件）

**机制标签：** `paper_revision`、`evaluation`、`related_work`、`negative_results`

**复核链接：** [核心数值表态](https://openreview.net/forum?id=0ov0dMQ3mN&noteId=HwvsrDiHrd) · [重点评审 note](https://openreview.net/forum?id=0ov0dMQ3mN&noteId=WxhCpMIhZG) · [其他关键 note 2](https://openreview.net/forum?id=0ov0dMQ3mN&noteId=NZCrrwWozG) · [其他关键 note 4](https://openreview.net/forum?id=0ov0dMQ3mN&noteId=w3UXdIZK3C) · [公开档案](https://huggingface.co/datasets/McGill-NLP/AI-For-Science-Retreat-Data/blob/main/iclr-dataset/iclr_2025_raw.parquet)

## C54

### [Variational Bayesian Pseudo-Coreset](https://openreview.net/forum?id=0NAVeUm7sk)

**ICLR 2025 · Accept (Poster) · `qualified_positive`**

**记录到的变化：** sqcH 5→8；hhFq 5→8；8mt5 5→6

**证据身份：** 原始讨论与评分快照交叉核对；PaperCopilot公开评分快照匹配档案，按reviewer局部ID配对；tracing_score=1。快照可能晚于部分更新，不等同于真实初评历史；正文中的明确改分数字以原始note为准。

**原始阻碍：** 强调大数据/continual learning但只在toy数据验证；Gaussian likelihood与VI选择理由不足。

**作者动作：** 补ImageWoof、resized ImageNet1k和class-incremental CIFAR100；表中同时报告OOM和准确率/NLL；解释Laplace/EM替代方案的Hessian与双层优化代价。

**评审反馈：** sqcH明确因nontrivial任务可扩展性与近似过程解释而转accept；AC还折扣两份高度相似评审意见，自己阅读后支持接收。

**选例理由：** 规模实验与OOM报告有积极学习价值，但存在被AC折扣的高度相似评审，数字路径又需快照配对；保留为带来源限定辅例。

**可迁移机制：** 将大数据/continual动机落实到非toy任务，同时报告OOM、准确率与近似计算代价。

**必须保留的限制：** 不能把相似评审当独立投票或推测其生成方式；不据缺少本人数字短引判定原帖不存在，只按当前主表强度引用。 评分配对档案是采集时点快照，可能晚于部分更新；不作未经核实的真实初始评分向量。

**阅读范围与访问来源：** 关键目标评审的原评→作者逐点回应→追问/再回应完整主链，以及全页评审follow-up、AC meta-review和decision；未声称逐句精读每条无关评论。；公开原始OpenReview记录的McGill-NLP raw parquet（非缺嵌套回复的threads简化文件）

**机制标签：** `evaluation`、`efficiency`、`claim_scope`、`ac_summary`

**复核链接：** [重点评审 note](https://openreview.net/forum?id=0NAVeUm7sk&noteId=L8nLEBXLLf) · [其他关键 note 2](https://openreview.net/forum?id=0NAVeUm7sk&noteId=p4WQ4Ougig) · [其他关键 note 3](https://openreview.net/forum?id=0NAVeUm7sk&noteId=LXy0cDndsp) · [其他关键 note 4](https://openreview.net/forum?id=0NAVeUm7sk&noteId=F0CL7Zl9No) · [其他关键 note 5](https://openreview.net/forum?id=0NAVeUm7sk&noteId=CSMuGMIGoV) · [公开档案](https://huggingface.co/datasets/McGill-NLP/AI-For-Science-Retreat-Data/blob/main/iclr-dataset/iclr_2025_raw.parquet)

## C55

### [Generation and Comprehension Hand-in-Hand: Vision-guided Expression Diffusion for Boosting Referring Expression Generation and Comprehension](https://openreview.net/forum?id=1qbZekXGrp)

**ICLR 2025 · Accept (Poster) · `extended_positive`**

**记录到的变化：** XHYa 3→6（未文字回应，AC确认）；5XtB明确5→6

**证据身份：** AC确认历史；快照交叉核对；PaperCopilot公开评分快照匹配档案，按reviewer局部ID配对；tracing_score=-1。快照可能晚于部分更新，不等同于真实初评历史；正文中的明确改分数字以原始note为准。

**原始阻碍：** 遗漏CCL等最近基线，失败案例与成本/数据规模不清。

**作者动作：** 补CCL对照与机制区别；定位原文已有失败案例；明确1.2B参数、训练硬件时间、DDPM/DDIM延迟以及30%选择策略的实际样本数。

**评审反馈：** XHYa未回文字但AC确认提分；5XtB明确5→6，保留novelty疑问但承认效果已证明；AC接受。

**选例理由：** 5XtB有明确5→6，成本与样本量口径有用；主要3→6路径由AC确认且无本人文字，使用时限定到各自来源。

**可迁移机制：** 补近邻基线，报告真实参数/训练/推理账单和数据选择后的实际样本数。

**必须保留的限制：** XHYa的动机不可由沉默推断；不要把5XtB的本人证据借给XHYa的AC记录。 评分配对档案是采集时点快照，可能晚于部分更新；不作未经核实的真实初始评分向量。

**阅读范围与访问来源：** 关键目标评审的原评→作者逐点回应→追问/再回应完整主链，以及全页评审follow-up、AC meta-review和decision；未声称逐句精读每条无关评论。；公开原始OpenReview记录的McGill-NLP raw parquet（非缺嵌套回复的threads简化文件）

**机制标签：** `related_work`、`evaluation`、`efficiency`、`ac_summary`

**复核链接：** [重点评审 note](https://openreview.net/forum?id=1qbZekXGrp&noteId=IUT5MHiWcE) · [其他关键 note 2](https://openreview.net/forum?id=1qbZekXGrp&noteId=DKU5Z0Wj4g) · [其他关键 note 3](https://openreview.net/forum?id=1qbZekXGrp&noteId=AcA0rRQE7t) · [其他关键 note 4](https://openreview.net/forum?id=1qbZekXGrp&noteId=Ey5SGxWqd6) · [公开档案](https://huggingface.co/datasets/McGill-NLP/AI-For-Science-Retreat-Data/blob/main/iclr-dataset/iclr_2025_raw.parquet)

## C56

### [Shallow Diffuse: Robust and Invisible Watermarking through Low-Dimensional Subspaces in Diffusion Models](https://openreview.net/forum?id=1IwoEFyErz)

**ICLR 2025 · Reject · `outcome_counterexample`**

**记录到的变化：** 四名评审均5→6，最终Reject

**证据身份：** 原始讨论与评分快照交叉核对；PaperCopilot公开评分快照匹配档案，按reviewer局部ID配对；tracing_score=1。快照可能晚于部分更新，不等同于真实初评历史；正文中的明确改分数字以原始note为准。

**原始阻碍：** robustness和多用户适用性是否足够；图像一致性、质量与攻击基线。

**作者动作：** 补公平生成seed设定、可视化、adversarial attacks和sampling ablations，解释CLIP与image consistency目标；多用户试验仍不足。

**评审反馈：** 全部提分到6；a7Ds仍强调多用户是核心局限。AC逐表检查发现部分robustness/key identification不如RingID，且攻击类型太少，最终拒绝。

**选例理由：** Shallow Diffuse全部评审提到6仍Reject，是“分数共识不等于关键主张成立”的强反例。

**可迁移机制：** 逐表核对鲁棒性和多key结果，准确报告混合胜负，避免摘要宣称全面优越。

**必须保留的限制：** 多用户核心限制仍在；不把拒稿笼统归因于AC不理会评审，也不因反例用途否定论文全部贡献。 评分配对档案是采集时点快照，可能晚于部分更新；不作未经核实的真实初始评分向量。

**阅读范围与访问来源：** 关键目标评审的原评→作者逐点回应→追问/再回应完整主链，以及全页评审follow-up、AC meta-review和decision；未声称逐句精读每条无关评论。；公开原始OpenReview记录的McGill-NLP raw parquet（非缺嵌套回复的threads简化文件）

**机制标签：** `evaluation`、`negative_results`、`claim_scope`、`ac_summary`

**复核链接：** [重点评审 note](https://openreview.net/forum?id=1IwoEFyErz&noteId=E7x0QUpuNC) · [其他关键 note 2](https://openreview.net/forum?id=1IwoEFyErz&noteId=o0UZfmtQSu) · [其他关键 note 3](https://openreview.net/forum?id=1IwoEFyErz&noteId=rnme5uwhgV) · [其他关键 note 4](https://openreview.net/forum?id=1IwoEFyErz&noteId=JIwq2WKsW3) · [其他关键 note 5](https://openreview.net/forum?id=1IwoEFyErz&noteId=vZafEQQebE) · [公开档案](https://huggingface.co/datasets/McGill-NLP/AI-For-Science-Retreat-Data/blob/main/iclr-dataset/iclr_2025_raw.parquet)

## C57

### [GRIC: General Representation and Informative Content for Enhanced Out-of-Distribution Detection](https://openreview.net/forum?id=0owAtTCOlU)

**ICLR 2025 · Reject · `outcome_counterexample`**

**记录到的变化：** jgok和Z3Z1各3→6，DnKU5→6，V9Pr3→5；最终Reject

**证据身份：** 原始讨论与评分快照交叉核对；PaperCopilot公开评分快照匹配档案，按reviewer局部ID配对；tracing_score=1。快照可能晚于部分更新，不等同于真实初评历史；正文中的明确改分数字以原始note为准。

**原始阻碍：** zero-shot定义不成立：PCA使用ID图像；缺few-shot强基线；大幅性能提升表述混淆任务和绝对百分点。

**作者动作：** 先承诺改文和补基线但未上传；被评审明确指出后上传蓝色修订；继续补PCA/IP协同和few-shot对比。

**评审反馈：** 两位评审逐步提分；AC仍认为需把问题设定和实验整体改成few-shot并重写讨论，重大剩余问题导致拒稿。

**选例理由：** GRIC多数负转正仍Reject，因为zero-shot定义与实验体系需整体重构；用于展示核心设定错误不能被分数掩盖。

**可迁移机制：** 任务定义变化后同步调整baseline、数据使用和主张，并将承诺落实为已上传的可核查修订。

**必须保留的限制：** PCA用了ID图像这一设定问题未被简单措辞修复；已承诺、已完成和评审确认必须区分。 评分配对档案是采集时点快照，可能晚于部分更新；不作未经核实的真实初始评分向量。

**阅读范围与访问来源：** 关键目标评审的原评→作者逐点回应→追问/再回应完整主链，以及全页评审follow-up、AC meta-review和decision；未声称逐句精读每条无关评论。；公开原始OpenReview记录的McGill-NLP raw parquet（非缺嵌套回复的threads简化文件）

**机制标签：** `claim_scope`、`baseline_fairness`、`paper_revision`、`ac_summary`

**复核链接：** [重点评审 note](https://openreview.net/forum?id=0owAtTCOlU&noteId=ykOuNZJSUs) · [其他关键 note 2](https://openreview.net/forum?id=0owAtTCOlU&noteId=sqemjGBZqI) · [其他关键 note 3](https://openreview.net/forum?id=0owAtTCOlU&noteId=wNU4hgxsBf) · [其他关键 note 4](https://openreview.net/forum?id=0owAtTCOlU&noteId=vxwtDPAoHz) · [其他关键 note 5](https://openreview.net/forum?id=0owAtTCOlU&noteId=9r5no89oWh) · [其他关键 note 6](https://openreview.net/forum?id=0owAtTCOlU&noteId=0H74swEpfF) · [公开档案](https://huggingface.co/datasets/McGill-NLP/AI-For-Science-Retreat-Data/blob/main/iclr-dataset/iclr_2025_raw.parquet)

## C58

### [Multi-modal Agent Tuning: Building a VLM-Driven Agent for Efficient Tool Usage](https://openreview.net/forum?id=0bmGL4q7vJ)

**ICLR 2025 · Accept (Spotlight) · `qualified_positive`**

**记录到的变化：** snR1 5→8；4Mmx5→6

**证据身份：** 原始讨论与评分快照交叉核对；PaperCopilot公开评分快照匹配档案，按reviewer局部ID配对；tracing_score=1。快照可能晚于部分更新，不等同于真实初评历史；正文中的明确改分数字以原始note为准。

**原始阻碍：** 生成文件可行性、五人用户研究可能偏差、GAIA不如GPT-4o agent、数据统计20K/28K/15K不一致。

**作者动作：** 明确不生成视频；将用户评估扩到30名有AI/编程经验者，混合盲评；加入相同模型量级GAIA baselines；承认图中重复计数并更正20K任务和15K文件关系。

**评审反馈：** snR1明确提分；其他评审确认更多参与者与匹配模型比较解决问题；AC摘要认可新增用户研究、跨backbone和开源模型生成证据。

**选例理由：** 盲评扩至30人、纠正数据统计和匹配模型对照很有价值；但主表所示本人短引仅说加分，5→8目标仍需按快照来源陈述。

**可迁移机制：** 扩大并盲化用户研究，统一任务/文件去重口径，按相同backbone比较agent能力。

**必须保留的限制：** 不能把5→8写成该短引本人给出的数字；用户样本扩大也不等于代表所有用户。 评分配对档案是采集时点快照，可能晚于部分更新；不作未经核实的真实初始评分向量。

**阅读范围与访问来源：** 关键目标评审的原评→作者逐点回应→追问/再回应完整主链，以及全页评审follow-up、AC meta-review和decision；未声称逐句精读每条无关评论。；公开原始OpenReview记录的McGill-NLP raw parquet（非缺嵌套回复的threads简化文件）

**机制标签：** `evaluation`、`benchmark_value`、`baseline_fairness`、`paper_revision`

**复核链接：** [重点评审 note](https://openreview.net/forum?id=0bmGL4q7vJ&noteId=lKbzXFBqf9) · [其他关键 note 2](https://openreview.net/forum?id=0bmGL4q7vJ&noteId=sUJc3fuXIi) · [其他关键 note 3](https://openreview.net/forum?id=0bmGL4q7vJ&noteId=ZKtKUv0PgP) · [其他关键 note 4](https://openreview.net/forum?id=0bmGL4q7vJ&noteId=BPcmgjbKf1) · [其他关键 note 5](https://openreview.net/forum?id=0bmGL4q7vJ&noteId=mw69OYJyo7) · [公开档案](https://huggingface.co/datasets/McGill-NLP/AI-For-Science-Retreat-Data/blob/main/iclr-dataset/iclr_2025_raw.parquet)

## C59

### [NetMoE: Accelerating MoE Training through Dynamic Sample Placement](https://openreview.net/forum?id=1qP3lsatCR)

**ICLR 2025 · Accept (Spotlight) · `evidence_exclusion`**

**记录到的变化：** 评分档案RL6X 3→6；EW5K6→8；但AC回顾称initial 6–8，与档案冲突

**证据身份：** 异常或互相冲突的评分证据；PaperCopilot公开评分快照匹配档案，按reviewer局部ID配对；tracing_score=0。快照可能晚于部分更新，不等同于真实初评历史；正文中的明确改分数字以原始note为准。

**原始阻碍：** inter-node主导假设在其他硬件配置下是否成立，KM立方复杂度是否适合大模型，设备/节点数变化缺实验。

**作者动作：** 给出带宽与通信量实测、2/4/8 GPUs per node实验；解释KM复杂度取决于每卡microbatch而非参数量；承认少节点多设备情境可能不适用，再列出实际集群条件并补入附录。

**评审反馈：** RL6X感谢实际场景解释；EW5K明确升accept；AC接受但初始分数概述与独立档案不一致。

**选例理由：** NetMoE配对档案初分与AC回顾冲突尚未消解；不选为最强数字逆转确证，但保留硬件边界与实测机制。

**可迁移机制：** 先承认反例硬件条件，再测带宽/通信/设备布局支持适用域；数据冲突并列呈现。

**必须保留的限制：** 排除的是未经稳定核验的初末数字叙事，不是论文、接收决定或实测价值；不得挑更戏剧化的一组数字。 评分配对档案是采集时点快照，可能晚于部分更新；不作未经核实的真实初始评分向量。

**阅读范围与访问来源：** 关键目标评审的原评→作者逐点回应→追问/再回应完整主链，以及全页评审follow-up、AC meta-review和decision；未声称逐句精读每条无关评论。；公开原始OpenReview记录的McGill-NLP raw parquet（非缺嵌套回复的threads简化文件）

**机制标签：** `efficiency`、`claim_scope`、`negative_results`、`ac_summary`

**复核链接：** [重点评审 note](https://openreview.net/forum?id=1qP3lsatCR&noteId=m4l4gosFxJ) · [其他关键 note 2](https://openreview.net/forum?id=1qP3lsatCR&noteId=sI1NXB1t1y) · [其他关键 note 3](https://openreview.net/forum?id=1qP3lsatCR&noteId=AyVy3Wctnc) · [其他关键 note 4](https://openreview.net/forum?id=1qP3lsatCR&noteId=PKXk3fkshJ) · [其他关键 note 5](https://openreview.net/forum?id=1qP3lsatCR&noteId=fPubePdR0e) · [其他关键 note 6](https://openreview.net/forum?id=1qP3lsatCR&noteId=wqzkGvH7Go) · [公开档案](https://huggingface.co/datasets/McGill-NLP/AI-For-Science-Retreat-Data/blob/main/iclr-dataset/iclr_2025_raw.parquet)

## C60

### [ThunderKittens: Simple, Fast, and $\textit{Adorable}$ Kernels](https://openreview.net/forum?id=0fJfVOSUra)

**ICLR 2025 · Accept (Spotlight) · `qualified_positive`**

**记录到的变化：** nd8y和ANEJ均5→8

**证据身份：** 原始讨论与评分快照交叉核对；PaperCopilot公开评分快照匹配档案，按reviewer局部ID配对；tracing_score=1。快照可能晚于部分更新，不等同于真实初评历史；正文中的明确改分数字以原始note为准。

**原始阻碍：** 适用硬件/precision/kernel狭窄，和CUTLASS/Triton差别不明，GPU技术表述及runtime复现细节不足。

**作者动作：** 补FP8 GEMM、causal attention、不整齐tile、4090和Apple M2；给Feature比较表；补microbenchmark和官方profiling文档纠正技术误解，同时承认非原创roofline模型、部分性能差距和单GPU范围。

**评审反馈：** ANEJ认可新实验和比较表，要求放入正文和固定Triton commit；nd8y多轮技术交流后认为多数问题解决并提分。

**选例理由：** microbenchmark与官方技术文档是好的纠正误读方式，但主表5→8依赖配对档案且本人短引未给目标，列为带来源限定的硬件辅例。

**可迁移机制：** 给代表性硬件/precision/kernel测试和feature表，固定实现commit，承认非原创分析与覆盖限制。

**必须保留的限制：** 不能将引用文档当权威压人；精确分数保留快照来源，单GPU证据不扩展成分布式普遍结论。 评分配对档案是采集时点快照，可能晚于部分更新；不作未经核实的真实初始评分向量。

**阅读范围与访问来源：** 关键目标评审的原评→作者逐点回应→追问/再回应完整主链，以及全页评审follow-up、AC meta-review和decision；未声称逐句精读每条无关评论。；公开原始OpenReview记录的McGill-NLP raw parquet（非缺嵌套回复的threads简化文件）

**机制标签：** `efficiency`、`evaluation`、`related_work`、`claim_scope`

**复核链接：** [重点评审 note](https://openreview.net/forum?id=0fJfVOSUra&noteId=rx8VtsHol3) · [其他关键 note 2](https://openreview.net/forum?id=0fJfVOSUra&noteId=e5jt5BEgRN) · [其他关键 note 3](https://openreview.net/forum?id=0fJfVOSUra&noteId=kK1epCZp0Y) · [其他关键 note 4](https://openreview.net/forum?id=0fJfVOSUra&noteId=lWMAnryuEJ) · [其他关键 note 5](https://openreview.net/forum?id=0fJfVOSUra&noteId=sUiVk6sFoM) · [其他关键 note 6](https://openreview.net/forum?id=0fJfVOSUra&noteId=T1Nt0ZMchc) · [其他关键 note 7](https://openreview.net/forum?id=0fJfVOSUra&noteId=XrGj1YkI1z) · [公开档案](https://huggingface.co/datasets/McGill-NLP/AI-For-Science-Retreat-Data/blob/main/iclr-dataset/iclr_2025_raw.parquet)

## C61

### [Bayesian Optimization via Continual Variational Last Layer Training](https://openreview.net/forum?id=1jcnvghayD)

**ICLR 2025 · Accept (Spotlight) · `qualified_positive`**

**记录到的变化：** asqH 5→8；wtu3 3→5；最终仍保留一张5分而Spotlight

**证据身份：** 原始讨论与评分快照交叉核对；PaperCopilot公开评分快照匹配档案，按reviewer局部ID配对；tracing_score=0。快照可能晚于部分更新，不等同于真实初评历史；正文中的明确改分数字以原始note为准。

**原始阻碍：** 以效率为动机却没有wall-clock收益；LLLA噪声更敏感缺证据；GP lengthscale baseline可能弱；early stopping optimal说法过强。

**作者动作：** 补surrogate fit time与BO性能、按D-scaled hyperprior重跑GP并移除原lengthscale限制；将optimal改为good empirical performance；首轮噪声图未支持论点后承认不足，补多噪声级别并愿意撤掉过强结论。

**评审反馈：** asqH继续追问baseline初始化和噪声解释，最终评分档案5→8；AC确认内部讨论全员支持，即使一人分数未完全更新，最终5/8/8/8。

**选例理由：** 时间—性能曲线、重跑强GP和愿撤过强结论值得学习；提分数值来自评分档案，且接收仍有5分，适合作为混合状态辅例。

**可迁移机制：** 为效率主张补wall-clock，公平调baseline；遇图不支持噪声主张时降格表述并补多噪声设置。

**必须保留的限制：** 不能把最终支持等同全部分数超过阈值；5→8的动机与数值要分别保留来源。 评分配对档案是采集时点快照，可能晚于部分更新；不作未经核实的真实初始评分向量。

**阅读范围与访问来源：** 关键目标评审的原评→作者逐点回应→追问/再回应完整主链，以及全页评审follow-up、AC meta-review和decision；未声称逐句精读每条无关评论。；公开原始OpenReview记录的McGill-NLP raw parquet（非缺嵌套回复的threads简化文件）

**机制标签：** `efficiency`、`baseline_fairness`、`negative_results`、`claim_scope`、`ac_summary`

**复核链接：** [重点评审 note](https://openreview.net/forum?id=1jcnvghayD&noteId=lGopSQgMyt) · [其他关键 note 2](https://openreview.net/forum?id=1jcnvghayD&noteId=VuePiBIDLB) · [其他关键 note 3](https://openreview.net/forum?id=1jcnvghayD&noteId=Mi1QCbqkiN) · [其他关键 note 4](https://openreview.net/forum?id=1jcnvghayD&noteId=tCI4DS6BLD) · [其他关键 note 5](https://openreview.net/forum?id=1jcnvghayD&noteId=v4sVduorwX) · [公开档案](https://huggingface.co/datasets/McGill-NLP/AI-For-Science-Retreat-Data/blob/main/iclr-dataset/iclr_2025_raw.parquet)

## C62

### [Large Language Models Cannot Self-Correct Reasoning Yet](https://openreview.net/forum?id=IkmD3fKBPQ)

**ICLR 2024 · Accept (Poster) · `qualified_positive`**

**记录到的变化：** 3→6；N1pE 6→8

**证据身份：** 本人条件性表态；另有明确提分；原始评审文字明确No3p 3→6（b2CsLfx0dr）及N1pE 6→8（DFtNcvk87n）。PaperCopilot本例tracing_score=2，高于作者建议的<=1；N1pE快照为8→8，未覆盖其真正初评分。不使用快照均分作为初评。

**原始阻碍：** 标题和结论超出两类任务与特定提示的证据；带偏见反馈可能造成失败。

**作者动作：** 补GPT-4/GPT-4-Turbo、Llama-2-70B和更中性提示实验；承认intrinsic self-correction的范围，承诺将标题改为Reexamining...。

**评审反馈：** No3p明确表示仅在标题承诺成立的前提下从3升6；N1pE因新增实验从6升8；仍有评审维持原分。

**选例理由：** 同时含有条件3→6和另一位明确6→8，且快照与本人初分冲突；适合范围收窄及证据分层，不作单一无条件逆转模板。

**可迁移机制：** 用中性prompt和更多模型检验边界，将大标题收窄到intrinsic self-correction的受测范围。

**必须保留的限制：** No3p路径附标题承诺；N1pE6→8可独立引用但原本正面。不能把8→8采集快照改成与原话同等的历史真值。 N1pE原始note明确6→8，评分档案快照却为8→8；以原始note的直接陈述报告路径。tracing_score=2，本例不能用通用<=1标签。

**阅读范围与访问来源：** 关键目标评审的原评→作者逐点回应→追问/再回应完整主链，以及全页评审follow-up、AC meta-review和decision；未声称逐句精读每条无关评论。；公开原始OpenReview记录的MlouisBE研究档案（非研究者生成的摘要）

**机制标签：** `claim_scope`、`evaluation`、`paper_revision`、`ac_summary`

**复核链接：** [重点评审 note](https://openreview.net/forum?id=IkmD3fKBPQ&noteId=b2CsLfx0dr) · [其他关键 note 2](https://openreview.net/forum?id=IkmD3fKBPQ&noteId=5NiRq3ATEJ) · [其他关键 note 3](https://openreview.net/forum?id=IkmD3fKBPQ&noteId=DFtNcvk87n) · [其他关键 note 4](https://openreview.net/forum?id=IkmD3fKBPQ&noteId=T57BjkGGNR) · [公开档案](https://huggingface.co/datasets/MlouisBE/iclr-rebuttal-analysis/blob/main/data/raw/ICLR.cc_2024.json)

## C63

### [Adaptive Rational Activations to Boost Deep Reinforcement Learning](https://openreview.net/forum?id=g90ysX1sVs)

**ICLR 2024 · Accept (Spotlight) · `extended_positive`**

**记录到的变化：** 3→6；两人5→8；一人6→8

**证据身份：** 原始讨论与评分快照交叉核对；PaperCopilot公开评分快照匹配档案，按reviewer局部ID配对；tracing_score=0。快照可能晚于部分更新，不等同于真实初评历史；正文中的明确改分数字以原始note为准。

**原始阻碍：** 结构和定理不清；收益可能只是增加参数；plasticity解释缺机制证据。

**作者动作：** 给出架构图、每层/跨层共享定义，明确只多10或40参数；修正定理条件；补permuted-MNIST、冻结activation和相关baseline/参数容量对照。

**评审反馈：** 其他三位评审明确表示新实验、CReLU对照、图示和相关工作解决顾虑并提分；AC确认所有评审转为支持。

**选例理由：** 参数量/容量/机制分开的消融很有判别力；在核心案例已覆盖相同原则后保留为RL扩展。

**可迁移机制：** 用共享定义和架构图固定参数预算，结合冻结activation、CReLU与plasticity任务隔离解释。

**必须保留的限制：** 具体多评审数字按原notes和快照各自来源，不把全部变化归于单个消融；新增条件须写回定理。 评分配对档案是采集时点快照，可能晚于部分更新；不作未经核实的真实初始评分向量。

**阅读范围与访问来源：** 关键目标评审的原评→作者逐点回应→追问/再回应完整主链，以及全页评审follow-up、AC meta-review和decision；未声称逐句精读每条无关评论。；公开原始OpenReview记录的MlouisBE研究档案（非研究者生成的摘要）

**机制标签：** `evaluation`、`baseline_fairness`、`theory_repair`、`paper_revision`

**复核链接：** [重点评审 note](https://openreview.net/forum?id=g90ysX1sVs&noteId=lJPa2kx2YJ) · [其他关键 note 2](https://openreview.net/forum?id=g90ysX1sVs&noteId=jhlZVaJRZ1) · [其他关键 note 3](https://openreview.net/forum?id=g90ysX1sVs&noteId=fzmQUjdWUB) · [其他关键 note 4](https://openreview.net/forum?id=g90ysX1sVs&noteId=jqi5D1sWxt) · [其他关键 note 5](https://openreview.net/forum?id=g90ysX1sVs&noteId=OU3E6fNuC6) · [公开档案](https://huggingface.co/datasets/MlouisBE/iclr-rebuttal-analysis/blob/main/data/raw/ICLR.cc_2024.json)

## C64

### [PF-LRM: Pose-Free Large Reconstruction Model for Joint Pose and Shape Prediction](https://openreview.net/forum?id=noe76eRcPC)

**ICLR 2024 · Accept (Spotlight) · `core_positive`**

**记录到的变化：** 3→8；T3us 5→8；另一评审先降后回升

**证据身份：** 原始讨论与评分快照交叉核对；PaperCopilot公开评分快照匹配档案，按reviewer局部ID配对；tracing_score=0。快照可能晚于部分更新，不等同于真实初评历史；正文中的明确改分数字以原始note为准。

**原始阻碍：** 用更大训练数据的方法与旧checkpoint比较，无法区分方法收益与数据规模；pose-free仅推理阶段。

**作者动作：** 首轮以cross-dataset generalization辩护未说服评审；随后真正用相同Objaverse数据重训RelPose++，报告三套测试集；补novel-view PSNR，明确训练需要pose，增加limitations并说明FORGE未能扩展的限制。

**评审反馈：** XwFE和另一评审先坚持公平比较问题；看到重训表后明确称实验支持主张并升到8；AC采纳该解决链。

**选例理由：** 本人明确提高到8；首轮泛化辩护不够、同数据真正重训baseline后才认可，是最直接的公平比较范例。

**可迁移机制：** 锁定数据规模这一混杂因素，用同一训练数据重训最接近baseline，并在相同测试集比较。

**必须保留的限制：** pose-free仅推理成立，训练仍用pose；快照起点保留采集限制，不能把更高数据预算当方法优势。 评分配对档案是采集时点快照，可能晚于部分更新；不作未经核实的真实初始评分向量。

**阅读范围与访问来源：** 关键目标评审的原评→作者逐点回应→追问/再回应完整主链，以及全页评审follow-up、AC meta-review和decision；未声称逐句精读每条无关评论。；公开原始OpenReview记录的MlouisBE研究档案（非研究者生成的摘要）

**机制标签：** `baseline_fairness`、`multi_round`、`claim_scope`、`evaluation`

**复核链接：** [核心数值表态](https://openreview.net/forum?id=noe76eRcPC&noteId=hxlzqg9zyV) · [重点评审 note](https://openreview.net/forum?id=noe76eRcPC&noteId=mhgl0z4oWL) · [其他关键 note 2](https://openreview.net/forum?id=noe76eRcPC&noteId=9jEHGYCXUZ) · [其他关键 note 3](https://openreview.net/forum?id=noe76eRcPC&noteId=HH9Glybycm) · [其他关键 note 4](https://openreview.net/forum?id=noe76eRcPC&noteId=hMwClt2i9C) · [其他关键 note 6](https://openreview.net/forum?id=noe76eRcPC&noteId=SizcooUD6c) · [公开档案](https://huggingface.co/datasets/MlouisBE/iclr-rebuttal-analysis/blob/main/data/raw/ICLR.cc_2024.json)

## C65

### [Learning Delays in Spiking Neural Networks using Dilated Convolutions with Learnable Spacings](https://openreview.net/forum?id=4r2ybzJnmN)

**ICLR 2024 · Accept (Poster) · `qualified_positive`**

**记录到的变化：** 3→8；Wbur 3→6

**证据身份：** 原始讨论与评分快照交叉核对；PaperCopilot公开评分快照匹配档案，按reviewer局部ID配对；tracing_score=0。快照可能晚于部分更新，不等同于真实初评历史；正文中的明确改分数字以原始note为准。

**原始阻碍：** 贡献只在SNN圈内；未与标准temporal convolution比较；SOTA任务不一致；motivation过宽。

**作者动作：** 补标准dense temporal convolution对照，解释11类与35类GSC的差异，补ablation并澄清LIF self-recurrence；但一段将评审批评归为不喜欢SNN的回复被强烈反驳。

**评审反馈：** 评审明确批评作者aggressive style和曲解其观点；仍因新增标准卷积比较使更广泛贡献成立而提高分数。

**选例理由：** 3→8虽强，但评审明确批评aggressive style；只保留新增标准卷积对照的机制，不将整段回复作为可模仿正面范本。

**可迁移机制：** 面对领域局限用通用baseline建立更广泛贡献，澄清数据集任务类别与模型机制。

**必须保留的限制：** 不能从提分推导强硬/揣测评审动机有效；该次认可主要对应技术证据，语气反而受批评。 评分配对档案是采集时点快照，可能晚于部分更新；不作未经核实的真实初始评分向量。

**阅读范围与访问来源：** 关键目标评审的原评→作者逐点回应→追问/再回应完整主链，以及全页评审follow-up、AC meta-review和decision；未声称逐句精读每条无关评论。；公开原始OpenReview记录的MlouisBE研究档案（非研究者生成的摘要）

**机制标签：** `baseline_fairness`、`evaluation`、`novelty`、`claim_scope`

**复核链接：** [重点评审 note](https://openreview.net/forum?id=4r2ybzJnmN&noteId=YHNDSBss1E) · [其他关键 note 2](https://openreview.net/forum?id=4r2ybzJnmN&noteId=WoICQPiMGC) · [其他关键 note 3](https://openreview.net/forum?id=4r2ybzJnmN&noteId=3d13F214ha) · [其他关键 note 4](https://openreview.net/forum?id=4r2ybzJnmN&noteId=vmivtmzvTZ) · [其他关键 note 5](https://openreview.net/forum?id=4r2ybzJnmN&noteId=egVkumSyY3) · [公开档案](https://huggingface.co/datasets/MlouisBE/iclr-rebuttal-analysis/blob/main/data/raw/ICLR.cc_2024.json)

## C66

### [Open the Black Box: Step-based Policy Updates for Temporally-Correlated Episodic Reinforcement Learning](https://openreview.net/forum?id=mnipav175N)

**ICLR 2024 · Accept (Poster) · `extended_positive`**

**记录到的变化：** 两人3→6，两人5→6；全部升分

**证据身份：** 原始讨论与评分快照交叉核对；PaperCopilot公开评分快照匹配档案，按reviewer局部ID配对；tracing_score=1。快照可能晚于部分更新，不等同于真实初评历史；正文中的明确改分数字以原始note为准。

**原始阻碍：** 增量贡献不清、full covariance收益缺本方法直接ablation、训练代价不明。

**作者动作：** 第一轮补实验仍留下full covariance疑问；第二轮直接比较TCE Cov vs TCE Std并报告约10%训练时间差，解释参数空间和轨迹空间复杂度；重整论文并补smoothness等实验。

**评审反馈：** psBV在第二轮明确顾虑已解并提分；dLeV虽升6但仍保留4/50任务零成功率问题；AC明确记录四位初末分数。

**选例理由：** full与diagonal covariance的直接对照和训练代价是优秀最小实验，可作核心多轮例的机器人方向扩展。

**可迁移机制：** 将剩余唯一问题化成同方法的移除/替代实验，同时报告性能和训练时间。

**必须保留的限制：** 全员数字变化按AC回顾/原notes来源；仍有4/50任务零成功率，不得总结所有缺陷全解。 评分配对档案是采集时点快照，可能晚于部分更新；不作未经核实的真实初始评分向量。

**阅读范围与访问来源：** 关键目标评审的原评→作者逐点回应→追问/再回应完整主链，以及全页评审follow-up、AC meta-review和decision；未声称逐句精读每条无关评论。；公开原始OpenReview记录的MlouisBE研究档案（非研究者生成的摘要）

**机制标签：** `evaluation`、`multi_round`、`efficiency`、`negative_results`、`ac_summary`

**复核链接：** [重点评审 note](https://openreview.net/forum?id=mnipav175N&noteId=DFn01HHdOK) · [其他关键 note 2](https://openreview.net/forum?id=mnipav175N&noteId=k0ZYWyKXj6) · [其他关键 note 3](https://openreview.net/forum?id=mnipav175N&noteId=Sam7nUmlZu) · [其他关键 note 4](https://openreview.net/forum?id=mnipav175N&noteId=X9AIY6u7wu) · [其他关键 note 5](https://openreview.net/forum?id=mnipav175N&noteId=88D998ZEh1) · [公开档案](https://huggingface.co/datasets/MlouisBE/iclr-rebuttal-analysis/blob/main/data/raw/ICLR.cc_2024.json)

## C67

### [Teaching Large Language Models to Self-Debug](https://openreview.net/forum?id=KuPixIqPiq)

**ICLR 2024 · Accept (Poster) · `core_positive`**

**记录到的变化：** hHB2明确3→5→6；AdYB 3→6

**证据身份：** 原始讨论与评分快照交叉核对；PaperCopilot公开评分快照匹配档案，按reviewer局部ID配对；tracing_score=0。快照可能晚于部分更新，不等同于真实初评历史；正文中的明确改分数字以原始note为准。

**原始阻碍：** 2–3%收益可能只是prompt波动；基线采样次数不公平；unit test泄漏误读；正文可读性差。

**作者动作：** 先把prompt图和表格设置移入主文，解决写作使3→5；补100样本baseline与8样本self-debug比较仍未直接回答prompt问题；随后对同一弱化prompt做配对试验，仍有2.1%收益；另按评审建议补第二次重采样baseline。

**评审反馈：** hHB2明确解释其问题是prompt variability而非收益绝对大小；作者第二轮针对性实验后认可，并最终升6。

**选例理由：** 本人明确分阶段3→5→6，且亲口纠正作者误听的问题；适合学习追问阶段如何重新识别混杂因素。

**可迁移机制：** 先复述prompt variability假说，再用同一弱化prompt作配对实验，另配平采样次数。

**必须保留的限制：** 提高呈现只解决第一阶段；不能把后续技术认可全部归因于写作，原初末分仍保留讨论/档案口径。 评分配对档案是采集时点快照，可能晚于部分更新；不作未经核实的真实初始评分向量。

**阅读范围与访问来源：** 关键目标评审的原评→作者逐点回应→追问/再回应完整主链，以及全页评审follow-up、AC meta-review和decision；未声称逐句精读每条无关评论。；公开原始OpenReview记录的MlouisBE研究档案（非研究者生成的摘要）

**机制标签：** `baseline_fairness`、`multi_round`、`evaluation`、`paper_revision`

**复核链接：** [核心数值表态](https://openreview.net/forum?id=KuPixIqPiq&noteId=n3hMAyMgy3) · [其他关键 note 2](https://openreview.net/forum?id=KuPixIqPiq&noteId=a1S78nQYEO) · [其他关键 note 3](https://openreview.net/forum?id=KuPixIqPiq&noteId=vjngdPLj9W) · [其他关键 note 4](https://openreview.net/forum?id=KuPixIqPiq&noteId=83Uqlqoj02) · [其他关键 note 5](https://openreview.net/forum?id=KuPixIqPiq&noteId=nQ8FN6D4Av) · [公开档案](https://huggingface.co/datasets/MlouisBE/iclr-rebuttal-analysis/blob/main/data/raw/ICLR.cc_2024.json)

## C68

### [In-Context Learning Dynamics with Random Binary Sequences](https://openreview.net/forum?id=62K7mALO2q)

**ICLR 2024 · Accept (Poster) · `core_positive`**

**记录到的变化：** 两人3→6，两人5→6

**证据身份：** 原始讨论与评分快照交叉核对；PaperCopilot公开评分快照匹配档案，按reviewer局部ID配对；tracing_score=1。快照可能晚于部分更新，不等同于真实初评历史；正文中的明确改分数字以原始note为准。

**原始阻碍：** 贡献难懂，Bayesian framework解释不足，binary toy与真实任务关系弱，pseudorandomness术语不当。

**作者动作：** 压缩背景并重写贡献；新增toy图连理论与结果；补MMLU混入二进制序列、generator complexity与prompt mismatch实验；删除引发密码学误解的pseudorandomness术语。

**评审反馈：** rqBo标题明确主顾虑解决升6；F7kD明确3→6并强调删掉误导术语使多项批评不再成立；其他两位升6但建议仍要报告开放模型正负结果。

**选例理由：** 主表记录F7kD本人明确3→6并说明删除误导术语的价值；适合术语、理论与toy实验联系的教学。

**可迁移机制：** 重写贡献和框架图，删除会引入错误学术含义的术语，再用现实任务联系和机制实验支持范围。

**必须保留的限制：** 术语修正并非万能；其他评审仍要求开放模型正负结果，不能只靠换词就泛化为充分证据。 评分配对档案是采集时点快照，可能晚于部分更新；不作未经核实的真实初始评分向量。

**阅读范围与访问来源：** 关键目标评审的原评→作者逐点回应→追问/再回应完整主链，以及全页评审follow-up、AC meta-review和decision；未声称逐句精读每条无关评论。；公开原始OpenReview记录的MlouisBE研究档案（非研究者生成的摘要）

**机制标签：** `claim_scope`、`theory_repair`、`evaluation`、`paper_revision`

**复核链接：** [核心数值表态](https://openreview.net/forum?id=62K7mALO2q&noteId=JMCLcyWOxs) · [重点评审 note](https://openreview.net/forum?id=62K7mALO2q&noteId=MZJoxtJytr) · [其他关键 note 2](https://openreview.net/forum?id=62K7mALO2q&noteId=wDdse8aWew) · [其他关键 note 3](https://openreview.net/forum?id=62K7mALO2q&noteId=QM1ziAyFrV) · [其他关键 note 4](https://openreview.net/forum?id=62K7mALO2q&noteId=0kUeKBnYp6) · [其他关键 note 6](https://openreview.net/forum?id=62K7mALO2q&noteId=VcCFwmEAbs) · [公开档案](https://huggingface.co/datasets/MlouisBE/iclr-rebuttal-analysis/blob/main/data/raw/ICLR.cc_2024.json)

## C69

### [Role of Locality and Weight Sharing in Image-Based Tasks: A Sample Complexity Separation between CNNs, LCNs, and FCNs](https://openreview.net/forum?id=AfnsTnYphT)

**ICLR 2024 · Accept (Spotlight) · `core_positive`**

**记录到的变化：** o7GU 3→8；jtyo5→8

**证据身份：** 原始讨论与评分快照交叉核对；PaperCopilot公开评分快照匹配档案，按reviewer局部ID配对；tracing_score=0。快照可能晚于部分更新，不等同于真实初评历史；正文中的明确改分数字以原始note为准。

**原始阻碍：** 似乎只是Wang & Wu已有旋转/置换等变思想的重复；两步GD太简单；下界宽度和norm限制不合理。

**作者动作：** 承认沿用等变工具，逐层说明新任务带来的非旋转不变输入、旧Fano工具不适用、新随机化reduction和Fano变体；解释计算有效GD对比ERM的必要性及限制为何只证明固定width。

**评审反馈：** o7GU明确问题解决并升8，要求正文加入更直接的前作比较；另一评审因新增实验提分；AC认可技术新意并保留理想化模型局限。

**选例理由：** 本人明确将分数提高到8；逐步解释旧证明为何不适用及新引理修复何处，适合理论新颖性核心范例。

**可迁移机制：** 承认沿用等变工具，指出旧Fano步骤失败的位置，展示新reduction/变体及假设对应关系。

**必须保留的限制：** 理想化任务、固定width与计算有效性边界仍在；勿把数学更复杂本身当新增贡献，也不要隐藏对前作工具的依赖。 评分配对档案是采集时点快照，可能晚于部分更新；不作未经核实的真实初始评分向量。

**阅读范围与访问来源：** 关键目标评审的原评→作者逐点回应→追问/再回应完整主链，以及全页评审follow-up、AC meta-review和decision；未声称逐句精读每条无关评论。；公开原始OpenReview记录的MlouisBE研究档案（非研究者生成的摘要）

**机制标签：** `novelty`、`theory_repair`、`related_work`、`claim_scope`

**复核链接：** [核心数值表态](https://openreview.net/forum?id=AfnsTnYphT&noteId=eioQadU1Ny) · [重点评审 note](https://openreview.net/forum?id=AfnsTnYphT&noteId=LU7mrnXNe7) · [其他关键 note 2](https://openreview.net/forum?id=AfnsTnYphT&noteId=6JcY8AqoyQ) · [其他关键 note 3](https://openreview.net/forum?id=AfnsTnYphT&noteId=0vzSU617fu) · [其他关键 note 4](https://openreview.net/forum?id=AfnsTnYphT&noteId=zesOXLpzPT) · [其他关键 note 6](https://openreview.net/forum?id=AfnsTnYphT&noteId=ZCOK6Rdj71) · [公开档案](https://huggingface.co/datasets/MlouisBE/iclr-rebuttal-analysis/blob/main/data/raw/ICLR.cc_2024.json)

## C70

### [MovingParts: Motion-based 3D Part Discovery in Dynamic Radiance Field](https://openreview.net/forum?id=QQ6RgKYiQq)

**ICLR 2024 · Accept (Spotlight) · `extended_positive`**

**记录到的变化：** qQod与NTzN均3→8

**证据身份：** 原始讨论与评分快照交叉核对；PaperCopilot公开评分快照匹配档案，按reviewer局部ID配对；tracing_score=0。快照可能晚于部分更新，不等同于真实初评历史；正文中的明确改分数字以原始note为准。

**原始阻碍：** 仅静态精选图可能cherry-pick、真实单目视频证据少；关键模块无ablation；术语和decoder梯度来源不清。

**作者动作：** 搭匿名补充网页展示所有real/synthetic场景视频与消融；补LPIPS、Watch-It-Move比较、piecewise rigid假设；第二轮澄清D_L/D_E共享参数使梯度路径成立，承认Lagrangian模块约0.2dB rendering代价。

**评审反馈：** qQod称消融特别清楚，随后梯度问题解开；其他评审也明确视频有帮助，最终全员支持；大运动限制仍保留。

**选例理由：** 完整时序视频、所有场景和消融减少cherry-pick疑虑，作为视觉重建扩展；默认核心已覆盖评价和多轮机制。

**可迁移机制：** 提供匿名全场景视频/消融，解释共享参数的梯度路径，并报告新模块的画质代价。

**必须保留的限制：** 多评审3→8应沿原notes与评分档案说明；大运动局限和约0.2dB代价不可省略，漂亮视频不是充分统计证明。 评分配对档案是采集时点快照，可能晚于部分更新；不作未经核实的真实初始评分向量。

**阅读范围与访问来源：** 关键目标评审的原评→作者逐点回应→追问/再回应完整主链，以及全页评审follow-up、AC meta-review和decision；未声称逐句精读每条无关评论。；公开原始OpenReview记录的MlouisBE研究档案（非研究者生成的摘要）

**机制标签：** `evaluation`、`multi_round`、`negative_results`、`claim_scope`

**复核链接：** [重点评审 note](https://openreview.net/forum?id=QQ6RgKYiQq&noteId=9TrLjlAb3E) · [其他关键 note 2](https://openreview.net/forum?id=QQ6RgKYiQq&noteId=xvwEt1EhqE) · [其他关键 note 3](https://openreview.net/forum?id=QQ6RgKYiQq&noteId=ajbIIkBWjC) · [其他关键 note 4](https://openreview.net/forum?id=QQ6RgKYiQq&noteId=pSDfQ58PlZ) · [其他关键 note 5](https://openreview.net/forum?id=QQ6RgKYiQq&noteId=Gl9txgnAxi) · [其他关键 note 6](https://openreview.net/forum?id=QQ6RgKYiQq&noteId=GqZqghh5Mt) · [公开档案](https://huggingface.co/datasets/MlouisBE/iclr-rebuttal-analysis/blob/main/data/raw/ICLR.cc_2024.json)
