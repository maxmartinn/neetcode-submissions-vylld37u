class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res = []
        def backtrack(i, total, curr):
            if total == target:
                res.append(curr[:])
                return
            if total > target or i == len(candidates):
                return
            for j in range(i, len(candidates)):
                if j > i and candidates[j] == candidates[j - 1]:
                    continue
                curr.append(candidates[j])
                backtrack(j + 1, total + candidates[j], curr)
                curr.pop()

        backtrack(0, 0, [])
        return res