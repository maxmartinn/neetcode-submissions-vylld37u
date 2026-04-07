class Solution:
    def isValid(self, s: str) -> bool:
        # have a stk to keep track of opening parenthesis

        # have a parenMap that maps closing parenthesis to opening parenthis

        # iterate for each character see if its a open or close parenthiss

        # if closed then check if the matching open parenthsis is at top of tstk, if not then return false. then pop form stk
        # if open add to stk

        stk = [] # [( { {]

        parenMap = {")" : "(", "}" : "{", "]": "["}

        for c in s:
            if c in parenMap:
                if not stk or stk[-1] != parenMap[c]:
                    return False
                stk.pop()
            else:
                stk.append(c)
        return not stk



        """
        Input: s = "([{}])"

        stk = []

        Output: true

        """