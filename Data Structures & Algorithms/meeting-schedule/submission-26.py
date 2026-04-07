"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        # 0     5
        #       5   10
        #                   15      20 
        
        # start from interval 1 to end of interval list
        # check if the the end of interval 1 starts after the end of interval 2
        start = []
        end = []
        for i in intervals:
            start.append(i.start)
            end.append(i.end)
        start.sort()
        end.sort()
        p1 = 0
        p2 = 0
        while p1 < len(intervals) and p2 < len(intervals):
            if p1 - p2 >= 2:
                return False
            if start[p1] < end[p2]:
                p1 += 1
            else:
                p2 += 1
        return p1 - p2 < 2
            
        