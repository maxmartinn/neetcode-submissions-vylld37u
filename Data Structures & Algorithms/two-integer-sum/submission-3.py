class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # return indexes of two valid combinations to equal the target sum

        # store previous index value pairs in a hashmap

        # iterate through each number checking if the compliment (target - nums[i]) exists in the hashmap

        # if the compliment exists return [compliment index, currennt index]

        numMap = dict()

        for index in range(len(nums)):
            compliment = target - nums[index]
            if compliment in numMap:
                return [numMap[compliment], index]
            numMap[nums[index]] = index
        return [-1, -1]

        # inputs

        # nums = [3, 4, 5, 6]
        # target = 7

        # vars:

        # numMap = {3: 0}
        # index = 1
        # compliment = 3
        
