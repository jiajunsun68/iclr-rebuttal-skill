# 案例选择与证据边界

## 目录

- [研究范围](#研究范围)
- [六种教学角色](#六种教学角色)
- [核心案例门槛](#核心案例门槛)
- [机制索引](#机制索引)
- [大幅提分为什么不一定入选](#大幅提分为什么不一定入选)
- [使用与更新](#使用与更新)

## 研究范围

截至 2026-11-09，集合包含 **70 个独立 OpenReview 论文讨论页**：2026 年 49 篇、2025 年 12 篇、2024 年 9 篇。一个论文 forum 只算一例，多条评论不重复计数。64 篇最终接收、6 篇拒稿；这是有目的选择的教学样本，不能据此计算 rebuttal 成功率。

阅读范围是目标评审的关键完整主链、相关作者回复、AC 意见和最终决定，不声称逐句阅读所有无关支线。访问途径包括原站公开索引、作者保存的 OpenReview 网页 PDF 和保留匿名 note 字段的公开记录档案；部分原站页面存在访问验证。每条记录保留 `source_type`、`reading_scope`、原站/具体 note 和可用存档地址。

ICLR 2026 评分与 review 正文回滚，使当前评分栏不能代表讨论终分。详见 [证据与状态规则](evidence-and-followup.zh-CN.md#iclr-2026-特殊口径) 及其中官方来源。历史自述、无条件提分意愿、条件承诺、作者转述、AC 历史记录、AC 预测必须分开；不跨年合并平均涨幅。

## 六种教学角色

角色表示适合怎样使用一个案例，不是论文质量评级。全部 70 条仍保留在 [案例手册](casebook.zh-CN.md) 和 [结构化数据](cases.json)。

| 角色 | 数量 | 用途 |
|---|---:|---|
| `core_positive` | 22 | 默认正面范例。最终接收，有本人明确数值提分陈述、无未兑现的纯条件门槛；作者动作与评审反馈可定位，教学机制具体且覆盖互补。2026仅保证历史公开陈述，非当前评分栏。 |
| `extended_positive` | 16 | 扩展正面阅读。方法机制有价值但与核心重复、场景更专门，或数字仍需按既有来源逐项归属；不以未入核心否定质量。 |
| `qualified_positive` | 19 | 带限定的正面/改进辅例。允许借鉴指定机制，必须同时呈现条件、意愿、支持者加分、来源差异、因果混杂或行为警示，不可整段当作成功话术模板。 |
| `outcome_counterexample` | 6 | 结果或闭环反例。改善/提分未带来该次接收，或条件未被确认；用于阻止“上涨=接收”等错误推断。 |
| `evidence_exclusion` | 2 | 排除为正面数字逆转确证：异常被AC剔除或初分来源冲突未消解。记录与可用机制仍保留，不判论文低质量。 |
| `context_only` | 5 | 上下文对照：AC独立判断、认可但不提分或全初始正面。学习决策过程，不能补写评审数字轨迹。 |

## 核心案例门槛

1. 本人给出明确数字目标或明确数字变化，且不是只靠作者转述、AC预测或未兑现条件。
2. 最终接收，但不把接收推断为某个动作的因果效果。
3. 原始讨论能连接拒稿依据、具体作者动作、评审回应与剩余限制。
4. 同等证据下优先可复用机制和题材覆盖，避免按最大涨分或最高接收等级选样。
5. 引用含mixed证据的论文时只使用满足条件的那一位评审路径；其他路径单列。

22 篇核心中，2026 年 16 篇、2025 年 2 篇、2024 年 4 篇。`core_numeric_anchor` 定位符合门槛的具体评审，不能以该字段替代同一论文其他评审的状态。已宣布的目标分仍要区分正在上调、已上调和无条件未来意愿，不能一概声称系统已改分。

核心案例的详细入选理由见仓库 [README](https://github.com/jiajunsun68/iclr-rebuttal-skill#核心正面范例) 与每条案例的 `selection.reason`。字段 `reusable_mechanism` 说明可借鉴的动作；`caution` 必须同时读取。接收和提分仅是观察到的结果，不能证明某个措辞或某个实验独立导致接收。

## 机制索引

按当前审稿问题选择机制，再筛选合适角色。下面只列核心集合覆盖，其他角色也可包含相同机制。

| 标签 | 核心案例 |
|---|---|
| `baseline_fairness` | [C09](casebook.zh-CN.md#c09)、[C10](casebook.zh-CN.md#c10)、[C11](casebook.zh-CN.md#c11)、[C17](casebook.zh-CN.md#c17)、[C25](casebook.zh-CN.md#c25)、[C32](casebook.zh-CN.md#c32)、[C64](casebook.zh-CN.md#c64)、[C67](casebook.zh-CN.md#c67) |
| `theory_repair` | [C10](casebook.zh-CN.md#c10)、[C12](casebook.zh-CN.md#c12)、[C18](casebook.zh-CN.md#c18)、[C23](casebook.zh-CN.md#c23)、[C33](casebook.zh-CN.md#c33)、[C68](casebook.zh-CN.md#c68)、[C69](casebook.zh-CN.md#c69) |
| `novelty` | [C17](casebook.zh-CN.md#c17)、[C18](casebook.zh-CN.md#c18)、[C28](casebook.zh-CN.md#c28)、[C52](casebook.zh-CN.md#c52)、[C69](casebook.zh-CN.md#c69) |
| `claim_scope` | [C02](casebook.zh-CN.md#c02)、[C10](casebook.zh-CN.md#c10)、[C12](casebook.zh-CN.md#c12)、[C13](casebook.zh-CN.md#c13)、[C15](casebook.zh-CN.md#c15)、[C19](casebook.zh-CN.md#c19)、[C23](casebook.zh-CN.md#c23)、[C25](casebook.zh-CN.md#c25)、[C28](casebook.zh-CN.md#c28)、[C64](casebook.zh-CN.md#c64)、[C68](casebook.zh-CN.md#c68)、[C69](casebook.zh-CN.md#c69) |
| `multi_round` | [C02](casebook.zh-CN.md#c02)、[C09](casebook.zh-CN.md#c09)、[C10](casebook.zh-CN.md#c10)、[C12](casebook.zh-CN.md#c12)、[C13](casebook.zh-CN.md#c13)、[C15](casebook.zh-CN.md#c15)、[C19](casebook.zh-CN.md#c19)、[C28](casebook.zh-CN.md#c28)、[C52](casebook.zh-CN.md#c52)、[C64](casebook.zh-CN.md#c64)、[C67](casebook.zh-CN.md#c67) |
| `benchmark_value` | [C15](casebook.zh-CN.md#c15)、[C19](casebook.zh-CN.md#c19) |
| `evaluation` | [C02](casebook.zh-CN.md#c02)、[C09](casebook.zh-CN.md#c09)、[C11](casebook.zh-CN.md#c11)、[C13](casebook.zh-CN.md#c13)、[C15](casebook.zh-CN.md#c15)、[C17](casebook.zh-CN.md#c17)、[C25](casebook.zh-CN.md#c25)、[C26](casebook.zh-CN.md#c26)、[C32](casebook.zh-CN.md#c32)、[C33](casebook.zh-CN.md#c33)、[C53](casebook.zh-CN.md#c53)、[C64](casebook.zh-CN.md#c64)、[C67](casebook.zh-CN.md#c67)、[C68](casebook.zh-CN.md#c68) |
| `efficiency` | [C11](casebook.zh-CN.md#c11)、[C17](casebook.zh-CN.md#c17)、[C26](casebook.zh-CN.md#c26)、[C32](casebook.zh-CN.md#c32)、[C33](casebook.zh-CN.md#c33) |
| `paper_revision` | [C09](casebook.zh-CN.md#c09)、[C11](casebook.zh-CN.md#c11)、[C12](casebook.zh-CN.md#c12)、[C13](casebook.zh-CN.md#c13)、[C18](casebook.zh-CN.md#c18)、[C23](casebook.zh-CN.md#c23)、[C26](casebook.zh-CN.md#c26)、[C52](casebook.zh-CN.md#c52)、[C53](casebook.zh-CN.md#c53)、[C67](casebook.zh-CN.md#c67)、[C68](casebook.zh-CN.md#c68) |
| `related_work` | [C18](casebook.zh-CN.md#c18)、[C23](casebook.zh-CN.md#c23)、[C28](casebook.zh-CN.md#c28)、[C52](casebook.zh-CN.md#c52)、[C53](casebook.zh-CN.md#c53)、[C69](casebook.zh-CN.md#c69) |
| `negative_results` | [C09](casebook.zh-CN.md#c09)、[C10](casebook.zh-CN.md#c10)、[C19](casebook.zh-CN.md#c19)、[C53](casebook.zh-CN.md#c53) |
| `ac_summary` | [C02](casebook.zh-CN.md#c02)、[C33](casebook.zh-CN.md#c33) |

## 大幅提分为什么不一定入选

- **数值异常缺少可解释的讨论链**：Dynamic Neural Fortresses 的 1→8 被 AC 明确剔除。保留证据审计价值，不能当成作者回复成功的证明。
- **来源冲突未解决**：NetMoE 的初分档案与 AC 回顾不一致。可以学习硬件实测，不能选择涨幅最大的版本。
- **提分仍未接收**：MonoSoup、Shallow Diffuse、GRIC、ASMG、FuseGPT 等说明评分上涨与最终决定不同；需要继续检查核心有效性和剩余贡献。
- **条件或预测没有闭环**：DeMo、InfoNCE、PLAGUE 等适合解释 AC 决策和条件状态，不能补造逐评审终分。
- **技术动作可学，整段话术不可照搬**：Quantum Attention 的修订幅度受到评审批评；SNN Learning Delays 的进攻性语气受到批评。保留指定技术机制，不能把被批评的行为当作通用策略。
- **还有其他影响因素**：Parallel Tempering 的变化包含同行讨论。可以分析过程，不将全部效果归因于作者表达。
- **本来就是支持者或数字来自转述**：I-LLMRec、Music RFM 等可以用于巩固支持与评估设计，不能包装为明确负转正。

逐项原始讨论与完整理由见 [案例手册](casebook.zh-CN.md) 的对应 ID，以及仓库 [README](https://github.com/jiajunsun68/iclr-rebuttal-skill) 的排除与谨慎使用表。这里的“排除”指排除相应的正面逆转确证或默认措辞范本，记录本身没有删除。

## 使用与更新

每次选 2–4 个与当前阻碍最接近的案例，至少读作者动作、评审回应、剩余限制和证据锚点。脚本只检索本地记录，不把网页内容发送到第三方，也不复现原论文实验。

更新一条案例时保留稳定 `case_id` 和 `forum_id`；核对发表年份、原文角色、时间和具体 note。新发现推翻旧记录时保留来源冲突说明，不静默替换为更好看的数字。角色变化须更新数量与 README，使用仓库验证脚本检查一致性。

匿名评审编号仅用于追溯公开讨论，不反向推断真实身份。研究的是可检验的学术问题和回应动作。
