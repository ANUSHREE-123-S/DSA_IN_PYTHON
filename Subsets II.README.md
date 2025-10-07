# 🌟 Subsets II — Handling Duplicates

## 🧩 Problem Description
Given an integer array `nums` that **may contain duplicates**, return **all possible unique subsets (the power set)**.

The solution set **must not contain duplicate subsets**, and subsets can be returned in any order.

# 💡 Approach — Backtracking with Duplicate Skipping

This problem is an extension of the **Subsets (Power Set)** problem, with one key twist — the input may have **duplicate elements**.  
To handle duplicates, we:
1. **Sort** the array first.
2. **Skip duplicate elements** during recursion to avoid generating identical subsets.

# 🔹 Steps:
1. Sort the input array → ensures duplicates are adjacent.
2. Use a recursive `backtrack(start, path)` function.
3. For each index `i`:
   - Skip the element if it’s the **same as the previous one** and not the first element in this recursion level.
   - Include `nums[i]`, then recursively build further subsets.
   - Backtrack (remove last element) and continue.
4. Store all subsets in the result list `res`.

 ✅ Code Implementation

```python
from typing import List

class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()  # Sort to handle duplicates

        def backtrack(start, path):
            res.append(path[:])
            for i in range(start, len(nums)):
                # Skip duplicate numbers at the same recursion level
                if i > start and nums[i] == nums[i - 1]:
                    continue
                path.append(nums[i])
                backtrack(i + 1, path)
                path.pop()  # backtrack

        backtrack(0, [])
        return res
