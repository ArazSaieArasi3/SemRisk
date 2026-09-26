#!/usr/bin/env bash
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$ROOT"

WEBVOWL_REF="28e7dd9540622e8cb723dc000824b5eef5ae775f"
OWL2VOWL_REF="c6331c4c79b0034b8537a11cccd1a6587cedb0b9"
WORKDIR="${TMPDIR:-/tmp}/semrisk-webvowl-p1-r2"

rm -rf "$WORKDIR"
mkdir -p "$WORKDIR"

python - <<'PY'
import rdflib
assert rdflib.__version__ == "7.6.0", f"rdflib 7.6.0 required; got {rdflib.__version__}"
PY
python tools/build_p1_r2_webvowl_inputs.py

git clone https://github.com/VisualDataWeb/OWL2VOWL.git "$WORKDIR/owl2vowl"
git -C "$WORKDIR/owl2vowl" checkout "$OWL2VOWL_REF"
test "$(git -C "$WORKDIR/owl2vowl" rev-parse HEAD)" = "$OWL2VOWL_REF"
docker build -t semrisk-owl2vowl:c6331c4 "$WORKDIR/owl2vowl"

docker rm -f semrisk-owl2vowl >/dev/null 2>&1 || true
docker run -d --rm --name semrisk-owl2vowl -p 18080:8080 semrisk-owl2vowl:c6331c4 >/dev/null
trap 'docker rm -f semrisk-owl2vowl semrisk-webvowl >/dev/null 2>&1 || true' EXIT

for i in $(seq 1 50); do
  curl -sf http://127.0.0.1:18080/serverTimeStamp >/dev/null && break
  sleep 3
done

mkdir -p build/webvowl/json
curl -sf -X POST   -F "ontology=@build/webvowl/p1-r2-webvowl-local.ttl"   -F "sessionId=semrisk-local"   http://127.0.0.1:18080/convert   -o build/webvowl/json/p1-r2-local-webvowl.json
curl -sf -X POST   -F "ontology=@build/webvowl/p1-r2-webvowl-import-closure.ttl"   -F "sessionId=semrisk-imports"   http://127.0.0.1:18080/convert   -o build/webvowl/json/p1-r2-imports-webvowl.json

python tools/qa_p1_r2_webvowl_json.py build/webvowl/json/p1-r2-local-webvowl.json --scope local
python tools/qa_p1_r2_webvowl_json.py build/webvowl/json/p1-r2-imports-webvowl.json --scope imports

git clone https://github.com/VisualDataWeb/WebVOWL.git "$WORKDIR/webvowl"
git -C "$WORKDIR/webvowl" checkout "$WEBVOWL_REF"
test "$(git -C "$WORKDIR/webvowl" rev-parse HEAD)" = "$WEBVOWL_REF"
docker build -t semrisk-webvowl:v1.1.7 "$WORKDIR/webvowl"

docker rm -f semrisk-webvowl >/dev/null 2>&1 || true
docker run -d --rm --name semrisk-webvowl -p 18081:8080 semrisk-webvowl:v1.1.7 >/dev/null
for i in $(seq 1 40); do
  curl -sf http://127.0.0.1:18081/ >/dev/null && break
  sleep 3
done

cat <<'EOF'
SEM_RISK_WEBVOWL_LOCAL_READY
Viewer: http://127.0.0.1:18081/
Preferred JSON: build/webvowl/json/p1-r2-local-webvowl.json
Import-context JSON: build/webvowl/json/p1-r2-imports-webvowl.json

Use WebVOWL's file-open control to load the preferred JSON first.
This is an offline derived visualization. Do not publish it as the canonical ontology.
EOF

# Keep containers alive while this shell remains open.
wait
