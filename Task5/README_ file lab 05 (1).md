# Minimax and Alpha-Beta Pruning

**Name:** M Waqar
**Roll Number:** 212

## Overview

This lab implements Minimax and Alpha-Beta pruning on a small game tree, adds a leaf-evaluation counter to both, and shows how reordering the branches changes the amount of pruning while the root value stays the same.

Tree: eight terminal scores `3, 5, 2, 9, 3, 5, 2, 9`. The root is MAX, its children are MIN, and the nodes above the leaves are MAX.

## Files

| File | Purpose |
|---|---|
| `minimax.py` | Minimax, Alpha-Beta, leaf counters, branch reordering and the equal-scores edge case |
| `Minimax_Report_M_Waqar.docx` | Full lab report |

## How to Run

Requires Python 3. No extra packages are needed.

```
python minimax.py
```

The program prints, for each tree, the leaf sequence followed by `(Minimax value, Minimax leaves, Alpha-Beta value, Alpha-Beta leaves)`.

## Counting Rule

A leaf is counted each time a search reaches a terminal score. Alpha-Beta stops exploring a node's remaining children when alpha >= beta.

## Results

| Order | Leaf sequence | Root value | Minimax leaves | Alpha-Beta leaves |
|---|---|---|---|---|
| Original | 3, 5, 2, 9, 3, 5, 2, 9 | 5 | 8 | 6 |
| Reversed | 9, 2, 5, 3, 9, 2, 5, 3 | 5 | 8 | 8 |
| Best-first | 5, 3, 9, 2, 5, 3, 9, 2 | 5 | 8 | 5 |
| Worst-first | 2, 9, 3, 5, 2, 9, 3, 5 | 5 | 8 | 8 |
| All scores = 4 | 4, 4, 4, 4, 4, 4, 4, 4 | 4 | 8 | 5 |

Both algorithms always return the same root value. Only the number of leaves Alpha-Beta reads changes with the branch order.

## Limitations

The tree has only eight leaves, only a few orderings were tested, and the best-first order uses exact subtree values that a real game program would not know in advance.
