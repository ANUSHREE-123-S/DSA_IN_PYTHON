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
