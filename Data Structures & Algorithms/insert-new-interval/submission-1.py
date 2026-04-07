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
        for start, end in intervals:
            if base[0] > end:
                res.append([start, end])
            elif base[1] < start:
                res.append(base)
                base = [start, end]
            else:
                base = [min(base[0], start), max(end, base[1])] 
          
        res.append(base)
        return res