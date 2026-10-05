#!/usr/bin/env python3
"""Bounded diagram integrity checks; not a full OntoUML antipattern reasoner."""
import copy,csv,json,hashlib,re
from pathlib import Path
from xml.etree import ElementTree as ET
from jsonschema import Draft202012Validator
from pypdf import PdfReader
from rdflib import Graph,Namespace,URIRef
from build_ontouml_atlas_rc4 import ROOT,OUT

def require(ok,msg):
 if not ok:raise ValueError(msg)

def validate(project,spec):
 schema=json.loads((OUT/'vendor/ontouml-schema.json').read_text());validator=Draft202012Validator(schema)
 require(validator.is_valid(project),'project schema')
 elements=project['elements'];idx={e['id']:e for e in elements}
 require(len(idx)==len(elements),'duplicate IDs')
 for e in elements:
  ev=validator if e['type']!='Diagram' else Draft202012Validator({'$defs':schema['$defs'],'allOf':[{'$ref':'#/$defs/Diagram'},schema['$defs']['NamedElement']['allOf'][0],schema['$defs']['OntoumlElement']['allOf'][0]]})
  require(ev.is_valid(e),'element schema '+e['id'])
  for key in ['root','owner','isViewOf','rectangle','path','sourceView','targetView','specific','general','propertyType','note','element']:
   if e.get(key) is not None:require(e[key] in idx,'missing reference '+e['id']+' '+key)
  for key in ['contents','properties','literals','views','subsettedProperties','redefinedProperties']:
   for ref in e.get(key,[]):require(ref in idx,'missing member '+ref)
 for id,n in spec['nodes'].items():
  require(id in idx and idx[id]['type']=='Class','missing class '+id)
  require(idx[id]['stereotype']==n['stereotype'],'unsupported stereotype '+id)
 for id,e in spec['edges'].items():
  require(id in idx,'missing edge '+id);m=idx[id]
  if e['kind']=='association':
   require(m['type']=='BinaryRelation','association type '+id)
   for end,p in zip(['source','target'],m['properties']):
    require(idx[p]['propertyType']==e[end],'endpoint '+id)
    require(idx[p]['cardinality']==e[end+'_cardinality'],'cardinality '+id)
  elif e['kind']=='generalization':require((m['specific'],m['general'])==(e['source'],e['target']),'generalization direction '+id)
  else:require(m['type']=='Note','metadata is not association')
 for v in spec['views']:
  d=idx['D-'+v['id']];vv=[idx[x] for x in d['views']]
  require({x['isViewOf'] for x in vv if x['type']=='ClassView'}==set(v['nodes']),'view node coverage '+v['id'])
  require(set(v['edges'])<={x['isViewOf'] for x in vv},'view edge coverage '+v['id'])
  for x in vv:
   if x['type'] in ['GeneralizationView','BinaryRelationView']:
    e=spec['edges'][x['isViewOf']]
    require(idx[x['sourceView']]['isViewOf']==e['source'] and idx[x['targetView']]['isViewOf']==e['target'],'view direction')
  for x in vv:
   if x['type']=='ClassView':
    shape=idx[x['rectangle']];require(shape['width']>0 and shape['height']>0,'empty rectangle')
 return len(elements)

