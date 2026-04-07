class Solution:
    def findMin(self, nums: List[int]) -> int:
        # if left is smaller than right
        # go move right to the left

        l = 0
        r = len(nums) - 1
        curr_min = float("inf")
        while l <= r:
            m = (l + r) // 2
            curr_min = min(curr_min, nums[m])
            if nums[m] <= nums[r]:
                r = m - 1
            else:
                l = m + 1
        return curr_min


            