class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        minHeap = [(x1**2 + y1**2, (x1, y1)) for x1, y1 in points]
        heapq.heapify(minHeap)
        return [heapq.heappop(minHeap)[1] for _ in range(k)]