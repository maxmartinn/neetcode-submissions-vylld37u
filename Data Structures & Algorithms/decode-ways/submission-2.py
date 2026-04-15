class Solution:
    def numDecodings(self, s: str) -> int:
        # start from the end 

        # 12 can be 1 2 or 12, cosnider 2 first, go to the 1 then see if checking the character behind current character can form a two digits number between 10 and 26 
        # [2 1]
        n = len(s)
        dp = [0 for _ in range(n + 1)]
        dp[n] = 1
        dp[n - 1] = 0 if s[n - 1] == "0" else 1

        for i in range(len(s) - 2, -1, -1):
            # consider digit 1
            dp[i] += 0 if s[i] == "0" else dp[i + 1] 

            # consider two digits
            dp[i] += dp[i + 2] if 10 <= int(s[i : i + 2]) <= 26 else 0
        print(dp)
        return dp[0]