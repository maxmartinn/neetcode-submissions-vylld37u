class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        
        dp = [0] * (n + 1)
        dp[1] = 1  # 1 way to climb 1 stair
        dp[2] = 2  # 2 ways to climb 2 stairs
        
        for i in range(3, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2]
        
        return dp[n]