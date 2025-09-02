# Missing Number (LeetCode 268)

## 📌 Problem Statement
Given an array `nums` containing `n` distinct numbers in the range `[0, n]`,  
return the only number in the range that is **missing** from the array.

🔗 [LeetCode Problem Link](https://leetcode.com/problems/missing-number/)
- This works because exactly one number is missing.

- **Time Complexity:** O(n)  
- **Space Complexity:** O(1)

## 📝 Code
```python
from typing import List

class Solution:
  def missingNumber(self, nums: List[int]) -> int:
      n = len(nums)
      actual_sum = sum(nums)
      expected_sum = n * (n + 1) // 2
      return expected_sum - actual_sum
