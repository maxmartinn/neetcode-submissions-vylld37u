class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hashmapS = dict()
        hashmapT = dict()
        if len(s) == len(t):
            for i in range(len(s)):
                hashmapS[s[i]] = 1 + hashmapS.get(s[i], 0)
                hashmapT[t[i]] = 1 + hashmapT.get(t[i], 0)
        else:
            return False
        return hashmapS == hashmapT

