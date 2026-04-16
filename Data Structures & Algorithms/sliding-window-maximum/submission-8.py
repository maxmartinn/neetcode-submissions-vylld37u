class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res = []
        maxHeap = []
        for i in range(len(nums)):
            heapq.heappush(maxHeap, (-nums[i], i))
            if i >= k -1:
                while i - k + 1 > maxHeap[0][1]:
                    heapq.heappop(maxHeap)
                res.append(-maxHeap[0][0])
        return res

        """

        Input: nums = [1,2,1,0,4,2,6], k = 3
        res = [2, 2, 4, 4]
        Output: [2,2,4,4,6]

        maxHeap = [(-6, 4), (-4, 4), (-2, 1), (-2, 4) (-1, 0), (-1, 0), (0, 2)]

        Explanation:
        Window position            Max
        ---------------           -----
        [1  2  1] 0  4  2  6        2
        1 [2  1  0] 4  2  6        2
        1  2 [1  0  4] 2  6        4
        1  2  1 [0  4  2] 6        4
        1  2  1  0 [4  2  6]       6

        """

        # naive solution

        # using a heap store ((-) value, index)

        # add first k - 1 values to the heap

        # start from index k - 1:

        # add to heap
        # try to get maximum untill the current value is inside i - k + 1 <= index <= i
    