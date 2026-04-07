class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
         # O(n) space and time solution uses a counter checks over two
        numSet = set()
        for n in nums:
            if n in numSet:
                return True
            numSet.add(n)
        return False