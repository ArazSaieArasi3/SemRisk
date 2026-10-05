#!/usr/bin/env python3
"""Version/hash binding and offline assembly for the bounded foundational successor."""
import argparse,hashlib,json
from pathlib import Path
from xml.etree import ElementTree
from rdflib import Graph,OWL,RDF,Namespace
from check_foundational_revision import ROOT,V,D,MODULES,data,GUFO,EX,AC

def sources():
 return [f'ontology/releases/{V}/{m}.ttl' for m in MODULES]+[f'ontology/releases/{V}/catalog.xml',f'ontology/releases/{V}/profile-iri-registry.csv',
 'ontology/vendor/gufo-v1.0.0.ttl','foundational/revision-2026-10-05/definition-delta.json','foundational/revision-2026-10-05/concept-category-audit.csv','foundational/revision-2026-10-05/relation-formal-audit.csv',
 f'shapes/foundational-evidence-v{V}.ttl',f'testdata/foundational/grounded-responsibility-v{V}.ttl',
 'shapes/assessment-context-v0.2.0-rc.1.ttl','testdata/temporal/qualified-context-v0.2.0-rc.1.ttl','rules/enterprise/risk-owners-at-v0.2.0-rc.1.rq','relational/sql/V007__qualified_assessment_context.sql',
 'tools/check_foundational_revision.py','tools/build_foundational_candidate.py','tools/requirements-qualified-context.txt']
def manifest():
 return dict(candidate_version=V,baseline_commit='9fb392b2b592caf1e9fbf0f108daab9a73461320',previous_candidate='0.2.0-rc.1',publication_ready=False,module_count=7,
  semantic_changes=['RiskOwner metatype Role to RoleMixin','Four scope definition clarifications','Opt-in GroundedRiskResponsibility helper; no stricter constraints on legacy records'],
  preserved=['All historical release files','All old temporal SHACL/SQL/query files','35 local conceptual classes + 4 markers + 8 undeclared concepts'],
  source_sha256={p:hashlib.sha256((ROOT/p).read_bytes()).hexdigest() for p in sources()},
  remaining=['Scenario type/instance resolution','Information artifact identity helpers','Workflow value versus quality view','Complete editable OntoUML','Named-counterpart SQL projection only if adopted by case'],
  evidence_directory='evaluation/foundational/2026-10-05')
def assemble():
 cat=ElementTree.parse(D/'catalog.xml');ns={'c':'urn:oasis:names:tc:entity:xmlns:xml:catalog'}
 bind={x.attrib['name']:(D/x.attrib['uri']).resolve() for x in cat.findall('c:uri',ns)}
 todo=[D/f'{m}.ttl' for m in MODULES];seen=set();g=Graph()
 while todo:
  p=todo.pop()
  if p in seen:continue
  seen.add(p);part=Graph().parse(p)
  for iri in part.objects(None,OWL.imports):
   if str(iri) not in bind:raise ValueError('Unresolved import '+str(iri))
   todo.append(bind[str(iri)])
  g+=part
 g.remove((None,OWL.imports,None))
 g.parse(ROOT/'testdata/temporal/qualified-context-v0.2.0-rc.1.ttl')
 out=ROOT/'build/foundational-candidate';out.mkdir(parents=True,exist_ok=True)
 # Independent worlds. No attempted claim that the incomplete fixture passes the stricter SHACL profile.
 positive=Graph();positive+=g;positive+=data();positive.serialize(out/'positive.owl',format='xml')
 incomplete=Graph();incomplete+=positive;incomplete.remove((EX.responsibility,GUFO.mediates,EX.organization));incomplete.remove((EX.person,OWL.differentFrom,EX.organization));incomplete.serialize(out/'incomplete.owl',format='xml')
 contradiction=Graph();contradiction+=positive;contradiction.add((EX.person,RDF.type,GUFO.Event));contradiction.serialize(out/'contradiction.owl',format='xml')
 (out/'assembly.json').write_text(json.dumps(dict(version=V,source_files=sorted(str(p.relative_to(ROOT)) for p in seen),imports_resolved_offline=True,positive_triples=len(positive),contradiction='Same synthetic individual is Endurant and Event; gUFO disjointness must reject',incomplete='Second named witness absent; OWA permits an unnamed witness, while opt-in SHACL must reject'),indent=2)+'\n')
 print('Assembled three isolated formal probes from',len(seen),'source files.')
if __name__=='__main__':
 p=argparse.ArgumentParser();p.add_argument('--check',action='store_true');p.add_argument('--assemble',action='store_true');a=p.parse_args();s=json.dumps(manifest(),indent=2)+'\n';target=D/'manifest.json'
 if a.check:assert target.read_text()==s,'Candidate hash binding changed'
 else:target.write_text(s)
 if a.assemble:assemble()
 print('Foundational candidate binding verified' if a.check else 'Foundational candidate binding generated')
