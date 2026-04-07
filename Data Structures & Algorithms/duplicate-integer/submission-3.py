class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
         # using a hashset we can look up if an element exists in the data structure in O(1) time

         # while iterating through the nums array it is possible to check if the current number is in the set and then add it to the set if it isnt


         # if at any moment the current number is in the set it is possible to return true

         # return false at the end of iterations

        numSet = set()

        for n in nums:
            if n in numSet:
                return True
            numSet.add(n)
        return False