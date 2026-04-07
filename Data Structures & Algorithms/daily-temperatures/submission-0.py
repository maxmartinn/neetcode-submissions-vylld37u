class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # monotomic decreasing stk
        # solve for the temperature at the top of the stk
        # [40, 28]

        # while the current tmp is greater than the top of the stk
        # pop the top of the stk and get the dinstance between the two days

        res = [0] * len(temperatures)

        stk = [] # (index, temp)
        index = 0
        while index < len(temperatures):
            while stk and stk[-1][1] < temperatures[index]: 
                popped = stk.pop()
                res[popped[0]] = index - popped[0]
            # check if stk or temp is smaller than top of stk
            if index < len(temperatures):
                stk.append((index, temperatures[index]))
            index += 1

        return res
