#!/usr/bin/env python3
"""Build an information-level literature dataset; do not invent domain occurrences."""
import csv, io, json, hashlib
from pathlib import Path
from collections import Counter
from rdflib import Graph, Namespace, URIRef, Literal, RDF, RDFS, OWL
from rdflib.namespace import DCTERMS, XSD

ROOT=Path(__file__).resolve().parents[1]
DATA=ROOT/'case/pharma/literature-pilot-v0.1.0'
SR=Namespace('urn:semrisk:entity:'); IST=Namespace('urn:semrisk:profile:information-state:')
GUFO=Namespace('http://purl.org/nemo/gufo#'); PROV=Namespace('http://www.w3.org/ns/prov#')
CASE=Namespace('urn:semrisk:case:pharma-literature:metadata:')
BASE='urn:semrisk:case:pharma-literature:v0.1.0:'
def read(name):return json.loads((DATA/name).read_text())
def write(name,data): (DATA/name).write_text(json.dumps(data,ensure_ascii=False,indent=2)+'\n')
def graph(rows,mappings,sources):
 g=Graph();byid={m['statement_id']:m for m in mappings}
 for prefix,ns in [('sr',SR),('ist',IST),('gufo',GUFO),('prov',PROV),('case',CASE),('dcterms',DCTERMS)]:g.bind(prefix,ns)
 for s in sources:
  u=URIRef('https://doi.org/'+s['doi']);g.add((u,RDF.type,PROV.Entity));g.add((u,DCTERMS.title,Literal(s['title'])))
  g.add((u,DCTERMS.identifier,Literal(s['source_id'])))
 for r in rows:
  m=byid[r['statement_id']];a=URIRef(BASE+r['statement_id']);v=URIRef(str(a)+':version');c=URIRef(str(a)+':content')
  source=next(s for s in sources if s['source_id']==r['source_id']);u=URIRef('https://doi.org/'+source['doi'])
  g.add((a,RDF.type,IST.ManagedInformationArtifact));g.add((a,RDF.type,SR['SR-CPT-020']))
  g.add((v,RDF.type,IST.ArtifactVersion));g.add((v,IST.versionOf,a));g.add((v,OWL.differentFrom,a));g.add((v,IST.expressesContent,c))
  g.add((c,RDF.type,IST.InformationContent));g.add((c,RDF.value,Literal(r['statement_paraphrase'],lang='en')))
  g.add((v,PROV.wasDerivedFrom,u));g.add((v,DCTERMS.identifier,Literal(r['statement_id'])))
  for k,val in r.items():g.add((v,CASE[k],Literal(val)))
  g.add((v,CASE.mapping_status,Literal(m['mapping_status'])))
  g.add((v,CASE.mapping_rationale,Literal(m['mapping_rationale'])))
  for target in m['semrisk_ids']:g.add((v,DCTERMS.subject,SR[target]))
  if m['scenario_type_created']:
   t=URIRef(str(a)+':scenario-type');g.add((v,RDF.type,SR['SR-CPT-034']));g.add((v,SR['SR-REL-002'],t))
   g.add((t,RDF.type,SR['SR-CPT-006']));g.add((t,RDF.type,GUFO.SituationType));g.add((t,RDF.type,OWL.Class));g.add((t,RDFS.subClassOf,GUFO.Situation))
   g.add((t,RDFS.label,Literal(r['potential_event']+' / '+r['consequence'],lang='en')))
 return g
def csv_text(rows):
 out=io.StringIO(newline='');w=csv.DictWriter(out,fieldnames=list(rows[0]),lineterminator='\n');w.writeheader()
 for r in rows:w.writerow({k:json.dumps(v,ensure_ascii=False,sort_keys=True) if isinstance(v,(list,dict,bool)) else v for k,v in r.items()})
 return out.getvalue()
def outputs():
 rows=read('statements.json');maps=read('mappings.json');sources=read('sources.json');g=graph(rows,maps,sources)
 out={name+'.csv':csv_text(value).encode() for name,value in [('statements',rows),('mappings',maps),('sources',sources)]}
 # Sorted N-Triples is deterministic, blank-node-free and also valid Turtle syntax.
 out['statements.ttl']=(''.join(sorted(g.serialize(format='nt').splitlines(keepends=True)))).encode()
 for k,v in out.items():(DATA/k).write_bytes(v)
 metrics=dict(statement_count=len(rows),source_count=len(sources),mapping_status=dict(sorted(Counter(m['mapping_status'] for m in maps).items())),categories=dict(sorted(Counter(r['enterprise_context'] for r in rows).items())),source_reuse_statements=dict(sorted(Counter(r['source_role'] for r in rows).items())),source_reuse_sources=dict(sorted(Counter(s['source_role'] for s in sources).items())),scenario_type_count=sum(m['scenario_type_created'] for m in maps),rdf_triples=len(g),missingness={k:sum(r[k]=='NOT_REPORTED' for r in rows) for k in ['potential_event','consequence','likelihood_reported','impact_reported','control_reported','temporal_qualifier']},independently_reviewed_statements=0,independent_validation_sources=0,occurred_events_asserted=0,unique_global_risks='NOT_ESTIMATED',note='All rates use 24 source-local statements or 6 selected sources, never incidents, companies or all pharmaceutical risks.')
 write('metrics.json',metrics)
 lines=['# Extraction bibliography','', 'All six retained studies are cited below. Only the inspected passages, not the complete studies, were extracted.','']
 for s in sources:lines.append(f"- **{s['source_id']}** {s['authors']} ({s['year']}). {s['title']}. https://doi.org/{s['doi']}. Publisher version of record.\n")
 (DATA/'bibliography.md').write_text('\n'.join(lines))
 return metrics
def manifest():
 files=[p for p in DATA.iterdir() if p.is_file() and p.name not in ['manifest.json','postgres-results.json','ci-evidence.json']]
 files += [ROOT/p for p in ['tools/build_pharma_literature_pilot.py','tools/check_pharma_literature_pilot.py','relational/scripts/literature_io.py','tools/check_literature_postgres.py','.github/workflows/paper1-literature-pilot.yml','tools/build_literature_review.mjs','outputs/semrisk-run9/pharma-literature-pilot-v0.1.0.xlsx'] if (ROOT/p).exists()]
 write('manifest.json',dict(dataset_version='0.1.0',status='research_candidate_not_scholarly_release',ontology_version='0.2.0-rc.4',ontology_commit='231a82cde3a43ccbafc06afa744ea9df35af7c26',cm_pharme_version='1.0.0',build='python tools/build_pharma_literature_pilot.py',files=[dict(path=str(p.relative_to(ROOT)),bytes=p.stat().st_size,sha256=hashlib.sha256(p.read_bytes()).hexdigest()) for p in sorted(files)],exclusions=['Runtime CI evidence is bound to its commit separately.','No source article full text, confidential workbook or participant records redistributed.']))
if __name__=='__main__':print(json.dumps(outputs(),indent=2));manifest()
