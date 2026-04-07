class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def dfs(nums):
            res = []
            if len(nums) == 1:
                return [nums[:]]
            
            for i in range(len(nums)):
                n = nums.pop(0)
                perms = dfs(nums)

                for perm in perms:
                    perm.append(n)
                res.extend(perms)
                nums.append(n)
            return res
        return dfs(nums)