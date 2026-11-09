#!/usr/bin/env python3
"""Check case integrity, source routing, and bundled reference links offline.

This validates structure and consistency, not scientific truth or causality.
"""

from collections import Counter
import json
from pathlib import Path
import re
import sys
from urllib.parse import parse_qs, urlparse

ROOT = Path(__file__).resolve().parents[1]
SKILL = ROOT / 'skills' / 'iclr-rebuttal'
sys.path.insert(0, str(SKILL / 'scripts'))
from search_cases import MECHANISMS, ROLES  # noqa: E402


def validate():
    errors = []
    try:
        data = json.loads((SKILL / 'references/cases.json').read_text(encoding='utf-8'))
        cases = data['cases']
    except (OSError, ValueError, KeyError) as exc:
        return [f'Catalogue is unavailable or malformed: {exc}'], {}
    ids = [case['forum_id'] for case in cases]
    if len(ids) != len(set(ids)):
        errors.append('Duplicate OpenReview forum IDs')
    case_ids = [case['case_id'] for case in cases]
    if len(case_ids) != len(set(case_ids)):
        errors.append('Duplicate local case IDs')
    if data['metadata']['summary']['total'] != len(cases):
        errors.append('Metadata total disagrees with catalogue')
    years = {str(k): v for k, v in Counter(c['year'] for c in cases).items()}
    if years != data['metadata']['summary']['by_year']:
        errors.append('Year counts disagree with metadata')
    accepted = sum(c['accepted'] for c in cases)
    if accepted != data['metadata']['summary']['accepted']:
        errors.append('Accepted count disagrees with metadata')
    if len(cases) - accepted != data['metadata']['summary']['rejected']:
        errors.append('Rejected count disagrees with metadata')
    roles = Counter()
    for case in cases:
        cid = case['case_id']
        sel = case.get('selection', {})
        if sel.get('role') not in ROLES:
            errors.append(f'{cid}: unknown selection role')
        roles[sel.get('role')] += 1
        for key in ['reason', 'reusable_mechanism', 'caution']:
            if not sel.get(key):
                errors.append(f'{cid}: empty selection {key}')
        tags = sel.get('mechanisms', [])
        if not tags or not set(tags).issubset(MECHANISMS):
            errors.append(f'{cid}: missing or unknown mechanisms')
        if sel.get('role') == 'core_positive':
            if not case['accepted'] or case.get('excluded_from_clean_numeric_examples'):
                errors.append(f'{cid}: rejected/flagged evidence cannot be core positive')
            anchor = sel.get('core_numeric_anchor', {})
            if not all(anchor.get(key) for key in ['kind', 'reviewer', 'stated_target', 'url', 'basis']):
                errors.append(f'{cid}: missing reviewer numeric anchor')
        urls = [case['url'], case['evidence_url']] + case['key_note_urls'] + case['author_note_urls']
        urls += [case[k] for k in ['ac_url', 'decision_url'] if case.get(k)]
        urls += [sel['core_numeric_anchor']['url']] if sel.get('core_numeric_anchor', {}).get('url') else []
        for url in urls:
            parsed = urlparse(url)
            if parsed.scheme != 'https' or parsed.netloc != 'openreview.net':
                errors.append(f'{cid}: unexpected discussion URL {url}')
            if parse_qs(parsed.query).get('id') != [case['forum_id']]:
                errors.append(f'{cid}: source points to another forum')
        quotations = [case.get('quote', '')] + [e.get('quote', '') for e in case.get('events', [])]
        if sum(len(q.replace(' / ', ' ').split()) for q in quotations) > 25:
            errors.append(f'{cid}: more than 25 quoted English words')
        if not case.get('numeric_source') or not case.get('reading_scope'):
            errors.append(f'{cid}: missing provenance caveat')
    expected_roles = data['metadata']['selection_summary']
    if dict(roles) != expected_roles:
        errors.append('Selection role counts disagree with metadata')
    for path in ROOT.rglob('*.md'):
        if '.git' in path.parts:
            continue
        content = path.read_text(encoding='utf-8')
        if '/workspace/scratch/' in content or '/root/.codex/' in content:
            errors.append(f'{path.relative_to(ROOT)}: private workspace path')
        for target in re.findall(r'\]\(([^)]+)\)', content):
            target = target.split('#', 1)[0].split(' ', 1)[0]
            if not target or re.match(r'^[a-zA-Z][a-zA-Z0-9+.-]*:', target):
                continue
            if not (path.parent / target).exists():
                errors.append(f'{path.relative_to(ROOT)}: broken local link {target}')
    for path in [ROOT / 'LICENSE', ROOT / 'THIRD_PARTY_NOTICES.md', SKILL / 'references/humanizer-LICENSE.txt']:
        if not path.is_file():
            errors.append(f'Missing licence/notice: {path.relative_to(ROOT)}')
    return errors, {'cases': len(cases), 'by_year': years, 'selection_roles': dict(roles)}


if __name__ == '__main__':
    problems, stats = validate()
    print(json.dumps({'ok': not problems, 'stats': stats, 'errors': problems}, ensure_ascii=False, indent=2))
    raise SystemExit(bool(problems))
