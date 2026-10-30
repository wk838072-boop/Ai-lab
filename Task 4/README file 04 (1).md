# Lab 4: Informed Search (A*)

**Name:** M Waqar
**Roll Number:** 212

## Overview

This lab finds the cheapest route from building S to building G on a small campus graph using A* search, and compares it with Uniform Cost Search (UCS). It also tests what happens when one heuristic value is raised above the true remaining cost.

Graph (travel time): S-A 1, S-B 4, A-C 2, B-G 5, C-G 3.
Heuristic: h(S) = 5, h(A) = 4, h(B) = 4, h(C) = 2, h(G) = 0.

## Files

| File | Purpose |
|---|---|
| `astar.py` | A* and UCS (h = 0) on the main graph, the h(C) = 10 experiment, true remaining costs, and the hand-calculation trace for the first three expansions |
| `tests.py` | Edge-case tests: start equals goal, unreachable goal, stale entry, negative edge cost, heuristic consistency |
| `Lab4_Report_Zeeshan_Haider.docx` | Full lab report |

## How to Run

Requires Python 3. Only the standard library is used (`heapq`, `json`).

```
python astar.py
python tests.py
```

## Conventions

- The priority queue orders entries by f, then g, then node name.
- A node counts as expanded only when its successors are examined. The goal is recorded in the processed trace but not counted.
- Queue entries whose g is worse than the best known g are stale and skipped.

## Results

| Run | Path | Cost | Expansions |
|---|---|---|---|
| A* (supplied h) | S, A, C, G | 6 | 3 |
| UCS (h = 0) | S, A, C, G | 6 | 4 |
| A* with h(C) = 10 | S, B, G | 9 | 3 |

The supplied heuristic is admissible and consistent on this graph. Setting h(C) = 10 overestimates the true remaining cost of 3, and A* then returns a route that costs 9 instead of 6.

## Limitations

The graph has only five nodes, the heuristic values are abstract, and only one overestimate was tested, so the results show behaviour on this example and do not prove a general rule.
