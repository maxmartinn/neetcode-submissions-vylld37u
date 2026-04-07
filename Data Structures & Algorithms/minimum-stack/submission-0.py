class MinStack:

    def __init__(self):
        self.stk = []
        self.minStk = []

    def push(self, val: int) -> None:
        self.stk.append(val)
        if self.minStk:
            if self.minStk[-1] >= val:
                self.minStk.append(val)
        else:
            self.minStk.append(val)


    def pop(self) -> None:
        popped = self.stk.pop()
        if popped == self.minStk[-1]:
            self.minStk.pop()

    def top(self) -> int:
        return self.stk[-1]

    def getMin(self) -> int:
        return self.minStk[-1]
