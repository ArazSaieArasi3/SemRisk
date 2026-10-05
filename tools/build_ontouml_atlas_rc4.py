#!/usr/bin/env python3
"""Build a source-bound editable OntoUML model and DOT view specifications.
Unclassified boundary nodes are intentionally explicit, not fabricated stereotypes.
"""
import csv,json,hashlib,re,html,argparse
from pathlib import Path
from rdflib import Graph,RDF,RDFS,OWL,Namespace,URIRef
ROOT=Path(__file__).resolve().parents[1];V='0.2.0-rc.4';OUT=ROOT/'diagrams/ontouml'/V
SR=Namespace('urn:semrisk:entity:');AC=Namespace('urn:semrisk:profile:assessment-context:');IS=Namespace('urn:semrisk:profile:information-state:');GUFO=Namespace('http://purl.org/nemo/gufo#');SH=Namespace('http://www.w3.org/ns/shacl#')
DATE='2026-10-05T00:00:00Z'
def lang(s):return {'en':s} if s else None
def c(n):return f'SR-CPT-{n:03}'
def named(id,type,name,description=''):
 return dict(id=id,type=type,name=lang(name),description=lang(description),alternativeNames=[],editorialNotes=[],creators=[],contributors=[],created=DATE,modified=DATE,customProperties={})
