"""Explicit numeric-profile RDF/PostgreSQL projection; caller owns transaction."""
from decimal import Decimal
from uuid import uuid5, NAMESPACE_URL
from rdflib import Graph, URIRef, RDF, Literal, XSD
from check_qualified_context import AC, SR, DCT, PROV, c, r, validate_graph

def uid(iri):return uuid5(NAMESPACE_URL,str(iri))
def one(g,s,p,optional=False):
 vals=list(g.objects(s,p))
 if optional and not vals:return None
 if len(vals)!=1:raise ValueError(f'exactly one {p} for {s}')
 return vals[0]
def zoned(v):
 if v is None:return None
 d=v.toPython()
 if v.datatype!=XSD.dateTime or not hasattr(d,'tzinfo') or d.tzinfo is None:
  raise ValueError('explicit timestamp timezone required')
 return d
def local(v):return str(v).removeprefix(str(AC))
def load_graph(conn,g):
 ok,_,report=validate_graph(g)
 if not ok:raise ValueError('profile validation failed: '+report)
 def instance(s,type_id):
  conn.execute('INSERT INTO meta.semantic_instance(instance_id,instance_iri,semantic_type_id,evidence_role,synthetic_flag) VALUES(%s,%s,%s,%s,%s)',
               (uid(s),str(s),type_id,'synthetic_test',True))
 # This loader is deliberately a synthetic regression loader. Reuse for real
 # data requires an explicit provenance/evidence-role loader, not flag removal.
 for s in sorted(g.subjects(RDF.type,c(1))):
  instance(s,'SR-CPT-001');conn.execute('INSERT INTO core.risk(risk_id) VALUES(%s)',(uid(s),))
 for s in sorted(g.subjects(RDF.type,c(12))):
  instance(s,'SR-CPT-012');conn.execute('INSERT INTO assessment.assessment_method(method_id,method_code,version_ref) VALUES(%s,%s,%s)',(uid(s),'synthetic-method',str(one(g,s,DCT.hasVersion))))
 for s in sorted(g.subjects(RDF.type,AC.NumericScale)):
  conn.execute('INSERT INTO assessment.numeric_scale VALUES(%s,%s,%s,%s,%s)',(str(s),str(one(g,s,DCT.hasVersion)),local(one(g,s,AC.dimension)),one(g,s,AC.minimum).toPython(),one(g,s,AC.maximum).toPython()))
 pending=set(g.subjects(RDF.type,c(11)));done=set()
 while pending:
  ready=[s for s in pending if one(g,s,r(34),True) is None or one(g,s,r(34),True) in done]
  if not ready:raise ValueError('cyclic/unresolved assessment predecessor')
  for s in sorted(ready):
   prior=one(g,s,r(34),True);instance(s,'SR-CPT-011')
   conn.execute('INSERT INTO assessment.assessment_activity(assessment_id,risk_id,method_id,prior_assessment_id) VALUES(%s,%s,%s,%s)',(uid(s),uid(one(g,s,r(13))),uid(one(g,s,r(14))),uid(prior) if prior else None))
   done.add(s);pending.remove(s)
 pending=set(g.subjects(RDF.type,AC.QualifiedAssessmentResult));done=set()
 while pending:
  ready=[s for s in pending if one(g,s,r(33),True) is None or one(g,s,r(33),True) in done]
  if not ready:raise ValueError('cyclic/unresolved result predecessor')
  for s in sorted(ready):
   baseline=local(one(g,s,AC.controlBaseline));kind='inherent' if baseline=='BeforeControl' else 'residual'
   instance(s,'SR-CPT-017' if kind=='inherent' else 'SR-CPT-018')
   activities=list(g.subjects(r(15),s));assert len(activities)==1
   prior=one(g,s,r(33),True)
   conn.execute('INSERT INTO assessment.assessment_result(result_id,assessment_id,risk_id,result_kind,supersedes_result_id,value_numeric) VALUES(%s,%s,%s,%s,%s,%s)',(uid(s),uid(activities[0]),uid(one(g,s,r(16))),kind,uid(prior) if prior else None,one(g,s,AC.numericValue).toPython()))
   conn.execute('INSERT INTO assessment.result_context VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s)',(uid(s),local(one(g,s,AC.dimension)),baseline,local(one(g,s,AC.evaluationBasis)),str(one(g,s,AC.scale)),uid(one(g,s,AC.method)),str(one(g,s,AC.methodVersion)),zoned(one(g,s,AC.assessedAt)),zoned(one(g,s,AC.referenceTime))))
   done.add(s);pending.remove(s)
 actors=set()
 for s in sorted(g.subjects(RDF.type,c(31))):
  actor=one(g,s,r(28));instance(s,'SR-CPT-031')
  if actor not in actors:
   conn.execute('INSERT INTO enterprise.actor_ref(actor_id,actor_iri,actor_kind) VALUES(%s,%s,%s)',(uid(actor),str(actor),'synthetic'))
   actors.add(actor)
  conn.execute('INSERT INTO enterprise.risk_responsibility(responsibility_id,actor_id,risk_id,valid_from,valid_to,invalidated_at) VALUES(%s,%s,%s,%s,%s,%s)',(uid(s),uid(actor),uid(one(g,s,r(27))),zoned(one(g,s,AC.validFrom,True)),zoned(one(g,s,AC.validTo,True)),zoned(one(g,s,PROV.invalidatedAtTime,True))))

