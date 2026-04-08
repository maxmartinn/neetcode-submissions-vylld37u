class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)
        dp = [0 for _ in range(len(s) + 1)]
        dp[n] = 1
        dp[n - 1] = 1 if s[n - 1] != "0" else 0

        for i in range(n - 2, -1, -1):
            if s[i] != "0":
                dp[i] += dp[i + 1]
            
            two = int(s[i: i + 2])
            if 10 <= two <= 26:
                dp[i] += dp[i + 2]
        
        return dp[0]

