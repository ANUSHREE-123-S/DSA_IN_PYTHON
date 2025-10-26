from typing import List

class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()  # sort to handle duplicates
         
        def backtrack(start, target, path):
            if target == 0:
                res.append(path[:])
                return
            for i in range(start, len(candidates)):
                # skip duplicates
                if i > start and candidates[i] == candidates[i-1]:
                    continue
                if candidates[i] > target:
                    break
                path.append(candidates[i])
                backtrack(i+1, target-candidates[i], path)
                path.pop()
        
        backtrack(0, target, [])
        return res
