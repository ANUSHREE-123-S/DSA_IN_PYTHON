# 🔢 Next Greater Element I

## Problem Description
You are given two arrays **nums1** and **nums2**, where **nums1** is a subset of **nums2**.  
For each element in **nums1**, find the **next greater element** in **nums2**.  

The **next greater element** for an element `x` in `nums2` is the **first element to the right of `x`** that is greater than `x`.  
If no such element exists, return `-1`.
# Example

**Input:**  

# Approach

We solve this problem using a **monotonic decreasing stack**:

1. Traverse `nums2` in reverse order.
2. Maintain a stack that keeps track of potential "next greater" elements.
3. For each number:
   - Pop elements from the stack that are less than or equal to the current number.
   - If the stack is empty, there’s no next greater element → assign `-1`.
   - Otherwise, the top of the stack is the next greater element.
4. Store results in a hashmap (`next_greater`) for fast lookups.
5. For each number in `nums1`, retrieve the next greater element from the hashmap.

# Complexity Analysis

- **Time Complexity:** `O(n)` — Each element is pushed and popped from the stack at most once.
- **Space Complexity:** `O(n)` — Hashmap + stack.

# Code Implementation

```python
from typing import List

class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        next_greater = {}
        stack = []

        for num in reversed(nums2):
            while stack and stack[-1] <= num:
                stack.pop()
            next_greater[num] = -1 if not stack else stack[-1]
            stack.append(num)

        return [next_greater[num] for num in nums1]
