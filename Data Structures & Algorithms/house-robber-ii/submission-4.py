class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        def house_rob(houses):
            rob1, rob2 = 0, 0
            for n in houses:
                rob1, rob2 = rob2, max(rob2, rob1 + n)
            return rob2
        """

        
        # nums[:-1] = [2,3]
        rob1 = 2
        rob2 = 3
        # nums[1:] = [3,4]
        rob1 = 3
        rob2 = 4
        """
        return max(house_rob(nums[1:]), house_rob(nums[:-1]))