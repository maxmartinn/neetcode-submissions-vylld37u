class Solution:
    def longestPalindrome(self, s: str) -> str:
        # consider both even and odd longest palindromic substring
        # aba abba 

        # iterate for all starting center points:
            # iterate untill either l or r is out of bounds
                # start at both l and r or l and r + 1
        
        res = ""

        for i in range(len(s)):
            # odd length
            l = i
            r = i
            while l != -1 and r != len(s) and s[l] == s[r]:
                substr = s[l:r+1]
                res = substr if len(substr) >= len(res)  else res
                l -= 1
                r += 1
            # even length
            l = i
            r = i + 1
            while l != -1 and r != len(s) and s[l] == s[r]:
                substr = s[l:r+1]
                res = substr if len(substr) >= len(res)  else res
                l -= 1
                r += 1
        return res
