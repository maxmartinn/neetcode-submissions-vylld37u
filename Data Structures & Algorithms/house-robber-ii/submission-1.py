class Solution:
    def rob(self, nums: List[int]) -> int:
        # [rob1, rob2, n]
        
        def robHouses(nums):
            rob1 = 0
            rob2 = 0
            for n in nums:
                curr = max(rob1 + n, rob2)
                rob1 = rob2
                rob2 = curr
            return rob2
        return max(nums[0],robHouses(nums[1:]), robHouses(nums[:-1]))