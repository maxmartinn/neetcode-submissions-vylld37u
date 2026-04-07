class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # have a cache consisting of all the characters in the window
        # have a value containing the max freq of repeating characters
        # slide the windows based upon requirements
        # windowSize - maxFreq < k
        cache = {}
        l, r = 0, 0
        maxFreq = 0
        res = 0
        while r < len(s):
            cache[s[r]] = cache.get(s[r], 0) + 1
            maxFreq = max(cache[s[r]], maxFreq)

            while r - l + 1 - maxFreq > k:
                cache[s[l]] -= 1
                l += 1
            res = max(res, r - l + 1)
            r += 1
        return res
            


