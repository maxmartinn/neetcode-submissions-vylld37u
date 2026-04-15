class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)
        dp = [False for _ in range(len(s) + 1)]
        dp[n] = True # repersents empty string

        for i in range(n - 1, -1, -1):
            for w in wordDict:
                if s[i: i + len(w)] == w and dp[i + len(w)] == True:
                    dp[i] = True
        return dp[0]