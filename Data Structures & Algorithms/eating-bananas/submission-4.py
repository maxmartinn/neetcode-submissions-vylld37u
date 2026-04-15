class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        # minimum speed of eating bananas within h hours

        """


        Input: piles = [1,4,3,2], h = 9

        [False False True True True True True True True]

        Output: 2

        """

        l = 1
        r = max(piles)
        res = float("inf")
        while l <= r:
            speed = (l + r) // 2
            hoursTaken = 0
            for p in piles:
                hoursTaken += math.ceil(p / speed)
            if hoursTaken > h:
                l = speed + 1
            else:
                r = speed - 1
                res = min(res, speed)
        return res if res != float("inf") else -1