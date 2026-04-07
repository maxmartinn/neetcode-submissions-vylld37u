"""

push, pop, top just like a regular stk

some how always retireve them inimum element of a stk

# stk = [1, 2, 3, -1]
# minStk = [1, -1]

# initalize stk and minStk
# add to minStk whenever a new minimum is found on push()
# pop from minStk if the top of the stk and minStk are equal on pop()
# get top from stk if top
# get top from minStk if getMin

"""

class MinStack:

    def __init__(self):
        self.stk = [] # [1, 2, 3, -1]
        self.minStk = [] # [1, -1]

    def push(self, val: int) -> None:
        self.stk.append(val)
        if not self.minStk or val <= self.minStk[-1]:
            self.minStk.append(val)

    def pop(self) -> None:
        if self.minStk[-1] == self.stk[-1]:
            self.minStk.pop()
        self.stk.pop()

    def top(self) -> int:
        return self.stk[-1]

    def getMin(self) -> int:
        return self.minStk[-1]

    """

    Input: ["MinStack", "push", 1, "push", 2, "push", 0, "getMin", "pop", "top", "getMin"]

Output: [null,null,null,null,0,null,2,1]

Explanation:
MinStack minStack = new MinStack();
minStack.push(1);
minStack.push(2);
minStack.push(0);
minStack.getMin(); // return 0
minStack.pop();
minStack.top();    // return 2
minStack.getMin(); // return 1


    stk = [1, 2]
    minStk = [1]
"""