#!/usr/bin/env python3
"""Supplementary SHACL and asserted semantic regression; not empirical validation."""
import argparse
import json
import platform
from pathlib import Path
from rdflib import Graph, Namespace, RDF, Literal, XSD, OWL
from rdflib.compare import isomorphic
from pyshacl import validate
import pyshacl, rdflib

ROOT=Path(__file__).resolve().parents[1]
V='0.2.0-rc.1'
AC=Namespace('urn:semrisk:profile:assessment-context:')
EX=Namespace('urn:semrisk:run4:')
SR=Namespace('urn:semrisk:entity:')
DCT=Namespace('http://purl.org/dc/terms/')
PROV=Namespace('http://www.w3.org/ns/prov#')
def c(n):return SR[f'SR-CPT-{n:03}']
def r(n):return SR[f'SR-REL-{n:03}']
def fixture():return Graph().parse(ROOT/f'testdata/temporal/qualified-context-v{V}.ttl')
def copy(g):
 h=Graph()
 for t in g:h.add(t)
 return h
def validate_graph(g,meta=False):
 return validate(g,shacl_graph=Graph().parse(ROOT/f'shapes/assessment-context-v{V}.ttl'),
                 inference='none',meta_shacl=meta,advanced=False)
def owner_rows(g,stamp):
 dt=Literal(stamp,datatype=XSD.dateTime)
 if dt.toPython().tzinfo is None: raise ValueError('explicit timestamp timezone required')
 return sorted([list(map(str,row)) for row in g.query((ROOT/f'rules/enterprise/risk-owners-at-v{V}.rq').read_text(),initBindings={'asOf':dt})])

NEGATIVES=[
 ('N01','missing dimension','MinCountConstraintComponent'),
 ('N02','invalid evaluation basis','InConstraintComponent'),
 ('N03','timezone-less assessed timestamp','PatternConstraintComponent'),
 ('N04','reversed validity interval','LessThanConstraintComponent'),
 ('N05','out-of-scale value','CTX_RANGE'),
 ('N06','wrong scale dimension','CTX_RANGE'),
 ('N07','method version mismatch','CTX_METHOD'),
 ('N08','producing activity targets different risk','CTX_METHOD'),
 ('N09','cross-risk supersession','CTX_LINEAGE'),
 ('N10','cyclic supersession','CTX_LINEAGE'),
 ('N11','backwards assessment chronology','CTX_LINEAGE'),
 ('N12','incompatible result subtype/baseline','CTX_TYPE'),
 ('N13','missing scale version','MinCountConstraintComponent'),
 ('N14','multiple producing activities','MaxCountConstraintComponent'),
 ('N15','multiple method versions','MaxCountConstraintComponent'),
 ('N16','empty ownership interval','LessThanConstraintComponent'),
]
def mutate(g,id_):
 if id_=='N01':g.remove((EX.observed,AC.dimension,None))
 if id_=='N02':g.set((EX.observed,AC.evaluationBasis,AC.Unknown))
 if id_=='N03':g.set((EX.observed,AC.assessedAt,Literal('2026-10-05T08:00:00',datatype=XSD.dateTime)))
 if id_=='N04':g.set((EX['owner-active'],AC.validTo,Literal('2026-09-30T00:00:00Z',datatype=XSD.dateTime)))
 if id_=='N05':g.set((EX.observed,AC.numericValue,Literal('1.5',datatype=XSD.decimal)))
 if id_=='N06':g.set((EX.observed,AC.scale,EX['impact-scale']))
 if id_=='N07':g.set((EX.observed,AC.methodVersion,Literal('not-the-recorded-version')))
 if id_=='N08':g.set((EX.assessment,r(13),EX['other-risk']));g.add((EX['other-risk'],RDF.type,c(1)))
 if id_=='N09':g.set((EX.revised,r(33),EX.other));g.add((EX.other,r(16),EX['other-risk']))
 if id_=='N10':g.set((EX.observed,r(33),EX.revised))
 if id_=='N11':g.set((EX.revised,AC.assessedAt,Literal('2026-10-05T07:00:00Z',datatype=XSD.dateTime)))
 if id_=='N12':g.set((EX.observed,AC.controlBaseline,AC.BeforeControl))
 if id_=='N13':g.remove((EX.scale,DCT.hasVersion,None))
 if id_=='N14':g.add((EX['assessment-next'],r(15),EX.observed))
 if id_=='N15':g.add((EX.method,DCT.hasVersion,Literal('second-version')))
 if id_=='N16':g.set((EX['owner-active'],AC.validTo,Literal('2026-10-01T00:00:00Z',datatype=XSD.dateTime)))
 return g

