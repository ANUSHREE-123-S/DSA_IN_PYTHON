# 🎯 Combination Sum

## 🧩 Problem Description
Given an array of **distinct integers** `candidates` and a **target** integer `target`, return a **list of all unique combinations** of `candidates` where the chosen numbers sum to `target`.

You may use the **same number** from `candidates` an **unlimited number of times**.

All combinations must be **unique**, and the order of combinations does not matter.

# 💡 Approach — Backtracking

# 🔹 Idea:
We explore all possible combinations by:
1. **Choosing or skipping** each candidate.
2. Keeping track of the current sum.
3. If the sum exceeds the target → backtrack.
4. If the sum equals the target → record the combination.
5. Continue exploring from the current index to **reuse** the same number (since repetitions are allowed).

# ✅ Code Implementation

```python
from typing import List

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        
        def backtrack(start, current, total):
            # Base case: found a valid combination
            if total == target:
                result.append(list(current))
                return
            
            # Exceeded the target, stop exploring
            if total > target:
                return
            
            # Explore all choices
            for i in range(start, len(candidates)):
                current.append(candidates[i])  # Choose
                backtrack(i, current, total + candidates[i])  # Stay on same index (can reuse)
                current.pop()  # Undo choice (backtrack)
        
        backtrack(0, [], 0)
        return result
