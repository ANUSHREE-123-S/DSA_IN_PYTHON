# Zigzag Conversion (LeetCode 6)

## 📌 Problem Statement
The string `s` is written in a zigzag pattern on a given number of rows.
Then it is read line by line. Convert the string into that form.

🔗 [LeetCode Problem Link](https://leetcode.com/problems/zigzag-conversion/)

# 🚀 Solution Approach
1. Use a list of strings to represent each row.
2. Traverse characters in `s`, appending each to the current row.
3. Change direction when hitting the first or last row.
4. Concatenate all rows at the end.

# ⏱️ Complexity
- **Time Complexity:** `O(n)` (iterate once through the string)
- **Space Complexity:** `O(n)` (store characters in row buckets)

# 📝 Code
```python
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1 or numRows >= len(s):
            return s
        rows = [""] * numRows
        curr = 0
        going_down = False
        for char in s:
            rows[curr] += char
            if curr == 0 or curr == numRows - 1:
                going_down = not going_down
            curr += 1 if going_down else -1
        return "".join(rows)
