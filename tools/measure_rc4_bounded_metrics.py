#!/usr/bin/env python3
"""Four preselected asserted diagnostics, domain/helper populations kept separate."""
import argparse,csv,hashlib,io,json,platform,sys,tempfile,shutil
from pathlib import Path
from rdflib import Graph,URIRef,BNode,Literal,Namespace,__version__ as RDFLIB_VERSION
from rdflib.namespace import RDF,RDFS,OWL
from generate_rc4_formal_reference import closure,ROOT,RELEASE
OUT=Path('evaluation/oquare/rc4-bounded')
PROTOCOL_COMMIT='7a7f50bd699985faf5e2136b9daf2d35dabe1e7b'
METRICS=['TMOnto_asserted_scoped','ANOnto_assertion_density_scoped','Local_nonempty_label_coverage','Local_nonempty_comment_coverage']

def digest(data):return hashlib.sha256(data).hexdigest()
def member_hash(pop):return digest(('\n'.join(sorted(map(str,pop)))+'\n').encode())
def verify_bindings(bindings,root=ROOT):
 for path,expected in bindings['source_sha256'].items():
  if digest((root/path).read_bytes())!=expected:raise ValueError('SOURCE_HASH_DRIFT: '+path)

def local_union(graphs,root=ROOT):
 g=Graph()
 for path,graph in graphs.items():
  if path.parent==(root/RELEASE).resolve():g+=graph
 return g

def populations(g,d,h):
 declared={s for s in g.subjects(RDF.type,OWL.Class) if str(s).startswith('urn:semrisk:')}
 if d & h:raise ValueError('POPULATION_OVERLAP')
 if not d|h <= declared:raise ValueError('MISSING_REGISTRY_CLASS')
 if declared != d|h:raise ValueError('UNEXPECTED_LOCAL_CLASS')

def measure(g,pop):
 n=len(pop);multi=sum(len({o for o in g.objects(c,RDFS.subClassOf) if isinstance(o,URIRef)})>1 for c in pop)
 annotations=sum(1 for c in pop for p in [RDFS.label,RDFS.comment] for o in g.objects(c,p))
 missing={str(p):sorted(str(c) for c in pop if not any(isinstance(o,Literal) and str(o).strip() for o in g.objects(c,p))) for p in [RDFS.label,RDFS.comment]}
 nums=[multi,annotations,n-len(missing[str(RDFS.label)]),n-len(missing[str(RDFS.comment)])];dens=[n-1,n,n,n];out={}
 for i,id in enumerate(METRICS):
  undefined=(n<2 if i==0 else n==0)
  out[id]={'formula_version':1,'numerator':nums[i],'denominator':dens[i],'value':None if undefined else nums[i]/dens[i],'status':('UNDEFINED_POPULATION_LT_2' if i==0 else 'UNDEFINED_EMPTY_POPULATION') if undefined else 'COMPUTED_RAW','population_size':n,'member_list_sha256':member_hash(pop)}
 out[METRICS[2]]['missing_classes']=missing[str(RDFS.label)];out[METRICS[3]]['missing_classes']=missing[str(RDFS.comment)]
 return out

