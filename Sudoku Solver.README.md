# 🔢 Sudoku Solver

## 🧩 Problem Description

Write an algorithm to solve a **Sudoku puzzle** by filling the empty cells (`"."`) such that:
- Each row contains the digits **1–9** exactly once.
- Each column contains the digits **1–9** exactly once.
- Each of the 9 sub-boxes (3×3 grids) contains the digits **1–9** exactly once.

The input Sudoku board will always have a unique solution.

# 💡 Approach — Backtracking

We solve Sudoku using **backtracking**, similar to the N-Queens pattern.

# Steps:
1. **Preprocessing:**
   - For each row, column, and 3×3 box, track which numbers are already used.
   - Store all empty cell positions in a list.

2. **Backtracking Function (`backtrack`):**
   - If all empty cells are filled → return `True` (solution found).
   - For the current empty cell:
     - Try placing numbers `1–9`.
     - If valid (not present in same row, column, or box):
       - Place number.
       - Move to next empty cell recursively.
       - If recursion returns `True`, solution is found.
       - Otherwise, undo the placement (backtrack).

3. Continue until all cells are correctly filled.

---

## ✅ Code Implementation

```python
from typing import List

class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """

        # Step 1: Prepare sets for rows, columns, and boxes
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]
        empty = []

        # Step 2: Fill sets with existing numbers and note empty cells
        for r in range(9):
            for c in range(9):
                val = board[r][c]
                if val == ".":
                    empty.append((r, c))
                else:
                    rows[r].add(val)
                    cols[c].add(val)
                    boxes[(r // 3) * 3 + (c // 3)].add(val)

        # Step 3: Recursive backtracking
        def backtrack(idx=0):
            if idx == len(empty):
                return True  # All cells filled successfully

            r, c = empty[idx]
            box_index = (r // 3) * 3 + (c // 3)

            for ch in '123456789':
                if ch not in rows[r] and ch not in cols[c] and ch not in boxes[box_index]:
                    # Place number
                    board[r][c] = ch
                    rows[r].add(ch)
                    cols[c].add(ch)
                    boxes[box_index].add(ch)

                    # Move to next empty cell
                    if backtrack(idx + 1):
                        return True

                    # Undo the placement (Backtrack)
                    board[r][c] = '.'
                    rows[r].remove(ch)
                    cols[c].remove(ch)
                    boxes[box_index].remove(ch)

            return False  # No valid number found → backtrack

        backtrack()
