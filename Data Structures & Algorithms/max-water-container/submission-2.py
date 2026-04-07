class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # we need to bars to create the largest container
        # given two bars
        #   area = distance between * minimum height
        
        # one way to solve this
        #   we consider all pairs of boxes and calculate max area

        # maxArea = 0
        # for i in range(len(heights)):
        #     for j in range(i + 1, len(heights)):
        #         height = min(heights[i], heights[j])
        #         maxArea = max(maxArea, height * (j - i))
        # return maxArea

        # optimized

        # we can optimize this area by using two pointers
        # and we can first calculate current area
        #   then we move smallest height respectivly

        maxArea = 0
        l = 0
        r = len(heights) - 1
        while l < r:
            height = min(heights[l], heights[r])
            maxArea = max(maxArea, height * (r - l))
            if heights[l] <= heights[r]:
                l += 1
            else:
                r -= 1
        return maxArea

