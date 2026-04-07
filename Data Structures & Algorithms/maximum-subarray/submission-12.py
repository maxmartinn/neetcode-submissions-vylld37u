class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        res = nums[0]
        count = 0
        for n in nums:
                if count < 0:
                    count = 0
                count += n
                res = max(count, res)
        return res