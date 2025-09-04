# Valid Palindrome (LeetCode 125)

## 📌 Problem Statement
A phrase is a **palindrome** if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward.  
Given a string `s`, return `true` if it is a palindrome, or `false` otherwise.

🔗 [LeetCode Problem Link](https://leetcode.com/problems/valid-palindrome/)

# 🚀 Solution Approach
- Use the **two-pointer technique**:
  - Initialize `l` (left) at start and `r` (right) at end of the string.
  - Skip non-alphanumeric characters.
  - Compare characters after converting to lowercase.
  - If mismatch → return `False`.
  - If all match → return `True`.

- **Time Complexity:** O(n)  
- **Space Complexity:** O(1)

# 📝 Code
```python
class Solution:
    def isPalindrome(self, s: str) -> bool:
        l, r = 0, len(s) - 1
        while l < r:
            while l < r and not self.alphaNum(s[l]):
                l += 1
            while r > l and not self.alphaNum(s[r]):
                r -= 1
            if s[l].lower() != s[r].lower():
                return False
            l, r = l + 1, r - 1
        return True

    def alphaNum(self, c: str) -> bool:
        return (ord('A') <= ord(c) <= ord('Z') or
                ord('a') <= ord(c) <= ord('z') or
                ord('0') <= ord(c) <= ord('9'))
