# String to Integer (atoi) (LeetCode 8)

## 📌 Problem Statement
Implement the `myAtoi(string s)` function, which converts a string to a **32-bit signed integer**.

The algorithm should:
1. Ignore leading whitespace.
2. Check for an optional '+' or '-' sign.
3. Read in digits until a non-digit is encountered.
4. Clamp result to the 32-bit signed integer range: [-2^31, 2^31 - 1].

🔗 [LeetCode Problem Link](https://leetcode.com/problems/string-to-integer-atoi/)

# 🚀 Solution Approach
- Strip leading/trailing spaces.
- Determine the sign (`+` or `-`).
- Read digits until encountering a non-digit character.
- Convert digits into an integer.
- Clamp the result into the 32-bit signed integer range:
  - INT_MIN = -2³¹  
  - INT_MAX = 2³¹ - 1

# Complexity
- **Time Complexity:** O(n)  
- **Space Complexity:** O(1)  

# 📝 Code
```python
class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.strip()
        if not s:
            return 0

        sign = 1
        res = 0

        if s[0] == '+' or s[0] == '-':
            if s[0] == '-':
                sign = -1
            s = s[1:]

        for char in s:
            if not char.isdigit():
                break
            res = res * 10 + int(char)

        res *= sign

        if res < -2**31:
            return -2**31
        elif res > 2**31 - 1:
            return 2**31 - 1
        return res
