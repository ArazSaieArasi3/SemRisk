#!/usr/bin/env python3
"""Check disposition/reference integrity, not semantic adequacy or source import."""
import argparse
import csv
import json
from collections import Counter
from pathlib import Path
from rdflib import Graph, Namespace, RDF, OWL, SKOS

ROOT = Path(__file__).resolve().parents[1]
def read(path): return list(csv.DictReader((ROOT / path).open(encoding='utf-8-sig')))
def main():
    graph = Graph()
    for path in json.loads((ROOT / 'evaluation/core-contract/2026-10-05/protocol.json').read_text())['source_hashes']:
        graph.parse(ROOT / path)
    sr = Namespace('urn:semrisk:entity:')
    concepts = read('conceptualization/revision-2026-10-05/concept-dispositions.csv')
    registry = read('conceptualization/core/core-concept-registry-v0.1.csv')
    assert len(concepts) == 47
    assert {x['semantic_id'] for x in concepts} == {x['semantic_id'] for x in registry}
    for x in concepts:
        term = sr[x['semantic_id']]
        actual = 'OWL_CLASS' if (term, RDF.type, OWL.Class) in graph else 'SKOS_MARKER' if (term, RDF.type, SKOS.Concept) in graph else 'NOT_LOCALLY_DECLARED'
        assert x['formal_status'] == actual, x['semantic_id']
        assert x['definition'] and x['rationale'] and x['next_owner']
    declarations = dict(Counter(x['formal_status'] for x in concepts))
    assert declarations == {'OWL_CLASS': 35, 'SKOS_MARKER': 4, 'NOT_LOCALLY_DECLARED': 8}

    legacy = read('foundational/legacy-pr-58-61-semantic-disposition-2026-10-05.csv')
    assert len(legacy) == len({(x['legacy_file'], x['semantic_id']) for x in legacy}) == 71
    assert sorted(Counter(x['legacy_file'] for x in legacy).values()) == [32, 39]
    for x in legacy:
        path, identifier = x['current_locator'].split('#')
        assert any(identifier in row.values() for row in read(path)), x['semantic_id']
        assert x['decision'] and x['rationale'] and x['remaining_owner']

    fields = read('evaluation/integrity/derived-field-use-audit-2026-10-05.csv')
    source = read('conceptualization/source-mining/SRC-OP-001-jira-risk-attributes-concepts.csv')
    assert len(fields) == 27 and {x['source_field_id'] for x in fields} == {x['source_concept_id'] for x in source}
    catalog = read('relational/design/schema-table-field-catalog-v0.1.csv')
    columns = {'.'.join(x[k] for k in ['schema','table','column']) for x in catalog}
    for x in fields:
        assert not x['implemented_column'] or x['implemented_column'] in columns, x['source_field_id']
     assert x['reason_and_limit'] and x['private_record_load'] == 'NOT_EXECUTED_IN_THIS_AUDIT'
    uses = dict(Counter(x['disposition'] for x in fields))
    assert uses == {'IMPLEMENTED_PROJECTION': 6, 'PARTIAL': 13, 'DESIGN_ONLY': 7, 'DEFERRED_PROFILE': 1}

    req = read('conceptualization/requirements/semantic-requirements-registry.csv')
    cqs = read('conceptualization/requirements/conceptual-cq-registry.csv')
    traces = read('conceptualization/requirements/requirement-cq-traceability.csv')
    req_ids = {x['requirement_id'] for x in req}; cq_ids = {x['cq_id'] for x in cqs}
    assert len(req_ids) == len(req) == 20 and len(cq_ids) == len(cqs) == 40
    assert len(traces) == len({x['trace_id'] for x in traces}) == 66
    assert {x['requirement_id'] for x in traces} == req_ids
    assert {x['cq_id'] for x in traces} == cq_ids
    method = read('method/sabio-executed-process-crosswalk-v1.1.csv')
    assert {x['id'] for x in method} == {f'{k}{i}' for k in ['D','S'] for i in range(1,6)}
    for x in method:
        for path in x['artifact_paths'].split(';'): assert (ROOT/path).is_file(), path
        assert x['primary_locator'] and x['completion_boundary']
    domains = read('conceptualization/revision-2026-10-05/domain-membership.csv')
    assert len(domains) == 13 and sum(x['kind'] == 'portfolio_scope' for x in domains) == 12
    assert all('&' not in x['scope'] for x in domains)
    result = {'result':'PASS_REFERENCE_INTEGRITY_ONLY','concepts':47,'declarations':declarations,
              'legacy_dispositions':71,'derived_fields':27,'field_dispositions':uses,
              'semantic_requirements':20,'conceptual_cqs':40,'trace_links':66,
              'method_crosswalk_rows':10,'domain_rows':13,'portfolio_scopes':12,
              'all_trace_endpoints_exist':True,'semantic_adequacy_proven':False,
              'private_source_record_import_verified':False}
    return result
if __name__ == '__main__':
    p=argparse.ArgumentParser();p.add_argument('--write',action='store_true');a=p.parse_args()
    result=main()
    if a.write: (ROOT/'evaluation/core-contract/2026-10-05/traceability-results.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(result,indent=2))
