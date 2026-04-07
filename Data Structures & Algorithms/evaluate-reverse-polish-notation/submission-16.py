class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        # create a stk that contains computed numbers
        # every opperation pop the last 2 numbers and append the compute
        # return stk[-1]

        stk = []
        opSet = {'+', '-', '*', '/'}
        for token in tokens:
            if token not in opSet:
                stk.append(int(token))
            else:
                val1 = stk.pop()
                val2 = stk.pop()
                if token == '+':
                    stk.append(val1 + val2)
                elif token == '-':
                    stk.append(val2 - val1)
                elif token == '*':
                    stk.append(val1 * val2)
                elif token == '/':
                    stk.append(int(val2 / val1))
        return stk[-1]
