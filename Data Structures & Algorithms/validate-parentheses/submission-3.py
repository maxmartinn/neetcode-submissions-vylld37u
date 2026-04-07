class Solution:
    def isValid(self, s: str) -> bool:
        # have a stk containing the latest seen opening paranthesis
        # if the current char is a open par, add to stk
        # if the current char is a close par, check top of stack for matching open par
        
        stk = []

        matchingMap = {")" : "(", "}": "{" , "]" : "["}

        for char in s:
            if char in matchingMap:
                if stk and stk[-1] == matchingMap[char]:
                     stk.pop()
                else:
                    return False
            else:
                stk.append(char)
               
        return True if not stk else False