# Maximum Product Subarray (LeetCode 152)

## 📌 Problem Statement
Given an integer array `nums`, find a contiguous non-empty subarray within the array that has the **largest product**, and return the product.

🔗 [LeetCode Problem Link](https://leetcode.com/problems/maximum-product-subarray/)

# 🚀 Solution Approach
- Maintain two variables while iterating:
  - `curr_max` → max product ending at current index  
  - `curr_min` → min product ending at current index (handles negative flips)  
- At each step:
  - Update `curr_max` and `curr_min` using current number `n`.
  - Update the result `res` with `curr_max`.
- Answer is the maximum product found.

- **Time Complexity:** O(n)  
- **Space Complexity:** O(1)

## 📝 Code
```python
from typing import List

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = max(nums)
        curr_max = curr_min = 1
        for n in nums:
            temp = curr_max * n
            curr_max = max(temp, curr_min * n, n)
            curr_min = min(temp, curr_min * n, n)
            res = max(res, curr_max)
        return res
