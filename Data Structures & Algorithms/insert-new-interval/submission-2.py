class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        # start at first interval
        res = []
        for start, end in intervals:
            if newInterval[0] > end:
                res.append([start, end])
            elif newInterval[1] < start:
                res.append(newInterval)
                newInterval = [start, end]
            else:
                newInterval = [min(newInterval[0], start), max(end, newInterval[1])] 
          
        res.append(newInterval)
        return res