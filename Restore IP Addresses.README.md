# 🌐 Restore IP Addresses

## 🧩 Problem Description
Given a string `s` containing only digits, return **all possible valid IP address combinations** that can be formed by inserting dots (`.`) into `s`.

A **valid IP address** consists of **exactly four integers (0–255)**, separated by single dots, with no leading zeros (except for the number 0 itself).

# 💡 Approach — Backtracking

We use **backtracking** to explore all possible placements of dots (`.`) that divide the string into **four valid segments**.

At each recursive step:
- We try to form a segment of length `1`, `2`, or `3`.
- We validate the segment:
  - It cannot have leading zeros (e.g. `"01"` ❌).
  - Its integer value must be between `0` and `255`.
- If the segment is valid, we continue building the next segment.
- Once we have **4 valid segments** and have used up all digits, we join them with dots and store the result.

# 🪜 Steps

1. Define a recursive helper function `backtrack(start, path)`:
   - `start` → current index in the string.
   - `path` → list of valid segments found so far.
2. Base case:  
   If `len(path) == 4` and `start == len(s)` → add `".".join(path)` to the result.
3. Loop through segment lengths 1 to 3:
   - Extract substring `s[start:start+length]`.
   - Check if it’s a valid segment (no leading zero unless it's `"0"`, and ≤ 255).
   - If valid → recurse with updated `start` and `path`.
4. Return all valid IP addresses.

# ✅ Code Implementation

```python
from typing import List

class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        res = []

        def backtrack(start, path):
            if len(path) == 4:
                if start == len(s):
                    res.append(".".join(path))
                return

            for length in range(1, 4):
                if start + length > len(s):
                    break
                part = s[start:start+length]

                # Skip invalid parts
                if (part.startswith("0") and len(part) > 1) or int(part) > 255:
                    continue

                backtrack(start + length, path + [part])

        backtrack(0, [])
        return res
