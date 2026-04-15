"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        startList = [i.start for i in intervals]
        endList = [i.end for i in intervals]

        startList.sort()
        endList.sort()

        """
        s = [0 5 15]
                      i
        e = [10 20 40]
                i
        """
        s = 0
        e = 0
        res = 0

        while s != len(startList):
            if startList[s] < endList[e]:
                s += 1
            else:
                e += 1
            res = max(res, s - e)
        return res