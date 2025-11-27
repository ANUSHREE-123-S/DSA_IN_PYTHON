
# 🏠 House Robber — README

## 📘 Problem Summary

You are a professional robber planning to rob houses along a street.
Each house has a certain amount of money, but **adjacent houses cannot be robbed on the same night** because they have security systems connected.

You are given an integer array `nums`, where each `nums[i]` represents the amount of money in the `i-th` house.

### 🎯 Goal

Return the **maximum amount of money** you can rob *without robbing two adjacent houses*.

---

## ✅ Approach: Dynamic Programming (Space Optimized)

This problem is a classic **Dynamic Programming** question.

At each house, you have two choices:

1. **Rob it** → add the current house money to the value robbed two houses back (`rob1 + nums[i]`)
2. **Skip it** → take the maximum amount till previous house (`rob2`)

We iteratively compute the best option using two variables:

* `rob1` → max money robbed up to house *i-2*
* `rob2` → max money robbed up to house *i-1*

For each house:

```
newRob = max(rob2, rob1 + nums[i])
```

This gives the optimal solution using **O(1) space** and **O(n) time**.

---

## 💡 Intuition

* If you rob the current house → you must skip the previous house.
* If you skip the current house → you keep whatever was the best total up to the previous house.
* Always choose the better of the two decisions.

---

## 🧩 Code Implementation

```python
class Solution:
    def rob(self, nums: List[int]) -> int:
        rob1, rob2 = 0, 0
        
        for n in nums:
            newrob = max(rob2, rob1 + n)
            rob1 = rob2
            rob2 = newrob
        
        return rob2
```

---

## ⏱️ Time & Space Complexity

| Complexity | Value |
| ---------- | ----- |
| **Time**   | O(n)  |
| **Space**  | O(1)  |

---

## 📝 Example

**Input:** `nums = [2,7,9,3,1]`
**Output:** `12`
**Explanation:** Rob house 1 (2), house 3 (9), and house 5 (1) ⇒ total = 12.

---

## 🏁 Summary

* Choose between robbing or skipping each house.
* Use only two variables to track previous best results.
* Efficient and optimal DP solution.


