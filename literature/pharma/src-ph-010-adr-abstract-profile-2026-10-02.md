# SRC-PH-010 bounded pharmacovigilance profile

**Owner:** #15. Henegar et al., *Building an ontology of adverse drug reactions for automated signal generation in pharmacovigilance*, Computers in Biology and Medicine 36(7–8), 748–767 (2006). DOI `10.1016/j.compbiomed.2005.04.009`. Online date 2005-09-26 and issue year 2006 are different publication events, not duplicate studies.

**Inspected evidence:** [PubMed 16185681](https://pubmed.ncbi.nlm.nih.gov/16185681/) and its [Europe PMC core record](https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID:16185681%20AND%20SRC:MED&format=json&resultType=core), abstract/identity, 2026-10-02. The publisher full-text route was not retrieved; section/figure/table extraction remains open.

**Source facts, paraphrased:** the authors construct an ADR ontology using MedDRA terminology. Subsumption and approximate matching support grouping related medical conditions. The abstract reports improved signal generation and substantial modeling effort; it supplies no inspected effect-size denominator here.

**SemRisk decisions:** terminology, ADR event and detected signal must not be conflated. Route these as future pharmacovigilance profile/method candidates, with no new Core classes or MedDRA redistribution. Do not infer exact classes, axioms, sensitivity/specificity, independent validation or a reusable formal release from the abstract. This evidence narrows generic signal-ontology novelty; it does not validate the bounded shortage case.

**Disposition:** ABSTRACT_PROFILED / FULLTEXT_UNMINED / ARTIFACT_UNBOUND. #15 remains open.
