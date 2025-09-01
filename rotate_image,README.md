# Rotate Image (LeetCode 48)

## 📌 Problem Statement
You are given an `n x n` 2D matrix representing an image.  
Rotate the image by **90 degrees clockwise**.  
You must rotate the image **in-place** (i.e., modify the input matrix directly, without using extra space).

🔗 [LeetCode Problem Link](https://leetcode.com/problems/rotate-image/)

# 🚀 Solution Approach
- Rotate the matrix **layer by layer**:
  - For each square layer, swap elements in groups of 4:
    - **top-left → top-right**
    - **bottom-left → top-left**
    - **bottom-right → bottom-left**
    - **top-right → bottom-right**
- After rotating a layer, shrink boundaries inward (`l += 1`, `r -= 1`).

- **Time Complexity:** O(n²)  
- **Space Complexity:** O(1) (in-place)

# 📝 Code
```python
from typing import List

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        l, r = 0, len(matrix) - 1
        while l < r:
            for i in range(r - l):
                top, bottom = l, r
                topleft = matrix[top][l + i]
                matrix[top][l + i] = matrix[bottom - i][l]
                matrix[bottom - i][l] = matrix[bottom][r - i]
                matrix[bottom][r - i] = matrix[top + i][r]
                matrix[top + i][r] = topleft
            r -= 1
            l += 1
