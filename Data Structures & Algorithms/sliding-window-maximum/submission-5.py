class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # window of size k, return max element

        # check if window size is size k

        # put value into heap (val, index), check if index is within window

        l = 0 # 0
        r = 0 # 0
        # [(-1, 0), (-1, 2), (0, 3), (4, 4)]
        # res = [2, 2]
        #
        #
        #

        maxHeap = [] # (val, index)
        # [2]
        res = []
        for r in range(len(nums)):
            heapq.heappush(maxHeap, (nums[r] * -1, r))
            while maxHeap[0][1] + k <= r: # clean heap if boundry is out of bounds
                heapq.heappop(maxHeap)
            if r - l + 1 == k:
                val = maxHeap[0][0] * -1
                res.append(val)
                l += 1
            print(maxHeap)
        return res
            
