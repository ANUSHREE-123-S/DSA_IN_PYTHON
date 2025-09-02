# Majority Element (LeetCode 169)

## 📌 Problem Statement
Given an array `nums` of size `n`, return the **majority element**.  
The majority element is the element that appears **more than ⌊n / 2⌋ times**.

You may assume that the majority element always exists in the array.

🔗 [LeetCode Problem Link](https://leetcode.com/problems/majority-element/)

# 🚀 Solution Approach
We use the **Boyer-Moore Voting Algorithm**:
- Keep track of a **candidate** and a **count**.
- If `count == 0`, choose the current number as candidate.
- Increase `count` if the current number matches the candidate, else decrease it.
- The final candidate is guaranteed to be the majority element.

- **Time Complexity:** O(n)  
- **Space Complexity:** O(1)

# 📝 Code
```python
from typing import List

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        candidate = None
        count = 0
        for num in nums:
            if count == 0:
                candidate = num
            if num == candidate:
                count += 1
            else:
                count -= 1
        return candidate
