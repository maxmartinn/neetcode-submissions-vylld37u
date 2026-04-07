class Solution:
    def climbStairs(self, n: int) -> int:
        # (n)
        dp = [1, 1]
        for i in range(n - 1):
            dp[0], dp[1] = dp[1], dp[0] + dp[1]
        
        return dp[1]