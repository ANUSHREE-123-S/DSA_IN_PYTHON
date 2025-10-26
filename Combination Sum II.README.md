# 🎯 Combination Sum II

## 🧩 Problem Description
Given a collection of **candidate numbers** (`candidates`) and a **target number** (`target`), find all **unique combinations** in `candidates` where the chosen numbers sum to `target`.

Each number in `candidates` **may only be used once** in the combination.

> ⚠️ The solution set must not contain duplicate combinations.

# 💡 Approach — Backtracking (with Duplicate Handling)

# 🔹 Idea:
1. Sort the input array to easily **detect duplicates**.  
2. Explore combinations recursively using backtracking:
   - Choose an element.
   - Recurse to find combinations that meet the remaining target.
   - Skip elements that would create **duplicate combinations**.
3. Each element can be used **only once**, so move to the next index on recursion (`i+1`).

# ✅ Code Implementation

```python
from typing import List

class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()  # Sort to handle duplicates
         
        def backtrack(start, target, path):
            if target == 0:
                res.append(path[:])
                return
            for i in range(start, len(candidates)):
                # Skip duplicates
                if i > start and candidates[i] == candidates[i-1]:
                    continue
                # Stop early if number exceeds target
                if candidates[i] > target:
                    break
                path.append(candidates[i])
                backtrack(i+1, target-candidates[i], path)
                path.pop()
        
        backtrack(0, target, [])
        return res
