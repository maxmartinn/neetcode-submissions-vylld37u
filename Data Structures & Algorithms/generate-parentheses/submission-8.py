class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        def backtrack(s, openP, closeP):
            if openP < closeP or openP > n:
                return
            if openP == n and closeP == n:
                res.append("".join(s))
                return
            s.append("(")
            backtrack(s, openP + 1, closeP)
            s.pop()
            s.append(")")
            backtrack(s, openP, closeP + 1)
            s.pop()
        backtrack([], 0, 0)
        return res