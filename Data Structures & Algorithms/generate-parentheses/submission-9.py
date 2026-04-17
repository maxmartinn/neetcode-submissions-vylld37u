class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        # a parenthesis can only be closed if there are more opening parenthesis before  it
        res = []
        def backtrack(op, cl, curr):
            if op == cl == n:
                res.append("".join(curr))
                return
            if cl > op or op > n:
                return
            curr.append("(")
            backtrack(op + 1, cl, curr)
            curr.pop()
            curr.append(")")
            backtrack(op, cl + 1, curr)
            curr.pop()
        backtrack(0, 0, [])
        return res