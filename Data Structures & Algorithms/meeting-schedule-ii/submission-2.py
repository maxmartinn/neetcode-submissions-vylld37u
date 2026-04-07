"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        hashmap = defaultdict(list)
        # sort the interval list
        # find where the current interval can:
        # this can be done by checking the start of current interval
        # and check with the end of the last interval at the current day
        # [(0, 40), (5, 10), (15, 20)]
        intervals = sorted(intervals, key=lambda x: x.start)
        for index in range(len(intervals)):
            maxDays = len(hashmap) + 1
            for day in range(maxDays):
                if hashmap[day] and intervals[index].start >= hashmap[day][-1].end:
                    hashmap[day].append(intervals[index])
                    break
                elif not hashmap[day]:
                    hashmap[day].append(intervals[index])
                    break
        return len(hashmap)


