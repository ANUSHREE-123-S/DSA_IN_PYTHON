# Palindromic Substrings (LeetCode 647)

## 📌 Problem Statement
Given a string `s`, return the **number of palindromic substrings** in it.  

A substring is palindromic if it reads the same backward as forward.

🔗 [LeetCode Problem Link](https://leetcode.com/problems/palindromic-substrings/)

# 🚀 Solution Approach
We use the **Expand Around Center** approach:
- Every palindrome has a center (either a single character or between two characters).
- Expand outward while characters match.
- Count all palindromes found during expansion.

# Complexity
- **Time Complexity:** O(n²)  
- **Space Complexity:** O(1)  

## 📝 Code
```python
class Solution:
    def countSubstrings(self, s: str) -> int:
        res = 0
        for i in range(len(s)):
            # Odd-length palindromes
            l = r = i
            while l >= 0 and r < len(s) and s[l] == s[r]:
                res += 1
                l -= 1
                r += 1

            # Even-length palindromes
            l, r = i, i + 1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                res += 1
                l -= 1
                r += 1

        return res
