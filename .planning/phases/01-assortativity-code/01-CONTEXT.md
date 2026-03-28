# Phase 1: Assortativity Code - Context

**Gathered:** 2026-03-28
**Status:** Ready for planning

<domain>
## Phase Boundary

Fix and verify all Part 1 assortativity computations. Write corrected code directly into Assignment2.ipynb (not into Part1.ipynb). The phase covers: country assortativity (Q1), configuration model (Q2-Q3), 100 random networks country assortativity (Q4), degree assortativity (Q5), and degree assortativity vs random networks (Q6). Reflection text (Q7-Q9) is Phase 2.

</domain>

<decisions>
## Implementation Decisions

### Q1: Country Assortativity Formula
- Implement Newman equation 2 for categorical attributes using full mixing matrix approach
- Build mixing matrix `e_ij` = fraction of edges connecting country i to country j
- Compute `r = (Tr(e) - ||e²||) / (1 - ||e²||)` where Tr(e) is sum of diagonal, ||e²|| is sum of squared row/column sums
- Do NOT use NetworkX implementation — manual formula required
- This replaces the existing code which incorrectly computes degree assortativity for Q1

### Edge Weights in Configuration Model
- Config model operates on unweighted graph topology (current behavior is correct)
- Swaps alter which nodes connect, not edge strength — preserving unweighted degree
- Degree assortativity function (Q5/Q6) correctly uses `weight='weight'` for weighted degree
- Country assortativity (Q1/Q4) counts edges, not weights — categorical attribute

### Missing Country Handling
- Exclude edges where either endpoint node has no country (country_map returns None)
- Only count edges between nodes with known country codes in the mixing matrix
- This applies to both the original network assortativity and the random network comparisons

### Q3 Comparison Bug Fix
- Current code sets `original_r = r` where `r` is degree assortativity from Q1, then compares against country assortativity of random networks
- Fix: compute country assortativity of the original network first using the manual formula, store as `original_country_r`, then compare against random networks' country assortativity

### Code Strategy
- Write corrected code directly into Assignment2.ipynb — skip fixing Part1.ipynb
- Reuse working code (graph construction, config model, degree assortativity) from Part1.ipynb
- Fix Q1 formula, fix Q3 comparison variable, add missing country handling

### Claude's Discretion
- Exact cell structure and splitting within Assignment2.ipynb
- Whether to add brief inline comments or keep code minimal
- Plot styling details (colors, figure size) as long as axes are labeled

</decisions>

<canonical_refs>
## Canonical References

**Downstream agents MUST read these before planning or implementing.**

### Source Code
- `Assignment2/Part1.ipynb` — Existing Part 1 code to base corrections on (graph construction, config model, degree assortativity all here)
- `Week8/part1.ipynb` — Part 2 TF-IDF code (not needed for Phase 1, but shares same graph)

### Data Files
- `Assignment2/D2_temp_papers.csv` — Paper dataset with author_ids column
- `Assignment2/final_authors.csv` — Author metadata with country_code column

### Assignment Spec
- GitHub: `lalessan/comsocsci2026/assignments/Assignment2.ipynb` — Official assignment questions and requirements

</canonical_refs>

<code_context>
## Existing Code Insights

### Reusable Assets
- Graph construction (pair_counts → weighted_edgelist → G): Working, reuse as-is
- `configuration_mode_swap(G)`: Working correctly for unweighted topology, reuse
- `degree_assortativity(G)`: Working correctly with weighted degrees, reuse for Q5/Q6
- Country mapping from `final_authors.csv`: Working, reuse

### Established Patterns
- Uses `defaultdict(int)` for pair counting
- Uses `tqdm` for progress on 100-network loops
- Matplotlib plots with `plt.axvline` for original value comparison

### Integration Points
- Graph `G` is shared across all questions — constructed once, used everywhere
- Country attributes must be set before Q1 (currently set before Q4 — move earlier)
- `authors_df` loaded from `final_authors.csv` — needed for country mapping

</code_context>

<specifics>
## Specific Ideas

- The Newman paper equation 2 for directed networks: r = (Tr(e) - ||e²||) / (1 - ||e²||). For undirected networks, the mixing matrix is symmetric, so this simplifies slightly.
- Country attributes currently assigned in the Part 3 section (cell `59825d2c`) — need to move this up before Q1 since Q1 now needs country info.

</specifics>

<deferred>
## Deferred Ideas

None — discussion stayed within phase scope

</deferred>

---

*Phase: 01-assortativity-code*
*Context gathered: 2026-03-28*
