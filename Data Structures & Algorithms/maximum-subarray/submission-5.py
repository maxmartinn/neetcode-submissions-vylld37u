class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # iterate through nums and keep a running count
        # make res the max of running count and res
        # make running count max of 0, and count
        # return res
        res = nums[0] # 4
        count = nums[0] # 
        for n in nums[1:]:
            count += n
            count = max(count, n)
            res = max(res, count, n)
            print(count)
        return res