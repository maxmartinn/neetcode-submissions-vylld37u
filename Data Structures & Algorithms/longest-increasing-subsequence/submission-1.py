class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [1 for _ in range(n)]

        # start from the back

        # check from current to end of list to see if theres any larger values

        # if a larger value is spotted get the maximum of that LIS and current

        for i in range(n - 1, -1, -1):
            for j in range(i + 1, n):
                if nums[i] < nums[j]:
                    dp[i] = max(dp[j] + 1, dp[i])
        return max(dp)


