# Merge Intervals (LeetCode 56)

## 📌 Problem Statement
Given an array of `intervals` where `intervals[i] = [start, end]`, merge all **overlapping intervals** and return an array of the non-overlapping intervals that cover all the intervals in the input.

🔗 [LeetCode Problem Link](https://leetcode.com/problems/merge-intervals/)

# 🚀 Solution Approach
1. **Sort intervals** by starting time.
2. Initialize an empty `merged` list.
3. Traverse through each interval:
   - If `merged` is empty OR the current interval does not overlap, append it.
   - Otherwise, merge the current interval with the last one in `merged`.
4. Return `merged`.

- **Time Complexity:** O(n log n) (due to sorting)  
- **Space Complexity:** O(n)

## 📝 Code
```python
from typing import List

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        merged = []
        for interval in intervals:
            if not merged or merged[-1][1] < interval[0]:
                merged.append(interval)
            else:
                merged[-1][1] = max(merged[-1][1], interval[1])
        return merged
