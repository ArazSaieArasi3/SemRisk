#!/usr/bin/env python3
"""Check bounded documentary joins and frozen test citations; does not rerun scientific tests."""
import argparse,copy,csv,hashlib,json
from collections import Counter
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
ANNEX=ROOT/'docs/execution/2026-10-04/objective-domain-crosswalk-2026-10-06.json'
RESULT=ROOT/'docs/execution/2026-10-04/objective-domain-crosswalk-results.json'
BASELINE='d3bdb437844880d7c3686959b2d3dc59dbec5f1a'
REQUIRED_SOURCES={'foundational/semantic-identity-v0.2.0-rc.3/decisions.md', 'docs/formal/0.2.0-rc.4/entity-inventory.csv', 'evaluation/cq/issue52-cq-results-v1.0.csv', 'docs/formal/formal-ontology-description-rc4.md', 'site/ontology/0.2.0-rc.4/docs-20261006/catalog.html', 'evaluation/exposure-scale/v0.2.0-rc.4/results.json', 'case/pharma/literature-pilot-v0.1.0/validation-results.json', 'case/pharma/literature-pilot-v0.1.0/README.md', 'evaluation/semantic-identity/v0.2.0-rc.3/ci-evidence.json', 'architecture/g2/concept-relation-ownership-matrix-v0.1.csv', 'shapes/assessment-context-v0.2.0-rc.1.ttl', 'conceptualization/revision-2026-10-05/domain-membership.csv', 'evaluation/temporal/v0.2.0-rc.1/ci-evidence.json', 'evaluation/semantic-identity/v0.2.0-rc.3/results.json', 'ontology/p1-r2-candidate-manifest.yaml', 'conceptualization/core/core-concept-registry-v0.1.csv', 'rules/enterprise/workflow-at-v0.2.0-rc.3.rq', 'rules/enterprise/risk-owners-at-v0.2.0-rc.1.rq', 'evaluation/exposure-scale/v0.2.0-rc.4/ci-evidence.json', 'formalization/qualified-context-contract-v0.2.0-rc.1.md', 'shapes/exposure-scale-v0.2.0-rc.4.ttl', 'architecture/g2/module-profile-registry-v0.1.csv', 'shapes/semantic-identity-v0.2.0-rc.3.ttl', 'ontology/releases/0.2.0-rc.4/manifest.json', 'docs/research/domain-profile-roadmap.md', 'docs/formal/0.2.0-rc.4/source-manifest.json', 'evaluation/temporal/v0.2.0-rc.1/semantic-results.json', 'docs/execution/2026-10-04/scientific-contract.md', 'foundational/exposure-scale-v0.2.0-rc.4/decisions.md', 'case/pharma/literature-pilot-v0.1.0/ci-evidence.json'}
REQUIRED_TESTS={'EA-OWNERSHIP': {'OWNER-4', 'OWNER-6', 'N16', 'OWNER-UNBOUND', 'OWNER-3', 'OWNER-1', 'OWNER-2', 'OWNER-5'}, 'EA-WORKFLOW': {'W08', 'W03', 'W05', 'W07', 'W04', 'HALF-OPEN-BOUNDARY', 'W06', 'SNAPSHOT-NOT-HISTORY', 'HALF-OPEN-BEFORE'}, 'EA-REASSESSMENT': {'N08', 'N10', 'N12', 'N09', 'N07', 'SHACL-POS', 'N11'}, 'CORE-EXPOSURE-SCALE': {'S02', 'SCALE-IDENTITY', 'E03', 'E02', 'E01', 'EXPOSURE-ENDPOINTS', 'INTERVAL-ZONE', 'S01', 'INTERVAL-BOUNDARY', 'UNBOUND-TIME', 'INTERVAL-BEFORE', 'UNKNOWN-START'}, 'PHARMA-PROVENANCE': {'RDF-EQUALITY', 'SOURCE-COUNT-CQ', 'MAPPING-COUNT-CQ', 'N01-MISSING-LOCATOR', 'N04-FALSE-OBSERVATION', 'N05-FALSE-HOLDOUT', 'N08-ROLE-DRIFT', 'SHACL-ARTIFACT-IDENTITY', 'N09-FALSE-REVIEW'}}
def load(p):return json.loads((ROOT/p).read_text())
def rows(p):return list(csv.DictReader((ROOT/p).open()))
def require(value,message):
 if not value:raise ValueError(message)
