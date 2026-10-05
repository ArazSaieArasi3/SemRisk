"""Bounded rc.4 exposure projection into the existing V001 table; no scale projection."""
import uuid
from rdflib import Graph,RDF,URIRef,Literal,XSD
from check_exposure_scale import c,r,AC,ROOT
from pyshacl import validate
def uid(iri):return uuid.uuid5(uuid.NAMESPACE_URL,str(iri))
def represented(g):
 out=Graph()
 for e in g.subjects(RDF.type,c(10)):
  out.add((e,RDF.type,c(10)))
  for p in [r(39),r(40),AC.validFrom,AC.validTo]:
   for o in g.objects(e,p):out.add((e,p,o))
  for p,t in [(r(39),c(2)),(r(40),c(3))]:
   for x in g.objects(e,p):
    if (x,RDF.type,t) in g:out.add((x,RDF.type,t))
 return out
def normalized(g):
 def term(x):
  if isinstance(x,Literal) and x.datatype==XSD.dateTime:return ('dateTime',x.toPython().isoformat())
  return str(x)
 return {tuple(term(x) for x in t) for t in represented(g)}
def load_graph(conn,g):
 # Missing fields are checked before creating rows; numeric scale profile is outside this adapter.
 h=represented(g);ok,_,msg=validate(h,shacl_graph=Graph().parse(ROOT/'shapes/exposure-scale-v0.2.0-rc.4.ttl'),inference='none',meta_shacl=True)
 if not ok:raise ValueError(msg)
 for x,t in h.subject_objects(RDF.type):
  typ=str(t).rsplit(':',1)[-1]
  old=conn.execute('SELECT semantic_type_id FROM meta.semantic_instance WHERE instance_iri=%s',(str(x),)).fetchone()
  if old and old[0]!=typ:raise ValueError('Existing IRI has a different asserted projection type')
  conn.execute("INSERT INTO meta.semantic_instance(instance_id,instance_iri,semantic_type_id,evidence_role,synthetic_flag) VALUES(%s,%s,%s,'synthetic_test',true) ON CONFLICT(instance_iri) DO NOTHING",(uid(x),str(x),typ))
 for e in h.subjects(RDF.type,c(10)):
  start=h.value(e,AC.validFrom);end=h.value(e,AC.validTo)
  row=(uid(e),uid(h.value(e,r(39))),uid(h.value(e,r(40))),start.toPython() if start else None,end.toPython() if end else None)
  prev=conn.execute('SELECT exposure_id,subject_instance_id,source_instance_id,valid_from,valid_to FROM core.exposure WHERE exposure_id=%s',(row[0],)).fetchone()
  if prev and tuple(prev)!=row:raise ValueError('Exposure row conflict; no silent history rewrite')
  conn.execute('INSERT INTO core.exposure(exposure_id,subject_instance_id,source_instance_id,valid_from,valid_to) VALUES(%s,%s,%s,%s,%s) ON CONFLICT(exposure_id) DO NOTHING',row)
def export_graph(conn,prefix):
 out=Graph();rows=conn.execute('''SELECT e.instance_iri,s.instance_iri,t.instance_iri,x.valid_from,x.valid_to
 FROM core.exposure x JOIN meta.semantic_instance e ON e.instance_id=x.exposure_id
 JOIN meta.semantic_instance s ON s.instance_id=x.subject_instance_id
 JOIN meta.semantic_instance t ON t.instance_id=x.source_instance_id
 WHERE e.instance_iri LIKE %s ORDER BY e.instance_iri''',(prefix+'%',)).fetchall()
 for e,s,t,a,b in rows:
  e,s,t=map(URIRef,[e,s,t]);out.add((e,RDF.type,c(10)));out.add((s,RDF.type,c(2)));out.add((t,RDF.type,c(3)));out.add((e,r(39),s));out.add((e,r(40),t))
  if a:out.add((e,AC.validFrom,Literal(a,datatype=XSD.dateTime)))
  if b:out.add((e,AC.validTo,Literal(b,datatype=XSD.dateTime)))
 return out
def at_sql(conn,instant,prefix):
 return conn.execute('''SELECT e.instance_iri,s.instance_iri,t.instance_iri FROM core.exposure x
 JOIN meta.semantic_instance e ON e.instance_id=x.exposure_id
 JOIN meta.semantic_instance s ON s.instance_id=x.subject_instance_id
 JOIN meta.semantic_instance t ON t.instance_id=x.source_instance_id
 WHERE e.instance_iri LIKE %s AND x.valid_from<=%s::timestamptz
 AND (x.valid_to IS NULL OR %s::timestamptz<x.valid_to) ORDER BY e.instance_iri''',(prefix+'%',instant,instant)).fetchall()
