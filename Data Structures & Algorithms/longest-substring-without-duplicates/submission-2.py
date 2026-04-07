class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        cache = set()
        l = 0
        r = 0
        res = 0
        while r < len(s):
            while s[r] in cache:
                cache.remove(s[l])
                l += 1
            cache.add(s[r])
            res = max(r - l + 1, res)
            r += 1
        return res
            
