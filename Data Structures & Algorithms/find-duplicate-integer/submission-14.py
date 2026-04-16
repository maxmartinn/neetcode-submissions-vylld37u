class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        """
        given nums array
            nums=[1,2,3,4,4]

        using current number as an index, if that current number index is marked than the current number is the duplicate, 


        """

        for i in range(len(nums)):
            idx = abs(nums[i]) - 1
            if nums[idx] < 0:
                return abs(nums[i])
            nums[idx] *= -1
        return -1