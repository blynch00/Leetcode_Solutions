from collections import *
from typing import *
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) == 1:
            return 0
        # "buy low, sell high"
        buy, sell = 0, 1
        profit = 0
        # While we still have potential days to sell
        while sell < len(prices):
            # If we found a new profitable day, update profit
            if prices[sell] > prices[buy]:
                curr_prof = prices[sell] - prices[buy]
                profit = max(profit, curr_prof)
            else:
                # Otherwise, the best day to buy is updated
                buy = sell
            sell += 1
        return profit

