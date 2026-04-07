class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # have a window of all characters in the current window
        # while the length of window - maxFreq > k
        # maxFreq is the max of the widnow
        l = 0
        window = dict()
        maxF = 0
        for r in range(len(s)):
            window[s[r]] = window.get(s[r], 0) + 1
            maxF = max(maxF, window[s[r]])
            if r - l + 1 - maxF > k:
                window[s[l]] -= 1
                l += 1
            
            
           
        return r - l + 1
