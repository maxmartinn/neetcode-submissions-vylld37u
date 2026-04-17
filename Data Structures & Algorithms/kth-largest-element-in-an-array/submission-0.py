class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        minHeap = [] # make of size k

        for n in nums:
            heapq.heappush(minHeap, n)
            if len(minHeap) > k:
                heapq.heappop(minHeap)
        return minHeap[0]