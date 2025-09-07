# Longest Palindromic Substring (LeetCode 5)

## 📌 Problem Statement
Given a string `s`, return the **longest palindromic substring** in `s`.

🔗 [LeetCode Problem Link](https://leetcode.com/problems/longest-palindromic-substring/)

# 🚀 Solution Approach
We use the **Expand Around Center** approach:
- Each palindrome has a center (either one character or between two characters).
- Expand outward while the substring remains a palindrome.
- Track the longest palindrome found.

# Complexity
- **Time Complexity:** O(n²)  
- **Space Complexity:** O(1)  

# 📝 Code
```python
class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = ""
        longest = 0

        for i in range(len(s)):
            # Odd-length palindrome
            l, r = i, i
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r - l + 1) > longest:
                    res = s[l:r + 1]
                    longest = r - l + 1
                l -= 1
                r += 1

            # Even-length palindrome
            l, r = i, i + 1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r - l + 1) > longest:
                    res = s[l:r + 1]
                    longest = r - l + 1
                l -= 1
                r += 1

        return res
