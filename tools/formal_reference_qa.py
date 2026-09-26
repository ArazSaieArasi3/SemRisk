"""Exact local-source QA for the curated P1-R2 FD-A–FD-J reference.

Only six local ontology modules are in scope. Imported ontologies and future
publication-release binding remain separate tasks.
"""
import csv,hashlib,collections,re,sys
from pathlib import Path
from xml.etree import ElementTree as ET
from rdflib import Graph, URIRef, Literal
from rdflib.namespace import RDF,RDFS,OWL,SKOS,DCTERMS
base=Path('.')
rows=list(csv.DictReader(open('docs/ontology/p1-r2-formal-source-entity-reference-v0.1.csv')))
by=collections.defaultdict(list)
for r in rows:by[r['source_path']].append(r)
errs=[]; type_map={'owl:Class':OWL.Class,'owl:ObjectProperty':OWL.ObjectProperty,'skos:Concept':SKOS.Concept}
gufo='http://purl.org/nemo/gufo#';sr='urn:semrisk:entity:'
def uri(x):
 if x.startswith('sr:'):return URIRef(sr+x[3:])
 if x.startswith('gufo:'):return URIRef(gufo+x[5:])
 raise ValueError(x)
allids=[]
for path,rs in by.items():
 data=Path(path).read_bytes();sha=hashlib.sha1(b'blob '+str(len(data)).encode()+b'\0'+data).hexdigest()
 g=Graph().parse(data=data.decode(),format='turtle')
 decl=set()
 for typ in type_map.values():decl|={str(s) for s in g.subjects(RDF.type,typ) if str(s).startswith(sr)}
 catalog={r['iri'] for r in rs};errs += [f'{path}: source/catalog declaration difference {sorted(decl^catalog)}'] if decl!=catalog else []
 for r in rs:
  s=URIRef(r['iri']); allids.append(r['semantic_id'])
  if sha!=r['source_blob_sha']:errs.append(r['semantic_id']+' SHA drift')
  if str(s)!=sr+r['semantic_id']:errs.append(r['semantic_id']+' IRI mismatch')
  if (s,RDF.type,type_map[r['rdf_type']]) not in g:errs.append(r['semantic_id']+' missing rdf type')
  if r['label'] not in {str(o) for o in g.objects(s,RDFS.label)}:errs.append(r['semantic_id']+' label mismatch')
  for col,pred in [('asserted_subclass',RDFS.subClassOf),('asserted_domain_in_declaration',RDFS.domain),('asserted_range_in_declaration',RDFS.range),('asserted_inverse_in_declaration',OWL.inverseOf)]:
   vals={str(o) for o in g.objects(s,pred)}
   wanted={str(uri(x.strip())) for x in r[col].split(';') if x.strip()}
   if vals!=wanted:errs.append(r['semantic_id']+' '+col+' '+str((vals,wanted)))
  cq={x.strip() for o in g.objects(s,DCTERMS.relation) for x in str(o).split(';') if x.strip().startswith('CQ-')}
  wanted={x.strip() for x in r['cq_annotations'].split(';') if x.strip()}
  if cq!=wanted:errs.append(r['semantic_id']+' CQ mismatch '+str((cq,wanted)))
counts=collections.Counter(x['rdf_type'] for x in rows)
if len(rows)!=76 or len(set(allids))!=76 or counts!={'owl:Class':35,'owl:ObjectProperty':37,'skos:Concept':4}:
 errs.append(f'local declaration inventory count/type drift: {len(rows)}, {counts}')

combined=Graph()
for path in by:combined.parse(path,format='turtle')
local=sr
pairs=[('SR-CPT-011','SR-CPT-013'),('SR-CPT-001','SR-CPT-013'),
       ('SR-CPT-008','SR-CPT-015'),('SR-CPT-004','SR-CPT-009'),
       ('SR-CPT-006','SR-CPT-007'),('SR-CPT-033','SR-CPT-001'),
       ('SR-CPT-034','SR-CPT-006'),('SR-CPT-034','SR-CPT-007'),
       ('SR-CPT-036','SR-CPT-035')]
