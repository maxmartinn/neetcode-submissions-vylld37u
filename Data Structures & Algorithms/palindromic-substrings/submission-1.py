class Solution:
    def countSubstrings(self, s: str) -> int:
        # account for odd and even legnth index

        # start from center

        res = 0

        for i in range(len(s)):
            # odd
            l = i
            r = i
            while l != -1 and r != len(s) and s[l] == s[r]:
                res += 1
                l -= 1
                r += 1

            # even
            l = i
            r = i + 1
            while l != -1 and r != len(s) and s[l] == s[r]:
                res += 1
                l -= 1
                r += 1
        return res
            
