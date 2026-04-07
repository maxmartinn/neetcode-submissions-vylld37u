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
        meetings = []
        for i in intervals:
            meetings.append(("start", i.start))
            meetings.append(("end", i.end))
        meetings.sort(key=lambda i : (i[1], i[0] == "start"))
        count = 0
        print(meetings)
        for event in meetings:
            if count >= 2:
                return False
            if event[0] == "start":
                count += 1
            if event[0] == "end":
                count -= 1
        return True
        