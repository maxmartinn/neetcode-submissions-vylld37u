class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # array of integers stones

        # stones[i] repersents the weight of the ith stone

        # simulaiton:
            # choose two heaviest stones
            # if x == y destroy both stones
            # if x < y x is destroyed and y is equal to y - x

        # algo

        # have a maxHeap that is able to get the two largest stones in O(1) time

        # simulate comparison then add the remainder stone to the heap

        # iterate while the length of the max heap is greater than one
        stones = [-s for s in stones]
        heapq.heapify(stones)

        while len(stones) > 1:
            y = -1 * heapq.heappop(stones)
            x = -1 * heapq.heappop(stones)

            if y > x:
                heapq.heappush(stones, x - y)
        stones.append(0)
        return abs(stones[0])