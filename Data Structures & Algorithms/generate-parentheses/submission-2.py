class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        # break if close is greater than openCount
        # add if open < n
        # append if open == close == n

        stk = []
        res = []

        def helper(openCount, closeCount):
            if openCount == closeCount == n:
                res.append("".join(stk))
                return
            if openCount < n:
                stk.append('(')
                helper(openCount + 1, closeCount)
                stk.pop()
            if closeCount < openCount:
                stk.append(')')
                helper(openCount, closeCount + 1)
                stk.pop()

        helper(0,0)
        return res


