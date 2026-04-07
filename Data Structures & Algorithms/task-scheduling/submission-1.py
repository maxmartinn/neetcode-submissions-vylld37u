import heapq
from collections import deque
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = Counter(tasks)
        maxHeap = [-cnt for cnt in count.values()]
        heapq.heapify(maxHeap)
        q = deque() # pair of values (-occurence, avalaibleTime)
        time = 0
        while maxHeap or q:
            time += 1
            if maxHeap:
                op = 1 + heapq.heappop(maxHeap)
                if op:
                    q.append([op, time + n])
            if q and q[0][1] == time:
                heapq.heappush(maxHeap, q.popleft()[0])
        return time