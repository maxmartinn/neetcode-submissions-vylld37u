class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        openCount, closeCount = n, n
        def helper(openCount, closeCount, w):
            if openCount == 0 and closeCount == 0:
                stk = []
                for token in w:
                    if token == ')':
                        if stk and stk[-1] == '(':
                            stk.pop()
                        else:
                            return
                    else:
                        stk.append('(')
                res.append(w)
            if openCount < 0 or closeCount < 0:
                return
            helper(openCount - 1, closeCount, w + '(')
            helper(openCount, closeCount - 1, w + ')')
            
        helper(openCount, closeCount, "")
        return res
