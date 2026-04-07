class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        wordDict = defaultdict(int) 
        if len(s) != len(t):
            return False
        n = len(s)
        for i in range(n):
            wordDict[s[i]] += 1
        for i in range(n):
            wordDict[t[i]] -= 1
            if wordDict[t[i]] == 0:
                del wordDict[t[i]]
        return len(wordDict) == 0
