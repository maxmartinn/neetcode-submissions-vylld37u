class Solution:
    def findMin(self, nums: List[int]) -> int:
        # two arrays 
        # left side [3, 4, 5, 6]
        # right side [1, 2]

        # goal is to find the start of the right side array and to exit the loop with the minimum

        # patterns if current index is greater than start of array, go right is current index is smaller than start of array go left
        l = 0
        r = len(nums) - 1
        res = nums[0]

        while l <= r:
            m = (l + r) // 2
            res = min(res , nums[m])
            if nums[m] >= nums[0]:
                l = m + 1
            else:
                r = m - 1
        return res

