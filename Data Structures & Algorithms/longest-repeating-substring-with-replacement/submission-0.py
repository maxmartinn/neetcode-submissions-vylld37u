class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # res = 5
        # {A: 2, B: 3}
        # maxOfCache = "B"
        # length of cache - maxCache <= k

        # how do you know the max of Cache?
        # Hold maxOfCache as a string, if the element just added to the window
        # is greater than one just added, change maxOfCache
        # length of cache - maxCache <= k
        l = 0
        r = 0
        res = 0
        maxf = 0
        cache = {}
        # "{A: 1, B: 2, C: 1}"
        while r < len(s):
            cache[s[r]] = cache.get(s[r], 0) + 1
            maxf = max(cache.get(s[r], 0), maxf)
            
            while r - l + 1 - maxf > k:
                cache[s[l]] -= 1
                l += 1
            res = max(res, r - l + 1)
            r += 1
        return res
            


