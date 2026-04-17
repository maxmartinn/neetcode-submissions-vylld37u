class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        def isPalindrome(w):
            n = len(w)
            for i in range(n // 2):
                if w[i] != w[n - 1 - i]:
                    return False
            return True
        res = []
        def backtrack(i, curr):
            if i == len(s):
                res.append(curr[:])
                return
            for j in range(i, len(s)):
                w = s[i:j + 1]
                if isPalindrome(w):
                    curr.append(w)
                    backtrack(j + 1, curr)
                    curr.pop()
        backtrack(0, [])
        return res

