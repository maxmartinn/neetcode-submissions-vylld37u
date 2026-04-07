class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        # create a stk that contains computed numbers
        # every opperation pop the last 2 numbers and append the compute
        # return stk[-1]

        stk = []
        opSet = {'+', '-', '*', '/'}
        for token in tokens:
                if token == '+':
                    val1 = stk.pop()
                    val2 = stk.pop()
                    stk.append(val1 + val2)
                elif token == '-':
                    val1 = stk.pop()
                    val2 = stk.pop()
                    stk.append(val2 - val1)
                elif token == '*':
                    val1 = stk.pop()
                    val2 = stk.pop()
                    stk.append(val1 * val2)
                elif token == '/':
                    val1 = stk.pop()
                    val2 = stk.pop()
                    stk.append(int(val2 / val1))
                else:
                    stk.append(int(token))
        return stk[-1]
