# Pascal's Triangle (LeetCode 118)

## 📌 Problem Statement
Given an integer `numRows`, return the first `numRows` of **Pascal's Triangle**.  

In Pascal's Triangle:
- Each number is the sum of the two numbers directly above it.

🔗 [LeetCode Problem Link](https://leetcode.com/problems/pascals-triangle/)

# 🚀 Solution Approach
- Start with the base case: the first row `[1]`.
- To generate a new row:
  - Pad the previous row with `0`s at both ends.
  - Compute each element as the sum of two adjacent elements.
- Continue until `numRows` rows are generated.

- **Time Complexity:** O(numRows²)  
- **Space Complexity:** O(numRows²)
## 📝 Code
```python
from typing import List

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        res = [[1]]
        for _ in range(numRows - 1):
            temp = [0] + res[-1] + [0]
            row = []
            for j in range(len(res[-1]) + 1):
                row.append(temp[j] + temp[j + 1])
            res.append(row)
        return res
