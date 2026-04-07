class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        

        # have a numSet

        # precompute by adding all values to the numSet

        
        # iterate through all numbers in numSet

        # if the number - 1 doesnt exists iterate the number untill it doesnt exist


        # return the longest res

        numSet = set()
        res = 0

        for n in nums:
            numSet.add(n)
        for n in nums:
            streak = 0
            if n - 1 not in numSet:
                while n + streak in numSet:
                    streak += 1
            res = max(streak, res)
        return res




