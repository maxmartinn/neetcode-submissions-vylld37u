class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        meetingTimes = []
        
        # Add all start and end times to meetingTimes
        for interval in intervals:
            meetingTimes.append(("start", interval.start))
            meetingTimes.append(("end", interval.end))
        
        # Sort the times by time value first, and by type ("end" before "start" in case of a tie)
        meetingTimes.sort(key=lambda i: (i[1], i[0] == "start"))
        
        count = 0
        maxOverlap = 0
        
        # Traverse the sorted times and calculate overlaps
        for event in meetingTimes:
            if event[0] == "start":
                count += 1  # A meeting starts, increase the overlap count
                maxOverlap = max(maxOverlap, count)  # Track maximum overlap
            else:
                count -= 1  # A meeting ends, decrease the overlap count
        
        return maxOverlap
        