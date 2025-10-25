from typing import List

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        
        def backtrack(start, current, total):
            # If we reach the target, save the combination
            if total == target:
                result.append(list(current))
                return
            
            # If total exceeds target, stop exploring
            if total > target:
                return
            
            # Explore further
            for i in range(start, len(candidates)):
                current.append(candidates[i])  # choose
                backtrack(i, current, total + candidates[i])  # not i+1, because we can reuse same element
                current.pop()  # un-choose (backtrack)
        
        backtrack(0, [], 0)
        return result
