#!/usr/bin/env python3
import argparse, csv, hashlib, json, os, platform, re, sys
from pathlib import Path
from rdflib import Graph, URIRef
from rdflib.namespace import RDF, RDFS, OWL
from pyshacl import validate as shacl_validate
import rdflib
import pyshacl

ROOT = Path(__file__).resolve().parents[1]
BUILD = ROOT / "build" / "semantic-ci"
BUILD.mkdir(parents=True, exist_ok=True)

MODULES = [
    "ontology/core/semrisk-core-v0.1.0-rc.1.ttl",
    "ontology/enterprise/semrisk-enterprise-v0.1.0-rc.1.ttl",
    "ontology/method/semrisk-method-v0.1.0-rc.1.ttl",
    "ontology/governance/semrisk-governance-v0.1.0-rc.1.ttl",
    "ontology/pharma/semrisk-pharma-v0.1.0-rc.1.ttl",
    "ontology/mappings/semrisk-mappings-v0.1.0-rc.1.ttl",
]
SHAPES = "shapes/semrisk-paper1-shapes-v0.1.0-rc.1.ttl"
POSITIVE = "testdata/p1-r2-positive-smoke-v0.1.ttl"
NEGATIVES = [
    "testdata/negative/entry-missing-risk.ttl",
    "testdata/negative/workflow-two-current.ttl",
    "testdata/negative/responsibility-missing-assignee.ttl",
    "testdata/negative/assessment-result-missing-trace.ttl",
    "testdata/negative/pharma-wrong-target.ttl",
]
TRACE_NEG = "testdata/negative/trace-mismatch.csv"
SUBSET = "architecture/g2/paper1-semantic-subset-manifest-v0.1.csv"
IRI_MAP = "governance/identity/conceptual-id-formal-iri-map-v0.1.csv"
EXT_BINDINGS = "governance/identity/external-dependency-binding-registry-v1.0.csv"
RULE = "rules/enterprise/derive-has-risk-owner-v0.1.0-rc.1.rq"

ALLOWED_STATUSES = {"PASS","FAIL","WARNING","ERROR","UNSUPPORTED","NOT_RUN","N-A"}
checks=[]

def add(cid,family,status,message):
    if status not in ALLOWED_STATUSES:
        raise ValueError(status)
    checks.append({"id":cid,"family":family,"status":status,"message":message})

def sha256(path):
    h=hashlib.sha256()
    with open(path,"rb") as f:
        for block in iter(lambda:f.read(1024*1024),b""):
            h.update(block)
    return h.hexdigest()

def parse_graph(path):
    g=Graph()
    g.parse(ROOT/path, format="turtle")
    return g

def union_graph(paths):
    g=Graph()
    for p in paths:
        g.parse(ROOT/p, format="turtle")
    return g

def csv_rows(path):
    with open(ROOT/path, newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f))

def canonical_text():
    return "\n".join((ROOT/p).read_text(encoding="utf-8") for p in MODULES)

