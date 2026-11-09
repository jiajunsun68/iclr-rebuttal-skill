# 证据、修订与评审态度

## 目录

- [事实账本](#事实账本)
- [完成状态](#完成状态)
- [评审态度](#评审态度)
- [ICLR 2026 特殊口径](#iclr-2026-特殊口径)
- [多轮讨论](#多轮讨论)
- [AC 摘要](#ac-摘要)

## 事实账本

为每项影响结论的事实记录 `claim_id / 内容 / 来源或实验配置 / 核验状态 / 适用条件 / 论文位置`。

锁定以下内容再做语言润色：

| 对象 | 要核对的细节 |
|---|---|
| 结果 | 数值、单位、方向、分母、绝对/相对提升、样本量、随机性 |
| 公平性 | 数据与划分、预训练、模型大小、调参预算、调用次数、实现版本 |
| 统计 | 种子数、方差/区间、检验假设；没有依据时不用 statistically significant |
| 理论 | 假设、量词、极限/有限样本、必要/充分、上界/实际值、存在性/可训练性 |
| 评价 | judge、人工评估、规则、失败处理、盲法或顺序设置 |
| 修改 | 实际版本、页/节/表/附录、尚未执行的承诺 |
| 引用 | 文献真实存在、比较对象相关、链接指向所述记录 |

结果冲突时指出冲突，回到来源核验。不要让表达流畅度决定哪个数字被保留。案例中的数字不能复制到用户论文中。

## 完成状态

按证据分开记录，不合并成一个“已解决”勾选框：

| 工作状态 | 允许的英文表述 | 还不能声称什么 |
|---|---|---|
| planned | We plan to evaluate… / We will add…（有落实能力时） | 已完成实验或修改 |
| running | The experiment is running; the result is not yet available. | 任意预期结果 |
| completed_unverified | We have completed the run and are checking… | 可靠结论或已通过核验 |
| verified | We evaluated… The verified result is… | 已写入论文，除非确已落稿 |
| incorporated | We have added the verified results to Table X of revision Y. | 评审已经认可 |

已经运行但设置有错，不能继续标 verified。已写回稿件的说明后来被删除或改动，也应更新状态。承诺的实验未完成，选择保留限制或调整主张；不要伪造已完成句式。

## 评审态度

用 `no_response / unresolved / partly_resolved / author_revision_pending_confirmation / reviewer_confirmed / conditional_raise / explicit_raise / disputed` 等标签分别记录。

- 作者解释充分，不代表评审确认充分。
- 评审认可某个实验，不代表全部意见解决。
- 条件承诺需要记录条件、作者动作、后续确认；作者已做与评审已确认不同。
- 本人说愿意提分但没给数字，不推补目标分数。
- AC 明确回顾历史改分，与 AC 预计会改分不同。
- 有后续反对时，不能只引用更早的乐观概括。
- 评分从 2 到 4 可能仍在拒稿侧。按当年量表解释，不跨年机械套用。

证据优先级用于解决具体事实冲突：精确、可定位的本人陈述通常优于作者总结；明确的历史记录不同于预测。若原始记录与采集快照不一致，保留差异，不挑更大的涨幅。

## ICLR 2026 特殊口径

ICLR 在 2025 年 11 月安全事件后将 review 正文与评分回滚至讨论开始前，冻结 reviewer 讨论并更换 AC。新 AC 根据已有原评、作者/评审讨论与独立判断评估论文，并推断讨论正常进行时的可能结果。

来源：

- [官方安全事件处理说明，2025-12-03](https://blog.iclr.cc/2025/12/03/iclr-2026-response-to-security-incident/)
- [官方评审流程回顾，2026-03-31](https://blog.iclr.cc/2026/03/31/a-retrospective-on-the-iclr-2026-review-process/)
- [ICLR 2026 Reviewer Guide](https://iclr.cc/Conferences/2026/ReviewerGuide)

因此，当前 rating 字段不能当成讨论终分。保留历史发言的日期、角色与 noteId。`would increase`、`likely increase` 是预测；“初始 8/4/2/2，最后 Oral”也不能证明三个低分评审都实际转正。

这里的“负转正”是评审判断从拒稿侧转向接收侧，不是正式 Reject 后申诉改判。对于其他会议/年份，核查其独立规则、分档、修订窗口和评论可见性；不要照搬 2026 的例外流程。

## 多轮讨论

每轮只更新最新争点，不重新发送整段首轮回复：

1. 摘出评审新回复明确保留的问题。
2. 区分新证据请求、对既有证据的质疑和定义/范围误解。
3. 将“足够答案”改为这一轮的条件，检查上一轮哪些证据仍然相关。
4. 给直接答案、关键证据、确实完成的修改及剩余边界。
5. 必要时询问新增证据是否回应主要担忧；不要催分或要求先承诺接收。

例子：[NSPO 的第二次提分](https://openreview.net/forum?id=GFyVxtyMvq&noteId=6jKiyVjkYR)对应近似与分布边界；[SCUBA 的第二次提分](https://openreview.net/forum?id=bkjKnO9s7T&noteId=PPgb7XQe7O)涉及轨迹采集与任务合成；[Self-Debug](https://openreview.net/forum?id=KuPixIqPiq)涉及 prompt 混杂。不要把同一个 2→4→6 写成单次措辞优化。

## AC 摘要

用 3–5 个最重要的变化组织，逐条给可核验位置：

| 争点 | 已完成证据 | 论文位置 | 评审实际回应 | 剩余问题 |
|---|---|---|---|---|
| 明确原问题 | 只列已核实工作 | 版本、节/表 | 原话的准确转述与链接 | 未解决或未确认项 |

若评审没有回复，直接写未回复；若保留理论意见，不能写 all concerns addressed；若作者做完条件所要求的修改但没有本人确认，写“修改已完成，等待确认”。

仅在确有流程/质量问题时向 AC 提供原句、论文证据、错误内容和影响。低分、不同学术判断或某种行文风格本身不能证明失职。最终接收还取决于剩余核心缺陷及 AC 判断，不能把均分上升作为充分理由。

边界案例：[FASA](https://openreview.net/forum?id=FnSgecCEwg&noteId=un60K64zf2)、[DeMo](https://openreview.net/forum?id=U9oewpa7cn&noteId=MbpXnuAD0V)、[Censoring](https://openreview.net/forum?id=vSXIEbTVhE&noteId=pyIl197Hos)、[MonoSoup](https://openreview.net/forum?id=ICANwnoGgN&noteId=Ax5fH58HGb)。