def sources(a):
 for p,h in a['source_sha256'].items():require((ROOT/p).is_file() and hashlib.sha256((ROOT/p).read_bytes()).hexdigest()==h,'SOURCE_DRIFT: '+p)
def validate(a,data):
 require(a['baseline_commit']==BASELINE,'BASELINE_IDENTITY')
 require(set(a['source_sha256'])==REQUIRED_SOURCES,'SOURCE_COVERAGE')
 require(a['objective_source']['path']=='docs/execution/2026-10-04/scientific-contract.md' and a['objective_source']['anchors']==['Position and intended outcome','Questions, proposed contributions and acceptance evidence'],'OBJECTIVE_SOURCE')
 require(a['requirements']==['1.4','2.7','4.5'],'REQUIREMENT_SCOPE')
 require(len(a['rows'])==5 and {r['id'] for r in a['rows']}=={'EA-OWNERSHIP','EA-WORKFLOW','EA-REASSESSMENT','CORE-EXPOSURE-SCALE','PHARMA-PROVENANCE'},'ROW_COVERAGE')
 for r in a['rows']:
  require(r['use_case'] and r['delivered_properties'] and r['test_scope'] and r['permitted_ceiling'],'MISSING_CEILING')
  require(r['requirements'] and set(r['requirements'])<= {'1.4','2.7'},'ROW_SCOPE')
  tests={t['id']:t for t in data[r['result_path']]['tests']}
  require(set(r['test_ids'])==REQUIRED_TESTS[r['id']] and len(r['test_ids'])==len(REQUIRED_TESTS[r['id']]),'TEST_COVERAGE')
  require(r['negative_test_ids'] and set(r['negative_test_ids'])<=set(r['test_ids']),'NEGATIVE_EVIDENCE_MISSING')
  require(r['test_ids'] and all(t in tests and tests[t]['passed'] is True for t in r['test_ids']),'TEST_CITATION')
  require(r['tested_commit']==data[r['receipt_path']][r['commit_field']],'TESTED_VERSION')
  require(all(p in a['source_sha256'] for p in [r['result_path'],r['receipt_path'],*r['artifact_paths']]),'UNBOUND_EVIDENCE')
 gaps=a['explicit_gaps'];require(set(gaps)=={'CQ-013','CQ-017','objective_capability_process_implementation','enterprise_impact_propagation_demonstrated','organizational_resilience_demonstrated','independent_validation_demonstrated','full_rc4_sql_parity_demonstrated'},'GAP_COVERAGE');cq={r['cq_id']:r for r in data['cq']}
 require(gaps['CQ-013']==cq['CQ-013']['state']=='partially_executable','EA_GAP_013')
 require(gaps['CQ-017']==cq['CQ-017']['state']=='conceptual_only','EA_GAP_017')
 require(all(v is False for k,v in gaps.items() if not k.startswith('CQ-')),'UNSUPPORTED_CAPABILITY')
 concepts=data['concepts'];ids={r['semantic_id'] for r in concepts}
 require(all(r['definition'].strip() and r['preferred_term'].strip() for r in concepts),'CONCEPT_DEFINITIONS')
 require(a['domain_module_acceptance']['governed_concepts']==47,'GOVERNED_CONCEPT_COUNT')
 require(len(concepts)==47 and ids=={f'SR-CPT-{i:03}' for i in range(1,48)},'CONCEPT_IDS')
 owners=[r for r in data['owners'] if r['item_type']=='concept']
 require(len(owners)==47 and {r['semantic_id'] for r in owners}==ids,'OWNER_COVERAGE')
 require(all(r['semantic_owner'] and r['ownership_status'] and r['architecture_module'] for r in owners),'OWNER_FIELDS')
 external={r['semantic_id'] for r in owners if r['semantic_owner']=='External'}
 require(external=={'SR-CPT-037','SR-CPT-038','SR-CPT-039','SR-CPT-040'},'EXTERNAL_OWNERSHIP')
 d=a['domain_module_acceptance'];require(dict(Counter(r['semantic_owner'] for r in owners))==d['ownership_distribution'],'OWNER_COUNTS')
 require(len(data['modules'])==d['architecture_responsibilities']==10 and len({r['module_id'] for r in data['modules']})==10,'ARCHITECTURE_COUNT')
 require(all(r['responsibility'] and r['semantic_owner'] and r['paper1_status'] for r in data['modules']),'ARCHITECTURE_FIELDS')
 require(len(data['membership'])==d['membership_rows']==13 and len({r['scope'] for r in data['membership']})==13,'MEMBERSHIP_IDS')
 portfolio={line.strip('|').split('|')[1].strip().replace('**','') for line in data['roadmap'].splitlines() if line.startswith('| `P')}
 require({r['scope'] for r in data['membership']}==portfolio|{'Method'},'MEMBERSHIP_SCOPES')
 for row in data['membership']:
  expected=[r['preferred_term'] for r in concepts if row['scope'] in r['module_profile'].split('/')]
  require(int(row['conceptual_member_count'])==len(expected) and row['concept_names']==('; '.join(expected) if expected else 'No assignments in current registry'),'MEMBERSHIP_JOIN')
 require(sum(line.startswith('| `P') for line in data['roadmap'].splitlines())==d['planned_scopes']==12,'PLANNED_SCOPES')
 manifest=data['manifest'];require(manifest['module_count']==d['current_modules']==7 and d['historical_modules']==sum(line.startswith('  - id: ONT-') for line in data['historical_manifest'].splitlines())==6,'VERSION_MODULES')
 kinds=Counter(r['kind'] for r in data['inventory'] if r['iri'].rsplit(':',1)[-1] in ids)
 require(kinds=={'class':35,'marker':4} and d['domain_classes']==35 and d['markers']==4 and d['undeclared_conceptual_slots']==47-sum(kinds.values())==8,'DECLARATION_COUNTS')
 require(manifest['domain_concepts']=={'local_classes':35,'markers':4,'undeclared':8},'MANIFEST_COUNTS')
 require(d['membership_additive'] is False and d['planned_profiles_are_implemented'] is False and d['semantic_adequacy_established'] is False,'COUNTING_SCOPE')
 return True