def run_pre():
    parsed={}
    try:
        for p in MODULES+[SHAPES,POSITIVE]+NEGATIVES+["ontology/vendor/gufo-v1.0.0.ttl"]:
            parsed[p]=parse_graph(p)
        add("PARSE-001","RDF_PARSE","PASS",f"Parsed {len(parsed)} Turtle inputs.")
    except Exception as e:
        add("PARSE-001","RDF_PARSE","FAIL",repr(e))
        raise

    formal=union_graph(MODULES)
    text=canonical_text()

    subset=csv_rows(SUBSET)
    missing=[]
    for row in subset:
        iri=URIRef("urn:semrisk:entity:"+row["semantic_id"])
        if not any(True for _ in formal.triples((iri,None,None))) and not any(True for _ in formal.triples((None,None,iri))):
            missing.append(row["semantic_id"])
    if missing:
        add("TRACE-001","TRACEABILITY","FAIL","Missing release-critical IDs: "+",".join(missing))
    else:
        add("TRACE-001","TRACEABILITY","PASS",f"{len(subset)}/{len(subset)} release-critical IDs present.")

    neg_missing=[]
    for row in csv_rows(TRACE_NEG):
        iri=URIRef("urn:semrisk:entity:"+row["semantic_id"])
        present=any(True for _ in formal.triples((iri,None,None))) or any(True for _ in formal.triples((None,None,iri)))
        if not present:
            neg_missing.append(row["semantic_id"])
    add("TRACE-NEG-001","TRACEABILITY_NEGATIVE","PASS" if len(neg_missing)==2 else "FAIL",
        f"Known trace mismatch detected for {len(neg_missing)}/2 fake IDs.")

    ids=csv_rows(IRI_MAP)
    idvals=[r["semantic_id"] for r in ids]
    iris=[r["canonical_internal_iri"] for r in ids]
    identity_ok=len(idvals)==len(set(idvals)) and len(iris)==len(set(iris))
    add("IRI-001","IDENTITY","PASS" if identity_ok else "FAIL",
        f"ID uniqueness={len(idvals)==len(set(idvals))}; IRI uniqueness={len(iris)==len(set(iris))}.")

    eqc=list(formal.triples((None,OWL.equivalentClass,None)))
    eqp=list(formal.triples((None,OWL.equivalentProperty,None)))
    add("MAP-001","MAPPING_INTEGRITY","PASS" if not eqc and not eqp else "FAIL",
        f"Unapproved equivalence triples: class={len(eqc)}, property={len(eqp)}.")

    leaks="urn:semrisk:test:" in text
    mutable=bool(re.search(r"(githubusercontent|github\.com)[^\n]*(/main/|/master/|latest)", text, re.I))
    add("BOUNDARY-001","TEST_ISOLATION","PASS" if not leaks else "FAIL","No test namespace in canonical ontology sources." if not leaks else "Test namespace leaked into ontology sources.")
    add("DEP-001","DEPENDENCY_INTEGRITY","PASS" if not mutable else "FAIL","No mutable GitHub main/master/latest dependency in ontology source." if not mutable else "Mutable dependency detected.")

    bindings=(ROOT/EXT_BINDINGS).read_text(encoding="utf-8")
    pinned=("12b098158a9244179c5e0e2534cd85254a2d3b7e" in bindings and "W3C Recommendation 30 Apr 2013" in bindings and "W3C Recommendation 19 Oct 2017" in bindings)
    add("DEP-002","DEPENDENCY_INTEGRITY","PASS" if pinned else "FAIL","Pinned gUFO/PROV-O/OWL-Time bindings present." if pinned else "Required exact dependency binding missing.")

    shapes=parse_graph(SHAPES)
    ont=union_graph(MODULES)
    data=parse_graph(POSITIVE)
    conforms, report_g, report_txt=shacl_validate(data_graph=data, shacl_graph=shapes, ont_graph=ont, inference="none", advanced=False, meta_shacl=False)
    (BUILD/"shacl-positive-report.txt").write_text(str(report_txt),encoding="utf-8")
    add("SHACL-POS-001","SHACL","PASS" if conforms else "FAIL","Positive fixture conforms." if conforms else str(report_txt)[:1200])

    neg_pass=0
    for i,p in enumerate(NEGATIVES,1):
        dg=parse_graph(p)
        conforms, rg, txt=shacl_validate(data_graph=dg, shacl_graph=shapes, ont_graph=ont, inference="none", advanced=False, meta_shacl=False)
        (BUILD/f"shacl-negative-{i}.txt").write_text(str(txt),encoding="utf-8")
        if not conforms:
            neg_pass+=1
    add("SHACL-NEG-001","SHACL_NEGATIVE","PASS" if neg_pass==len(NEGATIVES) else "FAIL",
        f"{neg_pass}/{len(NEGATIVES)} known-negative SHACL fixtures failed as expected.")

    rg=parse_graph(POSITIVE)
    q=(ROOT/RULE).read_text(encoding="utf-8")
    constructed=rg.query(q)
    derived=Graph()
    for triple in constructed:
        derived.add(triple)
    expected=(URIRef("urn:semrisk:test:risk-001"),URIRef("urn:semrisk:entity:SR-REL-026"),URIRef("urn:semrisk:test:actor-001"))
    ok=expected in derived
    derived.serialize(destination=str(BUILD/"derived-owner.ttl"),format="turtle")
    add("RULE-001","RULE","PASS" if ok else "FAIL",f"Derived owner triple present={ok}; constructed triples={len(derived)}.")

    inventory=[]
    for p in MODULES+[SHAPES,RULE,POSITIVE]+NEGATIVES+["ontology/vendor/gufo-v1.0.0.ttl","ontology/catalog-v001.xml"]:
        inventory.append({"path":p,"sha256":sha256(ROOT/p),"bytes":(ROOT/p).stat().st_size})
    (BUILD/"inventory.json").write_text(json.dumps(inventory,indent=2,sort_keys=True),encoding="utf-8")
    add("INV-001","REPRODUCIBILITY","PASS",f"Checksum inventory generated for {len(inventory)} governed inputs.")

