# Roman to Integer (LeetCode 13)

## 📌 Problem Statement
Given a Roman numeral, convert it into an integer.

🔗 [LeetCode Problem Link](https://leetcode.com/problems/roman-to-integer/)

---

## 💡 Roman Numeral Rules
Roman numerals are based on these values:

| Symbol | Value |
|--------|-------|
| I      | 1     |
| V      | 5     |
| X      | 10    |
| L      | 50    |
| C      | 100   |
| D      | 500   |
| M      | 1000  |

Special cases involve **subtractive notation**:
- `IV = 4` (5 - 1)
- `IX = 9` (10 - 1)
- `XL = 40` (50 - 10)
- `XC = 90` (100 - 10)
- `CD = 400` (500 - 100)
- `CM = 900` (1000 - 100)

# 🚀 Solution Approach
1. Map each Roman symbol to its integer value.
2. Traverse the string:
   - If a numeral is smaller than the next one → subtract it.
   - Otherwise → add it.
3. Add the last numeral (always counted).

# ⏱️ Complexity
- **Time Complexity:** `O(n)` (traverse each character once)  
- **Space Complexity:** `O(1)` (fixed mapping dictionary)

# 📝 Code
```python
class Solution:
    def romanToInt(self, s: str) -> int:
        roman_map = {
            'I': 1, 'V': 5, 'X': 10,
            'L': 50, 'C': 100, 'D': 500, 'M': 1000
        }
        total = 0
        for i in range(len(s) - 1):
            if roman_map[s[i]] < roman_map[s[i + 1]]:
                total -= roman_map[s[i]]
            else:
                total += roman_map[s[i]]
        total += roman_map[s[-1]]
        return total

## 💡 Example
### Example 1:
