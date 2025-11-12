# 🏝️ Number of Islands

## 🧩 Problem Description
Given an `m x n` 2D binary grid representing a map of `'1'`s (land) and `'0'`s (water), return the **number of islands**.

An **island** is surrounded by water and is formed by connecting adjacent lands horizontally or vertically.  
You may assume all four edges of the grid are surrounded by water.

# 🎯 Intuition
Each `'1'` represents land. When a `'1'` is found, we can treat it as the start of a new island.  
To **mark the entire island as visited**, we perform a **Depth-First Search (DFS)** to traverse all connected `'1'`s and convert them to `'0'` (water).

This prevents counting the same island multiple times.

# 🧠 Approach — Depth-First Search (DFS)

### Steps:
1. Loop through every cell in the grid.
2. When a `'1'` is found:
   - Increment the island count.
   - Run a DFS to mark all connected `'1'` cells (land) as `'0'` (visited).
3. Continue scanning until all islands are discovered.

# DFS Logic:
- Base Case: Stop when we move out of bounds or encounter `'0'`.
- Recursive Case: Mark the current cell as `'0'` and explore **up, down, left, right**.

# ✅ Code Implementation

```python
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0

        rows, cols = len(grid), len(grid[0])
        island = 0

        def dfs(r, c):
            if r < 0 or c < 0 or r >= rows or c >= cols or grid[r][c] == "0":
                return
            grid[r][c] = "0"  # mark as visited
            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1":
                    island += 1
                    dfs(r, c)

        return island
