class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stk = []
        opSet = {'+', '-', '*', '/'}
        for token in tokens:
            if token not in opSet:
                stk.append(int(token))
            else:
                a = stk.pop() 
                b = stk.pop()
                if token == '+':
                    stk.append(a + b)
                if token == '-':
                    stk.append(b - a)
                if token == '*':
                    stk.append(a * b)
                if token == '/':
                    stk.append(int(b / a))
        return stk[-1]