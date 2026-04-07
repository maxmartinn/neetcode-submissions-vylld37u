class Solution:
    def isValid(self, s: str) -> bool:
        # have a stk containing the latest seen opening paranthesis
        # if the current char is a open par, add to stk
        # if the current char is a close par, check top of stack for matching open par
        
        stk = []

        matchingMap = {")" : "(", "}": "{" , "]" : "["}

        for char in s:
            if char not in matchingMap:
                stk.append(char)
            else:
                if not stk or stk[-1] != matchingMap[char]:
                    return False
                stk.pop()
        return False if stk else True