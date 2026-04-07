class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # have a window of all characters in the current window
        # while the length of window - maxFreq > k
        # maxFreq is the max of the widnow
        l = 0
        res = 0
        window = dict()
        for r in range(len(s)):
            window[s[r]] = window.get(s[r], 0) + 1
            while window and (r - l + 1 - max(window.values()) > k):
                window[s[l]] -= 1
                l += 1
            
            res = max(r - l + 1, res)
        return res
