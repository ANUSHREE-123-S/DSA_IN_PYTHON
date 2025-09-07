# Longest Substring Without Repeating Characters (LeetCode 3)

## 📌 Problem Statement
Given a string `s`, find the length of the **longest substring** without repeating characters.

🔗 [LeetCode Problem Link](https://leetcode.com/problems/longest-substring-without-repeating-characters/)

# 🚀 Solution Approach
- Use a **sliding window** with two pointers (`l`, `r`).
- Keep a **set** of characters to track duplicates.
- Expand the right pointer (`r`) and check if character already exists in the set.
- If duplicate found → shrink from the left (`l`) until no duplicates remain.
- Update `longest` with the maximum window size.

- **Time Complexity:** O(n)  
- **Space Complexity:** O(k), where `k` is the character set size (e.g., 26/128/256).

# 📝 Code
```python
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        longest = 0
        newset = set()
        n = len(s)

        for r in range(n):
            while s[r] in newset:
                newset.remove(s[l])
                l += 1
            newset.add(s[r])
            longest = max(longest, r - l + 1)

        return longest
