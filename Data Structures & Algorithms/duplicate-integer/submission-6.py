class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        """

        nums = List[int]

        naive approach:

        iterate the list starting at each index:
            iterate again from that index + 1 to check if the two indices match


        """


        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] == nums[j]:
                    return True
        return False
