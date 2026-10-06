# rc.4 offline formal documentation surfaces

This candidate binds the accepted rc.4 formal sources to two offline HTML views and a separate Wiki draft. It does not update the live Wiki, enable Pages, publish a manuscript or declare a scholarly release.

## Contents and authority

- `site/ontology/0.2.0-rc.4/index.html`: all 116 local declaration anchors and their named/literal asserted statements, with pinned source links.
- `site/ontology/0.2.0-rc.4/guide.html`: complete curated FD-A–FD-J content, navigation and 14 selected critical term commitments.
- `docs/wiki/rc4/Formal-Reference.md`: separately staged Wiki projection; the bundle includes the identical `wiki-draft.md`.
- `baseline-source-lock.json`: independently checked exact bd7 source Git blobs and SHA-256 values. Its digest is fixed in the builder; working-tree hash regeneration cannot relabel changed sources as the old commit.
- `surface-bindings.json`: route, source/output bindings and explicit publication states.
- `validation-results.json`: bounded structural checks and deliberately corrupted-source/navigation/history controls.

The count units remain distinct: 1,618 asserted closure triples, eight closure files, 116 local terms, 47 conceptual entries and 40 relation decisions. The generated term index omits anonymous-expression detail rather than inventing readable axioms; its complete graph/source links preserve that detail. It is not an entailment inventory or an ontology-quality score.

## Reproduce and verify

Install `requirements.txt`, then run:

1. `python tools/build_rc4_documentation_surfaces.py`
2. `python tools/check_rc4_documentation_surfaces.py`
3. `python tools/check_rc4_surface_history.py --base HEAD^` in a checkout with that commit available.
4. Preserve the existing historical checks: `build_pages_reference.py --check`, `check_pages_route_history.py` and `wiki_formal_parity_qa.py`.

The builder refuses to overwrite different existing output. History verification separately checks every previously frozen rc.4 output against the base commit. A semantic/source change needs a new source/version binding and review, not an in-place relabeling of this route.

The dedicated CI also renders desktop/mobile Chromium pages and exercises local term/guide/FD navigation. Browser screenshots must be inspected before recording visual acceptance. A browser smoke pass is not target-reader usability or live-surface validation.

## Retained gates

Live Wiki readback remains at the historical P1-R2 revision `f548d865885f74b39b20bbf055280af9f08eb136`. GitHub reports Pages disabled. Historical eight-page Wiki source and `/ontology/0.1.0-rc.1/` are preserved byte-for-byte. No new public Wiki revision or Pages URL is assigned here.

#115/#124 remain open for their broader contracts. #117 live deployment/backlinks, #55/#56 publication identity/availability, full model conformance and actual reader-route acceptance remain separate. #125 and external review remain deferred. No operational runtime work is included.
