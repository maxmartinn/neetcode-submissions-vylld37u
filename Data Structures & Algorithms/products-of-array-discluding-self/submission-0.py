class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # keep an array of the prefix product
        # keep an array of the postfix product
        prefix = 1
        postfix = 1
        prefixArr = [1] * len(nums)
        postfixArr = [1] * len(nums)
        res = [1] * len(nums)

        # iterate through array and multiple the current index by the prefix/postfix
        # [1, 1, 2, 8]
        # [48, 24, 6, 1]

        for i in range(len(nums)):
            prefixArr[i] *= prefix
            prefix *= nums[i]

        for i in range(len(nums) - 1, -1, -1):
            postfixArr[i] *= postfix
            postfix *= nums[i]

        print(postfixArr)
        print(prefixArr)

        for i in range(len(nums)):
            res[i] = postfixArr[i] * prefixArr[i]
        return res
            