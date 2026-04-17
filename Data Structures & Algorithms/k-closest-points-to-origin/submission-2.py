class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        minHeap = []
        res = []
        for x1, y1 in points:
            heapq.heappush(minHeap, (x1**2 + y1**2, (x1, y1)))
        
        for _ in range(k):
            res.append(heapq.heappop(minHeap)[1])
        return res