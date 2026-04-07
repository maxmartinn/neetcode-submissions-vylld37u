"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        # 0                           30
        #       5.  10
        #               15   20

        if not intervals:
            return True

        intervals.sort(key = lambda i: i.start)
        base = intervals[0]
        for i in range(1, len(intervals)):
            interval = intervals[i]

            if base.end > interval.start:
                return False
            base = interval
        return True  

