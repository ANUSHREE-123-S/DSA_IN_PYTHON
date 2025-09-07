# Merge Sorted Array (LeetCode 88)

## 📌 Problem Statement
You are given two integer arrays `nums1` and `nums2`, sorted in **non-decreasing order**,  
and two integers `m` and `n`, representing the number of elements in `nums1` and `nums2` respectively.  

Merge `nums2` into `nums1` as one sorted array.  
The final sorted array should not be returned by the function, but instead be stored inside `nums1`.

🔗 [LeetCode Problem Link](https://leetcode.com/problems/merge-sorted-array/)

# 🚀 Solution Approach
- Use **three pointers**:
  - `x = m - 1` (last valid element in nums1)
  - `y = n - 1` (last element in nums2)
  - `z = m + n - 1` (last index of nums1)
- Compare `nums1[x]` and `nums2[y]`, place the larger one at `nums1[z]`.
- Move the respective pointer (`x` or `y`) backward.
- Continue until all elements from nums2 are merged into nums1.

- **Time Complexity:** O(m + n)  
- **Space Complexity:** O(1) (in-place merge)

# 📝 Code
```python
from typing import List

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        x, y = m - 1, n - 1
        for z in range(m + n - 1, -1, -1):
            if x < 0:
                nums1[z] = nums2[y]
                y -= 1
            elif y < 0:
                break
            elif nums1[x] > nums2[y]:
                nums1[z] = nums1[x]
                x -= 1
            else:
                nums1[z] = nums2[y]
                y -= 1
