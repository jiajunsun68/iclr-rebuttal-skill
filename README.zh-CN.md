# 中文说明 · Chinese documentation

[English (default)](README.md) | **简体中文（当前）**

# ICLR Rebuttal

一个面向 ICLR 与机器学习论文审稿回复的 skill：把审稿意见转化为**可检验的科学担忧**，决定何时补证据、明确反驳、承认修正或收窄主张，再组织逐点回复、论文修改、多轮追评和 AC 总结。

案例库整理了 **70 篇不同论文的 OpenReview 讨论记录**，包括 ICLR 2026 年 49 篇、2025 年 12 篇、2024 年 9 篇；其中选择 **22 篇核心正面范例**供优先参考。全部 70 篇继续保留，包含提分仍拒、条件未闭合、数字冲突和 AC 独立判断等情况。收录数量不等于成功逆转数量，案例也不能证明某种话术会导致提分或接收。完整来源、评分口径与限制见 [案例库](skills/iclr-rebuttal/references/casebook.zh-CN.md) 和 [结构化记录](skills/iclr-rebuttal/references/cases.json)。

## 快速导航

- [安装与开始使用](#安装与开始使用)
- [工作流程](#工作流程)
- [评分与逆转证据](#如何理解评分与逆转证据)
- [核心案例与选择理由](#为什么选择这-22-篇核心范例)
- [大涨分案例的排除与使用限制](#为什么有些大涨分或高规格接收没有进入核心集合)
- [检索案例](#检索案例)
- [Humanizer 学术适配](#humanizer-学术适配与归属)
- [文档导航](#文档导航)
- [仓库验证](#仓库验证)

## 安装与开始使用

使用 [vercel-labs/skills 官方 CLI](https://github.com/vercel-labs/skills) 安装，需要 **Node.js 22.20 或更新版本**。在希望使用该 skill 的项目目录中执行：

```bash
npx skills add jiajunsun68/iclr-rebuttal-skill --skill iclr-rebuttal -a codex
```

如需全局安装，在命令末尾添加 `-g`。Claude Code 用户可使用：

```bash
npx skills add jiajunsun68/iclr-rebuttal-skill --skill iclr-rebuttal -a claude-code
```

其他安装选项以 [skills 官方文档](https://github.com/vercel-labs/skills) 为准。也可以直接阅读 [SKILL.md](skills/iclr-rebuttal/SKILL.zh-CN.md) 和下方参考材料。

使用时提供完整 review、相关论文段落或表格、已有回复、实际完成的实验，以及字数、截止时间和可用资源。一个起始请求可以是：

```text
请使用 iclr-rebuttal 分析下面的审稿意见。

先逐条说明评审的可检验担忧、判断依据和可能的其他理解，
再区分必须补的证据、可以据理反驳的问题、需要承认修正的问题，
并按影响 recommendation 的程度排序。

请给出最小补充计划、相关案例、英文逐点回复和论文修改清单。
未完成的实验保留为待办，不补造结果，不把承诺写成已完成。

[粘贴 review、论文相关内容、已有结果与限制]
```

也可以只请求一项任务，例如分析某条负评、判断是否需要补实验、修改已有回复、撰写追评或压缩 AC 总结；不必每次运行完整流程。

## 工作流程

### 1. 判断评审需要确认什么

这里的“意图”指**由评审原句和论文上下文支持的科学判断条件**，不是猜测评审的身份、私人动机或情绪。例如，“提升很小”可能在质疑随机波动、调参公平性或实际价值；三种理解对应不同证据，不能自动归结为“再跑几个数据集”。

为重要意见记录原句、论文位置、可能的科学担忧、推断置信度、替代解释和足够的答案。依据不足时保留不确定性，提出会改变行动的最小澄清问题。详见 [审稿意图与动作决策](skills/iclr-rebuttal/references/reviewer-intent.zh-CN.md)。

### 2. 选择实质动作

| 动作 | 何时采用 | 回复中需要给出的内容 |
|---|---|---|
| **补数据或证明** | 核心主张缺少有判别力的证据，或公平性、机制、评价、推导存在缺口 | 与质疑直接对应的最小实验或推导、匹配条件、结果及局限；未完成时明确写计划 |
| **明确反驳** | 评审的事实或数学判断可被原文、配置、推导、反例证明不成立，或要求改变了已声明的研究问题 | 直接说明不同意的具体判断，给可核对依据；需要时改善论文表述 |
| **承认、致歉并修正** | 已核实漏引、错误表格、实现偏差、不公平比较、无效论证或过强结论 | 简洁承认错误；重要错误可简短致歉；说明修正、影响与落稿位置，不为正常学术分歧道歉 |
| **收窄主张** | 证据支持的范围小于原来的普遍性、最优性或适用范围主张 | 给出精确的新主张、仍成立的贡献，并同步修改标题、摘要、定理或实验结论 |
| **澄清或追问** | 依据已存在但定义和呈现造成误读，或多种解释会导致不同工作 | 先给答案，再定位依据并写回论文；真正不明确时再问一个具体问题 |

按核心有效性、公平性和贡献优先级安排工作。资源不足时，应明确限制或缩小主张；“必须回答这一科学问题”并不意味着承诺无法完成的实验。表达模板见 [templates.md](skills/iclr-rebuttal/references/templates.zh-CN.md)。

### 3. 用相关案例设计证据

按当前阻碍选择 2–4 个机制相近的案例，读取“作者做了什么—评审如何回应—仍有什么限制”。核心例子帮助设计证据，反例帮助识别边界。不要只找涨幅最大的论文，或从一句礼貌表达推断提分原因。

### 4. 写回复，同时落实论文修改

每个关键问题优先交代：**直接答案、证据、修订位置、剩余边界**。格式随问题调整，不机械套用四个小标题。始终区分计划中、运行中、已运行、已核验、已写回论文；`will add` 不能被编辑成 `have added`。

### 5. 跟进剩余问题并总结给 AC

根据最新追评更新问题状态，避免重复整段首轮回复。AC 总结聚焦决定性的变化，附真实证据与位置，并区分评审确认、部分认可、条件承诺、未回复和仍反对。详见 [证据与多轮跟进](skills/iclr-rebuttal/references/evidence-and-followup.zh-CN.md)。

### 6. 最后精修学术表达

先锁定科学事实，再压缩套话、重复致谢和空泛形容词，保留数字、量词、假设、否定、引用、完成状态和必要的专业术语。表达精修不能替代补证据，也不能把弱结论润色成强结论。详见 [Humanizer 学术适配](skills/iclr-rebuttal/references/humanizer-academic.zh-CN.md)。

## 如何理解评分与“逆转”证据

**评分栏、公开表态和正式决定是不同证据。** 案例中的箭头必须结合记录中的来源与限制阅读：

| 证据类型 | 可以说明什么 | 不能据此断言什么 |
|---|---|---|
| 评审本人说“已提高到 6” | 本人在该条讨论中明确报告已提分 | 今天可见的评分栏必定仍是 6 |
| 评审本人无条件说“将提高到 6” | 本人明确宣布或承诺提分 | 已经完成评分栏更新 |
| “如果补齐 X，我会提高到 6” | 存在条件性承诺，需要追踪条件及后续确认 | 作者说已完成 X 就等于评审确认提分 |
| 作者总结或 AC 记录历史变化 | 该来源记录了变化，需保留归属 | 数字一定出自评审本人原话 |
| AC 说“预计会提高”或“应该在 6 以上” | AC 对讨论结果的预测或综合判断 | 每位评审实际改到该分数 |
| “维持评分”、仅认可解释、未回复 | 相应的态度或缺失反馈 | 隐含提分或默认同意 |
| 论文最终接收 | 该次正式决策为接收 | 所有负评都转正，或接收由某项回复单独造成 |

### ICLR 2026 的特殊口径

ICLR 2026 在安全事件后将 review 正文和评分回滚到 rebuttal 前的状态，保留讨论，由新 AC 结合讨论和作者回应重新评估。因此，**不能把目前可见的 `rating` 当作 rebuttal 后终分**，也不能用当前低分否定讨论中已经出现的历史提分表态。政策依据见 [2025-12-03 官方说明](https://blog.iclr.cc/2025/12/03/iclr-2026-response-to-security-incident/) 和 [2026-03-31 官方回顾](https://blog.iclr.cc/2026/03/31/a-retrospective-on-the-iclr-2026-review-process/)。

其他年份的评分快照也可能晚于首次更新。案例记录分别保留起点来源、本人表态、作者或 AC 转述及正式决定，不把一次采集快照自动当成完整评分历史。不同年份的分档和流程应分别核对。

## 为什么选择这 22 篇核心范例

核心集合包含 **16 篇 ICLR 2026、2 篇 2025、4 篇 2024**。入选需要同时满足：

1. 至少一位评审本人给出明确数字变化或无条件的明确数字提分表态；不只依赖作者转述、AC 预测或未兑现的条件句。
2. 论文最终接收；但不将接收等同于所有问题都解决，也不作因果归因。
3. 可以对应原始担忧、具体作者动作、评审反馈与剩余限制。
4. 机制可复用，并覆盖公平基线、理论、创新性、主张范围、多轮回应和 benchmark 价值；不按涨幅或 Oral、Spotlight 等接收类别排名。

一篇论文可能同时包含强证据与条件性路径。选作核心只使用满足门槛的那一位评审路径，其他路径仍按自身证据等级记录。完整规则见 [case-selection.md](skills/iclr-rebuttal/references/case-selection.zh-CN.md)。

### 核心正面范例

下表的分数是带来源限定的历史轨迹或本人表态；具体区分“已提高”与“宣布将提高”，请查看对应案例记录和讨论 note。

| 案例 | 年份 | 建议学习的机制与入选价值 |
|---|---:|---|
| [C64 · PF-LRM](https://openreview.net/forum?id=noe76eRcPC) | 2024 | 同数据重训争议 baseline 后本人明确升至 8，展示公平对照。 |
| [C09 · Explainable LLM Unlearning through Reasoning](https://openreview.net/forum?id=wec4qy2XIF) | 2026 | 审计并改正弱 baseline；承认对方优势，2→6 后仍保留最优性疑问。 |
| [C17 · Conductor](https://openreview.net/forum?id=U23A2BUKYt) | 2026 | 用强模型直接替代新模块，同时报告成本，检验模块必要性。 |
| [C10 · NSPO](https://openreview.net/forum?id=GFyVxtyMvq) | 2026 | 公平比较后 2→4，说明近似与分布边界后 4→6。 |
| [C12 · Best-of-N through the Smoothing Lens](https://openreview.net/forum?id=tCv1D3M7Lb) | 2026 | 撤去未能支撑原解释的定理表述，重建论据，2→6；不据此断言原不等式为假。 |
| [C23 · Taming Score-Based Denoisers](https://openreview.net/forum?id=BiXwSIIMIq) | 2026 | 将理想平稳假设下的分析修到实际有限步算法，4→6。 |
| [C18 · Softmax Transformers are Turing-Complete](https://openreview.net/forum?id=FdkPOHlChS) | 2026 | 讲清主定理、假设、前作关系与理想化训练条件，多位评审提分。 |
| [C69 · Role of Locality and Weight Sharing in Image-Based Tasks](https://openreview.net/forum?id=AfnsTnYphT) | 2024 | 指出旧证明在哪一步失效、新工具修复哪一步，本人宣布升至 8。 |
| [C28 · LCA](https://openreview.net/forum?id=3uINmRldVW) | 2026 | 承认辅助组件沿用前作，重新界定主贡献，4→6。 |
| [C52 · GenSE](https://openreview.net/forum?id=1p6xFLBU4J) | 2025 | 漏引后做机制与任务的实质比较，本人明确调至 6。 |
| [C13 · GPG](https://openreview.net/forum?id=inccdtfx8x) | 2026 | 将范围解释写回论文后，获得明确已升至 6 的确认。 |
| [C68 · In-Context Learning Dynamics with Random Binary Sequences](https://openreview.net/forum?id=62K7mALO2q) | 2024 | 删除误导术语，连接简化设定与真实任务；F7kD 明确 3→6。 |
| [C25 · FACT](https://openreview.net/forum?id=j3gNYqrHtl) | 2026 | 将平均指标、变量顺序和调参疑虑变成直接实验，4→6。 |
| [C02 · FASA](https://openreview.net/forum?id=FnSgecCEwg) | 2026 | 核心校准问题解决后 4→6，保留理论疑问而不夸大全部解决。 |
| [C67 · Teaching Large Language Models to Self-Debug](https://openreview.net/forum?id=KuPixIqPiq) | 2024 | 复述真正的 prompt 混杂，再做配对实验，3→5→6。 |
| [C15 · SCUBA](https://openreview.net/forum?id=bkjKnO9s7T) | 2026 | 用轨迹采集路径、任务模板与评测代码解释 benchmark 的价值。 |
| [C19 · InnovatorBench](https://openreview.net/forum?id=w8rZ2Jd6Jo) | 2026 | 收窄标题并如实补充零分结果；初称不改分者后来明确 2→6。 |
| [C11 · Keep the Best, Forget the Rest](https://openreview.net/forum?id=LrHfYPFTtg) | 2026 | 发布实际强 baseline、多 judge 与敏感性结果，兑现补实验承诺。 |
| [C32 · Procedural Mistake Detection](https://openreview.net/forum?id=HsB5EuQOoS) | 2026 | 澄清测试阈值协议、补充强模型对照，2→6。 |
| [C33 · Metric Tensors on Neuromanifolds](https://openreview.net/forum?id=Ssevs8KCsU) | 2026 | 用可计算真值标定估计器，4→6；不让 AC 记录中的旧分覆盖本人表态。 |
| [C26 · Atomic HINs](https://openreview.net/forum?id=AG7fjg5azU) | 2026 | 报告真实成本、摊销和跨后端复用，4→6。 |
| [C53 · CO-MOT](https://openreview.net/forum?id=0ov0dMQ3mN) | 2025 | 重投稿逐项列出可定位改动，本人明确升至 6。 |

这些例子仍保留未解决事项，例如 FASA 的理论基础、Explainable Unlearning 的新指标可靠性、SCUBA 的维护与评测边界、InnovatorBench 的任务数。入选表示可以学习指定机制，不表示所有回复语气和全部论断都值得复制。

### 全部 70 篇如何保留

| 角色 | 数量 | 用途 |
|---|---:|---|
| `core_positive` | 22 | 优先参考的正面范例，满足上述证据门槛 |
| `extended_positive` | 16 | 补充专门场景或相近机制，仍保留各自来源限制 |
| `qualified_positive` | 19 | 必须同时说明条件、意愿、支持者加分、因果混杂或行为限制的辅例 |
| `outcome_counterexample` | 6 | 提分仍拒或关键条件未闭合，用于理解结果边界 |
| `evidence_exclusion` | 2 | 异常或来源冲突，排除为正面数字逆转确证，记录仍保留 |
| `context_only` | 5 | AC 独立判断、认可但未提分等上下文，不补写数字轨迹 |

### 为什么有些大涨分或高规格接收没有进入核心集合

下表区分**未入核心、不可作为数字逆转确证、不可照搬话术**三种情况。排除仅针对相应用途，记录本身继续保留；不表示论文低质量，也不表示回应毫无价值。

| 案例 | 数字或结果（须结合限制理解） | 保留什么、为何谨慎使用 |
|---|---|---|
| [C50 · Dynamic Neural Fortresses](https://openreview.net/forum?id=029hDSVoXK) | 异常 1→8，最终接收 | AC 明确剔除这次异常涨分，缺乏对应讨论链；保留审计反例，不把异常归功于 rebuttal。 |
| [C59 · NetMoE](https://openreview.net/forum?id=1qP3lsatCR) | 档案 3→6、6→8，Spotlight | 初分档案与 AC 回顾冲突未消解；保留硬件实测机制，不采用最戏剧化的数字叙事。 |
| [C43 · MonoSoup](https://openreview.net/forum?id=ICANwnoGgN) | AC 记录 4→6 及两次 6→8 | 最终 Reject，AC 仍认为理论支撑与收益不足；保留“提分不保证接收”反例。 |
| [C56 · Shallow Diffuse](https://openreview.net/forum?id=1IwoEFyErz) | 配对档案显示四名评审均 5→6 | 最终 Reject，鲁棒性、多 key 结果与全面优越说法不符；保留主张审计反例及快照来源限制。 |
| [C57 · GRIC](https://openreview.net/forum?id=0owAtTCOlU) | 配对档案显示多位 3/5→6 | 最终 Reject，任务定义和实验体系仍需重构；不能用加分掩盖核心设定问题。 |
| [C46 · ASMG](https://openreview.net/forum?id=xsqiDQjSvV) | 两位 4→6，另一位愿升至 6 | 最终 Reject，规模、复杂度与收益仍不充分；支持者人数不是充分条件。 |
| [C44 · FuseGPT](https://openreview.net/forum?id=tNnXu5bKoo) | 2→4 | 仍处拒稿档且最终 Reject；上涨与跨过接受门槛不同。 |
| [C45 · Censoring with Plausible Deniability](https://openreview.net/forum?id=vSXIEbTVhE) | 2→4，再有 4→6 条件句 | 核心隐私问题未闭合；作者完成修改或自行概括不等于评审确认。 |
| [C37 · DeMo](https://openreview.net/forum?id=U9oewpa7cn) | 四个 4，最终接收 | NyAn 仅有条件式 4→6；AC 预期全员 6 不是四次实际改分。借鉴公平基线与披露，不编造共识。 |
| [C47 · InfoNCE Induces Gaussian Distribution](https://openreview.net/forum?id=BlSH7gNQSq) | 8/4/2/2，最终 Oral | AC 预计最终高于 6；保留 AC 独立判断，不能补写逐评审终分。 |
| [C48 · GAGA](https://openreview.net/forum?id=Q9gz8lVyAi) | 一位承诺 2→6，最终接收 | 个人明确承诺可引用；AC 对另一评审会转正的推断被其反对，不能称“全体逆转”。 |
| [C49 · PLAGUE](https://openreview.net/forum?id=05hNleYOcG) | 2/2/4/2，最终 Poster | 接收来自 AC 综合判断，仅有可能提分的预期；不能称所有低分变正面。 |
| [C27 · Quantum Attention Approximation](https://openreview.net/forum?id=0zIcPe4CtY) | 本人 4→8 | 数字可信，但评审警告原稿不成熟、修订过大；用作证明修复辅例，不鼓励把核心缺口留到 rebuttal。 |
| [C65 · Learning Delays in Spiking Neural Networks](https://openreview.net/forum?id=4r2ybzJnmN) | 3→8、3→6 | 技术对照有用，但 aggressive style 被明确批评；不模仿整段语气，仍保留实验机制。 |
| [C38 · Accelerated Parallel Tempering](https://openreview.net/forum?id=CODnlyYUli) | 本人 2→4→6 | 最后变化还受到同行讨论影响；不能将全部效果归因于作者话术。 |
| [C01 · BiasFreeBench](https://openreview.net/forum?id=Ncf2LFDT4e) | 4→6 | 本人只说提高，目标 6 来自作者；保留贡献定位辅例，不冒充本人明确数字。 |
| [C04 · Token-Efficient Item Representation via Images for LLM Recommender Systems](https://openreview.net/forum?id=vizM7B7vuW) | 6→8、8→10 | 本人确认提高，目标由作者补充，且原本正面；不是负评转正的确证。 |
| [C06 · Steering Autoregressive Music Generation](https://openreview.net/forum?id=NaHzPMaCY9) | 8→10 | 已有支持者的提分意愿，原 2 分者未转正；保留巩固支持者与独立评测经验。 |
| [C62 · Large Language Models Cannot Self-Correct Reasoning Yet](https://openreview.net/forum?id=IkmD3fKBPQ) | 3→6 及 6→8 | 3→6 附标题条件，另一位 6→8 是明确支持增强；快照也与本人初分不一致，必须分路径陈述。 |

## 检索案例

仓库提供只依赖 Python 标准库的 [search_cases.py](skills/iclr-rebuttal/scripts/search_cases.py)。以下命令从仓库根目录运行：

```bash
# 查找公平基线相关的 2026 核心案例
python3 skills/iclr-rebuttal/scripts/search_cases.py --year 2026 --role core_positive --mechanism baseline_fairness --limit 4

# 查找某篇论文，并保留结构化来源和限制
python3 skills/iclr-rebuttal/scripts/search_cases.py --query SCUBA --format json

# 阅读提分仍拒或关键条件未闭合的反例
python3 skills/iclr-rebuttal/scripts/search_cases.py --role outcome_counterexample --limit 6
```

可按年份、角色、关键词与机制组合筛选。关键词搜索覆盖标题、过程分析和选择理由，因此查询 SCUBA 也可能返回提到它的对照案例；需要精确查找时使用案例 ID 或 forum ID，例如 `--query bkjKnO9s7T`。机制标签包括 `baseline_fairness`、`theory_repair`、`novelty`、`claim_scope`、`multi_round`、`benchmark_value`、`evaluation`、`efficiency`、`paper_revision`、`related_work`、`negative_results`、`ac_summary`。输出同时保留机制、注意事项和原始讨论链接，便于回看上下文。

## Humanizer 学术适配与归属

表达精修模块部分改编自 [blader/humanizer](https://github.com/blader/humanizer)，固定到提交 [`0ef9fe5bc3572734fd3ae6c448fe00a30cd5dcf0`](https://github.com/blader/humanizer/commit/0ef9fe5bc3572734fd3ae6c448fe00a30cd5dcf0)。该版本的 [SKILL.md](https://github.com/blader/humanizer/blob/0ef9fe5bc3572734fd3ae6c448fe00a30cd5dcf0/SKILL.md) 自报 **v3.1.0**，包含 **26 项写作模式**；本仓库按学术 rebuttal 语境逐项适配，不将通用文体建议机械套用到数学、实验和引用文本。

[学术适配文档](skills/iclr-rebuttal/references/humanizer-academic.zh-CN.md) 包含 **12 组原创改写例句**，用于展示事实保真、语气与组织方式；这些示例不是上游案例，也不是真实 ICLR 实验结果。模块以读者可读性为目标，不承诺通过 AI 检测或提高接收率，不改写事实、完成状态或应保留的披露。

上游版权为 **Copyright (c) 2025 Siqi Chen**，采用 MIT 许可证。完整许可与归属见 [上游 MIT 许可](skills/iclr-rebuttal/references/humanizer-LICENSE.txt) 和 [THIRD_PARTY_NOTICES.md](THIRD_PARTY_NOTICES.md)；本适配不代表上游作者的认可。仓库许可见 [LICENSE](LICENSE)。

## 文档导航

| 文件 | 内容 |
|---|---|
| [SKILL.md](skills/iclr-rebuttal/SKILL.zh-CN.md) | 完整使用流程与交付约束 |
| [reviewer-intent.md](skills/iclr-rebuttal/references/reviewer-intent.zh-CN.md) | 科学担忧推断、置信度、动作决策与表达 |
| [evidence-and-followup.md](skills/iclr-rebuttal/references/evidence-and-followup.zh-CN.md) | 证据与状态记录、2026 口径、多轮跟进及 AC 总结 |
| [templates.md](skills/iclr-rebuttal/references/templates.zh-CN.md) | 澄清、反驳、承认修正、补证据、收窄范围的短模板 |
| [humanizer-academic.md](skills/iclr-rebuttal/references/humanizer-academic.zh-CN.md) | 26 项学术适配、事实保真检查与 12 组原创例句 |
| [case-selection.md](skills/iclr-rebuttal/references/case-selection.zh-CN.md) | 选例门槛、角色定义与谨慎使用理由 |
| [casebook.md](skills/iclr-rebuttal/references/casebook.zh-CN.md) | 70 篇案例的证据、动作、反馈与边界 |
| [cases.json](skills/iclr-rebuttal/references/cases.json) | 可检索的结构化案例记录与来源 |
| [search_cases.py](skills/iclr-rebuttal/scripts/search_cases.py) | 本地关键词、年份、角色及机制检索 |
| [THIRD_PARTY_NOTICES.md](THIRD_PARTY_NOTICES.md) | 第三方来源、固定版本和许可归属 |
| [evals/RESULTS.md](evals/RESULTS.zh-CN.md) | 已记录的验证范围与结果 |

## 仓库验证

从仓库根目录运行：

```bash
python3 scripts/validate_repository.py
python3 -m unittest discover -s tests -v
```

这些检查面向案例字段与计数一致性、来源链接归属、本地文档链接，以及检索筛选和命令行行为。它们**不证明论文的科学结论、提分的因果机制或未来接收效果**。已执行的检查及其结果以 [验证记录](evals/RESULTS.zh-CN.md) 为准。
