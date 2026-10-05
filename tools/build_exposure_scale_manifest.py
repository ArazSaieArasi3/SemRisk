#!/usr/bin/env python3
"""Bind rc.4 source and retain all historical release bytes."""
import argparse,json,hashlib
from pathlib import Path
from check_exposure_scale import ROOT,D,V,MODULES
def digest(paths):return {str(p.relative_to(ROOT)):hashlib.sha256(p.read_bytes()).hexdigest() for p in sorted(set(paths))}
def manifest():
 paths=[D/f'{m}.ttl' for m in MODULES]+[D/'catalog.xml',D/'profile-iri-registry.csv',D/'information-state-iri-registry.csv',D/'conceptual-iri-register.csv',ROOT/'ontology/vendor/gufo-v1.0.0.ttl']
 paths += list((ROOT/f'foundational/exposure-scale-v{V}').glob('*'))
 paths += [ROOT/p for p in [f'shapes/exposure-scale-v{V}.ttl','shapes/assessment-context-v0.2.0-rc.1.ttl','shapes/semantic-identity-v0.2.0-rc.3.ttl',f'testdata/foundational/exposure-scale-v{V}.ttl',f'rules/core/exposure-at-v{V}.rq','tools/check_exposure_scale.py','tools/check_exposure_postgres.py','tools/build_exposure_scale_manifest.py','relational/scripts/exposure_io.py','relational/sql/V001__paper1_projection.sql','.github/workflows/paper1-exposure-scale.yml',f'evaluation/exposure-scale/v{V}/acceptance-contract.md']]
 old=[p for v in ['0.2.0-rc.1','0.2.0-rc.2','0.2.0-rc.3'] for p in (ROOT/'ontology/releases'/v).rglob('*') if p.is_file()]
 return dict(candidate_version=V,previous_candidate='0.2.0-rc.3',baseline_commit='6d619c5bbcb3532d68e250e2c27a9a3232fd06f9',publication_ready=False,module_count=7,domain_concepts=dict(local_classes=35,markers=4,undeclared=8),registered_relations=40,local_registered_object_properties=39,metadata_relations=1,helper_inventory=dict(classes=11,object_properties=11,data_properties=8,controlled_individuals=7),semantic_changes=['Explicit Exposure subject/source relations, without global cardinality or consequence rule','NumericScale specializes ArtifactVersion with inherited Subkind identity'],source_sha256=digest(paths),historical_release_sha256=digest(old),limits=['Full editor/antipattern and IEEE fit remain open','Native SQL claim is exposure-only; scale/content/workflow parity incomplete','Synthetic examples only'])
if __name__=='__main__':
 p=argparse.ArgumentParser();p.add_argument('--check',action='store_true');a=p.parse_args();s=json.dumps(manifest(),indent=2)+'\n'
 if a.check:assert (D/'manifest.json').read_text()==s,'rc.4 binding or historical release bytes differ'
 else:(D/'manifest.json').write_text(s)
 print('EXPOSURE_SCALE_BINDING_PASS')
