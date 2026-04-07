class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # have a pointer at the start and pointer at the end
        # get the width of the rectangle
        l = 0
        r = len(heights) - 1
        res = 0
        while l < r:
            width = r - l
            height = min(heights[r], heights[l])
            area = width * height
            res = max(area, res)
            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1
        return res