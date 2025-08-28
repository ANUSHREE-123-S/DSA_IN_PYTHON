# Insert Interval (LeetCode 57)

## 📌 Problem Statement
You are given an array of non-overlapping intervals `intervals` where `intervals[i] = [start, end]` sorted in ascending order by `start`, and a new interval `newInterval = [start, end]`.  

Insert `newInterval` into `intervals` such that the intervals remain non-overlapping and sorted.  

Return the resulting array of intervals.

🔗 [LeetCode Problem Link](https://leetcode.com/problems/insert-interval/)

## 🚀 Solution Approach
1. Append all intervals ending before `newInterval` starts.
2. Merge all intervals overlapping with `newInterval`.
3. Append the merged `newInterval`.
4. Add all intervals starting after `newInterval`.

- **Time Complexity:** O(n)  
- **Space Complexity:** O(n)

CODE
``python
from typing import List

class Solution:
    def insert(self, intervals: List[List[int]], newinterval: List[int]) -> List[List[int]]:
        result = []
        i = 0
        n = len(intervals)
        while i < n and intervals[i][1] < newinterval[0]:
            result.append(intervals[i])
            i += 1
        while i < n and intervals[i][0] <= newinterval[1]:
            newinterval[0] = min(newinterval[0], intervals[i][0])
            newinterval[1] = max(newinterval[1], intervals[i][1])
            i += 1
        result.append(newinterval)
        while i < n:
            result.append(intervals[i])
            i += 1
        return result
