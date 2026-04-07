class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # [1, 2, 3, 2, 2]
        # [1, 1, 2, 3]
        #  0, 1, 2, 3, 4
        # slow = 1
        # 0 -> 2 -> 3 -> 2   
        slow = 0
        fast = 0
        for _ in nums: # detects cycle
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break

        slow2 = 0
        for _ in nums:
            slow = nums[slow]
            slow2 = nums[slow2]
            if slow == slow2:
                return slow
        return -1

