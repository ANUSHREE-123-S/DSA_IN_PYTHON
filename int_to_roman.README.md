# Integer to Roman (LeetCode 12)

## 📌 Problem Statement
Given an integer, convert it to a Roman numeral.

🔗 [LeetCode Problem Link](https://leetcode.com/problems/integer-to-roman/)

---

## 💡 Roman Numeral Rules
Roman numerals are based on these symbols:

| Value | Symbol |
|-------|---------|
| 1     | I       |
| 4     | IV      |
| 5     | V       |
| 9     | IX      |
| 10    | X       |
| 40    | XL      |
| 50    | L       |
| 90    | XC      |
| 100   | C       |
| 400   | CD      |
| 500   | D       |
| 900   | CM      |
| 1000  | M       |

Roman numerals are formed by **greedy subtraction**: repeatedly subtract the largest possible value.


## 🚀 Solution Approach
1. Define a mapping of integers → Roman symbols.
2. Iterate over values in descending order.
3. For each value, append its symbol to the result while subtracting from `num`.
4. Continue until `num` is reduced to `0`.


# ⏱️ Complexity
- **Time Complexity:** `O(1)` (constant number of Roman numeral values)  
- **Space Complexity:** `O(1)`

# 📝 Code
```python
class Solution:
    def intToRoman(self, num: int) -> str:
        num_map = {
            1: 'I', 4: 'IV', 5: 'V', 9: 'IX',
            10: 'X', 40: 'XL', 50: 'L', 90: 'XC',
            100: 'C', 400: 'CD', 500: 'D', 900: 'CM',
            1000: 'M'
        }
        result = ""
        for n in [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]:
            while num >= n:
                result += num_map[n]
                num -= n
        return result
