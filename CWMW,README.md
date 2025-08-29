# Container With Most Water (LeetCode 11)

## 📌 Problem Statement
You are given an integer array `height` of length `n`. There are `n` vertical lines drawn such that the two endpoints of the i-th line are `(i, 0)` and `(i, height[i])`.

Find two lines that together with the x-axis form a container, such that the container contains the **most water**.

Return the maximum amount of water a container can store.

🔗 [LeetCode Problem Link](https://leetcode.com/problems/container-with-most-water/)

# 🚀 Solution Approach
- Use **two pointers**: `left = 0`, `right = n-1`.
- Calculate area = `(right-left) * min(height[left], height[right])`.
- Update the maximum area.
- Move the pointer pointing to the smaller line inward (since moving the taller line cannot increase area).
- Repeat until `left < right`.

- **Time Complexity:** O(n)  
- **Space Complexity:** O(1)

# 📝 Code
```python
from typing import List

class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_area = 0
        left, right = 0, len(height) - 1
        while left < right:
            max_area = max(max_area, (right - left) * min(height[left], height[right]))
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return max_area
