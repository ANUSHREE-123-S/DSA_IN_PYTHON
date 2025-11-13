# 🧩 Surrounded Regions

## 📘 Problem Description
You are given an `m x n` matrix `board` containing `'X'` and `'O'`.  
You need to **capture all regions** that are completely surrounded by `'X'`.

A region is captured by flipping all `'O'`s into `'X'`s in that surrounded region.

**Explanation:**  
The `'O'`s that are not connected to the boundary are completely surrounded and flipped to `'X'`.  
The `'O'` at the bottom is **not flipped** because it’s connected to the boundary.

# 🎯 Intuition
All `'O'`s **connected to the boundary** cannot be surrounded.  
So the idea is:

1. Mark all boundary-connected `'O'`s as **safe** (`'S'`).
2. Flip all **remaining `'O'`s** to `'X'` (they are surrounded).
3. Convert `'S'` back to `'O'`.
4. # 🧠 Approach — Depth-First Search (DFS)

### Steps:
1. Iterate over all boundary cells (first and last rows/columns).
2. Whenever you find `'O'`, run DFS to mark it (and connected `'O'`s) as `'S'`.
3. After marking:
   - Change all `'O'`s to `'X'` (captured region).
   - Change all `'S'`s back to `'O'` (safe region).

 ✅ Code Implementation

```python
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        if not board or not board[0]:
            return
        
        rows, cols = len(board), len(board[0])

        def dfs(r, c):
            if r < 0 or c < 0 or r >= rows or c >= cols or board[r][c] != "O":
                return
            board[r][c] = "S"
            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)

        # Step 1: Mark boundary-connected 'O's as safe
        for i in range(rows):
            if board[i][0] == "O":
                dfs(i, 0)
            if board[i][cols - 1] == "O":
                dfs(i, cols - 1)

        for j in range(cols):
            if board[0][j] == "O":
                dfs(0, j)
            if board[rows - 1][j] == "O":
                dfs(rows - 1, j)

        # Step 2: Flip surrounded 'O's to 'X' and safe 'S's back to 'O'
        for i in range(rows):
            for j in range(cols):
                if board[i][j] == "O":
                    board[i][j] = "X"
                elif board[i][j] == "S":
                    board[i][j] = "O"
