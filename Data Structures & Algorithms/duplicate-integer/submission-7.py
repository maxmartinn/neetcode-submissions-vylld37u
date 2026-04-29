class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        """

        nums = List[int]

        naive approach:

        iterate the list starting at each index:
            iterate again from that index + 1 to check if the two indices match

        Time Complexity = O(n^2)
        Space Complexity = O(1)

        Time Complexity = O(N)
        Space Complexity = O(N)

        set

        using a set:

        iterate through nums checking the current number is in the set:

        add number to set

        """

        numSet = set()

        for n in nums:
            if n in numSet:
                return True
            numSet.add(n)
        return False