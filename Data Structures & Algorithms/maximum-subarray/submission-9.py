class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        n = len(nums)
        # [2, -3, 4, -2]
        
        

        res = nums[0]
        count = 0
        for i in range(n):
                count = max(nums[i], count + nums[i])
                res = max(count, res)
        return res