class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        # naive solution

        # create a combination of all subarrays and multiply minimum height be length of the array
        

        # the stk repersents the farthest that the current rectangle can extend to

        # while iterating add current height and the index that the rectangle can extend to

        # the rectangle can extend if the height is less than the value to its right

        # for example in Input: heights = [7,1,7,2,2,4]

        # at index 4 the 2 can extend from 7 to 4

        """ 
        by creating a strictly increasing array, iterate through heights adding to the stk 
        stk = [] (start_extension_index, value)

        the start_extension_index is when popping the value. it is value of the most recently popped index

        Input: heights = [7,1,7,2,2,4]

        Output: 8
        res = 7
        stk = [(0, 1), (2, 2), (5, 4)]

        now check the stack seeing if a new result is found
                        height       <-------width --------->
        res = max(res,  stk[i][1] * (len(heights) - stk[i][0]))
        """ 

        
        """

        stk = []

        """




        stk = [] # (index, height)
        res = 0
        for i, h in enumerate(heights):
            start = i
            while stk and h <= stk[-1][1]:
                start, prev_h = stk.pop()
                res = max(res, (i - start) * prev_h)
            stk.append((start, h))
        
        for i, h in stk:
            res = max(res, (len(heights) - i) * h)

        return res

        """

        Input: heights = [7,1,7,2,2,4]
                                    i
        Output: 8

        res = 8
        start = 5
            prev_h = 2
        stk = [(0, 1), (2, 2), (5, 4)]



        """ 