def synthetic_tests(bindings):
 tests=[];EX=Namespace('urn:semrisk:metric-test:');d={EX.a,EX.b,EX.c};h={EX.helper};g=Graph()
 for c in d|h:g.add((c,RDF.type,OWL.Class));g.add((c,RDFS.label,Literal(str(c).split(':')[-1])));g.add((c,RDFS.comment,Literal('Meaningful fixture description')))
 g.add((EX.a,RDFS.subClassOf,EX.parent));g.add((EX.b,RDFS.subClassOf,EX.parent));g.add((EX.b,RDFS.subClassOf,EX.other))
 original=set(g);base=measure(g,d)
 def clone():z=Graph();z+=g;return z
 def test(name,ok):
  if not ok:raise AssertionError(name)
  tests.append({'id':name,'result':'PASS'})
 def val(m,i):return m[METRICS[i]]['value']
 test('BASE_EXPECTED', [val(base,i) for i in range(4)]==[.5,2,1,1])
 z=clone();z.add((EX.a,RDFS.subClassOf,EX.third));m=measure(z,d);test('SECOND_PARENT',val(m,0)==1 and all(m[METRICS[i]]==base[METRICS[i]] for i in range(1,4)))
 z=clone();z.add((EX.b,RDFS.subClassOf,EX.third));test('THIRD_PARENT_BLIND_SPOT',measure(z,d)==base)
 z=clone();z.add((EX.a,RDFS.subClassOf,BNode()));z.add((EX.a,RDF.type,URIRef('http://purl.org/nemo/gufo#Kind')));test('ANONYMOUS_AND_METATYPE_EXCLUDED',measure(z,d)==base)
 for p,i in [(RDFS.label,2),(RDFS.comment,3)]:
  z=clone();z.remove((EX.a,p,None));m=measure(z,d);test('REMOVE_ONLY_'+str(p).split('#')[-1].upper(),val(m,i)==2/3 and val(m,1)==5/3)
 z=clone();z.add((EX.a,RDFS.comment,Literal('Another useful explanation')));m=measure(z,d);test('DENSITY_NOT_COVERAGE',val(m,1)==7/3 and val(m,3)==1)
 z=clone();z.remove((EX.a,RDFS.label,None));z.add((EX.a,RDFS.label,Literal('   ')));z.add((EX.a,RDFS.label,EX.label));m=measure(z,d);test('EMPTY_URI_INFLATION',val(m,1)==7/3 and val(m,2)==2/3)
 z=clone();z.set((EX.a,RDFS.comment,Literal('nonsense xyz')));test('NONSENSE_BLIND_SPOT',measure(z,d)==base)
 z=clone();z.add((EX.a,RDFS.label,Literal('a')));test('DUPLICATE_COLLAPSE',measure(z,d)==base)
 z=clone();z.add((URIRef('http://example.org/vendor'),RDFS.comment,Literal('Imported')));test('IMPORTED_ANNOTATION_EXCLUDED',measure(z,d)==base)
 imported=Graph();imported.add((EX.a,RDFS.comment,Literal('Imported annotation about a measured local class')));imported.add((EX.a,RDFS.subClassOf,EX.importedParent))
 scoped=local_union({(ROOT/RELEASE/'core.ttl').resolve():g,(ROOT/'ontology/vendor/fixture.ttl').resolve():imported});test('IMPORTED_FILE_LOCAL_SUBJECT_EXCLUDED',measure(scoped,d)==base)
 z=clone();z.add((EX.helper,RDFS.comment,Literal('Extra helper detail')));test('HELPER_SEPARATION',measure(z,d)==base and measure(z,h)!=measure(g,h))
 empty=measure(g,set());one=measure(g,{EX.a});test('EMPTY_UNDEFINED',all(empty[id]['value'] is None for id in METRICS));test('SINGLETON_UNDEFINED_TANGLE',one[METRICS[0]]['value'] is None and one[METRICS[1]]['value']==2)
 for name,mutate,marker in [('MISSING_REGISTRY_CLASS',lambda z:z.remove((EX.a,RDF.type,OWL.Class)),'MISSING_REGISTRY_CLASS'),('UNEXPECTED_LOCAL_CLASS',lambda z:z.add((EX.extra,RDF.type,OWL.Class)),'UNEXPECTED_LOCAL_CLASS')]:
  z=clone();mutate(z)
  try:populations(z,d,h)
  except ValueError as e:test(name,marker in str(e))
  else:raise AssertionError(name)
 bad=json.loads(json.dumps(bindings));bad['source_sha256'][next(iter(bad['source_sha256']))]='0'*64
 try:verify_bindings(bad)
 except ValueError as e:test('SOURCE_HASH_REJECTED','SOURCE_HASH_DRIFT' in str(e))
 else:raise AssertionError('source drift accepted')
 with tempfile.TemporaryDirectory(prefix='semrisk-metric-import-') as td:
  root=Path(td)
  for path in bindings['source_sha256']:
   dest=root/path;dest.parent.mkdir(parents=True,exist_ok=True);shutil.copyfile(ROOT/path,dest)
  p=root/RELEASE/'catalog.xml';p.write_text(p.read_text().replace('http://purl.org/nemo/gufo#/1.0.0','urn:unbound:vendor'))
  try:closure(root)
  except ValueError as e:test('UNBOUND_IMPORT_REJECTED','UNBOUND_IMPORT' in str(e))
  else:raise AssertionError('unbound import accepted')
 test('FIXTURE_RESTORED',set(g)==original);verify_bindings(bindings)
 return tests

def inputs():
 bindings=json.loads((ROOT/OUT/'input-bindings.json').read_text());verify_bindings(bindings)
 graphs=closure();g=local_union(graphs)
 d={URIRef(r['iri']) for r in csv.DictReader((ROOT/RELEASE/'conceptual-iri-register.csv').open()) if r['kind']=='concept' and r['formal_status']=='LOCAL_CLASS'}
 h=set()
 for file in ['profile-iri-registry.csv','information-state-iri-registry.csv']:
  h|={URIRef(r['iri']) for r in csv.DictReader((ROOT/RELEASE/file).open()) if r['kind'].lower()=='class'}
 populations(g,d,h)
 return bindings,g,d,h

