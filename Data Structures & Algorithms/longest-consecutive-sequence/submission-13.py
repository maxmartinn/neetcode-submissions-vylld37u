class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # restate

        # given an array of integers, return the length of the longest consecutive sequence

        # numbers can be in any order to form the longest consecutive sequence

        # brute force

        # for each number in nums:
            # define the next number in the consecutive sequence
            # loop untill this number no longer exists in the nums array
                # update next number if the current search is found
            # update res to be largest number in sequence - current number + 1
        # return res

        # optmized 

        # instead of searching everytime, a search is only needed if the current number - 1 does not exist in the sequence
            # only start the search if at the start of the sequnce

        # plan

        # define a set to store all numbers in the nums array

        # iterate for each number in nums and check if the current number is the start of a consecutive sequence
        # loop untill the consecutive sequence can no longer be formed with the current number as the start 

        # subtract largest number in sequence minus current number in sequence + 1


        num_set = set(nums)
        res = 0

        for n in nums:
            if n - 1 in num_set:
                continue
            search_value = n + 1
            while search_value in num_set:
                search_value += 1
            print(search_value)
            res = max(res, search_value - n)
        
        return res

        """
        Input: nums = [2,20,4,10,3,4,5]

        Output: 4

        num_set = {2,20,4,10,3,4,5}
        
        res = 4

        search_value = 21

        Time Complexity = O(n)

        Space Complexity = O(n)

        """