# Evidence, revisions and reviewer follow-up

[English](evidence-and-followup.md) · [简体中文](evidence-and-followup.zh-CN.md)

## Fact ledger

For any claim affecting the argument, record \`claim_id / statement / source or experimental configuration / verification state / assumptions / manuscript location\`.

| Check | Protect |
|---|---|
| Results | Absolute vs relative differences; units, denominators, direction, sample count, random variation |
| Fairness | Dataset/split, pretrained weights, model size, tuning budget, inference calls, versions |
| Statistics | Number of seeds, spread and uncertainty, hypothesis/test; never assert significance without support |
| Theory | Assumptions, quantifiers, finite vs asymptotic guarantees, existence vs trainability, upper bound vs achieved value |
| Evaluation | Judge and protocol, human checks, failure handling, blind order or contamination risk |
| Revision | Exact manuscript version and section/figure/table; unexecuted plans |
| Attribution | Real citations, reviewer note IDs, and whether a score statement comes from reviewer/author/AC |

Conflicting numbers require source-level investigation; do not choose the more persuasive estimate. Never copy experimental numbers from a teaching case into the user's paper.

## Completion state (do not collapse)

| State | Accurate wording | Not justified |
|---|---|---|
| \`planned\` | We plan to test… / We will add… (only if feasible) | We ran / the result demonstrates |
| \`running\` | The experiment is running; results are not yet available. | Any predicted result |
| \`completed_unverified\` | We completed the run and are checking… | A verified result |
| \`verified\` | We tested… The verified result is… | Claiming it appears in the manuscript |
| \`incorporated\` | We added verified Table X to revision Y. | Claiming a reviewer endorsed the change |

If a run was performed under incorrect settings, it must not retain \`verified\` status. A change removed from the latest revision must not retain \`incorporated\` status.

## Reviewer stance (separate from work state)

Use explicit labels: \`no_response\`, \`unresolved\`, \`partly_resolved\`, \`author_revision_pending_confirmation\`, \`reviewer_confirmed\`, \`conditional_raise\`, \`explicit_raise\`, \`disputed\`.

Reviewer acknowledgement of one experiment is not proof that every concern is resolved. A conditional score raise requires recording the condition, author's action and reviewer confirmation separately. “Would increase” is not “increased”; an author's summary cannot supply a first-person numeric goal. An AC historical account is not an AC prediction. A 2→4 movement can remain on the reject side; interpret the year’s rating scale.

## ICLR 2026 rollback

Following the November 2025 security incident, ICLR restored text and ratings to their pre-discussion state, froze discussion and replaced ACs. New ACs used the surviving discussion and author responses plus their own judgment. Treat current rating fields as *pre-discussion* unless independently verified otherwise, and distinguish historical notes, reviewer's explicit intentions, conditions, author or AC reports, and predictions.

Official documents: [ICLR response, 2025-12-03](https://blog.iclr.cc/2025/12/03/iclr-2026-response-to-security-incident/) · [ICLR retrospective, 2026-03-31](https://blog.iclr.cc/2026/03/31/a-retrospective-on-the-iclr-2026-review-process/).

## Each follow-up changes the problem state

1. Quote the latest *remaining* issue, not the already addressed first-round concerns.
2. Check whether a new experiment/theory revision is actually needed or whether the confusion is only presentation.
3. Reply with the narrowest sufficient new evidence and exact revision location.
4. Ask one targeted question only if materially ambiguous.
5. Update work state and reviewer stance independently. Do not nag for a score.
6. Preserve the response chain (original review → author reply → reviewer follow-up → author correction → final response).

## AC summary

In 3–5 short units, identify: initial concern; newly verified evidence; location of incorporated change; reviewer-specific feedback and link; unresolved or conditional items. Do not claim universal support when reviewers were silent. For process-quality disputes, provide a grounded quote, demonstrable error and consequence—not guessed reviewer identity or motives.

Recommended concise status phrasing:

> R1 stated an unconditional intention to raise the score from 2 to 6 (note link); we have not independently verified a saved rating update. R2's conditional request remains partly unmet, and R3 has not followed up. The revised manuscript incorporates [verified change] in Section [X], while [remaining issue] is still a limitation.
