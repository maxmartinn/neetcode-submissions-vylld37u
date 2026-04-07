class Solution:
    def trap(self, height: List[int]) -> int:
        # have two pointers l and r stating from start and end
        # have 3 arrays contains the leftMax, rightMax and min(L, R)

        # iterate through the height list adding the different between min(L, R) and height

        l = 0
        r = len(height) - 1
        leftMax = [0 for _ in height]
        rightMax = [0 for _ in height]

        res = 0
        for i in range(1, len(height)):
            leftMax[i] = max(leftMax[i-1], height[i-1])
            rightMax[i] = max(rightMax[i - 1], height[len(height) - i])
        
        rightMax = rightMax[::-1]
        
        print(leftMax)
        print(rightMax)
        for i, h in enumerate(height):
            res += max(0, min(leftMax[i], rightMax[i]) - h)

        return res