def main():
 project=json.loads((OUT/'SemRisk-rc4.ontouml.json').read_text());spec=json.loads((OUT/'view-spec.json').read_text());checks=[]
 def check(name,fn):fn();checks.append({'check':name,'result':'PASS'})
 check('schema, reference integrity and source/view semantics',lambda:validate(project,spec))
 concepts=list(csv.DictReader((OUT/'concept-coverage.csv').open()));relations=list(csv.DictReader((OUT/'relation-coverage.csv').open()))
 audit=list(csv.DictReader((ROOT/'foundational/exposure-scale-v0.2.0-rc.4/concept-category-audit.csv').open()))
 ra=list(csv.DictReader((ROOT/'foundational/exposure-scale-v0.2.0-rc.4/relation-formal-audit.csv').open()))
 check('47 concepts, exact source registry IDs, all rendered',lambda:require(len(concepts)==47 and {x['semantic_id'] for x in concepts}=={x['semantic_id'] for x in audit} and all(x['views'] for x in concepts),'concept coverage'))
 check('40 relations, exact source registry IDs, all rendered',lambda:require(len(relations)==40 and {x['relation_id'] for x in relations}=={x['relation_id'] for x in ra} and all(x['views'] and x['model_edges'] for x in relations),'relation coverage'))
 check('all diagram nodes and model edges appear',lambda:require(set(spec['nodes'])=={n for v in spec['views'] for n in v['nodes']} and set(spec['edges'])=={e for v in spec['views'] for e in v['edges']},'orphan model elements'))
 def check_shape_bounds():
  g=Graph();SH=Namespace('http://www.w3.org/ns/shacl#');AC='urn:semrisk:profile:assessment-context:';IS='urn:semrisk:profile:information-state:'
  for f in ['assessment-context-v0.2.0-rc.1.ttl','semantic-identity-v0.2.0-rc.3.ttl','foundational-evidence-v0.2.0-rc.2.ttl']:g.parse(ROOT/'shapes'/f)
  sm={'H-QualifiedAssessmentResult':AC+'ResultShape','H-NumericScale':AC+'ScaleShape','H-ArtifactVersion':IS+'VersionShape','SR-CPT-036':IS+'ValueShape','H-WorkflowAssignment':IS+'AssignmentShape','H-GroundedRiskResponsibility':'urn:semrisk:shape:foundational-evidence:GroundedResponsibilityShape'}
  def bound(shape,iri):
   pp=[p for p in g.objects(URIRef(shape),SH.property) if g.value(p,SH.path)==URIRef(iri)];require(len(pp)==1,'missing shape path '+shape+' '+iri)
   lo=int(g.value(pp[0],SH.minCount) or 0);hi=g.value(pp[0],SH.maxCount);hi=str(hi) if hi is not None else '*'
   return str(lo) if str(lo)==hi else str(lo)+'..'+hi
  for e in spec['edges'].values():
   if e['id'].startswith('HP-'):require(e['target_cardinality']==bound(sm[e['source']],e['iri']),'SHACL object bound '+e['id'])
  idx={e['id']:e for e in project['elements']}
  for n in spec['nodes']:
   for aid in idx[n]['properties']:
    a=idx[aid];shape=AC+'ResponsibilityShape' if n=='H-GroundedRiskResponsibility' else sm[n]
    require(a['cardinality']==bound(shape,a['customProperties']['sourceIRI']),'SHACL datatype bound '+aid)
 check('helper cardinalities independently match actual SHACL shapes',check_shape_bounds)
 check('helper inventory: 11 classes, 11 local object properties, 8 datatype properties, 7 literals',lambda:require(sum(n.startswith('H-') for n in spec['nodes'])==11 and len({e['iri'] for e in spec['edges'].values() if e['id'].startswith('HP-') and e['id']!='HP-mediates'})==11 and len({e['customProperties']['sourceIRI'] for e in project['elements'] if e['type']=='Property' and e['propertyType'] is None})==8 and sum(e['type']=='Literal' for e in project['elements'])==7,'helper inventory'))
 metrics=json.loads((OUT/'render-metrics.json').read_text())
 check('review atlas 15 A3 landscape pages',lambda:require(len(PdfReader(OUT/'SemRisk-rc4-review-atlas.pdf').pages)==15 and all(abs(float(p.mediabox.width)-1190.55)<1 and abs(float(p.mediabox.height)-841.89)<1 for p in PdfReader(OUT/'SemRisk-rc4-review-atlas.pdf').pages),'PDF dimensions'))
 check('minimum review font 7 pt; honest IEEE fit status',lambda:require(metrics['minimum_review_font_pt']>=7 and metrics['full_master_IEEE_170mm']=='FAIL_READABILITY','readability'))
 check('draw.io has all 15 diagrams',lambda:require(len(ET.parse(OUT/'SemRisk-rc4.drawio').getroot().findall('diagram'))==15,'drawio pages'))
 manifest=json.loads((OUT/'source-manifest.json').read_text())
 check('exact bound source hashes',lambda:require(all(hashlib.sha256((ROOT/p).read_bytes()).hexdigest()==h for p,h in manifest['sha256'].items()),'source hash mismatch'))
 # Fault injections ensure the checker rejects six material classes of corruption.
 mutations=[('missing concept',lambda p:p['elements'].__setitem__(slice(None),[e for e in p['elements'] if e['id']!='SR-CPT-010'])),('missing relation',lambda p:p['elements'].__setitem__(slice(None),[e for e in p['elements'] if e['id']!='SR-REL-002'])),('invented stereotype',lambda p:next(e for e in p['elements'] if e['id']=='SR-CPT-001').update(stereotype='riskPattern')),('guessed cardinality',lambda p:next(e for e in p['elements'] if e['id']=='SR-REL-002-target').update(cardinality='1')),('broken view reference',lambda p:next(e for e in p['elements'] if e['type']=='ClassView').update(isViewOf='NONEXISTENT')),('reversed generalization',lambda p:next(e for e in p['elements'] if e['type']=='Generalization').update(specific='SR-CPT-001'))]
 for label,mut in mutations:
  p=copy.deepcopy(project);mut(p)
  try:validate(p,spec)
  except (ValueError,KeyError):checks.append({'check':'negative: '+label,'result':'EXPECTED_REJECTION'})
  else:raise ValueError('Negative control accepted: '+label)
 result={'scope':'Bounded source/serialization/render integrity; not full UFO validation or native-editor round-trip','checks':checks,'passed':len(checks),'total':len(checks),'negative_controls':len(mutations),'concept_coverage':'47/47','registered_relation_coverage':'40/40','model_elements':len(project['elements']),'review_pages':15,'open_gates':['external RoleMixin sortal realization','complete figure at IEEE width','native editor import round-trip','full pattern/antipattern analysis']}
 (OUT/'validation-results.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps({k:v for k,v in result.items() if k!='checks'},indent=2))
if __name__=='__main__':main()
