class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        wordList = [0] * 26
        if len(t) != len(s):
            return False
        n = len(s)
        for i in range(n): 
            wordList[ord(s[i]) - ord('a')] += 1
            wordList[ord(t[i]) - ord('a')] -= 1
        for v in wordList:
            if v != 0:
                return False
        return True