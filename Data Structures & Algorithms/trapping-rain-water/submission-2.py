class Solution:
    def trap(self, height: List[int]) -> int:
        # have two pointers l and r stating from start and end

        # iterate through the height list adding the different between min(L, R) and height

        l = 0
        r = len(height) - 1
        leftMax = 0
        rightMax = 0
        res = 0

        while l <= r:
            if leftMax <= rightMax:
                res += max(0, min(leftMax, rightMax) - height[l])
                leftMax = max(height[l], leftMax)
                l += 1
            else:
                res += max(0, min(leftMax, rightMax) - height[r])
                rightMax = max(height[r], rightMax)
                r -= 1


        return res

