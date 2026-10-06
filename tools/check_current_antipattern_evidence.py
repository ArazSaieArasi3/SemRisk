#!/usr/bin/env python3
"""Bounded asserted-source regressions, never a full OntoUML antipattern verdict."""
import argparse,copy,csv,hashlib,json,sys
import rdflib
from pathlib import Path
from rdflib import Graph,Namespace,URIRef
from rdflib.namespace import RDF,RDFS,OWL,SKOS
from generate_rc4_formal_reference import MODULES,RELEASE
ROOT=Path(__file__).resolve().parents[1];OUT=ROOT/'evaluation/antipatterns/0.2.0-rc.4'
SR=Namespace('urn:semrisk:entity:');GUFO=Namespace('http://purl.org/nemo/gufo#');IST=Namespace('urn:semrisk:profile:information-state:')
COVER=URIRef('https://purl.org/krdb-core/cover#Risk');ROSE=URIRef('http://rose.com#SecurityMechanism')
def c(n):return SR[f'SR-CPT-{n:03}']
def distinct(g,a,b):return (a,OWL.disjointWith,b) in g or (b,OWL.disjointWith,a) in g
def no_equivalence(g,a,b):return (a,OWL.equivalentClass,b) not in g and (b,OWL.equivalentClass,a) not in g
HELPERS={'H-QualifiedAssessmentResult','H-GroundedRiskResponsibility','H-NumericScale','H-Dimension','H-ControlBaseline','H-EvaluationBasis','H-ManagedInformationArtifact','H-ArtifactVersion','H-InformationContent','H-WorkflowSchemeVersion','H-WorkflowAssignment'}
BOUNDARIES={'B-Endurant','B-Context','B-Affected','B-Actor','B-Pharma','B-Profile','B-Core'}
IST_HELPERS={'H-ManagedInformationArtifact','H-ArtifactVersion','H-InformationContent','H-WorkflowSchemeVersion','H-WorkflowAssignment'}
HELPER_IRIS={h:('urn:semrisk:profile:information-state:' if h in IST_HELPERS else 'urn:semrisk:profile:assessment-context:')+h[2:] for h in HELPERS}
def checks(g,spec,concept_ids):
 nodes=spec['nodes'];a=lambda s,p,o:(s,p,o) in g
 return {
 'FAP-001':a(c(1),SKOS.relatedMatch,COVER) and no_equivalence(g,c(1),COVER) and not a(c(1),RDFS.subClassOf,GUFO.Quality),
 'FAP-002':a(c(11),RDFS.subClassOf,GUFO.Event) and a(c(13),RDFS.subClassOf,IST.ArtifactVersion) and distinct(g,c(11),c(13)),
 'FAP-003':a(c(34),RDFS.subClassOf,IST.ArtifactVersion) and a(c(6),RDFS.subClassOf,GUFO.SituationType) and a(c(7),RDFS.subClassOf,GUFO.Event) and distinct(g,c(6),c(7)) and distinct(g,c(34),c(6)) and distinct(g,c(34),c(7)) and no_equivalence(g,c(34),c(6)),
 'FAP-004':all(a(c(n),RDFS.subClassOf,c(13)) and not a(c(n),RDFS.subClassOf,c(1)) for n in [17,18]),
 'FAP-005':a(c(30),RDF.type,GUFO.RoleMixin) and not a(c(30),RDF.type,GUFO.Role) and not a(c(30),RDF.type,GUFO.Kind) and nodes['SR-CPT-030']['stereotype']=='roleMixin',
 'FAP-007':a(c(31),RDFS.subClassOf,GUFO.Relator),
 'FAP-008':a(c(29),RDF.type,GUFO.RoleMixin) and a(c(29),SKOS.relatedMatch,ROSE) and no_equivalence(g,c(29),ROSE),
 'FAP-009':a(c(9),RDFS.subClassOf,GUFO.IntrinsicMode) and a(c(4),RDFS.subClassOf,GUFO.Situation) and distinct(g,c(9),c(4)),
 'FAP-010':a(c(35),RDFS.subClassOf,GUFO.Situation) and a(c(36),RDFS.subClassOf,GUFO.QualityValue) and distinct(g,c(35),c(36)),
 'FAP-011':a(c(14),RDFS.subClassOf,c(13)) and a(c(14),RDFS.subClassOf,IST.ArtifactVersion) and not a(c(14),RDFS.subClassOf,GUFO.Quality),
 'FAP-015':concept_ids=={f'SR-CPT-{n:03}' for n in range(1,48)} and all(nodes[h].get('iri')==iri and a(URIRef(iri),RDF.type,OWL.Class) for h,iri in HELPER_IRIS.items() if h in nodes) and all(nodes[n].get('iri')==str(SR[n]) for n in concept_ids if n in nodes) and {x for x in nodes if x.startswith('SR-CPT-')}==concept_ids and {x for x in nodes if x.startswith('H-')}==HELPERS and {x for x in nodes if x.startswith('B-')}==BOUNDARIES and set(nodes)==concept_ids|HELPERS|BOUNDARIES,
 }
