class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        # start at first interval
        res = []
        for start, end in intervals:
            newIntStart, newIntEnd = newInterval
            if newIntStart > end:
                res.append([start, end])
            elif newIntEnd < start:
                res.append(newInterval)
                newInterval = [start, end]
            else:
                newInterval = [min(newIntStart, start), max(newIntEnd, end)] 
          
        res.append(newInterval)
        return res