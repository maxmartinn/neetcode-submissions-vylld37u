"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        intervals = sorted(intervals, key=lambda x: x.start)
        # [(0, 30), (5, 10), (15, 20)]

        for index in range(1, len(intervals)):
            x1 = intervals[index - 1]
            x2 = intervals[index]
            if x1.end > x2.start:
                return False

        return True

            