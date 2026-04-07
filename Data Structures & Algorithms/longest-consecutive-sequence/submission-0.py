class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # 2 3 4 5, 10, 20
        numSet = set(nums)
        res = 0
        runningCount = 0
        for n in nums:
            if n - 1 in numSet:
                pass
            else:
                while n in numSet:
                    runningCount += 1
                    n += 1
                res = max(runningCount, res)
                runningCount = 0
        return res

