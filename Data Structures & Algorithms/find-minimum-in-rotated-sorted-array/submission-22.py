class Solution:
    def findMin(self, nums: List[int]) -> int:

        # [3, 4, 5, 1, 2]
        # l.     m.    r
        res = float("inf")
        l = 0
        r = len(nums) - 1
        # if left is smaller or equal to middle
        # 
        while l <= r:
            m = (l + r) // 2
            res = min(res, nums[m])
            if nums[r] >= nums[m]:
                r = m - 1
            else:
                l = m + 1
        return res

            