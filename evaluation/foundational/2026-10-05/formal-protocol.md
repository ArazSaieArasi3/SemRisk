# Declared formal hypotheses and reproduction

This protocol separates profile membership, logical consistency, named data completeness, entailment and non-entailment. It is supplementary Verification/Assurance evidence under the recorded VVEAA contract, not independent Validation or empirical utility.

| Probe | Input | Required observation |
|---|---|---|
| Positive DL/consistency | Seven successor modules, exact local gUFO closure, temporal fixture and named-participant fixture | OWL 2 DL and HermiT success |
| Two class entailments | Responsibility asserted only as `ac:GroundedRiskResponsibility` | `SR-CPT-031` and `gufo:Relator` types absent from input and present in reasoner-generated ClassAssertion output |
| Missing named witness | Remove named counterpart and explicit distinctness from the positive world | HermiT remains consistent under OWA; the corresponding stricter shape case rejects missing evidence |
| Non-entailment countermodel | Assert the risk individual belongs to the complement of Endurant in an otherwise positive world | HermiT success establishes a countermodel to forcing that Risk individual to be an Endurant |
| Contradictory category | One participant asserted as both Endurant and Event | Nonzero reasoner exit and an inconsistency-specific log; network/tool failures do not count as success |

The fixtures are four separate worlds. The countermodel is a logical test, not a claim that every real risk must be non-endurant. The named-witness shape intentionally targets only the new opt-in helper. No named counterpart is fabricated for existing data. The 29 structural/shape tasks and their seven negative cases are not added to the original 40 competency questions.

## Exact execution

- Python and dependency pins: `.github/workflows/paper1-foundational-revision.yml` and `tools/requirements-qualified-context.txt` (RDFLib 7.6.0, pySHACL 0.40.1).
- ROBOT **1.9.10**, JAR SHA-256 `16a73c074f3df359a7338a84b4e0788785fe06117f931bb9796e9619ea776105`, Java 17. Bundled HermiT metadata is extracted from the actual JAR and recorded in CI; no independent installation/version is guessed.
- `python tools/build_foundational_candidate.py --check --assemble` binds all imports offline and creates isolated formal probes.
- `python tools/check_foundational_revision.py --write` executes source-delta, inventory, SHACL and ownership-preservation checks.
- The workflow supplies the exact ROBOT commands. For positive entailments it explicitly selects `SubClass ClassAssertion` with indirect assertions included; default subclass-only output is insufficient.
- CI retains the input closures, reasoned output, assembly metadata, negative log and local result JSON. The committed CI evidence binds the observed run and commit; candidate-head CI and merge readback are separate checkpoints.

No inference runtime or scalability claim follows from these small fixtures. The old temporal pipeline still executes native PostgreSQL and its guarded migration/round-trip tasks independently. New named-counterpart evidence is not claimed to round-trip through V007.

## Original references and operational documentation

1. B. Glimm, I. Horrocks, B. Motik, G. Stoilos, and Z. Wang, “HermiT: An OWL 2 Reasoner,” *Journal of Automated Reasoning*, 2014. Author publication metadata: https://www.cs.ox.ac.uk/people/ian.horrocks/Publications/horrocks2014_bib.html ; author manuscript: https://www.cs.ox.ac.uk/people/boris.motik/pubs/ghmsw14HermiT.pdf .
2. R. C. Jackson, J. P. Balhoff, E. Douglass, N. L. Harris, C. J. Mungall, and J. A. Overton, “ROBOT: A Tool for Automating Ontology Workflows,” *BMC Bioinformatics*, vol. 20, article 407, 2019, doi:10.1186/s12859-019-3002-3. https://link.springer.com/article/10.1186/s12859-019-3002-3
3. ROBOT, “Reason,” sections Logical Validation and Generated Axioms. https://robot.obolibrary.org/reason
4. ROBOT, “Validate Profile.” https://robot.obolibrary.org/validate-profile
5. W3C, *Shapes Constraint Language (SHACL)*, Recommendation, 2017. https://www.w3.org/TR/shacl/

P15 should cite the original methods and summarize only the claim-relevant outcomes, using the single consolidated result table. Full command and failure logs belong in this companion evidence package.
