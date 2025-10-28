# ♕ N-Queens Problem

## 🧩 Problem Description

The **N-Queens problem** asks you to place `n` queens on an `n x n` chessboard such that:
- No two queens attack each other.
- A queen can attack another queen if they share the same **row**, **column**, or **diagonal**.

Your task is to return **all distinct solutions**, where each solution contains a valid board configuration.

**Explanation:**
There are 2 distinct ways to place 4 queens on a 4×4 board so that none attack each other.

# 💡 Approach — Backtracking

# 🔹 Intuition:
We use **backtracking** to explore all possible queen placements row by row.

For each row:
1. Try placing a queen in every column.
2. Skip columns or diagonals that are already attacked.
3. If a valid placement is found, move to the next row.
4. If all rows are filled → store that configuration as a solution.

When backtracking, remove the last queen placed and explore the next possible column.

---

## ✅ Code Implementation

```python
from typing import List

class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        def backtrack(row, cols, diagonals1, diagonals2, board):
            # Base case: all queens are placed
            if row == n:
                result.append(["".join(r) for r in board])
                return

            for col in range(n):
                # Check if current position is under attack
                if col in cols or (row - col) in diagonals1 or (row + col) in diagonals2:
                    continue

                # Place queen
                board[row][col] = 'Q'
                cols.add(col)
                diagonals1.add(row - col)
                diagonals2.add(row + col)

                # Move to the next row
                backtrack(row + 1, cols, diagonals1, diagonals2, board)

                # Backtrack: remove the queen
                board[row][col] = '.'
                cols.remove(col)
                diagonals1.remove(row - col)
                diagonals2.remove(row + col)

        result = []
        board = [["."] * n for _ in range(n)]
        backtrack(0, set(), set(), set(), board)
        return result
