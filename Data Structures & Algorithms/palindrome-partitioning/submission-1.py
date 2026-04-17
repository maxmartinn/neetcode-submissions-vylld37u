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
        def backtrack(i, start, curr):
            if i == len(s):
                if start == len(s):
                    res.append(curr[:])
                return
            if isPalindrome(s[start:i+1]):
                curr.append(s[start:i+1])
                backtrack(i + 1, i+1, curr)
                curr.pop()
            backtrack(i + 1, start, curr)

        backtrack(0, 0, [])
        return res

