# smallHeap = [-3 -1]
# largeHeap = [2]

# smallHeap is always equal or 1 greater than large heap

# smallHeap is a max heap
# largeHeap is a minHeap

# check if the max of small Heap is less than new number:
# input = [5, 1, 3, 4, 5]

#

class MedianFinder:

    def __init__(self):
        self.smallHeap = []
        self.largeHeap = []
    def addNum(self, num: int) -> None:
        smallHeap, largeHeap = self.smallHeap, self.largeHeap
        heapq.heappush(smallHeap, -num)
        if largeHeap and -smallHeap[0] > largeHeap[0]:
            val = heapq.heappop(smallHeap)
            heapq.heappush(largeHeap, -val)
        if len(smallHeap) > len(largeHeap) + 1:
            val = heapq.heappop(smallHeap)
            heapq.heappush(largeHeap, -val)
        if len(largeHeap) > len(smallHeap):
            val = heapq.heappop(largeHeap)
            heapq.heappush(smallHeap, -val)

    def findMedian(self) -> float:
        smallHeap, largeHeap = self.smallHeap, self.largeHeap
        if (len(smallHeap) + len(largeHeap)) % 2 == 0:
            return (-smallHeap[0] + largeHeap[0]) / 2
        return -smallHeap[0]
        