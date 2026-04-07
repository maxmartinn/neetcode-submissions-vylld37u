class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # [3, 4, 5, 6, 1, 2] # target = 6
        # L.     M.       R

        l = 0
        r = len(nums) - 1
        while l <= r:
            m = (l + r) // 2
            if nums[m] == target:
                return m
            if nums[l] <= nums[m]:
                if nums[m] < target or nums[l] > target:
                    l = m + 1
                else:
                    r = m - 1
            else:
                if nums[r] < target or nums[m] > target:
                    r = m - 1
                else:
                    l = m + 1

        return -1