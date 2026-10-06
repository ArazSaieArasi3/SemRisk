#!/usr/bin/env python3
"""Reject alteration/removal of rc.4 outputs already present in an exact base commit."""
import argparse,hashlib,json,subprocess
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1];MAN='docs/documentation/rc4/surface-bindings.json'
def verify(old,current,read_bytes):
 if old['route']!=current['route'] or old['source_commit']!=current['source_commit']:raise ValueError('FROZEN_ROUTE_IDENTITY')
 for p,h in old['output_sha256'].items():
  if p not in current['output_sha256'] or current['output_sha256'][p]!=h or hashlib.sha256(read_bytes(p)).hexdigest()!=h:raise ValueError('FROZEN_ROUTE_BYTES')
def main():
 p=argparse.ArgumentParser();p.add_argument('--base',default='HEAD^');a=p.parse_args()
 subprocess.run(['git','cat-file','-e',a.base+'^{commit}'],cwd=ROOT,check=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
 paths=subprocess.check_output(['git','ls-tree','--name-only',a.base,'--',MAN],cwd=ROOT,text=True).splitlines()
 if not paths:print('RC4_HISTORY_PASS: first version addition; historical rc.1 guard remains separate');return
 old=json.loads(subprocess.check_output(['git','show',a.base+':'+MAN],cwd=ROOT,text=True));current=json.loads((ROOT/MAN).read_text());verify(old,current,lambda p:(ROOT/p).read_bytes());print('RC4_HISTORY_PASS: every previously frozen output remains byte-identical')
if __name__=='__main__':main()
