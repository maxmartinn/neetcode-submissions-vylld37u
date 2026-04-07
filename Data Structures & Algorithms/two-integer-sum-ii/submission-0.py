class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # restate:

        # given a list of sorted numbers and a target number

        # find a combination of two integers that add up to the target number

        # brute force:
        
        # iterate for each number in numbers:
            # using current nubmer check if adding another number in numbers would add up to target.
            # if a pair is found return both indexes

        # optimization of this: use a hashmap to check if another number exists to add up to target

        # O(1) space optimization
            # because numbers list is sorted two pointers can be used to find target

        # plan:

        # have a pointer starting at end of list and start of list

            # if the sum of both pointers is greater than target reduce right pointer by one

            # if the sum of both pointers is less than target increase left pointer by one

            # if the sum of both pointers eqauls target than return left and right pointer positions

        # dry run

        # [1, 2, 4] target = 3

        # l = 0 : 1
        # r = 1 : 2

        # target = 3 

        # code

        l = 0
        r = len(numbers) - 1
        
        while l < r:
            if numbers[l] + numbers[r] == target:
                return [l + 1, r + 1]
            if numbers[l] + numbers[r] > target:
                r -= 1
            if numbers[l] + numbers[r] < target:
                l += 1
        return
        # [1, 2, 4] target = 3

        # l = 0 : 1
        # r = 1 : 2



