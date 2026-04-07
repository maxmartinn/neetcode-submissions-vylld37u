class Solution:
    def evalRPN(self, tokens: List[str]) -> int:

        """
        Input: tokens = ["1","2","+","3","*","4","-"]

        Output: 5


        stk = [1, 2] 
        val1 = stk.pop() 2
        val2 = stk.pop() 1
        """

        # using a stk add value then whenever an operaotr is found preform that operation

        stk = []

        for op in tokens:
            if op not in "+-/*":
                stk.append(op)
                continue
            val1 = int(stk.pop())
            val2 = int(stk.pop())
            
            if op == "+":
                stk.append(val2 + val1)
            elif op == "-":
                stk.append(val2 - val1)
            elif op == "/":
                stk.append(val2 / val1)
            elif op == "*":
                stk.append(val2 * val1)
        return int(stk[0])
        """
        stk = [9 4]
        val1 = 4
        val2 = 9
        """



            