class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        if len(stones) == 1:
            return stones[0]
        negativeStones = [-stone for stone in stones]
        heapq.heapify(negativeStones)

        while len(negativeStones) > 1:
            stone1 = -heapq.heappop(negativeStones) 
            stone2 = -heapq.heappop(negativeStones)
            print(stone1 - stone2)
            if stone1 - stone2:
                heapq.heappush(negativeStones, stone2 - stone1)

        return -negativeStones[0] if negativeStones else 0