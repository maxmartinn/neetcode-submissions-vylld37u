class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        n = len(nums)
        stk = []
        def dfs(i):
            if i == n:
                res.append(stk.copy())
                return
            stk.append(nums[i])
            dfs(i + 1)
            stk.pop()
            dfs(i + 1)

        dfs(0)
        return res
            