class Solution:
    def rob(self, nums: List[int]) -> int:
        # first and last house cannot be robbed together. cosnider house rob excluding first house and excluding last house
        if len(nums) == 1:
            return nums[0]
        def house_rob(nums):
            if len(nums) == 1:
                return nums[0]
            dp = [0 for _ in range(len(nums))]
            dp[0] = nums[0]
            dp[1] = max(nums[0], nums[1])
            for i in range(2, len(nums)):
                dp[i] = max(dp[i - 2] + nums[i], dp[i - 1])
            return dp[len(nums) - 1]
        return max(nums[0], house_rob(nums[:-1]), house_rob(nums[1:]))