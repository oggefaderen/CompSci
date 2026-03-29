# Phase 5: Notebook Assembly - Context

**Gathered:** 2026-03-29
**Status:** Ready for planning

<domain>
## Phase Boundary

Final structural cleanup and assembly of Assignment2.ipynb. All content (Part 1 code, Part 1 reflections, Part 2 TF-IDF, Part 2 writing/word clouds) is already present in the notebook. This phase fixes ordering, headers, output verbosity, and ensures Kernel > Restart & Run All completes cleanly.

</domain>

<decisions>
## Implementation Decisions

### Cell ordering
- Move Ex1 Q1 explanation cell (currently at cell 34, end of notebook) to before the Q2 code cell ("Create Community Token Documents")
- Assignment reading order: Q1 explanation → Q2 documents → Q3 TF → Q4 TF-IDF → Exercise 2 → Exercise 3

### Header structure
- Rename "## Part 2: TF-IDF Analysis" section to "## Exercise 1"
- Rename "## Q2/Q3/Q4:" sub-headers to "### Q2:/Q3:/Q4:" (one level down, under Exercise 1)
- Fix "## Part 5: Reflection Questions" (cell 19) → "## Part 1: Reflections"
- Keep "## Exercise 2" and "## Exercise 3" headers as-is (already correctly named from Phase 4)

### Contribution statement
- Leave "..." placeholders for Lovro, Oskar, Uffe — students fill in their own text before submitting
- Ensure the cell is properly formatted markdown (repo link + contribution structure correct)

### Output control
- Suppress per-iteration prints in 100-network loops (Q3 country assortativity, Q5 degree assortativity)
- Limit printed TF/TF-IDF word lists to top-10 entries
- Use `display()` for DataFrames instead of raw print where applicable
- Word cloud grid (9 subplots) is acceptable as a single figure output — no suppression needed

### Claude's Discretion
- Exact mechanism for suppressing loop prints (suppress flag, redirect stdout, or just remove existing print statements)
- Whether to clear saved outputs from already-run cells before final submission

</decisions>

<canonical_refs>
## Canonical References

**Downstream agents MUST read these before planning or implementing.**

### Target file
- `Assignment2/Assignment2.ipynb` — The notebook to modify (40 cells, read current structure before any edits)

### Source of truth for structure
- `.planning/REQUIREMENTS.md` — ASBL-01 through ASBL-07 define all assembly requirements
- `.planning/phases/04-part-2-writing-and-word-clouds/04-CONTEXT.md` — Decisions locked in Phase 4 (word cloud format, author name resolution, header style)

</canonical_refs>

<code_context>
## Existing Code Insights

### Reusable Assets
- Cell ordering in Jupyter JSON: `nb['cells']` is a list — reorder by splicing indices
- Cells are identified by source content since no tags are set

### Established Patterns
- `./` relative paths for all CSV files (established Phase 3)
- Full question text as markdown header before each answer cell (established Phase 1-4)
- Code cells split per question (one question = one code cell + one markdown analysis cell)

### Integration Points
- Cell 34 (Ex1 Q1 explanation) needs to move to before cell 25 (Q2 code) in the JSON cell list
- Cell 19 header text needs editing (Part 5 → Part 1)
- Cells 22, 25, 27, 30 need header level adjustments
- Cells 14, 18 (100-network loops) may have verbose iteration output to suppress

</code_context>

<specifics>
## Specific Ideas

- Assignment requires: "Kernel > Restart & Run All completes without errors and all plots render"
- The contribution cell (cell 0) format: repo link on line 1, then "# Contributions" section with one entry per person — structure is already correct, just leave "..." content

</specifics>

<deferred>
## Deferred Ideas

None — discussion stayed within phase scope

</deferred>

---

*Phase: 05-notebook-assembly*
*Context gathered: 2026-03-29*