def validate_ids(rows,key,expected):
 values=[r[key] for r in rows]
 if len(values)!=len(expected) or set(values)!=expected:raise ValueError('REGISTER_IDS: '+key)
def run():
 g=Graph();paths=[RELEASE/(m+'.ttl') for m in MODULES]
 for p in paths:g.parse(ROOT/p)
 specpath=Path('diagrams/ontouml/0.2.0-rc.4/view-spec.json');spec=json.loads((ROOT/specpath).read_text())
 registry=Path('foundational/exposure-scale-v0.2.0-rc.4/concept-category-audit.csv');registry_rows=list(csv.DictReader((ROOT/registry).open()));ids={r['semantic_id'] for r in registry_rows}
 validate_ids(registry_rows,'semantic_id',{f'SR-CPT-{n:03}' for n in range(1,48)})
 legacy=Path('foundational/foundational-antipattern-register.csv');rows=list(csv.DictReader((ROOT/legacy).open()))
 validate_ids(rows,'finding_id',{f'FAP-{n:03}' for n in range(1,16)})
 result=checks(g,spec,ids)
 if not all(result.values()):raise ValueError('CURRENT_ASSERTION_FAILURE: '+repr([x for x,v in result.items() if not v]))
 mutations={
 'FAP-001':lambda h,s:h.add((c(1),OWL.equivalentClass,COVER)),
 'FAP-002':lambda h,s:h.remove((c(13),RDFS.subClassOf,IST.ArtifactVersion)),
 'FAP-003':lambda h,s:h.add((c(34),OWL.equivalentClass,c(6))),
 'FAP-004':lambda h,s:h.add((c(17),RDFS.subClassOf,c(1))),
 'FAP-005':lambda h,s:h.add((c(30),RDF.type,GUFO.Role)),
 'FAP-005#kind':lambda h,s:h.add((c(30),RDF.type,GUFO.Kind)),
 'FAP-015#iri':lambda h,s:s['nodes']['H-ArtifactVersion'].update(iri=str(c(13))),
 'FAP-007':lambda h,s:h.remove((c(31),RDFS.subClassOf,GUFO.Relator)),
 'FAP-008':lambda h,s:h.add((c(29),OWL.equivalentClass,ROSE)),
 'FAP-009':lambda h,s:h.remove((c(9),RDFS.subClassOf,GUFO.IntrinsicMode)),
 'FAP-010':lambda h,s:h.remove((c(36),RDFS.subClassOf,GUFO.QualityValue)),
 'FAP-011':lambda h,s:h.add((c(14),RDFS.subClassOf,GUFO.Quality)),
 'FAP-015':lambda h,s:s['nodes'].update({'H-Invented':{'id':'H-Invented'}}),
 }
 for fid,mut in mutations.items():
  h=Graph();h+=g;s=copy.deepcopy(spec);mut(h,s)
  if checks(h,s,ids)[fid.split('#')[0]]:raise ValueError('NEGATIVE_ACCEPTED: '+fid)
 # A coordinated extra registry/view node must not expand the accepted domain denominator.
 s=copy.deepcopy(spec);s['nodes']['SR-CPT-048']={'iri':str(c(48))}
 if checks(g,s,ids|{'SR-CPT-048'})['FAP-015']:raise ValueError('NEGATIVE_ACCEPTED: coordinated inventory expansion')
 for data,key,expected in [(rows,'finding_id',{f'FAP-{n:03}' for n in range(1,16)}),(registry_rows,'semantic_id',ids)]:
  for altered in [data[:-1],data+[data[0]]]:
   try:validate_ids(altered,key,expected)
   except ValueError:pass
   else:raise ValueError('REGISTER_CORRUPTION_ACCEPTED')
 criteria={
 'FAP-001':'Risk relatedMatch COVER Risk; no direct equivalentClass either direction; no direct subclass Quality.',
 'FAP-002':'Activity direct subclass Event; Result direct subclass ArtifactVersion; explicit pair disjointness. Other identity/category assertions are not excluded by this predicate.',
 'FAP-003':'Description direct subclass ArtifactVersion; Scenario SituationType; Event Event; explicit pair disjointness; no direct Description/Scenario equivalence. Other equivalence paths not checked.',
 'FAP-004':'Inherent/Residual direct subclass Result; neither directly subclasses Risk. Equivalence and transitive ancestry are not checked here.',
 'FAP-005':'Owner typed RoleMixin; neither Role nor Kind asserted; diagram stereotype roleMixin. External realization not checked.',
 'FAP-007':'Responsibility directly subclasses Relator only; grounding/mediation cardinality not checked.',
 'FAP-008':'Control typed RoleMixin; relatedMatch ROSE SecurityMechanism; no direct equivalence either direction. Other metatype assertions and specialization paths not checked.',
 'FAP-009':'Vulnerability direct IntrinsicMode; PredisposingCondition direct Situation; explicit disjointness.',
 'FAP-010':'RiskState direct Situation; WorkflowState direct QualityValue; explicit disjointness.',
 'FAP-011':'LikelihoodResult directly subclasses Result and ArtifactVersion, not Quality. External equivalence and inferred typing not checked.',
 'FAP-015':'Exactly47 unique expected concept IDs; exactly11 helper IDs with exact declared local class IRIs; exactly7 boundary IDs; conceptual node IRIs match IDs. Edges, stereotypes, boundary IRIs and native model not checked.'}
 limitations={
 'FAP-001':'Asserted mapping/category check only; no general proof of Risk identity or all inferred equivalences.',
 'FAP-002':'Selected assertions/disjointness only; no independent domain-validation result.',
 'FAP-003':'Selected type levels only; no universal scenario identity or full description/event analysis.',
 'FAP-004':'Direct superclass check only; assessment-context adequacy is separate.',
 'FAP-005':'Historical Role wording is stale: rc.4 uses RoleMixin. External sortal realization remains open.',
 'FAP-006':'Owner reification/rule semantics require separately versioned execution evidence; not rerun here.',
 'FAP-007':'Relator superclass alone does not prove two grounded participants, temporal adequacy or mediation correctness.',
 'FAP-008':'No asserted ROSE equivalence; heterogeneous control realization remains separate.',
 'FAP-009':'Selected category/disjointness only; empirical susceptibility is not established.',
 'FAP-010':'Selected domain/value separation only; complete workflow temporal semantics remain separately tested.',
 'FAP-011':'Artifact subclass check only; no measurement validity or full likelihood semantics.',
 'FAP-012':'Global-versus-profile cardinality analysis requires restriction/property/shape review; not assessed by this subset.',
 'FAP-013':'No general causal non-entailment proof in this subset; no causal inference or observed effect established.',
 'FAP-014':'External bridge stereotype/version fidelity requires its own source audit; not inferred from local OWL.',
 'FAP-015':'Historical canonical-ID-only rule is stale: 47 conceptual,11 helper,7 boundary nodes are separate governed units. No native-editor round-trip or full semantic conformance.'}
 findings=[{'finding_id':r['finding_id'],'historical_status':r['recheck_status'],'historical_pattern':r['pattern'],'asserted_criterion':criteria.get(r['finding_id'],'No predicate in this subset'),'current_status':'PASS_ASSERTED_SUBSET_ONLY' if r['finding_id'] in result else 'NOT_ASSESSED_BY_THIS_SUBSET','full_antipattern_status':'NOT_ESTABLISHED','limitation':limitations[r['finding_id']]} for r in rows]
 sources={str(p):hashlib.sha256((ROOT/p).read_bytes()).hexdigest() for p in paths+[specpath,registry,legacy,Path('tools/check_current_antipattern_evidence.py'),Path('tools/generate_rc4_formal_reference.py')]}
 return {'candidate':'0.2.0-rc.4','baseline_commit':'88ef9e22feaf24ac1d9dffff3b0a23c714e7cfb4','scope':'Asserted local source regressions; no reasoning/native editor/full antipattern detector','historical_findings':15,'asserted_subset_checks':len(result),'deliberate_mutations_rejected':len(mutations)+5,'mutation_meaning':'Targeted predicate false or input-register validation error; not domain-record rejection','rdflib_version':rdflib.__version__,'full_antipattern_acceptance':'NOT_ESTABLISHED','findings':findings,'source_sha256':sources}
def main():
 p=argparse.ArgumentParser();p.add_argument('--write',action='store_true');a=p.parse_args();r=run();content=json.dumps(r,indent=2)+'\n';target=OUT/'results.json'
 if a.write:OUT.mkdir(parents=True,exist_ok=True);target.write_text(content)
 elif not target.exists() or target.read_text()!=content:raise ValueError('GENERATED_DRIFT')
 print('Python runtime: '+sys.version.split()[0]);print(json.dumps({k:v for k,v in r.items() if k not in ['findings','source_sha256']},indent=2))
if __name__=='__main__':main()
