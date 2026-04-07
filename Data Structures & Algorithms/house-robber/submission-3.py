class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        dp = [0] * len(nums)
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])
        for i in range(2, len(nums)):
            curr = max(nums[i] + dp[i - 2], dp[i - 1])
            dp[i] = curr
        return max(dp[-1], dp[-2])

