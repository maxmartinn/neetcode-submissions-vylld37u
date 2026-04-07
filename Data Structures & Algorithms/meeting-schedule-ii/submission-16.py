"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        meetingRooms = []
        res = 0
        for interval in intervals:
            meetingRooms.append(("start", interval.start))
            meetingRooms.append(("end", interval.end))
        meetingRooms.sort(key=lambda i: (i[1], i[0] == "start"))
        count = 0
        for event in meetingRooms:
            if event[0] == "start":
                count += 1
            else:
                count -= 1
            res = max(count, res)
        return res

        # 0                         40
        #       5   10
        #               15  20

        