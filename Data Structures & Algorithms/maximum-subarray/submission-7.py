class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        n = len(nums)
        # [2, -3, 4, -2]
        
        

        res = nums[0]
        for i in range(n):
            count = 0
            for j in range(i, n):
                count += nums[j]
                res = max(count, res)
        return res