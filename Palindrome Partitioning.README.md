# ✂️ Palindrome Partitioning

## 🧩 Problem Description
Given a string `s`, partition it such that every substring of the partition is a **palindrome**.  
Return all possible palindrome partitioning combinations.

A **palindrome** is a string that reads the same backward as forward.

**Explanation:**
- `"a"`, `"a"`, `"b"` → all are palindromes  
- `"aa"`, `"b"` → both are palindromes  

# 💡 Approach — Backtracking

We use **backtracking** to explore all possible ways to partition the string.  
At each step:
- We try all possible substrings starting from the current index.
- If the substring is a palindrome → include it and recursively explore further.
- If we reach the end of the string → add the current path to the result.

# 🪜 Steps
1. Define a helper function `is_palindrome(sub)` to check if a substring is a palindrome.
2. Use a recursive function `backtrack(start)`:
   - Base case: if `start == len(s)`, append the current partition (path) to `res`.
   - Loop through all possible end indices.
   - For each substring `s[start:end]`:
     - If it’s a palindrome → add it to the path and recurse from `end`.
     - After recursion → remove the last element (backtrack).
3. Return all valid palindrome partitions.

 ✅ Code Implementation

```python
from typing import List

class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        path = []

        def is_palindrome(sub):
            return sub == sub[::-1]

        def backtrack(start):
            if start == len(s):
                res.append(path[:])
                return

            for end in range(start + 1, len(s) + 1):
                substring = s[start:end]
                if is_palindrome(substring):
                    path.append(substring)
                    backtrack(end)
                    path.pop()

        backtrack(0)
        return res