def run_post(reasoned):
    if not reasoned:
        add("REASON-POST-001","REASONING","NOT_RUN","No reasoned output supplied.")
        return
    p=Path(reasoned)
    if not p.exists():
        add("REASON-POST-001","REASONING","ERROR",f"Reasoned file not found: {p}")
        return
    g=Graph()
    g.parse(p)
    pairs=[
      ("SR-CPT-017","SR-CPT-013"),
      ("SR-CPT-018","SR-CPT-013"),
      ("SR-CPT-014","SR-CPT-013"),
      ("SR-CPT-015","SR-CPT-013"),
    ]
    miss=[]
    for a,b in pairs:
        if (URIRef("urn:semrisk:entity:"+a),RDFS.subClassOf,URIRef("urn:semrisk:entity:"+b)) not in g:
            miss.append(a+"<"+b)
    add("REASON-POST-001","REASONING","PASS" if not miss else "FAIL","Expected subclass entailments present." if not miss else "Missing: "+",".join(miss))

    # Release-critical named-class satisfiability check after HermiT classification.
    # An ontology can be globally consistent while still containing unsatisfiable
    # named classes, so this is recorded separately from consistency.
    unsat=set()
    for s,_,_ in g.triples((None,RDFS.subClassOf,OWL.Nothing)):
        if str(s).startswith("urn:semrisk:entity:"):
            unsat.add(str(s))
    for s,_,_ in g.triples((None,OWL.equivalentClass,OWL.Nothing)):
        if str(s).startswith("urn:semrisk:entity:"):
            unsat.add(str(s))
    add("REASON-SAT-001","REASONING_SATISFIABILITY","PASS" if not unsat else "FAIL",
        "No named SemRisk class classified as owl:Nothing." if not unsat else "Unsatisfiable named classes: "+",".join(sorted(unsat)))

    same=list(g.triples((URIRef("urn:semrisk:entity:SR-CPT-033"),OWL.equivalentClass,URIRef("urn:semrisk:entity:SR-CPT-001"))))
    add("REASON-NON-001","REASONING_NON_ENTAILMENT","PASS" if not same else "FAIL","Risk Register Entry is not equivalent to Risk.")

def emit(stage):
    commit=os.environ.get("GITHUB_SHA","LOCAL_UNBOUND")
    payload={
      "schema_version":"1.0",
      "candidate":"P1-R2 / 0.1.0-rc.1",
      "stage":stage,
      "commit":commit,
      "tools":{"python":platform.python_version(),"rdflib":rdflib.__version__,"pyshacl":pyshacl.__version__},
      "checks":checks,
      "inventory":{"path":"build/semantic-ci/inventory.json" if (BUILD/"inventory.json").exists() else None}
    }
    (BUILD/f"evidence-{stage}.json").write_text(json.dumps(payload,indent=2,sort_keys=True),encoding="utf-8")
    bad=[c for c in checks if c["status"] in {"FAIL","ERROR"}]
    print(json.dumps(payload,indent=2))
    return 1 if bad else 0

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("--stage",choices=["pre","post"],required=True)
    ap.add_argument("--reasoned")
    args=ap.parse_args()
    if args.stage=="pre":
        run_pre()
    else:
        run_post(args.reasoned)
    sys.exit(emit(args.stage))

if __name__=="__main__":
    main()
