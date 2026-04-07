"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        start = []
        end = []
        for i in intervals:
            start.append(i.start)
            end.append(i.end)
        start.sort()
        end.sort()
        p1 = 0
        p2 = 0
        count = 0
        while p1 < len(intervals) and p2 < len(intervals):
            if start[p1] < end[p2]:
                p1 += 1
            else:
                p2 += 1
            count = max(count, p1 - p2)
        return count
            

        