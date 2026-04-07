class Solution:
    def isValid(self, s: str) -> bool:
        stk = [] # have stks contain opening parenthesis and when corresponding closing parenthesis exists then pop

        parenMap = {"(" : ")", "{" : "}", "[": "]"}

        for c in s:
            if c in parenMap:
                stk.append(c)
            else:
                if stk and parenMap[stk[-1]] == c:
                    stk.pop()
                else:
                    return False
        return len(stk) == 0

        """
        Input: s = "([{}])"

        stk = []

        Output: true

        """