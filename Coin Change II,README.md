# 📘 Problem Summary

You are given:

* An integer **amount**
* An array of **coins**, each representing a coin denomination

Your task is to determine **how many combinations** of coins can be used to make the given amount.
**Order does not matter** — combinations, not permutations.

This corresponds to **LeetCode 518 – Coin Change II**.
# 💡 Approach

# 🔹 Key Idea

Use **Dynamic Programming (DP)** to count the number of ways to make each amount from `0` to `amount`.

# 🔹 DP Definition

`dp[x]` = the number of ways to make amount `x` using the coins considered so far.

# 🔹 Base Case

```
dp[0] = 1
```

There is **1 way** to make amount 0: choose no coins.

# 🔹 Transition

For each coin:

```
dp[x] += dp[x - coin]
```

Meaning:

* When using a coin of value `coin`, the number of new combinations for amount `x` is the number of ways to make `x - coin`.

### 🔹 Why Outer Loop Over Coins?

To avoid counting permutations.
E.g., `[1,2]` and `[2,1]` are treated as the **same combination**, which is why coins must be fixed first.

# ✅ Time & Space Complexity

* **Time Complexity:**
  ( O(n \times \text{amount}) )
  where `n` is the number of coins.

* **Space Complexity:**
  ( O(\text{amount}) )

# 🧠 Code Implementation

```python
class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = [0] * (amount + 1)
        dp[0] = 1

        for coin in coins:
            for x in range(coin, amount + 1):
                dp[x] += dp[x - coin]

        return dp[amount]
```

---

## 📝 Example

**Input:**

```
amount = 5
coins = [1,2,5]
```

**Output:**

```
4
```

**Explanation:**
The combinations are:

1. 1+1+1+1+1
2. 1+1+1+2
3. 1+2+2
4. 5

# 🎯 Why This Works

* The DP ensures all smaller subproblems are solved first.
* Coins loop first ensures combinations (not permutations) are counted.
* Space-efficient 1D DP array stores only necessary information.
