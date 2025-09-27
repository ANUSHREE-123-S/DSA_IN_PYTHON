# 🔄 Next Greater Element II

## Problem Description
You are given a **circular array** `nums` (the next element of the last element is the first element of the array).  
For each element in `nums`, find the **next greater number**.  
If it does not exist, return `-1`.

Explanation:  
- For `1` → Next greater is `2`  
- For `2` → No greater element → `-1`  
- For last `1` → Since the array is circular, next greater is `2`
# Approach

This is solved using a **monotonic decreasing stack** and the **circular array trick**:

1. Use an array `res` initialized with `-1` to store results.
2. Traverse the array **twice** (`2 * n` times) to simulate circularity.
   - Use `nums[i % n]` to wrap around indices.
3. Maintain a stack of indices where we haven’t found a next greater element yet.
4. For each number:
   - While stack is not empty and the current number is greater than `nums[stack[-1]]`, update `res` for that index.
   - If we are in the **first pass** (`i < n`), push the index to the stack.
5. Return `res`.

# Complexity Analysis

- **Time Complexity:** `O(n)`  
  Each element is pushed and popped at most once.  
- **Space Complexity:** `O(n)`  
  Stack + result array.
# Code Implementation

```python
from typing import List

class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [-1] * n
        stack = []

        for i in range(2 * n):
            num = nums[i % n]
            while stack and nums[stack[-1]] < num:
                res[stack.pop()] = num
            if i < n:
                stack.append(i)

        return res
