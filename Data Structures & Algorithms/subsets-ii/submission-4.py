class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = [] # [[] [1] [1 1] [1 1 2] [1 2] [2]]
        # [1, 1, 2]
        def backtrack(i, curr):
            res.append(curr[:])
            for j in range(i, len(nums)):
                if j > i and nums[j] == nums[j - 1]:
                    continue
                curr.append(nums[j])
                backtrack(j + 1, curr)
                curr.pop()
        backtrack(0, [])
        return res