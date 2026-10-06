# Bounded rc.4 source tutorial

> Ontology documentation candidate 0.2.0-rc.4. Source snapshot `67247f13ba5d0c7d32163f2b3e848af15067d92e`. Not a scholarly release or independent domain validation. No manuscript is included.

# Bounded rc.4 tutorial

This engineering exercise reads committed synthetic ontology artifacts. It does not use private source workbooks, demonstrate treatment effects or test SQL parity.

## 1. Obtain the exact source snapshot

```sh
git clone https://github.com/ArazSaieArasi3/SemRisk.git
cd SemRisk
git checkout 67247f13ba5d0c7d32163f2b3e848af15067d92e
python -m venv .venv
. .venv/bin/activate
python -m pip install rdflib==7.6.0
```

## 2. Inspect an explicit asserted distinction

```python
from pathlib import Path
from rdflib import Graph, URIRef
from rdflib.namespace import OWL, RDFS
root = Path('.')
g = Graph().parse(root / 'docs/formal/0.2.0-rc.4/asserted-closure.nt', format='nt')
scenario = URIRef('urn:semrisk:entity:SR-CPT-006')
event = URIRef('urn:semrisk:entity:SR-CPT-007')
assert len(g) == 1618
assert (scenario, OWL.disjointWith, event) in g or (event, OWL.disjointWith, scenario) in g
assert (scenario, RDFS.subClassOf, URIRef('http://purl.org/nemo/gufo#SituationType')) in g
print('1618 asserted triples; scenario/event distinction found')
```

Expected output is the one printed line. This reads explicit triples; it does not run an OWL reasoner. Removing the checked disjointness triple makes the corresponding assertion fail. A record's workflow status does not by itself establish a change in the managed Risk.

## 3. Trace the interpretation

Locate SR-CPT-006 and SR-CPT-007 in the formal term index, read their exact source modules and compare the scenario/occurrence conceptual view. Use the Explorer only as a locator. Anonymous axioms and omitted constructs must be checked in the formal source, not inferred from graph position.

## 4. Keep versions separate

The historical rc.1 route and its tests retain their old inputs and denominators. Do not transfer its eight-task SQL result to the complete rc.4 candidate. External reader tasks and final release identity remain open.


## Navigation

[Overview](https://github.com/ArazSaieArasi3/SemRisk/wiki/rc4-Overview) · [Domains and Concepts](https://github.com/ArazSaieArasi3/SemRisk/wiki/rc4-Domains-and-Concepts) · [Relations](https://github.com/ArazSaieArasi3/SemRisk/wiki/rc4-Relations) · [Formal Reference](https://github.com/ArazSaieArasi3/SemRisk/wiki/rc4-Formal-Reference) · [Diagrams and Explorer](https://github.com/ArazSaieArasi3/SemRisk/wiki/rc4-Diagrams-and-Explorer) · [Tutorial](https://github.com/ArazSaieArasi3/SemRisk/wiki/rc4-Tutorial) · [Sources and Limits](https://github.com/ArazSaieArasi3/SemRisk/wiki/rc4-Sources-and-Limits)

[Home](https://github.com/ArazSaieArasi3/SemRisk/wiki/Home) · [Versioned Pages](https://arazsaiearasi3.github.io/SemRisk/ontology/0.2.0-rc.4/docs-20261006/index.html) · [Canonical repository](https://github.com/ArazSaieArasi3/SemRisk/blob/67247f13ba5d0c7d32163f2b3e848af15067d92e/ontology/releases/0.2.0-rc.4/README.md)
