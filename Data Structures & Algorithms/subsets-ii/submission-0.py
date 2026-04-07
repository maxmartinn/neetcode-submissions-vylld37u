class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        inRes = set()
        # have a solution that either includes or doesn't include current index
        res = []
        def dfs(i, curr):
            # check if i is in bounds
            if i == len(nums):
                if tuple(curr) not in inRes:
                    res.append(curr[:])
                    inRes.add(tuple(curr))
                return
            curr.append(nums[i])
            dfs(i + 1, curr)
            curr.pop()
            dfs(i + 1,curr)
        dfs(0, [])
        return res
