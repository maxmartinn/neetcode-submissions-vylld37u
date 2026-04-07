class Solution:
    def rob(self, nums: List[int]) -> int:
        rob1Away = 0
        rob2Away = 0
        for n in nums:
            curr = max(n + rob1Away, rob2Away)
            rob1Away = rob2Away
            rob2Away = curr
        return rob2Away

