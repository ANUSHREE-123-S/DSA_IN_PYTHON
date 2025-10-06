# 🌟 Subsets (Power Set)

# 🧩 Problem Description
Given an integer array `nums` containing **distinct elements**, return **all possible subsets (the power set)**.

The solution set **must not contain duplicate subsets**, and the order of subsets does not matter.

# 💡 Approach — Backtracking

We use **backtracking** to explore all possible combinations (subsets) by deciding whether to **include or exclude** each number.

# 🔹 Steps:
1. Start from index `0` with an empty subset (`path = []`).
2. At each step:
   - Add the current subset (`path[:]`) to the result.
   - For each index `i` from `start` to end:
     - Add `nums[i]` to `path`.
     - Recursively call the function with `start = i + 1`.
     - Backtrack (remove the last element added).
3. Continue until all possibilities are explored.

This ensures that all subsets are generated without repetition.

# ✅ Code Implementation

```python
from typing import List

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        
        def backtrack(start, path):
            # Add the current subset
            res.append(path[:])
            # Explore further elements
            for i in range(start, len(nums)):
                path.append(nums[i])
                backtrack(i + 1, path)
                path.pop()  # backtrack
                
        backtrack(0, [])
        return res
