#!/usr/bin/env python3
"""Search the bundled, source-linked case catalogue; standard library only."""

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


def normalize(value):
    return unicodedata.normalize('NFKC', str(value)).casefold()


def select_cases(cases, query='', year=None, role=None, mechanism=None):
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
                'limitations', 'selection',
            )
        }, ensure_ascii=False))
        if all(term in searchable for term in terms):
            selected.append(case)
    return selected


def bounded_limit(value):
    parsed = int(value)
    if not 1 <= parsed <= 100:
        raise argparse.ArgumentTypeError('limit must be between 1 and 100')
    return parsed


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--query', default='', help='Case-insensitive terms; all must match')
    parser.add_argument('--year', type=int)
    parser.add_argument('--role', choices=ROLES)
    parser.add_argument('--mechanism', choices=MECHANISMS)
    parser.add_argument('--limit', type=bounded_limit, default=5)
    parser.add_argument('--format', choices=('text', 'json'), default='text')
    args = parser.parse_args(argv)
    try:
        data = json.loads(DATA_PATH.read_text(encoding='utf-8'))
        matches = select_cases(data['cases'], args.query, args.year, args.role, args.mechanism)
    except (OSError, ValueError, KeyError) as exc:
        print(f'Cannot read bundled case catalogue: {exc}', file=sys.stderr)
        return 1
    visible = matches[:args.limit]
    if args.format == 'json':
        print(json.dumps({
            'as_of': data['metadata']['as_of'],
            'total_matches': len(matches), 'shown': len(visible),
            'score_caveat': data['metadata']['score_caveat'], 'cases': visible,
        }, ensure_ascii=False, indent=2))
    else:
        print(f'{len(matches)} matches; showing {len(visible)}. Dates and scores retain their source caveats.')
        print(data['metadata']['score_caveat'])
        for case in visible:
            selection = case['selection']
            print(f"\n{case['case_id']} | ICLR {case['year']} | {case['title']}")
            print(f"  Role: {selection['role']} | Decision: {case['decision']}")
            print(f"  Path / statement: {case['trajectory']}")
            print(f"  Evidence: {case['evidence']}")
            print(f"  Why selected: {selection['reason']}")
            print(f"  Mechanism: {selection['reusable_mechanism']}")
            print(f"  Caution: {selection['caution']}")
            print(f"  Thread: {case['url']}")
            anchor = selection.get('core_numeric_anchor')
            if anchor:
                print(f"  Core numerical statement (not current rating): {anchor['reviewer']} states {anchor['stated_target']}")
                print(f"  Core statement note: {anchor['url']}")
            for url in dict.fromkeys([case['evidence_url']] + case['key_note_urls']):
                print(f'  Evidence note: {url}')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
