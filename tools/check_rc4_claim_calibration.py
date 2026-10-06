#!/usr/bin/env python3
"""Bounded evidence-binding and textual claim regressions; not semantic proof."""
import argparse,copy,csv,hashlib,json,re,subprocess
from pathlib import Path
from author_review_claim_guard import UNSAFE as HISTORICAL_UNSAFE
ROOT=Path(__file__).resolve().parents[1];OUT=ROOT/'publications/2026-icaea-sbu/claims-rc4'
EXPECTED=['SR-CL'+str(i).zfill(2) for i in range(1,10)]
SOURCE_BASELINE='c02f7d2213191a71618f80cf702dbd6959a81d39'
PROTECTED_FIELDS={'SR-CL01': {'status': 'supported_with_narrower_scope', 'evidence_role': 'formal_and_synthetic_verification', 'unit_denominator': '47 conceptual entries / 40 registered relation decisions; figure selects 9/47 and 8/40'}, 'SR-CL02': {'status': 'supported_with_narrower_scope', 'evidence_role': 'design_reconciliation_nonindependent', 'unit_denominator': '27 field dispositions: 6 implemented projection / 13 partial / 7 design-only / 1 deferred'}, 'SR-CL03': {'status': 'partially_supported', 'evidence_role': 'architecture_and_constructed_application', 'unit_denominator': 'Selected external-owner boundaries and bounded links, not all EA entities'}, 'SR-CL04': {'status': 'supported_with_narrower_scope', 'evidence_role': 'historical_synthetic_task_verification', 'unit_denominator': '8/8 historical P49 tasks; not a fresh complete rc.4 rerun'}, 'SR-CL05': {'status': 'supported_with_narrower_scope', 'evidence_role': 'constructed_case_and_literature_applicability', 'unit_denominator': '24 source-local statements / 6 studies; 12 partial / 11 ambiguous / 1 unmapped'}, 'SR-CL06': {'status': 'insufficient_evidence', 'evidence_role': 'independent_validation_NOT_EXECUTED', 'unit_denominator': '0 independently reviewed pilot statements / 0 independent validation sources; no executed shortage holdout'}, 'SR-CL07': {'status': 'partially_supported', 'evidence_role': 'source_comparison_and_synthetic_diagnostic', 'unit_denominator': 'Seven historical comparison units; bounded controlled distinction study'}, 'SR-CL08': {'status': 'supported_with_narrower_scope', 'evidence_role': 'formal_and_synthetic_verification', 'unit_denominator': '31/31 checks including 17 negatives; 4 entailments / 2 countermodels / 2 expected inconsistencies'}, 'SR-CL09': {'status': 'supported_with_narrower_scope', 'evidence_role': 'engineering_reproducibility_with_access_limits', 'unit_denominator': 'Exact candidate sources and tested tasks only, not every original source byte'}}
PATTERNS=HISTORICAL_UNSAFE+[
 r'(?:the pilot contains )?24 observed (?:incidents|risk events)',
 r'(?:complete|full) (?:rc\.4 |current )?(?:helper )?SQL(?:/SPARQL)? parity (?:is |has been )?(?:established|verified|proven)',
 r'full (?:ontology )?atlas (?:is |has been )?(?:print[- ]readable|readable at 170 mm)',
 r'(?:raw metrics|OQuaRE score) (?:prove|proves|establish|establishes) (?:overall |scientific |semantic )?quality',
 r'all (?:eleven|11) helpers have (?:complete |nonempty )?(?:labels|comments)',
]

def unsafe(text):
 failures=[];flat=' '.join(text.split())
 for pattern in PATTERNS:
  for match in re.finditer(pattern,flat,re.I):
   prefix=re.split(r'[.;!?]',flat[max(0,match.start()-160):match.start()])[-1]
   direct=re.search(r'(?:\bno\s+|\bnot\s+|\b(?:do not|does not|did not|cannot|never)\s+(?:claim|assert|suggest|conclude|contain|represent|establish|demonstrate)\s+(?:that\s+)?(?:the\s+)?|\bwithout\s+(?:claiming|asserting)\s+(?:that\s+)?)$',prefix,re.I)
   if direct:continue
   failures.append({'match':match.group(),'pattern':pattern})
 return failures

def pinned_blob(path):
 try:return subprocess.check_output(['git','rev-parse',SOURCE_BASELINE+':'+path],cwd=ROOT,text=True,stderr=subprocess.DEVNULL).strip()
 except subprocess.CalledProcessError:raise ValueError('PINNED_SOURCE_REF_UNAVAILABLE: fetch the declared source commit first')

