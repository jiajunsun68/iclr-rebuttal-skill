## 精修后的英文 rebuttal

> 虚构演练的模型输出，不对应真实投稿或实验。[输入材料](../03_style_fidelity.md)。除链接转为仓库相对路径及本说明外，保留原输出内容。


**R2-W1: Stability of the empirical results**

The current evidence does not establish stable gains across random seeds. Relative to the baseline, accuracy changes by +1.3 percentage points on A, +0.2 on B, and −0.3 on C. The preregistered two-sided test on A gives \(p=0.08\), which does not meet the significance threshold of \(\alpha=0.05\). We do not claim statistical significance for B or C.

The five-seed extension is still running, and its results are not yet available. The original table does not report means from these extension runs. Table 4 and Appendix B of revision v2 contain the original comparisons on all three datasets and the specification of the test on A.

**R2-W2: Scope of the theoretical guarantee**

Under the stated L-smooth assumptions and 0 < η ≤ 1/L, we establish
\[
f(x_{t+1}) \le f(x_t) - \frac{\eta}{2}\|\nabla f(x_t)\|^2.
\]
This inequality provides a per-step descent guarantee under these conditions. It does not establish global optimality. Our analysis follows \cite{smith2024}.

## 实质改动说明

- 删除“所有数据集均显著优于基线”的结论，保留三个准确率差异及“百分点”单位，明确 C 为负结果。A 的 \(p=0.08\) 未达到 \(\alpha=0.05\)；B、C 未提供检验，因此不作显著性判断。
- 明确五个 seed 的扩展实验仍在运行，原表不是这些扩展运行的均值；保留 revision v2、Table 4 和 Appendix B 的定位，不宣称稳定性问题已解决。
- 将全局最优主张收窄为给定 L-smooth 条件与步长范围下的逐步下降保证；公式及引用键 `\cite{smith2024}` 原样保留。
- 删除过度致谢和突破性、变革性等无证据修辞；未新增实验结果、文献或修订承诺。
