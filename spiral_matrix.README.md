# Spiral Matrix (LeetCode 54)

## 📌 Problem Statement
Given an `m x n` matrix, return all elements of the matrix in **spiral order**.

🔗 [LeetCode Problem Link](https://leetcode.com/problems/spiral-matrix/)

# 🚀 Solution Approach
- Use a **simulation approach**:
  - Start at the **top-left corner** `(0,0)`.
  - Move in the order: **right → down → left → up**.
  - Change direction whenever:
    - You move out of bounds, or
    - You reach a visited cell.
- Keep appending elements until all are visited.

- **Time Complexity:** O(m × n)  
- **Space Complexity:** O(1) (excluding result list)

# 📝 Code
```python
from typing import List

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        rows, cols = len(matrix), len(matrix[0])
        x, y, dx, dy = 0, 0, 1, 0
        res = []
        for _ in range(rows * cols):
            res.append(matrix[y][x])
            matrix[y][x] = "."
            if not (0 <= x + dx < cols and 0 <= y + dy < rows and matrix[y + dy][x + dx] != "."):
                dx, dy = -dy, dx
            x += dx
            y += dy
        return res
