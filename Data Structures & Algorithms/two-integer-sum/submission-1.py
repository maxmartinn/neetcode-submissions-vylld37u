class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            complement = target - nums[i]
            for j in range(i+1, len(nums)):
                if complement == nums[j]:
                    return [i, j]
        return [0,0]