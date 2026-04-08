class Solution:
    def rob(self, nums: List[int]) -> int:
        

        # cannot rob two adjacent houses

        # two choices: rob dp[i - 2] or nums[i] can be robbed or continue using dp[i - 1]
        n = len(nums)
        if n == 1:
            return nums[0]
        dp = [0 for _ in range(n)]
        rob1 = nums[0]
        rob2 = max(rob1, nums[1])
        for i in range(2, len(nums)):
            rob2, rob1 = max(rob1 + nums[i], rob2), rob2
        return rob2