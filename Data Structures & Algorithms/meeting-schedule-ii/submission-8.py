"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        start = [i.start for i in intervals]
        end = [i.end for i in intervals]
        start.sort()
        end.sort()
        startIndex = 0
        endIndex = 0
        currRes, res = 0, 0
        while startIndex < len(start):
            if start[startIndex] < end[endIndex]:
                currRes += 1
                startIndex += 1
            else:
                endIndex += 1
                currRes -= 1
            res = max(currRes, res)

        return res


