class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [float("inf") for _ in range(amount + 1)] # dp[i] repersents the minimum number of coins to create i
        dp[0] = 0
        for i in range(1, amount + 1):
            for c in coins:
                dp[i] = min(dp[i], 1 + dp[i - c] if i - c >= 0 else float("inf"))
        print(dp)
        # amount = 12
        # coins = [1, 5, 10]
        # [3, 2, 1, 5, 4, 3, 2, 1, 4, 3, 2, 1, 0]
        return dp[amount] if dp[amount] != float("inf") else -1
