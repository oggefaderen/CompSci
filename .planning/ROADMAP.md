# Roadmap: DTU 02467 Assignment 2

## Overview

The assignment delivers a single Jupyter notebook (`Assignment2.ipynb`) covering assortativity analysis (Part 1) and TF-IDF/word cloud analysis (Part 2). Existing code in Part1.ipynb and Week8/part1.ipynb provides the foundation but has correctness gaps and missing written analysis. The phases move from fixing code to writing analysis to final assembly — each phase produces a coherent, verifiable chunk of the finished notebook.

## Phases

**Phase Numbering:**
- Integer phases (1, 2, 3): Planned milestone work
- Decimal phases (2.1, 2.2): Urgent insertions (marked with INSERTED)

Decimal phases appear between their surrounding integers in numeric order.

- [ ] **Phase 1: Assortativity Code** - Part 1 code is verified correct and produces valid outputs for all six assortativity requirements
- [ ] **Phase 2: Part 1 Reflections** - All three written reflection answers for Part 1 are complete
- [ ] **Phase 3: TF-IDF Implementation** - IDF bug fixed, TF-IDF code runs correctly, Q3 and Q4 analysis written
- [ ] **Phase 4: Part 2 Writing and Word Clouds** - TF-IDF explanation, word cloud code, all Part 2 commentary, and field reflection written
- [ ] **Phase 5: Notebook Assembly** - All work merged into Assignment2.ipynb, runs end-to-end, meets formatting requirements

## Phase Details

### Phase 1: Assortativity Code
**Goal**: Part 1 code computes country assortativity and degree assortativity correctly using manual formulas, with a working configuration model that generates and compares 100 random networks
**Depends on**: Nothing (first phase)
**Requirements**: ASRT-01, ASRT-02, ASRT-03, ASRT-04, ASRT-05, ASRT-06
**Success Criteria** (what must be TRUE):
  1. Country assortativity is computed using Newman equation 2 (manual formula, not NetworkX) and outputs a single numeric value
  2. Configuration model generates a randomized network via double edge swap and the degree sequence before and after is identical
  3. A plot of country assortativity distribution over 100 random networks renders, with the original network's value marked visually
  4. Degree assortativity is computed using the lecture formula and outputs a value that can be compared against the random network baseline
  5. A plot of degree assortativity distribution over 100 random networks renders, with the original value marked
**Plans**: 2 plans

Plans:
- [x] 01-01-PLAN.md — Foundation cells + Q1 country assortativity (Newman eq. 2)
- [ ] 01-02-PLAN.md — Q2 config model, Q3 country distribution, Q4 degree assort, Q5 degree distribution

### Phase 2: Part 1 Reflections
**Goal**: The three written reflection questions (Q7, Q8, Q9) are answered in the notebook with precise, data-supported prose
**Depends on**: Phase 1
**Requirements**: REFL-01, REFL-02, REFL-03
**Success Criteria** (what must be TRUE):
  1. Q7 answer explains whether degree assortativity results were expected, citing the computed values and what they imply about hub-to-hub connections
  2. Q8 answer explains why edge direction is flipped 50% of the time in the configuration model, with a mechanistic justification
  3. Q9 answer describes the shape of the random network assortativity distribution and connects it to theoretical expectations
**Plans**: TBD

### Phase 3: TF-IDF Implementation
**Goal**: The IDF computation bug is fixed, TF-IDF code runs correctly over all required communities, and written analysis for Q3 and Q4 is complete
**Depends on**: Phase 1
**Requirements**: TFID-02, TFID-03, TFID-04
**Success Criteria** (what must be TRUE):
  1. Community documents are created by groupby/explode over all communities (not just 5), so IDF is computed over the full corpus
  2. Top 5 TF terms are listed for each of the top 5 communities, with written analysis explaining similarities, differences, and why TF alone is insufficient
  3. Top 10 TF words and top 10 TF-IDF words are listed for each of the top 9 communities, with top 3 authors by degree identified per community
  4. Written analysis for Q4 explains whether TF-IDF is more descriptive than TF alone and why IDF improves specificity
**Plans**: TBD

### Phase 4: Part 2 Writing and Word Clouds
**Goal**: TF-IDF concept explanation, word cloud visualizations, community commentary, and field reflection are all complete
**Depends on**: Phase 3
**Requirements**: TFID-01, VIZN-01, VIZN-02, VIZN-03, CSCI-01
**Success Criteria** (what must be TRUE):
  1. TF-IDF explanation in own words defines both TF and IDF clearly, including the log base choice for TF
  2. A word cloud renders for each community with the top 3 author names displayed alongside it
  3. Commentary on word clouds explains what sub-communities reveal about the Computational Social Science field
  4. Top author per community has been looked up online and results are discussed (do they make sense given the community's terms?)
  5. Field reflection explains whether understanding of Computational Social Science has changed after the analysis, with a concrete stance
**Plans**: TBD

### Phase 5: Notebook Assembly
**Goal**: All code and writing is merged into a single Assignment2.ipynb that runs end-to-end, meets all formatting requirements, and is ready to submit
**Depends on**: Phase 4
**Requirements**: ASBL-01, ASBL-02, ASBL-03, ASBL-04, ASBL-05, ASBL-06, ASBL-07
**Success Criteria** (what must be TRUE):
  1. Assignment2.ipynb exists as a single file containing all Part 1 and Part 2 content with question text repeated as markdown headers before each answer
  2. First cell contains repo link and contribution statement (listing Lovro, Oskar, Uffe)
  3. Kernel > Restart & Run All completes without errors and all plots render
  4. All plots have labeled axes, titles, and are accompanied by explanatory text
  5. No cell produces excessively long output (prints minimized, display length controlled)
**Plans**: TBD

## Progress

**Execution Order:**
Phases execute in numeric order: 1 → 2 → 3 → 4 → 5

Note: Phase 2 (reflections) and Phase 3 (TF-IDF) are independent after Phase 1 — they can be worked in parallel if desired.

| Phase | Plans Complete | Status | Completed |
|-------|----------------|--------|-----------|
| 1. Assortativity Code | 1/2 | In Progress|  |
| 2. Part 1 Reflections | 0/TBD | Not started | - |
| 3. TF-IDF Implementation | 0/TBD | Not started | - |
| 4. Part 2 Writing and Word Clouds | 0/TBD | Not started | - |
| 5. Notebook Assembly | 0/TBD | Not started | - |
