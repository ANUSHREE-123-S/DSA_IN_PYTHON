# 🔢 Permutations II (Unique Permutations)

## 🧩 Problem Description
Given a collection of numbers `nums` that **might contain duplicates**, return **all possible unique permutations**.

You must **not return duplicate permutations**.

# 💡 Approach — Backtracking with Duplicate Check

# 🔹 Idea:
1. **Sort the array** so that duplicates are adjacent.
2. Use a **`used` array** to track which elements are included in the current path.
3. During recursion, skip an element if:
   - It’s already used (`used[i] == True`)
   - It is a duplicate of the previous element (`nums[i] == nums[i-1]`) and the previous element is **not used** in the current recursion.
4. Recursively build the permutation by choosing unused numbers.

# ✅ Code Implementation

```python
from typing import List

class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        used = [False] * len(nums)
        
        def backtrack(path):
            if len(path) == len(nums):
                res.append(path[:])
                return
            for i in range(len(nums)):
                if used[i]:
                    continue
                if i > 0 and nums[i] == nums[i-1] and not used[i-1]:
                    continue
                used[i] = True
                path.append(nums[i])
                backtrack(path)
                path.pop()
                used[i] = False
        
        backtrack([])
        return res
