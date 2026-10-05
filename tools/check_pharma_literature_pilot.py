#!/usr/bin/env python3
"""Dataset integrity checks; these do not establish domain/expert validity."""
import csv,copy,hashlib,io,json,re
from collections import Counter
from rdflib import Graph,RDF,URIRef,OWL
from pyshacl import validate as shacl
from build_pharma_literature_pilot import ROOT,DATA,read,write,graph,SR,IST,CASE,BASE,csv_text

FIELD_TYPES={'statements': {'statement_id': 'str', 'source_id': 'str', 'source_locator': 'str', 'source_role': 'str', 'extracted_at': 'str', 'statement_paraphrase': 'str', 'enterprise_context': 'str', 'subject_actor': 'str', 'potential_event': 'str', 'consequence': 'str', 'likelihood_reported': 'str', 'impact_reported': 'str', 'other_quantity_reported': 'str', 'temporal_qualifier': 'str', 'control_reported': 'str', 'evidence_kind': 'str', 'review_status': 'str', 'extraction_method': 'str', 'rights_status': 'str', 'duplicate_group': 'str', 'occurrence_status': 'str'}, 'mappings': {'statement_id': 'str', 'mapping_status': 'str', 'semrisk_ids': 'list', 'external_ids': 'list', 'external_mapping_status': 'str', 'external_rationale': 'str', 'mapping_rationale': 'str', 'scenario_type_created': 'bool', 'source_field_dispositions': 'dict'}, 'sources': {'source_id': 'str', 'title': 'str', 'authors': 'str', 'year': 'int', 'doi': 'str', 'url': 'str', 'version': 'str', 'source_role': 'str', 'evaluation_use': 'str', 'discovery_route': 'str', 'method': 'str', 'study_context': 'str', 'rights_note': 'str', 'limitations': 'str', 'accessed_at': 'str', 'locator_review': 'str', 'independent_validation': 'bool'}}
def strict_fields(records, contract):
 types={'str':str,'int':int,'bool':bool,'list':list,'dict':dict}
 for record in records:
  assert set(record)==set(contract),'SCHEMA_FIELDS'
  assert all(type(record[k]) is types[t] for k,t in contract.items()),'SCHEMA_TYPES'

def validate(rows,maps,sources):
 for records,key in [(rows,"statements"),(maps,"mappings"),(sources,"sources")]:strict_fields(records,FIELD_TYPES[key])
 assert rows and sources,'EMPTY'
 ids=[r['statement_id'] for r in rows];assert len(ids)==len(set(ids)),'DUPLICATE_ID'
 assert len(maps)==len(rows) and {m['statement_id'] for m in maps}==set(ids),'MAPPING_JOIN'
 ss={s['source_id']:s for s in sources};assert len(ss)==len(sources),'DUPLICATE_SOURCE'
 assert len({s['doi'].lower() for s in sources})==len(sources),'DUPLICATE_DOI'
 frozen=Graph()
 for p in (ROOT/'ontology/releases/0.2.0-rc.4').glob('*.ttl'):frozen.parse(p)
 known={str(x).rsplit(':',1)[-1] for x in frozen.subjects() if str(x).startswith(str(SR))}
 for s in sources:
  assert s['evaluation_use']=='applicability_only' and not s['independent_validation'],'FALSE_HOLDOUT'
  assert s['source_role'] in ['design_reused','evaluation_new'],'SOURCE_ROLE'
  assert s['doi'].startswith('10.') and s['url'].startswith('https://'),'SOURCE_LOCATOR'
 for r in rows:
  assert re.fullmatch(r'PRS-\d{4}',r['statement_id']),'ID_FORMAT'
  assert r['source_id'] in ss,'UNKNOWN_SOURCE'
  for k in ['source_locator','statement_paraphrase','enterprise_context','subject_actor','extracted_at','rights_status','extraction_method']:assert isinstance(r.get(k),str) and r[k].strip(),'MISSING_PROVENANCE'
  assert r['source_role']==ss[r['source_id']]['source_role'],'ROLE_DRIFT'
  assert r['occurrence_status']=='NOT_ASSERTED' and r['evidence_kind']=='author_analysis','FABRICATED_OBSERVATION'
  assert r['review_status']=='unreviewed','FALSE_REVIEW'
  for k in ['potential_event','consequence','likelihood_reported','impact_reported','control_reported','temporal_qualifier']:
   assert isinstance(r[k],str) and r[k],'MISSING_VALUE_AMBIGUITY'
  allowed_likelihood={'NOT_REPORTED','High probability group; source-local uncalibrated category','Low probability group; source-local uncalibrated category'}
  assert r['likelihood_reported'] in allowed_likelihood,'UNQUALIFIED_LIKELIHOOD'
  assert r['impact_reported'] in {'NOT_REPORTED','High hazard group; source-local uncalibrated category'},'UNQUALIFIED_IMPACT'
 for m in maps:
  assert m['mapping_status'] in ['partial','ambiguous','unmapped'] and m['mapping_rationale'],'MAPPING_STATUS'
  assert set(m['semrisk_ids'])<=known,'INVALID_SEMANTIC_ID'
  assert not m['external_ids'],'UNREVIEWED_EXTERNAL_ID'
  if m['scenario_type_created']:
   r=next(r for r in rows if r['statement_id']==m['statement_id'])
   assert m['mapping_status']=='partial' and r['potential_event']!='NOT_REPORTED' and r['consequence']!='NOT_REPORTED','FORCED_SCENARIO'
 return True