def run():
 a=json.loads(ANNEX.read_text());sources(a)
 data={r[k]:load(r[k]) for r in a['rows'] for k in ['result_path','receipt_path']}
 data.update(concepts=rows('conceptualization/core/core-concept-registry-v0.1.csv'),owners=rows('architecture/g2/concept-relation-ownership-matrix-v0.1.csv'),modules=rows('architecture/g2/module-profile-registry-v0.1.csv'),membership=rows('conceptualization/revision-2026-10-05/domain-membership.csv'),inventory=rows('docs/formal/0.2.0-rc.4/entity-inventory.csv'),cq=rows('evaluation/cq/issue52-cq-results-v1.0.csv'),roadmap=(ROOT/'docs/research/domain-profile-roadmap.md').read_text(),manifest=load('ontology/releases/0.2.0-rc.4/manifest.json'),historical_manifest=(ROOT/'ontology/p1-r2-candidate-manifest.yaml').read_text())
 validate(a,data)
 cases={
 'wrong_objective_source':lambda a,d:a['objective_source'].update(path='invented.md'),
 'missing_ownership_source':lambda a,d:a['source_sha256'].pop('architecture/g2/concept-relation-ownership-matrix-v0.1.csv'),
 'invented_scope':lambda a,d:next(r for r in d['membership'] if r['scope']=='News').update(scope='Invented'),
 'blank_definition':lambda a,d:d['concepts'][0].update(definition=''),
 'invented_concept_count':lambda a,d:a['domain_module_acceptance'].update(governed_concepts=999),
 'relabeled_baseline':lambda a,d:a.update(baseline_commit='0'*40),
 'reduced_test_set':lambda a,d:a['rows'][0].update(test_ids=['OWNER-1']),
 'dropped_adverse_flag':lambda a,d:a['explicit_gaps'].pop('independent_validation_demonstrated'),
 'missing_negative_citation':lambda a,d:a['rows'][0]['test_ids'].remove('OWNER-UNBOUND'),
 'empty_negative_evidence':lambda a,d:a['rows'][0].update(negative_test_ids=[]),
 'duplicate_crosswalk_row':lambda a,d:a['rows'].append(copy.deepcopy(a['rows'][0])),
 'missing_owner':lambda a,d:d['owners'].pop(0),
 'duplicate_owner':lambda a,d:d['owners'].append(copy.deepcopy(d['owners'][0])),
 'wrong_membership_name':lambda a,d:d['membership'][0].update(concept_names='Invented'),
 'wrong_membership_count':lambda a,d:d['membership'][0].update(conceptual_member_count='999'),
 'external_reownership':lambda a,d:next(r for r in d['owners'] if r['semantic_id']=='SR-CPT-037').update(semantic_owner='SemRisk'),
 'planned_as_implemented':lambda a,d:a['domain_module_acceptance'].update(planned_profiles_are_implemented=True),
 'historical_module_substitution':lambda a,d:a['domain_module_acceptance'].update(current_modules=6),
 'marker_as_class':lambda a,d:next(r for r in d['inventory'] if r['kind']=='marker').update(kind='class'),
 'invented_test':lambda a,d:a['rows'][0]['test_ids'].append('INVENTED'),
 'failed_test':lambda a,d:next(t for t in d[a['rows'][0]['result_path']]['tests'] if t['id']=='OWNER-1').update(passed=False),
 'tested_commit_relabel':lambda a,d:a['rows'][0].update(tested_commit=a['baseline_commit']),
 'erased_ea_gap':lambda a,d:a['explicit_gaps'].update({'CQ-013':'executable'}),
 'independent_validation_claim':lambda a,d:a['explicit_gaps'].update(independent_validation_demonstrated=True),
 'additive_membership':lambda a,d:a['domain_module_acceptance'].update(membership_additive=True),
 }
 for name,mut in cases.items():
  aa=copy.deepcopy(a);dd=copy.deepcopy(data);mut(aa,dd)
  try:validate(aa,dd)
  except ValueError:continue
  raise ValueError('NEGATIVE_ACCEPTED: '+name)
 return {'result':'PASS_BOUNDED_DOCUMENTARY_CROSSWALK','requirements':['1.4','2.7','4.5'],'source_files':len(a['source_sha256']),'crosswalk_rows':len(a['rows']),'governed_concepts':47,'membership_rows':13,'negative_controls_rejected':list(cases),'new_scientific_experiments':0,'historical_tests_rerun':False,'whole_package_acceptance':False,'annex_sha256':hashlib.sha256(ANNEX.read_bytes()).hexdigest(),'checker_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
if __name__=='__main__':
 p=argparse.ArgumentParser();p.add_argument('--write',action='store_true');args=p.parse_args();result=run();text=json.dumps(result,indent=2)+'\n'
 if args.write:RESULT.write_text(text)
 elif RESULT.exists():require(RESULT.read_text()==text,'RESULT_DRIFT')
 print(text,end='')
