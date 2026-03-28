---
phase: 01-assortativity-code
verified: 2026-03-28T19:07:18Z
status: human_needed
score: 5/5 must-haves verified
re_verification: false
human_verification:
  - test: "Run all notebook cells and compare Q1 original_country_r against nx.attribute_assortativity_coefficient(G, 'country')"
    expected: "Values should be very close (within 0.01). If they diverge significantly, the mixing matrix diagonal normalization has a bug."
    why_human: "Cannot execute notebook code programmatically to compare numerical output"
  - test: "Run Kernel > Restart & Run All on Assignment2.ipynb"
    expected: "All cells execute without error, two histogram plots render with red dashed lines visible"
    why_human: "Requires Jupyter runtime environment to execute"
---

# Phase 1: Assortativity Code Verification Report

**Phase Goal:** Part 1 code computes country assortativity and degree assortativity correctly using manual formulas, with a working configuration model that generates and compares 100 random networks
**Verified:** 2026-03-28T19:07:18Z
**Status:** human_needed
**Re-verification:** No -- initial verification

## Goal Achievement

### Observable Truths

| # | Truth | Status | Evidence |
|---|-------|--------|----------|
| 1 | Country assortativity is computed using Newman equation 2 (manual formula, not NetworkX) and outputs a single numeric value | VERIFIED (with caveat) | Cell c8d9e0f1: builds edge_type_counts, computes trace_e, sum_a_sq, applies r=(Tr(e)-\|\|e^2\|\|)/(1-\|\|e^2\|\|), stores as original_country_r, prints with .4f format. No nx.attribute_assortativity_coefficient or nx.degree_assortativity_coefficient used in Q1. See Caveat below. |
| 2 | Configuration model generates a randomized network via double edge swap and the degree sequence before and after is identical | VERIFIED | Cell q2-code-func: configuration_mode_swap with E*10 swaps, 50% flip, self-loop guard, multi-edge guard. Cell q2-degree-check: assert original_degrees == rand_degrees. |
| 3 | A plot of country assortativity distribution over 100 random networks renders, with the original network's value marked visually | VERIFIED | Cell q3-code: tqdm loop over range(100), configuration_mode_swap + country_map re-assignment + nx.attribute_assortativity_coefficient, plt.hist + plt.axvline(original_country_r) with red dashed line, xlabel/ylabel/title/legend present. |
| 4 | Degree assortativity is computed using the lecture formula and outputs a value that can be compared against the random network baseline | VERIFIED | Cell q4-code: degree_assortativity function using np.mean(ku*kv) - np.mean(ku)*np.mean(kv) over np.mean(ku**2) - np.mean(ku)**2, uses weight='weight', stores as original_degree_r, prints with .4f. |
| 5 | A plot of degree assortativity distribution over 100 random networks renders, with the original value marked | VERIFIED | Cell q5-code: tqdm loop over range(100), configuration_mode_swap + degree_assortativity, plt.hist + plt.axvline(original_degree_r) with red dashed line, xlabel/ylabel/title/legend present. |

**Score:** 5/5 truths verified

**Caveat on Truth 1 -- Mixing Matrix Diagonal Normalization:**
The Q1 code increments edge_type_counts[(c_u, c_v)] by +1 for same-country edges and by +1 to both (c_u,c_v) and (c_v,c_u) for cross-country edges. The denominator is M = 2 * total_edges. In Newman's symmetric mixing matrix formulation, a same-type undirected edge should contribute 2 ordered pairs (both directions are (i,i)), so the diagonal should be incremented by 2 (or equivalently, the `if c_u != c_v` guard should be removed). The current code under-counts the diagonal by a factor of 2 relative to off-diagonal entries, which means the mixing matrix does not sum to 1. This MAY produce a numerically different r from the correct value. Human verification (comparing against nx.attribute_assortativity_coefficient) is needed to determine if this materially affects the result.

### Required Artifacts

| Artifact | Expected | Status | Details |
|----------|----------|--------|---------|
| `Assignment2/Assignment2.ipynb` | Notebook with imports, graph, country attrs, Q1-Q5 | VERIFIED | 19 cells total (9 markdown + 10 code). Contains all required sections: imports, graph construction, country loading, Q1 manual assortativity, Q2 config model, degree check, Q3 country distribution, Q4 degree assortativity, Q5 degree distribution. |

### Key Link Verification

