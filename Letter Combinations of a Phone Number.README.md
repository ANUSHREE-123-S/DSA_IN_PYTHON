# ☎️ Letter Combinations of a Phone Number

## 🧩 Problem Description
Given a string containing digits from `2-9`, return **all possible letter combinations** that the number could represent.

The mapping of digits to letters is the same as on a **telephone keypad**.

# 💡 Approach — Backtracking (DFS)

This problem is a classic **backtracking** question.  
We explore all possible combinations of letters corresponding to the input digits.

# 🔹 Idea:
1. Create a mapping (`phone_map`) of each digit to its corresponding letters.
2. Use a recursive function `backtrack(index, path)` to:
   - Keep track of the current position (`index`) in the input digits.
   - Store the current partial combination (`path`).
3. When we reach the end of digits (`index == len(digits)`), we add the complete combination to our result list.
4. Otherwise, we iterate through each letter mapped to the current digit and continue recursion.

# ✅ Code Implementation

```python
class Solution:
    def letterCombinations(self, digits: str):
        if not digits:
            return []
        
        phone_map = {
            "2": "abc", "3": "def", "4": "ghi", "5": "jkl",
            "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"
        }
        
        res = []

        def backtrack(index, path):
            if index == len(digits):
                res.append("".join(path))
                return
            for char in phone_map[digits[index]]:
                backtrack(index + 1, path + [char])
        
        backtrack(0, [])
        return res
