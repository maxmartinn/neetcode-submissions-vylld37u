class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        # start at first interval
        base = newInterval
        res = []
        # iterate through a
        # 1. 2
        #       3. 5
        #                       9   10
        #               6  7
        # if baseInterval starts after current interval ends and starts before current interval
            # merge
        for interval in intervals:
            if base[0] > interval[1]:
                res.append(interval)
            elif base[1] < interval[0]:
                res.append(base)
                base = interval
            else:
                base = [min(base[0], interval[0]), max(interval[1], base[1])] 
          
        res.append(base)
        return res