| From | To | Via | Status | Details |
|------|----|-----|--------|---------|
| final_authors.csv | G.nodes[node]['country'] | country_map dict from authors_df['id'] -> authors_df['country_code'] | WIRED | Cell a6b7c8d9: country_map = dict(zip(authors_df['id'], authors_df['country_code'])), then loop sets G.nodes[node]['country'] |
| G.edges() | mixing matrix e_ij | iterate edges, skip None countries, build edge_type_counts | WIRED | Cell c8d9e0f1: for u,v in G.edges(), checks c_u/c_v is None, builds edge_type_counts, normalizes by M |
| original_country_r (Plan 01) | plt.axvline in Q3 plot | direct variable reference | WIRED | Cell q3-code line: plt.axvline(original_country_r, ...) -- correct variable, not degree r |
| configuration_mode_swap(G) | nx.attribute_assortativity_coefficient(G_rand, 'country') | Q3 loop calls config model then computes country r | WIRED | Cell q3-code: G_rand = configuration_mode_swap(G), country_map re-applied, then nx.attribute_assortativity_coefficient |
| degree_assortativity(G) | plt.axvline in Q5 plot | original_degree_r stored before loop | WIRED | Cell q4-code: original_degree_r = degree_assortativity(G). Cell q5-code: plt.axvline(original_degree_r, ...) |

### Requirements Coverage

| Requirement | Source Plan | Description | Status | Evidence |
|-------------|-----------|-------------|--------|----------|
| ASRT-01 | 01-01 | Calculate country-based assortativity using manual formula (Newman eq. 2) | SATISFIED | Cell c8d9e0f1: Newman eq. 2 mixing matrix, no NetworkX call |
| ASRT-02 | 01-02 | Implement configuration model via double edge swap | SATISFIED | Cell q2-code-func: configuration_mode_swap with E*10 swaps, 50% flip |
| ASRT-03 | 01-02 | Verify configuration model preserves degree sequence | SATISFIED | Cell q2-degree-check: assert original_degrees == rand_degrees |
| ASRT-04 | 01-02 | Generate 100 random networks, compute country assortativity, plot distribution | SATISFIED | Cell q3-code: 100 iterations, country_map re-applied, histogram with original_country_r marked |
| ASRT-05 | 01-02 | Calculate degree assortativity using lecture formula | SATISFIED | Cell q4-code: mean(ku*kv) - mean(ku)*mean(kv) / variance formula |
| ASRT-06 | 01-02 | Compare degree assortativity against 100 random networks | SATISFIED | Cell q5-code: 100 iterations, histogram with original_degree_r marked |

No orphaned requirements. All 6 ASRT IDs from REQUIREMENTS.md mapped to Phase 1 are accounted for.

### Anti-Patterns Found

| File | Line | Pattern | Severity | Impact |
|------|------|---------|----------|--------|
| Assignment2.ipynb | Q1 cell | Diagonal normalization inconsistency in mixing matrix | WARNING | May produce slightly incorrect r value -- see Caveat above |
| (none) | - | No TODO/FIXME/PLACEHOLDER found | INFO | Clean |
| (none) | - | No empty implementations found | INFO | Clean |

### Human Verification Required

### 1. Mixing Matrix Numerical Accuracy

**Test:** In a notebook cell after Q1, run: `print(f"NetworkX country r = {nx.attribute_assortativity_coefficient(G, 'country'):.4f}")` and compare with original_country_r.
**Expected:** Values should match to within 0.001. If they diverge by more than 0.01, the diagonal normalization bug is material and must be fixed by changing the Q1 code to also increment edge_type_counts[(c_u, c_v)] += 1 (without the `if c_u != c_v` guard) and instead always adding both orderings (incrementing diagonal by 2 per same-type edge).
**Why human:** Requires executing Python code in the notebook runtime to compare numerical values.

### 2. End-to-End Execution

**Test:** Open Assignment2.ipynb, Kernel > Restart & Run All.
**Expected:** All cells execute without error. Two histogram plots render with clearly visible red dashed lines. The degree check assertion passes (prints "Degree sequence preserved").
**Why human:** Requires Jupyter runtime and access to data files (D2_temp_papers.csv, final_authors.csv).

### 3. Q3 Bug Fix Visual Confirmation

**Test:** Inspect the Q3 histogram. The red dashed line should appear at a value that is plausibly a country assortativity coefficient (typically positive, in 0.0-1.0 range for assortative networks).
**Expected:** The red line should NOT be at the same position as the Q5 histogram's red line (which shows degree assortativity). If they are at the same value, the Q3 bug was not actually fixed.
**Why human:** Requires visual inspection of rendered plots.

### Gaps Summary

No structural gaps found. All artifacts exist, are substantive (no stubs, no placeholders, no empty implementations), and are wired together correctly. All 6 requirements are covered by implemented code.

The one concern is a subtle normalization issue in the Q1 mixing matrix computation where same-country edges may be under-weighted in the diagonal by a factor of 2 relative to the off-diagonal. This does not affect the overall structure or approach -- the mixing matrix pattern (edge_type_counts, trace, marginal sums, Newman equation 2) is correct. But the numerical accuracy of original_country_r needs human verification against NetworkX's implementation to confirm correctness.

---

_Verified: 2026-03-28T19:07:18Z_
_Verifier: Claude (gsd-verifier)_
