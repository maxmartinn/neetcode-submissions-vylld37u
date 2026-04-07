class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res = deque()
        cache = set()
        output = 0
        for c in s:
            while c in cache:
                val = res.popleft()
                cache.remove(val)
            cache.add(c)
            res.append(c)
            output = max(len(res), output)
        return output