def export_graph(conn,namespace):
 """Export selected qualified results and risk-scoped responsibilities only."""
 g=Graph()
 def add(s,p,o):g.add((s,p,o))
 def iri(s):return URIRef(s)
 def decimal(v):return Literal(v,datatype=XSD.decimal)
 rows=conn.execute('SELECT * FROM assessment.v_qualified_result_context WHERE result_iri LIKE %s ORDER BY result_iri',(namespace+'%',)).fetchall()
 for row in rows:
  s,risk,act,m,dim,baseline,basis,scale,sv,lo,hi,mv,at,rt,val,prior=row
  s,risk,act,m,scale=map(iri,[s,risk,act,m,scale])
  for typ in [AC.QualifiedAssessmentResult,c(13),c({'Likelihood':14,'Impact':15,'RiskLevel':16}[dim]),c(17 if baseline=='BeforeControl' else 18)]:add(s,RDF.type,typ)
  add(risk,RDF.type,c(1));add(act,RDF.type,c(11));add(m,RDF.type,c(12));add(m,DCT.hasVersion,Literal(mv))
  add(act,r(13),risk);add(act,r(14),m);add(act,r(15),s);add(s,r(16),risk)
  for p,o in [(AC.dimension,AC[dim]),(AC.controlBaseline,AC[baseline]),(AC.evaluationBasis,AC[basis]),(AC.scale,scale),(AC.method,m),(AC.methodVersion,Literal(mv)),(AC.assessedAt,Literal(at,datatype=XSD.dateTime)),(AC.referenceTime,Literal(rt,datatype=XSD.dateTime)),(AC.numericValue,decimal(val))]:add(s,p,o)
  add(scale,RDF.type,AC.NumericScale);add(scale,DCT.hasVersion,Literal(sv));add(scale,AC.dimension,AC[dim]);add(scale,AC.minimum,decimal(lo));add(scale,AC.maximum,decimal(hi))
  if prior:add(s,r(33),iri(prior))
 for a,b in conn.execute('SELECT si.instance_iri,pi.instance_iri FROM assessment.assessment_activity a JOIN meta.semantic_instance si ON si.instance_id=a.assessment_id JOIN meta.semantic_instance pi ON pi.instance_id=a.prior_assessment_id WHERE si.instance_iri LIKE %s',(namespace+'%',)):
  add(iri(a),r(34),iri(b))
 for s,risk,actor,start,end,invalid in conn.execute('SELECT si.instance_iri,ri.instance_iri,a.actor_iri,rr.valid_from,rr.valid_to,rr.invalidated_at FROM enterprise.risk_responsibility rr JOIN meta.semantic_instance si ON si.instance_id=rr.responsibility_id JOIN meta.semantic_instance ri ON ri.instance_id=rr.risk_id JOIN enterprise.actor_ref a USING(actor_id) WHERE si.instance_iri LIKE %s',(namespace+'%',)):
  s=iri(s);add(s,RDF.type,c(31));add(s,r(27),iri(risk));add(s,r(28),iri(actor))
  for p,v in [(AC.validFrom,start),(AC.validTo,end),(PROV.invalidatedAtTime,invalid)]:
   if v is not None:add(s,p,Literal(v,datatype=XSD.dateTime))
 return g

def normalized_triples(g):
 """Value-normalize decimals/timezones; disregard only fixture-package annotation."""
 rows=[]
 for s,p,o in g:
  if str(s).endswith(':fixture'):continue
  if isinstance(o,Literal) and o.datatype==XSD.decimal:o=('decimal',str(Decimal(str(o)).normalize()))
  elif isinstance(o,Literal) and o.datatype==XSD.dateTime:
   from datetime import timezone
   o=('datetime',o.toPython().astimezone(timezone.utc).isoformat())
  else:o=('term',o.n3())
  rows.append((s.n3(),p.n3(),o))
 return set(rows)
