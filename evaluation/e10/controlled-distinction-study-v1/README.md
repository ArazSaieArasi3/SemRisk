# Controlled distinction study v1

This is an information-loss diagnostic on the existing **constructed** pharmaceutical fixture at `1b0b96456845ce73e8deccc832ca9aeee81cd799`. The protocol, questions, expected answer sets and expected affected tasks were written before execution. It is not a benchmark against named ontologies, a user study, or independent case validation.

## Design
Four shared tasks retrieve (T1) risk versus workflow states, (T2) assessment/result history, (T3) evidence support role, and (T4) unchanged external entity identities. Three ablations remove only state links, history links, or evidence-role qualifications. Other facts remain. The restored control adds exactly the removed triples back before rerunning all tasks.

Acceptance requires exact set equality for the intact/restored controls, loss of the declared answer set for each ablated feature, and unchanged answers for the other tasks. Every actual answer and removed-triple count is saved. The input hash makes unnoticed fixture drift a failure.

Run from repository root: `python tools/run_distinction_study.py`. Pin the reported RDFLib version to reproduce. No network, private file, HermiT or SQL service is used. Historical native SQL↔SPARQL parity remains a separate eight-task result in `evaluation/parity/p49-parity-results-v1.0.csv`.

## Interpretation boundary
The diagnostic tests whether these explicit distinctions carry information needed by these questions. Information deletion is expected to lose answers; this is a sensitivity/control result, not a novel theorem or evidence that OWL is necessary. An adequately extended relational representation can preserve the same facts. No comparator has been run on this fixture. The study cannot establish exclusivity, overall superiority, semantic truth, organizational effectiveness, general temporal reasoning or clinical validity. Future core changes reopen the input binding and expected-answer review.
