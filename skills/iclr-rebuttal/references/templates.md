# Response templates by substantive action

[English](templates.md) · [简体中文说明与模板](templates.zh-CN.md)

These are original, adaptable *structures*, not actual text from the ICLR case authors. Brackets denote unverified placeholders. No template authorizes inventing measurements, citations, reviewer agreement, or finished manuscript edits. Choose the tense appropriate to the fact ledger and remove unused alternatives.

## 1. Clarify existing evidence

> Both methods use [verified matched condition], as specified in [location]. They differ in [precise distinction]. We [have clarified / will clarify] this setup in [location] so the comparison is easier to verify.

Use when evidence exists but presentation is unclear. Do not finish with “please see our paper”; quote the essential distinction. If the existing control is genuinely inadequate, proceed to add evidence rather than treating it as reviewer oversight.

## 2. Rebut a demonstrably false factual or mathematical premise

> The statement that [disputed premise] does not hold under [specified definition/assumption]. In particular, [checkable derivation, configuration, or counterexample]. This supports [bounded conclusion]. We [have clarified / will clarify] [explanation] in [location].

Check that the reviewer and authors are using the same settings. Correct the proposition, not the reviewer’s competence. Do not apologize for a supported disagreement.

## 3. Admit and correct a real error

> You are correct that [specific verified mistake]. We apologize for [material mistake, if appropriate]. We [have corrected / will correct] [concrete change]. [State verified effect on results, or explicitly say the impact is still being evaluated.] The revision is [actual location or pending status].

Use for a missing citation, numerical/implementation error, unfair comparison, or unsound proof—not for routine theoretical disagreement. A minor explanation problem often needs acknowledgement and correction without an apology.

## 4. Report verified additional evidence

> We tested whether [alternative explanation] accounts for the improvement using [discriminative, matched comparison]. Under the same [data/budget/protocol], we observed [actual result and relevant uncertainty]. This supports [precise conclusion] within [specified scope]. We have added [actual result] to [real revision location].

Delete the last sentence if the result has not been incorporated. A negative or mixed result should be reported as such; do not insert “significant,” “consistently,” or “state of the art” without support.

## 5. Evidence is important but not yet available

> The present comparison does not isolate [confound]. We [plan to test / cannot currently complete] [specific control] under [matched conditions]. Until those results are available, we [have narrowed / will narrow] the conclusion to [currently supported scope]. We cannot yet establish [stronger assertion].

Only say “plan to test” when feasible. This is a transparent interim statement, not a submission-ready positive result.

## 6. Narrow an overbroad claim

> We agree that our original claim was too broad. The evidence supports [new bounded claim] under [conditions], but does not establish [unsupported generalization]. We [have revised / will revise] the abstract, [relevant theorem or experiment], and the limitations accordingly.

When novelty is questioned, distinguish inherited components from a new mechanism, insight, setting or capability.

## 7. Address related work and novelty precisely

> [Prior work] already introduces [shared mechanism], which our original draft did not sufficiently distinguish. Our contribution is [specific new result/problem/implementation], not [inherited component]. We have added [direct comparison or corrected citation] to [actual location].

If a citation was omitted, acknowledge the omission directly. Do not portray recombination as an entirely new primitive.

## 8. Decline an out-of-scope requirement without evasiveness

> [Requested setting] changes [assumption/target task] relative to the claim studied here. We therefore do not use the present evidence to claim success in that setting. To clarify the boundary, we [have added / will add] [scope statement or feasible diagnostic] in [location].

A request can still expose a weakness in generalization; assess whether the paper itself promised that scope.

## 9. Respond to a follow-up

> The remaining question is whether [reviewer's latest concern]. Our first reply addressed [previous, distinct issue] but did not establish [missing link]. We now [provide new, verified evidence or explicitly state current limitation]. The updated [section/table] is [location].

Do not paste the previous rebuttal in full. If the new work is pending, label the pending state.

## 10. Ask a narrow clarification question

> We read this comment as asking whether [testable interpretation A], rather than [materially different B]. We can test [control] for A, while B would require [different scope]. Which is the concern most relevant to the recommendation?

Ask only when the distinction changes action. If both are directly answerable, answer them first.

## 11. AC summary with evidence attribution

> The main concerns were [A], [B] and [C]. We have incorporated [verified changes and locations]. R1 explicitly [reported an increase / expressed an unconditional intention / gave a conditional intention] in [note]. R2 [partly accepted / did not reply / remained opposed] regarding [issue]. The outstanding limitation is [X]. We do not claim reviewer agreement beyond these records.

Do not turn a conditional “would raise if X” into “raised,” or an AC prediction into a reviewer action.

## Final language audit

Check every number, equation, negative statement, assumption, statistical inference, experimental completion verb, reviewer position and revision location against the supplied materials. Use [the academic Humanizer adaptation](humanizer-academic.md) *only after* the substantive claim is correct.
