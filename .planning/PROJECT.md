# DTU 02467 — Assignment 2: Computational Social Science

## What This Is

Assignment 2 for DTU course 02467 (Computational Social Science, Spring 2026). A group project (Lovro, Oskar, Uffe) delivering a single Jupyter notebook (`Assignment2.ipynb`) that analyzes a co-authorship network of computational social scientists using mixing patterns, assortativity, TF-IDF, and word clouds.

## Core Value

Every question in the assignment is answered completely — code runs end-to-end, plots render with proper labels, and written analysis is precise, data-supported, and concise.

## Requirements

### Validated

(None yet — ship to validate)

### Active

- [ ] Part 1: Assortativity coefficient by country (manual formula, not NetworkX)
- [ ] Part 1: Configuration model via double edge swap
- [ ] Part 1: 100 random networks — country assortativity distribution + comparison
- [ ] Part 1: Degree assortativity (manual formula)
- [ ] Part 1: Degree assortativity vs 100 random networks + analysis
- [ ] Part 1: Reflection Q7 — degree assortativity expectations
- [ ] Part 1: Reflection Q8 — why edge flipping is needed
- [ ] Part 1: Reflection Q9 — distribution of assortativity in random networks
- [ ] Part 2 Ex1 Q1: TF-IDF explanation (what is TF? what is IDF?)
- [ ] Part 2 Ex1 Q2: Create large documents per community
- [ ] Part 2 Ex1 Q3: Top 5 TF terms for top 5 communities + analysis
- [ ] Part 2 Ex1 Q4: TF-IDF for top 9 communities + analysis
- [ ] Part 2 Ex2: Word clouds per community + commentary + author lookup
- [ ] Part 2 Ex3: Reflection on computational social science field
- [ ] Assembly: Merge into single Assignment2.ipynb with question headers
- [ ] Formatting: Axis labels, clean outputs, contribution statement, repo link

### Out of Scope

- Original data collection — uses existing CSVs from prior weeks
- Week 7 tokenization work — reuse existing implementation
- Community detection — reuse Week 6 results (author_communities.csv)

## Context

- **Existing code:** Part 1 code is complete in `Assignment2/Part1.ipynb`. Part 2 code is largely complete in `Week8/part1.ipynb`.
- **Data files:** `D2_temp_papers.csv`, `final_authors.csv` (in Assignment2/), `author_communities.csv` (in Week6/)
- **Key issues found:**
  1. Part 1 Q1 computes degree assortativity but assignment asks for country assortativity with manual formula — needs verification
  2. IDF in Week8/part1.ipynb is computed over 5 communities but used for TF-IDF over 9 — needs fix
  3. All Part 2 written analysis (explanations, comparisons, reflections) is missing
- **Dependencies:** NetworkX, pandas, matplotlib, nltk, wordcloud, numpy
- **Repo:** https://github.com/oggefaderen/CompSci.git

## Constraints

- **Deadline:** Apr 7, 2026 at 23:59
- **Format:** Single Jupyter notebook named `Assignment2.ipynb`
- **Style:** Objective language (no "I think"), data-supported observations, questions repeated before answers, code split by question
- **Platform:** Jupyter notebook, Python, must run with Kernel > Restart & Run All

## Key Decisions

| Decision | Rationale | Outcome |
|----------|-----------|---------|
| Reuse Week 6 community assignments | Assignment builds on prior exercise work | — Pending |
| Manual assortativity formula | Assignment explicitly forbids nx implementation for Q1 | — Pending |
| Use existing Part1.ipynb + Week8/part1.ipynb as base | Code is largely complete, just needs assembly and text | — Pending |

---
*Last updated: 2026-03-28 after initialization*
