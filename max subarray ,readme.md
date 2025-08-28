# Maximum Subarray (LeetCode 53)

## 📌 Problem Statement
Given an integer array `nums`, find the **subarray with the largest sum**, and return its sum.

🔗 [LeetCode Problem Link](https://leetcode.com/problems/maximum-subarray/)

🚀 Solution Approach
- Use **Kadane’s Algorithm**.
- Keep a running total of the current subarray sum.
- If the total drops below `0`, reset it to `0`.
- Update the result with the maximum sum found.

- **Time Complexity:** O(n)  
- **Space Complexity:** O(1)

📝 Code
```python
from typing import List

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        res = nums[0]
        total = 0
        for i in nums:
            if total < 0:
                total = 0
            total += i
            res = max(res, total)
        return res
