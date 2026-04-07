class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        # clarification

        # return a list of numbers where each index consists of the value of multiple all numbers except for the original index value

        # [1, 2, 3]
        # [6, 3, 2]

        # brute force

        # iterate all numbers
        #   and the current values and skip the current index in the multiplication process
        # time complexity O(n^2)
        # space complexity O(n)
        # optimal

        # [1, 2, 3]

        # possible to get multiplication simply by skipping current value, prefix and postfix

        """

        simply by multiplying prefix and postfix values results in the index being correct

        iterating forward obtaining a prefix and multiplying the current index
        iterating backwards obtaining a post and multiplying the current index

        # nums = [2, 4, 3]

        # res = [12, 6, 8]
        # prefix = 24
        # postfix = 24
        """

        res = [1 for _ in nums]

        prefix = 1
        for i in range(len(nums)):
            res[i] *= prefix
            prefix *= nums[i]
    
        postfix = 1
        for i in range(len(nums) - 1, -1, -1):
            res[i] *= postfix
            postfix *= nums[i]
        
        return res