#!/usr/bin/env python3
"""Check the bounded nine-claim VVEAA crosswalk and its exact evidence blobs.

This checks evidence integrity, not scientific adequacy, human validation or
publication approval. A new assessment requires an intentional profile update.
"""
import argparse
import copy
import csv
import hashlib
import json
import os
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MATRIX = ROOT / 'evaluation/vveaa/paper1-vveaa-claim-method-evidence-v0.1.csv'
EXPECTED = {
    'SR-CL01': 'NARROWED_PENDING_HUMAN',
    'SR-CL02': 'SUPPORTED_BOUNDED_NONINDEPENDENT',
    'SR-CL03': 'PARTIAL',
    'SR-CL04': 'SUPPORTED_TASK_BOUNDED',
    'SR-CL05': 'NARROWED_NONINDEPENDENT',
    'SR-CL06': 'BLOCKED_FOR_INDEPENDENT_TRANSFER',
    'SR-CL07': 'PROVISIONAL',
    'SR-CL08': 'SUPPORTED_FORMAL_BOUNDED',
    'SR-CL09': 'SUPPORTED_WITH_ACCESS_LIMITS',
}
FIELDS = ('claim_id', 'vveaa_functions', 'e_layers', 'dataset_role',
          'tool_version_ref', 'method_and_test',
          'unit_denominator', 'expected_criterion', 'observed_result',
          'current_assessment', 'primary_artifact_and_blob', 'evidence_role',
          'challenging_or_missing_evidence', 'claim_ceiling', 'next_recheck')


def git_blob(data):
    return hashlib.sha1(b'blob ' + str(len(data)).encode() + b'\0' + data).hexdigest()


def check(rows, root=ROOT):
    errors = []
    if [r.get('claim_id') for r in rows] != list(EXPECTED):
        errors.append('claim IDs/order must be exactly SR-CL01 through SR-CL09')
    for row in rows:
        cid = row.get('claim_id', '?')
        for field in FIELDS:
            if not row.get(field, '').strip():
                errors.append(f'{cid}: missing {field}')
        if row.get('current_assessment') != EXPECTED.get(cid):
            errors.append(f'{cid}: assessment changed; explicit evidence/review update required')
        if not set(row.get('vveaa_functions', '').split('|')) <= {
                'Verification', 'Validation', 'Evaluation', 'Assessment', 'Assurance'}:
            errors.append(f'{cid}: unknown VVEAA function')
        if not set(row.get('e_layers', '').split('|')) <= {f'E{i}' for i in range(1, 12)}:
            errors.append(f'{cid}: unknown E-layer')
        if cid == 'SR-CL06' and 'NOT_EXECUTED' not in row.get('dataset_role', ''):
            errors.append(f'{cid}: independent holdout cannot be reported as executed')
        if cid in ('SR-CL01', 'SR-CL08') and 'semantic CI 35850078877@8fa6e221d4e2e7cf36817e666bf374ba11a921b7' not in row.get('tool_version_ref', ''):
            errors.append(f'{cid}: missing exact prior semantic execution binding')
        ref = row.get('primary_artifact_and_blob', '')
        match = re.fullmatch(r'(.+)@([0-9a-f]{40})', ref)
        if not match:
            errors.append(f'{cid}: evidence must be path@Git-blob-SHA')
            continue
        path, expected_sha = match.groups()
        target = (root / path).resolve()
        if not target.is_relative_to(root.resolve()):
            errors.append(f'{cid}: evidence path escapes repository')
        elif not target.is_file():
            errors.append(f'{cid}: missing evidence file {path}')
        elif git_blob(target.read_bytes()) != expected_sha:
            errors.append(f'{cid}: evidence blob drift {path}')
    return errors


def selftest(rows):
    if check(rows):
        raise SystemExit('Self-test baseline invalid: ' + '; '.join(check(rows)))
    mutations = []
    r = copy.deepcopy(rows); r.pop(); mutations.append(('missing claim', r))
    r = copy.deepcopy(rows); r[1]['claim_id'] = r[0]['claim_id']; mutations.append(('duplicate ID', r))
    r = copy.deepcopy(rows); r[5]['current_assessment'] = 'PASS'; mutations.append(('invented transfer PASS', r))
    r = copy.deepcopy(rows); r[0]['challenging_or_missing_evidence'] = ''; mutations.append(('hidden adverse evidence', r))
    r = copy.deepcopy(rows); r[0]['e_layers'] = 'E99'; mutations.append(('invented E-layer', r))
    r = copy.deepcopy(rows); r[0]['vveaa_functions'] = 'Certification'; mutations.append(('invented certification', r))
    r = copy.deepcopy(rows); r[0]['primary_artifact_and_blob'] = r[0]['primary_artifact_and_blob'].split('@')[0] + '@' + '0' * 40; mutations.append(('wrong evidence hash', r))
    r = copy.deepcopy(rows); r[0]['primary_artifact_and_blob'] = 'missing-evidence.csv@' + '0' * 40; mutations.append(('missing evidence', r))
    r = copy.deepcopy(rows); r[0]['primary_artifact_and_blob'] = '../outside.csv@' + '0' * 40; mutations.append(('path escape', r))
    r = copy.deepcopy(rows); r[0]['tool_version_ref'] = ''; mutations.append(('missing tool and ref', r))
    r = copy.deepcopy(rows); r[5]['dataset_role'] = 'independent_holdout_executed'; mutations.append(('invented holdout', r))
    for label, altered in mutations:
        if not check(altered):
            raise SystemExit('Undetected negative control: ' + label)
    print(f'SEM_RISK_VVEAA_NEGATIVE_CONTROLS_PASS ({len(mutations)}/{len(mutations)})')


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--selftest', action='store_true')
    parser.add_argument('--report', type=Path)
    args = parser.parse_args()
    with MATRIX.open(encoding='utf-8', newline='') as stream:
        rows = list(csv.DictReader(stream))
    errors = check(rows)
    if errors:
        raise SystemExit('\n'.join('FAIL: ' + error for error in errors))
    if args.selftest:
        selftest(rows)
    if args.report:
        report = {
            'integrity_status': 'PASS_BOUNDED',
            'tested_ref': os.environ.get('GITHUB_SHA', 'LOCAL_UNBOUND'),
            'matrix_blob': git_blob(MATRIX.read_bytes()),
            'claims': [{k: row[k] for k in ('claim_id', 'current_assessment',
                        'dataset_role', 'tool_version_ref',
                        'primary_artifact_and_blob', 'claim_ceiling',
                        'challenging_or_missing_evidence')} for row in rows],
            'human_validation': 'PENDING_ISSUE_51',
            'publication_assurance': 'PENDING_ISSUES_53_54_55',
            'limitation': 'Integrity and declared-state checks only; no semantic-validity verdict.'}
        args.report.parent.mkdir(parents=True, exist_ok=True)
        args.report.write_text(json.dumps(report, indent=2) + '\n', encoding='utf-8')
    print('SEM_RISK_VVEAA_EVIDENCE_INTEGRITY_PASS (9/9 claim bindings)')


if __name__ == '__main__':
    main()