def run():
 tests=[]
 def record(id_,ok,details):tests.append({'id':id_,'passed':bool(ok),'details':details})
 old='A condition or occurrence that initiates or activates a transition in a risk-relevant scenario, event, monitoring or response process.'
 new='An occurrence acting as the initiating event for a risk-relevant event or process transition; an enabling condition is represented separately as a Predisposing Condition.'
 for m in ['core','enterprise','method','governance','pharma','mappings']:
  before=Graph().parse(ROOT/f'ontology/{m}/semrisk-{m}-v0.1.0-rc.1.ttl')
  s=(ROOT/f'ontology/releases/{V}/{m}.ttl').read_text()
  normalized=s.replace(V,'0.1.0-rc.1').replace('2026-10-05','2026-09-23').replace(new,old)
  after=Graph().parse(data=normalized,format='turtle')
  record('BASE-'+m,isomorphic(before,after),'Only version/date metadata and declared Trigger annotation differ; logical assertions preserved.')
 base=fixture();ok,_,txt=validate_graph(base,meta=True)
 record('SHACL-POS',ok,txt.strip())
 for id_,title,marker in NEGATIVES:
  ok,_,txt=validate_graph(mutate(copy(base),id_))
  record(id_,not ok and marker in txt,{'case':title,'expected_marker':marker,'marker_observed':marker in txt})
 stamps=[
 ('2026-09-30T23:59:59Z',['actor-d']),
 ('2026-10-01T00:00:00Z',['actor-a','actor-d','actor-f']),
 ('2026-10-04T00:00:00Z',['actor-a','actor-d']),
 ('2026-10-05T08:00:00Z',['actor-a','actor-b']),
 ('2026-10-06T00:00:00Z',['actor-a','actor-b','actor-c']),
 ('2026-10-05T11:30:00+03:30',['actor-a','actor-b'])]
 for i,(stamp,names) in enumerate(stamps,1):
  rows=owner_rows(base,stamp);expected=[[str(EX.risk),str(EX[n])] for n in names]
  record(f'OWNER-{i}',rows==expected,{'at':stamp,'actual':rows})
 q=(ROOT/f'rules/enterprise/risk-owners-at-v{V}.rq').read_text()
 record('OWNER-UNBOUND',len(list(base.query(q)))==0,'Explicit asOf binding required.')
 return {'profile_version':V,'scope':'supplementary asserted/SHACL regressions, no empirical validation',
  'python':platform.python_version(),'rdflib':rdflib.__version__,'pyshacl':pyshacl.__version__,
  'total':len(tests),'passed':sum(x['passed'] for x in tests),'tests':tests,
  'negative_controls':len(NEGATIVES),'original_cq_total_unchanged':40,'expert_responses':0}
if __name__=='__main__':
 p=argparse.ArgumentParser();p.add_argument('--write',action='store_true');args=p.parse_args();out=run()
 if args.write:
  (ROOT/f'evaluation/temporal/v{V}/semantic-results.json').write_text(json.dumps(out,indent=2)+'\n')
 print(json.dumps(out,indent=2));raise SystemExit(0 if out['passed']==out['total'] else 1)
