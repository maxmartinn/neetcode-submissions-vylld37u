class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        # recursively make paranthesis options by adding either an opening or closing parenthesis
        # have a running count of opening and closing
        # if they both equal 3 then check if its a valid paranthesis, add to stk

        res = []
        resCache = set()
        def dfs(openCount, closeCount, word):
            if openCount == n and closeCount == n and word not in resCache:
                stk = []
                for c in word:
                    if c == "(":
                        stk.append(c)
                    else:
                        if stk and stk[-1] == "(":
                            stk.pop()
                        else:
                            return
                res.append(word)
                resCache.add(word)
            if openCount > n or closeCount > n:
                return
            dfs(openCount + 1, closeCount, word + "(")
            dfs(openCount, closeCount + 1, word + ")")
        dfs(0, 0, "")
        return res

