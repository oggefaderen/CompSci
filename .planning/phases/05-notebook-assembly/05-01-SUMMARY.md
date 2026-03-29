---
phase: 05-notebook-assembly
plan: 01
subsystem: notebook
tags: [jupyter, notebook, assignment2, tf-idf, cell-ordering]

# Dependency graph
requires:
  - phase: 04-part-2-writing-and-word-clouds
    provides: Q1 TF-IDF explanation cell added to Assignment2 notebook
  - phase: 03-tf-idf-implementation
    provides: Q2/Q3/Q4 code cells in Assignment2 notebook
provides:
  - Corrected header hierarchy (Part 1/Exercise 1 naming scheme)
  - Q1 TF-IDF explanation positioned immediately before Q2 header
affects: [notebook-submission, assignment2-final-structure]

# Tech tracking
tech-stack:
  added: []
  patterns: [direct JSON manipulation of .ipynb via Python script for multi-cell edits]

key-files:
  created: []
  modified:
    - Assignment2/Assignment2.ipynb

key-decisions:
  - "Verification script in plan has false-negative: '## Q2:' not in src fails because '### Q2:' contains '## Q2:' as substring — corrected to use startswith check on first line"

patterns-established:
  - "Notebook cell edits: use Python json.load/json.dump for multi-cell changes; locate cells by source content pattern, not hardcoded index"

requirements-completed: [ASBL-01, ASBL-02, ASBL-03, ASBL-04]

# Metrics
duration: 2min
completed: 2026-03-29
---

# Phase 5 Plan 01: Notebook Assembly — Cell Ordering and Header Fixes Summary

**5 header renames (Part 5 → Part 1, Part 2 → Exercise 1, Q2/Q3/Q4 demoted to ###) and Q1 TF-IDF explanation moved to immediately precede Q2 in Assignment2/Assignment2.ipynb**

## Performance

- **Duration:** 2 min
- **Started:** 2026-03-29T10:09:26Z
- **Completed:** 2026-03-29T10:11:42Z
- **Tasks:** 2
- **Files modified:** 1

## Accomplishments

- Cell [19] header corrected: "## Part 5: Reflection Questions" → "## Part 1: Reflections"
- Cell [22] header corrected: "## Part 2: TF-IDF Analysis" → "## Exercise 1"
- Cells [25], [27], [30] demoted from ## to ### level (Q2, Q3, Q4 sub-headers)
- Ex1 Q1 explanation cell moved from index 34 to index 25 (immediately before Q2 header at 26)
- Total cell count remains exactly 40 — no cells lost or duplicated

## Task Commits

Each task was committed atomically:

1. **Task 1: Fix 5 header cells** - `5c2abbb` (fix)
2. **Task 2: Move Ex1 Q1 explanation cell before Q2 header** - `a744e67` (feat)

## Files Created/Modified

- `Assignment2/Assignment2.ipynb` — 5 header edits + Q1 cell repositioned to reading order position

## Decisions Made

- Plan verification script had a logic bug: `'## Q2:' not in src25` evaluates False even after correct edit because `### Q2:` is a superset of `## Q2:` as a Python substring. Fixed verification by using `str.startswith('### Q2:')` on the first line of the cell source instead.

## Deviations from Plan

### Auto-fixed Issues

**1. [Rule 1 - Bug] Corrected verification assertion for Q-header level checks**
- **Found during:** Task 1 (verify step)
- **Issue:** `assert '## Q2:' not in src25` failed because `### Q2:` contains `## Q2:` as a substring in Python string matching
- **Fix:** Replaced assertion with `src25.split('\n')[0].startswith('### Q2:')` which correctly detects the heading level
- **Files modified:** None (verification script only, not notebook)
- **Verification:** Corrected assertion passed; notebook content confirmed correct
- **Committed in:** 5c2abbb (Task 1 commit — notebook content was already correct)

---

**Total deviations:** 1 auto-fixed (Rule 1 — bug in verification logic, not in implementation)
**Impact on plan:** Verification script had a false-negative that masked a passing state. Actual notebook edits were correct on the first attempt. No scope creep.

## Issues Encountered

- Python substring semantics: `'## Q2:' in '### Q2: ...'` evaluates to True because `##` is a prefix of `###`. The plan's verify script used `not in` to detect lingering `## Q2:` patterns, but this check always fails after a correct `### Q2:` replacement. Resolved by switching to `startswith` on the parsed first line.

## User Setup Required

None - no external service configuration required.

## Next Phase Readiness

- Assignment2/Assignment2.ipynb has correct cell ordering and header hierarchy
- Ready for Phase 05 Plan 02 (any remaining notebook assembly tasks)
- All ASBL requirements satisfied: reading flow is Part 1 Reflections → Exercise 1 → [Q1 explanation] → Q2 → Q3 → Q4 → Exercise 2 → Exercise 3

---
*Phase: 05-notebook-assembly*
*Completed: 2026-03-29*
