# Generate Parentheses (LeetCode 22)

## 📌 Problem Statement
Given `n` pairs of parentheses, generate **all combinations** of well-formed parentheses.

🔗 [LeetCode Problem Link](https://leetcode.com/problems/generate-parentheses/)

# 🚀 Solution Approach
This is a **backtracking problem**:
- We build parentheses strings step by step.
- At each step, we can add:
  - `'('` if we haven’t used all `n` opening parentheses.
  - `')'` if the number of closing parentheses is **less than** the number of opening ones.
- Once the string has `2 * n` characters, it’s valid and added to the result.

✅ This ensures **only valid parentheses sequences** are generated.

# Complexity
- **Time Complexity:** ~O(4^n / √n)  
  (follows Catalan number growth)  
- **Space Complexity:** O(n) (recursion depth + temporary string storage)

# 📝 Code
```python
from typing import List

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans, sol = [], []

        def backtrack(openn, close):
            if len(sol) == 2 * n:
                ans.append(''.join(sol))
                return
            if openn < n:
                sol.append('(')
                backtrack(openn + 1, close)
                sol.pop()
            if close < openn:
                sol.append(')')
                backtrack(openn, close + 1)
                sol.pop()

        backtrack(0, 0)
        return ans
