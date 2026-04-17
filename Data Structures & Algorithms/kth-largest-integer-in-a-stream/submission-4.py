# 3 [5, 6, 7]
class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.minHeap = nums # minHeap should always be size k
        self.k = k
        heapq.heapify(self.minHeap)
        while len(self.minHeap) > self.k:
            heapq.heappop(self.minHeap)    

    def add(self, val: int) -> int:
        heapq.heappush(self.minHeap, val)
        if len(self.minHeap) > self.k:
            heapq.heappop(self.minHeap)         
        return self.minHeap[0]   
