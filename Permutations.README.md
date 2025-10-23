
# 🔢 Permutations

## 🧩 Problem Description
Given an array `nums` of distinct integers, return **all possible permutations**.

A permutation is a unique rearrangement of all the elements in the list.


# 💡 Approach — Backtracking (DFS)

This problem is a **classic backtracking** problem where we try all possible orderings of elements.

# 🔹 Idea:
1. Maintain two lists:
   - `path`: the current permutation being built.
   - `remaining`: elements yet to be added.
2. When `remaining` becomes empty, we have formed one valid permutation — add it to the result.
3. Recursively pick each element from `remaining`, append it to `path`, and continue the process with the updated `remaining`.

# ✅ Code Implementation

```python
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []
        def backtrack(path, remaining):
            if not remaining:
                result.append(path[:])
                return
            for i in range(len(remaining)):
                backtrack(path + [remaining[i]], remaining[:i] + remaining[i+1:])
        backtrack([], nums)
        return result
