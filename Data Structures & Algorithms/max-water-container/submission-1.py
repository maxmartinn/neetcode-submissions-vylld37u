class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # we need to bars to create the largest container
        # given two bars
        #   area = distance between * minimum height
        
        # one way to solve this
        #   we consider all pairs of boxes and calculate max area

        maxArea = 0
        for i in range(len(heights)):
            for j in range(i + 1, len(heights)):
                height = min(heights[i], heights[j])
                maxArea = max(maxArea, height * (j - i))
        return maxArea