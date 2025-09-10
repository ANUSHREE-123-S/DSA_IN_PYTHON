# Valid Parentheses (LeetCode 20)

## 📌 Problem Statement
Given a string `s` containing just the characters `'('`, `')'`, `'{'`, `'}'`, `'['` and `']'`,  
determine if the input string is **valid**.

A string is valid if:
1. Open brackets are closed by the same type of brackets.
2. Open brackets are closed in the correct order.
3. Every closing bracket has a corresponding open bracket.

🔗 [LeetCode Problem Link](https://leetcode.com/problems/valid-parentheses/)

# 🚀 Solution Approach
- Use a **stack** to track opening brackets.
- Use a **hashmap** (`closeToOpen`) to map closing brackets to their corresponding opening brackets.
- For each character:
  - If it’s a **closing bracket**, check if it matches the last opening bracket in the stack.
  - Otherwise, push it into the stack.
- At the end, if the stack is empty, the string is valid.

# Complexity
- **Time Complexity:** O(n) — scan through the string once.  
- **Space Complexity:** O(n) — stack usage in the worst case.

# 📝 Code
```python
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        closeToOpen = {")": "(", "]": "[", "}": "{"}

        for c in s:
            if c in closeToOpen:
                if stack and stack[-1] == closeToOpen[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)

        return not stack
