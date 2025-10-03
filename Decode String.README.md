# 🔐 Decode String

## Problem Description
Given an encoded string, return its decoded version.

The encoding rule is:
where `encoded_string` inside the square brackets is repeated exactly `k` times.  
You may assume the input string is always valid and contains only:
- Digits (`0-9`)
- Lowercase English letters
- Brackets (`[`, `]`)

### Example 1
**Input:**

## Approach

We use **two stacks**:
1. `numstack` → stores repetition counts (`k`)  
2. `strstack` → stores previous strings before encountering `[`  

We also keep track of:
- `currstr`: the string being built  
- `currnum`: the number being built (in case of multiple digits like `12[a]`)  

### Steps:
1. Traverse each character in `s`.  
2. If it’s a **digit** → build the current number.  
3. If it’s a **`[`**:
   - Push `currnum` to `numstack`
   - Push `currstr` to `strstack`
   - Reset `currnum` and `currstr`  
4. If it’s a **`]`**:
   - Pop repetition count from `numstack`
   - Pop previous string from `strstack`
   - Repeat `currstr` `k` times and append to previous string  
5. If it’s a **letter**, append to `currstr`.  
6. Return `currstr` at the end.  

## Complexity Analysis
- **Time Complexity:** `O(n)` → each character is processed once  
- **Space Complexity:** `O(n)` → for stacks in the worst case (nested brackets)  

# Code Implementation

```python
class Solution:
    def decodeString(self, s: str) -> str:
        numstack = []
        strstack = []
        currstr = ""
        currnum = 0

        for ch in s:
            if ch.isdigit():
                currnum = currnum * 10 + int(ch)
            elif ch == "[":
                numstack.append(currnum)
                strstack.append(currstr)
                currnum = 0
                currstr = ""
            elif ch == "]":
                repeatetimes = numstack.pop()
                prevstr = strstack.pop()
                currstr = prevstr + currstr * repeatetimes
            else:
                currstr += ch

        return currstr
