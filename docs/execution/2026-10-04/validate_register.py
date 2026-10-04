#!/usr/bin/env python3
"""Validate revision-control coverage; this is not an ontology validity test."""
import json
from pathlib import Path

ROOT=Path(__file__).resolve().parent
def read(name): return json.loads((ROOT/name).read_text())
def main():
 req=read('requirements.json'); tasks=read('work-packages.json'); routes=read('issue-map.json')
 expected={f'{g}.{i}' for g,n in enumerate([12,12,10,12,10,12,13,9],1) for i in range(1,n+1)}
 assert len(req)==90 and {r['id'] for r in req}==expected, 'Missing/duplicate author requirement'
 byid={t['id']:t for t in tasks}
 assert len(tasks)==19 and set(byid)=={f'P{i:02}' for i in range(1,20)}
 issue_ids={r['issue'] for r in routes}
 assert len(routes)==33 and len(issue_ids)==33
 assert sum(r['kind']=='existing' for r in routes)==29
 assert sum(r['kind']=='new_delta' for r in routes)==4
 for r in req:
  t=byid[r['package_id']]
  assert r['primary_issue']==t['primary_issue'] in issue_ids
  assert r['acceptance_check'].strip() and r['artifact_destinations']
  assert r['status']=='not_reverified' or r['evidence_refs'], 'Completion needs evidence'
 visiting=set();seen=set()
 def walk(i):
  assert i not in visiting, 'Dependency cycle'
  if i in seen:return
  visiting.add(i)
  for d in byid[i]['deps']:walk(d)
  visiting.remove(i);seen.add(i)
 for t in tasks:
  walk(t['id'])
  assert t['done'] and t['reject'] and t['human'] and t['outputs']
  assert t['primary_issue'] in issue_ids
  assert set(t['requirement_ids'])=={r['id'] for r in req if r['package_id']==t['id']}
  assert (ROOT/'prompts'/f"{t['id']}.md").is_file()
  if t['status']=='completed': assert t['acceptance_result'].startswith('PASS') and t['evidence_refs']
 rubric=read('rhetorical-rubric.json')
 assert len(rubric['criteria'])==33
 assert set(rubric['critical_criterion_ids'])<={r['id'] for r in rubric['criteria']}
 gates=read('gates.json');assert [g['id'] for g in gates]==[f'EG{i}' for i in range(7)]
 assert len(read('artifact-register.json'))==12
 assert len(read('additional-findings.json'))==18
 cq=read('baseline.json')['historical_evidence']['cq']
 assert cq['total']==sum(cq[k] for k in ['executable','partial','conceptual','deferred'])==40
 result=dict(result='PASS_EXECUTION_CONTROL_ONLY',requirements=90,packages=19,existing_issue_routes=29,new_issue_routes=4,package_prompts=19,rhetorical_criteria=33,artifact_groups=12,additional_findings=18,dependency_cycle=False,completed_packages=[t['id'] for t in tasks if t['status']=='completed'],scientific_quality_assessed=False)
 print(json.dumps(result,indent=2));return result
if __name__=='__main__':main()
