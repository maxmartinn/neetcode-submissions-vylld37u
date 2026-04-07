class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        currMinPrice = prices[0]
        for i in range(1, len(prices)):
            profit = max(profit, prices[i] - currMinPrice)
            currMinPrice = min(prices[i], currMinPrice)
        return profit