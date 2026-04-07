class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        n = len(nums)
        res = nums[0]
        for i in range(n):
            for j in range(i, n):
                count = 0
                for k in range(i, j + 1):
                    count += nums[k]
                res = max(count, res)
        return res