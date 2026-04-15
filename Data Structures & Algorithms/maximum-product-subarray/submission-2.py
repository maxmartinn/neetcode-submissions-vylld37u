class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        val1 = nums[0]
        val2 = nums[0]

        res = val1

        for n in nums[1:]:
            val1, val2 = min(val1 * n, val2 * n, n), max(val1 * n, val2 * n, n)
            res = max(val1, val2, res)
        return res