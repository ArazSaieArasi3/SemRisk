#!/usr/bin/env python3
from pathlib import Path
import csv, os, subprocess
from rdflib import Graph

ROOT=Path(__file__).resolve().parents[1]
REG=ROOT/"evaluation/parity/p49-paired-query-registry-v1.0.csv"

g=Graph()
for p in [
    ROOT/"ontology/core/semrisk-core-v0.1.0-rc.1.ttl",
    ROOT/"ontology/enterprise/semrisk-enterprise-v0.1.0-rc.1.ttl",
    ROOT/"case/pharma/constructed-pharma-case-v1.0.ttl",
    ROOT/"case/pharma/e2e-scenario-v1.0.ttl",
]:
    g.parse(p,format="turtle")

PREFIX="""PREFIX sr: <urn:semrisk:entity:>
PREFIX case: <urn:semrisk:scenario:p1:e2e:>
PREFIX base: <urn:semrisk:case:pharma:v1:>
PREFIX dcterms: <http://purl.org/dc/terms/>
"""

pairs={
"P49-01":(
PREFIX+"""SELECT ?scenario ?event WHERE {
  VALUES ?scenario { base:scenario }
  ?scenario sr:SR-REL-003 ?event .
}""",
"""SELECT s.instance_iri,e.instance_iri
FROM core.risk_event re
JOIN meta.semantic_instance e ON e.instance_id=re.event_id
JOIN meta.semantic_instance s ON s.instance_id=re.realizes_scenario_id
WHERE re.realizes_scenario_id='47000000-0000-0000-0001-000000000004';"""
),
"P49-02":(
PREFIX+"""SELECT ?event ?trigger ?consequence WHERE {
  VALUES ?event { case:event }
  ?event sr:SR-REL-007 ?trigger ;
         sr:SR-REL-004 ?consequence .
}""",
"""SELECT e.instance_iri,t.instance_iri,c.instance_iri
FROM core.risk_event re
JOIN core.event_trigger et ON et.event_id=re.event_id
JOIN core.trigger_event tr ON tr.trigger_id=et.trigger_id
JOIN core.event_consequence ec ON ec.event_id=re.event_id
JOIN core.consequence co ON co.consequence_id=ec.consequence_id
JOIN meta.semantic_instance e ON e.instance_id=re.event_id
JOIN meta.semantic_instance t ON t.instance_id=tr.trigger_id
JOIN meta.semantic_instance c ON c.instance_id=co.consequence_id
WHERE re.event_id='48000000-0000-0000-0001-000000000002';"""
),
"P49-03":(
PREFIX+"""SELECT ?risk ?pre ?post ?inherent ?residual WHERE {
  VALUES ?post { case:assessment-post }
  ?post sr:SR-REL-034 ?pre ;
        sr:SR-REL-015 ?residual .
  ?pre sr:SR-REL-015 ?inherent .
  ?residual sr:SR-REL-033 ?inherent ;
            sr:SR-REL-016 ?risk .
  ?inherent sr:SR-REL-016 ?risk .
}""",
"""SELECT r.instance_iri,prei.instance_iri,posti.instance_iri,ini.instance_iri,resi.instance_iri
FROM assessment.assessment_activity post
JOIN assessment.assessment_activity pre ON pre.assessment_id=post.prior_assessment_id
JOIN assessment.assessment_result res ON res.assessment_id=post.assessment_id
JOIN assessment.assessment_result inh ON inh.result_id=res.supersedes_result_id
JOIN meta.semantic_instance r ON r.instance_id=res.risk_id
JOIN meta.semantic_instance prei ON prei.instance_id=pre.assessment_id
JOIN meta.semantic_instance posti ON posti.instance_id=post.assessment_id
JOIN meta.semantic_instance ini ON ini.instance_id=inh.result_id
JOIN meta.semantic_instance resi ON resi.instance_id=res.result_id
WHERE post.assessment_id='48000000-0000-0000-0001-000000000013';"""
),
"P49-04":(
PREFIX+"""SELECT ?strategy ?plan ?activity ?control WHERE {
  VALUES ?strategy { base:pooled-procurement-strategy }
  ?plan sr:SR-REL-022 ?strategy .
  ?activity sr:SR-REL-023 ?plan ;
            sr:SR-REL-024 ?control .
}""",
"""SELECT si.instance_iri,pi.instance_iri,ai.instance_iri,ci.instance_iri
FROM treatment.plan p
JOIN treatment.activity a ON a.plan_id=p.plan_id
JOIN treatment.activity_control ac ON ac.activity_id=a.activity_id
JOIN meta.semantic_instance si ON si.instance_id=p.strategy_id
JOIN meta.semantic_instance pi ON pi.instance_id=p.plan_id
JOIN meta.semantic_instance ai ON ai.instance_id=a.activity_id
JOIN meta.semantic_instance ci ON ci.instance_id=ac.control_id
WHERE p.plan_id='48000000-0000-0000-0001-000000000008';"""
),
"P49-05":(
PREFIX+"""SELECT ?risk ?actorLabel WHERE {
  VALUES ?resp { case:responsibility }
  ?resp sr:SR-REL-027 ?risk ;
        sr:SR-REL-028 ?actor .
  ?actor dcterms:title ?actorLabel .
}""",
"""SELECT r.instance_iri,a.label
FROM enterprise.v_risk_owner v
JOIN meta.semantic_instance r ON r.instance_id=v.risk_id
JOIN enterprise.actor_ref a ON a.actor_id=v.actor_id
WHERE v.risk_id='47000000-0000-0000-0001-000000000001';"""
),
"P49-06":(
PREFIX+"""SELECT ?family ?state WHERE {
 { ?state a sr:SR-CPT-035 . FILTER(STRSTARTS(STR(?state),"urn:semrisk:scenario:p1:e2e:")) BIND("risk_state" AS ?family) }
 UNION
 { ?state a sr:SR-CPT-036 . FILTER(STRSTARTS(STR(?state),"urn:semrisk:scenario:p1:e2e:")) BIND("workflow_state" AS ?family) }
}""",
"""SELECT 'risk_state',i.instance_iri
FROM enterprise.risk_state_history r JOIN meta.semantic_instance i ON i.instance_id=r.risk_state_id
WHERE r.risk_state_id IN ('48000000-0000-0000-0001-000000000015','48000000-0000-0000-0001-000000000016')
UNION ALL
SELECT 'workflow_state',i.instance_iri
FROM enterprise.workflow_state_history w JOIN meta.semantic_instance i ON i.instance_id=w.workflow_state_id
WHERE w.workflow_state_id IN ('48000000-0000-0000-0001-000000000017','48000000-0000-0000-0001-000000000018');"""
),
"P49-07":(
PREFIX+"""SELECT ?result ?evidence WHERE {
 VALUES ?result { case:result-inherent case:result-residual }
 ?result sr:SR-REL-017 ?evidence .
}""",
"""SELECT ri.instance_iri,ei.instance_iri
FROM assessment.assessment_evidence ae
JOIN meta.semantic_instance ri ON ri.instance_id=ae.result_id
JOIN meta.semantic_instance ei ON ei.instance_id=ae.evidence_id
WHERE ae.result_id IN ('48000000-0000-0000-0001-000000000012','48000000-0000-0000-0001-000000000014');"""
),
"P49-08":(
PREFIX+"""SELECT ?context ?target WHERE {
 VALUES ?context { base:risk-context base:scenario }
 ?context sr:SR-REL-037 ?target .
 FILTER(STRSTARTS(STR(?target),"urn:cm-pharme:v1.0.0:"))
}""",
"""SELECT ci.instance_iri,ee.owner_semantic_id
FROM pharma.context_link pc
JOIN ref.external_entity ee ON ee.external_entity_id=pc.external_entity_id
JOIN meta.semantic_instance ci ON ci.instance_id=COALESCE(pc.risk_id,pc.scenario_id)
WHERE pc.risk_id='47000000-0000-0000-0001-000000000001'
   OR pc.scenario_id='47000000-0000-0000-0001-000000000004';"""
),
}