def check(data):
 errors=[];rows=data.get('claims',[])
 if [r.get('claim_id') for r in rows]!=EXPECTED:errors.append('CLAIM_IDS')
 if data.get('candidate')!='0.2.0-rc.4' or data.get('source_baseline')!=SOURCE_BASELINE:errors.append('CANDIDATE_REF_DRIFT')
 if data.get('sql_parity')!='HISTORICAL_TASK_ONLY; #125 DEFERRED':errors.append('SQL_SCOPE_UPGRADE')
 prior={r['threat_id'] for r in csv.DictReader((ROOT/'evaluation/integrity/threat-limitation-registry-v1.0.csv').open())}
 delta=json.loads((OUT/'threat-delta.json').read_text());known=prior|{r['id'] for r in delta['delta']}
 if hashlib.sha256((ROOT/delta['inherited_registry']).read_bytes()).hexdigest()!=delta['inherited_registry_sha256']:errors.append('INHERITED_THREAT_DRIFT')
 for threat in delta['delta']:
  if hashlib.sha256((ROOT/threat['source']).read_bytes()).hexdigest()!=threat['source_sha256']:errors.append('THREAT_SOURCE_DRIFT')
  if threat.get('source_commit')!=SOURCE_BASELINE:errors.append('THREAT_SOURCE_REF')
  raw=(ROOT/threat['source']).read_bytes();blob=hashlib.sha1(b'blob '+str(len(raw)).encode()+b'\0'+raw).hexdigest()
  if pinned_blob(threat['source'])!=blob:errors.append('THREAT_COMMIT_BLOB_DRIFT')
  for source in threat.get('additional_sources',[]):
   if hashlib.sha256((ROOT/source['path']).read_bytes()).hexdigest()!=source['sha256'] or source.get('source_commit')!=SOURCE_BASELINE:errors.append('THREAT_ADDITIONAL_SOURCE_DRIFT')
   raw=(ROOT/source['path']).read_bytes();blob=hashlib.sha1(b'blob '+str(len(raw)).encode()+b'\0'+raw).hexdigest()
   if pinned_blob(source['path'])!=blob:errors.append('THREAT_ADDITIONAL_COMMIT_DRIFT')
 required=['rq','contribution','status','calibrated_wording','unit_denominator','evidence_role','supporting_sources','challenging_or_missing_evidence','threat_ids','manuscript_locations','location_status','owner','recheck_trigger']
 for r in rows:
  cid=r.get('claim_id','?')
  for key,expected in PROTECTED_FIELDS.get(cid,{}).items():
   if r.get(key)!=expected:errors.append('PROTECTED_'+key+': '+cid)
  for key in required:
   if not r.get(key):errors.append('MISSING_'+key+': '+cid)
  if set(r.get('threat_ids',[]))-known:errors.append('UNKNOWN_THREAT: '+cid)
  if unsafe(r.get('calibrated_wording','')):errors.append('UNSAFE_WORDING: '+cid)
  for source in r.get('supporting_sources',[]):
   path=(ROOT/source['path']).resolve()
   if not path.is_relative_to(ROOT):errors.append('SOURCE_ESCAPE');continue
   if not path.exists():errors.append('MISSING_SOURCE');continue
   content=path.read_bytes();blob=hashlib.sha1(b'blob '+str(len(content)).encode()+b'\0'+content).hexdigest()
   if blob!=source['git_blob_sha'] or hashlib.sha256(content).hexdigest()!=source['sha256']:errors.append('SOURCE_DRIFT: '+cid)
   if pinned_blob(source['path'])!=source['git_blob_sha']:errors.append('COMMIT_BLOB_DRIFT: '+cid)
   if source.get('source_commit')!=SOURCE_BASELINE:errors.append('SOURCE_REF: '+cid)
 if data.get('human_domain_responses')!=0:errors.append('INVENTED_HUMAN')
 if data.get('independent_transfer')!='NOT_DEMONSTRATED':errors.append('INVENTED_TRANSFER')
 if data.get('global_assurance')!='NOT_ASSESSED':errors.append('INVENTED_ASSURANCE')
 for row in rows:
  if row.get('claim_id')=='SR-CL06' and row.get('status')!='insufficient_evidence':errors.append('TRANSFER_STATUS_UPGRADE')
 return errors

def projection(data):
 lines=['# Current rc.4 authoring ceilings','','These are calibrated authoring inputs, not proof of final manuscript placement. Exact citations and headline anchors are checked during manuscript integration. No wording below waives the linked adverse evidence.','']
 for row in data['claims']:
  lines += ['## '+row['claim_id']+' — '+row['status'],'',row['calibrated_wording'],'','- RQ / contribution: '+row['rq']+' / '+row['contribution'],'- Unit: '+row['unit_denominator'],'- Evidence role: '+row['evidence_role'],'- Counterevidence/limit: '+row['challenging_or_missing_evidence'],'- Threats: '+', '.join(row['threat_ids']),'- Planned locations: '+', '.join(row['manuscript_locations'])+'; exact derivative anchors remain pending.','']
 lines += ['## Scope of machine checking','','The guard verifies source identity, mandatory ledger fields, protected evidence states and declared unsafe wording fixtures. It is a bounded regression aid, not a natural-language theorem prover or substitute for scientific review. Full final-document location and citation audit remains a manuscript gate.']
 return '\n'.join(lines)+'\n'

