class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(t) != len(s):
            return False
        wordList = [0] * 26
        for i in range(len(s)): 
            wordList[ord(s[i]) - ord('a')] += 1
            wordList[ord(t[i]) - ord('a')] -= 1
        for v in wordList:
            if v != 0:
                return False
        return True