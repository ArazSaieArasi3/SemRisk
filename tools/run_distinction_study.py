#!/usr/bin/env python3
"""Bounded query-sensitivity experiment. No formal or peer-superiority claim."""
import argparse
import hashlib
import json
import pathlib
import platform
import sys

import rdflib
from rdflib import Graph, Namespace, RDF

ROOT = pathlib.Path(__file__).resolve().parents[1]
STUDY = ROOT / 'evaluation/e10/controlled-distinction-study-v1'
SR = Namespace('urn:semrisk:entity:')
DCT = Namespace('http://purl.org/dc/terms/')


def evaluate(output):
    protocol_bytes = (STUDY / 'protocol.json').read_bytes()
    protocol = json.loads(protocol_bytes)
    fixture = ROOT / protocol['fixture']
    actual_hash = hashlib.sha256(fixture.read_bytes()).hexdigest()
    if actual_hash != protocol['fixture_sha256']:
        raise ValueError('Fixture drift: review the protocol and expected answers before rerunning.')
    full = Graph().parse(fixture, format='turtle')
    removals = {
        'without_state_links': {t for t in full if t[1] in (SR['SR-REL-030'], SR['SR-REL-031'])},
        'without_history_links': {t for t in full if t[1] in (SR['SR-REL-033'], SR['SR-REL-034'])},
        'without_evidence_qualification': {
            t for t in full if t[1] == DCT.type and (t[0], RDF.type, RDF.Statement) in full
        },
    }
    if not all(removals.values()):
        raise ValueError('A declared ablation removes no information.')
    restored = set(full)
    for removed in removals.values():
        restored -= removed
    for removed in removals.values():
        restored |= removed
    if restored != set(full):
        raise AssertionError('Restoration failed.')
    outcomes = []
    for variant, affected in protocol['variants'].items():
        graph = Graph()
        selected = restored if variant == 'restored' else set(full) - removals.get(variant, set())
        for triple in selected:
            graph.add(triple)
        for task in protocol['tasks']:
            actual = sorted({tuple(str(term) for term in row) for row in graph.query(task['query'])})
            actual = [list(row) for row in actual]
            preserved = actual == task['expected']
            expected_preservation = task['id'] not in affected
            outcomes.append({
                'variant': variant, 'task': task['id'], 'actual_answers': actual,
                'expected_complete_answers': task['expected'],
                'answer_preserved': preserved, 'expected_preservation': expected_preservation,
                'diagnostic_expectation_met': preserved == expected_preservation,
            })
    result = {
        'study_version': protocol['version'], 'baseline_commit': protocol['baseline_commit'],
        'fixture_sha256': actual_hash,
        'protocol_sha256': hashlib.sha256(protocol_bytes).hexdigest(),
        'runner_sha256': hashlib.sha256(pathlib.Path(__file__).read_bytes()).hexdigest(),
        'python': platform.python_version(), 'rdflib': rdflib.__version__,
        'fixture_triples': len(full),
        'removed_triples': {name: len(value) for name, value in removals.items()},
        'diagnostic_expectations_met': sum(x['diagnostic_expectation_met'] for x in outcomes),
        'diagnostic_expectations_total': len(outcomes),
        'outcomes': outcomes,
        'claim_boundary': 'Single synthetic fixture, query sensitivity only. No peer benchmark, OWL necessity, causal effect or expert validation.',
    }
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(json.dumps(result, indent=2) + '\n')
    print(json.dumps({k: result[k] for k in ('fixture_triples', 'removed_triples', 'diagnostic_expectations_met', 'diagnostic_expectations_total')}))
    return all(x['diagnostic_expectation_met'] for x in outcomes)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--output', type=pathlib.Path, default=STUDY / 'results.json')
    args = parser.parse_args()
    sys.exit(0 if evaluate(args.output) else 1)
