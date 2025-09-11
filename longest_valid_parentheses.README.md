# Longest Valid Parentheses (LeetCode 32)

## 📌 Problem Statement
Given a string `s` containing just the characters `'('` and `')'`,  
find the **length of the longest valid (well-formed) parentheses substring**.

🔗 [LeetCode Problem Link](https://leetcode.com/problems/longest-valid-parentheses/)

# 🚀 Solution Approach
We use a **stack** to track indices of unmatched parentheses:
- Start with `stack = [-1]` as a base index.
- Traverse the string:
  - If `'('`, push its index.
  - If `')'`, pop from the stack.
    - If stack is empty, push current index as a new base.
    - Otherwise, calculate valid length = `i - stack[-1]`.
- Keep track of the **maximum length** found.

# Complexity
- **Time Complexity:** O(n) — one pass through the string.  
- **Space Complexity:** O(n) — stack usage in the worst case.  

## 📝 Code
```python
class Solution:
    def longestValidParentheses(self, s: str) -> int:
        stack = [-1]
        max_len = 0

        for i in range(len(s)):
            if s[i] == "(":
                stack.append(i)
            else:
                stack.pop()
                if not stack:
                    stack.append(i)
                else:
                    max_len = max(max_len, i - stack[-1])

        return max_len
