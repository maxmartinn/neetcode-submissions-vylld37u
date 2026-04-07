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
        print(numSet)
        for n in nums:
            count = 0
            if n - 1 not in numSet:
                n += 1
                while n - 1 in numSet:
                    count += 1
                    n += 1
            print(n)
            res = max(count, res)
        return res




