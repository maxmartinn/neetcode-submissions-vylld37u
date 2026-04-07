class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # result i repersents the list of days until a warmer temperature is found

        # [30 38 30, 40]
        # [1 2, 1, 0]
        # stk = [(3, 40)]
        # keep popping from stack while current temp is larger than top of stk
            # when pop at the popped index add the value of current index - popped index
        # add to index and temp to top of stk  


        result = [0] * len(temperatures)

        stk = []

        for curr_index, curr_temp in enumerate(temperatures):
            while stk and stk[-1][1] < curr_temp:
                prev_index = stk.pop()[0]
                result[prev_index] = curr_index - prev_index
            stk.append((curr_index, curr_temp))
        return result
        
        # [51, 38, 30, 40]
        # stk = [(0, 51), (4, 40)]
        # result = [0, 1, 2]
        # prev_index = 1