class Solution:
    def findMin(self, nums: List[int]) -> int:

        # [3, 4, 5, 1, 2]
        # l.    m.     r
        res = nums[0]
        l = 0
        r = len(nums) - 1
        # if left is smaller or equal to middle
        # 
        while l <= r:
            m = (l + r) // 2
            if nums[l] < nums[r]:
                res = min(res, nums[l])
                break
            res = min(res, nums[m])
            if nums[l] <= nums[m]:
                l = m + 1
            else:
                r = m - 1
        return res

            