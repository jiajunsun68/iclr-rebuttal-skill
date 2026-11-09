# 从审稿意见到证据义务和回应动作

适用于逐条分析评审意见、拟定补证据计划、撰写回应及整理 AC 摘要。规则来自已读取的公开讨论案例，但属于有目的样本中的实践归纳，不是提分概率模型，也不保证接收。


## 目录

- [一、工作目标与不可越过的边界](#一工作目标与不可越过的边界)
- [二、意图推断的方法：两种置信度，而非读心](#二意图推断的方法两种置信度而非读心)
- [三、回应动作的判定规则](#三回应动作的判定规则)
- [四、17类审稿表述（概括）：意图、充分条件和动作](#四17类审稿表述概括意图充分条件和动作)
- [五、多轮跟进规则](#五多轮跟进规则)
- [六、AC 摘要规则](#六ac-摘要规则)
- [七、工作表字段与质量门槛](#七工作表字段与质量门槛)
- [八、速查规则](#八速查规则)

## 一、工作目标与不可越过的边界

目标是让论文的主张、证据和表达相互一致，使评审能核查其顾虑是否得到回应。评分变化可以记录，但不应成为虚构结果、隐藏限制或夸大共识的理由。

“推断审稿意图”仅指从评审文字推断待核验的学术问题。例如，把“没有强基线”解释为“收益是否仍成立于合理的竞争方法”，不能解释成“这位评审喜欢某个实验室”“他只想刁难作者”或“他是某篇论文的作者”。不得猜测身份、国籍、资历、人格、情绪、学术派系或私人动机。不得根据这些猜测选择迎合策略。

严格分开四层信息：

1. **原始观察**：评审实际写了什么，位于哪个 note、哪个问题、哪一轮。
2. **可检验问题**：这段文字直接要求验证什么。
3. **解释性推断**：它可能担心哪种替代解释，依据是什么，还有哪些可能解释。
4. **回应决策**：需要澄清、补实验、补证明、纠错、收窄、合理反驳还是暂留未完成。

不要把第3层写成评审已经表达的事实。对作者也同样严格：作者说“实验已完成”不能自动等同于结果已核查；作者说“评审已同意”不能自动替代评审本人原文。

以下英文话术是新写的状态敏感模板，并非案例作者原话。方括号必须替换成已核实内容；标注“未完成”的版本只在实际未完成时使用。没有结果时不能把计划改写为过去时，不能填入看起来合理的数字、误差条、定理或引用。

## 二、意图推断的方法：两种置信度，而非读心

### 2.1 对每条意见形成可复核记录

先写：`原句 → 直接问题 → 最可能的待验证假设 → 替代解释 → 所需证据`。

同时记录两种不同置信度：

- **问题解释置信度**：我们是否正确理解这句话要求验证什么。
- **决策重要性置信度**：我们是否有证据认为这个问题会影响 recommendation。

例如，“请报告运行时间”让我们对“需要成本证据”的解释具有高置信度，但不能单凭这句话推断“给出运行时间就会接受”。

| 等级 | 问题解释的依据 | 决策重要性的依据 | 行动 |
|---|---|---|---|
| 高 | 评审直接说出替代解释、所需比较或具体数学错误 | 明确标为主要问题、表示若解决则改变评价，或追评说明这是剩余阻碍 | 直接回答明确问题，并保留原句作为依据 |
| 中 | 含义由相邻语句和具体论文位置支持，但有多个合理解释 | 多轮重复、与低 soundness / contribution 判断吻合，但没有明确改分条件 | 优先做兼容多种解释的诊断；必要时用一句话确认理解 |
| 低 | 只有“有限”“不够强”“不令人信服”等宽泛形容 | 无法确定其是否决定推荐 | 不把猜测当任务清单；提出具体可选解释，请评审澄清关键点 |

不编造精确概率，如“有87%概率评审在担心过拟合”。使用高/中/低并写出文本依据即可。

### 2.2 最少保留一个替代解释

“新颖性不足”可能是漏引近邻工作，也可能是作者没有说明新增机制，或是新增机制确实不够重要。“缺少实验”可能是可信度问题，也可能只是扩展建议。没有进一步证据前，不应把它们都处理成“再补一张结果表”。

在含糊情形下，可使用：

> We interpret the main concern as whether [testable issue], rather than only [alternative reading]. Is that the key point affecting your assessment?

这里的两种解释必须都来自评审文字和论文内容，不能虚构一个更容易回应的版本。如果已经能够回答双方共有的核心问题，应先给有用答案，再请求必要澄清。

## 三、回应动作的判定规则

### 3.1 何时必须补数据、实验或证明

同时满足以下条件时，不能只靠措辞澄清：

1. 质疑针对当前论文正在主张的结论，或该结论赖以成立的必要前提。
2. 现有材料没有直接回答它，或已有证据存在明确混杂、泄漏、预算不匹配、逻辑缺口。
3. 正确回答需要新增可观察结果或新增推导，而非仅定位已经存在的事实。

典型必补项：决定核心增益的公平基线；宣称组件必要但缺相应消融；实际算法不满足理论假设；声称跨域通用却只有单域证据；用测试集选阈值后仍声称无偏测试性能；效率主张缺必要资源核算。

“必须补”表示**要保留该主张就负有证据义务**，不表示无条件服从每一个实验要求。如果无法完成，可以删除或收窄相应主张；若它就是论文核心、又没有可成立的替代贡献，应明确当前论证仍未成立。不能把核心有效性问题仅移入未来工作来规避。

数学问题的证据应是缺失条件、证明、反例检查及相应定理修改。更多实验不能证明错误定理；一条更弱但正确的定理也不能继续支持原来的强结论。

### 3.2 何时应明确反驳事实错误

先核对**评审所读版本**、提交附件、表格、代码入口和时间，防止用后来添加的内容声称“原稿已经有”。满足以下条件才可直接纠正：

- 事实具有客观可核验依据，例如代码确在提交的补充材料中，实验确在某张表里，算法并没有使用测试标签。
- 引用位置足够精确，能让评审独立复查。
- 纠正没有掩盖另一个仍然有效的问题。例如，“我们提供代码”不能回答“代码不能运行”。

回应结构为：**明确事实 → 证据位置 → 对疑虑的影响 → 如有必要改善可发现性**。可以承认表达不清，不必为一个没有发生的实验错误道歉。避免“你没有认真读”“显然”“这完全错误”等攻击性归因。

已核验事实时可用：

> To clarify, [specific factual statement], as shown in [submitted-version location]. This addresses [precise concern]. [Any remaining limitation] is a separate issue.

### 3.3 何时应拒绝或调整超出主张的要求

必须先解释技术边界，不能只写“out of scope”。合格的边界说明至少包含：

1. 本文研究对象与实际结论是什么。
2. 所提任务需要改变哪些假设、数据、目标函数或算法。
3. 为什么该扩展不决定当前结论的正确性。
4. 标题、摘要、实验和贡献表述是否已经遵守这个较窄范围。

若评审要求的场景恰好是作者用来宣传价值的核心场景，就不能一面保留宽泛宣传，一面把验证要求排除。此时要补证据或同步收窄。若扩展确实不适用，可提出成本更低且能验证同一疑虑的替代测试。

### 3.4 何时必须承认错误并实际修订

发现客观错误、遗漏必要假设、无效证明、不公平比较、错误引用或无法支持的机制解释时，直接承认具体问题。道歉宜一次、简洁，并与修复绑定；不需长篇自责。

处理顺序：**错误是什么 → 修正是什么 → 哪些结果受影响 → 核心结论保留到什么程度 → 哪些位置已改、哪些未改**。如果重新计算后优势消失，应如实报告；不能只展示仍有优势的子集。

确认存在错误后可用：

> We agree that [specific statement] is incorrect. The correction is [verified correction], which changes [affected claim]. We apologize for the error. [State the actual revision status and location.]

“已修订”只在修改实际进入指定版本后使用。理论方向正确但写法含糊时，可承认表述问题，不能把尚未判定的理论问题虚假承认为已证实错误。

### 3.5 何时收窄范围

出现以下任一情况应检查标题、摘要、贡献和结论：普遍性仅由少数设置支持；近似实现被描述成精确保证；组合中的既有组件被描述成独立创新；某指标胜出被概括为整体更好；仅支持固定预算却声称全预算占优。

收窄不是只加一段 limitations。需要修改对应的主张，并明确剩下的、仍有证据支持的知识增量。可以保留真实价值，例如通信显著减少但训练损失略差，或少数据条件下有效而不声称全数据通用。

### 3.6 实验来不及：保留未完成状态

采用至少六种不同状态：`未计划`、`已计划未开始`、`进行中`、`已完成待核查`、`已核查`、`已纳入指定版本`。它们不能相互代替。另设“评审是否明确认可”，不要将它混入执行状态。

- 给出已经知道的结论和证据缺口，不编造一个“预计会正面”的结果。
- 若作者已确认资源与计划，可以说明打算做什么；未确认的计划不能写成无条件承诺。
- 只有实际启动后才写 running；只有完成并核查后才写结果；只有提交了相应修订版本后才写 incorporated。
- 不完整运行、单个 seed 或尚未收敛的结果必须标为 preliminary，不能用确定语气覆盖其局限。
- 若截止前不能满足必要证据义务，明确收窄/撤回相应主张，或保留“核心问题未解决”。

未完成时可用：

> We do not yet have a completed, verified result for [test]. We therefore cannot claim [unsupported conclusion]. The current evidence supports only [verified scope]; [state any feasible next step without presenting it as completed].

## 四、17类审稿表述（概括）：意图、充分条件和动作

以下代表性表述是对已核验初评意见的概括，不是逐字引文；链接指向对应评审或作者 note，便于查看准确原文。案例展示的是实际发生过的讨论，作者报告的实验并不等于本技能独立复现了实验。“足够答案”指足以正面回答该项问题，不是保证评审提分。

### 01. 缺少真正相关的竞争基线

**代表性表述（概括）**：只与常规优化器比较，还不能说明相对于其他减少分布式通信的方法是否有优势。

**来源**：[DeMo，NyAn 初评](https://openreview.net/forum?id=U9oewpa7cn&noteId=kTKI6c3Z20)。后续出现[条件性提分承诺](https://openreview.net/forum?id=U9oewpa7cn&noteId=MbpXnuAD0V)，不代表全部疑虑消失。

**优先验证的假设**：相对于真正解决同一问题的现有方法，本文优势是否仍然成立。问题解释置信度高；重要性高，因为原评明确要求强化比较才改变意见。**替代解释**：评审也可能不清楚本文与其他方法的部署约束不同，而非一定认为某个基线更强。

**足够答案的条件**：比较同任务、可比质量/成本预算的代表性基线；说明实现来源、调参和失败处理。若基线不能直接适用，应具体解释所需改造，并避免将“技术上不同”当作不比较的全部理由。

**义务与动作**：先核对最近邻方法；缺关键对照且保留优越性主张时必须补。结果不利时转为真实的成本—质量取舍，不能重选不利于基线的设置。

**未完成时英文**：

> A direct comparison with [relevant baseline] is needed to establish [claim]. That comparison is not yet complete, so our current conclusion is limited to [verified scope].

### 02. 基线可能没有公平调参

**代表性表述（概括）**：如果增强基线没有获得合理的调参和控制条件，当前性能差距可能高估了本文的优势。

**来源**：[WILD-Diffusion，vXtY 初评](https://openreview.net/forum?id=OrCVuQAYzF&noteId=Q6k8zoxuge)；[作者补调参敏感性与条件生成实验](https://openreview.net/forum?id=OrCVuQAYzF&noteId=sls1f8npue)。

**优先验证的假设**：优势是否来自更好的方法，而非只给本文更合适的超参数。问题解释高、重要性中高。**替代解释**：基线确实已合理调参，但论文未披露；或者标准默认值在该数据分布不适用。

**足够答案的条件**：披露搜索空间、验证集选择规则、各方法预算、随机种子及最终选择；区分默认值、缩小预算调参和充分调参。不能只说“遵循原论文”来证明公平。

**义务与动作**：已有日志足以核验时先澄清；存在不对称搜索时补匹配实验或降低性能主张。不要使用测试结果挑最优超参数。

**未完成时英文**：

> The current comparison does not establish matched tuning effort. A controlled search over [specified ranges] is still needed; we should not attribute the entire gap to the method before that check.

### 03. 某个组件的作用没有被隔离

**代表性表述（概括）**：请补充只保留 MD、移除 SCA 的配置，以分清两个组件各自的贡献。

**来源**：[MOSAIC，cdZj 初评](https://openreview.net/forum?id=7AH0y1OtnC&noteId=eHffXZKdWy)；[完整消融回应](https://openreview.net/forum?id=7AH0y1OtnC&noteId=kf9570Bavb)。

**优先验证的假设**：性能来自哪个组件，二者是否互补或只是一个组件独立起作用。问题解释高、重要性中；不能仅凭补一项消融推断必然提分。**替代解释**：评审可能想比较实现成本，而不只是性能贡献。

**足够答案的条件**：在相同训练与评测配置下给 baseline、A、B、A+B；必要时区分参数量、额外监督和训练预算。说明交互项及稳定性，避免把一次差值直接称作普遍因果效应。

**义务与动作**：若主张组件独立必要或协同，缺对应对照就必须补。若算力只够最小实验，优先做能区分解释的缺失格，而非无关新数据集。

**未完成时英文**：

> The missing [B-only] setting is necessary to separate the contributions of [A] and [B]. Until it is evaluated, we cannot claim that both components are independently necessary.

### 04. 平均指标可能掩盖失败或权衡

**代表性表述（概括）**：跨预测距离取平均，可能掩盖某些距离尤其较远时点上的性能退化。

**来源**：[FACT，5JYU 初评](https://openreview.net/forum?id=j3gNYqrHtl&noteId=4TezqJ3sqL)；[作者补具体预测时点](https://openreview.net/forum?id=j3gNYqrHtl&noteId=B3jyOj0QRt)。

**优先验证的假设**：总体均值改善是否由容易的子任务驱动，最重要或最困难的条件是否反而变差。问题解释高、重要性中高。**替代解释**：原指标是领域标准，但评审关心的部署目标不同；标准协议和补充分解可以并存。

**足够答案的条件**：保留标准指标，同时展示按预测距离、任务、群体或难度分层的结果；明确预先选择规则。报告不利分层，不只列最有利部分。

**义务与动作**：已有逐样本输出时可重算，不必重新训练。若整体结论无法在重要分层成立，修改“全面优越”的措辞。

**未完成时英文**：

> The aggregate metric does not answer whether performance degrades at [critical condition]. We need the corresponding breakdown before making that claim; the standard aggregate alone is insufficient.

### 05. 定理没有覆盖实际运行的算法

**代表性表述（概括）**：实现中存在随机操作，而当前分析按确定性映射处理，两者之间的理论覆盖关系尚未成立。

**来源**：[ADMM-PnP，srVv 初评](https://openreview.net/forum?id=BiXwSIIMIq&noteId=AaQdIH9D86)；[作者补有限步分析](https://openreview.net/forum?id=BiXwSIIMIq&noteId=rcP00y9UGz)。

**优先验证的假设**：理论结论是否依赖实现中不成立的确定性、平稳性、步长或凸性。问题解释高、重要性高。**替代解释**：分析本来只描述理想版本，但论文没有把理想版和实现版分开。

**足够答案的条件**：逐条映射算法步骤与假设；给出包含实际随机性/有限步误差的定理，或明确缩小保证。将固定点收敛、目标驻点和最优解区分。

**义务与动作**：若声称理论覆盖实现，发现缺口必须修证明或撤回该覆盖主张。不能用更多视觉样例回答数学缺口。公开承认必要的假设修正，不把全部差异称作“minor clarification”。

**未完成时英文**：

> The present theorem covers [idealized setting], while the implementation uses [verified difference]. Extending the guarantee requires [missing argument]; we do not yet claim that this extension has been proved.

### 06. 定义、记号或概率设置不清

**代表性表述（概括）**：该假设使用了 F、G 等对象，但它们的定义及所在位置不够清楚。

**来源**：[Bilevel Uniform Convexity，qtYP 初评](https://openreview.net/forum?id=dJgb3ngAvT&noteId=mtXgizlMxV)；[定义及组织回应](https://openreview.net/forum?id=dJgb3ngAvT&noteId=dGq80DsO59)；[独立随机源说明](https://openreview.net/forum?id=dJgb3ngAvT&noteId=1SXHdKN9Na)。

**优先验证的假设**：读者能否明确重建数学对象及保证依赖关系。问题解释高、重要性中高。**替代解释**：定义已经在其他位置，但不易发现；也可能确实缺少定义或量词，影响正确性。

**足够答案的条件**：核对提交版，给精确定位；统一符号、修编号，将算法必需定义移至可见位置；明确期望和高概率分别针对哪些随机源。不能仅以“见附录”回应一个实际缺失的定义。

**义务与动作**：已有定义则明确纠正事实并改善定位；缺失则补充；如果补充后改变定理含义，按实质修正处理。

**已核验原稿确有定义时英文**：

> In the submitted version, [symbol] is defined in [exact location]. The connection to [assumption] is not sufficiently explicit. [State the actual status of a clearer cross-reference or definition.]

### 07. 方法似乎只是已有组件或简单删减

**代表性表述（概括）**：删除已有模块除了工程简化之外，究竟带来了什么非平凡的方法或知识增量？

**来源**：[Triangle Multiplication，J8sg 初评](https://openreview.net/forum?id=CrXcfMLR9q&noteId=tpvXc0GfSk)；[机制分析后的评审回应](https://openreview.net/forum?id=CrXcfMLR9q&noteId=Kq0Zg9XRM1)。另见 [LCA 承认 IM 属直接适配](https://openreview.net/forum?id=3uINmRldVW&noteId=yDlbZYGp2i)及[评审认可贡献定位](https://openreview.net/forum?id=3uINmRldVW&noteId=yxNHvwiq0P)。

**优先验证的假设**：论文新增了什么可验证的知识，而不只是换名字、移植场景或挑选已有模块。问题解释高、重要性高。**替代解释**：新知识存在但没有被解释，或者贡献应定位为可靠的简化、机制发现或系统实证。

**足够答案的条件**：逐项列已有部分、真正新增部分及其价值；用机制分析、严格比较或理论支持对应增量。不能只用更高分数证明思想新颖，也不能把“首次用于某模型”自动等同方法创新。

**义务与动作**：承认已有组件；发现原表述夸大时改引言与贡献列表；需要机制证据时补分析。若确实只有工程贡献，应按实证强度和实际价值解释，不虚构数学创新。

**定位核实后英文**：

> [Component] is an adaptation of [verified prior work], not a separate novelty claim. The contribution we can support is [specific new knowledge], backed by [verified evidence or clearly identified missing evidence].

### 08. 结论只在窄任务或模型族中验证

**代表性表述（概括）**：当前任务覆盖不足以证明剪枝结论也适用于生成、数学推理等不同能力。

**来源**：[Layer Pruning，mE3b 初评](https://openreview.net/forum?id=04Tfwy3LLC&noteId=nII3u1uhJm)；[作者补生成和MoE证据](https://openreview.net/forum?id=04Tfwy3LLC&noteId=GNfmVg8Bgn)。

**优先验证的假设**：结论是否依赖多项选择任务、某架构或某规模，不能推广到作者声称的目标范围。问题解释高、重要性高，因为原评明确给出补实验后愿重新评价。**替代解释**：文章本来只主张窄场景，但标题/摘要让人以为通用。

**足够答案的条件**：根据差异机制选择有判别力的新任务/架构，而非随机增加数据集；说明协议、原模型性能及匹配基线。一个新增模型只能支持相应范围，不能证明全面通用。

**义务与动作**：保留广泛主张就必须补足代表性验证；无法完成则改标题、摘要与结论。不要借用他人论文的不同设置数字作为严格同条件比较而不披露。

**未完成时英文**：

> The current experiments establish [tested scope], but not [requested generalization]. We do not yet have verified results for [new setting], so that broader claim should remain unmade.

### 09. 搜索、预处理或部署成本可能被藏起来

**代表性表述（概括）**：结构搜索本身可能很昂贵，需要解释其真实时间成本，而不能只报告搜索完成后的效果。

**来源**：[Atomic HINs，8dUP 初评](https://openreview.net/forum?id=AG7fjg5azU&noteId=k14YmT8pQ9)；[逐trial耗时和复用说明](https://openreview.net/forum?id=AG7fjg5azU&noteId=3nu0AAQ7Q0)。

**优先验证的假设**：核心收益是否被未计入的搜索、构图或调参成本抵消。问题解释高、重要性高，评审明确将提分与澄清相联系。**替代解释**：成本是一次性的，可跨模型/任务摊销，但正文没说明。

**足够答案的条件**：给端到端与分项成本、硬件、输入规模、运行次数；区分一次性与每次部署成本；摊销必须有真实复用条件。理论复杂度、FLOPs、秒数、显存不是同一指标。

**义务与动作**：若效率是核心卖点，必要成本缺失应补测或撤回效率比较。已有日志可提取实测值，不必重复所有训练；不能排除不利的失败trial或搜索成本。

**未完成时英文**：

> The cost accounting must include [search/preprocessing] as well as [main stage]. Until those terms are measured, we cannot claim an end-to-end efficiency advantage.

### 10. 阈值或模型选择可能使用了测试集

**代表性表述（概括）**：如果根据测试结果选择最佳阈值，所报告的测试性能就可能受到模型选择泄漏的影响。

**来源**：[Procedural Mistake Detection，JzSx 初评](https://openreview.net/forum?id=HsB5EuQOoS&noteId=zFSIr5C01q)；[固定阈值网格与聚合协议说明](https://openreview.net/forum?id=HsB5EuQOoS&noteId=gwewxbD6xU)。

**优先验证的假设**：测试性能是否受评测泄漏或事后挑选所抬高。问题解释高、重要性高。**替代解释**：实际是预先规定的阈值积分/聚合，评审误以为选最佳阈值。

**足够答案的条件**：列明每个参数何时、用哪部分数据确定；区分固定扫描后聚合与利用测试标签挑最大值；给可执行评测规则。不能只说“标准协议”或“没有泄漏”而不解释数据流。

**义务与动作**：若是误读，直接用真实协议纠正；若确有测试集选择，必须改成合法验证流程并重算，或明确原结果不支持无偏测试结论。这是有效性问题，不宜推迟为未来工作。

**核实协议后英文**：

> The relevant distinction is between [predefined aggregation] and selecting a threshold using test labels. Our verified protocol is [exact rule and data split]. [State any required correction and its actual status.]

### 11. 定理的条件保证被误解为存在性保证

**代表性表述（概括）**：证明中的数据规模、合成集大小和维度之间的关系不清，似乎不能覆盖有意义的大幅压缩区间。

**来源**：[Dataset Distillation Guarantees，3Mno 初评](https://openreview.net/forum?id=zueIXg5FP5&noteId=rDb425zHej)；[第二轮存在性与下界澄清](https://openreview.net/forum?id=zueIXg5FP5&noteId=ZJa4qlv8xJ)。

**优先验证的假设**：结论是否真的覆盖作者宣传的压缩区间；“若存在一个合成集则有保证”是否被误述为“任意小合成集都存在”。问题解释中高、重要性高；追问通常能进一步确认。**替代解释**：证明中辅助网的大小被误认为原数据规模限制。

**足够答案的条件**：写清量词、条件对象与辅助构造；分别回答保证、存在性、可计算性；给必要下界、反例或不覆盖情形。不要只重述定理而回避评审提出的参数范围。

**义务与动作**：若推断超出定理，改主张；若证明混乱，给简化例子和明确变量表；缺存在性结论时不能凭小型实验宣称理论已解决。

**核实定理后英文**：

> This is a conditional guarantee: if [condition], then [conclusion]. It does not establish the existence of [stronger object] for arbitrary [parameter]. That distinction must remain explicit in the claim.

### 12. 理论估计器缺少准确性标定或实际用途

**代表性表述（概括）**：缺少可以获得真实答案的分布上的校验，尤其缺少支持高维准确性主张的验证。

**来源**：[Neuromanifold Metric Tensors，rVQk 初评](https://openreview.net/forum?id=Ssevs8KCsU&noteId=PatpJvipfo)；[真实FIM对照与用途说明](https://openreview.net/forum?id=Ssevs8KCsU&noteId=lrdIzIbByp)。

**优先验证的假设**：估计器是否准确、与现有近似相比何时值得多付成本。问题解释高、重要性中高。**替代解释**：评审不一定要求一整套新下游SOTA系统，只是需要理解估计精度为何重要。

**足够答案的条件**：在可得真实值的规模上给误差、方差与成本；区分无偏估计和有偏替代；若宣称下游改善就需相应下游证据，若只提供理论工具则准确解释其可用范围。

**义务与动作**：核心准确性未标定时补真实值对照；不要用另一估计器的输出冒充ground truth。若资源不足以算全规模真实值，采用可解释的小规模标定并承认外推限制。

**未完成时英文**：

> Accuracy should be checked against [available ground truth], not only another approximation. Without that calibration, we cannot yet substantiate [accuracy claim] at [target scale].

### 13. 要求真实数据或另一更新规则，可能超出当前理论对象

**代表性表述（概括）**：实验尚未涉及自然数据，因此需要说明当前理论对象与实际数据的关系及适用边界。

**来源**：[Dense Associative Memory Dynamics，cF5v 初评](https://openreview.net/forum?id=TeDkzf34hs&noteId=HAsFrILc41)；[独立模式与同步更新边界说明](https://openreview.net/forum?id=TeDkzf34hs&noteId=vS2CMprrEa)。

**优先验证的假设**：理论对象与自然数据/实践使用是否足够相关，或作者是否对应用性过度概括。问题解释中、重要性中高。**替代解释**：评审可能按应用论文标准评价一篇明确研究特定分布的理论论文。

**足够答案的条件**：说明分析依赖的独立性、分布和更新规则；解释替换后哪些推导需要改变；确认本文的贡献在当前对象上是否成立。若正文宣传自然图像表现，就必须补验证或收窄，而不能只说不适用。

**义务与动作**：若评审明确以缺少该扩展否定现有理论贡献，可说明不同研究目标及其依据；不能把一个补实验建议擅自改写成评审否定了全部理论价值。自然数据和异步分析尚未完成就保持未完成；不能把已讨论的未来方向写成已解决。

**范围核实后英文**：

> Our analysis assumes [specific distribution/update rule]. Extending it to [requested setting] requires [technical change] and is not established here. The claim we can support is [bounded contribution].

### 14. “没有代码/没有某实验”等可核对的事实判断

**代表性表述（概括）**：评审没有找到可以使用的代码，因此认为当前材料不足以支持复现。

**来源**：[SuperMAN/GMAN，PX2M 初评](https://openreview.net/forum?id=1MVeSLvfxU&noteId=m0odp4ORGX)；[作者指出提交的补充zip](https://openreview.net/forum?id=1MVeSLvfxU&noteId=LMsAPlcXZ7)。

**优先验证的假设**：评审能否获取足以复现的材料。问题解释高，决策重要性未知。**替代解释**：材料确实缺失；已提交但入口难找；链接失效或权限不对；只有代码而缺运行说明。

**足够答案的条件**：核对当时提交包与匿名访问状态，指出具体路径和运行入口。若无法访问，修复访问比争论“曾经上传”更重要。

**义务与动作**：确认原稿已有则明确纠正，必要时承认入口不清；实际新增则如实写新增日期，不倒写成原先已有。不能把代码存在等同可复现性已经全面解决。

**确认提交包确有材料后英文**：

> The submitted supplementary archive contains [file/path] and [verified instructions]. The entry point may have been difficult to find. [State any verified access issue and the actual correction status.]

### 15. 机制解释只有直觉，没有对应测量

**代表性表述（概括）**：如果要用教师表征持续变好来解释收益，就应测量其训练过程中的质量变化，而不只给最终生成效果。

**来源**：[Self-Representation Alignment，NzJf 初评](https://openreview.net/forum?id=ds5w2xth93&noteId=Y2v5D8MB2F)；[作者报告教师/学生随训练线性探测](https://openreview.net/forum?id=ds5w2xth93&noteId=F6wmJxEqdZ)。

**优先验证的假设**：所谓教师持续改善是否发生，以及它是否能支持作者提出的机制解释。问题解释高、重要性中高。**替代解释**：整体生成性能提高，但教师表征质量不一定提高；二者相关也不自动证明因果。

**足够答案的条件**：用对应机制的代理指标和时间序列测量，给相同评测协议；若要声称因果作用，还需要干预或相应消融。不能用最后一轮FID代替对教师能力轨迹的测量。

**义务与动作**：如果机制是解释性猜想，明确标记；若当作已证实机制，就补测量或降格为假设。结果不支持时删去该解释，不必因此否认仍成立的经验结果。

**未完成时英文**：

> The proposed mechanism predicts [observable trend], which has not yet been measured. We should treat it as a hypothesis, not an established explanation of the performance gain.

### 16. 评审和作者对任务价值或成本目标理解不同

**代表性表述（概括）**：不仅实验对照不足，这个选视角任务在真实使用中是否有必要也需要说明。

**来源**：[PEERING INTO THE UNKNOWN，Wvnw 初评](https://openreview.net/forum?id=e7gbgdw05A&noteId=zRY9kzCkBC)；[观测预算与更强重建后端回应](https://openreview.net/forum?id=e7gbgdw05A&noteId=rx6BVJe4UA)。

**优先验证的假设**：这个任务在真实约束下是否有用，收益是否只是离线评测定义产生的。问题解释高、重要性高。**替代解释**：评审把观测/运动成本误当成重建训练时间；或作者的真实部署动机本来就欠充分。

**足够答案的条件**：明确谁使用系统、受什么约束、优化哪种成本；给全信息上界和强后端对照；说明离线模拟不能验证哪些真实部署因素。

**义务与动作**：若成本目标被误解，直接纠正定义；如果正文同样含糊，必须改正文。更强后端、真实可达视角等与结论相关时补验证，不能只讲应用故事。

**目标核实后英文**：

> The target resource is [observation/motion cost], not [different resource]. Under [explicit constraint], the relevant question is [testable benefit]. [State what evidence exists and what remains unverified.]

### 17. 复杂度的计算模型、精度或隐藏因子不一致

**代表性表述（概括）**：有限精度计算通常只能产生近似结果，不能不计精度代价就调用精确求逆并沿用原有复杂度结论。

**来源**：[Quantum Attention，zcdq 初评](https://openreview.net/forum?id=0zIcPe4CtY&noteId=LB4mcYJhXY)；[小矩阵条件数与子空间嵌入回应](https://openreview.net/forum?id=0zIcPe4CtY&noteId=kwnRwQZXxe)；[提分及重大修订警告](https://openreview.net/forum?id=0zIcPe4CtY&noteId=RhSckfziEE)。

**优先验证的假设**：论文宣称的次线性/加速是否在合理计算模型下仍成立，误差精度或条件数是否抵消收益。问题解释高、重要性高。**替代解释**：不同复杂度模型的界都正确，但作者把它们混在一个主张中。

**足够答案的条件**：定义输入访问、位精度、成功概率、输出对象、误差范数和隐藏参数；把每个子程序代价及误差传播代入最终界，检查目标规模下是否仍满足声称速率。

**义务与动作**：存在缺口时必须补严格分析或削弱复杂度主张；不能以“标准子程序”跳过决定结论的代价。修复若实质改变论文，应如实说明，不能把大修包装成笔误。

**未完成时英文**：

> The runtime claim must include the dependence on [precision/conditioning/access model]. That dependence is not yet justified by the current argument, so the stated bound requires correction or a complete derivation.

## 五、多轮跟进规则

### 5.1 每轮重新提取剩余问题

对最新追评单独解析，不沿用首轮标签。例如，第一轮补消融后，评审转而质疑新颖性；此时重复消融不会回答新问题。LCA 的[后续贡献定位](https://openreview.net/forum?id=3uINmRldVW&noteId=yDlbZYGp2i)与 Dataset Distillation 的[第二轮存在性澄清](https://openreview.net/forum?id=zueIXg5FP5&noteId=ZJa4qlv8xJ)都体现了问题焦点变化。

每轮记录：

1. 已明确认可的事项。
2. 仍有分歧的事项及具体原因。
3. 新提出的问题及其与原问题的关系。
4. 是否出现明确改分条件。
5. 作者实际完成的动作和仍未完成的部分。

“大部分解决”不能自动关闭整条问题；“thanks”不能自动解释为满意；没有回复始终是未获确认。新问题也不自动意味着评审在移动门槛，应先检查它是否由新结果或此前不完整解释引出。

### 5.2 条件性提分必须保留条件

将“我会升分，条件是X”存为 `条件承诺，X未核实/已落实`。作者落实X只证明动作完成，不自动证明评审已经再次确认或系统中的数字已经更新。若后续评审明确确认，再升级状态。

DeMo 的[条件承诺](https://openreview.net/forum?id=U9oewpa7cn&noteId=MbpXnuAD0V)与[作者报告已补说明](https://openreview.net/forum?id=U9oewpa7cn&noteId=NvEbHm5jYY)应作为两个事件记录。不能写成四位评审均已提高评分。

### 5.3 跟进的内容与频率

优先在补充了实质证据、完成了承诺修订，或临近截止且已给对方合理阅读时间时做一次简短跟进。给出新增内容与精确位置，询问是否仍有核心问题，不重复催分。

> The response now addresses [specific remaining issue] through [verified evidence/location]. Is there a remaining technical concern affecting your recommendation?

该模板只在确有新增证据时使用；否则可如实询问先前问题是否需要进一步解释。不得利用作者投入、时间压力或人情要求认可；不得推测不回复的动机。

### 5.4 对不同意见的三种状态分别处理

- **事实分歧**：对照提交版本、日志和协议；给可验证定位。
- **理论/实验分歧**：给推导、对照或反例；必要时承认未解决。
- **价值判断分歧**：准确陈述双方已达成和未达成的判断，让 AC 评估；不要把没有被说服等同评审错误。

APT 的[评审后续自我修正](https://openreview.net/forum?id=CODnlyYUli&noteId=vKLQpAKi1u)明确包含同行讨论因素，说明提分未必全部由作者回应直接造成。技能不能将任何时间上相邻的修订与涨分都归为确定因果。

## 六、AC 摘要规则

### 6.1 摘要应让 AC 能独立复查

按争点组织，而非堆砌感谢或一长串新增实验：`核心顾虑 → 新证据 → 论文位置/版本 → 评审实际态度 → 剩余边界`。

状态必须使用不同字段或标签：

- 评审本人明确说已改分。
- 评审本人明确表示将改分。
- 带条件的提分意愿，及条件当前状态。
- AC 对历史变化的明确记录。
- AC 对正常讨论会如何发展的预测。
- 作者转述、无法独立确认。
- 证据冲突，需保留两方原句。

没有终值就写未知。评审只表示提高了评分、却未给总评分终值时，不得补成6→8。只有初始低分和最终接收时，不得推出该评审已经转正。

### 6.2 2026的特殊记录方式

ICLR 2026 将评分和评审正文回滚到讨论前，并由新的 AC 解读已发生的讨论。回滚字段不能作为讨论结束后的分数；“would / likely / expected”不等于实际改分。参见[官方安全事件说明](https://blog.iclr.cc/2025/12/03/iclr-2026-response-to-security-incident/)与[官方评审流程回顾](https://blog.iclr.cc/2026/03/31/a-retrospective-on-the-iclr-2026-review-process/)。其他年份须核对当年规则，不能机械套用2026流程。

摘要模板：

> The main concerns were [A], [B], and [C]. For [A], the verified new evidence is [artifact/location]. For [B], [state whether a correction is incorporated or still pending]. [C] remains unresolved within [scope].
>
> Reviewer [R1] explicitly stated [actual stance; note link]. Reviewer [R2] expressed a conditional intention to [change], subject to [condition]; the condition is [verified status]. Reviewer [R3] has not responded, so we do not infer a changed assessment.
>
> The contribution supported by the revised evidence is [bounded claim]. The remaining limitation is [specific limitation].

正文中任何“所有问题已解决”“所有评审支持”“一致同意”的词都要逐条核对；有一个未回复或保留疑虑，就不能使用这些概括。

## 七、工作表字段与质量门槛

建议一行对应一个可独立验证的问题，而非一位评审一行。不同评审提出相同核心问题时可共享证据任务，但分别保留各自原句、态度和追评状态。

| 字段组 | 建议字段 | 约束 |
|---|---|---|
| 来源与身份 | issue_id；匿名reviewer_id；forum_url；review_note_id；note时间；轮次；原句与原问题编号 | 只使用公开匿名标识，不反向推测真实身份 |
| 当前主张 | claim_id；准确主张；论文版本；页/节/表/公式；贡献重要性 | 防止用新版本内容反驳旧版本缺失 |
| 意图推断 | 直接问题；优先验证假设；问题解释置信度；置信依据；至少一个替代解释 | 推断与原话分列，不假装心理事实 |
| 决策重要性 | 主要/次要/未知；重要性置信度；明确改分条件；相关原句 | 分数低不等于每条意见都决定拒稿 |
| 证据义务 | 需要排除的混杂；最小充分证据；可接受替代测试；是否需要补实验/证明 | 每个实验对应一个问题，不能只列数量 |
| 现有证据 | 数据/代码/日志/证明路径；版本；复核状态；与主张的对应关系 | 作者口述不自动等同已核查证据 |
| 执行计划 | 动作类别；数据划分；基线；搜索预算；seed；指标；资源；负责人；截止；依赖 | 计划不作为完成事实；避免测试集选参 |
| 结果与限制 | 已验证结果；不利结果；误差/波动；不能回答的问题；影响哪些主张 | 不隐去失败或把小规模结果外推全范围 |
| 执行状态 | 未计划/已计划/进行中/完成待核查/已核查/已纳入版本 | 状态需由相应产物支持 |
| 修订传播 | 需更新的摘要/贡献/正文/图注/附录/代码；实际位置；版本时间 | 回应修改不等于论文修改；跨评审数字保持一致 |
| 对话状态 | 未回应/已回应/部分认可/明确认可/仍反对/未再回复；下一步问题 | 作者判断“解决”与评审“认可”分别记录 |
| 评分证据 | 初分来源；实际自述/承诺/条件/AC历史/AC预测/作者声称/冲突；终值或未知；note链接 | 不把条件承诺、沉默或预测写成实际改分 |
| 文字输出 | 英文草稿；可验证定位；未完成声明；适度道歉是否必要；待核查句子 | 每个过去时动作和每个数字必须有依据 |

### 输出前检查

- 每个推断是否有原句依据并保留合理替代解释？
- 是否把“需要验证”误写成“评审已经否定”？
- 所有实验、证明、修订动作的时态是否与产物状态一致？
- 直接反驳是否基于评审所读版本，而非后来补上的材料？
- 是否承认了已经核实的错误，并说明它如何影响结论？
- 是否一边保留宽泛宣传，一边用范围限制拒绝必要验证？
- 新数据或新证明是否回答核心问题，而不是转移话题？
- 未完成的工作、负结果和仍然存在的缺口是否明确保留？
- 是否将评审的礼貌、沉默、部分认可或条件意愿夸大成完全同意？
- AC摘要中的每个态度与数字是否能回到具体note核查？

## 八、速查规则

1. 先准确解释问题，再选择证据，最后写措辞。
2. 对审稿问题的理解与它对决策的重要性分别评级。
3. 为保留一个主张承担相应证据义务；不能完成则缩小主张或保留未解决。
4. 客观事实错误可以直接纠正；必要证据缺失必须补或让步，不能混淆。
5. 承认错误要跟随修复、影响说明和真实修订状态。
6. 方法增益、机制解释、理论保证与实用价值是不同主张，需要不同证据。
7. 每轮回应最新剩余问题，不重复上一轮已完成的辩护。
8. 评审是否认可、作者是否完成、系统是否改分是三件不同的事。
9. 诚实记录结果、边界和不确定性，不能为提分创造事实。
