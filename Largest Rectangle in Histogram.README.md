# 📊 Largest Rectangle in Histogram

## Problem Description
Given an array `heights` representing the height of bars in a histogram, return the **area of the largest rectangle** that can be formed inside the histogram.

# Approach

We solve this using a **monotonic stack**:

1. Traverse through each bar (index `i` and height `h`).
2. Maintain a stack of indices of **increasing heights**.
3. If the current height is smaller than the stack’s top:
   - Pop from stack until the stack is valid.
   - For each popped bar:
     - Compute its area as `height × width`.
     - Width is determined by the current index and the new stack top.
4. After traversal, process remaining bars in the stack (as if heights end with `0`).
5. Track the maximum area found.

# Complexity Analysis
- **Time Complexity:** `O(n)`  
  Each bar is pushed and popped at most once.  
- **Space Complexity:** `O(n)`  
  For storing indices in the stack.  

# Code Implementation

```python
class Solution:
    def largestRectangleArea(self, heights):
        stack = []  # store indices of bars
        max_area = 0

        for i, h in enumerate(heights):
            while stack and heights[stack[-1]] > h:
                height = heights[stack.pop()]
                width = i if not stack else i - stack[-1] - 1
                max_area = max(max_area, height * width)
            stack.append(i)

        n = len(heights)
        while stack:
            height = heights[stack.pop()]
            width = n if not stack else n - stack[-1] - 1
            max_area = max(max_area, height * width)

        return max_area
