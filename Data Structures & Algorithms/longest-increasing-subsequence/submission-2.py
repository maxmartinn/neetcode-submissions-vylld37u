class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [1 for _ in range(n)]


        # iterate through

        for i in range(n - 1, -1, -1):
            for j in range(i + 1, n):
                dp[i] = max(dp[j] + 1, dp[i]) if nums[i] < nums[j] else dp[i]
        return max(dp)


