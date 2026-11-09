#!/usr/bin/env python3
"""Search 70 source-linked rebuttal cases in English (default) or 简体中文."""

import argparse
import json
from pathlib import Path
import sys
import unicodedata

DATA_PATH = Path(__file__).resolve().parents[1] / 'references' / 'cases.json'
ROLES = (
    'core_positive', 'extended_positive', 'qualified_positive',
    'outcome_counterexample', 'evidence_exclusion', 'context_only',
)
MECHANISMS = (
    'baseline_fairness', 'theory_repair', 'novelty', 'claim_scope',
    'multi_round', 'benchmark_value', 'evaluation', 'efficiency',
    'paper_revision', 'related_work', 'negative_results', 'ac_summary',
)
LANGS = ('en', 'zh-CN')


def normalize(value):
    return unicodedata.normalize('NFKC', str(value)).casefold()


def select_cases(cases, query='', year=None, role=None, mechanism=None):
    """Search source fields and both localizations without changing case identity."""
    terms = normalize(query).split()
    selected = []
    for case in cases:
        selection = case['selection']
        if year is not None and case['year'] != year:
            continue
        if role is not None and selection['role'] != role:
            continue
        if mechanism is not None and mechanism not in selection['mechanisms']:
            continue
        searchable = normalize(json.dumps({
            key: case.get(key, '') for key in (
                'case_id', 'forum_id', 'title', 'short_title', 'trajectory',
                'evidence', 'blocker', 'actions', 'feedback', 'lesson',
                'limitations', 'selection', 'i18n',
            )
        }, ensure_ascii=False))
        if all(term in searchable for term in terms):
            selected.append(case)
    return selected


def bounded_limit(value):
    try:
        parsed = int(value)
    except ValueError as exc:
        raise argparse.ArgumentTypeError('limit must be an integer from 1 to 100') from exc
    if not 1 <= parsed <= 100:
        raise argparse.ArgumentTypeError('limit must be between 1 and 100')
    return parsed


def localized_case(case, lang):
    """Expose a language-appropriate view; retain original IDs and provenance."""
    selected = case['selection']
    base = {
        'case_id': case['case_id'],
        'forum_id': case['forum_id'],
        'year': case['year'],
        'title': case['title'],
        'decision': case['decision'],
        'role': selected['role'],
        'mechanisms': selected['mechanisms'],
        'url': case['url'],
        'evidence_url': case['evidence_url'],
        'key_note_urls': case['key_note_urls'],
        'events': case['events'],
        'historical_trajectory_source_text': case['trajectory'],
    }
    if lang == 'en':
        base.update(case['i18n']['en'])
        base['source_provenance'] = (
            'For source language, exact score wording and attribution see '
            'the linked notes and raw cases.json record.'
        )
    else:
        base.update({
            'concern': case['blocker'],
            'author_response_and_feedback': case['actions'] + '\n' + case['feedback'],
            'reusable_lesson': case['lesson'],
            'selection_reason': selected['reason'],
            'caution': selected['caution'],
            'source_provenance': case['numeric_source'],
        })
    return base


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--query', default='', help='Search terms (English or Chinese); all terms must match')
    parser.add_argument('--year', type=int)
    parser.add_argument('--role', choices=ROLES)
    parser.add_argument('--mechanism', choices=MECHANISMS)
    parser.add_argument('--lang', choices=LANGS, default='en',
                        help='Display language; English is the default')
    parser.add_argument('--limit', type=bounded_limit, default=5)
    parser.add_argument('--format', choices=('text', 'json'), default='text')
    parser.add_argument('--raw', action='store_true',
                        help='In JSON mode output complete original bilingual case records')
    args = parser.parse_args(argv)

    try:
        data = json.loads(DATA_PATH.read_text(encoding='utf-8'))
        matches = select_cases(data['cases'], args.query, args.year, args.role, args.mechanism)
    except (OSError, ValueError, KeyError) as exc:
        print(f'Cannot read case catalogue: {exc}', file=sys.stderr)
        return 1
    visible = matches[:args.limit]
    caveat = data['metadata']['score_caveat_en' if args.lang == 'en' else 'score_caveat']

    if args.format == 'json':
        print(json.dumps({
            'language': args.lang,
            'as_of': data['metadata']['as_of'],
            'total_matches': len(matches),
            'shown': len(visible),
            'score_caveat': caveat,
            'cases': visible if args.raw else [localized_case(c, args.lang) for c in visible],
        }, ensure_ascii=False, indent=2))
    else:
        if args.lang == 'en':
            print(f'{len(matches)} matches; showing {len(visible)}. Historical scores require attribution.')
        else:
            print(f'匹配 {len(matches)} 条，显示 {len(visible)} 条；历史评分须区分来源。')
        print(caveat)
        for case in visible:
            view = localized_case(case, args.lang)
            print(f"\n{view['case_id']} | ICLR {view['year']} | {view['title']}")
            if args.lang == 'en':
                print(f"  Role: {view['role']} | Decision: {view['decision']}")
                print(f"  Scientific concern: {view['concern']}")
                print(f"  Author action / feedback: {view['author_response_and_feedback']}")
                print(f"  Selection reason: {view['selection_reason']}")
                print(f"  Caution: {view['caution']}")
                print(f"  Original score-path text (source language): {view['historical_trajectory_source_text']}")
                print(f"  Thread: {view['url']}")
                print(f"  Evidence note: {view['evidence_url']}")
            else:
                print(f"  角色：{view['role']} | 决定：{view['decision']}")
                print(f"  争点：{view['concern']}")
                print(f"  作者动作与反馈：{view['author_response_and_feedback']}")
                print(f"  选例理由：{view['selection_reason']}")
                print(f"  注意事项：{view['caution']}")
                print(f"  原始评分路径：{view['historical_trajectory_source_text']}")
                print(f"  讨论：{view['url']}")
                print(f"  关键来源：{view['evidence_url']}")
            anchor = case['selection'].get('core_numeric_anchor')
            if anchor:
                print(f"  {'Reviewer numeric statement' if args.lang == 'en' else '评审本人数字表态'}: "
                      f"{anchor['reviewer']} → {anchor['stated_target']}; {anchor['url']}")
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
