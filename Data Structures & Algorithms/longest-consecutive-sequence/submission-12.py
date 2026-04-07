class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set()


        for n in nums:
            numSet.add(n)

        
        res = 0

        for n in nums:
            if not n - 1 in numSet:
                streak = 0
                while n + streak in numSet:
                    streak += 1
                res = max(res, streak)

        return res



