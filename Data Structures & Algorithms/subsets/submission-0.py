class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        def helper(i, running):
            if len(nums) <= i:
                res.append(running.copy())
                return
            helper(i+1, running.copy())
            running.append(nums[i])
            helper(i+1, running.copy())
        
        helper(0, [])
        return res