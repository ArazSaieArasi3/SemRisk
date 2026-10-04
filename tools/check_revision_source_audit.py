#!/usr/bin/env python3
"""Check declared source inventory and expert subcheck coverage without inflating evidence."""
import csv
import json
import pathlib

ROOT = pathlib.Path(__file__).resolve().parents[1]
AUDIT = ROOT / 'evaluation/standards/nist-schema-audit-2026-10-04'


def read_csv(path):
    with path.open(newline='') as f:
        return list(csv.DictReader(f))


def main():
    rows = read_csv(AUDIT / 'field-dispositions.csv')
    keys = [(r['schema'], r['field']) for r in rows]
    assert len(keys) == len(set(keys)), 'Duplicate field dispositions'
    summary = {}
    for name in ['RR', 'RDR']:
        schema = json.loads((AUDIT / f'{name}-normalized-retrieval.json').read_text())
        fields = set(schema['properties']) | set(schema['required'])
        selected = [r for r in rows if r['schema'] == name]
        assert {r['field'] for r in selected} == fields, 'Source field inventory mismatch'
        for row in selected:
            field = row['field']
            assert row['required'] == str(field in schema['required'])
            assert row['defined_in_properties'] == str(field in schema['properties'])
            assert row['source_type'] == schema['properties'].get(field, {}).get('type', 'UNDEFINED')
            assert row['locator'].endswith('/' + field) or row['locator'].endswith('#/required')
            assert row['target_candidate'] and row['mapping_kind'] and row['decision_boundary']
        summary[name] = {'defined_properties': len(schema['properties']), 'required_names': len(schema['required']),
                         'required_without_definition': sorted(set(schema['required']) - set(schema['properties']))}
    assert summary['RDR']['required_without_definition'] == ['currentRiskAnalysis']
    expert = ROOT / 'evaluation/expert'
    cross = read_csv(expert / 'expert-review-v1-to-v1.1-crosswalk.csv')
    instrument = read_csv(expert / 'expert-review-instrument-v1.1-light.csv')
    legacy = read_csv(expert / 'expert-review-instrument-v1.0.csv')
    assert len(cross) == len(legacy) == 20
    assert {r['legacy_item'] for r in cross} == {r['item_id'] for r in legacy}
    assert len(instrument) == 12 and len({r['item_id'] for r in instrument}) == 12
    assert {r['light_item'] for r in cross} == {r['item_id'] for r in instrument}
    for item in instrument:
        assert set(item['legacy_subchecks'].split(';')) == {r['legacy_item'] for r in cross if r['light_item'] == item['item_id']}
    assert read_csv(expert / 'expert-responses-v1.1-template.csv') == [], 'Templates cannot contain fabricated responses'
    assert read_csv(ROOT / 'case/pharma/literature-risk-statements-template.csv') == [], 'Template is not an extracted dataset'
    comparison = read_csv(ROOT / 'conceptualization/comparison/paper1-claim-critical-comparison-2026-10-04.csv')
    assert len(comparison) == 80 and len({r['comparator'] for r in comparison}) == 10
    for row in comparison:
        assert row['primary_evidence_locator'] and row['version'] and row['observation']
    print(json.dumps({'source_schema_inventory': summary, 'field_dispositions': len(rows), 'comparison_cells': len(comparison),
                      'legacy_expert_subchecks_retained': len(cross), 'light_expert_criteria': len(instrument),
                      'actual_expert_responses': 0, 'actual_extracted_dataset_records': 0, 'result': 'PASS'}))


if __name__ == '__main__':
    main()
