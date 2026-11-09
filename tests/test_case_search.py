import importlib.util
import json
from pathlib import Path
import subprocess
import sys
import unittest

ROOT = Path(__file__).resolve().parents[1]
SKILL = ROOT / 'skills/iclr-rebuttal'
SCRIPT = SKILL / 'scripts/search_cases.py'
spec = importlib.util.spec_from_file_location('case_search', SCRIPT)
search = importlib.util.module_from_spec(spec)
spec.loader.exec_module(search)
CASES = json.loads((SKILL / 'references/cases.json').read_text(encoding='utf-8'))['cases']


class CaseSearchTests(unittest.TestCase):
    def test_fairness_filter_keeps_only_qualified_core_cases(self):
        rows = search.select_cases(CASES, year=2026, role='core_positive', mechanism='baseline_fairness')
        self.assertTrue(rows)
        self.assertTrue(all(r['year'] == 2026 and r['accepted'] for r in rows))
        self.assertTrue(all(r['selection']['role'] == 'core_positive' for r in rows))
        self.assertTrue(all('baseline_fairness' in r['selection']['mechanisms'] for r in rows))

    def test_unicode_query_and_case_identity(self):
        self.assertEqual([r['forum_id'] for r in search.select_cases(CASES, 'ＦＡＳＡ')], ['FnSgecCEwg'])
        self.assertEqual(search.select_cases(CASES, 'SCUBA', year=2024), [])

    def test_anomalous_large_jump_is_not_returned_as_core(self):
        self.assertEqual(search.select_cases(CASES, '029hDSVoXK', role='core_positive'), [])
        rows = search.select_cases(CASES, '029hDSVoXK', role='evidence_exclusion')
        self.assertEqual(len(rows), 1)

    def test_cli_is_portable_from_another_working_directory(self):
        result = subprocess.run([sys.executable, str(SCRIPT), '--query', 'bkjKnO9s7T', '--format', 'json'],
                                cwd=ROOT, capture_output=True, text=True, check=True)
        data = json.loads(result.stdout)
        self.assertEqual(data['total_matches'], 1)
        self.assertEqual(data['cases'][0]['forum_id'], 'bkjKnO9s7T')

    def test_cli_rejects_invalid_limit(self):
        result = subprocess.run([sys.executable, str(SCRIPT), '--limit', '0'],
                                cwd=ROOT, capture_output=True, text=True)
        self.assertEqual(result.returncode, 2)


if __name__ == '__main__':
    unittest.main()
