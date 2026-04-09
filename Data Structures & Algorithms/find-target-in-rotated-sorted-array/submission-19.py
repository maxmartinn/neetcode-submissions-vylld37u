class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # all elements of the left side of the array is greater than nums[0]
        # all elements of the right side of the array is smaller than nums[0]

        # to search for a target need to first get to the correct side of the array
        # there are four differnece cases and that determines if it goes left or right. suppose to take a while and trip people up


        # case 1:
        # target is on left side and m is on left side and greater than target: move to right

        l = 0
        r = len(nums) - 1

        while l <= r:
            m = (l + r) // 2
            if target == nums[m]:
                return m

            if target >= nums[0]: # target is on left side
                if nums[m] < nums[0] or nums[m] > target: # m is on right side or m is larget than target
                        r = m - 1
                else:
                        l = m + 1
            else: # target is on right side
                if nums[m] >= nums[0] or nums[m] < target: # if m is on left side or m is smaller than target
                    l = m + 1
                else:
                    r = m - 1
                

        return -1