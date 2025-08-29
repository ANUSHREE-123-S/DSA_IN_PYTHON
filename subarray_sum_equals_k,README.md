# Subarray Sum Equals K (LeetCode 560)

## 📌 Problem Statement
Given an array of integers `nums` and an integer `k`, return the **total number of subarrays** whose sum equals to `k`.

🔗 [LeetCode Problem Link](https://leetcode.com/problems/subarray-sum-equals-k/)

# 🚀 Solution Approach
- Use **Prefix Sum + HashMap**:
  - Maintain a running `prefix_sum`.
  - Use a hashmap (`prefix_map`) to store how many times each prefix sum has occurred.
  - For each element, check if `(prefix_sum - k)` exists in map:
    - If yes → it means there’s a subarray ending here that sums to `k`.
  - Update `prefix_map` with current `prefix_sum`.

- **Time Complexity:** O(n)  
- **Space Complexity:** O(n)

# 📝 Code
```python
from typing import List

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count = 0
        prefix_sum = 0
        prefix_map = {0: 1}
        for num in nums:
            prefix_sum += num
            if prefix_sum - k in prefix_map:
                count += prefix_map[prefix_sum - k]
            prefix_map[prefix_sum] = prefix_map.get(prefix_sum, 0) + 1
        return count
