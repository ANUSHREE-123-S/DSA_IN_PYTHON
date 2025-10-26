# 🔠 Word Search

## 🧩 Problem Description
Given an `m x n` grid of characters `board` and a string `word`, return **True** if `word` exists in the grid.

The word can be constructed from **letters of sequentially adjacent cells**, where adjacent cells are horizontally or vertically neighboring.  
The same letter cell **may not be used more than once**.

# 💡 Approach — Backtracking + DFS

# 🔹 Intuition:
We perform a **Depth-First Search (DFS)** starting from every cell that matches the first letter of `word`.  
At each step:
- Check if the current cell matches the current character in `word`.
- Temporarily **mark the cell as visited** (to avoid reuse).
- Recursively explore in **4 directions** (up, down, left, right).
- If all letters are found, return `True`.

After exploring a path, **restore the cell** to its original value (backtracking).

# ✅ Code Implementation

```python
from typing import List

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows = len(board)
        cols = len(board[0])

        def backtrack(r, c, index):
            if index == len(word):
                return True
            if (r < 0 or c < 0 or r >= rows or c >= cols or board[r][c] != word[index]):
                return False

            temp = board[r][c]
            board[r][c] = '#'  # mark as visited

            res = (
                backtrack(r + 1, c, index + 1) or
                backtrack(r - 1, c, index + 1) or
                backtrack(r, c + 1, index + 1) or
                backtrack(r, c - 1, index + 1)
            )

            board[r][c] = temp  # restore for backtracking
            return res

        for i in range(rows):
            for j in range(cols):
                if board[i][j] == word[0] and backtrack(i, j, 0):
                    return True

        return False
