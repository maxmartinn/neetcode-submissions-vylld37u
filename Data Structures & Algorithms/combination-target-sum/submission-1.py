class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        n = len(nums)
        stk = []
        def dfs(i, total):
            if i == n:
                if total == target:
                    res.append(stk.copy())
                return
            if total > target:
                return
            stk.append(nums[i])
            dfs(i, total + nums[i])
            stk.pop()
            dfs(i + 1, total)
        dfs(0,0)
        return res