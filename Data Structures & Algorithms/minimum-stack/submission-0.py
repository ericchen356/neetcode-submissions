import math 

class MinStack:

    def __init__(self):
        self.stack = [] # (value, minimum so far at that level)
        
    def push(self, val: int) -> None:

        if self.stack: 
            minimum = min(val, self.stack[-1][1])
        else: 
            minimum = val
        self.stack.append((val, minimum))

    def pop(self) -> None:
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1][0]

    def getMin(self) -> int:
        return self.stack[-1][1]