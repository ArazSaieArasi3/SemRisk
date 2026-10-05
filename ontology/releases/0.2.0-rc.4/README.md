# SemRisk 0.2.0-rc.4 candidate

Seven version-bound modules retain 47 conceptual IDs (35 local classes, four markers, eight external/planned slots), with 40 registered relation decisions (39 local object properties and one metadata relation). Operational helpers remain 11 classes, 19 properties and seven controlled individuals.

The successor adds Exposure's subject/source links and classifies NumericScale as a subkind of issued ArtifactVersion. Read [decisions and migration boundaries](../../../foundational/exposure-scale-v0.2.0-rc.4/decisions.md). Exposure's existing relational table needs no migration; the new adapter is a bounded synthetic test. Scale/version/content and workflow relational parity remain separate work.

Run `python tools/build_exposure_scale_manifest.py --check` and `python tools/check_exposure_scale.py --assemble`. The dedicated workflow verifies actual OWL 2 DL/HermiT, the native exposure projection and complete editable diagram rebuild. Local results and later CI evidence are distinct. This is not a publication release, a final manuscript, empirical case or expert validation. Historical rc.1–rc.3 files are unchanged.
