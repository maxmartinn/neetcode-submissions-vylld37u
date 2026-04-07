class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        def backtrack(i, cnt, curr):
            if cnt == target:
                res.append(curr[:])
                return
            if cnt > target or i == len(nums):
                return
            curr.append(nums[i])
            backtrack(i, cnt + nums[i], curr)
            curr.pop()
            backtrack(i + 1, cnt, curr)
        backtrack(0, 0, [])
        return res
            