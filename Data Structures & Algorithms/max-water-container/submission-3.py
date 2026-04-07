class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # given an integer array heights, heights[i] respersent the height of the ith bar

        # choose any bars to form a container and return the maximum amount of water

        # brute force:

        # calculate the width of all boxes iterate for each pair of boxes and calculate area between boxes

        # optimization:

        # instead of using each pair, start from the left and right pairs and shift the smaller box to calculate the next area

        # return the highest area found

        # plan

        # initalize two pointers: left and right

        # iterate untill left and right equal each other

        # calculate area by finding the minimum height of both boxes, and get the width by subtracting right and left

        # shift the index with the smallest box


        l = 0
        r = len(heights) - 1
        res = 0
        while l < r:
            height = min(heights[l], heights[r])
            area = height * (r - l)
            res = max(area, res)
            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1
        return res
        """
        Input: height = [1, 2, 3]
                            l  r
        l = 1
        r = 2
        height = 2
        area = 2
        res = 2
        Output: 2
        """