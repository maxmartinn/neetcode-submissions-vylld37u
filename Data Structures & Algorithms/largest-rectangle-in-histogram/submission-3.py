class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        # keep a stack of indexes and heights
        # keep the stack monoincreasing
        # if there is a height that is less than the top of the stack
        # pop stack untill that isnt true
        
        stk = [] # (index, height)
        maxArea = -1
        for index, height in enumerate(heights):
            start = index
            while stk and height < stk[-1][1]:
                poppedIndex, poppedHeight = stk.pop()
                maxArea = max(maxArea, poppedHeight * (index - poppedIndex))
                start = poppedIndex
            stk.append((start, height))
        for index, height in stk:
            maxArea = max(maxArea, height * (len(heights) - index))

        return maxArea

