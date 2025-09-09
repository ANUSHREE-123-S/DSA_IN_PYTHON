# Find the Index of the First Occurrence in a String (LeetCode 28)

## 📌 Problem Statement
Given two strings `haystack` and `needle`, return the **index of the first occurrence** of `needle` in `haystack`.  
If `needle` is not part of `haystack`, return `-1`.

🔗 [LeetCode Problem Link](https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/)

# 🚀 Solution Approach
We use a **sliding window**:
- Iterate over `haystack` from index `0` to `len(haystack) - len(needle)`.
- Compare each substring of length `len(needle)` with `needle`.
- If a match is found, return the index.
- If no match is found, return `-1`.

# Complexity
- **Time Complexity:** O(n * m)  
  - where `n = len(haystack)`, `m = len(needle)`  
- **Space Complexity:** O(1)  

# 📝 Code
```python
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        for i in range(len(haystack) - len(needle) + 1):
            if haystack[i:i+len(needle)] == needle:
                return i
        return -1
