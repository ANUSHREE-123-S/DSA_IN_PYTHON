# Find Minimum in Rotated Sorted Array (LeetCode 153)

## 📌 Problem Statement
Suppose an array of length `n` sorted in ascending order is rotated between `1` and `n` times.  
Return the minimum element of this array.  
You must solve this in **O(log n)** time.

🔗 [LeetCode Problem Link](https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/)

# 🚀 Solution Approach
- Use **binary search**:
  - If `nums[mid] > nums[right]`, the **minimum** must be in the **right half**.
  - Otherwise, the minimum lies in the **left half (including mid)**.
- Continue until `left == right`, which points to the minimum.

- **Time Complexity:** O(log n)  
- **Space Complexity:** O(1)

# 📝 Code
```python
from typing import List

class Solution:
    def findMin(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1
        while left < right:
            mid = (left + right) // 2
            if nums[mid] > nums[right]:
                left = mid + 1
            else:
                right = mid
        return nums[left]
