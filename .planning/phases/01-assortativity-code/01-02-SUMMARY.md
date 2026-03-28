---
phase: 01-assortativity-code
plan: 02
subsystem: analysis
tags: [networkx, numpy, matplotlib, configuration-model, assortativity, jupyter]

# Dependency graph
requires:
  - phase: 01-assortativity-code
    plan: 01
    provides: "G graph with country attrs, country_map, original_country_r variable from Q1"
provides:
  - configuration_mode_swap function with E*10 double-edge swaps and 50% flip
  - degree sequence assertion verifying config model correctness
  - Q3 country assortativity null distribution over 100 random networks
  - degree_assortativity function using lecture formula (mean product - product of means / variance)
  - Q5 degree assortativity null distribution over 100 random networks
affects: [02-written-analysis, any phase reading Assignment2.ipynb]

# Tech tracking
tech-stack:
  added: []
  patterns:
    - "Configuration model via double-edge swap with E*10 iterations and 50% directional flip"
    - "Null distribution comparison: store original metric before loop, use axvline to mark on histogram"
    - "Explicit variable naming: original_country_r and original_degree_r (not overloaded 'r')"

key-files:
  created: []
  modified:
    - Assignment2/Assignment2.ipynb

key-decisions:
  - "Q3 axvline uses original_country_r (country assortativity from Q1), not degree r — fixes bug present in Part1.ipynb where original_r = r was set after degree assortativity was computed"
  - "original_degree_r stored as named variable before Q5 loop (not reusing 'r') to prevent cross-contamination between Q3 and Q5 plots"
  - "country_map re-applied inside Q3 loop on G_rand nodes to ensure country attributes are present on each randomized graph"

patterns-established:
  - "Null model loop pattern: compute original metric before loop, append per-iteration to list, plot histogram with axvline for original"
  - "Config model always called configuration_mode_swap (matches Part1.ipynb function name)"

requirements-completed: [ASRT-02, ASRT-03, ASRT-04, ASRT-05, ASRT-06]

# Metrics
duration: 3min
completed: 2026-03-28
---

# Phase 01 Plan 02: Q2-Q5 Configuration Model and Assortativity Distributions Summary

**Double-edge-swap config model with E*10 swaps, two 100-network null distribution plots (country and degree assortativity), and bug fix ensuring Q3 axvline references country r not degree r**

## Performance

- **Duration:** 3 min
- **Started:** 2026-03-28T18:59:18Z
- **Completed:** 2026-03-28T19:02:00Z
- **Tasks:** 2
- **Files modified:** 1

## Accomplishments
- configuration_mode_swap function with correct E*10 swap count, 50% directional flip, and no-self-loop guard
- Degree sequence assertion confirming config model preserves node degrees exactly
- Q3: 100-network country assortativity null distribution with original_country_r (from Q1) marked as red dashed line
- Q4: degree_assortativity function implementing lecture formula (mean(ku*kv) - mean(ku)*mean(kv)) / (mean(ku^2) - mean(ku)^2)
- Q5: 100-network degree assortativity null distribution with original_degree_r marked as red dashed line

## Task Commits

Each task was committed atomically:

1. **Task 1: Q2 configuration model and degree sequence verification** - `c4f2844` (feat)
2. **Task 2: Q3 country assort distribution, Q4 degree assort formula, Q5 degree assort distribution** - `ebdba15` (feat)

**Plan metadata:** (docs commit follows)

## Files Created/Modified
- `Assignment2/Assignment2.ipynb` - Added 10 cells: Q2 markdown + config model function + degree check + Q3 markdown + Q3 loop/plot + Q4 markdown + degree_assortativity function + Q5 markdown + Q5 loop/plot

## Decisions Made
- Q3 axvline uses `original_country_r` (fixed bug from Part1.ipynb where `original_r = r` captured degree assortativity instead)
- `original_degree_r` named explicitly before Q5 loop to prevent any variable collision with Q3's country r variable
- `country_map.get(node, None)` applied inside Q3 loop on each G_rand so attribute_assortativity_coefficient has data to work with

## Deviations from Plan

None - plan executed exactly as written.

## Issues Encountered
None.

## User Setup Required
None - no external service configuration required.

## Next Phase Readiness
- All 6 ASRT requirements now addressed: ASRT-01 through ASRT-06
- Assignment2.ipynb runs end-to-end: imports, graph construction, country attributes, Q1 manual assortativity, Q2 config model, Q3 country null distribution, Q4 degree assortativity, Q5 degree null distribution
- Phase 01 complete — ready for written analysis phase

## Self-Check: PASSED

- Assignment2/Assignment2.ipynb: FOUND
- .planning/phases/01-assortativity-code/01-02-SUMMARY.md: FOUND
- Commit c4f2844: FOUND
- Commit ebdba15: FOUND

---
*Phase: 01-assortativity-code*
*Completed: 2026-03-28*
