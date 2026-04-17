class Solution:
    def isValid(self, s: str) -> bool:
        # is input always of type size
        # how large is the string
        # can string be None
        # can string be empty
        # does string always contain only characters of '(', ')', '{', '}', '[' and ']'.

        # assumptions:

            # 1 <= s <= 10^2
            # s cant be none
            # s is always type string
            # string cant be empty
            # valid means that there is no open or closed parenthesis inside of a larger opening paranthesis
            # for example: ([]) is valid. ([) is not.
        parenMap = {"}" : "{", ")": "(", "]" : "["}

        stk = []

        for c in s:
            if c in parenMap:
                if stk and stk[-1] == parenMap[c]:
                    stk.pop()
                else:
                    return False
            else:
                stk.append(c)
        return False if stk else True

        "[{]"

        # stk = [[, {]