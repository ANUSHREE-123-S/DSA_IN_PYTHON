

# 🏠 House Robber II — README

## 🔍 Problem Summary

You are given an array `nums` where each element represents the amount of money in a house.
However, **all houses are arranged in a circle**, which means:

* You **cannot rob two adjacent houses**
* The **first and last house are also adjacent**

Your goal is to return the **maximum amount of money** you can rob without triggering alarms.

---

## 💡 Key Insight

Since the first and last houses are adjacent, you can’t rob both.
So, break the problem into **two linear cases**:

1. **Rob houses from index `0` to `n-2`** (exclude last)
2. **Rob houses from index `1` to `n-1`** (exclude first)

Then take the **maximum** of the two results.

This reduces the circular problem to the original **House Robber I** problem.

---

## 🧠 Approach Explained

We use a helper function `rob_linear()` that works exactly like House Robber I:

```
rob[i] = max(rob[i-1], rob[i-2] + nums[i])
```

But to optimize space, we use two variables:

* `rob1` → (i−2)th result
* `rob2` → (i−1)th result

Update them iteratively.

---

## ✅ Time & Space Complexity

| Operation | Complexity |
| --------- | ---------- |
| Time      | **O(n)**   |
| Space     | **O(1)**   |

---

## 📌 Code

```python
class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums)==1:
            return nums[0]
        
        def rob_linear(arr):
            rob1,rob2=0,0
            for money in arr:
                newrob=max(rob2,rob1+money)
                rob1=rob2
                rob2=newrob
            return rob2
        
        case1=rob_linear(nums[:-1])  # Exclude last house
        case2=rob_linear(nums[1:])   # Exclude first house
        
        return max(case1, case2)
```

---

## 🧪 Example

**Input:**
`nums = [2, 3, 2]`

**Possible choices:**

* Rob houses 1 & 3 → invalid (adjacent in circle)
* Rob house 2 → 3

**Output:**
`3`

