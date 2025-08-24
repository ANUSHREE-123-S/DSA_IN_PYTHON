2. Best Time to Buy and Sell Stock (LeetCode 121)

## 📌 Problem Statement
You are given an array `prices` where `prices[i]` is the price of a given stock on the `i-th` day.  

You want to maximize your profit by choosing a single day to **buy one stock** and choosing a different day in the future to **sell that stock**.  

Return the maximum profit you can achieve from this transaction. If no profit is possible, return `0`.

🔗 [LeetCode Problem Link](https://leetcode.com/problems/best-time-to-buy-and-sell-stock/)

## 🚀 Solution Approach
- Keep track of the **minimum price** encountered so far.
- At each day, calculate the profit if selling today (`prices[i] - min_price`).
- Update the maximum profit accordingly.
- Time Complexity: **O(n)**
- Space Complexity: **O(1)**

--📝 Code
```python
from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        
        buy_price = prices[0]
        profit = 0
        n = len(prices)
        
        for i in range(1, n):
            if prices[i] < buy_price:
                buy_price = prices[i]
            else:
                profit = max(profit, prices[i] - buy_price)
        
        return profit

