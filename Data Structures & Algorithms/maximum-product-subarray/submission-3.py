class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        curMin = curMax = res = nums[0]

        for n in nums[1:]:
            curMin, curMax = min(curMin * n, curMax * n, n), max(curMin * n, curMax * n, n)
            res = max(curMax, res)
        return res