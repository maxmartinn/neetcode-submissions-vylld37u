class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        # if newInterval start date is before current Interval end date, interval needs to be merged

        """
        Input: intervals = [[1,2],[4,8], [10, 12], [45, 50]], newInterval = [2,5]

        Output: [[1,10]]

        curr = [1, 6]

        """
        res = []
        i = 0
        while i != len(intervals) and newInterval[0] > intervals[i][1]:
            res.append(intervals[i])
            i += 1
        while i != len(intervals) and newInterval[1] >= intervals[i][0]:
            newInterval[0] = min(intervals[i][0], newInterval[0])
            newInterval[1] = max(intervals[i][1], newInterval[1])
            i += 1
        res.append(newInterval)
        while i != len(intervals):
            res.append(intervals[i])
            i += 1
        return res