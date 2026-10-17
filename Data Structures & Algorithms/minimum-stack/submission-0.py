class MinStack:
    # Value	Minimum so far	Stored pair
    #     5	5	(5, 5)
    #     3	3	(3, 3)
    #     7	3	(7, 3)
    #     2	2	(2, 2)
    
    def __init__(self):
        self.stack = []        

    def push(self, val: int) -> None:
        minm = min(val, self.stack[-1][1]) if self.stack else val
        self.stack.append((val, minm))

    def pop(self) -> None:
        self.stack.pop()
        
    def top(self) -> int:
        return self.stack[-1][0]
        

    def getMin(self) -> int:
        return self.stack[-1][1]
