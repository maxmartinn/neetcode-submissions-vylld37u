class Solution:
    def search(self, nums: List[int], target: int) -> int:
        """
        case 1: target is on left side and m is on right side (go left)
        case 2: target is on left side and m is on left side (pass)
        case 3: target is on left side and m is on riight side (go right)
        case 4: target is on right side and m is on right side (pass)

        now that i know the current value is on the right side. now i need to determine which direction to go just as a regulare binary search
        """
        

        l = 0
        r = len(nums) - 1

        while l <= r:
            m = (l + r) // 2

            if target == nums[m]:
                return m

            if target >= nums[0]: # target is on left side # m must be on left side
                if nums[m] < nums[0] or nums[m] > target:
                    r = m - 1
                else:
                    l = m + 1
            else: # target is on right side # m must be on right side
                if nums[m] >= nums[0] or nums[m] < target:
                    l = m + 1
                else:
                    r = m - 1
        return -1