def sparql_rows(q):
    return {tuple(str(v) for v in row) for row in g.query(q)}

def sql_rows(q):
    env=os.environ.copy()
    p=subprocess.run(["psql","-At","-F","\t","-v","ON_ERROR_STOP=1","-c",q],check=True,text=True,capture_output=True,env=env)
    return {tuple(line.split("\t")) for line in p.stdout.splitlines() if line.strip()}

def normalize(pid,rows,side):
    out=set()
    for row in rows:
        r=list(row)
        if pid=="P49-08" and side=="rdf":
            r[1]=r[1].rsplit(":",1)[-1]
        out.add(tuple(r))
    return out

registry={r["pair_id"]:r for r in csv.DictReader(REG.open(encoding="utf-8"))}
results=[]
for pid,(sq,pq) in pairs.items():
    rdf=normalize(pid,sparql_rows(sq),"rdf")
    sql=normalize(pid,sql_rows(pq),"sql")
    expected=registry[pid]["expected_parity_class"]
    if pid=="P49-07":
        # Task-level result/evidence pair is equal; classification remains partial due RDB-only support_role.
        ok=(rdf==sql)
        actual="partial" if ok else "implementation_bug"
    elif pid in ("P49-05","P49-08"):
        ok=(rdf==sql)
        actual="equivalent_after_declared_normalization" if ok else "implementation_bug"
    else:
        ok=(rdf==sql)
        actual="equivalent_for_task" if ok else "implementation_bug"
    results.append((pid,expected,actual,len(rdf),len(sql),rdf,sql))
    if actual!=expected:
        print(f"{pid}: expected {expected}, actual {actual}\nRDF={rdf}\nSQL={sql}")
        raise SystemExit(1)
    print(f"PASS {pid}: {actual} rows rdf={len(rdf)} sql={len(sql)}")

print("SEM_RISK_ISSUE_49_SQL_SPARQL_PARITY_PASS")