def main():
 rows=read('statements.json');maps=read('mappings.json');sources=read('sources.json');tests=[]
 def check(n,yes):tests.append(dict(id=n,passed=bool(yes)));assert yes,n
 check('DATA-CONTRACT',validate(rows,maps,sources))
 for name,x in [('statements',rows),('mappings',maps),('sources',sources)]:
  actual=(DATA/(name+'.csv')).read_bytes();check('CSV-'+name,actual==csv_text(x).encode())
  decoded=list(csv.DictReader(io.StringIO(actual.decode())))
  check('CSV-ROUNDTRIP-'+name,len(decoded)==len(x) and all(all(v==str(r[k]) if not isinstance(r[k],(list,dict,bool)) else json.loads(v)==r[k] for k,v in d.items()) for d,r in zip(decoded,x)))
 g=graph(rows,maps,sources);on_disk=Graph().parse(DATA/'statements.ttl')
 check('RDF-EQUALITY',set(g)==set(on_disk))
 check('RDF-NO-OCCURRENCE',not list(g.subjects(RDF.type,SR['SR-CPT-007'])))
 check('RDF-NO-ASSESSMENT',not list(g.subjects(RDF.type,SR['SR-CPT-013'])))
 check('RDF-NO-INSTANCE-WITNESS',all(not list(g.subjects(RDF.type,t)) for t in g.subjects(RDF.type,SR['SR-CPT-006'])))
 q='SELECT ?s (COUNT(?v) AS ?n) WHERE {?v <http://www.w3.org/ns/prov#wasDerivedFrom> ?s} GROUP BY ?s'
 got={str(x[0]):int(x[1]) for x in g.query(q)}
 expected={'https://doi.org/'+s['doi']:sum(r['source_id']==s['source_id'] for r in rows) for s in sources}
 check('SOURCE-COUNT-CQ',got==expected)
 q='SELECT ?status (COUNT(?v) AS ?n) WHERE {?v <urn:semrisk:case:pharma-literature:metadata:mapping_status> ?status} GROUP BY ?status'
 check('MAPPING-COUNT-CQ',{str(x[0]):int(x[1]) for x in g.query(q)}==dict(Counter(m['mapping_status'] for m in maps)))
 shapes=Graph().parse(ROOT/'shapes/semantic-identity-v0.2.0-rc.3.ttl')
 check('SHACL-ARTIFACT-IDENTITY',shacl(g,shacl_graph=shapes,inference='none')[0])
 mutations=[('N11-UNKNOWN-FIELD',lambda r,m,s:r[0].update(unregistered_field='x')),('N12-BOOLEAN-TYPE',lambda r,m,s:m[0].update(scenario_type_created='false')),('N01-MISSING-LOCATOR',lambda r,m,s:r[0].update(source_locator='')),('N02-DUPLICATE-ID',lambda r,m,s:r[1].update(statement_id=r[0]['statement_id'])),('N03-INVALID-ID',lambda r,m,s:m[0]['semrisk_ids'].append('SR-CPT-999')),('N04-FALSE-OBSERVATION',lambda r,m,s:r[0].update(occurrence_status='observed')),('N05-FALSE-HOLDOUT',lambda r,m,s:s[0].update(independent_validation=True)),('N06-INVENTED-PROBABILITY',lambda r,m,s:r[0].update(likelihood_reported='0.9018')),('N07-FORCED-SCENARIO',lambda r,m,s:m[0].update(scenario_type_created=True)),('N08-ROLE-DRIFT',lambda r,m,s:r[0].update(source_role='evaluation_new')),('N09-FALSE-REVIEW',lambda r,m,s:r[0].update(review_status='independent_review'))]
 for n,mutation in mutations:
  r,m,s=copy.deepcopy((rows,maps,sources));mutation(r,m,s)
  try:validate(r,m,s)
  except AssertionError:check(n,True)
  else:check(n,False)
 bad=Graph();bad+=g;v=URIRef(BASE+rows[0]['statement_id']+':version');bad.remove((v,IST.versionOf,None))
 check('N10-MISSING-VERSION-PARENT',not shacl(bad,shacl_graph=shapes,inference='none')[0])
 check('DEDUP-ACCOUNTING',{d['statement_id'] for d in read('dedup-decisions.json')}=={r['statement_id'] for r in rows})
 result=dict(result='PASS_BOUNDED_INFORMATION_DATASET',total=len(tests),passed=sum(t['passed'] for t in tests),negative_controls=12,tests=tests,limits=['No independent extractor, domain expert review, inter-rater agreement or empirical ontology validation.','SQL information staging is tested separately; no full domain/temporal SQL parity claim.'])
 write('validation-results.json',result);print(json.dumps(result,indent=2))
 return result
if __name__=='__main__':main()
