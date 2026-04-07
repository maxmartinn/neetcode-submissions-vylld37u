class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        # have a minHeap of size k
        # k = 3
        # [4, 5, 6] 
        heapq.heapify(nums)
        self.nums = nums
        self.k = k

    def add(self, val: int) -> int:
        heapq.heappush(self.nums, val)

        while len(self.nums) > self.k:
            heapq.heappop(self.nums)
        return self.nums[0]
        
