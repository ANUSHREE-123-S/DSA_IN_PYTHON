# Search in Rotated Sorted Array (LeetCode 33)

## 📌 Problem Statement
You are given an integer array `nums` sorted in ascending order (with **distinct values**), but it has been **rotated at an unknown pivot index**.  
Given the array `nums` and an integer `target`, return the index of `target` if it is in `nums`, or `-1` if it is not in `nums`.

🔗 [LeetCode Problem Link](https://leetcode.com/problems/search-in-rotated-sorted-array/)

# 🚀 Solution Approach
- This is a **modified binary search** problem.  
- At each step:
  1. Find `mid`.
  2. Check if `nums[mid] == target`.
  3. If the **left half** (`nums[left] → nums[mid]`) is sorted:
     - If `target` lies in that range → search left.
     - Else → search right.
  4. Otherwise, the **right half** is sorted:
     - If `target` lies in that range → search right.
     - Else → search left.

- **Time Complexity:** O(log n)  
- **Space Complexity:** O(1)

## 📝 Code
```python
from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            if nums[left] <= nums[mid]:
                if nums[left] <= target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            else:
                if nums[mid] < target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1
        return -1