def tests(data):
 cases=[
 ('field_completeness','27/27 proves ERM completeness.'),
 ('global_parity','Global ontology-to-database equivalence has been established.'),
 ('treatment_effect','DS-003 demonstrates treatment effectiveness.'),
 ('transfer','Independent transferability has been demonstrated.'),
 ('simulated_human','Simulated R1–R8 panel is independent human validation.'),
 ('standards','Complete ISO conformance is demonstrated.'),
 ('external_owner','External Pharma ontology is locally owned by SemRisk Core.'),
 ('pilot_incidents','The pilot contains 24 observed incidents.'),
 ('current_sql','Full rc.4 SQL parity is established.'),
 ('atlas','The full atlas is print-readable.'),
 ('quality','Raw metrics prove scientific quality.'),
 ('helper_annotations','All eleven helpers have nonempty labels.'),
 ]
 for id,phrase in cases:
  assert unsafe(phrase),id
  # Direct negation is scoped to the exact claim, not arbitrary nearby negatives.
  assert not unsafe('We do not claim that '+phrase[0].lower()+phrase[1:]),id+' negation'
 for phrase in ['Not only is this useful, independent transferability has been demonstrated.','We do not claim superiority, but global ontology-to-database equivalence has been established.']:
  assert unsafe(phrase),'UNRELATED_NEGATION'
 controls=[]
 for name,mutation,marker in [
 ('missing_claim',lambda d:d['claims'].pop(),'CLAIM_IDS'),
 ('hidden_counterevidence',lambda d:d['claims'][0].update(challenging_or_missing_evidence=''),'MISSING_challenging'),
 ('source_hash',lambda d:d['claims'][0]['supporting_sources'][0].update(sha256='0'*64),'SOURCE_DRIFT'),
 ('invented_human',lambda d:d.update(human_domain_responses=5),'INVENTED_HUMAN'),
 ('transfer_upgrade',lambda d:d['claims'][5].update(status='supported_as_worded'),'TRANSFER_STATUS'),
 ('unknown_threat',lambda d:d['claims'][0]['threat_ids'].append('UNKNOWN'),'UNKNOWN_THREAT'),
 ('missing_location',lambda d:d['claims'][0].update(manuscript_locations=[]),'MISSING_manuscript'),
 ('fabricated_commit',lambda d:d['claims'][0]['supporting_sources'][0].update(source_commit='0'*40),'SOURCE_REF'),
 ('candidate_upgrade',lambda d:d.update(candidate='FINAL_RELEASE'),'CANDIDATE_REF'),
 ('sql_scope_upgrade',lambda d:d.update(sql_parity='FULL_CURRENT_PARITY'),'SQL_SCOPE'),
 ('role_upgrade',lambda d:d['claims'][4].update(evidence_role='independent_validation'),'PROTECTED_evidence_role'),
 ('denominator_upgrade',lambda d:d['claims'][4].update(unit_denominator='24 independently validated incidents'),'PROTECTED_unit_denominator'),
 ]:
  changed=copy.deepcopy(data);mutation(changed);assert any(marker in e for e in check(changed)),name;controls.append(name)
 return {'unsafe_rejected':len(cases),'direct_nonclaims_accepted':len(cases),'unrelated_negation_rejected':2,'ledger_corruptions_rejected':controls}

def main():
 p=argparse.ArgumentParser();p.add_argument('--write',action='store_true');p.add_argument('--text',type=Path);a=p.parse_args();data=json.loads((OUT/'claim-register.json').read_text());errors=check(data)
 if errors:raise SystemExit('\n'.join(errors))
 results=tests(data);text=projection(data)
 if a.write:(OUT/'authoring-ceilings.md').write_text(text)
 elif (OUT/'authoring-ceilings.md').read_text()!=text:raise SystemExit('CLAIM_PROJECTION_DRIFT')
 if a.text:
  failures=unsafe(a.text.read_text())
  if failures:raise SystemExit(json.dumps(failures,indent=2))
 print(json.dumps({'result':'PASS_BOUNDED_CLAIM_BINDINGS','claim_count':9,**results,'limits':['Final manuscript anchors/citations remain separate','No independent human validation or global assurance','Textual patterns are not exhaustive semantic analysis']},indent=2))
if __name__=='__main__':main()
