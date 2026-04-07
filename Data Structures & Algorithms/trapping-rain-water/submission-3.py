class Solution:
    def trap(self, height: List[int]) -> int:
        # [0,2, 0, 0, 1]
        #.         lr
        # output = 2
        # lMax = 2
        # rMax = 1
        # area = 2
        
        area = 0
        l = 0 
        r = len(height) - 1
        lMax = 0
        rMax = 0
        while l <= r:
            if lMax <= rMax:
                height_diff = min(rMax, lMax) - height[l]
                area += max(0, height_diff)
                lMax = max(lMax, height[l])
                l += 1
            else:
                height_diff = min(rMax, lMax) - height[r]
                area += max(0, height_diff)
                rMax = max(rMax, height[r])
                r -= 1
        return area
        """
        clarification

        given an array of integers repersenting an elevation map

        the goal is to calculate hte maximum area of water that can be trapped between the bars
        

        example

        given an array of [1, 0, 1]

        1 water cell can be trapped in between indexes 0 and 2

        given an array of [2 0 0 2]

        4 water cells can be trapped in between indexes 0 and 3

        # brute force

        # for each bar the goal is to calcuate the amount of water that can be trapped between the bars

        # at each bar find the tallest bar from the left and right the right

        # once the tallest bar from the left and right are found, calculate the minimum of these two values and subtract current height

        # add amount of trapped water to the result if the amount of trapped water is greater than 0

        # optmize - there is repeated work when iterating from the left and right to find the tallest bar

        # plan:

        # set the area as 0
        # set the l highest and r highest as 0
        # iterate while l is less than r
        # move the left to the right if l is smaller or equal to r
        # move the right to the left if l is smaller or equal r
        # when moving a value, first add the value - height[moved_index] to the res if positve

        #. l  <-- i --> r
        #      [0 5 0 6]
        """
