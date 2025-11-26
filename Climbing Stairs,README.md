
# 🧗‍♂️ Climbing Stairs 

# 🔍 Problem Summary

You are climbing a staircase with **n steps**.
You can take **either 1 step or 2 steps at a time**.

Your task is to determine:

> **How many distinct ways can you reach the top?**

This is a classic **Dynamic Programming** problem.

---

## 💡 Key Insight

To reach step `n`, you could have come from:

* step `n-1` by taking **1 step**, OR
* step `n-2` by taking **2 steps**

So the recurrence becomes:

```
ways[n] = ways[n-1] + ways[n-2]
```

This is exactly the **Fibonacci sequence**!

---

# 🚀 Approach

Instead of using an array, we use **two variables** (`a` and `b`) to store:

* `a` → ways to reach step `n-2`
* `b` → ways to reach step `n-1`

Then compute next values iteratively in O(n) time and O(1) space.

# 🧩 Code Implementation

```python
class Solution:
    def climbStairs(self, n: int) -> int:
        if n<=2:
            return n
        a,b=1,2
        for _ in range(3,n+1):
            a,b=b,a+b
        return b
```

---
# ⏱️ Time & Space Complexity

| Type      | Complexity |
| --------- | ---------- |
| **Time**  | O(n)       |
| **Space** | O(1)       |

# 📝 Example

**Input:**

```
n = 4
```

**Computation:**

* ways(1) = 1
* ways(2) = 2
* ways(3) = 3
* ways(4) = 5

**Output:**

```
5
```

There are **5 distinct ways** to climb 4 steps.
# 🟦 Conclusion

This solution is optimal and uses constant space.
Great example of using **dynamic programming + Fibonacci logic** to simplify computation.
