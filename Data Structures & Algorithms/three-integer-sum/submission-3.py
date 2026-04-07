class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # clarification

        # given an integer array called nums, return all triplets where nums[i] + nums[j] + nums[k] == 0

        # -nums[i] == nums[j]  + nums[k]

        # brute force

        # select i and then search for all pairs of j and k that add up to - nums[i]

        # using sorting iterate all starting values of and then using two pointers to select the k value and j value

        # optimize

        # should not contain duplicate triplets, skip untill i is new

        # select -nums[i], using two pointers select the j and k value.

        # if at any point j and k meet, continue to next i
        
        res = []
        nums.sort()
        for i in range(len(nums)): 
            if i != 0 and nums[i - 1] == nums[i]:
                continue
            j = i + 1
            k = len(nums) - 1
            target = -nums[i]
            while j < k:
                if nums[j] + nums[k] < target:
                    j += 1
                elif nums[j] + nums[k] > target:
                    k -= 1
                elif nums[j] + nums[k] == target:
                    res.append([nums[i], nums[j], nums[k]])
                    j += 1
                    while j < k and nums[j - 1] == nums[j]:
                        j += 1
                print(nums[i], nums[j], nums[k])
        return res

        """

        Input: nums = [0, 0, 0, 0]

        Output: [[0, 0, 0]]

        nums = [0, 0, 0, 0]
i     j  k 
        
        res = []

        """