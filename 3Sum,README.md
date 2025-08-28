# 3Sum (LeetCode 15)

## 📌 Problem Statement
Given an integer array `nums`, return all the **unique triplets** `[nums[i], nums[j], nums[k]]` such that:

- `i != j != k`
- `nums[i] + nums[j] + nums[k] == 0`

The solution set must not contain duplicate triplets.

🔗 [LeetCode Problem Link](https://leetcode.com/problems/3sum/)

# 🚀 Solution Approach
1. Sort the array.
2. Iterate through each element `nums[i]`:
   - Skip duplicates.
   - Use **two pointers** (`j` = left, `k` = right) to find a pair such that `nums[i] + nums[j] + nums[k] == 0`.
3. Adjust pointers accordingly:
   - If sum > 0 → move right pointer left.
   - If sum < 0 → move left pointer right.
   - If sum == 0 → record triplet, then skip duplicates.
4. Collect all unique triplets.

- **Time Complexity:** O(n²)  
- **Space Complexity:** O(1) (ignoring result storage)

# 📝 Code
```python
from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        n = len(nums)
        nums.sort()
        for i in range(n):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            j, k = i + 1, n - 1
            while j < k:
                total = nums[i] + nums[j] + nums[k]
                if total > 0:
                    k -= 1
                elif total < 0:
                    j += 1
                else:
                    res.append([nums[i], nums[j], nums[k]])
                    j += 1
                    k -= 1
                    while j < k and nums[j] == nums[j - 1]:
                        j += 1
                    while j < k and nums[k] == nums[k + 1]:
                        k -= 1
        return res
