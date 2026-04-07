class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        res = 0
        l = 1
        r = max(piles)
        while l <= r:
            speed = (l + r) // 2
            totalHours = 0
            for pile in piles:
                hoursTaken = float(pile / speed)
                totalHours += math.ceil(hoursTaken)
            if totalHours <= h:
                r = speed - 1
                res = speed
            else:
                l = speed + 1
        return res
                    
