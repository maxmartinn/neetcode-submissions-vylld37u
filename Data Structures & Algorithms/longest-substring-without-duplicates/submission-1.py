class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        cache = set()
        l = 0
        r = 0
        maxLength = 0
        while r < len(s):
            # check if r is in cache:
            # if r is in cache remove l from cache and increment r
            while s[r] in cache:
                cache.remove(s[l])
                l = l + 1
            maxLength = max(r - l + 1, maxLength)
            cache.add(s[r])
            r += 1
        return maxLength

