# 🔥 Sliding Window Maximum

## Problem Description
You are given an array `nums` and an integer `k`.  
Return the **maximum value in each sliding window of size `k`** as the window moves from left to right.

# Approach

We solve this using a **monotonic decreasing deque**:

1. Use a deque to store **indices** of elements, keeping the values in decreasing order:
   - The front (`dq[0]`) always stores the index of the current window’s maximum.
2. For each index `i`:
   - Remove elements from the front if they are **out of the window** (`i - k`).
   - Remove elements from the back while they are **smaller than the current element**, since they can never be maximum again.
   - Add the current index to the deque.
3. Starting from `i >= k-1`, record the **maximum** (the value at `nums[dq[0]]`).

# Complexity Analysis
- **Time Complexity:** `O(n)`  
  Each element is added and removed from deque at most once.
- **Space Complexity:** `O(k)`  
  Deque stores at most `k` indices.

# Code Implementation

```python
from collections import deque

class Solution:
    def maxSlidingWindow(self, nums, k):
        dq = deque()   # stores indices of elements
        result = []

        for i in range(len(nums)):
            # Remove elements outside the current window
            if dq and dq[0] == i - k:
                dq.popleft()

            # Maintain decreasing order in deque
            while dq and nums[dq[-1]] < nums[i]:
                dq.pop()

            dq.append(i)

            # Append the maximum once the first window is complete
            if i >= k - 1:
                result.append(nums[dq[0]])

        return result
