class Solution:
    def rob(self, nums: List[int]) -> int:
        

        # cannot rob two adjacent houses

        # two choices: rob dp[i - 2] or nums[i] can be robbed or continue using dp[i - 1]
        n = len(nums)
        if n == 1:
            return nums[0]
        dp = [0 for _ in range(n)]
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])
        for i in range(2, len(nums)):
            dp[i] = max(dp[i - 2] + nums[i], dp[i - 1])
        print(dp)
        return dp[n - 1]