def build():
 if RDFLIB_VERSION!='7.6.0':raise ValueError('PINNED_RDFLIB_REQUIRED')
 bindings,g,d,h=inputs()
 tests=synthetic_tests(bindings) # Protocol-fixed fixtures run BEFORE candidate calculation.
 results={name:measure(g,pop) for name,pop in [('domain',d),('helpers',h)]}
 rows=[]
 for name,pop in [('domain',d),('helpers',h)]:
  for c in sorted(pop,key=str):
   def terms(p):return [dict(kind='literal' if isinstance(o,Literal) else 'iri' if isinstance(o,URIRef) else 'blank',value=str(o),language=o.language if isinstance(o,Literal) else None,datatype=str(o.datatype) if isinstance(o,Literal) and o.datatype else None) for o in sorted(g.objects(c,p),key=lambda o:o.n3())]
   rows.append({'population':name,'iri':str(c),'direct_named_parents':json.dumps(sorted(str(o) for o in g.objects(c,RDFS.subClassOf) if isinstance(o,URIRef))),'labels':json.dumps(terms(RDFS.label),ensure_ascii=False),'comments':json.dumps(terms(RDFS.comment),ensure_ascii=False)})
 f=io.StringIO();w=csv.DictWriter(f,fieldnames=list(rows[0]),lineterminator='\n');w.writeheader();w.writerows(rows)
 report={'candidate':'0.2.0-rc.4','source_commit':bindings['source_commit'],'protocol_commit':PROTOCOL_COMMIT,'protocol_sha256':digest((ROOT/OUT/'protocol.md').read_bytes()),'script_sha256':digest(Path(__file__).read_bytes()),'scope_clarification_sha256':digest((ROOT/OUT/'scope-clarification.md').read_bytes()),'excluded_external_declarations':sorted(str(c) for c in g.subjects(RDF.type,OWL.Class) if not str(c).startswith('urn:semrisk:')),'rdflib_version':RDFLIB_VERSION,'scope':'Seven local asserted module union; import closure bound but imported classes/annotations excluded from populations','populations':{'domain':sorted(map(str,d)),'helpers':sorted(map(str,h))},'results':results,'synthetic_tests':tests,'source_sha256':bindings['source_sha256'],'overall_quality_score':None,'scale_bands':'NOT_APPLIED','limits':['Two OQuaRE-style local operationalizations; two local documentation-presence diagnostics','TMOnto root-subtraction convention is a limitation of the scoped adaptation','Nonempty comments can be nonsense; scores do not establish semantic adequacy','No official Java engine, full OQF adoption, domain-expert validation or SQL parity claim']}
 lines=['# rc.4 bounded metric results','','Protocol commit: `'+PROTOCOL_COMMIT+'`; source commit: `'+bindings['source_commit']+'`. The protocol was recorded before the new calculation, with historical pilot and inventory counts already known.','','| Population | Diagnostic | Numerator | Denominator | Raw value |','| --- | --- | ---: | ---: | ---: |']
 for name,metrics in results.items():
  for id,m in metrics.items():lines.append(f"| {name} | {id} | {m['numerator']} | {m['denominator']} | {m['value']} |")
 lines+=['','All results are descriptive and scope-bound. Domain and helper rows are not pooled. Zero coverage, if observed, means missing nonempty annotations under the declared local rule, not absence of semantics or a command to fabricate documentation. The class ledger exposes missing values and all counted assertions.','',str(len(tests))+' protocol-derived synthetic/sensitivity checks passed before each candidate calculation (including added source-boundary hardening). The third-parent and nonsense-comment tests deliberately demonstrate insensitivity. No one-to-five bands or aggregate score is produced.','', 'Reproduce: `python tools/measure_rc4_bounded_metrics.py --check`. Existing P1-R2 pilot bytes are unchanged. Full CQ/SQL reevaluation, broader P07/P09 acceptance and scholarly publication remain separate.']
 return {'results.json':json.dumps(report,indent=2,ensure_ascii=False,allow_nan=False)+'\n','class-evidence.csv':f.getvalue(),'results.md':'\n'.join(lines)+'\n'}

def check_outputs(outputs,actual):
 for name,value in outputs.items():
  if actual.get(name)!=value:raise ValueError('GENERATED_RESULT_DRIFT: '+name)

def main():
 p=argparse.ArgumentParser();p.add_argument('--check',action='store_true');a=p.parse_args();outputs=build()
 bad=dict(outputs);bad['results.json']=bad['results.json']+' '
 try:check_outputs(outputs,bad)
 except ValueError as e:assert 'GENERATED_RESULT_DRIFT' in str(e)
 else:raise AssertionError('generated drift accepted')
 if a.check:check_outputs(outputs,{name:(ROOT/OUT/name).read_text() for name in outputs})
 else:
  for name,value in outputs.items():(ROOT/OUT/name).write_text(value)
 report=json.loads(outputs['results.json']);print(json.dumps({'result':'PASS_BOUNDED_RAW_METRICS','synthetic_tests':len(report['synthetic_tests']),'generated_drift_rejection':True,'python':platform.python_version(),'rdflib':RDFLIB_VERSION,'results':report['results'],'limits':report['limits']},indent=2))
if __name__=='__main__':main()
