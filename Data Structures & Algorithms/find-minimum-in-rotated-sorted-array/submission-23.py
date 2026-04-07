class Solution:
    def findMin(self, nums: List[int]) -> int:
        # [3, 4, 5, 6, 1, 2]
        #  L.    M.       R

        # have a reccuring check if the res is smaller than current value
        # if the right is smaller than middle than 
        # search right
        # else
        # search left

        res = nums[0]
        l = 0
        r = len(nums) - 1
        while l <= r:
            m = (l + r) // 2
            res = min(res, nums[m])
            if nums[r] < nums[m]:
                l = m + 1
            else:
                r = m - 1
        return res

            