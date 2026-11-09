# 场景 3：去 AI 味时保持科研语义

以下文本和数字均为虚构演练材料，不对应真实实验、论文或会议政策。请使用 `skills/iclr-rebuttal/SKILL.md`，只做英文 rebuttal 精修，并用简短中文列出实质改动或必须核实的内容。保留可核对的定位、公式和引用键，不需要查外部资料。

## 已核验事实

- R2-W1 关心效果是否稳定。三个数据集的准确率差异（本文减基线）分别是 A +1.3、B +0.2、C −0.3 个百分点，结果均已核验。
- A 的预注册双侧检验 p=0.08，阈值 α=0.05。B、C 没有给定统计检验。
- 五个 seed 的扩展实验正在运行，未完成；原表并非这五次扩展运行的均值。
- revision v2 的 Table 4 和 Appendix B 已包含上述三个数据集的原始比较和检验说明。
- 在已注明的 L-smooth 条件及 0 < η ≤ 1/L 下，论文只证明下面的下降不等式，不证明全局最优。公式必须保持不变。
- `\cite{smith2024}` 是演练中已有的引用键；没有提供它之外的新文献。

## 待编辑草稿

> We are profoundly grateful for the reviewer's exceptionally insightful comment. Our comprehensive and groundbreaking evaluation clearly demonstrates statistically significant superiority across every dataset. Specifically, A improves by 1.3 percentage points (p=0.08), B by 0.2, while C changes by −0.3. The five-seed extension is currently running. Table 4 and Appendix B of revision v2 now contain these comparisons and the A-test specification. This result marks a pivotal breakthrough and highlights the transformative potential of our robust optimization framework.
>
> R2-W2: Under the stated L-smooth assumptions and 0 < η ≤ 1/L, we establish
> \[
> f(x_{t+1}) \le f(x_t) - \frac{\eta}{2}\|\nabla f(x_t)\|^2.
> \]
> This guarantees globally optimal solutions in all practical settings. Our analysis follows \cite{smith2024}. In conclusion, this is not merely an incremental improvement but a new paradigm for reliable learning.
