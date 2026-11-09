# Validation results — English-first bilingual release

[English](RESULTS.md) · [简体中文：initial release validation](RESULTS.zh-CN.md)

**Scope:** bilingual documentation, case localization and data-preserving search, built on the original 2026-11-09 source-linked case dataset. Original v1 test report is retained in Chinese without rewriting historical observations. These are **structural and behavior checks**, not an empirical study of acceptance rates.

## Run locally

~~~bash
python3 scripts/validate_repository.py
python3 -m unittest discover -s tests -v
~~~

Checks validate:

1. **70 distinct forum IDs**, 49/12/9 year counts, source URLs routed to the correct forum, original score-provenance preservation and correct selection-role counts (22 core, 16 extended, 19 qualified, 6 counterexamples, 2 exclusions, 5 contextual).
2. Presence of **English descriptions for each of 70 cases**, original Chinese fields, and paired English/Chinese documentation for core modules.
3. All local Markdown links, license/attribution files and absence of private scratch paths.
4. Bilingual query behavior: English is default, \`--lang zh-CN\` returns Chinese, Unicode normalization works, the anomaly is not erroneously selected as core, source-preserving \`--raw\` works, and invalid limits are rejected.
5. Historical source caveats remain visible in search output; localization does not turn stated intentions or AC predictions into verified saved scores.

## Earlier behavioral exercises

The original release included three independent simulated exercises: mixed reviewer critique (fact error, tuning mismatch, missing citation, significance and scope), AC summary (conditional/unconditional/no-response states), and academic language editing (numbers, negative findings, in-progress runs, formula and citations). The initial human-reviewed observations and outputs are retained in [the Chinese record](RESULTS.zh-CN.md), [scenario files](01_mixed_review.md) and [saved outputs](outputs/01_response.md).

**Limitations:** Passing validation cannot establish that an OpenReview note remains accessible, a paper's experiment is reproducible, or particular rhetoric caused a score increase. The 2026 score rollback, source disagreements and purposive sampling require continued independent judgment. The bilingual update does not rerun full agent behavioral evaluations on real submissions.
