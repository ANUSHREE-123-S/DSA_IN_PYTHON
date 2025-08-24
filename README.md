# DSA_IN_PYTHON
# LeetCode Solutions

## 1. Two Sum

**Problem Link:** [Two Sum](https://leetcode.com/problems/two-sum/)

### Problem Statement
Given an array of integers `nums` and an integer `target`, return the indices of the two numbers such that they add up to `target`.  
You may assume that each input would have exactly one solution, and you may not use the same element twice.  
You can return the answer in any order.

### Solution (Python)
```python
from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        for i in range(len(nums)):
            hashmap[nums[i]] = i
        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in hashmap and hashmap[complement] != i:
                return [i, hashmap[complement]]
        return []
"""
Approach

Use a hash map to store numbers and their indices.

For each number, compute its complement (target - num).

Check if the complement exists in the hash map and is not the same index.

Time Complexity: O(n)

Space Complexity: O(n)
"""
