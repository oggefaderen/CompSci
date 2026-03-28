# Phase 3: TF-IDF Implementation - Context

**Gathered:** 2026-03-28
**Status:** Ready for planning

<domain>
## Phase Boundary

Fix IDF bug, complete TF-IDF code for Q2-Q4, and write analysis for Q3 and Q4. Append all cells to Assignment2.ipynb after Part 1 content. This phase covers the code and analysis for Exercise 1 questions 2-4. Exercise 1 Q1 (TF-IDF explanation) and Exercise 2-3 (word clouds, commentary, reflection) are Phase 4.

</domain>

<decisions>
## Implementation Decisions

### IDF Bug Fix
- Compute IDF across ALL communities (all 13), not just top 5
- N = total number of communities with tokens (exclude community 12 which has 0 tokens)
- Document frequency (df) counts how many of ALL communities contain a given word
- Use natural log (math.log) — state this choice in Q3 analysis
- Recompute TF-IDF after fixing IDF so Q4 results are correct

### Data Paths
- Copy author_communities.csv into Assignment2/ folder so notebook is self-contained
- All data paths use relative paths within Assignment2/ (e.g., `./author_communities.csv`, `./D2_temp_papers.csv`)
- Do NOT reference ../Week5/ or ../Week6/ paths

### Q3 Written Analysis
- 120-150 words, analytical objective tone, full question text as header
- Must cover: similarities between top 5 communities' TF terms, differences, why TF alone is insufficient (generic words dominate), log base choice and whether it matters
- Placeholder values for specific term lists if needed

### Q4 Written Analysis
- 120-150 words, analytical objective tone, full question text as header
- Must cover: are TF-IDF words more descriptive than TF? What role does IDF play in filtering generic terms?
- Reference specific community examples to support the argument

### Code Structure
- Reuse working code from Week8/part1.ipynb as base
- Split code into separate cells per question (Q2, Q3, Q4) matching the established pattern
- Each question gets a markdown header cell with full question text, then code cell(s), then analysis markdown cell

### Claude's Discretion
- Exact cell splitting and ordering
- Whether to show community token counts inline or as a table
- Plot styling for any visualizations in this phase

</decisions>

<canonical_refs>
## Canonical References

**Downstream agents MUST read these before planning or implementing.**

### Source Code
- `Week8/part1.ipynb` — Existing TF-IDF code to adapt (cells 37bbaeb9 through f9baef8e)
- `Assignment2/Assignment2.ipynb` — Target file, append after Phase 2 reflection cells

### Data Files
- `Assignment2/D2_temp_papers.csv` — Paper dataset with abstracts (already exists)
- `Assignment2/final_authors.csv` — Author metadata (already exists)
- `Week6/author_communities.csv` — Community assignments (MUST be copied to Assignment2/)

### Assignment Spec
- GitHub: `lalessan/comsocsci2026/assignments/Assignment2.ipynb` — Exercise 1 Q2-Q4 requirements

</canonical_refs>

<code_context>
## Existing Code Insights

### Reusable Assets
- `inverted_index_to_text()` function: converts abstract inverted index to plain text — reuse as-is
- `tokenize()` function: lowercase + stopword/punctuation removal — reuse as-is
- Community document creation via `merged.groupby('community')['text'].apply(...)` — reuse as-is
- TF calculation via Counter — reuse as-is
- TF-IDF display loop (top 10 TF, top 10 TF-IDF, top 3 authors) — reuse structure, fix IDF

### Bug to Fix
- Cell `09f20394`: `N = len(top_communities)` where top_communities = 5, but IDF is used for TF-IDF over 9 communities
- Fix: compute IDF with N = number of all non-empty communities, df counts across all communities

### Established Patterns
- Assignment2.ipynb uses `## Q{N}:` headers with full question text
- nltk for tokenization, Counter for term frequencies, math.log for IDF

### Integration Points
- Part 2 content starts after the last Phase 2 cell (q9-reflection)
- Needs new imports: nltk, string, Counter, math (add to a new imports cell or extend existing)
- community_df loaded from ./author_communities.csv

</code_context>

<specifics>
## Specific Ideas

- The assignment says "exploit pandas builtin functions such as groupby.apply or explode" for Q2 — make sure the code uses these
- Q3 asks about log base — state we use natural log and note that the base is a scaling factor that doesn't change the ranking of terms

</specifics>

<deferred>
## Deferred Ideas

None — discussion stayed within phase scope

</deferred>

---

*Phase: 03-tf-idf-implementation*
*Context gathered: 2026-03-28*
