# Set Matrix Zeroes (LeetCode 73)

## 📌 Problem Statement
Given an `m x n` integer matrix, if an element is `0`, set its **entire row and column** to `0`.  

You must do it **in place**.

🔗 [LeetCode Problem Link](https://leetcode.com/problems/set-matrix-zeroes/)

# 🚀 Solution Approach
- Use the **first row and first column as markers** to avoid extra space.
- Track separately if the **first row** and **first column** need to be zeroed.
- Steps:
  1. Scan matrix and mark zeros in the first row/col.
  2. Traverse again, zero out cells based on marks.
  3. Handle first row/col at the end.

- **Time Complexity:** O(m × n)  
- **Space Complexity:** O(1) (in-place)

# 📝 Code
```python
from typing import List

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        m, n = len(matrix), len(matrix[0])
        first_row_zero = any(matrix[0][j] == 0 for j in range(n))
        first_col_zero = any(matrix[i][0] == 0 for i in range(m))
        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0
        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0
        if first_row_zero:
            for j in range(n):
                matrix[0][j] = 0
        if first_col_zero:
            for i in range(m):
                matrix[i][0] = 0
