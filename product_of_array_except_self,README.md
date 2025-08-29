# Product of Array Except Self (LeetCode 238)

## 📌 Problem Statement
Given an integer array `nums`, return an array `answer` such that:
- `answer[i] = product of all the elements of nums except nums[i]`.

⚠️ You must solve it **without using division** and in **O(n)** time.

🔗 [LeetCode Problem Link](https://leetcode.com/problems/product-of-array-except-self/)

# 🚀 Solution Approach
1. Create a result array initialized with `1`.
2. **Left pass:** compute prefix product for each index.
3. **Right pass:** compute suffix product and multiply with prefix result.
4. This ensures `res[i] = product of all elements except nums[i]`.

- **Time Complexity:** O(n)  
- **Space Complexity:** O(1) (ignoring result array)

# 📝 Code
```python
from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [1] * n
        left = 1
        for i in range(n):
            res[i] = left
            left *= nums[i]
        right = 1
        for i in range(n - 1, -1, -1):
            res[i] *= right
            right *= nums[i]
        return res
