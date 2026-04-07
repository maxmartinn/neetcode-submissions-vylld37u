class Solution:
    def trap(self, height: List[int]) -> int:
        # have two pointers one from the left and one at the end
        # hold the maximum wall to the left and the maximum wall to the right
        # add the value of the current pointers height and subtract by the minimum of the maximum of left and right wall
        # move the pointer with the smaller wall
        l = 0
        r = len(height) - 1
        maxLeft = 0
        maxRight = 0
        res = 0
        while l <= r:
            if maxLeft <= maxRight:
                res = max(res, res + min(maxLeft, maxRight) - height[l])
                maxLeft = max(maxLeft, height[l])
                l += 1
            else:
                res = max(res, res + min(maxLeft, maxRight) - height[r])
                maxRight = max(maxRight, height[r])
                r -= 1
            print(res, maxLeft, maxRight)
        return res