for a,b in pairs:
 x,y=URIRef(local+a),URIRef(local+b)
 if (x,OWL.disjointWith,y) not in combined and (y,OWL.disjointWith,x) not in combined:
  errs.append(f'curated FD-G disjointness absent: {a}/{b}')
if any(True for _ in combined.triples((None,OWL.equivalentClass,None))):
 errs.append('local owl:equivalentClass appeared; revisit FD-G nonclaim')

sh=Graph().parse('shapes/semrisk-paper1-shapes-v0.1.0-rc.1.ttl',format='turtle')
shape_type=URIRef('http://www.w3.org/ns/shacl#NodeShape')
shape_ids={str(s).split(':')[-1] for s in sh.subjects(RDF.type,shape_type)}
if shape_ids!={f'SR-SHP-{i:03d}' for i in range(1,6)}:
 errs.append(f'FD-G shape inventory drift: {shape_ids}')
rule=Path('rules/enterprise/derive-has-risk-owner-v0.1.0-rc.1.rq').read_text()
if not all(token in rule for token in ('CONSTRUCT','SR-REL-026','SR-REL-027','SR-REL-028','invalidatedAtTime')):
 errs.append('FD-G derived-owner rule structure drift')

formal=list(csv.DictReader(open('ontology/formal-entity-inventory-v0.1.csv')))
critical=[r for r in formal if r['release_critical']=='yes']
if len(critical)!=71 or len({r['semantic_id'] for r in critical})!=71 or any(r['coverage_status']!='COVERED' for r in critical):
 errs.append('FD-I 71-ID critical inventory drift')
cqs=list(csv.DictReader(open('evaluation/cq/issue52-cq-results-v1.0.csv')))
if len(cqs)!=40 or len({r['cq_id'] for r in cqs})!=40:
 errs.append('FD-J 40-CQ denominator drift')
states=collections.Counter(r['state'] for r in cqs)
if states!={'executable':26,'partially_executable':7,'conceptual_only':6,'deferred':1}:
 errs.append(f'FD-J CQ status breakdown drift: {states}')

catalog=ET.parse('ontology/catalog-v001.xml')
ns={'c':'urn:oasis:names:tc:entity:xmlns:xml:catalog'}
targets={e.attrib['name']:Path('ontology')/e.attrib['uri'] for e in catalog.findall('c:uri',ns)}
for path in by:
 g=Graph().parse(path,format='turtle')
 for imported in g.objects(None,OWL.imports):
  if str(imported) not in targets:
   errs.append(f'FD-A import without local catalog binding: {path} -> {imported}')
  elif not targets[str(imported)].is_file():
   errs.append(f'FD-A import catalog target missing: {imported} -> {targets[str(imported)]}')

doc=Path('docs/ontology/formal-ontology-description-p1-r2-v0.2.md').read_text()
for section in 'ABCDEFGHIJ':
 if not re.search(r'FD-'+section+r'\b',doc):errs.append(f'missing FD-{section} documentation section')
for path in by:
 sha=rows[next(i for i,r in enumerate(rows) if r['source_path']==path)]['source_blob_sha']
 if path not in doc or sha not in doc:errs.append(f'FD-B path/blob not present in reference: {path}')
if errors:=errs:
 raise SystemExit('FORMAL_REFERENCE_QA_FAIL\n'+'\n'.join(errors[:30]))
print('SEM_RISK_FORMAL_REFERENCE_LOCAL_SOURCE_PASS | 76/76 declared IDs; 35 classes, 37 object properties, 4 SKOS markers; 9/9 selected disjointness pairs; 5 shapes; 1 rule; 71/71 critical IDs; 40/40 CQ rows; declared imports resolve via catalog')
