class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res = 0
        for i in range(len(s)):
            cache = set()
            noDups = True
            for j in range(i, len(s)):
                if s[j] in cache:
                    noDups = False
                    res = max(res, len(cache))
                    break
                cache.add(s[j])
            if noDups:
                res = max(res, len(cache))
        return res
