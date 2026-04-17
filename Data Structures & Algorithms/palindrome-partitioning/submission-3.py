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
            for j in range(i + 1, len(s) + 1):
                w = s[i:j]
                if isPalindrome(w):
                    curr.append(w)
                    backtrack(j, curr)
                    curr.pop()
        backtrack(0, [])
        return res

