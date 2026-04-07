class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        count = [0 for _ in range(26)]
        if len(s) != len(t):
            return False
        # first check if two lengths are equal

        # create an counter array that is able to increment place values based on index of alaphebet where a = 1 b = 2 ... z = 26

        # compare if two arrays are identical
        for i in range(len(s)):
            count[ord(s[i]) - ord('a')] += 1
            count[ord(t[i]) - ord('a')] -= 1
        
        for v in count:
            if v != 0:
                return False
        return True