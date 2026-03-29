# Requirements: DTU 02467 Assignment 2

**Defined:** 2026-03-28
**Core Value:** Every question answered completely with running code, rendered plots, and precise written analysis

## v1 Requirements

### Assortativity (Part 1)

- [x] **ASRT-01**: Calculate country-based assortativity coefficient using manual formula (equation 2 from Newman paper) — not NetworkX
- [x] **ASRT-02**: Implement configuration model via double edge swap algorithm (steps a-f from assignment)
- [x] **ASRT-03**: Verify configuration model preserves degree sequence
- [x] **ASRT-04**: Generate 100 random networks, compute country assortativity for each, plot distribution, compare with original
- [x] **ASRT-05**: Calculate degree assortativity using lecture formula
- [x] **ASRT-06**: Compare degree assortativity against 100 random networks, analyze hub-to-hub connection tendency

### Reflections (Part 1)

- [x] **REFL-01**: Written analysis — were degree assortativity results expected? Why/why not?
- [x] **REFL-02**: Written analysis — why is edge flipping (50% direction flip) included in configuration model?
- [x] **REFL-03**: Written analysis — describe distribution of degree assortativity in random networks, discuss theoretical expectations

### TF-IDF (Part 2)

- [ ] **TFID-01**: Explain TF-IDF in own words (what is TF? what is IDF?)
- [x] **TFID-02**: Create large token documents per community using pandas groupby/explode
- [x] **TFID-03**: Calculate TF for top 5 communities, list top 5 terms, discuss similarities/differences, explain why TF alone is insufficient, state log base choice
- [x] **TFID-04**: Calculate TF-IDF for top 9 communities — list top 10 TF words, top 10 TF-IDF words, top 3 authors by degree, discuss whether TF-IDF is more descriptive and why IDF helps

### Visualization (Part 2)

- [ ] **VIZN-01**: Generate word cloud per community with top 3 author names displayed
- [ ] **VIZN-02**: Comment on results — what do sub-communities reveal about Computational Social Science?
- [ ] **VIZN-03**: Look up top author per community online, discuss whether results make sense

### Reflection (Part 2)

- [ ] **CSCI-01**: Reflection — has understanding of Computational Social Science field changed? How?

### Notebook Assembly

- [x] **ASBL-01**: Merge Part 1 and Part 2 into single Assignment2.ipynb
- [x] **ASBL-02**: First cell contains repo link and contribution statement
- [x] **ASBL-03**: Each question repeated as markdown header before its answer
- [x] **ASBL-04**: Code split by question (not monolithic cells)
- [x] **ASBL-05**: All plots have labeled axes, titles, and explanatory text
- [x] **ASBL-06**: Notebook runs end-to-end with Kernel > Restart & Run All
- [x] **ASBL-07**: No long outputs — minimize prints, control display length

## v2 Requirements

None — single assignment delivery.

## Out of Scope

| Feature | Reason |
|---------|--------|
| Original data collection | Reuse CSVs from prior weeks |
| Community detection | Reuse Week 6 results |
| Tokenization implementation | Reuse Week 7/8 code |
| Interactive visualizations | Static matplotlib sufficient |

## Traceability

| Requirement | Phase | Status |
|-------------|-------|--------|
| ASRT-01 | Phase 1 | Complete |
| ASRT-02 | Phase 1 | Complete |
| ASRT-03 | Phase 1 | Complete |
| ASRT-04 | Phase 1 | Complete |
| ASRT-05 | Phase 1 | Complete |
| ASRT-06 | Phase 1 | Complete |
| REFL-01 | Phase 2 | Complete |
| REFL-02 | Phase 2 | Complete |
| REFL-03 | Phase 2 | Complete |
| TFID-01 | Phase 4 | Pending |
| TFID-02 | Phase 3 | Complete |
| TFID-03 | Phase 3 | Complete |
| TFID-04 | Phase 3 | Complete |
| VIZN-01 | Phase 4 | Pending |
| VIZN-02 | Phase 4 | Pending |
| VIZN-03 | Phase 4 | Pending |
| CSCI-01 | Phase 4 | Pending |
| ASBL-01 | Phase 5 | Complete |
| ASBL-02 | Phase 5 | Complete |
| ASBL-03 | Phase 5 | Complete |
| ASBL-04 | Phase 5 | Complete |
| ASBL-05 | Phase 5 | Complete |
| ASBL-06 | Phase 5 | Complete |
| ASBL-07 | Phase 5 | Complete |

**Coverage:**
- v1 requirements: 24 total
- Mapped to phases: 24
- Unmapped: 0

---
*Requirements defined: 2026-03-28*
*Last updated: 2026-03-28 — REFL-01, REFL-02, REFL-03 marked complete after Phase 2 execution*
