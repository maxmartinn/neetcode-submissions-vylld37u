class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # [3, 4, 5, 6, 1, 2] # target = 1
        #. L.    M.        R
        # check if on left or right
        # check if m equals target
        # if L < M then on left sorted array
        #.  if l > target or m < target:
        #       search right
        #   else:
        #         search left
        # else L >= M then on right sorted array
        #.  if r < target or m > target:
        #       search left
        #   else:
        #         search right
        l = 0
        r = len(nums) - 1
        while l <= r:
            m = (l + r) // 2
            if nums[m] == target:
                return m
            if nums[l] <= nums[m]:
                if nums[l] > target or nums[m] < target:
                    l = m + 1
                else:
                    r = m - 1
            else:
                if nums[r] < target or nums[m] > target:
                    r = m - 1
                else:
                    l = m + 1
        return -1