def build():
 g=Graph()
 for p in sorted((ROOT/'ontology/releases'/V).glob('*.ttl')):g.parse(p)
 audit=list(csv.DictReader((ROOT/f'foundational/exposure-scale-v{V}/concept-category-audit.csv').open()))
 rels=list(csv.DictReader((ROOT/f'foundational/exposure-scale-v{V}/relation-formal-audit.csv').open()))
 elems=[];nodes={};edges={};byiri={};members={}
 def node(id,label,stereo,status,iri=None,definition='',order='1',attrs=None):
  nature={'kind':'functional-complex','subkind':'functional-complex','role':'functional-complex','relator':'relator','mode':'intrinsic-mode','event':'event','situation':'situation','abstract':'abstract','enumeration':'abstract','type':'type'}.get(stereo)
  n=named(id,'Class',label,definition);n.update(stereotype=stereo,isDerived=False,isAbstract=stereo in ['roleMixin','category'],properties=[],literals=[],restrictedTo=[nature] if nature else [],isPowertype=False,order=order)
  n['customProperties']=dict(sourceIRI=iri,scopeStatus=status,stereotypeBasis='Candidate semantics and Run 6 identity decisions plus Run 8 scale specialization' if stereo else 'Deliberately unclassified boundary; not a completed OntoUML classification')
  nodes[id]=dict(id=id,label=label,stereotype=stereo,status=status,iri=iri,attributes=attrs or []);elems.append(n)
  if iri:byiri[iri]=id
 for r in audit:
  local=r['formal_status']=='LOCAL_CLASS';st=r['ontouml_stereotype_if_supported'] or None
  status='implemented' if local and st else 'pattern boundary' if local else 'external reference' if r['formal_status']=='EXTERNAL_OR_PATTERN_MARKER' else 'planned / external'
  node(r['semantic_id'],r['term'],st,status,str(SR[r['semantic_id']]),r['definition'],order='2' if st=='type' else '1')
 # All 11 operational helper classes; NumericScale is deliberately not promoted to a kind.
 helpers={'QualifiedAssessmentResult':('Qualified Assessment Result','subkind',AC),'GroundedRiskResponsibility':('Grounded Responsibility','relator',AC),'NumericScale':('Numeric Scale Version','subkind',AC),'Dimension':('Assessment Dimension','enumeration',AC),'ControlBaseline':('Control Baseline','enumeration',AC),'EvaluationBasis':('Evaluation Basis','enumeration',AC),'ManagedInformationArtifact':('Managed Information Artifact','kind',IS),'ArtifactVersion':('Artifact Version','subkind',IS),'InformationContent':('Information Content','abstract',IS),'WorkflowSchemeVersion':('Workflow Scheme Version','subkind',IS),'WorkflowAssignment':('Workflow Assignment','situation',IS)}
 for name,(label,st,ns) in helpers.items():
  id='H-'+name;node(id,label,st,'profile helper' if st else 'unclassified OWL helper',str(ns[name]),str(g.value(ns[name],RDFS.comment) or 'Operational helper, counted separately from the domain inventory.'))
  enum=g.value(ns[name],OWL.oneOf)
  if enum:
   vals=list(g.items(enum));members[id]=[str(x).split(':')[-1] for x in vals]
   for val in vals:
    lid='L-'+str(val).split(':')[-1];lit=named(lid,'Literal',str(val).split(':')[-1]);elems.append(lit);next(x for x in elems if x['id']==id)['literals'].append(lid)
 # Explicit conceptual boundaries for broad property endpoints; no invented OWL entities.
 for id,label,st in [('B-Endurant','Endurant (external)','category'),('B-Context','Risk-chain entity',None),('B-Affected','Affected external entity',None),('B-Actor','External Actor',None),('B-Pharma','External pharma entity',None),('B-Profile','Profile concept',None),('B-Core','Core concept',None)]:
  node(id,label,st,'external category' if st else 'endpoint boundary',str(GUFO.Endurant) if st else None,'A diagram boundary, not a newly adopted SemRisk class.')
  if id=='B-Endurant':next(e for e in elems if e['id']==id)['restrictedTo']=['functional-complex','collective','quantity','relator','intrinsic-mode','extrinsic-mode','quality']
 def edge(id,source,target,label,st=None,sm='0..*',tm='0..*',basis='No global cardinality bound asserted; 0..* is deliberately unconstrained.',kind='association',iri=None):
  edges[id]=dict(id=id,source=source,target=target,label=label,stereotype=st,source_cardinality=sm,target_cardinality=tm,basis=basis,kind=kind,iri=iri)
  if kind=='generalization':
   e=named(id,'Generalization',label,basis);e.update(specific=source,general=target);elems.append(e);return
  # Metadata is carried as a Note, not mislabeled an OWL property.
  if kind=='metadata':
   e=named(id,'Note',label,basis);e['text']=lang(label+'; '+basis);elems.append(e);return
  e=named(id,'BinaryRelation',label,basis);e.update(stereotype=st,isDerived=id.startswith('SR-REL-026'),isAbstract=False,properties=[id+'-source',id+'-target']);e['customProperties']=dict(sourceIRI=iri,multiplicityBasis=basis);elems.append(e)
  for suffix,typ,card in [('source',source,sm),('target',target,tm)]:
   q=named(id+'-'+suffix,'Property',suffix);q.update(stereotype=None,isDerived=False,subsettedProperties=[],redefinedProperties=[],aggregationKind='NONE',cardinality=card,isOrdered=False,isReadOnly=False,propertyType=typ);elems.append(q)
 # Scoped typed projections retain one source relation ID even when rendered more than once.
 pairs={1:([33,34],[1]),2:([34],[6]),3:([6],[7]),4:([6,7],[8]),5:([1,6],[3]),6:([6,7],[4]),7:([7],[5]),8:(['B-Context'],['B-Context']),9:(['B-Context'],['B-Context']),10:([1,7,8],['B-Affected']),11:([3,4],[2]),12:([2],[9]),13:([11],[1]),14:([11],[12]),15:([11],[13]),16:([13],[1]),17:([11,13,20],[20]),18:([23],[22]),19:(['H-ManagedInformationArtifact'],[21]),20:([13],[19]),21:([1,33],[26]),22:([27],[26]),23:([28],[27]),24:([28],[29]),25:([29],['B-Affected']),26:([1,33],['B-Actor']),27:([31],[1,33,27]),28:([31],[30,'B-Actor']),29:([32],[33]),30:([33],[36]),31:([1],[35]),32:([35],[35]),33:([13],[13]),34:([11],[11,13]),35:([1,39],[24]),36:([24,12,44],[25]),37:([1,6,7,8],['B-Pharma']),38:(['B-Profile'],['B-Core']),39:([10],[2]),40:([10],[3])}
 for r in rels:
  n=int(r['relation_id'].split('-')[-1]);a,b=pairs[n]
  for i,s in enumerate(a):
   for j,t in enumerate(b):
    source=c(s) if isinstance(s,int) else s;target=c(t) if isinstance(t,int) else t
    id=r['relation_id']+(f'-view-{i+1}-{j+1}' if len(a)*len(b)>1 else '')
    basis='Scoped conceptual endpoint projection of '+r['relation_id']+'. 0..* imposes no global bound; closed-world profile constraints are drawn separately.'
    if n==38:basis='Registry extension metadata only; not a local OWL property or an OntoUML association.'
    if n==32:basis+=' Only Risk State ordering is drawn; workflow-value ordering is not temporal assignment ordering.'
    if n==10:basis+=' Affected entity covers Risk Subject, Objective, Capability and Business Process references without supplying their identity.'
    edge(id,source,target,r['label'],kind='metadata' if n==38 else 'association',basis=basis,iri=str(SR[r['relation_id']]) if n!=38 else None)
 # Every asserted named superclass between displayed entities is preserved, even redundant ones.
 for s,t in sorted(g.subject_objects(RDFS.subClassOf),key=lambda p:(str(p[0]),str(p[1]))):
  if str(s) in byiri and str(t) in byiri:edge('GEN-'+byiri[str(s)]+'-'+byiri[str(t)],byiri[str(s)],byiri[str(t)],'specializes',kind='generalization',basis='Asserted rdfs:subClassOf in the unchanged rc.3 source.')
 # All 11 helper object properties. Specific minima/maxima belong solely to these named profile views.
 helper_edges=[('dimension','H-QualifiedAssessmentResult','H-Dimension',AC,'1'),('controlBaseline','H-QualifiedAssessmentResult','H-ControlBaseline',AC,'1'),('evaluationBasis','H-QualifiedAssessmentResult','H-EvaluationBasis',AC,'1'),('method','H-QualifiedAssessmentResult',c(12),AC,'1'),('scale','H-QualifiedAssessmentResult','H-NumericScale',AC,'1'),('expressesContent','H-ArtifactVersion','H-InformationContent',IS,'1..*'),('versionOf','H-ArtifactVersion','H-ManagedInformationArtifact',IS,'1'),('inScheme',c(36),'H-WorkflowSchemeVersion',IS,'1'),('record','H-WorkflowAssignment',c(33),IS,'1'),('value','H-WorkflowAssignment',c(36),IS,'1'),('scheme','H-WorkflowAssignment','H-WorkflowSchemeVersion',IS,'1')]
 for name,s,t,ns,card in helper_edges:edge('HP-'+name,s,t,name,tm=card,basis='Explicit opt-in SHACL profile only; not an unconditional OWL cardinality.',iri=str(ns[name]))
 edge('HP-scale-dimension','H-NumericScale','H-Dimension','dimension',tm='1',basis='Numeric Scale SHACL ScaleShape requires exactly one dimension; opt-in profile only.',iri=str(AC.dimension))
 # Remaining eight helper properties are datatype attributes, not object associations.
 attrs={'H-QualifiedAssessmentResult':[('numericValue','decimal','1'),('methodVersion','string','1'),('assessedAt','dateTime','1'),('referenceTime','dateTime','1')],'H-GroundedRiskResponsibility':[('validFrom','dateTime','0..1'),('validTo','dateTime','0..1')],'H-NumericScale':[('minimum','decimal','1'),('maximum','decimal','1')],'H-WorkflowAssignment':[('validFrom','dateTime','1'),('validTo','dateTime','0..1')]}
 for id,arr in attrs.items():
  for name,typ,card in arr:
   aid=id+'-attr-'+name;a=named(aid,'Property',name,'Qualified data-profile attribute; datatype '+typ);a.update(stereotype=None,isDerived=False,subsettedProperties=[],redefinedProperties=[],aggregationKind='NONE',cardinality=card,isOrdered=False,isReadOnly=False,propertyType=None);a['customProperties']={'sourceIRI':str(AC[name]),'datatype':typ};elems.append(a);next(e for e in elems if e['id']==id)['properties'].append(aid);nodes[id]['attributes'].append(f'{name}: {typ} [{card}]')
 # Actual gufo mediation is shown only in the opt-in named-participant profile.
 edge('HP-mediates','H-GroundedRiskResponsibility','B-Endurant','mediates',st='mediation',tm='2..*',basis='Grounded responsibility SHACL: at least two named, explicitly distinct Endurants; Risk is an aboutness target.',iri=str(GUFO.mediates))
 for id,vals in members.items():nodes[id]['attributes']+=vals
 views=[]
 def view(id,title,numbers,rel_numbers=(),extra=(),gen=False,note=''):
  ids={c(n) if isinstance(n,int) else n for n in numbers};chosen=[]
  for eid,e in edges.items():
   if (eid.startswith('SR-REL-') and int(eid.split('-')[2]) in rel_numbers and e['source'] in ids and e['target'] in ids) or eid in extra or (gen and e['kind']=='generalization' and e['source'] in ids and e['target'] in ids):chosen.append(eid);ids|={e['source'],e['target']}
  views.append(dict(id=id,title=title,nodes=sorted(ids),edges=chosen,note=note))
 view('01-scenario','Scenario, description and occurrence',[6,34,7,5,8,4,3], [2,3,4,5,6,7],note='Scenario is a second-order type; realization does not follow merely from its existence.')
 view('02-risk-context','Risk patterns and situational context',[1,2,3,4,9,10,35],[5,11,12,31,32,39,40],note='Orange nodes are broad patterns. Exposure now has registered subject/source links; endpoint existence does not entail a risk score or outcome.')
 view('03-assessment','Assessment activity and result distinctions',[11,12,13,14,15,16,17,18,19],[14,15,20,33,34],gen=True,note='Dimension and control-baseline subkinds may overlap. The ontology does not impose a universal score formula.')
 view('04-evidence','Observation, evidence and monitoring',[11,13,20,21,22,23,24,25,'H-ManagedInformationArtifact'],[17,18,19,36],gen=True,note='Evidence is a contextual role. Provenance is an external pattern reference; supporting evidence does not establish truth.')
 view('05-treatment','Treatment specification and execution',[26,27,28,29,1,33,'B-Affected'],[21,22,23,24,25],note='Plan, strategy, activity and control remain distinct. A control association does not prove effectiveness.')
 view('06-responsibility','Responsibility and explicit grounding',[31,30,1,33,27,'B-Actor','B-Endurant','H-GroundedRiskResponsibility'],[26,27,28],extra=['HP-mediates'],gen=True,note='Green profile mediation needs distinct Endurants. External Actor identity is not supplied locally; Risk Owner has no new sortal identity.')
 view('07-register','Register, description and workflow snapshot',[32,33,34,6,36,1],[1,2,29,30],note='Unqualified hasWorkflowState is a snapshot; use the separate qualified workflow view for historical answers.')
 view('08-information','Managed artifacts, versions and content',['H-ManagedInformationArtifact','H-ArtifactVersion','H-InformationContent',12,19,20,23,24,25,26,27,32,33,34],extra=['HP-versionOf','HP-expressesContent'],gen=True,note='Version/content multiplicities are strict data-profile requirements. Shared content does not merge artifact identity.')
 view('09-result-identity','Result inheritance and qualified profile',[13,14,15,16,17,18,'H-ArtifactVersion','H-QualifiedAssessmentResult'],gen=True,note='All shown named subclass axioms are asserted in rc.3; no new disjointness between independent result dimensions.')
 view('10-qualified-assessment','Qualified numeric assessment profile',['H-QualifiedAssessmentResult','H-NumericScale','H-ArtifactVersion','H-Dimension','H-ControlBaseline','H-EvaluationBasis',12],extra=['HP-scale-dimension','HP-dimension','HP-controlBaseline','HP-evaluationBasis','HP-method','HP-scale'],gen=True,note='Opt-in SHACL profile. Numeric Scale Version inherits ArtifactVersion identity; equal intervals do not merge versions.')
 view('11-workflow','Scheme-qualified temporal workflow',[33,36,'H-WorkflowAssignment','H-WorkflowSchemeVersion','H-ArtifactVersion'],extra=['HP-record','HP-value','HP-scheme','HP-inScheme'],gen=True,note='Exactly one record/value/scheme per assignment. Half-open intervals; no overlap for the same record and scheme.')
 view('12-federation','Enterprise and pharmaceutical references',[1,6,7,8,'B-Affected','B-Pharma'],[10,37],note='External endpoint references preserve their own identity. No invented CM-PharmE equivalence or asserted global domain.')
 view('13-generic','Generic relations and extension metadata',['B-Context','B-Profile','B-Core'],[8,9,38],note='A generic association is not causality. Dashed extension is registry metadata, not an OWL property.')
 view('14-assessment-context','Assessment context and indicator links',[1,11,13,24,25,12,39,44],[13,16,35,36],note='These typed endpoint projections do not narrow globally open property domains. External and planned concepts stay distinct.')
 view('15-external-boundaries','External references and planned concepts',[21,37,38,39,40,41,42,43,44,45,46,47],note='Twelve reference slots: four registry markers and eight undeclared candidates. No implied implementation or equivalence.')
 # Ensure every modeled edge is rendered; missed cross-view links get an explicit final view.
 seen={e for v in views for e in v['edges']};miss=sorted(set(edges)-seen)
 if miss:
  ids={edges[e][k] for e in miss for k in ['source','target']};view('16-cross-view','Cross-view relations and inheritance',ids,extra=miss,note='Cross-view links share the same stable model elements; they are not additional domain concepts.')
 project=named('SemRisk-rc4-project','Project','SemRisk complete candidate diagram package','OntoUML-based editable model with explicitly unclassified pattern and external boundaries; no claim of complete UFO validation.')
 project.pop('customProperties');project.update(elements=elems,root='root-package',publisher=None,designedForTasks=[],license=None,accessRights=[],themes=[],contexts=[],ontologyTypes=[],representationStyle=None,namespace='urn:semrisk:diagram:rc4:',landingPages=['https://github.com/ArazSaieArasi3/SemRisk'],sources=['https://github.com/OntoUML/ontouml-schema'],bibliographicCitations=[],keywords=[],acronyms=['SemRisk'],languages=['en'])
 package=named('root-package','Package','SemRisk 0.2.0-rc.4');package['contents']=[e['id'] for e in elems if e['type'] in ['Class','BinaryRelation','Generalization','Note']];elems.append(package)
 spec=dict(version=V,baseline_commit='6d619c5bbcb3532d68e250e2c27a9a3232fd06f9',nodes=nodes,edges=edges,views=views,enumerations=members,limits=['Unclassified broad patterns and external endpoints are intentional','RoleMixin external sortal specializations remain outside this core','Not a complete OntoUML antipattern detector','Full atlas is supplementary; IEEE fit is measured separately'])
 OUT.mkdir(parents=True,exist_ok=True)
 (OUT/'model-base.json').write_text(json.dumps(project,indent=2)+'\n');(OUT/'view-spec.json').write_text(json.dumps(spec,indent=2)+'\n')
 # Model names have no semantic codes; IDs remain in traceability files.
 for v in views:
  lines=['digraph G {','graph [rankdir=TB, bgcolor="white", pad="0.3", nodesep="0.42", ranksep="0.65", splines=polyline, outputorder=edgesfirst];','node [shape=plain, fontname="Helvetica", fontsize=14];','edge [fontname="Helvetica", fontsize=11, color="#526477", arrowsize=0.65];']
  for id in v['nodes']:
   n=nodes[id];st=n['stereotype'];color='#e7f2fc' if n['status'] in ['implemented','external category'] else '#e8f5f0' if n['status']=='profile helper' else '#fff0cf' if n['status'] in ['pattern boundary','unclassified OWL helper'] else '#f0e9fb'
   tag=f'«{st}»' if st else n['status'].upper()
   label='<TABLE BORDER="1" CELLBORDER="0" CELLSPACING="0" CELLPADDING="7" COLOR="#40546c" BGCOLOR="'+color+'"><TR><TD><FONT POINT-SIZE="11">'+html.escape(tag)+'</FONT></TD></TR><TR><TD><B>'+html.escape(n['label']).replace(' Assessment ',' Assessment<BR/>').replace(' Information ',' Information<BR/>')+'</B></TD></TR>'
   if n['attributes']:label+='<TR><TD ALIGN="LEFT"><FONT POINT-SIZE="10">'+'<BR ALIGN="LEFT"/>'.join(map(html.escape,n['attributes']))+'</FONT></TD></TR>'
   label+='</TABLE>';lines.append(json.dumps(id)+' [label=<'+label+'>];')
  if v['id']=='15-external-boundaries':
   ids=v['nodes']
   for j in range(0,len(ids),3):lines.append('{rank=same; '+ '; '.join(json.dumps(x) for x in ids[j:j+3])+';}')
   for j in range(len(ids)-3):lines.append(json.dumps(ids[j])+' -> '+json.dumps(ids[j+3])+' [style=invis, weight=100];')
  for eid in v['edges']:
   e=edges[eid];s=json.dumps(e['source']);t=json.dumps(e['target']);opts=[]
   if e['kind']=='generalization':opts=['arrowhead=empty','color="#34465d"']
   elif e['kind']=='metadata':opts=['style=dashed','arrowhead=vee','label="'+e['label']+'\\n[metadata]"']
   else:
    lab=('«'+e['stereotype']+'»\\n' if e['stereotype'] else '')+('/' if eid.startswith('SR-REL-026') else '')+e['label']
    opts=['arrowhead=none','label="'+lab+'"','taillabel="'+e['source_cardinality']+'"','headlabel="'+e['target_cardinality']+'"','labeldistance=1.8']
    if eid.startswith('HP-'):opts+=['color="#147e74"','fontcolor="#147e74"']
   if eid=='SR-REL-008':opts+=['tailport=n','headport=n']
   if eid=='SR-REL-009':opts+=['tailport=s','headport=s']
   opts+=['id='+json.dumps(eid)];lines.append(f'{s} -> {t} [{", ".join(opts)}];')
  lines.append('}');(OUT/'views'/f"{v['id']}.dot").write_text('\n'.join(lines)+'\n')
 # Trace exact entities and property coverage; multiple scoped projections do not increase registered relation counts.
 with (OUT/'concept-coverage.csv').open('w',newline='') as f:
  w=csv.DictWriter(f,fieldnames=['semantic_id','term','formal_status','diagram_status','stereotype','views']);w.writeheader()
  for r in audit:w.writerow(dict(semantic_id=r['semantic_id'],term=r['term'],formal_status=r['formal_status'],diagram_status=nodes[r['semantic_id']]['status'],stereotype=nodes[r['semantic_id']]['stereotype'] or '',views=';'.join(v['id'] for v in views if r['semantic_id'] in v['nodes'])))
 with (OUT/'relation-coverage.csv').open('w',newline='') as f:
  w=csv.DictWriter(f,fieldnames=['relation_id','name','status','model_edges','views']);w.writeheader()
  for r in rels:
   ids=[e for e in edges if e==r['relation_id'] or e.startswith(r['relation_id']+'-view-')];w.writerow(dict(relation_id=r['relation_id'],name=r['label'],status=r['formal_status'],model_edges=';'.join(ids),views=';'.join(v['id'] for v in views if set(ids)&set(v['edges']))))
 with (OUT/'multiplicity-evidence.csv').open('w',newline='') as f:
  w=csv.DictWriter(f,fieldnames=['edge_id','source','target','source_cardinality','target_cardinality','basis']);w.writeheader()
  for e in edges.values():
   if e['kind']=='association':w.writerow({k:e[k] for k in w.fieldnames if k!='edge_id'}|{'edge_id':e['id']})
 print(json.dumps(dict(nodes=len(nodes),model_edges=len(edges),views=len(views),concepts=len(audit),registered_relations=len(rels)),indent=2))
if __name__=='__main__':build()
