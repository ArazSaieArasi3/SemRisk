#!/usr/bin/env python3
"""Explicit opt-in metadata adapter. Never invents a realized scenario or event."""
import argparse
from rdflib import Graph,RDF,RDFS,OWL,Namespace
SR=Namespace('urn:semrisk:entity:');GUFO=Namespace('http://purl.org/nemo/gufo#')
def adapt(g):
 out=Graph();out+=g
 for s in g.subjects(RDF.type,SR['SR-CPT-006']):
  out.add((s,RDF.type,OWL.Class));out.add((s,RDFS.subClassOf,GUFO.Situation))
 return out
if __name__=='__main__':
 p=argparse.ArgumentParser();p.add_argument('input');p.add_argument('output');a=p.parse_args()
 if a.input==a.output:raise SystemExit('Use a new output file; preserve the source evidence.')
 g=Graph().parse(a.input);h=adapt(g);h.serialize(a.output,format='turtle');print('Added scenario declaration triples:',len(h)-len(g))
