class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # make a map of all tasks and frequencies

        # loop untill tasks is empty

        # use a min heap for when a task is completed, if tasks remaining greater than 0 add to heap the next time it is available

        # if a value is reached and the top of the heap is not ready yet, set time to that current value in heap and continue
        time = 0
        count = Counter(tasks)
        maxHeap = [-c for c in count.values()]
        heapq.heapify(maxHeap)

        q = deque() # (-c, availableTime)

        while q or maxHeap:
            time += 1

            if maxHeap:
                cnt = heapq.heappop(maxHeap) + 1
                if cnt:
                    q.append((cnt, time + n))
            
            if q and q[0][1] == time:
                heapq.heappush(maxHeap, (q.popleft()[0]))

        return time