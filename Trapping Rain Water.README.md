# 🌧️ Trapping Rain Water

## 🧩 Problem Description
Given `n` non-negative integers representing an elevation map where the width of each bar is `1`,  
compute how much water it can trap **after raining**.
# 💡 Approach — Two Pointer Technique

We use **two pointers (`left` and `right`)** to calculate trapped water efficiently.

1. Initialize:
   - `left = 0`, `right = len(height) - 1`
   - `left_max = 0`, `right_max = 0`
   - `trapped = 0` (to store total trapped water)
2. Move the pointer that has the **smaller height**:
   - If `height[left] < height[right]`:
     - If `height[left] >= left_max`: update `left_max`
     - Else: water trapped = `left_max - height[left]`
     - Move `left` one step right
   - Else:
     - If `height[right] >= right_max`: update `right_max`
     - Else: water trapped = `right_max - height[right]`
     - Move `right` one step left
3. Continue until `left >= right`.

This ensures every position’s trapped water is calculated only once.

---

## 🧠 Complexity Analysis
- **Time Complexity:** `O(n)` — Each element is visited once.  
- **Space Complexity:** `O(1)` — Only constant extra space used.  

---

## ✅ Code Implementation

```python
from typing import List

class Solution:
    def trap(self, height: List[int]) -> int:
        left, right = 0, len(height) - 1
        left_max = right_max = 0
        trapped = 0
        
        while left < right:
            if height[left] < height[right]:
                if height[left] >= left_max:
                    left_max = height[left]
                else:
                    trapped += left_max - height[left]
                left += 1
            else:
                if height[right] >= right_max:
                    right_max = height[right]
                else:
                    trapped += right_max - height[right]
                right -= 1
                
        return trapped
